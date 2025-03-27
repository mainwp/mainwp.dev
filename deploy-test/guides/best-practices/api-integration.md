# API Integration Best Practices for MainWP Add-ons

This guide covers best practices for integrating third-party APIs with MainWP add-ons. Following these practices will help you create reliable, secure, and maintainable integrations.

## Real-World MainWP Example: Google Analytics Integration

Here's a concrete example of integrating Google Analytics with MainWP to track website performance across all managed sites:

```php
class MainWP_Google_Analytics_Integration {
    private $api_client;
    private $view_id;
    
    public function __construct() {
        // Initialize Google Analytics API client
        $this->api_client = new Google_Analytics_API_Client(
            get_option('mainwp_ga_client_id'),
            get_option('mainwp_ga_client_secret')
        );
        
        // Set default view ID
        $this->view_id = get_option('mainwp_ga_view_id');
        
        // Hook into MainWP actions
        add_action('mainwp_site_synced', [$this, 'sync_analytics_data'], 10, 2);
        add_filter('mainwp_sync_others_data', [$this, 'add_analytics_data_to_sync'], 10, 2);
        
        // Add dashboard widget
        add_action('mainwp_dashboard_widgets', [$this, 'add_analytics_widget']);
    }
    
    /**
     * Sync analytics data when a site is synced
     */
    public function sync_analytics_data($website, $data) {
        // Skip if API client isn't configured
        if (!$this->api_client->is_configured()) {
            return;
        }
        
        try {
            // Get analytics data for this site
            $analytics_data = $this->api_client->get_site_analytics(
                $website->url,
                date('Y-m-d', strtotime('-30 days')),
                date('Y-m-d'),
                $this->view_id
            );
            
            // Store analytics data for this site
            update_option('mainwp_ga_data_' . $website->id, $analytics_data);
            update_option('mainwp_ga_last_sync_' . $website->id, time());
            
        } catch (Exception $e) {
            // Log error but continue
            error_log('Google Analytics API Error: ' . $e->getMessage());
        }
    }
    
    /**
     * Add analytics data to sync data
     */
    public function add_analytics_data_to_sync($sync_data, $website) {
        $sync_data['google_analytics'] = [
            'last_sync' => get_option('mainwp_ga_last_sync_' . $website->id, 0),
            'has_data' => !empty(get_option('mainwp_ga_data_' . $website->id, []))
        ];
        
        return $sync_data;
    }
    
    /**
     * Add analytics widget to dashboard
     */
    public function add_analytics_widget() {
        wp_add_dashboard_widget(
            'mainwp-google-analytics-widget',
            'Google Analytics Overview',
            [$this, 'render_analytics_widget']
        );
    }
    
    /**
     * Render analytics widget
     */
    public function render_analytics_widget() {
        // Get all websites
        $websites = MainWP\Dashboard\MainWP_DB::instance()->get_websites();
        
        // Collect analytics data
        $total_sessions = 0;
        $total_users = 0;
        $total_pageviews = 0;
        
        foreach ($websites as $website) {
            $analytics_data = get_option('mainwp_ga_data_' . $website->id, []);
            
            if (!empty($analytics_data)) {
                $total_sessions += $analytics_data['sessions'] ?? 0;
                $total_users += $analytics_data['users'] ?? 0;
                $total_pageviews += $analytics_data['pageviews'] ?? 0;
            }
        }
        
        // Display analytics data
        ?>
        <div class="ui grid">
            <div class="four wide column">
                <div class="ui statistic">
                    <div class="value"><?php echo number_format($total_sessions); ?></div>
                    <div class="label">Sessions</div>
                </div>
            </div>
            <div class="four wide column">
                <div class="ui statistic">
                    <div class="value"><?php echo number_format($total_users); ?></div>
                    <div class="label">Users</div>
                </div>
            </div>
            <div class="four wide column">
                <div class="ui statistic">
                    <div class="value"><?php echo number_format($total_pageviews); ?></div>
                    <div class="label">Pageviews</div>
                </div>
            </div>
        </div>
        <?php
    }
}
```

This example demonstrates:
1. **Hooking into MainWP events** - Using `mainwp_site_synced` to trigger data collection
2. **Extending sync data** - Adding custom data to the sync process
3. **Dashboard integration** - Displaying aggregated analytics data in the MainWP dashboard
4. **Error handling** - Gracefully handling API errors without disrupting MainWP
5. **Data storage** - Storing API data per website using WordPress options

## Common Pitfalls When Integrating APIs with MainWP

Avoid these common mistakes when building your MainWP API integration:

### 1. Blocking the Main Thread with Synchronous API Calls

**Problem**: Making synchronous API calls during critical MainWP operations can cause timeouts and a poor user experience.

**Solution**: Use asynchronous processing for non-critical operations:

```php
// Instead of this:
function on_site_sync($website_id) {
    $this->api_client->sync_data($website_id); // Blocks until complete
}

// Do this:
function on_site_sync($website_id) {
    wp_schedule_single_event(
        time(),
        'my_integration_async_sync',
        [$website_id]
    );
}

// Then handle it asynchronously:
add_action('my_integration_async_sync', [$this, 'process_async_sync']);
```

### 2. Not Respecting API Rate Limits

**Problem**: MainWP manages multiple sites, and your integration might trigger many API calls at once, quickly hitting rate limits.

**Solution**: Implement rate limiting and queuing:

```php
// Track API calls with timestamps
private function track_api_call() {
    $calls = get_option('my_integration_api_calls', []);
    $calls[] = time();
    
    // Keep only the last 100 calls
    $calls = array_slice($calls, -100);
    update_option('my_integration_api_calls', $calls);
}

// Check if we're within rate limits
private function can_make_api_call() {
    $calls = get_option('my_integration_api_calls', []);
    $recent_calls = array_filter($calls, function($time) {
        return $time > time() - 60; // Last minute
    });
    
    return count($recent_calls) < 60; // 60 calls per minute limit
}
```

### 3. Storing API Credentials Insecurely

**Problem**: Storing API keys and secrets in plain text makes them vulnerable to exposure.

**Solution**: Always encrypt sensitive credentials:

```php
// Encrypt API secret before storing
private function save_api_secret($secret) {
    $encrypted = $this->encrypt($secret);
    update_option('my_integration_api_secret', $encrypted);
}

// Decrypt when needed
private function get_api_secret() {
    $encrypted = get_option('my_integration_api_secret', '');
    return $this->decrypt($encrypted);
}
```

### 4. Not Handling MainWP Child Site Disconnections

**Problem**: If a site is removed from MainWP, your integration might continue trying to sync data for it.

**Solution**: Hook into the site deletion event:

```php
// Clean up when a site is removed from MainWP
add_action('mainwp_site_deleted', function($website_id) {
    // Delete site-specific data
    delete_option('my_integration_data_' . $website_id);
    delete_option('my_integration_last_sync_' . $website_id);
    
    // If needed, notify the third-party service
    try {
        $this->api_client->remove_site($website_id);
    } catch (Exception $e) {
        error_log('Failed to remove site from service: ' . $e->getMessage());
    }
});
```

### 5. Ignoring Error States in the UI

**Problem**: When API errors occur, users are left in the dark about what went wrong.

**Solution**: Provide clear error states and recovery options in your UI:

```php
// Store API connection state
public function check_api_connection() {
    try {
        $result = $this->api_client->test_connection();
        update_option('my_integration_connection_status', 'connected');
        return true;
    } catch (Exception $e) {
        update_option('my_integration_connection_status', 'error');
        update_option('my_integration_connection_error', $e->getMessage());
        return false;
    }
}

// Display connection status in admin UI
public function render_connection_status() {
    $status = get_option('my_integration_connection_status', '');
    
    if ($status === 'connected') {
        echo '<div class="ui green message">Connected to API</div>';
    } else if ($status === 'error') {
        $error = get_option('my_integration_connection_error', 'Unknown error');
        echo '<div class="ui red message">API Connection Error: ' . esc_html($error) . '</div>';
        echo '<button class="ui button" id="reconnect-api">Reconnect</button>';
    } else {
        echo '<div class="ui yellow message">Not connected to API</div>';
    }
}
```

## Quick Start for Experienced Developers

```php
// 1. Secure credential storage
class ApiCredentialManager {
    public static function save_credentials($api_key, $api_secret) {
        // Never store credentials in plain text
        update_option('my_integration_api_key', $api_key);
        update_option('my_integration_api_secret', self::encrypt($api_secret));
    }
    
    private static function encrypt($data) {
        if (!defined('AUTH_KEY')) return $data; // Fallback if AUTH_KEY not defined
        $iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length('aes-256-cbc'));
        $encrypted = openssl_encrypt($data, 'aes-256-cbc', AUTH_KEY, 0, $iv);
        return base64_encode($iv . $encrypted);
    }
}

// 2. Implement caching for performance
function get_api_data($endpoint, $params = []) {
    $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
    $cached = get_transient($cache_key);
    
    if (false !== $cached) {
        return $cached; // Return cached data if available
    }
    
    // Get fresh data from API
    $data = $api_client->get($endpoint, $params);
    
    // Cache for 5 minutes (adjust based on data volatility)
    set_transient($cache_key, $data, 5 * MINUTE_IN_SECONDS);
    
    return $data;
}

// 3. Implement graceful error handling
try {
    $data = $api_client->get('endpoint');
    // Process data
} catch (ApiRateLimitException $e) {
    // Log rate limit error and schedule retry
    error_log('Rate limit exceeded: ' . $e->getMessage());
    wp_schedule_single_event(time() + $e->getRetryAfter(), 'my_integration_retry_api_call', [$endpoint, $params]);
    // Show user-friendly message
    return ['error' => 'Service temporarily unavailable. Retry scheduled.'];
} catch (ApiException $e) {
    // Log error and show user-friendly message
    error_log('API Error: ' . $e->getMessage());
    return ['error' => 'Unable to connect to service. Please try again later.'];
}

// 4. Implement proper logging
function log_api_activity($action, $status, $message = '') {
    $logs = get_option('my_integration_logs', []);
    $logs[] = [
        'time' => current_time('mysql'),
        'action' => $action,
        'status' => $status,
        'message' => $message
    ];
    // Keep only the last 100 logs
    $logs = array_slice($logs, -100);
    update_option('my_integration_logs', $logs);
}
```

## Security Considerations

Security should be your top priority when integrating with third-party APIs. Here are key practices to follow:

### Secure Storage of API Credentials

Never store API keys, tokens, or secrets in plain text:

```php
/**
 * Save API credentials securely
 *
 * @param string $api_key API key
 * @param string $api_secret API secret
 * @return bool Whether the credentials were saved
 */
public function save_credentials($api_key, $api_secret) {
    // Validate credentials
    if (empty($api_key) || empty($api_secret)) {
        return false;
    }
    
    // Save API key
    update_option('my_integration_api_key', $api_key);
    
    // Encrypt and save API secret
    $encrypted_secret = $this->encrypt_secret($api_secret);
    update_option('my_integration_api_secret', $encrypted_secret);
    
    return true;
}

/**
 * Encrypt sensitive data
 *
 * @param string $data Data to encrypt
 * @return string Encrypted data
 */
private function encrypt_secret($data) {
    // Use WordPress AUTH_KEY as encryption key
    $key = defined('AUTH_KEY') ? AUTH_KEY : 'default-key';
    
    // Generate random initialization vector
    $iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length('aes-256-cbc'));
    
    // Encrypt data
    $encrypted = openssl_encrypt($data, 'aes-256-cbc', $key, 0, $iv);
    
    // Combine IV and encrypted data
    return base64_encode($iv . $encrypted);
}

/**
 * Decrypt sensitive data
 *
 * @param string $encrypted_data Encrypted data
 * @return string Decrypted data
 */
private function decrypt_secret($encrypted_data) {
    // Use WordPress AUTH_KEY as encryption key
    $key = defined('AUTH_KEY') ? AUTH_KEY : 'default-key';
    
    // Decode combined data
    $combined = base64_decode($encrypted_data);
    
    // Extract IV and encrypted data
    $iv_length = openssl_cipher_iv_length('aes-256-cbc');
    $iv = substr($combined, 0, $iv_length);
    $encrypted = substr($combined, $iv_length);
    
    // Decrypt data
    return openssl_decrypt($encrypted, 'aes-256-cbc', $key, 0, $iv);
}
```

### Use HTTPS for All API Communication

Always use HTTPS for API communication to prevent man-in-the-middle attacks:

```php
/**
 * Ensure API URL uses HTTPS
 *
 * @param string $url API URL
 * @return string Secure API URL
 */
private function ensure_https($url) {
    if (strpos($url, 'http://') === 0) {
        $url = 'https://' . substr($url, 7);
    }
    
    return $url;
}
```

### Implement Proper Authentication

Use the most secure authentication method available:

1. **OAuth 2.0**: Preferred for most APIs
2. **API Keys with HMAC**: Good for server-to-server communication
3. **JWT**: Good for stateless authentication
4. **Basic Auth**: Only use with HTTPS and when no better option is available

### Validate and Sanitize All Input

Always validate and sanitize input before sending it to the API:

```php
/**
 * Validate API parameters
 *
 * @param array $params API parameters
 * @param array $allowed_params Allowed parameters and their types
 * @return array Validated parameters
 */
private function validate_params($params, $allowed_params) {
    $validated = [];
    
    foreach ($params as $key => $value) {
        // Check if parameter is allowed
        if (!isset($allowed_params[$key])) {
            continue;
        }
        
        // Validate parameter type
        $type = $allowed_params[$key];
        switch ($type) {
            case 'string':
                $validated[$key] = sanitize_text_field($value);
                break;
            
            case 'int':
                $validated[$key] = (int)$value;
                break;
            
            case 'float':
                $validated[$key] = (float)$value;
                break;
            
            case 'bool':
                $validated[$key] = (bool)$value;
                break;
            
            case 'array':
                $validated[$key] = is_array($value) ? $value : [];
                break;
            
            default:
                $validated[$key] = $value;
                break;
        }
    }
    
    return $validated;
}
```

### Implement Rate Limit Protection

Protect your integration from abuse with rate limiting:

```php
/**
 * Check if rate limit is exceeded
 *
 * @param string $action Action name
 * @param int $limit Rate limit
 * @param int $period Period in seconds
 * @return bool Whether rate limit is exceeded
 */
public function is_rate_limited($action, $limit = 10, $period = 60) {
    // Get current user ID
    $user_id = get_current_user_id();
    if (!$user_id) {
        return false;
    }
    
    // Get rate limit data
    $rate_limits = get_user_meta($user_id, 'my_integration_rate_limits', true);
    if (!is_array($rate_limits)) {
        $rate_limits = [];
    }
    
    // Get action data
    $action_data = $rate_limits[$action] ?? [
        'count' => 0,
        'reset' => time() + $period
    ];
    
    // Check if period has expired
    if (time() > $action_data['reset']) {
        // Reset count and period
        $action_data = [
            'count' => 1,
            'reset' => time() + $period
        ];
        
        // Save rate limit data
        $rate_limits[$action] = $action_data;
        update_user_meta($user_id, 'my_integration_rate_limits', $rate_limits);
        
        return false;
    }
    
    // Check if limit is exceeded
    if ($action_data['count'] >= $limit) {
        return true;
    }
    
    // Increment count
    $action_data['count']++;
    
    // Save rate limit data
    $rate_limits[$action] = $action_data;
    update_user_meta($user_id, 'my_integration_rate_limits', $rate_limits);
    
    return false;
}
```

### Secure Webhook Handling

If your integration uses webhooks, implement proper security:

```php
/**
 * Verify webhook signature
 *
 * @param string $payload Webhook payload
 * @param string $signature Webhook signature
 * @return bool Whether the signature is valid
 */
public function verify_webhook_signature($payload, $signature) {
    // Get webhook secret
    $secret = get_option('my_integration_webhook_secret', '');
    if (empty($secret)) {
        return false;
    }
    
    // Calculate expected signature
    $expected_signature = hash_hmac('sha256', $payload, $secret);
    
    // Compare signatures
    return hash_equals($expected_signature, $signature);
}
```

## Performance Optimization

Optimize your integration for performance to provide a better user experience:

### Implement Caching

Cache API responses to reduce API calls and improve performance:

```php
/**
 * Get data with caching
 *
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param int $cache_time Cache time in seconds
 * @return array Response data
 */
public function get_cached($endpoint, $params = [], $cache_time = 300) {
    $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
    
    // Check cache
    $cached = get_transient($cache_key);
    if (false !== $cached) {
        return $cached;
    }
    
    // Get fresh data
    $data = $this->api_client->get($endpoint, $params);
    
    // Cache the data
    set_transient($cache_key, $data, $cache_time);
    
    return $data;
}
```

### Implement Batch Processing

Combine multiple API calls into a single batch request when possible:

```php
/**
 * Process batch of API requests
 *
 * @param array $requests Array of request data
 * @return array Response data
 */
public function batch_process($requests) {
    // Check if API supports batch processing
    if (!$this->api_client->supports_batch()) {
        // Process requests individually
        $responses = [];
        foreach ($requests as $key => $request) {
            $responses[$key] = $this->api_client->request(
                $request['method'],
                $request['endpoint'],
                $request['params'] ?? [],
                $request['data'] ?? null
            );
        }
        return $responses;
    }
    
    // Process requests in a batch
    return $this->api_client->batch($requests);
}
```

### Implement Asynchronous Processing

Use WordPress cron for asynchronous processing of non-critical tasks:

```php
/**
 * Schedule asynchronous API call
 *
 * @param string $method HTTP method
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param array $data Request data
 */
public function schedule_api_call($method, $endpoint, $params = [], $data = null) {
    wp_schedule_single_event(
        time(),
        'my_integration_api_call',
        [$method, $endpoint, $params, $data]
    );
}

/**
 * Process scheduled API call
 *
 * @param string $method HTTP method
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param array $data Request data
 */
public function process_scheduled_api_call($method, $endpoint, $params = [], $data = null) {
    try {
        $response = $this->api_client->request($method, $endpoint, $params, $data);
        $this->log_api_activity($endpoint, 'success');
    } catch (Exception $e) {
        $this->log_api_activity($endpoint, 'error', $e->getMessage());
    }
}
```

### Optimize Data Transfer

Minimize the amount of data transferred:

1. **Request only the data you need**: Use API parameters to filter results
2. **Compress data**: Use gzip compression when available
3. **Use pagination**: Request data in smaller chunks
4. **Use conditional requests**: Use ETag or If-Modified-Since headers

```php
/**
 * Get paginated data
 *
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param int $page_size Page size
 * @return array All data
 */
public function get_all_paginated_data($endpoint, $params = [], $page_size = 100) {
    $all_data = [];
    $page = 1;
    
    do {
        // Get page of data
        $page_params = array_merge($params, [
            'page' => $page,
            'per_page' => $page_size
        ]);
        
        $data = $this->api_client->get($endpoint, $page_params);
        
        // Add data to result
        if (!empty($data)) {
            $all_data = array_merge($all_data, $data);
        }
        
        // Increment page
        $page++;
        
        // Continue until no more data
    } while (!empty($data) && count($data) === $page_size);
    
    return $all_data;
}
```

## Error Handling and Graceful Degradation

Implement robust error handling to provide a better user experience:

### Implement Comprehensive Error Handling

Handle different types of errors appropriately:

```php
try {
    $data = $this->api_client->get('endpoint');
    // Process data
} catch (ApiAuthException $e) {
    // Handle authentication errors
    $this->log_error('Authentication error: ' . $e->getMessage());
    $this->notify_admin('API authentication failed. Please check your credentials.');
    return $this->get_fallback_data();
} catch (ApiRateLimitException $e) {
    // Handle rate limiting
    $this->log_error('Rate limit exceeded: ' . $e->getMessage());
    $this->schedule_retry($e->getRetryAfter());
    return $this->get_cached_data() ?: $this->get_fallback_data();
} catch (ApiServerException $e) {
    // Handle server errors
    $this->log_error('Server error: ' . $e->getMessage());
    return $this->get_cached_data() ?: $this->get_fallback_data();
} catch (ApiClientException $e) {
    // Handle client errors
    $this->log_error('Client error: ' . $e->getMessage());
    return $this->get_fallback_data();
} catch (Exception $e) {
    // Handle unexpected errors
    $this->log_error('Unexpected error: ' . $e->getMessage());
    return $this->get_fallback_data();
}
```

### Implement Retry Logic

Retry failed API calls with exponential backoff:

```php
/**
 * Retry API call with exponential backoff
 *
 * @param string $method HTTP method
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param array $data Request data
 * @param int $retry_count Retry count
 * @param int $max_retries Maximum number of retries
 * @return array Response data
 */
public function retry_api_call($method, $endpoint, $params = [], $data = null, $retry_count = 0, $max_retries = 3) {
    try {
        return $this->api_client->request($method, $endpoint, $params, $data);
    } catch (ApiRateLimitException $e) {
        // Handle rate limiting
        $retry_after = $e->getRetryAfter();
        if ($retry_count < $max_retries) {
            sleep($retry_after);
            return $this->retry_api_call($method, $endpoint, $params, $data, $retry_count + 1, $max_retries);
        }
        throw $e;
    } catch (ApiServerException $e) {
        // Handle server errors
        if ($retry_count < $max_retries) {
            $backoff = pow(2, $retry_count);
            sleep($backoff);
            return $this->retry_api_call($method, $endpoint, $params, $data, $retry_count + 1, $max_retries);
        }
        throw $e;
    } catch (ApiConnectionException $e) {
        // Handle connection errors
        if ($retry_count < $max_retries) {
            $backoff = pow(2, $retry_count);
            sleep($backoff);
            return $this->retry_api_call($method, $endpoint, $params, $data, $retry_count + 1, $max_retries);
        }
        throw $e;
    }
}
```

### Implement Fallback Mechanisms

Provide fallback mechanisms for when the API is unavailable:

```php
/**
 * Get fallback data
 *
 * @param string $endpoint API endpoint
 * @return array Fallback data
 */
public function get_fallback_data($endpoint = '') {
    // Check for cached data
    $cached = $this->get_cached_data($endpoint);
    if ($cached) {
        return $cached;
    }
    
    // Return default data
    switch ($endpoint) {
        case 'users':
            return ['status' => 'offline', 'data' => []];
        case 'stats':
            return ['status' => 'offline', 'data' => ['visits' => 0, 'conversions' => 0]];
        default:
            return ['status' => 'offline', 'data' => []];
    }
}
```

### Implement Circuit Breaker Pattern

Implement the circuit breaker pattern to prevent cascading failures:

```php
class CircuitBreaker {
    private $failures = 0;
    private $threshold = 5;
    private $reset_timeout = 60;
    private $last_failure_time = 0;
    private $state = 'closed'; // closed, open, half-open
    
    /**
     * Execute function with circuit breaker
     *
     * @param callable $func Function to execute
     * @return mixed Function result
     */
    public function execute($func) {
        // Check if circuit is open
        if ($this->is_open()) {
            // Check if reset timeout has passed
            if (time() - $this->last_failure_time > $this->reset_timeout) {
                // Set circuit to half-open
                $this->state = 'half-open';
            } else {
                throw new Exception('Circuit is open');
            }
        }
        
        try {
            // Execute function
            $result = $func();
            
            // Reset failures on success
            if ($this->state === 'half-open') {
                $this->reset();
            }
            
            return $result;
        } catch (Exception $e) {
            // Increment failures
            $this->failures++;
            $this->last_failure_time = time();
            
            // Open circuit if threshold is reached
            if ($this->failures >= $this->threshold) {
                $this->state = 'open';
            }
            
            throw $e;
        }
    }
    
    /**
     * Check if circuit is open
     *
     * @return bool Whether circuit is open
     */
    public function is_open() {
        return $this->state === 'open';
    }
    
    /**
     * Reset circuit
     */
    public function reset() {
        $this->failures = 0;
        $this->state = 'closed';
    }
}
```

## User Experience Design for API-Dependent Features

Design your integration with the user experience in mind:

### Provide Clear Feedback

Keep users informed about the status of API operations:

```php
/**
 * Display API status
 */
public function display_api_status() {
    // Check API status
    $status = $this->get_api_status();
    
    // Display status
    switch ($status) {
        case 'connected':
            ?>
            <div class="ui green message">
                <i class="check icon"></i>
                <?php esc_html_e('Connected to API', 'my-integration'); ?>
            </div>
            <?php
            break;
        
        case 'limited':
            ?>
            <div class="ui yellow message">
                <i class="exclamation triangle icon"></i>
                <?php esc_html_e('Connected to API with limited functionality', 'my-integration'); ?>
            </div>
            <?php
            break;
        
        case 'disconnected':
            ?>
            <div class="ui red message">
                <i class="times icon"></i>
                <?php esc_html_e('Disconnected from API', 'my-integration'); ?>
            </div>
            <?php
            break;
    }
}
```

### Implement Loading States

Show loading states during API operations:

```php
/**
 * Display loading state
 *
 * @param string $message Loading message
 */
public function display_loading_state($message = '') {
    ?>
    <div class="ui segment loading-state">
        <div class="ui active dimmer">
            <div class="ui text loader"><?php echo esc_html($message ?: __('Loading...', 'my-integration')); ?></div>
        </div>
        <p></p>
    </div>
    
    <script type="text/javascript">
    jQuery(document).ready(function($) {
        // Show loading state
        $('.loading-state').show();
        
        // Make API request
        $.ajax({
            url: ajaxurl,
            type: 'POST',
            data: {
                action: 'my_integration_api_request',
                nonce: '<?php echo wp_create_nonce('my_integration_api_request'); ?>'
            },
            success: function(response) {
                // Hide loading state
                $('.loading-state').hide();
                
                // Display response
                if (response.success) {
                    // Display success message
                } else {
                    // Display error message
                }
            },
            error: function() {
                // Hide loading state
                $('.loading-state').hide();
                
                // Display error message
            }
        });
    });
    </script>
    <?php
}
```

### Implement Offline Mode

Allow users to continue working when the API is unavailable:

```php
/**
 * Check if offline mode is enabled
 *
 * @return bool Whether offline mode is enabled
 */
public function is_offline_mode() {
    return get_option('my_integration_offline_mode', false);
}

/**
 * Enable offline mode
 */
public function enable_offline_mode() {
    update_option('my_integration_offline_mode', true);
}

/**
 * Disable offline mode
 */
public function disable_offline_mode() {
    update_option('my_integration_offline_mode', false);
}

/**
 * Get data with offline mode support
 *
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @return array Data
 */
public function get_data_with_offline_support($endpoint, $params = []) {
    // Check if offline mode is enabled
    if ($this->is_offline_mode()) {
        return $this->get_fallback_data($endpoint);
    }
    
    try {
        // Get data from API
        return $this->api_client->get($endpoint, $params);
    } catch (Exception $e) {
        // Enable offline mode
        $this->enable_offline_mode();
        
        // Return fallback data
        return $this->get_fallback_data($endpoint);
    }
}
```

## Data Synchronization Strategies

Implement effective data synchronization between MainWP and the third-party service:

### Implement Pull-Based Sync

Pull data from the third-party service on a schedule:

```php
/**
 * Schedule regular syncs
 */
public function schedule_syncs() {
    // Schedule daily sync if not already scheduled
    if (!wp_next_scheduled('my_integration_daily_sync')) {
        wp_schedule_event(time(), 'daily', 'my_integration_daily_sync');
    }
    
    // Add action hook for the event
    add_action('my_integration_daily_sync', [$this, 'sync_all_websites']);
}

/**
 * Sync all websites
 */
public function sync_all_websites() {
    // Get all MainWP websites
    $websites = MainWP\Dashboard\MainWP_DB::instance()->get_websites();
    
    foreach ($websites as $website) {
        // Check if integration is enabled for this website
        $enabled = get_option('my_integration_enabled_' . $website->id, false);
        if (!$enabled) {
            continue;
        }
        
        // Sync data
        $this->sync_from_service($website->id);
    }
}
```

### Implement Push-Based Sync

Push data to the third-party service when it changes:

```php
/**
 * Hook into MainWP events to push data
 */
public function register_push_hooks() {
    // Hook into site added event
    add_action('mainwp_site_added', [$this, 'push_site_added'], 10, 1);
    
    // Hook into site updated event
    add_action('mainwp_site_updated', [$this, 'push_site_updated'], 10, 1);
    
    // Hook into site deleted event
    add_action('mainwp_site_deleted', [$this, 'push_site_deleted'], 10, 1);
}

/**
 * Push site added event
 *
 * @param int $website_id Website ID
 */
public function push_site_added($website_id) {
    // Get website details
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return;
    }
    
    // Push data to third-party service
    $this->api_client->post('sites', [
        'url' => $website->url,
        'name' => $website->name
    ]);
}
```

### Implement Bidirectional Sync

Synchronize data in both directions:

```php
/**
 * Perform bidirectional sync
 *
 * @param int $website_id Website ID
 */
public function bidirectional_sync($website_id) {
    // Get website details
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return;
    }
    
    // Get last sync timestamp
    $last_sync = get_option('my_integration_last_sync_' . $website_id, 0);
    
    // Get changes from third-party service
    $service_changes = $this->api_client->get('sites/' . urlencode($website->url) . '/changes', [
        'since' => $last_sync
    ]);
    
    // Get local changes
    $local_changes = $this->get_local_changes($website_id, $last_sync);
    
    // Resolve conflicts
    $resolved_changes = $this->resolve_conflicts($service_changes, $local_changes);
    
    // Apply service changes locally
    $this->apply_service_changes($website_id, $resolved_changes['local_updates']);
    
    // Push local changes to service
    $this->push_local_changes($website_id, $resolved_changes['service_updates']);
    
    // Update last sync timestamp
    update_option('my_integration_last_sync_' . $website_id, time());
}
```

### Implement Conflict Resolution

Resolve conflicts when data changes in both systems:

```php
/**
 * Resolve conflicts between local and service changes
 *
 * @param array $service_changes Changes from third-party service
 * @param array $local_changes Local changes
 * @return array Resolved changes
 */
public function resolve_conflicts($service_changes, $local_changes) {
    $local_updates = [];
    $service_updates = [];
    
    // Process service changes
    foreach ($service_changes as $key => $service_item) {
        if (isset($local_changes[$key])) {
            // Conflict: both sides have changes
            $local_item = $local_changes[$key];
            
            // Resolve based on timestamp (newer wins)
            if ($service_item['updated_at'] > $local_item['updated_at']) {
                $local_updates[$key] = $service_item;
            } else {
                $service_updates[$key] = $local_item;
            }
            
            // Remove from local changes to mark as processed
            unset($local_changes[$key]);
        } else {
            // No conflict: only service has changes
            $local_updates[$key] = $service_item;
        }
    }
    
    // Remaining local changes need to be sent to service
    foreach ($local_changes as $key => $local_item) {
        $service_updates[$key] = $local_item;
    }
    
    return [
        'local_updates' => $local_updates,
        'service_updates' => $service_updates
    ];
}
```

## Handling API Rate Limits and Quotas

Implement strategies to handle API rate limits and quotas:

### Implement Rate Limit Tracking

Track API rate limits to avoid exceeding them:

```php
/**
 * Track API rate limits
 *
 * @param array $response API response
 */
public function track_rate_limits($response) {
    // Get rate limit headers
    $rate_limit = wp_remote_retrieve_header($response, 'X-RateLimit-Limit');
    $rate_limit_remaining = wp_remote_retrieve_header($response, 'X-RateLimit-Remaining');
    $rate_limit_reset = wp_remote_retrieve_header($response, 'X-RateLimit-Reset');
    
    // Save rate limit data
    update_option('my_integration_rate_limit', [
        'limit' => $rate_limit,
        'remaining' => $rate_limit_remaining,
        'reset' => $rate_limit_reset
    ]);
}

/**

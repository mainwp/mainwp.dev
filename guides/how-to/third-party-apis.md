# Working with Third-Party APIs in MainWP Integrations

This guide provides comprehensive information on working with third-party APIs in MainWP integrations. You'll learn how to design robust API clients, handle authentication, manage errors, implement caching, and more.

## Quick Start for Experienced Developers

```php
// 1. Create a reusable API client class
class ThirdPartyApiClient {
    private $api_key;
    private $api_url = 'https://api.third-party-service.com/v1/';
    private $timeout = 30;
    
    public function __construct($api_key) {
        $this->api_key = $api_key;
    }
    
    public function get($endpoint, $params = []) {
        return $this->request('GET', $endpoint, $params);
    }
    
    public function post($endpoint, $data = []) {
        return $this->request('POST', $endpoint, [], $data);
    }
    
    private function request($method, $endpoint, $params = [], $data = null) {
        $url = $this->api_url . $endpoint;
        $cache_key = 'tpapi_' . md5($method . $url . serialize($params) . serialize($data));
        
        // Check cache for GET requests
        if ($method === 'GET') {
            $cached = get_transient($cache_key);
            if (false !== $cached) {
                return $cached;
            }
        }
        
        // Prepare request
        $args = [
            'method' => $method,
            'headers' => [
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json',
                'Accept' => 'application/json'
            ],
            'timeout' => $this->timeout
        ];
        
        // Add query parameters
        if (!empty($params)) {
            $url = add_query_arg($params, $url);
        }
        
        // Add body data for POST/PUT/PATCH
        if ($data !== null && in_array($method, ['POST', 'PUT', 'PATCH'])) {
            $args['body'] = json_encode($data);
        }
        
        // Make request
        $response = wp_remote_request($url, $args);
        
        // Handle errors
        if (is_wp_error($response)) {
            throw new Exception('API request failed: ' . $response->get_error_message());
        }
        
        $status_code = wp_remote_retrieve_response_code($response);
        $body = wp_remote_retrieve_body($response);
        $result = json_decode($body, true);
        
        // Handle API errors
        if ($status_code >= 400) {
            $error_message = isset($result['message']) ? $result['message'] : 'Unknown API error';
            throw new Exception("API error ($status_code): $error_message");
        }
        
        // Cache successful GET responses
        if ($method === 'GET') {
            set_transient($cache_key, $result, 5 * MINUTE_IN_SECONDS);
        }
        
        return $result;
    }
}

// 2. Use the API client in your MainWP integration
class MyIntegration {
    private $api_client;
    
    public function __construct() {
        // Initialize API client
        $api_key = get_option('my_integration_api_key', '');
        if (!empty($api_key)) {
            $this->api_client = new ThirdPartyApiClient($api_key);
        }
        
        // Hook into MainWP
        add_action('mainwp_site_synced', [$this, 'sync_third_party_data'], 10, 2);
    }
    
    public function sync_third_party_data($website, $data) {
        if (!$this->api_client) {
            return;
        }
        
        try {
            // Get data from third-party API
            $api_data = $this->api_client->get('sites/' . urlencode($website->url));
            
            // Store the data for this site
            update_option('my_integration_data_' . $website->id, $api_data);
            update_option('my_integration_last_sync_' . $website->id, time());
        } catch (Exception $e) {
            // Log error but continue
            error_log('API Error: ' . $e->getMessage());
        }
    }
}
```

## Designing a Robust API Client

A well-designed API client is the foundation of any successful third-party integration. It should handle authentication, requests, responses, errors, and caching in a consistent way.

### Basic API Client Structure

Here's a comprehensive API client class that you can adapt for your integration:

```php
class ThirdPartyApiClient {
    private $api_key;
    private $api_url;
    private $timeout = 30;
    private $last_response;
    private $last_request;
    
    /**
     * Constructor
     *
     * @param string $api_key API key or token
     * @param string $api_url Base API URL
     */
    public function __construct($api_key, $api_url = 'https://api.third-party-service.com/v1/') {
        $this->api_key = $api_key;
        $this->api_url = $api_url;
    }
    
    /**
     * Make a GET request
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param bool $cache Whether to cache the response
     * @param int $cache_time Cache time in seconds
     * @return array|object Response data
     */
    public function get($endpoint, $params = [], $cache = true, $cache_time = 300) {
        return $this->request('GET', $endpoint, $params, null, $cache, $cache_time);
    }
    
    /**
     * Make a POST request
     *
     * @param string $endpoint API endpoint
     * @param array $data Post data
     * @param array $params Query parameters
     * @return array|object Response data
     */
    public function post($endpoint, $data = [], $params = []) {
        return $this->request('POST', $endpoint, $params, $data);
    }
    
    /**
     * Make a PUT request
     *
     * @param string $endpoint API endpoint
     * @param array $data Put data
     * @param array $params Query parameters
     * @return array|object Response data
     */
    public function put($endpoint, $data = [], $params = []) {
        return $this->request('PUT', $endpoint, $params, $data);
    }
    
    /**
     * Make a DELETE request
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @return array|object Response data
     */
    public function delete($endpoint, $params = []) {
        return $this->request('DELETE', $endpoint, $params);
    }
    
    /**
     * Make an API request
     *
     * @param string $method HTTP method
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param array $data Request body data
     * @param bool $cache Whether to cache the response
     * @param int $cache_time Cache time in seconds
     * @return array|object Response data
     * @throws Exception If the request fails
     */
    private function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300) {
        $url = $this->api_url . ltrim($endpoint, '/');
        $cache_key = 'tpapi_' . md5($method . $url . serialize($params) . serialize($data));
        
        // Check cache for GET requests
        if ($method === 'GET' && $cache) {
            $cached = get_transient($cache_key);
            if (false !== $cached) {
                return $cached;
            }
        }
        
        // Prepare request
        $args = [
            'method' => $method,
            'headers' => [
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json',
                'Accept' => 'application/json'
            ],
            'timeout' => $this->timeout
        ];
        
        // Add query parameters
        if (!empty($params)) {
            $url = add_query_arg($params, $url);
        }
        
        // Add body data for POST/PUT/PATCH
        if ($data !== null && in_array($method, ['POST', 'PUT', 'PATCH'])) {
            $args['body'] = json_encode($data);
        }
        
        // Store request for debugging
        $this->last_request = [
            'url' => $url,
            'method' => $method,
            'args' => $args
        ];
        
        // Make request
        $response = wp_remote_request($url, $args);
        $this->last_response = $response;
        
        // Handle connection errors
        if (is_wp_error($response)) {
            throw new Exception('API request failed: ' . $response->get_error_message());
        }
        
        $status_code = wp_remote_retrieve_response_code($response);
        $body = wp_remote_retrieve_body($response);
        $result = json_decode($body, true);
        
        // Handle API errors
        if ($status_code >= 400) {
            $error_message = isset($result['message']) ? $result['message'] : 'Unknown API error';
            throw new Exception("API error ($status_code): $error_message", $status_code);
        }
        
        // Cache successful GET responses
        if ($method === 'GET' && $cache) {
            set_transient($cache_key, $result, $cache_time);
        }
        
        return $result;
    }
    
    /**
     * Get the last response
     *
     * @return array|WP_Error Last response
     */
    public function get_last_response() {
        return $this->last_response;
    }
    
    /**
     * Get the last request
     *
     * @return array Last request
     */
    public function get_last_request() {
        return $this->last_request;
    }
    
    /**
     * Test the API connection
     *
     * @return bool Whether the connection is successful
     */
    public function test_connection() {
        try {
            // Replace 'test-endpoint' with an actual lightweight endpoint from your API
            $this->get('test-endpoint', [], false);
            return true;
        } catch (Exception $e) {
            return false;
        }
    }
}
```

### Key Features to Include

When designing your API client, consider including these features:

1. **Method-specific functions**: Create dedicated methods for GET, POST, PUT, DELETE, etc.
2. **Consistent error handling**: Throw exceptions with meaningful messages
3. **Response caching**: Cache GET responses to reduce API calls
4. **Request/response logging**: Store the last request and response for debugging
5. **Configurable timeouts**: Allow adjustment of request timeouts
6. **Connection testing**: Include a method to test the API connection

## Authentication Methods

Different APIs use different authentication methods. Here's how to implement the most common ones:

### API Key Authentication

Many APIs use API keys, either in the header or as a query parameter:

```php
// API key in header
$args = [
    'headers' => [
        'X-API-Key' => $this->api_key
    ]
];

// API key in query parameter
$url = add_query_arg(['api_key' => $this->api_key], $url);
```

### Bearer Token Authentication

Bearer tokens (including JWT) are typically sent in the Authorization header:

```php
$args = [
    'headers' => [
        'Authorization' => 'Bearer ' . $this->api_token
    ]
];
```

### Basic Authentication

Basic authentication uses base64-encoded username and password:

```php
$args = [
    'headers' => [
        'Authorization' => 'Basic ' . base64_encode($this->username . ':' . $this->password)
    ]
];
```

### OAuth 2.0 Authentication

OAuth 2.0 is more complex and typically involves:

1. Redirecting the user to the authorization server
2. Receiving an authorization code
3. Exchanging the code for access and refresh tokens
4. Using the access token for API requests
5. Refreshing the access token when it expires

Here's a simplified implementation:

```php
class OAuth2Client extends ThirdPartyApiClient {
    private $client_id;
    private $client_secret;
    private $redirect_uri;
    private $auth_url;
    private $token_url;
    private $access_token;
    private $refresh_token;
    private $token_expires;
    
    public function __construct($client_id, $client_secret, $redirect_uri, $auth_url, $token_url, $api_url) {
        $this->client_id = $client_id;
        $this->client_secret = $client_secret;
        $this->redirect_uri = $redirect_uri;
        $this->auth_url = $auth_url;
        $this->token_url = $token_url;
        
        // Load tokens from options
        $this->access_token = get_option('my_integration_access_token', '');
        $this->refresh_token = get_option('my_integration_refresh_token', '');
        $this->token_expires = get_option('my_integration_token_expires', 0);
        
        parent::__construct($this->access_token, $api_url);
    }
    
    /**
     * Get the authorization URL
     *
     * @param array $scope API scopes to request
     * @param string $state State parameter for security
     * @return string Authorization URL
     */
    public function get_auth_url($scope = [], $state = '') {
        $params = [
            'client_id' => $this->client_id,
            'redirect_uri' => $this->redirect_uri,
            'response_type' => 'code',
            'state' => $state ?: wp_create_nonce('oauth2_state')
        ];
        
        if (!empty($scope)) {
            $params['scope'] = implode(' ', $scope);
        }
        
        return add_query_arg($params, $this->auth_url);
    }
    
    /**
     * Exchange authorization code for tokens
     *
     * @param string $code Authorization code
     * @return bool Whether the exchange was successful
     */
    public function exchange_code_for_tokens($code) {
        $args = [
            'method' => 'POST',
            'headers' => [
                'Content-Type' => 'application/x-www-form-urlencoded'
            ],
            'body' => [
                'grant_type' => 'authorization_code',
                'code' => $code,
                'client_id' => $this->client_id,
                'client_secret' => $this->client_secret,
                'redirect_uri' => $this->redirect_uri
            ]
        ];
        
        $response = wp_remote_post($this->token_url, $args);
        
        if (is_wp_error($response)) {
            return false;
        }
        
        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);
        
        if (empty($data['access_token'])) {
            return false;
        }
        
        // Save tokens
        $this->access_token = $data['access_token'];
        $this->refresh_token = $data['refresh_token'] ?? '';
        $this->token_expires = time() + ($data['expires_in'] ?? 3600);
        
        update_option('my_integration_access_token', $this->access_token);
        update_option('my_integration_refresh_token', $this->refresh_token);
        update_option('my_integration_token_expires', $this->token_expires);
        
        return true;
    }
    
    /**
     * Refresh the access token
     *
     * @return bool Whether the refresh was successful
     */
    public function refresh_access_token() {
        if (empty($this->refresh_token)) {
            return false;
        }
        
        $args = [
            'method' => 'POST',
            'headers' => [
                'Content-Type' => 'application/x-www-form-urlencoded'
            ],
            'body' => [
                'grant_type' => 'refresh_token',
                'refresh_token' => $this->refresh_token,
                'client_id' => $this->client_id,
                'client_secret' => $this->client_secret
            ]
        ];
        
        $response = wp_remote_post($this->token_url, $args);
        
        if (is_wp_error($response)) {
            return false;
        }
        
        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);
        
        if (empty($data['access_token'])) {
            return false;
        }
        
        // Save tokens
        $this->access_token = $data['access_token'];
        if (!empty($data['refresh_token'])) {
            $this->refresh_token = $data['refresh_token'];
            update_option('my_integration_refresh_token', $this->refresh_token);
        }
        $this->token_expires = time() + ($data['expires_in'] ?? 3600);
        
        update_option('my_integration_access_token', $this->access_token);
        update_option('my_integration_token_expires', $this->token_expires);
        
        return true;
    }
    
    /**
     * Override request method to handle token refresh
     */
    protected function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300) {
        // Check if token is expired and refresh if needed
        if (time() > $this->token_expires - 60) {
            $this->refresh_access_token();
        }
        
        // Update the access token in the parent class
        $this->api_key = $this->access_token;
        
        return parent::request($method, $endpoint, $params, $data, $cache, $cache_time);
    }
}
```

To use this OAuth2 client in your MainWP integration:

```php
// In your admin page
public function render_auth_page() {
    $client_id = get_option('my_integration_client_id', '');
    $client_secret = get_option('my_integration_client_secret', '');
    $redirect_uri = admin_url('admin.php?page=MyIntegrationAuth');
    
    $oauth_client = new OAuth2Client(
        $client_id,
        $client_secret,
        $redirect_uri,
        'https://service.com/oauth/authorize',
        'https://service.com/oauth/token',
        'https://api.service.com/v1/'
    );
    
    // Handle authorization code callback
    if (isset($_GET['code']) && isset($_GET['state'])) {
        $code = sanitize_text_field($_GET['code']);
        $state = sanitize_text_field($_GET['state']);
        
        // Verify state to prevent CSRF
        if (!wp_verify_nonce($state, 'oauth2_state')) {
            ?>
            <div class="ui red message"><?php esc_html_e('Invalid state parameter. Please try again.', 'my-integration'); ?></div>
            <?php
            return;
        }
        
        if ($oauth_client->exchange_code_for_tokens($code)) {
            ?>
            <div class="ui green message"><?php esc_html_e('Successfully authenticated with the service.', 'my-integration'); ?></div>
            <?php
        } else {
            ?>
            <div class="ui red message"><?php esc_html_e('Failed to authenticate with the service.', 'my-integration'); ?></div>
            <?php
        }
    }
    
    // Display auth button if not authenticated
    if (empty(get_option('my_integration_access_token', ''))) {
        $auth_url = $oauth_client->get_auth_url(['read', 'write']);
        ?>
        <a href="<?php echo esc_url($auth_url); ?>" class="ui green button">
            <?php esc_html_e('Connect to Service', 'my-integration'); ?>
        </a>
        <?php
    } else {
        ?>
        <div class="ui green message"><?php esc_html_e('Connected to service.', 'my-integration'); ?></div>
        <a href="<?php echo esc_url(admin_url('admin.php?page=MyIntegrationAuth&disconnect=1')); ?>" class="ui red button">
            <?php esc_html_e('Disconnect from Service', 'my-integration'); ?>
        </a>
        <?php
    }
}
```

## Error Handling and Retry Strategies

Robust error handling is essential for reliable API integrations. Here's a comprehensive approach:

### Error Types to Handle

1. **Connection errors**: Network issues, timeouts
2. **Authentication errors**: Invalid or expired credentials
3. **Rate limiting**: Too many requests
4. **Server errors**: 5xx responses
5. **Client errors**: 4xx responses
6. **Parsing errors**: Invalid JSON responses

### Implementing Error Handling

Here's an enhanced version of the request method with comprehensive error handling:

```php
/**
 * Make an API request with error handling and retries
 *
 * @param string $method HTTP method
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param array $data Request body data
 * @param bool $cache Whether to cache the response
 * @param int $cache_time Cache time in seconds
 * @param int $retry_count Number of retry attempts
 * @return array|object Response data
 * @throws ApiConnectionException If the connection fails
 * @throws ApiAuthException If authentication fails
 * @throws ApiRateLimitException If rate limited
 * @throws ApiServerException If the server returns an error
 * @throws ApiClientException If the client makes an invalid request
 */
private function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300, $retry_count = 0) {
    $url = $this->api_url . ltrim($endpoint, '/');
    $cache_key = 'tpapi_' . md5($method . $url . serialize($params) . serialize($data));
    
    // Check cache for GET requests
    if ($method === 'GET' && $cache) {
        $cached = get_transient($cache_key);
        if (false !== $cached) {
            return $cached;
        }
    }
    
    // Prepare request
    $args = [
        'method' => $method,
        'headers' => [
            'Authorization' => 'Bearer ' . $this->api_key,
            'Content-Type' => 'application/json',
            'Accept' => 'application/json'
        ],
        'timeout' => $this->timeout
    ];
    
    // Add query parameters
    if (!empty($params)) {
        $url = add_query_arg($params, $url);
    }
    
    // Add body data for POST/PUT/PATCH
    if ($data !== null && in_array($method, ['POST', 'PUT', 'PATCH'])) {
        $args['body'] = json_encode($data);
    }
    
    // Store request for debugging
    $this->last_request = [
        'url' => $url,
        'method' => $method,
        'args' => $args
    ];
    
    // Make request
    $response = wp_remote_request($url, $args);
    $this->last_response = $response;
    
    // Handle connection errors
    if (is_wp_error($response)) {
        $error_message = $response->get_error_message();
        
        // Check if we should retry
        if ($retry_count < $this->max_retries) {
            // Exponential backoff: 1s, 2s, 4s, 8s, etc.
            $backoff = pow(2, $retry_count);
            sleep($backoff);
            return $this->request($method, $endpoint, $params, $data, $cache, $cache_time, $retry_count + 1);
        }
        
        throw new ApiConnectionException('API connection failed: ' . $error_message);
    }
    
    $status_code = wp_remote_retrieve_response_code($response);
    $body = wp_remote_retrieve_body($response);
    
    // Try to parse JSON response
    $result = json_decode($body, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        // Not JSON or invalid JSON
        $result = ['raw_response' => $body];
    }
    
    // Handle different error types
    if ($status_code >= 400) {
        $error_message = isset($result['message']) ? $result['message'] : 'Unknown API error';
        
        // Authentication errors
        if ($status_code === 401) {
            throw new ApiAuthException("Authentication failed: $error_message", $status_code);
        }
        
        // Rate limiting
        if ($status_code === 429) {
            // Get retry-after header if available
            $retry_after = wp_remote_retrieve_header($response, 'retry-after');
            $retry_after = $retry_after ? (int)$retry_after : 60;
            
            // Check if we should retry
            if ($retry_count < $this->max_retries) {
                sleep($retry_after);
                return $this->request($method, $endpoint, $params, $data, $cache, $cache_time, $retry_count + 1);
            }
            
            throw new ApiRateLimitException("Rate limit exceeded: $error_message", $status_code, $retry_after);
        }
        
        // Server errors
        if ($status_code >= 500) {
            // Check if we should retry
            if ($retry_count < $this->max_retries) {
                // Exponential backoff
                $backoff = pow(2, $retry_count);
                sleep($backoff);
                return $this->request($method, $endpoint, $params, $data, $cache, $cache_time, $retry_count + 1);
            }
            
            throw new ApiServerException("Server error ($status_code): $error_message", $status_code);
        }
        
        // Client errors
        throw new ApiClientException("Client error ($status_code): $error_message", $status_code);
    }
    
    // Cache successful GET responses
    if ($method === 'GET' && $cache) {
        set_transient($cache_key, $result, $cache_time);
    }
    
    return $result;
}
```

### Custom Exception Classes

Create custom exception classes for different error types:

```php
class ApiException extends Exception {
    protected $status_code;
    
    public function __construct($message, $status_code = 0, $code = 0) {
        $this->status_code = $status_code;
        parent::__construct($message, $code);
    }
    
    public function getStatusCode() {
        return $this->status_code;
    }
}

class ApiConnectionException extends ApiException {}
class ApiAuthException extends ApiException {}
class ApiRateLimitException extends ApiException {
    protected $retry_after;
    
    public function __construct($message, $status_code = 0, $retry_after = 60, $code = 0) {
        $this->retry_after = $retry_after;
        parent::__construct($message, $status_code, $code);
    }
    
    public function getRetryAfter() {
        return $this->retry_after;
    }
}
class ApiServerException extends ApiException {}
class ApiClientException extends ApiException {}
```

### Using Try-Catch for Error Handling

When using your API client, wrap calls in try-catch blocks:

```php
try {
    $data = $api_client->get('endpoint');
    // Process successful response
} catch (ApiAuthException $e) {
    // Handle authentication errors
    error_log('API Authentication Error: ' . $e->getMessage());
    // Prompt user to re-authenticate
} catch (ApiRateLimitException $e) {
    // Handle rate limiting
    error_log('API Rate Limit Error: ' . $e->getMessage());
    error_log('Retry After: ' . $e->getRetryAfter() . ' seconds');
    // Schedule a retry after the specified time
} catch (ApiServerException $e) {
    // Handle server errors
    error_log('API Server Error: ' . $e->getMessage());
    // Display a friendly message to the user
} catch (ApiClientException $e) {
    // Handle client errors
    error_log('API Client Error: ' . $e->getMessage());
    // Fix the request or display an error message
} catch (ApiConnectionException $e) {
    // Handle connection errors
    error_log('API Connection Error: ' . $e->getMessage());
    // Check network connectivity
} catch (Exception $e) {
    // Handle any other errors
    error_log('API Error: ' . $e->getMessage());
}
```

## Rate Limiting Considerations

Most APIs implement rate limits to prevent abuse. Here's how to handle them:

### Understanding Rate Limits

Rate limits can be:
- **Request-based**: X requests per time period
- **Resource-based**: X operations on a specific resource
- **User-based**: X requests per user
- **Token-based**: X requests per API token

### Strategies for Handling Rate Limits

1. **Caching**: Cache responses to reduce API calls
2. **Batching**: Combine multiple operations into a single request
3. **Queuing**: Queue requests and process them at a controlled rate
4. **Exponential backoff**: Increase wait time between retries
5. **Request prioritization**: Prioritize critical requests

### Implementing a Rate Limit Handler

```php
class RateLimitHandler {
    private $bucket_size;
    private $refill_rate;
    private $available_tokens;
    private $last_refill_time;
    private $option_name;
    
    /**
     * Constructor
     *
     * @param int $bucket_size Maximum number of tokens (requests)
     * @param int $refill_rate Tokens added per second
     * @param string $option_name Option name for storing state
     */
    public function __construct($bucket_size = 60, $refill_rate = 1, $option_name = 'api_rate_limit_state') {
        $this->bucket_size = $bucket_size;
        $this->refill_rate = $refill_rate;
        $this->option_name = $option_name;
        
        // Load state
        $state = get_option($option_name, [
            'available_tokens' => $bucket_size,
            'last_refill_time' => time()
        ]);
        
        $this->available_tokens = $state['available_tokens'];
        $this->last_refill_time = $state['last_refill_time'];
        
        // Refill tokens based on elapsed time
        $this->refill_tokens();
    }
    
    /**
     * Refill tokens based on elapsed time
     */
    private function refill_tokens() {
        $now = time();
        $elapsed = $now - $this->last_refill_time;
        
        if ($elapsed > 0) {
            $new_tokens = $elapsed * $this->refill_rate;
            $this->available_tokens = min($this->bucket_size, $this->available_tokens + $new_tokens);
            $this->last_refill_time = $now;
            
            // Save state
            update_option($this->option_name, [
                'available_tokens' => $this->available_tokens,
                'last_refill_time' => $this->last_refill_time
            ]);
        }
    }
    
    /**
     * Check if a request can be made
     *
     * @param int $tokens Number of tokens required (default 1)
     * @return bool Whether the request can be made
     */
    public function can_make_request($tokens = 1) {
        $this->refill_tokens();
        return $this->available_tokens >= $tokens;
    }
    
    /**
     * Consume tokens for a request
     *
     * @param int $tokens Number of tokens to consume (default 1)
     * @return bool Whether tokens were consumed
     */
    public function consume_tokens($tokens = 1) {
        if (!$this->can_make_request($tokens)) {
            return false;
        }
        
        $this->available_tokens -= $tokens;
        
        // Save state
        update_option($this->option_name, [
            'available_tokens' => $this->available_tokens,
            'last_refill_time' => $this->last_refill_time
        ]);
        
        return true;
    }
    
    /**
     * Get time until next token is available
     *
     * @return int Seconds until next token
     */
    public function get_wait_time() {
        if ($this->available_tokens > 0) {
            return 0;
        }
        
        return ceil(1 / $this->refill_rate);
    }
}
```

### Using the Rate Limit Handler

```php
class ThirdPartyApiClient {
    // ... other properties
    private $rate_limiter;
    
    public function __construct($api_key, $api_url = 'https://api.third-party-service.com/v1/') {
        $this->api_key = $api_key;
        $this->api_url = $api_url;
        
        // Initialize rate limiter with API limits (e.g., 60 requests per minute)
        $this->rate_limiter = new RateLimitHandler(60, 1, 'my_integration_rate_limit');
    }
    
    private function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300) {
        // Check if we can make a request
        if (!$this->rate_limiter->can_make_request()) {
            $wait_time = $this->rate_limiter->get_wait_time();
            throw new ApiRateLimitException("Rate limit exceeded. Try again in $wait_time seconds.", 429, $wait_time);
        }
        
        // Make the request
        // ... existing request code ...
        
        // Consume a token for the request
        $this->rate_limiter->consume_tokens();
        
        return $result;
    }
}
```

## Caching API Responses

Caching is essential for reducing API calls, improving performance, and avoiding rate limits. Here's how to implement effective caching:

### When to Cache

1. **GET requests**: Cache responses from GET requests, as they typically return the same data for the same parameters
2. **Rarely changing data**: Cache data that doesn't change frequently
3. **Expensive operations**: Cache responses from operations that are computationally expensive or have high latency

### Caching Strategies

1. **Time-based caching**: Cache data for a fixed period
2. **Conditional caching**: Use ETag or Last-Modified headers to validate cache freshness
3. **Hierarchical caching**: Cache different data for different durations

### Implementing Caching with WordPress Transients

WordPress transients provide a simple way to cache API responses:

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
    $data = $this->get($endpoint, $params, false);
    
    // Cache the data
    set_transient($cache_key, $data, $cache_time);
    
    return $data;
}
```

### Cache Invalidation

It's important to invalidate cache when data changes:

```php
/**
 * Invalidate cache for an endpoint
 *
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 */
public function invalidate_cache($endpoint, $params = []) {
    $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
    delete_transient($cache_key);
}
```

### Dynamic Cache Duration

Adjust cache duration based on data volatility:

```php
/**
 * Get cache duration for an endpoint
 *
 * @param string $endpoint API endpoint
 * @return int Cache duration in seconds
 */
private function get_cache_duration($endpoint) {
    $durations = [
        'user' => 60,           // User data: 1 minute
        'posts' => 300,         // Posts: 5 minutes
        'comments' => 180,      // Comments: 3 minutes
        'settings' => 3600,     // Settings: 1 hour
        'static' => 86400       // Static data: 24 hours
    ];
    
    foreach ($durations as $key => $duration) {
        if (strpos($endpoint, $key) !== false) {
            return $duration;
        }
    }
    
    return 300; // Default: 5 minutes
}
```

## Synchronizing Data between MainWP and Third-Party Services

One of the most common tasks in MainWP integrations is synchronizing data between MainWP and third-party services. Here's how to implement effective synchronization:

### Sync Strategies

1. **Pull-based sync**: MainWP pulls data from the third-party service
2. **Push-based sync**: MainWP pushes data to the third-party service
3. **Bidirectional sync**: Data flows in both directions
4. **Webhook-based sync**: Third-party service notifies MainWP of changes via webhooks

### Implementing Pull-Based Sync

Pull-based sync is the simplest approach and works well for most integrations:

```php
/**
 * Sync data from third-party service to MainWP
 *
 * @param int $website_id MainWP website ID
 * @return bool Whether the sync was successful
 */
public function sync_from_service($website_id) {
    // Get website details
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return false;
    }
    
    try {
        // Get data from third-party service
        $data = $this->api_client->get('sites/' . urlencode($website->url));
        
        // Process and store the data
        update_option('my_integration_data_' . $website_id, $data);
        update_option('my_integration_last_sync_' . $website_id, time());
        
        return true;
    } catch (Exception $e) {
        error_log('Sync Error: ' . $e->getMessage());
        return false;
    }
}
```

### Implementing Push-Based Sync

Push-based sync is useful when MainWP has data that needs to be sent to the third-party service:

```php
/**
 * Sync data from MainWP to third-party service
 *
 * @param int $website_id MainWP website ID
 * @param array $data Data to sync
 * @return bool Whether the sync was successful
 */
public function sync_to_service($website_id, $data) {
    // Get website details
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return false;
    }
    
    try {
        // Send data to third-party service
        $response = $this->api_client->post('sites/' . urlencode($website->url), $data);
        
        // Store sync timestamp
        update_option('my_integration_last_push_' . $website_id, time());
        
        return true;
    } catch (Exception $e) {
        error_log('Sync Error: ' . $e->getMessage());
        return false;
    }
}
```

### Implementing Bidirectional Sync

Bidirectional sync is more complex and requires conflict resolution:

```php
/**
 * Perform bidirectional sync between MainWP and third-party service
 *
 * @param int $website_id MainWP website ID
 * @return bool Whether the sync was successful
 */
public function bidirectional_sync($website_id) {
    // Get website details
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return false;
    }
    
    // Get last sync timestamp
    $last_sync = get_option('my_integration_last_sync_' . $website_id, 0);
    
    try {
        // Get data from third-party service that has changed since last sync
        $service_data = $this->api_client->get('sites/' . urlencode($website->url) . '/changes', [
            'since' => $last_sync
        ]);
        
        // Get local data that has changed since last sync
        $local_data = $this->get_local_changes($website_id, $last_sync);
        
        // Resolve conflicts
        $resolved_data = $this->resolve_conflicts($service_data, $local_data);
        
        // Update local data
        $this->update_local_data($website_id, $resolved_data['local_updates']);
        
        // Update service data
        $this->api_client->post('sites/' . urlencode($website->url) . '/batch-update', $resolved_data['service_updates']);
        
        // Update sync timestamp
        update_option('my_integration_last_sync_' . $website_id, time());
        
        return true;
    } catch (Exception $e) {
        error_log('Sync Error: ' . $e->getMessage());
        return false;
    }
}

/**
 * Resolve conflicts between local and service data
 *
 * @param array $service_data Data from third-party service
 * @param array $local_data Data from MainWP
 * @return array Resolved data
 */
private function resolve_conflicts($service_data, $local_data) {
    $local_updates = [];
    $service_updates = [];
    
    // Compare and resolve conflicts
    foreach ($service_data as $key => $service_item) {
        if (isset($local_data[$key])) {
            // Conflict: both sides have changes
            $local_item = $local_data[$key];
            
            // Resolve based on timestamp (newer wins)
            if ($service_item['updated_at'] > $local_item['updated_at']) {
                $local_updates[$key] = $service_item;
            } else {
                $service_updates[$key] = $local_item;
            }
            
            // Remove from local data to mark as processed
            unset($local_data[$key]);
        } else {
            // No conflict: only service has changes
            $local_updates[$key] = $service_item;
        }
    }
    
    // Remaining local data needs to be sent to service
    foreach ($local_data as $key => $local_item) {
        $service_updates[$key] = $local_item;
    }
    
    return [
        'local_updates' => $local_updates,
        'service_updates' => $service_updates
    ];
}
```

### Implementing Webhook-Based Sync

Webhook-based sync is efficient for real-time updates:

```php
/**
 * Register webhook endpoint
 */
public function register_webhook_endpoint() {
    add_action('rest_api_init', function() {
        register_rest_route('my-integration/v1', '/webhook', [
            'methods' => 'POST',
            'callback' => [$this, 'process_webhook'],
            'permission_callback' => [$this, 'verify_webhook']
        ]);
    });
}

/**
 * Verify webhook request
 *
 * @param WP_REST_Request $request REST request
 * @return bool Whether the request is valid
 */
public function verify_webhook($request) {
    // Get signature from header
    $signature = $request->get_header('X-Webhook-Signature');
    if (empty($signature)) {
        return false;
    }
    
    // Get webhook secret
    $secret = get_option('my_integration_webhook_secret', '');
    if (empty($secret)) {
        return false;
    }
    
    // Get request body
    $body = $request->get_body();
    
    // Calculate expected signature
    $expected_signature = hash_hmac('sha256', $body, $secret);
    
    // Compare signatures
    return hash_equals($expected_signature, $signature);
}

/**
 * Process webhook request
 *
 * @param WP_REST_Request $request REST request
 * @return WP_REST_Response REST response
 */
public function process_webhook($request) {
    // Get request data
    $data = $request->get_json_params();
    
    // Process webhook data
    $event_type = $data['event_type'] ?? '';
    $resource_id = $data['resource_id'] ?? '';
    
    switch ($event_type) {
        case 'site.updated':
            // Find MainWP website ID from resource ID
            $website_id = $this->get_website_id_from_resource_id($resource_id);
            if ($website_id) {
                // Sync data from service
                $this->sync_from_service($website_id);
            }
            break;
        
        case 'site.deleted':
            // Handle site deletion
            $website_id = $this->get_website_id_from_resource_id($resource_id);
            if ($website_id) {
                delete_option('my_integration_data_' . $website_id);
            }
            break;
        
        // Handle other event types
    }
    
    return new WP_REST_Response(['status' => 'success'], 200);
}
```

### Scheduling Regular Syncs

For data that doesn't need real-time updates, schedule regular syncs:

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

## Security Considerations

Security is critical when working with third-party APIs. Here are some best practices:

### Secure Storage of API Credentials

Never hardcode API credentials in your code. Instead, store them securely:

```php
/**
 * Save API credentials
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
 * Encrypt API secret
 *
 * @param string $secret API secret
 * @return string Encrypted secret
 */
private function encrypt_secret($secret) {
    // Get encryption key
    $encryption_key = $this->get_encryption_key();
    
    // Generate random initialization vector
    $iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length('aes-256-cbc'));
    
    // Encrypt secret
    $encrypted = openssl_encrypt($secret, 'aes-256-cbc', $encryption_key, 0, $iv);
    
    // Combine IV and encrypted data
    $combined = base64_encode($iv . $encrypted);
    
    return $combined;
}

/**
 * Decrypt API secret
 *
 * @param string $encrypted_secret Encrypted secret
 * @return string Decrypted secret
 */
private function decrypt_secret($encrypted_secret) {
    // Get encryption key
    $encryption_key = $this->get_encryption_key();
    
    // Decode combined data
    $combined = base64_decode($encrypted_secret);
    
    // Extract IV and encrypted data
    $iv_length = openssl_cipher_iv_length('aes-256-cbc');
    $iv = substr($combined, 0, $iv_length);
    $encrypted = substr($combined, $iv_length);
    
    // Decrypt secret
    $secret = openssl_decrypt($encrypted, 'aes-256-cbc', $encryption_key, 0, $iv);
    
    return $secret;
}

/**
 * Get encryption key
 *
 * @return string Encryption key
 */
private function get_encryption_key() {
    // Use WordPress salt as encryption key
    if (defined('AUTH_KEY')) {
        return AUTH_KEY;
    }
    
    // Fallback to a default key (not recommended)
    return 'default-encryption-key';
}
```

### Secure Communication

Always use HTTPS for API communication:

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

### Input Validation

Validate all input before sending it to the API:

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

### Rate Limit Protection

Implement rate limit protection to prevent abuse:

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

Verify webhook signatures to prevent spoofing:

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

## Testing API Integrations

Thorough testing is essential for reliable API integrations. Here's how to test your integration:

### Unit Testing API Client

Create unit tests for your API client:

```php
class ApiClientTest extends WP_UnitTestCase {
    private $api_client;
    
    public function setUp() {
        parent::setUp();
        
        // Create API client with test credentials
        $this->api_client = new ThirdPartyApiClient('test_api_key', 'https://api.example.com/v1/');
    }
    
    public function test_get_request() {
        // Mock response
        add_filter('pre_http_request', function($preempt, $args, $url) {
            if (strpos($url, 'https://api.example.com/v1/test') !== false) {
                return [
                    'response' => ['code' => 200],
                    'body' => json_encode(['success' => true])
                ];
            }
            
            return $preempt;
        }, 10, 3);
        
        // Make request
        $response = $this->api_client->get('test');
        
        // Assert response
        $this->assertTrue($response['success']);
    }
    
    public function test_error_handling() {
        // Mock response
        add_filter('pre_http_request', function($preempt, $args, $url) {
            if (strpos($url, 'https://api.example.com/v1/error') !== false) {
                return [
                    'response' => ['code' => 400],
                    'body' => json_encode(['message' => 'Bad request'])
                ];
            }
            
            return $preempt;
        }, 10, 3);
        
        // Expect exception
        $this->expectException(ApiClientException::class);
        
        // Make request
        $this->api_client->get('error');
    }
}
```

### Integration Testing

Test the integration with the actual API:

```php
class IntegrationTest extends WP_UnitTestCase {
    private $integration;
    
    public function setUp() {
        parent::setUp();
        
        // Create integration with test credentials
        $this->integration = new MyIntegration();
        $this->integration->set_test_mode(true);
    }
    
    public function test_sync_from_service() {
        // Create test website
        $website_id = $this->create_test_website();
        
        // Sync data
        $result = $this->integration->sync_from_service($website_id);
        
        // Assert result
        $this->assertTrue($result);
        
        // Assert data was saved
        $data = get_option('my_integration_data_' . $website_id);
        $this->assertNotEmpty($data);
    }
    
    private function create_test_website() {
        // Create test website in MainWP
        $website_id = MainWP\Dashboard\MainWP_DB::instance()->add_website([
            'name' => 'Test Website',
            'url' => 'https://test.example.com'
        ]);
        
        return $website_id;
    }
}
```

### Manual Testing

Create a testing checklist:

1. **Authentication**: Test all authentication methods
2. **API Operations**: Test all API operations (GET, POST, PUT, DELETE)
3. **Error Handling**: Test error scenarios (network errors, API errors)
4. **Rate Limiting**: Test rate limit handling
5. **Caching**: Test caching behavior
6. **Synchronization**: Test data synchronization
7. **Security**: Test security measures

### Testing Tools

Use these tools for API testing:

1. **Postman**: Test API endpoints manually
2. **Charles Proxy**: Inspect API requests and responses
3. **WP_UnitTestCase**: Create automated tests
4. **WP CLI**: Test from the command line

## Debugging API Issues

When things go wrong, use these debugging techniques:

### Logging API Requests and Responses

```php
/**
 * Log API request and response
 *
 * @param string $method HTTP method
 * @param string $url Request URL
 * @param array $args Request arguments
 * @param array|WP_Error $response Response
 */
private function log_request($method, $url, $args, $response) {
    // Check if debugging is enabled
    if (!$this->debug_mode) {
        return;
    }
    
    // Prepare log data
    $log = [
        'time' => current_time('mysql'),
        'method' => $method,
        'url' => $url,
        'args' => $args
    ];
    
    // Add response data
    if (is_wp_error($response)) {
        $log['error'] = $response->get_error_message();
    } else {
        $log['status'] = wp_remote_retrieve_response_code($response);
        $log['body'] = wp_remote_retrieve_body($response);
    }
    
    // Get existing logs
    $logs = get_option('my_integration_api_logs', []);
    
    // Add new log
    array_unshift($logs, $log);
    
    // Limit logs to 100 entries
    $logs = array_slice($logs, 0, 100);
    
    // Save logs
    update_option('my_integration_api_logs', $logs);
}
```

### Creating a Debug Mode

```php
/**
 * Enable debug mode
 *
 * @param bool $enable Whether to enable debug mode
 */
public function set_debug_mode($enable = true) {
    $this->debug_mode = $enable;
    update_option('my_integration_debug_mode', $enable);
}

/**
 * Check if debug mode is enabled
 *
 * @return bool Whether debug mode is enabled
 */
public function is_debug_mode() {
    return $this->debug_mode;
}
```

### Displaying Debug Information

```php
/**
 * Render debug information
 */
public function render_debug_info() {
    // Check if user has permission
    if (!current_user_can('manage_options')) {
        return;
    }
    
    // Check if debug mode is enabled
    if (!$this->is_debug_mode()) {
        ?>
        <div class="ui segment">
            <h3><?php esc_html_e('Debug Mode', 'my-integration'); ?></h3>
            <p><?php esc_html_e('Debug mode is disabled.', 'my-integration'); ?></p>
            <form method="post" action="">
                <?php wp_nonce_field('my_integration_debug_mode', 'my_integration_debug_mode_nonce'); ?>
                <button class="ui green button" type="submit" name="enable_debug_mode">
                    <?php esc_html_e('Enable Debug Mode', 'my-integration'); ?>
                </button>
            </form>
        </div>
        <?php
        return;
    }
    
    // Get API logs
    $logs = get_option('my_integration_api_logs', []);
    
    ?>
    <div class="ui segment">
        <h3><?php esc_html_e('Debug Mode', 'my-integration'); ?></h3>
        <p><?php esc_html_e('Debug mode is enabled.', 'my-integration'); ?></p>
        <form method="post" action="">
            <?php wp_nonce_field('my_integration_debug_mode', 'my_integration_debug_mode_nonce'); ?>
            <button class="ui red button" type="submit" name="disable_debug_mode">
                <?php esc_html_e('Disable Debug Mode', 'my-integration'); ?>
            </button>
        </form>
    </div>
    
    <div class="ui segment">
        <h3><?php esc_html_e('API Logs', 'my-integration'); ?></h3>
        
        <?php if (empty($logs)) : ?>
            <p><?php esc_html_e('No API logs found.', 'my-integration'); ?></p>
        <?php else : ?>
            <table class="ui celled table">
                <thead>
                    <tr>
                        <th><?php esc_html_e('Time', 'my-integration'); ?></th>
                        <th><?php esc_html_e('Method', 'my-integration'); ?></th>
                        <th><?php esc_html_e('URL', 'my-integration'); ?></th>
                        <th><?php esc_html_e('Status', 'my-integration'); ?></th>
                        <th><?php esc_html_e('Details', 'my-integration'); ?></th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($logs as $log) : ?>
                        <tr>
                            <td><?php echo esc_html($log['time']); ?></td>
                            <td><?php echo esc_html($log['method']); ?></td>
                            <td><?php echo esc_html($log['url']); ?></td>
                            <td>
                                <?php if (isset($log['error'])) : ?>
                                    <span class="ui red label">Error</span>
                                <?php else : ?>
                                    <span class="ui <?php echo $log['status'] < 400 ? 'green' : 'red'; ?> label">
                                        <?php echo esc_html($log['status']); ?>
                                    </span>
                                <?php endif; ?>
                            </td>
                            <td>
                                <button class="ui tiny button toggle-details">
                                    <?php esc_html_e('Show Details', 'my-integration'); ?>
                                </button>
                                <div class="ui segment details" style="display: none;">
                                    <h4><?php esc_html_e('Request', 'my-integration'); ?></h4>
                                    <pre><?php echo esc_html(json_encode($log['args'], JSON_PRETTY_PRINT)); ?></pre>
                                    
                                    <h4><?php esc_html_e('Response', 'my-integration'); ?></h4>
                                    <?php if (isset($log['error'])) : ?>
                                        <pre><?php echo esc_html($log['error']); ?></pre>
                                    <?php else : ?>
                                        <pre><?php echo esc_html($log['body']); ?></pre>
                                    <?php endif; ?>
                                </div>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
            
            <form method="post" action="">
                <?php wp_nonce_field('my_integration_clear_logs', 'my_integration_clear_logs_nonce'); ?>
                <button class="ui red button" type="submit" name="clear_logs">
                    <?php esc_html_e('Clear Logs', 'my-integration'); ?>
                </button>
            </form>
            
            <script type="text/javascript">
            jQuery(document).ready(function($) {
                $('.toggle-details').on('click', function() {
                    var $button = $(this);
                    var $details = $button.next('.details');
                    
                    $details.toggle();
                    
                    if ($details.is(':visible')) {
                        $button.text('<?php esc_html_e('Hide Details', 'my-integration'); ?>');
                    } else {
                        $button.text('<?php esc_html_e('Show Details', 'my-integration'); ?>');
                    }
                });
            });
            </script>
        <?php endif; ?>
    </div>
    <?php
}
```

### Troubleshooting Common API Issues

1. **Authentication Errors**:
   - Check API credentials
   - Verify authentication method
   - Check for expired tokens

2. **Rate Limiting**:
   - Implement caching
   - Add exponential backoff
   - Reduce unnecessary API calls

3. **Network Issues**:
   - Check internet connectivity
   - Verify API endpoint URL
   - Check for firewall or proxy issues

4. **Data Format Issues**:
   - Validate request data
   - Check response parsing
   - Verify content types

## Related Resources

- [Creating a Basic Integration](create-basic-integration.md)
- [Using MainWP Actions & Filters](actions-filters.md)
- [API Integration Best Practices](../best-practices/api-integration.md)
- [Third-Party API Integration Patterns](../reference/api-integration-patterns.md)
- [WordPress HTTP API Documentation](https://developer.wordpress.org/plugins/http-api/)
- [OAuth 2.0 Documentation](https://oauth.net/2
# Working with Third-Party APIs in MainWP Integrations

This guide provides comprehensive information on working with third-party APIs in MainWP integrations. You'll learn how to design robust API clients, handle authentication, manage errors, implement caching, and more.

## Quick Start for Experienced Developers

```php
// 1. Create a reusable API client class
class ThirdPartyApiClient {
    private $api_key;
    private $api_url = 'https://api.third-party-service.com/v1/';
    private $timeout = 30;
    
    public function __construct($api_key) {
        $this->api_key = $api_key;
    }
    
    public function get($endpoint, $params = []) {
        return $this->request('GET', $endpoint, $params);
    }
    
    public function post($endpoint, $data = []) {
        return $this->request('POST', $endpoint, [], $data);
    }
    
    private function request($method, $endpoint, $params = [], $data = null) {
        $url = $this->api_url . $endpoint;
        $cache_key = 'tpapi_' . md5($method . $url . serialize($params) . serialize($data));
        
        // Check cache for GET requests
        if ($method === 'GET') {
            $cached = get_transient($cache_key);
            if (false !== $cached) {
                return $cached;
            }
        }
        
        // Prepare request
        $args = [
            'method' => $method,
            'headers' => [
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json',
                'Accept' => 'application/json'
            ],
            'timeout' => $this->timeout
        ];
        
        // Add query parameters
        if (!empty($params)) {
            $url = add_query_arg($params, $url);
        }
        
        // Add body data for POST/PUT/PATCH
        if ($data !== null && in_array($method, ['POST', 'PUT', 'PATCH'])) {
            $args['body'] = json_encode($data);
        }
        
        // Make request
        $response = wp_remote_request($url, $args);
        
        // Handle errors
        if (is_wp_error($response)) {
            throw new Exception('API request failed: ' . $response->get_error_message());
        }
        
        $status_code = wp_remote_retrieve_response_code($response);
        $body = wp_remote_retrieve_body($response);
        $result = json_decode($body, true);
        
        // Handle API errors
        if ($status_code >= 400) {
            $error_message = isset($result['message']) ? $result['message'] : 'Unknown API error';
            throw new Exception("API error ($status_code): $error_message");
        }
        
        // Cache successful GET responses
        if ($method === 'GET') {
            set_transient($cache_key, $result, 5 * MINUTE_IN_SECONDS);
        }
        
        return $result;
    }
}

// 2. Use the API client in your MainWP integration
class MyIntegration {
    private $api_client;
    
    public function __construct() {
        // Initialize API client
        $api_key = get_option('my_integration_api_key', '');
        if (!empty($api_key)) {
            $this->api_client = new ThirdPartyApiClient($api_key);
        }
        
        // Hook into MainWP
        add_action('mainwp_site_synced', [$this, 'sync_third_party_data'], 10, 2);
    }
    
    public function sync_third_party_data($website, $data) {
        if (!$this->api_client) {
            return;
        }
        
        try {
            // Get data from third-party API
            $api_data = $this->api_client->get('sites/' . urlencode($website->url));
            
            // Store the data for this site
            update_option('my_integration_data_' . $website->id, $api_data);
            update_option('my_integration_last_sync_' . $website->id, time());
        } catch (Exception $e) {
            // Log error but continue
            error_log('API Error: ' . $e->getMessage());
        }
    }
}
```

## Designing a Robust API Client

A well-designed API client is the foundation of any successful third-party integration. It should handle authentication, requests, responses, errors, and caching in a consistent way.

### Basic API Client Structure

Here's a comprehensive API client class that you can adapt for your integration:

```php
class ThirdPartyApiClient {
    private $api_key;
    private $api_url;
    private $timeout = 30;
    private $last_response;
    private $last_request;
    
    /**
     * Constructor
     *
     * @param string $api_key API key or token
     * @param string $api_url Base API URL
     */
    public function __construct($api_key, $api_url = 'https://api.third-party-service.com/v1/') {
        $this->api_key = $api_key;
        $this->api_url = $api_url;
    }
    
    /**
     * Make a GET request
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param bool $cache Whether to cache the response
     * @param int $cache_time Cache time in seconds
     * @return array|object Response data
     */
    public function get($endpoint, $params = [], $cache = true, $cache_time = 300) {
        return $this->request('GET', $endpoint, $params, null, $cache, $cache_time);
    }
    
    /**
     * Make a POST request
     *
     * @param string $endpoint API endpoint
     * @param array $data Post data
     * @param array $params Query parameters
     * @return array|object Response data
     */
    public function post($endpoint, $data = [], $params = []) {
        return $this->request('POST', $endpoint, $params, $data);
    }
    
    /**
     * Make a PUT request
     *
     * @param string $endpoint API endpoint
     * @param array $data Put data
     * @param array $params Query parameters
     * @return array|object Response data
     */
    public function put($endpoint, $data = [], $params = []) {
        return $this->request('PUT', $endpoint, $params, $data);
    }
    
    /**
     * Make a DELETE request
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @return array|object Response data
     */
    public function delete($endpoint, $params = []) {
        return $this->request('DELETE', $endpoint, $params);
    }
    
    /**
     * Make an API request
     *
     * @param string $method HTTP method
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param array $data Request body data
     * @param bool $cache Whether to cache the response
     * @param int $cache_time Cache time in seconds
     * @return array|object Response data
     * @throws Exception If the request fails
     */
    private function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300) {
        $url = $this->api_url . ltrim($endpoint, '/');
        $cache_key = 'tpapi_' . md5($method . $url . serialize($params) . serialize($data));
        
        // Check cache for GET requests
        if ($method === 'GET' && $cache) {
            $cached = get_transient($cache_key);
            if (false !== $cached) {
                return $cached;
            }
        }
        
        // Prepare request
        $args = [
            'method' => $method,
            'headers' => [
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json',
                'Accept' => 'application/json'
            ],
            'timeout' => $this->timeout
        ];
        
        // Add query parameters
        if (!empty($params)) {
            $url = add_query_arg($params, $url);
        }
        
        // Add body data for POST/PUT/PATCH
        if ($data !== null && in_array($method, ['POST', 'PUT', 'PATCH'])) {
            $args['body'] = json_encode($data);
        }
        
        // Store request for debugging
        $this->last_request = [
            'url' => $url,
            'method' => $method,
            'args' => $args
        ];
        
        // Make request
        $response = wp_remote_request($url, $args);
        $this->last_response = $response;
        
        // Handle connection errors
        if (is_wp_error($response)) {
            throw new Exception('API request failed: ' . $response->get_error_message());
        }
        
        $status_code = wp_remote_retrieve_response_code($response);
        $body = wp_remote_retrieve_body($response);
        $result = json_decode($body, true);
        
        // Handle API errors
        if ($status_code >= 400) {
            $error_message = isset($result['message']) ? $result['message'] : 'Unknown API error';
            throw new Exception("API error ($status_code): $error_message", $status_code);
        }
        
        // Cache successful GET responses
        if ($method === 'GET' && $cache) {
            set_transient($cache_key, $result, $cache_time);
        }
        
        return $result;
    }
    
    /**
     * Get the last response
     *
     * @return array|WP_Error Last response
     */
    public function get_last_response() {
        return $this->last_response;
    }
    
    /**
     * Get the last request
     *
     * @return array Last request
     */
    public function get_last_request() {
        return $this->last_request;
    }
    
    /**
     * Test the API connection
     *
     * @return bool Whether the connection is successful
     */
    public function test_connection() {
        try {
            // Replace 'test-endpoint' with an actual lightweight endpoint from your API
            $this->get('test-endpoint', [], false);
            return true;
        } catch (Exception $e) {
            return false;
        }
    }
}
```

### Key Features to Include

When designing your API client, consider including these features:

1. **Method-specific functions**: Create dedicated methods for GET, POST, PUT, DELETE, etc.
2. **Consistent error handling**: Throw exceptions with meaningful messages
3. **Response caching**: Cache GET responses to reduce API calls
4. **Request/response logging**: Store the last request and response for debugging
5. **Configurable timeouts**: Allow adjustment of request timeouts
6. **Connection testing**: Include a method to test the API connection

## Authentication Methods

Different APIs use different authentication methods. Here's how to implement the most common ones:

### API Key Authentication

Many APIs use API keys, either in the header or as a query parameter:

```php
// API key in header
$args = [
    'headers' => [
        'X-API-Key' => $this->api_key
    ]
];

// API key in query parameter
$url = add_query_arg(['api_key' => $this->api_key], $url);
```

### Bearer Token Authentication

Bearer tokens (including JWT) are typically sent in the Authorization header:

```php
$args = [
    'headers' => [
        'Authorization' => 'Bearer ' . $this->api_token
    ]
];
```

### Basic Authentication

Basic authentication uses base64-encoded username and password:

```php
$args = [
    'headers' => [
        'Authorization' => 'Basic ' . base64_encode($this->username . ':' . $this->password)
    ]
];
```

### OAuth 2.0 Authentication

OAuth 2.0 is more complex and typically involves:

1. Redirecting the user to the authorization server
2. Receiving an authorization code
3. Exchanging the code for access and refresh tokens
4. Using the access token for API requests
5. Refreshing the access token when it expires

Here's a simplified implementation:

```php
class OAuth2Client extends ThirdPartyApiClient {
    private $client_id;
    private $client_secret;
    private $redirect_uri;
    private $auth_url;
    private $token_url;
    private $access_token;
    private $refresh_token;
    private $token_expires;
    
    public function __construct($client_id, $client_secret, $redirect_uri, $auth_url, $token_url, $api_url) {
        $this->client_id = $client_id;
        $this->client_secret = $client_secret;
        $this->redirect_uri = $redirect_uri;
        $this->auth_url = $auth_url;
        $this->token_url = $token_url;
        
        // Load tokens from options
        $this->access_token = get_option('my_integration_access_token', '');
        $this->refresh_token = get_option('my_integration_refresh_token', '');
        $this->token_expires = get_option('my_integration_token_expires', 0);
        
        parent::__construct($this->access_token, $api_url);
    }
    
    /**
     * Get the authorization URL
     *
     * @param array $scope API scopes to request
     * @param string $state State parameter for security
     * @return string Authorization URL
     */
    public function get_auth_url($scope = [], $state = '') {
        $params = [
            'client_id' => $this->client_id,
            'redirect_uri' => $this->redirect_uri,
            'response_type' => 'code',
            'state' => $state ?: wp_create_nonce('oauth2_state')
        ];
        
        if (!empty($scope)) {
            $params['scope'] = implode(' ', $scope);
        }
        
        return add_query_arg($params, $this->auth_url);
    }
    
    /**
     * Exchange authorization code for tokens
     *
     * @param string $code Authorization code
     * @return bool Whether the exchange was successful
     */
    public function exchange_code_for_tokens($code) {
        $args = [
            'method' => 'POST',
            'headers' => [
                'Content-Type' => 'application/x-www-form-urlencoded'
            ],
            'body' => [
                'grant_type' => 'authorization_code',
                'code' => $code,
                'client_id' => $this->client_id,
                'client_secret' => $this->client_secret,
                'redirect_uri' => $this->redirect_uri
            ]
        ];
        
        $response = wp_remote_post($this->token_url, $args);
        
        if (is_wp_error($response)) {
            return false;
        }
        
        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);
        
        if (empty($data['access_token'])) {
            return false;
        }
        
        // Save tokens
        $this->access_token = $data['access_token'];
        $this->refresh_token = $data['refresh_token'] ?? '';
        $this->token_expires = time() + ($data['expires_in'] ?? 3600);
        
        update_option('my_integration_access_token', $this->access_token);
        update_option('my_integration_refresh_token', $this->refresh_token);
        update_option('my_integration_token_expires', $this->token_expires);
        
        return true;
    }
    
    /**
     * Refresh the access token
     *
     * @return bool Whether the refresh was successful
     */
    public function refresh_access_token() {
        if (empty($this->refresh_token)) {
            return false;
        }
        
        $args = [
            'method' => 'POST',
            'headers' => [
                'Content-Type' => 'application/x-www-form-urlencoded'
            ],
            'body' => [
                'grant_type' => 'refresh_token',
                'refresh_token' => $this->refresh_token,
                'client_id' => $this->client_id,
                'client_secret' => $this->client_secret
            ]
        ];
        
        $response = wp_remote_post($this->token_url, $args);
        
        if (is_wp_error($response)) {
            return false;
        }
        
        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);
        
        if (empty($data['access_token'])) {
            return false;
        }
        
        // Save tokens
        $this->access_token = $data['access_token'];
        if (!empty($data['refresh_token'])) {
            $this->refresh_token = $data['refresh_token'];
            update_option('my_integration_refresh_token', $this->refresh_token);
        }
        $this->token_expires = time() + ($data['expires_in'] ?? 3600);
        
        update_option('my_integration_access_token', $this->access_token);
        update_option('my_integration_token_expires', $this->token_expires);
        
        return true;
    }
    
    /**
     * Override request method to handle token refresh
     */
    protected function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300) {
        // Check if token is expired and refresh if needed
        if (time() > $this->token_expires - 60) {
            $this->refresh_access_token();
        }
        
        // Update the access token in the parent class
        $this->api_key = $this->access_token;
        
        return parent::request($method, $endpoint, $params, $data, $cache, $cache_time);
    }
}
```

To use this OAuth2 client in your MainWP integration:

```php
// In your admin page
public function render_auth_page() {
    $client_id = get_option('my_integration_client_id', '');
    $client_secret = get_option('my_integration_client_secret', '');
    $redirect_uri = admin_url('admin.php?page=MyIntegrationAuth');
    
    $oauth_client = new OAuth2Client(
        $client_id,
        $client_secret,
        $redirect_uri,
        'https://service.com/oauth/authorize',
        'https://service.com/oauth/token',
        'https://api.service.com/v1/'
    );
    
    // Handle authorization code callback
    if (isset($_GET['code']) && isset($_GET['state'])) {
        $code = sanitize_text_field($_GET['code']);
        $state = sanitize_text_field($_GET['state']);
        
        // Verify state to prevent CSRF
        if (!wp_verify_nonce($state, 'oauth2_state')) {
            ?>
            <div class="ui red message"><?php esc_html_e('Invalid state parameter. Please try again.', 'my-integration'); ?></div>
            <?php
            return;
        }
        
        if ($oauth_client->exchange_code_for_tokens($code)) {
            ?>
            <div class="ui green message"><?php esc_html_e('Successfully authenticated with the service.', 'my-integration'); ?></div>
            <?php
        } else {
            ?>
            <div class="ui red message"><?php esc_html_e('Failed to authenticate with the service.', 'my-integration'); ?></div>
            <?php
        }
    }
    
    // Display auth button if not authenticated
    if (empty(get_option('my_integration_access_token', ''))) {
        $auth_url = $oauth_client->get_auth_url(['read', 'write']);
        ?>
        <a href="<?php echo esc_url($auth_url); ?>" class="ui green button">
            <?php esc_html_e('Connect to Service', 'my-integration'); ?>
        </a>
        <?php
    } else {
        ?>
        <div class="ui green message"><?php esc_html_e('Connected to service.', 'my-integration'); ?></div>
        <a href="<?php echo esc_url(admin_url('admin.php?page=MyIntegrationAuth&disconnect=1')); ?>" class="ui red button">
            <?php esc_html_e('Disconnect from Service', 'my-integration'); ?>
        </a>
        <?php
    }
}
```

## Error Handling and Retry Strategies

Robust error handling is essential for reliable API integrations. Here's a comprehensive approach:

### Error Types to Handle

1. **Connection errors**: Network issues, timeouts
2. **Authentication errors**: Invalid or expired credentials
3. **Rate limiting**: Too many requests
4. **Server errors**: 5xx responses
5. **Client errors**: 4xx responses
6. **Parsing errors**: Invalid JSON responses

### Implementing Error Handling

Here's an enhanced version of the request method with comprehensive error handling:

```php
/**
 * Make an API request with error handling and retries
 *
 * @param string $method HTTP method
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 * @param array $data Request body data
 * @param bool $cache Whether to cache the response
 * @param int $cache_time Cache time in seconds
 * @param int $retry_count Number of retry attempts
 * @return array|object Response data
 * @throws ApiConnectionException If the connection fails
 * @throws ApiAuthException If authentication fails
 * @throws ApiRateLimitException If rate limited
 * @throws ApiServerException If the server returns an error
 * @throws ApiClientException If the client makes an invalid request
 */
private function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300, $retry_count = 0) {
    $url = $this->api_url . ltrim($endpoint, '/');
    $cache_key = 'tpapi_' . md5($method . $url . serialize($params) . serialize($data));
    
    // Check cache for GET requests
    if ($method === 'GET' && $cache) {
        $cached = get_transient($cache_key);
        if (false !== $cached) {
            return $cached;
        }
    }
    
    // Prepare request
    $args = [
        'method' => $method,
        'headers' => [
            'Authorization' => 'Bearer ' . $this->api_key,
            'Content-Type' => 'application/json',
            'Accept' => 'application/json'
        ],
        'timeout' => $this->timeout
    ];
    
    // Add query parameters
    if (!empty($params)) {
        $url = add_query_arg($params, $url);
    }
    
    // Add body data for POST/PUT/PATCH
    if ($data !== null && in_array($method, ['POST', 'PUT', 'PATCH'])) {
        $args['body'] = json_encode($data);
    }
    
    // Store request for debugging
    $this->last_request = [
        'url' => $url,
        'method' => $method,
        'args' => $args
    ];
    
    // Make request
    $response = wp_remote_request($url, $args);
    $this->last_response = $response;
    
    // Handle connection errors
    if (is_wp_error($response)) {
        $error_message = $response->get_error_message();
        
        // Check if we should retry
        if ($retry_count < $this->max_retries) {
            // Exponential backoff: 1s, 2s, 4s, 8s, etc.
            $backoff = pow(2, $retry_count);
            sleep($backoff);
            return $this->request($method, $endpoint, $params, $data, $cache, $cache_time, $retry_count + 1);
        }
        
        throw new ApiConnectionException('API connection failed: ' . $error_message);
    }
    
    $status_code = wp_remote_retrieve_response_code($response);
    $body = wp_remote_retrieve_body($response);
    
    // Try to parse JSON response
    $result = json_decode($body, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        // Not JSON or invalid JSON
        $result = ['raw_response' => $body];
    }
    
    // Handle different error types
    if ($status_code >= 400) {
        $error_message = isset($result['message']) ? $result['message'] : 'Unknown API error';
        
        // Authentication errors
        if ($status_code === 401) {
            throw new ApiAuthException("Authentication failed: $error_message", $status_code);
        }
        
        // Rate limiting
        if ($status_code === 429) {
            // Get retry-after header if available
            $retry_after = wp_remote_retrieve_header($response, 'retry-after');
            $retry_after = $retry_after ? (int)$retry_after : 60;
            
            // Check if we should retry
            if ($retry_count < $this->max_retries) {
                sleep($retry_after);
                return $this->request($method, $endpoint, $params, $data, $cache, $cache_time, $retry_count + 1);
            }
            
            throw new ApiRateLimitException("Rate limit exceeded: $error_message", $status_code, $retry_after);
        }
        
        // Server errors
        if ($status_code >= 500) {
            // Check if we should retry
            if ($retry_count < $this->max_retries) {
                // Exponential backoff
                $backoff = pow(2, $retry_count);
                sleep($backoff);
                return $this->request($method, $endpoint, $params, $data, $cache, $cache_time, $retry_count + 1);
            }
            
            throw new ApiServerException("Server error ($status_code): $error_message", $status_code);
        }
        
        // Client errors
        throw new ApiClientException("Client error ($status_code): $error_message", $status_code);
    }
    
    // Cache successful GET responses
    if ($method === 'GET' && $cache) {
        set_transient($cache_key, $result, $cache_time);
    }
    
    return $result;
}
```

### Custom Exception Classes

Create custom exception classes for different error types:

```php
class ApiException extends Exception {
    protected $status_code;
    
    public function __construct($message, $status_code = 0, $code = 0) {
        $this->status_code = $status_code;
        parent::__construct($message, $code);
    }
    
    public function getStatusCode() {
        return $this->status_code;
    }
}

class ApiConnectionException extends ApiException {}
class ApiAuthException extends ApiException {}
class ApiRateLimitException extends ApiException {
    protected $retry_after;
    
    public function __construct($message, $status_code = 0, $retry_after = 60, $code = 0) {
        $this->retry_after = $retry_after;
        parent::__construct($message, $status_code, $code);
    }
    
    public function getRetryAfter() {
        return $this->retry_after;
    }
}
class ApiServerException extends ApiException {}
class ApiClientException extends ApiException {}
```

### Using Try-Catch for Error Handling

When using your API client, wrap calls in try-catch blocks:

```php
try {
    $data = $api_client->get('endpoint');
    // Process successful response
} catch (ApiAuthException $e) {
    // Handle authentication errors
    error_log('API Authentication Error: ' . $e->getMessage());
    // Prompt user to re-authenticate
} catch (ApiRateLimitException $e) {
    // Handle rate limiting
    error_log('API Rate Limit Error: ' . $e->getMessage());
    error_log('Retry After: ' . $e->getRetryAfter() . ' seconds');
    // Schedule a retry after the specified time
} catch (ApiServerException $e) {
    // Handle server errors
    error_log('API Server Error: ' . $e->getMessage());
    // Display a friendly message to the user
} catch (ApiClientException $e) {
    // Handle client errors
    error_log('API Client Error: ' . $e->getMessage());
    // Fix the request or display an error message
} catch (ApiConnectionException $e) {
    // Handle connection errors
    error_log('API Connection Error: ' . $e->getMessage());
    // Check network connectivity
} catch (Exception $e) {
    // Handle any other errors
    error_log('API Error: ' . $e->getMessage());
}
```

## Rate Limiting Considerations

Most APIs implement rate limits to prevent abuse. Here's how to handle them:

### Understanding Rate Limits

Rate limits can be:
- **Request-based**: X requests per time period
- **Resource-based**: X operations on a specific resource
- **User-based**: X requests per user
- **Token-based**: X requests per API token

### Strategies for Handling Rate Limits

1. **Caching**: Cache responses to reduce API calls
2. **Batching**: Combine multiple operations into a single request
3. **Queuing**: Queue requests and process them at a controlled rate
4. **Exponential backoff**: Increase wait time between retries
5. **Request prioritization**: Prioritize critical requests

### Implementing a Rate Limit Handler

```php
class RateLimitHandler {
    private $bucket_size;
    private $refill_rate;
    private $available_tokens;
    private $last_refill_time;
    private $option_name;
    
    /**
     * Constructor
     *
     * @param int $bucket_size Maximum number of tokens (requests)
     * @param int $refill_rate Tokens added per second
     * @param string $option_name Option name for storing state
     */
    public function __construct($bucket_size = 60, $refill_rate = 1, $option_name = 'api_rate_limit_state') {
        $this->bucket_size = $bucket_size;
        $this->refill_rate = $refill_rate;
        $this->option_name = $option_name;
        
        // Load state
        $state = get_option($option_name, [
            'available_tokens' => $bucket_size,
            'last_refill_time' => time()
        ]);
        
        $this->available_tokens = $state['available_tokens'];
        $this->last_refill_time = $state['last_refill_time'];
        
        // Refill tokens based on elapsed time
        $this->refill_tokens();
    }
    
    /**
     * Refill tokens based on elapsed time
     */
    private function refill_tokens() {
        $now = time();
        $elapsed = $now - $this->last_refill_time;
        
        if ($elapsed > 0) {
            $new_tokens = $elapsed * $this->refill_rate;
            $this->available_tokens = min($this->bucket_size, $this->available_tokens + $new_tokens);
            $this->last_refill_time = $now;
            
            // Save state
            update_option($this->option_name, [
                'available_tokens' => $this->available_tokens,
                'last_refill_time' => $this->last_refill_time
            ]);
        }
    }
    
    /**
     * Check if a request can be made
     *
     * @param int $tokens Number of tokens required (default 1)
     * @return bool Whether the request can be made
     */
    public function can_make_request($tokens = 1) {
        $this->refill_tokens();
        return $this->available_tokens >= $tokens;
    }
    
    /**
     * Consume tokens for a request
     *
     * @param int $tokens Number of tokens to consume (default 1)
     * @return bool Whether tokens were consumed
     */
    public function consume_tokens($tokens = 1) {
        if (!$this->can_make_request($tokens)) {
            return false;
        }
        
        $this->available_tokens -= $tokens;
        
        // Save state
        update_option($this->option_name, [
            'available_tokens' => $this->available_tokens,
            'last_refill_time' => $this->last_refill_time
        ]);
        
        return true;
    }
    
    /**
     * Get time until next token is available
     *
     * @return int Seconds until next token
     */
    public function get_wait_time() {
        if ($this->available_tokens > 0) {
            return 0;
        }
        
        return ceil(1 / $this->refill_rate);
    }
}
```

### Using the Rate Limit Handler

```php
class ThirdPartyApiClient {
    // ... other properties
    private $rate_limiter;
    
    public function __construct($api_key, $api_url = 'https://api.third-party-service.com/v1/') {
        $this->api_key = $api_key;
        $this->api_url = $api_url;
        
        // Initialize rate limiter with API limits (e.g., 60 requests per minute)
        $this->rate_limiter = new RateLimitHandler(60, 1, 'my_integration_rate_limit');
    }
    
    private function request($method, $endpoint, $params = [], $data = null, $cache = false, $cache_time = 300) {
        // Check if we can make a request
        if (!$this->rate_limiter->can_make_request()) {
            $wait_time = $this->rate_limiter->get_wait_time();
            throw new ApiRateLimitException("Rate limit exceeded. Try again in $wait_time seconds.", 429, $wait_time);
        }
        
        // Make the request
        // ... existing request code ...
        
        // Consume a token for the request
        $this->rate_limiter->consume_tokens();
        
        return $result;
    }
}
```

## Caching API Responses

Caching is essential for reducing API calls, improving performance, and avoiding rate limits. Here's how to implement effective caching:

### When to Cache

1. **GET requests**: Cache responses from GET requests, as they typically return the same data for the same parameters
2. **Rarely changing data**: Cache data that doesn't change frequently
3. **Expensive operations**: Cache responses from operations that are computationally expensive or have high latency

### Caching Strategies

1. **Time-based caching**: Cache data for a fixed period
2. **Conditional caching**: Use ETag or Last-Modified headers to validate cache freshness
3. **Hierarchical caching**: Cache different data for different durations

### Implementing Caching with WordPress Transients

WordPress transients provide a simple way to cache API responses:

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
    $data = $this->get($endpoint, $params, false);
    
    // Cache the data
    set_transient($cache_key, $data, $cache_time);
    
    return $data;
}
```

### Cache Invalidation

It's important to invalidate cache when data changes:

```php
/**
 * Invalidate cache for an endpoint
 *
 * @param string $endpoint API endpoint
 * @param array $params Query parameters
 */
public function invalidate_cache($endpoint, $params = []) {
    $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
    delete_transient($cache_key);
}
```

### Dynamic Cache Duration

Adjust cache duration based on data volatility:

```php
/**
 * Get cache duration for an endpoint
 *
 * @param string $endpoint API endpoint
 * @return int Cache duration in seconds
 */
private function get_cache_duration($endpoint) {
    $durations = [
        'user' => 60,           // User data: 1 minute
        'posts' => 300,         // Posts: 5 minutes
        'comments' => 180,      // Comments: 3 minutes
        'settings' => 3600,     // Settings: 1 hour
        'static' => 86400       // Static data: 24 hours
    ];
    
    foreach ($durations as $key => $duration) {
        if (strpos($endpoint, $key) !== false) {
            return $duration;
        }
    }
    
    return 300; // Default: 5 minutes
}
```

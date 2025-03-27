# Working with Third-Party APIs in MainWP Integrations

This guide provides comprehensive information on working with third-party APIs in MainWP integrations. You'll learn how to design robust API clients, handle authentication, manage errors, implement caching, and more.

## Quick Start for Experienced Developers

```php
namespace MyCompany\ThirdParty;

use Exception;
use WP_Error;

// 1. Create a reusable API client class
class ThirdPartyApiClient {
    /** @var string API key */
    private $api_key;
    /** @var string API URL */
    private $api_url = 'https://api.third-party-service.com/v1/';
    /** @var int Request timeout */
    private $timeout = 30;
    
    /**
     * Constructor
     * 
     * @param string $api_key API key
     */
    public function __construct($api_key) {
        $this->api_key = $api_key;
    }
    
    /**
     * Make a GET request
     * 
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @return array|WP_Error Response data
     */
    public function get($endpoint, $params = []) {
        return $this->request('GET', $endpoint, $params);
    }
    
    /**
     * Make a POST request
     * 
     * @param string $endpoint API endpoint
     * @param array $data Post data
     * @return array|WP_Error Response data
     */
    public function post($endpoint, $data = []) {
        return $this->request('POST', $endpoint, [], $data);
    }
    
    /**
     * Make an API request
     * 
     * @param string $method HTTP method
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param array|null $data Request body data
     * @return array|WP_Error Response data
     */
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
    /** @var ThirdPartyApiClient API client */
    private $api_client;
    
    /**
     * Constructor
     */
    public function __construct() {
        // Initialize API client
        $api_key = get_option('my_integration_api_key', '');
        if (!empty($api_key)) {
            $this->api_client = new ThirdPartyApiClient($api_key);
        }
        
        // Hook into MainWP
        add_action('mainwp_site_synced', [$this, 'sync_third_party_data'], 10, 2);
    }
    
    /**
     * Sync data from third-party service
     * 
     * @param object $website Website object
     * @param array $data Sync data
     */
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
namespace MyCompany\ThirdParty;

use Exception;
use WP_Error;

/**
 * Third-party API client
 */
class ThirdPartyApiClient {
    /** @var string API key */
    private $api_key;
    /** @var string API URL */
    private $api_url;
    /** @var int Request timeout */
    private $timeout = 30;
    /** @var array|WP_Error Last response */
    private $last_response;
    /** @var array Last request */
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
namespace MyCompany\ThirdParty\OAuth;

use Exception;
use WP_Error;

/**
 * OAuth2 client
 */
class OAuth2Client extends ThirdPartyApiClient {
    /** @var string Client ID */
    private $client_id;
    /** @var string Client secret */
    private $client_secret;
    /** @var string Redirect URI */
    private $redirect_uri;
    /** @var string Authorization URL */
    private $auth_url;
    /** @var string Token URL */
    private $token_url;
    /** @var string Access token */
    private $access_token;
    /** @var string Refresh token */
    private $refresh_token;
    /** @var int Token expiration timestamp */
    private $token_expires;
    
    /**
     * Constructor
     */
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

## Error Handling and Retry Strategies

Robust error handling is essential for reliable API integrations. Here's a comprehensive approach:

### Error Types to Handle

1. **Connection errors**: Network issues, timeouts
2. **Authentication errors**: Invalid or expired credentials
3. **Rate limiting**: Too many requests
4. **Server errors**: 5xx responses
5. **Client errors**: 4xx responses
6. **Parsing errors**: Invalid JSON responses

### Custom Exception Classes

Create custom exception classes for different error types:

```php
namespace MyCompany\ThirdParty\Exceptions;

use Exception;

/**
 * Base API exception
 */
class ApiException extends Exception {
    /** @var int HTTP status code */
    protected $status_code;
    
    /**
     * Constructor
     */
    public function __construct($message, $status_code = 0, $code = 0) {
        $this->status_code = $status_code;
        parent::__construct($message, $code);
    }
    
    /**
     * Get HTTP status code
     */
    public function getStatusCode() {
        return $this->status_code;
    }
}

class ApiConnectionException extends ApiException {}
class ApiAuthException extends ApiException {}
class ApiRateLimitException extends ApiException {
    /** @var int Retry after seconds */
    protected $retry_after;
    
    /**
     * Constructor
     */
    public function __construct($message, $status_code = 0, $retry_after = 60, $code = 0) {
        $this->retry_after = $retry_after;
        parent::__construct($message, $status_code, $code);
    }
    
    /**
     * Get retry after seconds
     */
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

### Implementing a Rate Limit Handler

```php
namespace MyCompany\ThirdParty\RateLimit;

/**
 * Rate limit handler using token bucket algorithm
 */
class RateLimitHandler {
    /** @var int Maximum number of tokens */
    private $bucket_size;
    /** @var int Tokens added per second */
    private $refill_rate;
    /** @var int Available tokens */
    private $available_tokens;
    /** @var int Last refill time */
    private $last_refill_time;
    /** @var string Option name for storing state */
    private $option_name;
    
    /**
     * Constructor
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
     * @param int $tokens Number of tokens required
     * @return bool Whether the request can be made
     */
    public function can_make_request($tokens = 1) {
        $this->refill_tokens();
        return $this->available_tokens >= $tokens;
    }
    
    /**
     * Consume tokens for a request
     *
     * @param int $tokens Number of tokens to consume
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

## Caching API Responses

Caching is essential for reducing API calls, improving performance, and avoiding rate limits. Here's how to implement effective caching:

### When to Cache

1. **GET requests**: Cache responses from GET requests, as they typically return the same data for the same parameters
2. **Rarely changing data**: Cache data that doesn't change frequently
3. **Expensive operations**: Cache responses from operations that are computationally expensive or have high latency

### Implementing Caching with WordPress Transients

WordPress transients provide a simple way to cache API responses:

```php
namespace MyCompany\ThirdParty\Cache;

/**
 * API response cache manager
 */
class CacheManager {
    /** @var int Default cache duration */
    private $default_duration = 300; // 5 minutes
    
    /**
     * Get cached data
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param int $duration Cache duration in seconds
     * @return array|false Response data or false if not cached
     */
    public function get_cached($endpoint, $params = [], $duration = null) {
        $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
        
        // Check cache
        $cached = get_transient($cache_key);
        if (false !== $cached) {
            return $cached;
        }
        
        return false;
    }
    
    /**
     * Cache data
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     * @param mixed $data Data to cache
     * @param int $duration Cache duration in seconds
     */
    public function cache_data($endpoint, $params, $data, $duration = null) {
        $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
        $duration = $duration ?? $this->default_duration;
        
        set_transient($cache_key, $data, $duration);
    }
    
    /**
     * Invalidate cache
     *
     * @param string $endpoint API endpoint
     * @param array $params Query parameters
     */
    public function invalidate_cache($endpoint, $params = []) {
        $cache_key = 'my_integration_' . md5($endpoint . serialize($params));
        delete_transient($cache_key);
    }
    
    /**
     * Get cache duration for an endpoint
     *
     * @param string $endpoint API endpoint
     * @return int Cache duration in seconds
     */
    public function get_cache_duration($endpoint) {
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
        
        return $this->default_duration;
    }
}
```

## Related Resources

- [Creating a Basic Integration](create-basic-integration.md)
- [Using MainWP Actions & Filters](actions-filters.md)
- [API Integration Best Practices](../best-practices/api-integration.md)
- [Third-Party API Integration Patterns](../reference/api-integration-patterns.md)
- [WordPress HTTP API Documentation](https://developer.wordpress.org/plugins/http-api/)
- [OAuth 2.0 Documentation](https://oauth.net/2/)

# MainWP Social Media Integration: Advanced Features

This guide covers advanced features and techniques for MainWP social media integrations, building on the [core concepts covered in part 1](social-media-integration.md). Here we'll explore Bluesky integration, advanced LinkedIn features, background processing, and best practices.

## Bluesky Integration

Bluesky offers a simpler API integration with fewer restrictions and an easier setup process compared to LinkedIn.

### Bluesky API Client

```php
namespace MyCompany\Bluesky;

use MainWP\Dashboard\MainWP_Connect;
use WP_Error;
use Exception;

/**
 * Bluesky API Client
 */
class BlueskyAPIClient {
    /** @var object Website object */
    private $website;
    /** @var string App password */
    private $app_password;
    /** @var string Username */
    private $username;
    /** @var int Cache expiration in seconds */
    private $cache_expiration = 300; // 5 minutes
    /** @var string API base URL */
    private $api_base_url = 'https://bsky.social/xrpc/';
    /** @var string|null Authentication token */
    private $auth_token = null;
    
    /**
     * Constructor
     * 
     * @param object $website Website object
     * @param string $username Bluesky username
     * @param string $app_password Bluesky app password
     */
    public function __construct($website, $username, $app_password) {
        $this->website = $website;
        $this->username = $username;
        $this->app_password = $app_password;
    }
    
    /**
     * Authenticate with Bluesky
     * 
     * @return bool|WP_Error True on success, error on failure
     */
    public function authenticate() {
        // Check if already authenticated
        if ($this->auth_token !== null) {
            return true;
        }
        
        // Prepare the request data for MainWP
        $data = [
            'bluesky_api' => true,
            'endpoint' => 'com.atproto.server.createSession',
            'method' => 'POST',
            'args' => [
                'identifier' => $this->username,
                'password' => $this->app_password
            ]
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'bluesky_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                return new WP_Error('api_error', $information['error']);
            }
            
            // Store authentication token
            if (isset($information['accessJwt'])) {
                $this->auth_token = $information['accessJwt'];
                return true;
            }
            
            return new WP_Error('auth_error', 'Authentication failed');
        } catch (Exception $e) {
            return new WP_Error('api_error', $e->getMessage());
        }
    }
    
    /**
     * Create a post (skeet)
     * 
     * @param string $text Post text
     * @param array $images Optional array of image URLs
     * @return array|WP_Error Post data or error
     */
    public function create_post($text, $images = []) {
        // Authenticate if needed
        $auth_result = $this->authenticate();
        if (is_wp_error($auth_result)) {
            return $auth_result;
        }
        
        // Prepare post data
        $post_data = [
            'collection' => 'app.bsky.feed.post',
            'repo' => $this->username,
            'record' => [
                'text' => $text,
                'createdAt' => date('c')
            ]
        ];
        
        // Add images if provided
        if (!empty($images)) {
            $post_data['record']['embed'] = [
                '$type' => 'app.bsky.embed.images',
                'images' => []
            ];
            
            foreach ($images as $image) {
                // Upload image first
                $blob_result = $this->upload_blob($image['url'], $image['mime_type']);
                if (is_wp_error($blob_result)) {
                    continue;
                }
                
                $post_data['record']['embed']['images'][] = [
                    'alt' => isset($image['alt']) ? $image['alt'] : '',
                    'image' => $blob_result
                ];
            }
        }
        
        // Prepare the request data for MainWP
        $data = [
            'bluesky_api' => true,
            'endpoint' => 'com.atproto.repo.createRecord',
            'method' => 'POST',
            'args' => $post_data,
            'auth_token' => $this->auth_token
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'bluesky_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                return new WP_Error('api_error', $information['error']);
            }
            
            return $information;
        } catch (Exception $e) {
            return new WP_Error('api_error', $e->getMessage());
        }
    }
    
    /**
     * Upload a blob (image)
     * 
     * @param string $image_url Image URL
     * @param string $mime_type Image MIME type
     * @return array|WP_Error Blob data or error
     */
    private function upload_blob($image_url, $mime_type) {
        // Get image data
        $response = wp_remote_get($image_url);
        if (is_wp_error($response)) {
            return $response;
        }
        
        $image_data = wp_remote_retrieve_body($response);
        
        // Prepare the request data for MainWP
        $data = [
            'bluesky_api' => true,
            'endpoint' => 'com.atproto.repo.uploadBlob',
            'method' => 'POST',
            'args' => [
                'b64' => base64_encode($image_data),
                'mime_type' => $mime_type
            ],
            'auth_token' => $this->auth_token
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'bluesky_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                return new WP_Error('api_error', $information['error']);
            }
            
            return $information['blob'];
        } catch (Exception $e) {
            return new WP_Error('api_error', $e->getMessage());
        }
    }
    
    /**
     * Get user profile
     * 
     * @param string $username Username to get profile for (defaults to authenticated user)
     * @return array|WP_Error Profile data or error
     */
    public function get_profile($username = null) {
        // Authenticate if needed
        $auth_result = $this->authenticate();
        if (is_wp_error($auth_result)) {
            return $auth_result;
        }
        
        // Use authenticated user if username not provided
        if ($username === null) {
            $username = $this->username;
        }
        
        // Prepare the request data for MainWP
        $data = [
            'bluesky_api' => true,
            'endpoint' => 'app.bsky.actor.getProfile',
            'method' => 'GET',
            'args' => [
                'actor' => $username
            ],
            'auth_token' => $this->auth_token
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'bluesky_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                return new WP_Error('api_error', $information['error']);
            }
            
            return $information;
        } catch (Exception $e) {
            return new WP_Error('api_error', $e->getMessage());
        }
    }
    
    /**
     * Get user timeline
     * 
     * @param string $username Username to get timeline for (defaults to authenticated user)
     * @param string $cursor Pagination cursor
     * @param int $limit Number of posts to retrieve (max 100)
     * @return array|WP_Error Timeline data or error
     */
    public function get_timeline($username = null, $cursor = null, $limit = 50) {
        // Authenticate if needed
        $auth_result = $this->authenticate();
        if (is_wp_error($auth_result)) {
            return $auth_result;
        }
        
        // Use authenticated user if username not provided
        if ($username === null) {
            $username = $this->username;
        }
        
        // Prepare arguments
        $args = [
            'actor' => $username,
            'limit' => min(100, max(1, $limit))
        ];
        
        if ($cursor !== null) {
            $args['cursor'] = $cursor;
        }
        
        // Prepare the request data for MainWP
        $data = [
            'bluesky_api' => true,
            'endpoint' => 'app.bsky.feed.getAuthorFeed',
            'method' => 'GET',
            'args' => $args,
            'auth_token' => $this->auth_token
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'bluesky_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                return new WP_Error('api_error', $information['error']);
            }
            
            return $information;
        } catch (Exception $e) {
            return new WP_Error('api_error', $e->getMessage());
        }
    }
}
```

### Bluesky Content Manager

```php
namespace MyCompany\Bluesky\Content;

use WP_Error;

/**
 * Bluesky Content Manager
 */
class BlueskyContentManager {
    /** @var BlueskyAPIClient API client */
    private $api_client;
    
    /**
     * Constructor
     * 
     * @param BlueskyAPIClient $api_client API client
     */
    public function __construct($api_client) {
        $this->api_client = $api_client;
    }
    
    /**
     * Create a text post
     * 
     * @param string $text Post text
     * @return array|WP_Error Post data or error
     */
    public function create_text_post($text) {
        return $this->api_client->create_post($text);
    }
    
    /**
     * Create a post with images
     * 
     * @param string $text Post text
     * @param array $images Array of image data (url, mime_type, alt)
     * @return array|WP_Error Post data or error
     */
    public function create_image_post($text, $images) {
        return $this->api_client->create_post($text, $images);
    }
    
    /**
     * Schedule a post
     * 
     * @param string $text Post text
     * @param array $images Optional array of image data
     * @param int $timestamp Timestamp to publish the post
     * @return bool Success or failure
     */
    public function schedule_post($text, $images = [], $timestamp) {
        // Validate timestamp
        if ($timestamp <= time()) {
            return new WP_Error('invalid_timestamp', 'Scheduled time must be in the future');
        }
        
        // Get scheduled posts
        $scheduled_posts = get_option('mainwp_bluesky_scheduled_posts', []);
        
        // Add new scheduled post
        $scheduled_posts[] = [
            'text' => $text,
            'images' => $images,
            'timestamp' => $timestamp
        ];
        
        // Save scheduled posts
        return update_option('mainwp_bluesky_scheduled_posts', $scheduled_posts);
    }
}
```

### Setting Up Bluesky Integration

1. **Get Bluesky Credentials**
   - Create a Bluesky account if you don't have one
   - Generate an app password in your account settings
   - Note your username and app password

2. **Configure the Integration**
   - Add Bluesky settings to your integration settings page
   - Store credentials securely using WordPress options API

```php
namespace MyCompany\Bluesky\Settings;

/**
 * Save Bluesky API credentials for a site
 * 
 * @param int $website_id The website ID
 * @param string $username Bluesky username
 * @param string $app_password Bluesky app password
 * @return bool Success or failure
 */
public function save_bluesky_credentials($website_id, $username, $app_password) {
    // Validate inputs
    $website_id = absint($website_id);
    if ($website_id <= 0) {
        return false;
    }
    
    $username = sanitize_text_field($username);
    $app_password = sanitize_text_field($app_password);
    
    // Get current settings
    $settings = get_option('mainwp_bluesky_settings', []);
    
    // Update settings for this site
    $settings[$website_id] = [
        'username' => $username,
        'app_password' => $app_password
    ];
    
    // Save settings
    return update_option('mainwp_bluesky_settings', $settings);
}
```

## Advanced LinkedIn Features

### Data Models for LinkedIn

Create models for LinkedIn data to improve code organization and maintainability:

```php
namespace MyCompany\LinkedIn\Models;

/**
 * Company Page Model
 */
class CompanyPage {
    /** @var string Company ID */
    public $id;
    /** @var string Company name */
    public $name;
    /** @var string Company vanity name */
    public $vanity_name;
    /** @var string Company logo URL */
    public $logo_url;
    /** @var string Company website */
    public $website;
    /** @var string Company industry */
    public $industry;
    /** @var int Company follower count */
    public $follower_count;
    /** @var string Company description */
    public $description;
    /** @var array Company locations */
    public $locations;
    
    /**
     * Create a company page from API data
     * 
     * @param array $data Company page data from API
     * @return CompanyPage Company page object
     */
    public static function from_api_data($data) {
        $company = new self();
        
        // Map API data to object properties
        $company->id = isset($data['id']) ? $data['id'] : '';
        $company->name = isset($data['name']) ? $data['name'] : '';
        $company->vanity_name = isset($data['vanityName']) ? $data['vanityName'] : '';
        $company->logo_url = isset($data['logoUrl']) ? $data['logoUrl'] : '';
        $company->website = isset($data['website']) ? $data['website'] : '';
        $company->industry = isset($data['industry']) ? $data['industry'] : '';
        $company->follower_count = isset($data['followerCount']) ? $data['followerCount'] : 0;
        $company->description = isset($data['description']) ? $data['description'] : '';
        $company->locations = isset($data['locations']) ? $data['locations'] : [];
        
        return $company;
    }
}

/**
 * Post Model
 */
class Post {
    /** @var string Post ID */
    public $id;
    /** @var string Author ID */
    public $author;
    /** @var string Post content */
    public $content;
    /** @var string Created time */
    public $created_time;
    /** @var string Last modified time */
    public $last_modified_time;
    /** @var array Media content */
    public $media;
    /** @var array Visibility settings */
    public $visibility;
    /** @var array Analytics data */
    public $analytics;
    
    /**
     * Create a post from API data
     * 
     * @param array $data Post data from API
     * @return Post Post object
     */
    public static function from_api_data($data) {
        $post = new self();
        
        // Map API data to object properties
        $post->id = isset($data['id']) ? $data['id'] : '';
        $post->author = isset($data['author']) ? $data['author'] : '';
        $post->content = isset($data['specificContent']['com.linkedin.ugc.ShareContent']['shareCommentary']['text']) 
            ? $data['specificContent']['com.linkedin.ugc.ShareContent']['shareCommentary']['text'] 
            : '';
        $post->created_time = isset($data['created']['time']) ? $data['created']['time'] : '';
        $post->last_modified_time = isset($data['lastModified']['time']) ? $data['lastModified']['time'] : '';
        $post->media = isset($data['specificContent']['com.linkedin.ugc.ShareContent']['media']) 
            ? $data['specificContent']['com.linkedin.ugc.ShareContent']['media'] 
            : [];
        $post->visibility = isset($data['visibility']) ? $data['visibility'] : [];
        $post->analytics = isset($data['analytics']) ? $data['analytics'] : [];
        
        return $post;
    }
}
```

### Analytics and Reporting

Implement analytics functionality to track post performance:

```php
namespace MyCompany\LinkedIn\Analytics;

use WP_Error;

/**
 * Analytics Manager
 */
class AnalyticsManager {
    /** @var LinkedInAPIClient API client */
    private $api_client;
    
    /**
     * Constructor
     * 
     * @param LinkedInAPIClient $api_client API client
     */
    public function __construct($api_client) {
        $this->api_client = $api_client;
    }
    
    /**
     * Get post analytics
     * 
     * @param string $company_id Company ID
     * @param string $post_id Post ID
     * @return array|WP_Error Analytics data or error
     */
    public function get_post_analytics($company_id, $post_id) {
        $endpoint = "organizationalEntityShareStatistics?q=organizationalEntity&organizationalEntity=urn:li:organization:{$company_id}&shares[0]=urn:li:share:{$post_id}";
        return $this->api_client->make_api_request($endpoint);
    }
    
    /**
     * Get company page analytics
     * 
     * @param string $company_id Company ID
     * @param string $timeRange Time range (DAY, WEEK, MONTH)
     * @return array|WP_Error Analytics data or error
     */
    public function get_company_analytics($company_id, $timeRange = 'DAY') {
        $endpoint = "organizationPageStatistics?q=organization&organization=urn:li:organization:{$company_id}&timeIntervals.timeGranularityType={$timeRange}&timeIntervals.timeRange.start=1577836800000";
        return $this->api_client->make_api_request($endpoint);
    }
    
    /**
     * Get follower demographics
     * 
     * @param string $company_id Company ID
     * @return array|WP_Error Demographics data or error
     */
    public function get_follower_demographics($company_id) {
        $endpoint = "organizationalEntityFollowerStatistics?q=organizationalEntity&organizationalEntity=urn:li:organization:{$company_id}";
        return $this->api_client->make_api_request($endpoint);
    }
    
    /**
     * Generate analytics report
     * 
     * @param string $company_id Company ID
     * @return array Report data
     */
    public function generate_report($company_id) {
        $report = [
            'company_id' => $company_id,
            'generated_at' => current_time('mysql'),
            'company_analytics' => [],
            'post_analytics' => [],
            'demographics' => []
        ];
        
        // Get company analytics
        $company_analytics = $this->get_company_analytics($company_id);
        if (!is_wp_error($company_analytics)) {
            $report['company_analytics'] = $company_analytics;
        }
        
        // Get recent posts
        $posts = $this->api_client->get_company_posts($company_id, ['count' => 10]);
        if (!is_wp_error($posts) && !empty($posts)) {
            foreach ($posts as $post) {
                if (isset($post['id'])) {
                    $post_analytics = $this->get_post_analytics($company_id, $post['id']);
                    if (!is_wp_error($post_analytics)) {
                        $report['post_analytics'][$post['id']] = $post_analytics;
                    }
                }
            }
        }
        
        // Get demographics
        $demographics = $this->get_follower_demographics($company_id);
        if (!is_wp_error($demographics)) {
            $report['demographics'] = $demographics;
        }
        
        return $report;
    }
}
```

## Background Processing

For operations that may take a long time, implement background processing:

```php
namespace MyCompany\SocialMedia\Background;

use MainWP\Dashboard\MainWP_DB;
use WP_Error;

/**
 * Schedule background tasks
 */
public function schedule_background_tasks() {
    if (!wp_next_scheduled('mainwp_social_media_background_tasks')) {
        wp_schedule_event(time(), 'hourly', 'mainwp_social_media_background_tasks');
    }
    
    // Hook into the scheduled event
    add_action('mainwp_social_media_background_tasks', [$this, 'process_scheduled_posts']);
}

/**
 * Process scheduled posts
 */
public function process_scheduled_posts() {
    // Process LinkedIn scheduled posts
    $this->process_linkedin_scheduled_posts();
    
    // Process Bluesky scheduled posts
    $this->process_bluesky_scheduled_posts();
}

/**
 * Process LinkedIn scheduled posts
 */
private function process_linkedin_scheduled_posts() {
    // Get scheduled LinkedIn posts
    $scheduled_posts = get_option('mainwp_linkedin_scheduled_posts', []);
    $current_time = time();
    $updated_posts = [];
    
    foreach ($scheduled_posts as $post) {
        if ($post['timestamp'] <= $current_time) {
            // Time to publish
            $api_client = $this->get_api_client($post['website_id']);
            if ($api_client) {
                $api_client->create_company_post($post['company_id'], $post['post_data']);
                
                // Log successful publishing if WP_DEBUG_LOG is enabled
                if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                    error_log(sprintf(
                        '[MainWP LinkedIn] Published scheduled post for company ID %s on website ID %d',
                        $post['company_id'],
                        $post['website_id']
                    ));
                }
            }
        } else {
            // Keep for future
            $updated_posts[] = $post;
        }
    }
    
    // Update scheduled posts
    update_option('mainwp_linkedin_scheduled_posts', $updated_posts);
}

/**
 * Process Bluesky scheduled posts
 */
private function process_bluesky_scheduled_posts() {
    // Get scheduled Bluesky posts
    $scheduled_posts = get_option('mainwp_bluesky_scheduled_posts', []);
    $current_time = time();
    $updated_posts = [];
    
    foreach ($scheduled_posts as $post) {
        if ($post['timestamp'] <= $current_time) {
            // Time to publish
            $api_client = $this->get_bluesky_api_client($post['website_id']);
            if ($api_client) {
                $api_client->create_post($post['text'], $post['images']);
                
                // Log successful publishing if WP_DEBUG_LOG is enabled
                if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                    error_log(sprintf(
                        '[MainWP Bluesky] Published scheduled post on website ID %d',
                        $post['website_id']
                    ));
                }
            }
        } else {
            // Keep for future
            $updated_posts[] = $post;
        }
    }
    
    // Update scheduled posts
    update_option('mainwp_bluesky_scheduled_posts', $updated_posts);
}
```

### Using Action Scheduler for More Complex Tasks

For more complex background processing, consider using the Action Scheduler library:

```php
namespace MyCompany\SocialMedia\Background;

use WP_Error;

/**
 * Schedule a post using Action Scheduler
 * 
 * @param int $website_id Website ID
 * @param string $company_id Company ID
 * @param array $post_data Post data
 * @param int $timestamp Timestamp to publish the post
 * @return int Action ID
 */
public function schedule_post_with_action_scheduler($website_id, $company_id, $post_data, $timestamp) {
    return as_schedule_single_action(
        $timestamp,
        'mainwp_linkedin_publish_post',
        [
            'website_id' => $website_id,
            'company_id' => $company_id,
            'post_data' => $post_data
        ]
    );
}

/**
 * Handle Action Scheduler publish post action
 * 
 * @param int $website_id Website ID
 * @param string $company_id Company ID
 * @param array $post_data Post data
 */
public function handle_publish_post_action($website_id, $company_id, $post_data) {
    $api_client = $this->get_api_client($website_id);
    if ($api_client) {
        $api_client->create_company_post($company_id, $post_data);
        
        // Log successful publishing if WP_DEBUG_LOG is enabled
        if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
            error_log(sprintf(
                '[MainWP LinkedIn] Published scheduled post for company ID %s on website ID %d via Action Scheduler',
                $company_id,
                $website_id
            ));
        }
    }
}
```

## Webhook Handling

Implement webhook handling to receive real-time notifications from social media platforms:

```php
namespace MyCompany\SocialMedia\Webhooks;

use WP_REST_Request;
use WP_REST_Response;
use WP_Error;
use Exception;

/**
 * Register webhook handlers
 */
public function register_webhook_handlers() {
    // Register webhook endpoint
    add_action('rest_api_init', function() {
        register_rest_route('mainwp-social-media/v1', '/linkedin-webhook/(?P<website_id>\d+)', [
            'methods' => 'POST',
            'callback' => [$this, 'handle_linkedin_webhook'],
            'permission_callback' => [$this, 'verify_linkedin_webhook'],
        ]);
        
        register_rest_route('mainwp-social-media/v1', '/bluesky-webhook/(?P<website_id>\d+)', [
            'methods' => 'POST',
            'callback' => [$this, 'handle_bluesky_webhook'],
            'permission_callback' => [$this, 'verify_bluesky_webhook'],
        ]);
    });
}

/**
 * Verify LinkedIn webhook request
 * 
 * @param WP_REST_Request $request Request object
 * @return bool Whether the request is valid
 */
public function verify_linkedin_webhook($request) {
    // Validate website ID
    $website_id = absint($request->get_param('website_id'));
    if ($website_id <= 0) {
        return false;
    }
    
    $signature = $request->get_header('X-LinkedIn-Signature');
    if (empty($signature)) {
        // Log missing signature if WP_DEBUG_LOG is enabled
        if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
            error_log(sprintf(
                '[MainWP LinkedIn] Missing webhook signature for website ID: %d',
                $website_id
            ));
        }
        return false;
    }
    
    // Get webhook secret for this site
    $settings = get_option('mainwp_linkedin_settings', []);
    $site_settings = isset($settings[$website_id]) ? $settings[$website_id] : [];
    
    if (empty($site_settings['webhook_secret'])) {
        // Log missing webhook secret if WP_DEBUG_LOG is enabled
        if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
            error_log(sprintf(
                '[MainWP LinkedIn] Webhook secret not configured for website ID: %d',
                $website_id
            ));
        }
        return false;
    }
    
    // Verify signature with constant-time comparison to prevent timing attacks
    $payload = $request->get_body();
    $calculated_signature = hash_hmac('sha256', $payload, $site_settings['webhook_secret']);
    
    return hash_equals($calculated_signature, $signature);
}

/**
 * Handle LinkedIn webhook request
 * 
 * @param WP_REST_Request $request Request object
 * @return WP_REST_Response Response object
 */
public function handle_linkedin_webhook($request) {
    $website_id = absint($request->get_param('website_id'));
    $payload = json_decode($request->get_body(), true);
    
    if (!$payload || !isset($payload['event'])) {
        return new WP_REST_Response([
            'success' => false,
            'message' => 'Invalid payload or missing event'
        ], 400);
    }
    
    try {
        // Process webhook based on event
        switch ($payload['event']) {
            case 'ORGANIZATION_UPDATED':
                $this->process_organization_update($website_id, $payload['data']);
                break;
            case 'SHARE_CREATED':
                $this->process_share_created($website_id, $payload['data']);
                break;
            default:
                // Log unknown event if WP_DEBUG_LOG is enabled
                if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                    error_log(sprintf(
                        '[MainWP LinkedIn] Unknown webhook event: %s for website ID: %d',
                        $payload['event'],
                        $website_id
                    ));
                }
                return new WP_REST_Response([
                    'success' => false,
                    '

# MainWP Social Media Integration: Quick Start Guide

This quick start guide provides the essential code and steps to implement a MainWP social media integration. For more detailed explanations and advanced features, see the [complete Social Media Integration guide](social-media-integration.md).

## Prerequisites

- WordPress with MainWP Dashboard installed
- Social media platform developer accounts (LinkedIn and/or Bluesky)
- Basic understanding of WordPress plugin development

## Quick Implementation: LinkedIn Integration

```php
<?php
/**
 * Plugin Name: MainWP LinkedIn Integration
 * Plugin URI: https://yourwebsite.com/mainwp-linkedin
 * Description: Integrates MainWP with LinkedIn for centralized social media management.
 * Version: 1.0.0
 * Author: Your Name
 * Author URI: https://yourwebsite.com
 * Text Domain: mainwp-linkedin
 */

namespace YourCompany\MainWPLinkedIn;

use MainWP\Dashboard\MainWP_DB;
use MainWP\Dashboard\MainWP_Connect;
use WP_Error;
use Exception;

// Prevent direct access
if (!defined('ABSPATH')) {
    exit;
}

// Register the integration with MainWP
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = [
        'plugin' => __FILE__,
        'api' => 'MainWPLinkedIn',
        'mainwp' => true,
        'callback' => [__NAMESPACE__ . '\\MainWPLinkedIn', 'get_instance'],
        'name' => 'LinkedIn Integration'
    ];
    return $extensions;
});

class MainWPLinkedIn {
    /** @var MainWPLinkedIn|null Instance */
    private static $instance = null;
    /** @var LinkedInAPIClient|null API Client */
    private $api_client = null;
    
    /**
     * Get singleton instance
     * @return MainWPLinkedIn Instance of the plugin
     */
    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    /**
     * Constructor
     */
    public function __construct() {
        // Initialize the integration
        add_action('admin_init', [$this, 'admin_init']);
        add_action('mainwp_admin_menu', [$this, 'init_menu']);
        
        // Hook into site sync to collect LinkedIn data
        add_action('mainwp_site_synced', [$this, 'site_synced'], 10, 2);
        
        // Add LinkedIn data to individual site view
        add_filter('mainwp_getsubpages_sites', [$this, 'add_linkedin_site_tab'], 10, 2);
    }
    
    /**
     * Initialize admin functionality
     */
    public function admin_init() {
        // Register settings
        register_setting('mainwp_linkedin_settings_group', 'mainwp_linkedin_settings');
    }
    
    /**
     * Initialize menu items
     */
    public function init_menu() {
        // Add LinkedIn dashboard page
        add_submenu_page(
            'mainwp_tab',
            __('LinkedIn', 'mainwp-linkedin'),
            __('LinkedIn', 'mainwp-linkedin'),
            'manage_options', // Use manage_options instead of read for better security
            'MainWPLinkedIn',
            [$this, 'render_dashboard_page']
        );
        
        // Add settings page
        add_submenu_page(
            'mainwp_tab',
            __('LinkedIn Settings', 'mainwp-linkedin'),
            __('LinkedIn Settings', 'mainwp-linkedin'),
            'manage_options', // Use manage_options instead of read for better security
            'MainWPLinkedInSettings',
            [$this, 'render_settings_page']
        );
    }
    
    /**
     * Process data after a site is synced
     * 
     * @param object $website The website object
     * @param array $data The sync data
     */
    public function site_synced($website, $data) {
        // Check if LinkedIn data is available
        if (isset($data['linkedin'])) {
            // Store the LinkedIn data for this site
            update_option('mainwp_linkedin_data_' . $website->id, $data['linkedin']);
        }
    }
    
    /**
     * Add LinkedIn tab to individual site view
     * 
     * @param array $subpages Current subpages
     * @param object $website The website object
     * @return array Modified subpages
     */
    public function add_linkedin_site_tab($subpages, $website) {
        $subpages[] = [
            'title' => __('LinkedIn', 'mainwp-linkedin'),
            'slug' => 'LinkedIn',
            'callback' => [$this, 'render_site_linkedin_tab'],
        ];
        return $subpages;
    }
    
    /**
     * Get LinkedIn API client for a specific site
     * 
     * @param int $website_id The website ID
     * @return LinkedInAPIClient|null API client or null on failure
     */
    private function get_api_client($website_id) {
        // Validate website ID
        $website_id = absint($website_id);
        if ($website_id <= 0) {
            return null;
        }
        
        // Get the website
        $website = MainWP_DB::instance()->get_website_by_id($website_id);
        if (!$website) {
            return null;
        }
        
        // Get API credentials from options
        $settings = get_option('mainwp_linkedin_settings', []);
        $site_settings = isset($settings[$website_id]) ? $settings[$website_id] : [];
        
        if (empty($site_settings['client_id']) || empty($site_settings['client_secret']) || empty($site_settings['access_token'])) {
            return null;
        }
        
        // Create API client
        return new LinkedInAPIClient(
            $website,
            $site_settings['client_id'],
            $site_settings['client_secret'],
            $site_settings['access_token']
        );
    }
    
    /**
     * Save API credentials for a site
     * 
     * @param int $website_id The website ID
     * @param string $client_id LinkedIn API client ID
     * @param string $client_secret LinkedIn API client secret
     * @param string $access_token LinkedIn API access token
     * @return bool Success or failure
     */
    public function save_api_credentials($website_id, $client_id, $client_secret, $access_token) {
        // Validate inputs
        $website_id = absint($website_id);
        if ($website_id <= 0) {
            return false;
        }
        
        $client_id = sanitize_text_field($client_id);
        $client_secret = sanitize_text_field($client_secret);
        $access_token = sanitize_text_field($access_token);
        
        // Get current settings
        $settings = get_option('mainwp_linkedin_settings', []);
        
        // Update settings for this site
        $settings[$website_id] = [
            'client_id' => $client_id,
            'client_secret' => $client_secret,
            'access_token' => $access_token
        ];
        
        // Save settings
        return update_option('mainwp_linkedin_settings', $settings);
    }
}

/**
 * LinkedIn API Client
 */
class LinkedInAPIClient {
    /** @var object Website object */
    private $website;
    /** @var string Client ID */
    private $client_id;
    /** @var string Client secret */
    private $client_secret;
    /** @var string Access token */
    private $access_token;
    /** @var int Cache expiration in seconds */
    private $cache_expiration = 300; // 5 minutes
    
    /**
     * Constructor
     * 
     * @param object $website Website object
     * @param string $client_id LinkedIn API client ID
     * @param string $client_secret LinkedIn API client secret
     * @param string $access_token LinkedIn API access token
     */
    public function __construct($website, $client_id, $client_secret, $access_token) {
        $this->website = $website;
        $this->client_id = $client_id;
        $this->client_secret = $client_secret;
        $this->access_token = $access_token;
    }
    
    /**
     * Get company page information
     * 
     * @param string $company_id Company ID
     * @return array|WP_Error Company info or error
     */
    public function get_company_info($company_id) {
        // Check cache first
        $cache_key = 'mainwp_linkedin_company_' . $this->website->id . '_' . $company_id;
        $cached_data = get_transient($cache_key);
        
        if (false !== $cached_data) {
            return $cached_data;
        }
        
        $endpoint = "organizations/{$company_id}";
        $result = $this->make_api_request($endpoint);
        
        // Cache the result if not an error
        if (!is_wp_error($result)) {
            set_transient($cache_key, $result, $this->cache_expiration);
        }
        
        return $result;
    }
    
    /**
     * Get company page posts
     * 
     * @param string $company_id Company ID
     * @param array $args Query arguments
     * @return array|WP_Error Posts or error
     */
    public function get_company_posts($company_id, $args = []) {
        // Check cache first
        $cache_key = 'mainwp_linkedin_posts_' . $this->website->id . '_' . $company_id . '_' . md5(serialize($args));
        $cached_data = get_transient($cache_key);
        
        if (false !== $cached_data) {
            return $cached_data;
        }
        
        $endpoint = "organizations/{$company_id}/posts";
        $result = $this->make_api_request($endpoint, 'GET', $args);
        
        // Cache the result if not an error
        if (!is_wp_error($result)) {
            set_transient($cache_key, $result, $this->cache_expiration);
        }
        
        return $result;
    }
    
    /**
     * Create a company page post
     * 
     * @param string $company_id Company ID
     * @param array $post_data Post data
     * @return array|WP_Error Post data or error
     */
    public function create_company_post($company_id, $post_data) {
        // Clear posts cache
        $this->clear_posts_cache($company_id);
        
        $endpoint = "organizations/{$company_id}/posts";
        return $this->make_api_request($endpoint, 'POST', $post_data);
    }
    
    /**
     * Clear posts cache for a company
     * 
     * @param string $company_id Company ID
     */
    private function clear_posts_cache($company_id) {
        global $wpdb;
        
        // Find and delete all posts cache transients for this company
        $like = $wpdb->esc_like('_transient_mainwp_linkedin_posts_' . $this->website->id . '_' . $company_id) . '%';
        $wpdb->query($wpdb->prepare("DELETE FROM $wpdb->options WHERE option_name LIKE %s", $like));
    }
    
    /**
     * Make an API request to the LinkedIn REST API
     * 
     * @param string $endpoint API endpoint
     * @param string $method HTTP method
     * @param array $args Request arguments
     * @return array|WP_Error Response or error
     */
    private function make_api_request($endpoint, $method = 'GET', $args = []) {
        // Prepare the request data for MainWP
        $data = [
            'linkedin_api' => true,
            'endpoint' => $endpoint,
            'method' => $method,
            'args' => $args,
            'client_id' => $this->client_id,
            'client_secret' => $this->client_secret,
            'access_token' => $this->access_token
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'linkedin_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                $error_message = $information['error'];
                // Log error if WP_DEBUG_LOG is enabled
                if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                    error_log(sprintf(
                        '[MainWP LinkedIn] API Error: %s (Endpoint: %s, Method: %s, Site ID: %d)',
                        $error_message,
                        $endpoint,
                        $method,
                        $this->website->id
                    ));
                }
                return new WP_Error('api_error', $error_message);
            }
            
            return $information;
        } catch (Exception $e) {
            $error_message = $e->getMessage();
            // Log exception if WP_DEBUG_LOG is enabled
            if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                error_log(sprintf(
                    '[MainWP LinkedIn] API Exception: %s (Endpoint: %s, Method: %s, Site ID: %d)',
                    $error_message,
                    $endpoint,
                    $method,
                    $this->website->id
                ));
            }
            return new WP_Error('api_error', $error_message);
        }
    }
}
```

## Step-by-Step Implementation

1. **Create the Plugin File**
   - Create a new PHP file in your WordPress plugins directory
   - Copy the code above into the file
   - Customize the plugin header information

2. **Set Up LinkedIn API Access**
   - Create a LinkedIn Developer account at [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
   - Create a new application
   - Request the necessary API permissions:
     - r_organization_social
     - w_organization_social
     - r_liteprofile
   - Note your Client ID and Client Secret

3. **Configure the Integration**
   - Activate the plugin in your MainWP Dashboard
   - Go to the LinkedIn Settings page
   - Enter the API credentials for each child site
   - Test the connection

4. **Use the Integration**
   - Navigate to the LinkedIn dashboard page
   - View and manage LinkedIn content across your network
   - Create and schedule posts

## Common Pitfalls to Avoid

1. **API Authentication Issues**
   - Ensure your API credentials are correct
   - Verify that your application has the necessary permissions
   - Check that your redirect URLs are properly configured

2. **Rate Limiting**
   - Implement caching to reduce API calls
   - Handle rate limit errors gracefully
   - Use exponential backoff for retries

3. **Security Concerns**
   - Always validate and sanitize user input
   - Store API credentials securely
   - Use proper capability checks (manage_options)
   - Implement nonce verification for forms

4. **Performance Issues**
   - Cache API responses appropriately
   - Use pagination for large datasets
   - Implement background processing for long-running tasks

## Next Steps

For more detailed information and advanced features, refer to:
- [Complete Social Media Integration Guide](social-media-integration.md)
- [Advanced Social Media Integration Features](social-media-integration-part2.md)

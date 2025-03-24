# MainWP WooCommerce Integration: Quick Start Guide

This quick start guide provides the essential code and steps to implement a MainWP WooCommerce integration. For more detailed explanations and advanced features, see the [complete WooCommerce Integration guide](woocommerce-integration.md).

## Prerequisites

- WordPress with MainWP Dashboard installed
- WooCommerce installed on child sites
- Basic understanding of WordPress plugin development

## Quick Implementation

```php
<?php
/**
 * Plugin Name: MainWP WooCommerce Integration
 * Plugin URI: https://yourwebsite.com/mainwp-woocommerce
 * Description: Integrates MainWP with WooCommerce for centralized store management.
 * Version: 1.0.0
 * Author: Your Name
 * Author URI: https://yourwebsite.com
 * Text Domain: mainwp-woocommerce
 * WC requires at least: 5.0.0
 * WC tested up to: 8.0.0
 */

namespace YourCompany\MainWPWooCommerce;

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
        'api' => 'MainWPWooCommerce',
        'mainwp' => true,
        'callback' => [__NAMESPACE__ . '\\MainWPWooCommerce', 'get_instance'],
        'name' => 'WooCommerce Integration'
    ];
    return $extensions;
});

class MainWPWooCommerce {
    /** @var MainWPWooCommerce|null Instance */
    private static $instance = null;
    /** @var WooCommerceAPIClient|null API Client */
    private $api_client = null;
    
    /**
     * Get singleton instance
     * @return MainWPWooCommerce Instance of the plugin
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
        
        // Hook into site sync to collect WooCommerce data
        add_action('mainwp_site_synced', [$this, 'site_synced'], 10, 2);
        
        // Add WooCommerce data to individual site view
        add_filter('mainwp_getsubpages_sites', [$this, 'add_woocommerce_site_tab'], 10, 2);
    }
    
    /**
     * Initialize admin functionality
     */
    public function admin_init() {
        // Register settings
        register_setting('mainwp_woocommerce_settings_group', 'mainwp_woocommerce_settings');
    }
    
    /**
     * Initialize menu items
     */
    public function init_menu() {
        // Add WooCommerce dashboard page
        add_submenu_page(
            'mainwp_tab',
            __('WooCommerce', 'mainwp-woocommerce'),
            __('WooCommerce', 'mainwp-woocommerce'),
            'manage_options', // Use manage_options instead of read for better security
            'MainWPWooCommerce',
            [$this, 'render_dashboard_page']
        );
        
        // Add settings page
        add_submenu_page(
            'mainwp_tab',
            __('WooCommerce Settings', 'mainwp-woocommerce'),
            __('WooCommerce Settings', 'mainwp-woocommerce'),
            'manage_options', // Use manage_options instead of read for better security
            'MainWPWooCommerceSettings',
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
        // Check if WooCommerce data is available
        if (isset($data['woocommerce'])) {
            // Store the WooCommerce data for this site
            update_option('mainwp_woocommerce_data_' . $website->id, $data['woocommerce']);
        }
    }
    
    /**
     * Add WooCommerce tab to individual site view
     * 
     * @param array $subpages Current subpages
     * @param object $website The website object
     * @return array Modified subpages
     */
    public function add_woocommerce_site_tab($subpages, $website) {
        $subpages[] = [
            'title' => __('WooCommerce', 'mainwp-woocommerce'),
            'slug' => 'WooCommerce',
            'callback' => [$this, 'render_site_woocommerce_tab'],
        ];
        return $subpages;
    }
    
    /**
     * Get WooCommerce API client for a specific site
     * 
     * @param int $website_id The website ID
     * @return WooCommerceAPIClient|null API client or null on failure
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
        $settings = get_option('mainwp_woocommerce_settings', []);
        $site_settings = isset($settings[$website_id]) ? $settings[$website_id] : [];
        
        if (empty($site_settings['consumer_key']) || empty($site_settings['consumer_secret'])) {
            return null;
        }
        
        // Create API client
        return new WooCommerceAPIClient(
            $website,
            $site_settings['consumer_key'],
            $site_settings['consumer_secret']
        );
    }
    
    /**
     * Save API credentials for a site
     * 
     * @param int $website_id The website ID
     * @param string $consumer_key WooCommerce API consumer key
     * @param string $consumer_secret WooCommerce API consumer secret
     * @return bool Success or failure
     */
    public function save_api_credentials($website_id, $consumer_key, $consumer_secret) {
        // Validate inputs
        $website_id = absint($website_id);
        if ($website_id <= 0) {
            return false;
        }
        
        $consumer_key = sanitize_text_field($consumer_key);
        $consumer_secret = sanitize_text_field($consumer_secret);
        
        // Get current settings
        $settings = get_option('mainwp_woocommerce_settings', []);
        
        // Update settings for this site
        $settings[$website_id] = [
            'consumer_key' => $consumer_key,
            'consumer_secret' => $consumer_secret
        ];
        
        // Save settings
        return update_option('mainwp_woocommerce_settings', $settings);
    }
    
    // Additional methods for rendering pages and handling API requests...
}

/**
 * WooCommerce API Client
 */
class WooCommerceAPIClient {
    /** @var object Website object */
    private $website;
    /** @var string Consumer key */
    private $consumer_key;
    /** @var string Consumer secret */
    private $consumer_secret;
    
    /**
     * Constructor
     * 
     * @param object $website Website object
     * @param string $consumer_key WooCommerce API consumer key
     * @param string $consumer_secret WooCommerce API consumer secret
     */
    public function __construct($website, $consumer_key, $consumer_secret) {
        $this->website = $website;
        $this->consumer_key = $consumer_key;
        $this->consumer_secret = $consumer_secret;
    }
    
    /**
     * Get products from the WooCommerce store
     * 
     * @param array $args Query arguments
     * @return array|WP_Error Products or error
     */
    public function get_products($args = []) {
        // Ensure args is an array
        $args = is_array($args) ? $args : [];
        
        return $this->make_api_request('products', 'GET', $args);
    }
    
    /**
     * Get orders from the WooCommerce store
     * 
     * @param array $args Query arguments
     * @return array|WP_Error Orders or error
     */
    public function get_orders($args = []) {
        // Ensure args is an array
        $args = is_array($args) ? $args : [];
        
        return $this->make_api_request('orders', 'GET', $args);
    }
    
    /**
     * Make an API request to the WooCommerce REST API
     * 
     * @param string $endpoint API endpoint
     * @param string $method HTTP method
     * @param array $args Request arguments
     * @return array|WP_Error Response or error
     */
    private function make_api_request($endpoint, $method = 'GET', $args = []) {
        // Prepare the request data for MainWP
        $data = [
            'wc_api' => true,
            'endpoint' => $endpoint,
            'method' => $method,
            'args' => $args,
            'consumer_key' => $this->consumer_key,
            'consumer_secret' => $this->consumer_secret
        ];
        
        try {
            // Send the request through MainWP
            $information = MainWP_Connect::fetch_url_authed(
                $this->website,
                'woocommerce_integration',
                $data
            );
            
            // Check for errors in the response
            if (is_array($information) && isset($information['error'])) {
                $error_message = $information['error'];
                // Log error if WP_DEBUG_LOG is enabled
                if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                    error_log(sprintf(
                        '[MainWP WooCommerce] API Error: %s (Endpoint: %s, Method: %s, Site ID: %d)',
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
                    '[MainWP WooCommerce] API Exception: %s (Endpoint: %s, Method: %s, Site ID: %d)',
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

2. **Set Up WooCommerce API Access**
   - On each child site, go to WooCommerce → Settings → Advanced → REST API
   - Click "Add key"
   - Enter a description (e.g., "MainWP Integration")
   - Set permissions to "Read/Write"
   - Click "Generate API key"
   - Save the Consumer Key and Consumer Secret

3. **Configure the Integration**
   - Activate the plugin in your MainWP Dashboard
   - Go to the WooCommerce Settings page
   - Enter the API credentials for each child site
   - Test the connection

4. **Use the Integration**
   - Navigate to the WooCommerce dashboard page
   - View and manage WooCommerce data across your network
   - Perform bulk operations on products and orders

## Common Pitfalls to Avoid

1. **API Authentication Issues**
   - Ensure your API credentials are correct
   - Verify that your child sites have WooCommerce REST API enabled
   - Check that your permissions are set correctly (Read/Write)

2. **Performance Considerations**
   - Implement caching to reduce API calls
   - Use pagination for large datasets
   - Consider background processing for bulk operations

3. **Security Best Practices**
   - Always use HTTPS for API communication
   - Store API credentials securely
   - Validate and sanitize all user input
   - Use proper capability checks (manage_options)

## Next Steps

For more detailed information and advanced features, refer to:
- [Complete WooCommerce Integration Guide](woocommerce-integration.md)
- [Advanced WooCommerce Integration Features](woocommerce-integration-part2.md)

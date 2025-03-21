## Step 4: Advanced Integration Techniques

### Handling WooCommerce Webhooks

WooCommerce webhooks can be used to receive real-time notifications about events in your WooCommerce stores:

```php
/**
 * Register webhook handlers
 */
public function register_webhook_handlers() {
    // Register webhook endpoint
    add_action('rest_api_init', function() {
        register_rest_route('mainwp-woocommerce/v1', '/webhook/(?P<website_id>\d+)', array(
            'methods' => 'POST',
            'callback' => array($this, 'handle_webhook'),
            'permission_callback' => array($this, 'verify_webhook'),
        ));
    });
}

/**
 * Verify webhook request
 * 
 * @param WP_REST_Request $request Request object
 * @return bool Whether the request is valid
 */
public function verify_webhook($request) {
    // Validate website ID
    $website_id = absint($request->get_param('website_id'));
    if ($website_id <= 0) {
        return false;
    }
    
    $signature = $request->get_header('X-WC-Webhook-Signature');
    if (empty($signature)) {
        // Log missing signature if WP_DEBUG_LOG is enabled
        if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
            error_log(sprintf(
                '[MainWP WooCommerce] Missing webhook signature for website ID: %d',
                $website_id
            ));
        }
        return false;
    }
    
    // Get webhook secret for this site
    $settings = get_option('mainwp_woocommerce_settings', array());
    $site_settings = isset($settings[$website_id]) ? $settings[$website_id] : array();
    
    if (empty($site_settings['webhook_secret'])) {
        // Log missing webhook secret if WP_DEBUG_LOG is enabled
        if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
            error_log(sprintf(
                '[MainWP WooCommerce] Webhook secret not configured for website ID: %d',
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
 * Handle webhook request
 * 
 * @param WP_REST_Request $request Request object
 * @return WP_REST_Response Response object
 */
public function handle_webhook($request) {
    $website_id = absint($request->get_param('website_id'));
    $payload = json_decode($request->get_body(), true);
    
    if (!$payload || !isset($payload['topic'])) {
        return new WP_REST_Response(array(
            'success' => false,
            'message' => 'Invalid payload or missing topic'
        ), 400);
    }
    
    try {
        // Process webhook based on topic
        switch ($payload['topic']) {
            case 'order.created':
                $this->process_new_order($website_id, $payload['data']);
                break;
            case 'product.updated':
                $this->process_product_update($website_id, $payload['data']);
                break;
            default:
                // Log unknown topic if WP_DEBUG_LOG is enabled
                if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                    error_log(sprintf(
                        '[MainWP WooCommerce] Unknown webhook topic: %s for website ID: %d',
                        $payload['topic'],
                        $website_id
                    ));
                }
                return new WP_REST_Response(array(
                    'success' => false,
                    'message' => 'Unknown webhook topic'
                ), 400);
        }
        
        return new WP_REST_Response(array('success' => true));
    } catch (\Exception $e) {
        // Log exception if WP_DEBUG_LOG is enabled
        if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
            error_log(sprintf(
                '[MainWP WooCommerce] Webhook processing error: %s for website ID: %d',
                $e->getMessage(),
                $website_id
            ));
        }
        
        return new WP_REST_Response(array(
            'success' => false,
            'message' => 'Error processing webhook: ' . $e->getMessage()
        ), 500);
    }
}

/**
 * Process new order webhook
 * 
 * @param int $website_id Website ID
 * @param array $data Order data
 */
private function process_new_order($website_id, $data) {
    // Validate inputs
    $website_id = absint($website_id);
    if ($website_id <= 0 || empty($data) || !is_array($data)) {
        return;
    }
    
    // Process new order
    // For example, send notification, update dashboard, etc.
}
```

### Implementing Background Processing

For operations that may take a long time, implement background processing:

```php
/**
 * Schedule background sync
 */
public function schedule_background_sync() {
    if (!wp_next_scheduled('mainwp_woocommerce_background_sync')) {
        wp_schedule_event(time(), 'hourly', 'mainwp_woocommerce_background_sync');
    }
    
    // Hook into the scheduled event
    add_action('mainwp_woocommerce_background_sync', array($this, 'do_background_sync'));
}

/**
 * Perform background sync
 */
public function do_background_sync() {
    // Get all websites with WooCommerce
    $websites = \MainWP\Dashboard\MainWP_DB::instance()->get_websites_by_plugin_name('woocommerce/woocommerce.php');
    
    foreach ($websites as $website) {
        // Skip sites without API credentials
        $api_client = $this->get_api_client($website->id);
        if (!$api_client) {
            continue;
        }
        
        // Sync products
        $this->sync_products($website->id, $api_client);
        
        // Sync orders
        $this->sync_orders($website->id, $api_client);
        
        // Sync other data as needed
    }
}

/**
 * Sync products for a site
 * 
 * @param int $website_id Website ID
 * @param WooCommerceAPIClient $api_client API client
 */
private function sync_products($website_id, $api_client) {
    // Get products from the site
    $products = $api_client->get_products(array('per_page' => 100));
    
    if (is_wp_error($products)) {
        // Log error
        return;
    }
    
    // Process products
    // For example, store in database, update inventory, etc.
}
```

### Synchronizing Inventory Across Stores

Implement inventory synchronization across multiple stores:

```php
/**
 * Synchronize inventory across stores
 * 
 * @param array $website_ids Array of website IDs to sync
 * @param array $product_data Array of product IDs and stock quantities
 * @return array Results
 */
public function sync_inventory($website_ids, $product_data) {
    $results = array();
    
    foreach ($website_ids as $website_id) {
        $api_client = $this->get_api_client($website_id);
        if (!$api_client) {
            $results[$website_id] = array(
                'success' => false,
                'message' => 'API credentials not configured'
            );
            continue;
        }
        
        $product_manager = new ProductManager($api_client);
        $site_results = array();
        
        foreach ($product_data as $product_id => $stock_quantity) {
            $result = $product_manager->update_stock($product_id, $stock_quantity);
            
            $site_results[$product_id] = array(
                'success' => !is_wp_error($result),
                'message' => is_wp_error($result) ? $result->get_error_message() : 'Success'
            );
        }
        
        $results[$website_id] = $site_results;
    }
    
    return $results;
}
```

## Common Challenges and Solutions

### API Authentication Issues

If you encounter API authentication issues:

1. **Check API Keys**: Ensure the Consumer Key and Consumer Secret are correct.
2. **Verify Permissions**: Make sure the API keys have the necessary permissions.
3. **Check SSL**: WooCommerce API requires SSL for secure connections.

```php
/**
 * Troubleshoot API connection
 * 
 * @param int $website_id Website ID
 * @return array Troubleshooting results
 */
public function troubleshoot_api_connection($website_id) {
    $results = array();
    
    // Check if website exists
    $website = \MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        $results['website'] = 'Website not found';
        return $results;
    }
    
    // Check if WooCommerce is active
    $is_woocommerce_active = \MainWP\Dashboard\MainWP_DB::instance()->is_plugin_active_on_site($website_id, 'woocommerce/woocommerce.php');
    $results['woocommerce'] = $is_woocommerce_active ? 'Active' : 'Not active';
    
    // Check API credentials
    $settings = get_option('mainwp_woocommerce_settings', array());
    $site_settings = isset($settings[$website_id]) ? $settings[$website_id] : array();
    
    $results['api_credentials'] = (!empty($site_settings['consumer_key']) && !empty($site_settings['consumer_secret'])) ? 'Configured' : 'Not configured';
    
    // Test API connection
    if ($results['api_credentials'] === 'Configured') {
        $api_client = $this->get_api_client($website_id);
        $test_result = $api_client->get_store_info();
        
        $results['api_connection'] = !is_wp_error($test_result) ? 'Success' : 'Failed: ' . $test_result->get_error_message();
    }
    
    return $results;
}
```

### Handling Large Product Catalogs

For stores with large product catalogs:

1. **Implement Pagination**: Use pagination to retrieve products in batches.
2. **Optimize Caching**: Cache product data to reduce API calls.
3. **Use Background Processing**: Process large catalogs in the background.

```php
/**
 * Get all products with pagination
 * 
 * @param int $website_id Website ID
 * @return array|WP_Error Products or error
 */
public function get_all_products($website_id) {
    $api_client = $this->get_api_client($website_id);
    if (!$api_client) {
        return new \WP_Error('api_error', 'API credentials not configured');
    }
    
    $all_products = array();
    $page = 1;
    $per_page = 100;
    
    while (true) {
        $products = $api_client->get_products(array(
            'page' => $page,
            'per_page' => $per_page
        ));
        
        if (is_wp_error($products)) {
            return $products;
        }
        
        if (empty($products)) {
            break;
        }
        
        $all_products = array_merge($all_products, $products);
        $page++;
    }
    
    return $all_products;
}
```

### Managing Different WooCommerce Versions

To handle different WooCommerce versions across your network:

1. **Version Detection**: Detect WooCommerce version on each site.
2. **Conditional Logic**: Implement conditional logic based on version.
3. **Fallback Mechanisms**: Provide fallback mechanisms for older versions.

```php
/**
 * Get WooCommerce version for a site
 * 
 * @param int $website_id Website ID
 * @return string|WP_Error WooCommerce version or error
 */
public function get_woocommerce_version($website_id) {
    $website = \MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return new \WP_Error('website_error', 'Website not found');
    }
    
    // Get plugin data from the site
    $plugins = json_decode($website->plugins, true);
    if (!$plugins) {
        return new \WP_Error('plugins_error', 'Unable to get plugins data');
    }
    
    // Find WooCommerce plugin
    foreach ($plugins as $plugin) {
        if ($plugin['slug'] === 'woocommerce/woocommerce.php') {
            return $plugin['version'];
        }
    }
    
    return new \WP_Error('woocommerce_error', 'WooCommerce not found');
}

/**
 * Check if WooCommerce version is compatible
 * 
 * @param string $version WooCommerce version
 * @param string $min_version Minimum required version
 * @return bool Whether the version is compatible
 */
public function is_woocommerce_compatible($version, $min_version = '3.0.0') {
    return version_compare($version, $min_version, '>=');
}
```

## Example: Complete WooCommerce Integration

Here's a more complete example of a MainWP WooCommerce integration:

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
 * WC requires at least: 3.0.0
 * WC tested up to: 8.0.0
 */

namespace YourCompany\MainWPWooCommerce;

// Prevent direct access
if (!defined('ABSPATH')) {
    exit;
}

// Register the integration with MainWP
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'MainWPWooCommerce',
        'mainwp' => true,
        'callback' => array('YourCompany\\MainWPWooCommerce\\MainWPWooCommerce', 'get_instance'),
        'name' => 'WooCommerce Integration'
    );
    return $extensions;
});

class MainWPWooCommerce {
    /** @var MainWPWooCommerce|null Instance */
    private static $instance = null;
    /** @var array Managers */
    private $managers = array();
    
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
        add_action('admin_init', array($this, 'admin_init'));
        add_action('mainwp_admin_menu', array($this, 'init_menu'));
        
        // Hook into site sync to collect WooCommerce data
        add_action('mainwp_site_synced', array($this, 'site_synced'), 10, 2);
        
        // Add WooCommerce data to individual site view
        add_filter('mainwp_getsubpages_sites', array($this, 'add_woocommerce_site_tab'), 10, 2);
        
        // Register AJAX handlers
        add_action('wp_ajax_mainwp_woocommerce_get_products', array($this, 'ajax_get_products'));
        add_action('wp_ajax_mainwp_woocommerce_get_orders', array($this, 'ajax_get_orders'));
        add_action('wp_ajax_mainwp_woocommerce_update_product', array($this, 'ajax_update_product'));
        
        // Schedule background tasks
        $this->schedule_background_tasks();
    }
    
    /**
     * Initialize admin functionality
     */
    public function admin_init() {
        // Register settings
        register_setting('mainwp_woocommerce_settings_group', 'mainwp_woocommerce_settings');
        
        // Register scripts and styles
        add_action('admin_enqueue_scripts', array($this, 'enqueue_scripts'));
    }
    
    /**
     * Enqueue scripts and styles
     */
    public function enqueue_scripts() {
        // Only enqueue on our pages
        $screen = get_current_screen();
        if (!$screen || strpos($screen->id, 'mainwp-woocommerce') === false) {
            return;
        }
        
        wp_enqueue_style('mainwp-woocommerce-style', plugins_url('assets/css/style.css', __FILE__), array(), '1.0.0');
        wp_enqueue_script('mainwp-woocommerce-script', plugins_url('assets/js/script.js', __FILE__), array('jquery'), '1.0.0', true);
        
        wp_localize_script('mainwp-woocommerce-script', 'mainwpWooCommerce', array(
            'ajaxUrl' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('mainwp_woocommerce_nonce')
        ));
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
            'read',
            'MainWPWooCommerce',
            array($this, 'render_dashboard_page')
        );
        
        // Add settings page
        add_submenu_page(
            'mainwp_tab',
            __('WooCommerce Settings', 'mainwp-woocommerce'),
            __('WooCommerce Settings', 'mainwp-woocommerce'),
            'read',
            'MainWPWooCommerceSettings',
            array($this, 'render_settings_page')
        );
        
        // Add products page
        add_submenu_page(
            'mainwp_tab',
            __('WooCommerce Products', 'mainwp-woocommerce'),
            __('WooCommerce Products', 'mainwp-woocommerce'),
            'read',
            'MainWPWooCommerceProducts',
            array($this, 'render_products_page')
        );
        
        // Add orders page
        add_submenu_page(
            'mainwp_tab',
            __('WooCommerce Orders', 'mainwp-woocommerce'),
            __('WooCommerce Orders', 'mainwp-woocommerce'),
            'read',
            'MainWPWooCommerceOrders',
            array($this, 'render_orders_page')
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
        $subpages[] = array(
            'title' => __('WooCommerce', 'mainwp-woocommerce'),
            'slug' => 'WooCommerce',
            'callback' => array($this, 'render_site_woocommerce_tab'),
        );
        return $subpages;
    }
    
    /**
     * Render dashboard page
     */
    public function render_dashboard_page() {
        // Check if user has permissions
        if (!mainwp_current_user_can('read')) {
            mainwp_do_not_have_permissions(__('WooCommerce', 'mainwp-woocommerce'));
            return;
        }
        
        // Get WooCommerce sites
        $websites = \MainWP\Dashboard\MainWP_DB::instance()->get_websites_by_plugin_name('woocommerce/woocommerce.php');
        
        // Render dashboard
        ?>
        <div class="ui segment">
            <h2 class="ui header"><?php esc_html_e('WooCommerce Dashboard', 'mainwp-woocommerce'); ?></h2>
            
            <div class="ui grid">
                <div class="four wide column">
                    <div class="ui card">
                        <div class="content">
                            <div class="header"><?php esc_html_e('Total Stores', 'mainwp-woocommerce'); ?></div>
                            <div class="description">
                                <h2><?php echo count($websites); ?></h2>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="four wide column">
                    <div class="ui card">
                        <div class="content">
                            <div class="header"><?php esc_html_e('Total Sales', 'mainwp-woocommerce'); ?></div>
                            <div class="description">
                                <h2><?php echo $this->get_total_sales($websites); ?></h2>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="four wide column">
                    <div class="ui card">
                        <div class="content">
                            <div class="header"><?php esc_html_e('Total Orders', 'mainwp-woocommerce'); ?></div>
                            <div class="description">
                                <h2><?php echo $this->get_total_orders($websites); ?></h2>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="four wide column">
                    <div class="ui card">
                        <div class="content">
                            <div class="header"><?php esc_html_e('Total Products', 'mainwp-woocommerce'); ?></div>
                            <div class="description">
                                <h2><?php echo $this->get_total_products($websites); ?></h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <h3 class="ui header"><?php esc_html_e('Recent Orders', 'mainwp-woocommerce'); ?></h3>
            <table class="ui celled table">
                <thead>
                    <tr>
                        <th><?php esc_html_e('Store', 'mainwp-woocommerce'); ?></th>
                        <th><?php esc_html_e('Order', 'mainwp-woocommerce'); ?></th>
                        <th><?php esc_html_e('Customer', 'mainwp-woocommerce'); ?></th>
                        <th><?php esc_html_e('Status', 'mainwp-woocommerce'); ?></th>
                        <th><?php esc_html_e('Total', 'mainwp-woocommerce'); ?></th>
                        <th><?php esc_html_e('Date', 'mainwp-woocommerce'); ?></th>
                    </tr>
                </thead>
                <tbody>
                    <?php $this->render_recent_orders($websites); ?>
                </tbody>
            </table>
        </div>
        <?php
    }
    
    /**
     * Render settings page
     */
    public function render_settings_page() {
        // Check if user has permissions
        if (!mainwp_current_user_can('read')) {
            mainwp_do_not_have_permissions(__('WooCommerce Settings', 'mainwp-woocommerce'));
            return;
        }
        
        // Get WooCommerce sites
        $websites = \MainWP\Dashboard\MainWP_DB::instance()->get_websites_by_plugin_name('woocommerce/woocommerce.php');
        
        // Get current settings
        $settings = get_option('mainwp_woocommerce_settings', array());
        
        // Save settings if form is submitted
        if (isset($_POST['submit'])) {
            // Verify nonce
            check_admin_referer('mainwp_woocommerce_settings_nonce', 'mainwp_woocommerce_settings_nonce');
            
            // Process settings for each site
            foreach ($websites as $website) {
                $site_settings = array(
                    'consumer_key' => sanitize_text_field($_POST['consumer_key_' . $website->id] ?? ''),
                    'consumer_secret' => sanitize_text_field($_POST['consumer_secret_' . $website->id] ?? ''),
                    'webhook_secret' => sanitize_text_field($_POST['webhook_secret_' . $website->id] ?? '')
                );
                
                $settings[$website->id] = $site_settings;
            }
            
            // Save settings
            update_option('mainwp_woocommerce_settings', $settings);
            
            // Show success message
            ?>
            <div class="ui green message"><?php esc_html_e('Settings saved successfully.', 'mainwp-woocommerce'); ?></div>
            <?php
        }
        
        // Render settings form
        ?>
        <div class="ui segment">
            <h2 class="ui header"><?php esc_html_e('WooCommerce Settings', 'mainwp-woocommerce'); ?></h2>
            
            <form class="ui form" method="post" action="">
                <?php wp_nonce_field('mainwp_woocommerce_settings_nonce', 'mainwp_woocommerce_settings_nonce'); ?>
                
                <div class="ui accordion">
                    <?php foreach ($websites as $website) : ?>
                        <?php
                        $site_settings = isset($settings[$website->id]) ? $settings[$website->id] : array(
                            'consumer_key' => '',
                            'consumer_secret' => '',
                            'webhook_secret' => ''
                        );
                        ?>
                        <div class="title">
                            <i class="dropdown icon"></i>
                            <?php echo esc_html($website->name); ?>
                        </div>
                        <div class="content">
                            <div class="field">
                                <label><?php esc_html_e('Consumer Key', 'mainwp-woocommerce'); ?></label>
                                <input type="text" name="consumer_key_<?php echo $website->id; ?>" value="<?php echo esc_attr($site_settings['consumer_key']); ?>">
                                <p class="description"><?php esc_html_e('Enter the WooCommerce API Consumer Key for this site.', 'mainwp-woocommerce'); ?></p>
                            </div>
                            
                            <div class="field">
                                <label><?php esc_html_e('Consumer Secret', 'mainwp-woocommerce'); ?></label>
                                <input type="password" name="consumer_secret_<?php echo $website->id; ?>" value="<?php echo esc_attr($site_settings['consumer_secret']); ?>">
                                <p class="description"><?php esc_html_e('Enter the WooCommerce API Consumer Secret for this site.', 'mainwp-woocommerce'); ?></p>
                            </div>
                            
                            <div class="field">
                                <label><?php esc_html_e('Webhook Secret', 'mainwp-woocommerce'); ?></label>
                                <input type="password" name="webhook_secret_<?php echo $website->id; ?>" value="<?php echo esc_attr($site_settings['webhook_secret']); ?>">
                                <p class="description"><?php esc_html_e('Enter the WooCommerce Webhook Secret for this site.', 'mainwp-woocommerce'); ?></p>
                            </div>
                            
                            <div class="field">
                                <button class="ui button test-connection" data-website-id="<?php echo $website->id; ?>"><?php esc_html_e('Test Connection', 'mainwp-woocommerce'); ?></button>
                                <span class="connection-status" id="connection-status-<?php echo $website->id; ?>"></span>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
                
                <button class="ui green button" type="submit" name="submit"><?php esc_html_e('Save Settings', 'mainwp-woocommerce'); ?></button>
            </form>
        </div>
        
        <script type="text/javascript">
        jQuery(document).ready(function($) {
            $('.ui.accordion').accordion();
            
            $('.test-connection').on('click', function(e) {
                e.preventDefault();
                
                var button = $(this);
                var websiteId = button.data('website-id');
                var statusElement = $('#connection-status-' + websiteId);
                
                button.addClass('loading');
                statusElement.html('');
                
                $.ajax({
                    url: ajaxurl,
                    type: 'POST',
                    data: {
                        action: 'mainwp_woocommerce_test_connection',
                        website_id: websiteId,
                        nonce: mainwpWooCommerce.nonce
                    },
                    success: function(response) {
                        button.removeClass('loading');
                        
                        if (response.success) {
                            statusElement.html('<span class="ui green text">' + response.data.message + '</span>');
                        } else {
                            statusElement.html('<span class="ui red text">' + response.data.message + '</span>');
                        }
                    },
                    error: function() {
                        button.removeClass('loading');
                        statusElement.html('<span class="ui red text">Error: Unable to test connection</span>');
                    }
                });
            });
        });
        </script>
        <?php
    }
    
    // Additional methods for rendering pages, handling AJAX requests, etc.
}

// Initialize the plugin
MainWPWooCommerce::get_instance();
```

## Additional Best Practices

### Error Handling Best Practices

1. **Log Meaningful Errors**: Include context information in error logs to make troubleshooting easier:
   ```php
   if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
       error_log(sprintf(
           '[MainWP WooCommerce] API Error: %s (Endpoint: %s, Method: %s, Site ID: %d)',
           $error_message,
           $endpoint,
           $method,
           $this->website->id
       ));
   }
   ```

2. **Implement Graceful Degradation**: Design your integration to continue functioning (perhaps with limited features) even when API calls fail:
   ```php
   public function get_products($args = array()) {
       $products = $this->api_client->get_products($args);
       
       // Return empty array instead of error
       if (is_wp_error($products)) {
           // Log the error for troubleshooting
           if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
               error_log(sprintf(
                   '[MainWP WooCommerce] Failed to get products: %s',
                   $products->get_error_message()
               ));
           }
           return array();
       }
       
       // Continue processing products
       return $products;
   }
   ```

3. **Provide User-Friendly Error Messages**: Convert technical errors into actionable messages for administrators:
   ```php
   public function render_dashboard_page() {
       // Get WooCommerce sites
       $websites = \MainWP\Dashboard\MainWP_DB::instance()->get_websites_by_plugin_name('woocommerce/woocommerce.php');
       
       // Check for sites without API credentials
       $sites_without_credentials = array();
       foreach ($websites as $website) {
           $api_client = $this->get_api_client($website->id);
           if (!$api_client) {
               $sites_without_credentials[] = $website->name;
           }
       }
       
       // Show notice if some sites are missing credentials
       if (!empty($sites_without_credentials)) {
           ?>
           <div class="ui yellow message">
               <p><?php esc_html_e('The following sites are missing WooCommerce API credentials:', 'mainwp-woocommerce'); ?></p>
               <ul>
                   <?php foreach ($sites_without_credentials as $site_name) : ?>
                       <li><?php echo esc_html($site_name); ?></li>
                   <?php endforeach; ?>
               </ul>
               <p><?php esc_html_e('Please configure API credentials in the settings page.', 'mainwp-woocommerce'); ?></p>
           </div>
           <?php
       }
       
       // Rest of the function...
   }
   ```

### Maintenance Best Practices

1. **Version Compatibility Checking**: Check WooCommerce version compatibility before performing operations:
   ```php
   public function is_site_compatible($website_id) {
       $version = $this->get_woocommerce_version($website_id);
       if (is_wp_error($version)) {
           return false;
       }
       
       return version_compare($version, '3.0.0', '>=');
   }
   ```

2. **Implement Admin Notices**: Display admin notices for configuration issues or API errors:
   ```php
   public function admin_notices() {
       // Only show on our pages
       $screen = get_current_screen();
       if (!$screen || strpos($screen->id, 'mainwp-woocommerce') === false) {
           return;
       }
       
       // Check for sites with WooCommerce but no API credentials
       $websites = \MainWP\Dashboard\MainWP_DB::instance()->get_websites_by_plugin_name('woocommerce/woocommerce.php');
       $unconfigured_sites = 0;
       
       foreach ($websites as $website) {
           $api_client = $this->get_api_client($website->id);
           if (!$api_client) {
               $unconfigured_sites++;
           }
       }
       
       if ($unconfigured_sites > 0) {
           ?>
           <div class="notice notice-warning">
               <p>
                   <?php printf(
                       esc_html__('%d WooCommerce sites are missing API credentials. Please configure them in the %sWooCommerce Settings%s.', 'mainwp-woocommerce'),
                       $unconfigured_sites,
                       '<a href="' . admin_url('admin.php?page=MainWPWooCommerceSettings') . '">',
                       '</a>'
                   ); ?>
               </p>
           </div>
           <?php
       }
   }
   ```

3. **Use Background Processing Libraries**: For complex operations, consider using libraries like Action Scheduler or WP Background Processing:
   ```php
   // Example using Action Scheduler
   public function schedule_inventory_sync($product_ids, $website_ids) {
       foreach ($product_ids as $product_id) {
           foreach ($website_ids as $website_id) {
               as_schedule_single_action(
                   time(),
                   'mainwp_woocommerce_sync_product_inventory',
                   array(
                       'product_id' => $product_id,
                       'website_id' => $website_id
                   )
               );
           }
       }
   }
   ```

## Next Steps and Resources

After implementing your WooCommerce integration, you might want to explore:

- **Advanced Reporting**: Implement more advanced reporting features.
- **Custom Dashboards**: Create custom dashboards for specific WooCommerce data.
- **Bulk Operations**: Implement more bulk operations for managing products and orders.
- **Automated Tasks**: Set up automated tasks for common WooCommerce operations.

### Resources

- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [MainWP Developer Documentation](https://mainwp.com/developer/)
- [WordPress Plugin Development](https://developer.wordpress.org/plugins/)
- [WooCommerce Developer Resources](https://woocommerce.com/documentation/plugins/woocommerce/woocommerce-developer-resources/)

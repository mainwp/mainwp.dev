# Creating a Basic MainWP Integration

This guide walks you through the process of creating a basic MainWP integration that connects with a third-party plugin or API. By the end, you'll have a functional integration that extends MainWP with third-party capabilities.

## Quick Start for Experienced Developers

```php
// 1. Clone the development extension
// git clone https://github.com/mainwp/mainwp-development-extension.git my-integration

// 2. Rename files and update plugin header
// mainwp-development-extension.php → my-integration.php

// 3. Update namespace and class names
namespace MyCompany\MyIntegration;

// 4. Register your integration with MainWP
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'MyIntegration',
        'mainwp' => true,
        'callback' => array('MyCompany\\MyIntegration\\MyIntegration', 'get_instance'),
        'name' => 'My Integration'
    );
    return $extensions;
});

// 5. Implement core functionality in your main class
class MyIntegration {
    public static function get_instance() {
        static $instance = null;
        if (null === $instance) {
            $instance = new self();
        }
        return $instance;
    }
    
    public function __construct() {
        // Hook into MainWP actions and filters
        add_action('mainwp_pageheader_extensions', array($this, 'page_header'));
        add_action('mainwp_pagefooter_extensions', array($this, 'page_footer'));
        
        // Initialize third-party API connection
        $this->init_api_connection();
    }
    
    private function init_api_connection() {
        // Initialize connection to third-party API
        // Check if required third-party plugin is active
        if ($this->is_third_party_plugin_active()) {
            // Set up API credentials
            $this->api_key = get_option('my_integration_api_key', '');
            // Initialize API client
            $this->api_client = new ApiClient($this->api_key);
        }
    }
    
    private function is_third_party_plugin_active() {
        // Check if the required third-party plugin is active
        return is_plugin_active('third-party-plugin/third-party-plugin.php');
    }
    
    // Implement required methods...
}
```

## Prerequisites

Before you begin creating a MainWP integration, ensure you have:

- A development environment with WordPress and MainWP Dashboard installed (see [Setting Up a Development Environment](setup-environment.md))
- Basic understanding of WordPress plugin development
- Familiarity with PHP object-oriented programming
- A code editor (like VS Code, PhpStorm, or Sublime Text)
- Access to the third-party API or plugin you want to integrate with
- API credentials or documentation for the third-party service

## Step 1: Plan Your Integration

Before writing any code, clearly define what your integration will do:

1. **Purpose**: What problem will your integration solve for MainWP users?
2. **Features**: What specific functionality will it provide?
3. **Third-Party Requirements**: What API or plugin will you integrate with?
4. **Integration Points**: How will it interact with both MainWP and the third-party service?
5. **User Interface**: What admin pages, settings, or widgets will it need?

Having a clear plan will guide your development process and help you create a more focused, useful integration.

## Step 2: Start with the Development Extension

MainWP provides a development extension template that includes the basic structure and boilerplate code you need to get started quickly.

1. Clone or download the MainWP Development Extension from GitHub:
   ```bash
   git clone https://github.com/mainwp/mainwp-development-extension.git my-integration
   ```

2. Navigate to your new integration directory:
   ```bash
   cd my-integration
   ```

The development extension includes a well-structured codebase with classes for different aspects of extension functionality, making it easier to understand and extend.

## Step 3: Customize the Plugin Information

1. Rename the main plugin file from `mainwp-development-extension.php` to match your integration name (e.g., `my-integration.php`).

2. Update the plugin header information in the main file:

   ```php
   /**
    * Plugin Name: My Integration for MainWP
    * Plugin URI: https://yourwebsite.com/my-integration
    * Description: Integrates MainWP with [Third-Party Service/Plugin].
    * Version: 1.0
    * Author: Your Name
    * Author URI: https://yourwebsite.com
    * Text Domain: my-integration
    * Requires at least: 4.6
    * Requires PHP: 7.0
    * WC requires at least: 3.0 (if integrating with WooCommerce)
    * WC tested up to: 6.0 (if integrating with WooCommerce)
    */
   ```

3. Update the text domain throughout the plugin to match your integration's slug.

## Step 4: Update Namespace and Class Names

1. Change the namespace in all PHP files from `MainWP\Dev` to your own namespace (e.g., `MyCompany\MyIntegration`).

2. Rename the main class and other classes to match your integration name.

3. Update all references to these classes throughout the codebase.

For example:

```php
namespace MyCompany\MyIntegration;

class MyIntegration {
    // Class implementation
}
```

## Step 5: Register Your Integration with MainWP

MainWP uses a filter to discover and load extensions. Update the `mainwp_getextensions` filter in your main plugin file:

```php
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'MyIntegration',
        'mainwp' => true,
        'callback' => array('MyCompany\\MyIntegration\\MyIntegration', 'get_instance'),
        'name' => 'My Integration'
    );
    return $extensions;
});
```

This tells MainWP:
- The location of your plugin file
- The API identifier for your integration
- That this is a MainWP extension (not a third-party integration)
- The callback function to initialize your integration
- The display name of your integration

## Step 6: Add Third-Party Integration Code

This is where your integration differs from a standard extension. You'll need to add code to connect with the third-party API or plugin:

1. **Check for Third-Party Plugin**: If your integration requires a specific plugin, check if it's installed and activated:

```php
private function is_third_party_plugin_active() {
    // Check if the required third-party plugin is active
    if (!function_exists('is_plugin_active')) {
        include_once(ABSPATH . 'wp-admin/includes/plugin.php');
    }
    return is_plugin_active('third-party-plugin/third-party-plugin.php');
}
```

2. **Initialize API Connection**: Set up the connection to the third-party API:

```php
private function init_api_connection() {
    // Initialize connection to third-party API
    if ($this->is_third_party_plugin_active()) {
        // Set up API credentials
        $this->api_key = get_option('my_integration_api_key', '');
        // Initialize API client
        $this->api_client = new ApiClient($this->api_key);
    }
}
```

3. **Create API Client Class**: Create a dedicated class for handling API communication:

```php
class ApiClient {
    private $api_key;
    private $api_url = 'https://api.third-party-service.com/v1/';
    
    public function __construct($api_key) {
        $this->api_key = $api_key;
    }
    
    public function get_data($endpoint, $params = array()) {
        $url = $this->api_url . $endpoint;
        $args = array(
            'headers' => array(
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json'
            ),
            'timeout' => 30
        );
        
        if (!empty($params)) {
            $url = add_query_arg($params, $url);
        }
        
        $response = wp_remote_get($url, $args);
        
        if (is_wp_error($response)) {
            return array('error' => $response->get_error_message());
        }
        
        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }
    
    public function post_data($endpoint, $data) {
        $url = $this->api_url . $endpoint;
        $args = array(
            'headers' => array(
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json'
            ),
            'body' => json_encode($data),
            'method' => 'POST',
            'timeout' => 30
        );
        
        $response = wp_remote_post($url, $args);
        
        if (is_wp_error($response)) {
            return array('error' => $response->get_error_message());
        }
        
        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }
}
```

## Step 7: Create Settings Page for API Credentials

Most integrations require API credentials or configuration settings:

```php
public function render_settings_page() {
    // Check if user has permissions
    if (!mainwp_current_user_can('read')) {
        mainwp_do_not_have_permissions(__('My Integration Settings', 'my-integration'));
        return;
    }
    
    // Save settings if form is submitted
    if (isset($_POST['submit'])) {
        // Verify nonce
        check_admin_referer('my_integration_settings_nonce', 'my_integration_settings_nonce');
        
        // Save API key
        $api_key = sanitize_text_field($_POST['api_key'] ?? '');
        update_option('my_integration_api_key', $api_key);
        
        // Test API connection
        $test_result = $this->test_api_connection($api_key);
        
        if ($test_result['success']) {
            ?>
            <div class="ui green message"><?php esc_html_e('API connection successful.', 'my-integration'); ?></div>
            <?php
        } else {
            ?>
            <div class="ui red message"><?php echo esc_html($test_result['message']); ?></div>
            <?php
        }
    }
    
    // Get current settings
    $api_key = get_option('my_integration_api_key', '');
    
    // Render settings form
    ?>
    <div class="ui segment">
        <h2 class="ui header"><?php esc_html_e('My Integration Settings', 'my-integration'); ?></h2>
        <form class="ui form" method="post" action="">
            <?php wp_nonce_field('my_integration_settings_nonce', 'my_integration_settings_nonce'); ?>
            
            <div class="field">
                <label><?php esc_html_e('API Key', 'my-integration'); ?></label>
                <input type="text" name="api_key" value="<?php echo esc_attr($api_key); ?>">
                <p class="description"><?php esc_html_e('Enter your API key from your Third-Party Service account.', 'my-integration'); ?></p>
            </div>
            
            <button class="ui green button" type="submit" name="submit"><?php esc_html_e('Save Settings', 'my-integration'); ?></button>
        </form>
    </div>
    <?php
}

private function test_api_connection($api_key) {
    // Create temporary API client with the provided key
    $api_client = new ApiClient($api_key);
    
    // Try to make a simple API request
    $response = $api_client->get_data('test-endpoint');
    
    if (isset($response['error'])) {
        return array(
            'success' => false,
            'message' => sprintf(__('API connection failed: %s', 'my-integration'), $response['error'])
        );
    }
    
    return array(
        'success' => true,
        'message' => __('API connection successful.', 'my-integration')
    );
}
```

## Step 8: Implement Integration Features

Now implement the specific features of your integration. This will depend on what your integration does, but here are some common patterns:

### Syncing Data from Third-Party Service to MainWP

```php
public function sync_third_party_data() {
    // Get data from third-party API
    $data = $this->api_client->get_data('some-endpoint');
    
    if (isset($data['error'])) {
        // Handle error
        return;
    }
    
    // Process and store the data
    update_option('my_integration_synced_data', $data);
    update_option('my_integration_last_sync', current_time('mysql'));
}
```

### Sending MainWP Data to Third-Party Service

```php
public function send_data_to_third_party($website_id, $data) {
    // Get website details
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return array('error' => 'Website not found');
    }
    
    // Prepare data for third-party service
    $prepared_data = array(
        'website_name' => $website->name,
        'website_url' => $website->url,
        'custom_data' => $data
    );
    
    // Send data to third-party API
    $response = $this->api_client->post_data('some-endpoint', $prepared_data);
    
    return $response;
}
```

### Adding Integration-Specific UI Elements

```php
public function render_dashboard_widget() {
    // Get synced data
    $data = get_option('my_integration_synced_data', array());
    $last_sync = get_option('my_integration_last_sync', '');
    
    ?>
    <div class="ui segment">
        <h3 class="ui header"><?php esc_html_e('Third-Party Service Data', 'my-integration'); ?></h3>
        
        <?php if (!empty($last_sync)) : ?>
            <p><?php echo sprintf(__('Last synced: %s', 'my-integration'), $last_sync); ?></p>
        <?php endif; ?>
        
        <?php if (!empty($data)) : ?>
            <!-- Display data here -->
            <div class="ui list">
                <?php foreach ($data as $item) : ?>
                    <div class="item">
                        <?php echo esc_html($item['name']); ?>
                    </div>
                <?php endforeach; ?>
            </div>
        <?php else : ?>
            <p><?php esc_html_e('No data available. Please sync with the third-party service.', 'my-integration'); ?></p>
        <?php endif; ?>
        
        <button class="ui green button sync-button" data-nonce="<?php echo wp_create_nonce('my_integration_sync_nonce'); ?>">
            <?php esc_html_e('Sync Now', 'my-integration'); ?>
        </button>
    </div>
    
    <script type="text/javascript">
    jQuery(document).ready(function($) {
        $('.sync-button').on('click', function() {
            var button = $(this);
            button.addClass('loading');
            
            $.ajax({
                url: ajaxurl,
                type: 'POST',
                data: {
                    action: 'my_integration_sync',
                    nonce: button.data('nonce')
                },
                success: function(response) {
                    button.removeClass('loading');
                    if (response.success) {
                        location.reload();
                    } else {
                        alert(response.data.message);
                    }
                },
                error: function() {
                    button.removeClass('loading');
                    alert('An error occurred. Please try again.');
                }
            });
        });
    });
    </script>
    <?php
}
```

## Step 9: Handle Dependency Management

Your integration may depend on third-party libraries or plugins. Here's how to handle these dependencies:

### Check for Required Plugins

```php
public function check_required_plugins() {
    if (!$this->is_third_party_plugin_active()) {
        add_action('admin_notices', function() {
            ?>
            <div class="notice notice-error">
                <p><?php echo sprintf(__('My Integration requires the %s plugin to be installed and activated.', 'my-integration'), '<a href="https://example.com/third-party-plugin" target="_blank">Third-Party Plugin</a>'); ?></p>
            </div>
            <?php
        });
        return false;
    }
    return true;
}
```

### Include Third-Party Libraries

If your integration requires PHP libraries, you can use Composer to manage them:

1. Create a `composer.json` file in your integration directory:

```json
{
    "name": "mycompany/my-integration",
    "description": "MainWP integration with Third-Party Service",
    "type": "wordpress-plugin",
    "require": {
        "php": ">=7.0",
        "third-party/api-client": "^1.0"
    },
    "autoload": {
        "psr-4": {
            "MyCompany\\MyIntegration\\": "src/"
        }
    }
}
```

2. Install dependencies:

```bash
composer install --no-dev
```

3. Include the Composer autoloader in your main plugin file:

```php
if (file_exists(__DIR__ . '/vendor/autoload.php')) {
    require_once __DIR__ . '/vendor/autoload.php';
}
```

## Step 10: Test Your Integration

Thoroughly test your integration to ensure it works correctly:

1. Install and activate it on a test MainWP Dashboard.
2. Configure the API credentials or third-party plugin settings.
3. Test all features and functionality.
4. Check for any errors or warnings in the browser console and PHP error logs.
5. Test with multiple child sites to ensure compatibility.
6. Verify that data is correctly synced between MainWP and the third-party service.

## Step 11: Package Your Integration

When your integration is ready for distribution:

1. Remove any development or debugging code.
2. Ensure all text is properly internationalized.
3. Create a readme.txt file with installation and usage instructions.
4. Package your integration as a ZIP file for distribution.

## Example: A Simple "Third-Party Service" Integration

Here's a minimal example of a MainWP integration that connects with a third-party service:

```php
<?php
/**
 * Plugin Name: Third-Party Service Integration for MainWP
 * Plugin URI: https://example.com/third-party-integration
 * Description: Integrates MainWP with Third-Party Service.
 * Version: 1.0
 * Author: Your Name
 * Author URI: https://example.com
 * Text Domain: third-party-integration
 */

namespace MyCompany\ThirdPartyIntegration;

// Register the integration with MainWP
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'ThirdPartyIntegration',
        'mainwp' => true,
        'callback' => array('MyCompany\\ThirdPartyIntegration\\ThirdPartyIntegration', 'get_instance'),
        'name' => 'Third-Party Service Integration'
    );
    return $extensions;
});

class ThirdPartyIntegration {
    private static $instance = null;
    private $api_client = null;
    
    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    public function __construct() {
        // Initialize the integration
        add_action('admin_init', array($this, 'admin_init'));
        add_action('mainwp_admin_menu', array($this, 'init_menu'));
        
        // Initialize API client
        $this->init_api_client();
    }
    
    public function admin_init() {
        // Check for required dependencies
        $this->check_required_plugins();
    }
    
    public function init_menu() {
        // Add submenu page to MainWP menu
        add_submenu_page(
            'mainwp_tab',
            __('Third-Party Service', 'third-party-integration'),
            __('Third-Party Service', 'third-party-integration'),
            'read',
            'ThirdPartyIntegration',
            array($this, 'render_admin_page')
        );
        
        // Add settings page
        add_submenu_page(
            'mainwp_tab',
            __('Third-Party Settings', 'third-party-integration'),
            __('Third-Party Settings', 'third-party-integration'),
            'read',
            'ThirdPartyIntegrationSettings',
            array($this, 'render_settings_page')
        );
    }
    
    private function init_api_client() {
        $api_key = get_option('third_party_integration_api_key', '');
        if (!empty($api_key)) {
            $this->api_client = new ApiClient($api_key);
        }
    }
    
    private function check_required_plugins() {
        if (!function_exists('is_plugin_active')) {
            include_once(ABSPATH . 'wp-admin/includes/plugin.php');
        }
        
        if (!is_plugin_active('third-party-plugin/third-party-plugin.php')) {
            add_action('admin_notices', function() {
                ?>
                <div class="notice notice-error">
                    <p><?php echo sprintf(__('Third-Party Service Integration requires the %s plugin to be installed and activated.', 'third-party-integration'), '<a href="https://example.com/third-party-plugin" target="_blank">Third-Party Plugin</a>'); ?></p>
                </div>
                <?php
            });
        }
    }
    
    public function render_admin_page() {
        // Check if user has permissions
        if (!mainwp_current_user_can('read')) {
            mainwp_do_not_have_permissions(__('Third-Party Service', 'third-party-integration'));
            return;
        }
        
        // Check if API key is set
        if (empty($this->api_client)) {
            ?>
            <div class="ui segment">
                <div class="ui yellow message">
                    <?php echo sprintf(__('Please configure your API key in the %s settings page.', 'third-party-integration'), '<a href="admin.php?page=ThirdPartyIntegrationSettings">Third-Party Service</a>'); ?>
                </div>
            </div>
            <?php
            return;
        }
        
        // Render admin page
        ?>
        <div class="ui segment">
            <h2 class="ui header"><?php esc_html_e('Third-Party Service Integration', 'third-party-integration'); ?></h2>
            
            <!-- Your integration UI here -->
            
        </div>
        <?php
    }
    
    public function render_settings_page() {
        // Check if user has permissions
        if (!mainwp_current_user_can('read')) {
            mainwp_do_not_have_permissions(__('Third-Party Settings', 'third-party-integration'));
            return;
        }
        
        // Save settings if form is submitted
        if (isset($_POST['submit'])) {
            // Verify nonce
            check_admin_referer('third_party_settings_nonce', 'third_party_settings_nonce');
            
            // Save API key
            $api_key = sanitize_text_field($_POST['api_key'] ?? '');
            update_option('third_party_integration_api_key', $api_key);
            
            // Reinitialize API client
            $this->init_api_client();
            
            ?>
            <div class="ui green message"><?php esc_html_e('Settings saved successfully.', 'third-party-integration'); ?></div>
            <?php
        }
        
        // Get current settings
        $api_key = get_option('third_party_integration_api_key', '');
        
        // Render settings form
        ?>
        <div class="ui segment">
            <h2 class="ui header"><?php esc_html_e('Third-Party Service Settings', 'third-party-integration'); ?></h2>
            <form class="ui form" method="post" action="">
                <?php wp_nonce_field('third_party_settings_nonce', 'third_party_settings_nonce'); ?>
                
                <div class="field">
                    <label><?php esc_html_e('API Key', 'third-party-integration'); ?></label>
                    <input type="text" name="api_key" value="<?php echo esc_attr($api_key); ?>">
                    <p class="description"><?php esc_html_e('Enter your API key from your Third-Party Service account.', 'third-party-integration'); ?></p>
                </div>
                
                <button class="ui green button" type="submit" name="submit"><?php esc_html_e('Save Settings', 'third-party-integration'); ?></button>
            </form>
        </div>
        <?php
    }
}

class ApiClient {
    private $api_key;
    private $api_url = 'https://api.third-party-service.com/v1/';
    
    public function __construct($api_key) {
        $this->api_key = $api_key;
    }
    
    public function get_data($endpoint, $params = array()) {
        $url = $this->api_url . $endpoint;
        $args = array(
            'headers' => array(
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json'
            ),
            'timeout' => 30
        );
        
        if (!empty($params)) {
            $url = add_query_arg($params, $url);
        }
        
        $response = wp_remote_get($url, $args);
        
        if (is_wp_error($response)) {
            return array('error' => $response->get_error_message());
        }
        
        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }
    
    public function post_data($endpoint, $data) {
        $url = $this->api_url . $endpoint;
        $args = array(
            'headers' => array(
                'Authorization' => 'Bearer ' . $this->api_key,
                'Content-Type' => 'application/json'
            ),
            'body' => json_encode($data),
            'method' => 'POST',
            'timeout' => 30
        );
        
        $response = wp_remote_post($url, $args);
        
        if (is_wp_error($response)) {
            return array('error' => $response->get_error_message());
        }
        
        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }
}
```

## Next Steps

After creating your basic integration, you might want to explore:

- [Using MainWP Actions & Filters](actions-filters.md) for deeper integration
- [Building Admin Interfaces](admin-interfaces.md) for more advanced UI elements
- [Working with Third-Party APIs](third-party-apis.md) for more advanced API integration techniques
- [API Integration Best Practices](../best-practices/api-integration.md) for security and performance considerations

## Related Resources

- [MainWP Development Extension on GitHub](https://github.com/mainwp/mainwp-development-extension)
- [MainWP Dashboard API Documentation](../../source-code/dashboard/)
- [MainWP Dashboard Hooks](../../mainwp-hooks/dashboard/)
- [WordPress HTTP API Documentation](https://developer.wordpress.org/plugins/http-api/)

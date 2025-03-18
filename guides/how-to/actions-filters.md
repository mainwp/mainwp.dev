# Using MainWP Actions & Filters

This guide explains how to use MainWP's actions and filters (hooks) to integrate your extension with the MainWP Dashboard and Child plugins. Understanding these hooks is essential for creating powerful, well-integrated extensions.

## Quick Start for Experienced Developers

```php
// Hook into MainWP Dashboard actions
add_action('mainwp_pageheader_extensions', function() {
    // Add content to extension page header
});

// Filter MainWP Dashboard data
add_filter('mainwp_getextensions', function($extensions) {
    // Register your extension
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'MyExtension',
        'mainwp' => true,
        'callback' => array('MyCompany\\MyExtension\\MyExtension', 'get_instance'),
        'name' => 'My Extension'
    );
    return $extensions;
});

// Hook into child site actions
add_action('mainwp_child_call', function($action) {
    // Handle requests from the dashboard
    if ($action == 'my_custom_action') {
        // Process the request
    }
});
```

Key hook categories:
- Registration hooks (`mainwp_getextensions`)
- UI hooks (`mainwp_pageheader_extensions`, `mainwp_admin_menu`)
- Site management hooks (`mainwp_site_synced`, `mainwp_site_actions`)
- Data hooks (`mainwp_site_sync_data`, `mainwp_get_site_option`)
- Child communication hooks (`mainwp_child_call`, `mainwp_child_init`)

## Understanding WordPress Hooks

Before diving into MainWP-specific hooks, it's important to understand the WordPress hooks system:

- **Actions**: Allow you to add custom functionality at specific points in execution
- **Filters**: Allow you to modify data before it's used by WordPress

### Actions

Actions are triggered at specific points during execution and allow you to add custom functionality:

```php
add_action('hook_name', 'callback_function', 10, 2);

function callback_function($arg1, $arg2) {
    // Do something when the hook is triggered
}
```

### Filters

Filters allow you to modify data before it's used:

```php
add_filter('hook_name', 'filter_function', 10, 1);

function filter_function($value) {
    // Modify $value
    return $modified_value;
}
```

## MainWP Dashboard Hooks

MainWP Dashboard provides numerous hooks for extending its functionality. Here are the most important ones for extension developers:

### Extension Registration

The most important hook for any MainWP extension is `mainwp_getextensions`, which registers your extension with the MainWP Dashboard:

```php
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'MyExtension',
        'mainwp' => true,
        'callback' => array('MyCompany\\MyExtension\\MyExtension', 'get_instance'),
        'name' => 'My Extension'
    );
    return $extensions;
});
```

This tells MainWP:
- The location of your plugin file
- The API identifier for your extension
- That this is a MainWP extension (not a third-party integration)
- The callback function to initialize your extension
- The display name of your extension

### Admin Menu Integration

To add menu items to the MainWP Dashboard:

```php
add_action('mainwp_admin_menu', function() {
    add_submenu_page(
        'mainwp_tab',
        __('My Extension', 'my-extension'),
        __('My Extension', 'my-extension'),
        'read',
        'MyExtension',
        array($this, 'render_admin_page')
    );
});
```

### Page Header and Footer

To add content to the header or footer of your extension's pages:

```php
add_action('mainwp_pageheader_extensions', function() {
    // Add content to the page header
    ?>
    <div class="ui segment">
        <h2 class="ui header"><?php esc_html_e('My Extension Header', 'my-extension'); ?></h2>
    </div>
    <?php
});

add_action('mainwp_pagefooter_extensions', function() {
    // Add content to the page footer
    ?>
    <div class="ui segment">
        <p><?php esc_html_e('My Extension Footer', 'my-extension'); ?></p>
    </div>
    <?php
});
```

### Dashboard Widgets

To add widgets to the MainWP Dashboard:

```php
add_action('mainwp_dashboard_widgets', function() {
    add_meta_box(
        'my_extension_widget',
        __('My Extension Widget', 'my-extension'),
        array($this, 'render_dashboard_widget'),
        'mainwp_dashboard',
        'normal',
        'default'
    );
});

public function render_dashboard_widget() {
    // Widget content
    ?>
    <div class="ui segment">
        <p><?php esc_html_e('Widget content here', 'my-extension'); ?></p>
    </div>
    <?php
}
```

### Site Actions

To add actions to the site actions dropdown menu:

```php
add_filter('mainwp_site_actions', function($actions, $website) {
    $actions['my_action'] = array(
        'label' => __('My Custom Action', 'my-extension'),
        'url' => admin_url('admin.php?page=MyExtension&site_id=' . $website->id),
        'icon' => 'cog',
    );
    return $actions;
}, 10, 2);
```

### Site Sync Data

To add custom data to the site sync process:

```php
add_filter('mainwp_site_sync_data', function($data, $website) {
    // Add custom data to the sync process
    $data['my_extension'] = array(
        'custom_field' => 'custom_value',
    );
    return $data;
}, 10, 2);
```

### After Site Sync

To perform actions after a site is synced:

```php
add_action('mainwp_site_synced', function($website, $data) {
    // Process data after site sync
    if (isset($data['my_extension'])) {
        // Process my_extension data
    }
}, 10, 2);
```

## MainWP Child Hooks

If your extension needs to interact with child sites, you'll need to use MainWP Child hooks:

### Handling Dashboard Requests

To handle requests from the MainWP Dashboard:

```php
add_action('mainwp_child_call', function($action) {
    // Check if this is a request for your extension
    if ($action == 'my_extension') {
        // Get the specific action
        $specific_action = $_POST['specific_action'] ?? '';
        
        // Handle the specific action
        switch ($specific_action) {
            case 'get_data':
                // Get and return data
                $data = array('result' => 'success', 'data' => 'your_data');
                wp_send_json($data);
                break;
            case 'update_data':
                // Update data
                $data = array('result' => 'success', 'message' => 'Data updated');
                wp_send_json($data);
                break;
            default:
                // Handle unknown action
                $data = array('result' => 'error', 'message' => 'Unknown action');
                wp_send_json($data);
                break;
        }
    }
});
```

### Child Plugin Initialization

To initialize your child plugin:

```php
add_action('mainwp_child_init', function() {
    // Initialize your child plugin
});
```

## Communication Between Dashboard and Child Sites

One of the most powerful features of MainWP is the ability to communicate between the dashboard and child sites. Here's how to implement this in your extension:

### Sending Requests from Dashboard to Child

```php
// In your dashboard extension
public function send_request_to_child($website_id, $action, $data = array()) {
    // Get the website
    $website = MainWP\Dashboard\MainWP_DB::instance()->get_website_by_id($website_id);
    if (!$website) {
        return array('error' => 'Website not found');
    }
    
    // Prepare the data
    $data['action'] = $action;
    
    // Send the request
    try {
        $information = MainWP\Dashboard\MainWP_Connect::fetch_url_authed(
            $website,
            'my_extension',
            $data
        );
        
        // Process the response
        if (is_array($information) && isset($information['result'])) {
            return $information;
        } else {
            return array('error' => 'Invalid response from child site');
        }
    } catch (Exception $e) {
        return array('error' => $e->getMessage());
    }
}
```

### Handling Requests on the Child Site

```php
// In your child plugin
add_action('mainwp_child_call', function($action) {
    if ($action == 'my_extension') {
        // Get the specific action
        $specific_action = $_POST['action'] ?? '';
        
        // Handle the specific action
        switch ($specific_action) {
            case 'get_plugin_data':
                // Get plugin data
                $plugin_data = get_plugin_data(WP_PLUGIN_DIR . '/my-plugin/my-plugin.php');
                wp_send_json(array(
                    'result' => 'success',
                    'data' => $plugin_data
                ));
                break;
            // Handle other actions
            default:
                wp_send_json(array(
                    'result' => 'error',
                    'message' => 'Unknown action'
                ));
                break;
        }
    }
});
```

## Common Hook Use Cases

### Adding a Settings Page

```php
// Add a settings page to the MainWP Dashboard
add_action('mainwp_admin_menu', function() {
    add_submenu_page(
        'mainwp_tab',
        __('My Extension Settings', 'my-extension'),
        __('My Extension Settings', 'my-extension'),
        'read',
        'MyExtensionSettings',
        array($this, 'render_settings_page')
    );
});

// Render the settings page
public function render_settings_page() {
    // Check if user has permissions
    if (!mainwp_current_user_can('read')) {
        mainwp_do_not_have_permissions(__('My Extension Settings', 'my-extension'));
        return;
    }
    
    // Save settings if form is submitted
    if (isset($_POST['submit'])) {
        // Verify nonce
        check_admin_referer('my_extension_settings_nonce', 'my_extension_settings_nonce');
        
        // Save settings
        $settings = array(
            'setting1' => sanitize_text_field($_POST['setting1'] ?? ''),
            'setting2' => sanitize_text_field($_POST['setting2'] ?? ''),
        );
        update_option('my_extension_settings', $settings);
        
        // Show success message
        ?>
        <div class="ui green message"><?php esc_html_e('Settings saved successfully.', 'my-extension'); ?></div>
        <?php
    }
    
    // Get current settings
    $settings = get_option('my_extension_settings', array(
        'setting1' => '',
        'setting2' => '',
    ));
    
    // Render settings form
    ?>
    <div class="ui segment">
        <h2 class="ui header"><?php esc_html_e('My Extension Settings', 'my-extension'); ?></h2>
        <form class="ui form" method="post" action="">
            <?php wp_nonce_field('my_extension_settings_nonce', 'my_extension_settings_nonce'); ?>
            
            <div class="field">
                <label><?php esc_html_e('Setting 1', 'my-extension'); ?></label>
                <input type="text" name="setting1" value="<?php echo esc_attr($settings['setting1']); ?>">
            </div>
            
            <div class="field">
                <label><?php esc_html_e('Setting 2', 'my-extension'); ?></label>
                <input type="text" name="setting2" value="<?php echo esc_attr($settings['setting2']); ?>">
            </div>
            
            <button class="ui green button" type="submit" name="submit"><?php esc_html_e('Save Settings', 'my-extension'); ?></button>
        </form>
    </div>
    <?php
}
```

### Adding a Custom Tab to Individual Sites

```php
// Add a custom tab to individual site pages
add_filter('mainwp_getsubpages_sites', function($subpages, $website) {
    $subpages[] = array(
        'title' => __('My Extension', 'my-extension'),
        'slug' => 'MyExtension',
        'callback' => array($this, 'render_site_tab'),
    );
    return $subpages;
}, 10, 2);

// Render the custom tab
public function render_site_tab($website) {
    // Render tab content
    ?>
    <div class="ui segment">
        <h2 class="ui header"><?php esc_html_e('My Extension', 'my-extension'); ?></h2>
        <p><?php esc_html_e('Site ID:', 'my-extension'); ?> <?php echo esc_html($website->id); ?></p>
        <!-- Tab content here -->
    </div>
    <?php
}
```

### Adding a Bulk Action

```php
// Add a bulk action to the sites page
add_filter('mainwp_managesites_bulk_actions', function($actions) {
    $actions['my_bulk_action'] = __('My Bulk Action', 'my-extension');
    return $actions;
});

// Handle the bulk action
add_action('mainwp_managesites_bulk_action', function($action, $sites) {
    if ($action == 'my_bulk_action') {
        // Process the bulk action for each site
        foreach ($sites as $site_id) {
            // Process the site
        }
        
        // Redirect back to the sites page
        wp_redirect(admin_url('admin.php?page=managesites&bulk_my_bulk_action=success'));
        exit;
    }
}, 10, 2);
```

## Best Practices for Using Hooks

### Use Unique Hook Names

If you need to create your own hooks for your extension, use a unique prefix to avoid conflicts:

```php
do_action('my_extension_custom_hook', $data);
apply_filters('my_extension_custom_filter', $value);
```

### Check Hook Availability

Some hooks may not be available in all versions of MainWP. Always check if a hook exists before using it:

```php
if (has_action('mainwp_hook_name')) {
    // Hook exists, safe to use
}
```

### Use Proper Priority

The priority parameter in `add_action()` and `add_filter()` determines the order in which callbacks are executed. Lower numbers run earlier:

```php
// Run early (priority 5)
add_action('mainwp_hook_name', 'early_function', 5);

// Run at default priority (10)
add_action('mainwp_hook_name', 'default_function');

// Run late (priority 20)
add_action('mainwp_hook_name', 'late_function', 20);
```

### Remove Hooks When Necessary

If you need to temporarily disable a hook, you can remove it:

```php
// Remove a hook
remove_action('mainwp_hook_name', 'callback_function');

// Do something without the hook

// Add the hook back
add_action('mainwp_hook_name', 'callback_function');
```

### Use Proper Error Handling

Always include error handling in your hook callbacks:

```php
add_action('mainwp_hook_name', function() {
    try {
        // Do something that might fail
    } catch (Exception $e) {
        // Handle the error
        error_log('My Extension Error: ' . $e->getMessage());
    }
});
```

## Debugging Hooks

### Check if a Hook is Firing

To check if a hook is firing, you can add a temporary debug callback:

```php
add_action('mainwp_hook_name', function() {
    error_log('mainwp_hook_name fired at ' . current_time('mysql'));
});
```

### List All Hooks

To see all hooks that are registered, you can use a plugin like [Query Monitor](https://wordpress.org/plugins/query-monitor/) or add this code:

```php
add_action('admin_footer', function() {
    global $wp_filter;
    echo '<pre>';
    print_r($wp_filter);
    echo '</pre>';
});
```

### Check Hook Parameters

To see what parameters a hook passes, you can use this debug callback:

```php
add_action('mainwp_hook_name', function() {
    $args = func_get_args();
    error_log('mainwp_hook_name parameters: ' . print_r($args, true));
}, 10, 99); // Accept up to 99 parameters
```

## Finding Available Hooks

MainWP provides many hooks for extension developers. Here are some ways to find them:

### MainWP Hooks Documentation

The [MainWP Hooks Documentation](../../mainwp-hooks/) provides a comprehensive list of available hooks, organized by category.

### Source Code

You can search the MainWP source code for hooks:

1. Look for `do_action()` and `apply_filters()` calls in the MainWP Dashboard and Child plugins
2. Check the [MainWP GitHub repositories](https://github.com/mainwp)

### Hook Categories

MainWP hooks are generally organized into these categories:

1. **Dashboard UI Hooks**: For modifying the MainWP Dashboard interface
2. **Site Management Hooks**: For interacting with managed sites
3. **Data Hooks**: For modifying data before it's used or displayed
4. **Communication Hooks**: For handling communication between Dashboard and Child sites
5. **Extension Hooks**: For registering and managing extensions

## Complete Hook Reference

For a complete reference of all available hooks, see the [MainWP Hooks Documentation](../../mainwp-hooks/):

- [MainWP Dashboard Actions](../../mainwp-hooks/dashboard/actions/)
- [MainWP Dashboard Filters](../../mainwp-hooks/dashboard/filters/)
- [MainWP Child Actions](../../mainwp-hooks/child/actions/)
- [MainWP Child Filters](../../mainwp-hooks/child/filters/)

## Next Steps

Now that you understand how to use MainWP actions and filters, you can:

- [Create a Basic MainWP Extension](create-basic-extension.md) that integrates with MainWP
- Learn about [Building Admin Interfaces](admin-interfaces.md) for your extension
- Explore [Data Storage and Retrieval](data-storage.md) for managing extension data

## Related Resources

- [WordPress Plugin API Documentation](https://developer.wordpress.org/plugins/hooks/)
- [MainWP Dashboard API Documentation](../../source-code/dashboard/)
- [MainWP Child API Documentation](../../source-code/child/)

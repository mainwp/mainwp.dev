# Understanding the MainWP Development Extension

The MainWP Development Extension is a template provided by MainWP to help developers create new extensions quickly and efficiently. This guide explains the structure and components of the development extension, helping you understand how to use it effectively in your own projects.

## Quick Start for Experienced Developers

The MainWP Development Extension follows a standard object-oriented structure:

- **Main Class** (`MainWP_Development_Extension`): Initializes the extension and hooks into MainWP
- **Admin Class**: Handles admin pages, settings, and UI elements
- **Database Class**: Manages database operations
- **Utility Class**: Contains helper functions
- **AJAX Class**: Handles AJAX requests
- **Overview/Individual Classes**: Manage site overview and individual site pages

Key files to modify:
1. `mainwp-development-extension.php`: Main plugin file with registration
2. `class/class-mainwp-development-extension.php`: Core functionality
3. `class/class-mainwp-development-extension-admin.php`: Admin interface

## Repository Overview

The [MainWP Development Extension](https://github.com/mainwp/mainwp-development-extension) is available on GitHub and serves as a starting point for creating new extensions. It includes:

- A complete extension structure
- Example code for common MainWP integration points
- Properly formatted code following WordPress coding standards
- Comments explaining key functionality

## Directory Structure

```
mainwp-development-extension/
├── assets/
│   ├── css/
│   │   └── mainwp-development-extension.css
│   ├── images/
│   └── js/
│       └── mainwp-development-extension.js
├── class/
│   ├── class-mainwp-development-extension.php
│   ├── class-mainwp-development-extension-admin.php
│   ├── class-mainwp-development-extension-ajax.php
│   ├── class-mainwp-development-extension-db.php
│   ├── class-mainwp-development-extension-individual.php
│   ├── class-mainwp-development-extension-overview.php
│   └── class-mainwp-development-extension-utility.php
├── includes/
│   └── functions.php
├── languages/
│   └── mainwp-development-extension.pot
├── readme.txt
└── mainwp-development-extension.php
```

## Key Components

### Main Plugin File

The `mainwp-development-extension.php` file is the entry point for your extension. It includes:

- Plugin header information
- Extension registration with MainWP
- Basic setup and initialization

```php
/**
 * Plugin Name: MainWP Development Extension
 * Plugin URI: https://mainwp.com
 * Description: MainWP Development Extension example.
 * Version: 4.0
 * Author: MainWP
 * Author URI: https://mainwp.com
 * Documentation URI: https://mainwp.com/help/
 */

// Registration with MainWP
add_filter('mainwp_getextensions', function($extensions) {
    $extensions[] = array(
        'plugin' => __FILE__,
        'api' => 'MainWP_Development_Extension',
        'mainwp' => true,
        'callback' => array('MainWP_Development_Extension', 'get_instance'),
        'name' => 'Development Extension'
    );
    return $extensions;
});
```

### Main Class

The `class-mainwp-development-extension.php` file contains the main class that initializes your extension and hooks into MainWP. Key features include:

- Singleton pattern implementation
- Hooks and filters registration
- Class loading and initialization

```php
class MainWP_Development_Extension {
    // Singleton instance
    private static $instance = null;
    
    // Get singleton instance
    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    // Constructor
    public function __construct() {
        // Load classes
        $this->includes();
        
        // Register hooks
        $this->setup_hooks();
    }
    
    // Load required files
    private function includes() {
        // Load classes and dependencies
    }
    
    // Set up hooks and filters
    private function setup_hooks() {
        // Register actions and filters
    }
}
```

### Admin Class

The `class-mainwp-development-extension-admin.php` file handles the admin interface for your extension, including:

- Admin menu registration
- Settings pages
- Admin UI elements

```php
class MainWP_Development_Extension_Admin {
    // Initialize admin functionality
    public function init() {
        // Add admin menu items
        add_action('mainwp_admin_menu', array($this, 'init_menu'));
    }
    
    // Register admin menu items
    public function init_menu() {
        // Add submenu pages
        add_submenu_page(
            'mainwp_tab',
            __('Development Extension', 'mainwp-development-extension'),
            __('Development Extension', 'mainwp-development-extension'),
            'read',
            'DevelopmentExtension',
            array($this, 'render_admin_page')
        );
    }
    
    // Render admin page
    public function render_admin_page() {
        // Display admin interface
    }
}
```

### Database Class

The `class-mainwp-development-extension-db.php` file manages database operations for your extension, including:

- Table creation and management
- Data storage and retrieval
- Database optimization

```php
class MainWP_Development_Extension_DB {
    // Database table name
    private $table_name;
    
    // Constructor
    public function __construct() {
        global $wpdb;
        $this->table_name = $wpdb->prefix . 'mainwp_development_extension';
    }
    
    // Create database tables
    public function create_table() {
        global $wpdb;
        
        // SQL for table creation
        $sql = "CREATE TABLE IF NOT EXISTS $this->table_name (
            id int(11) NOT NULL AUTO_INCREMENT,
            site_id int(11) NOT NULL,
            data text NOT NULL,
            created_at datetime NOT NULL,
            PRIMARY KEY (id)
        ) $wpdb->get_charset_collate();";
        
        // Create table
        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);
    }
    
    // Add data
    public function add_data($site_id, $data) {
        global $wpdb;
        
        // Insert data
        $wpdb->insert(
            $this->table_name,
            array(
                'site_id' => $site_id,
                'data' => $data,
                'created_at' => current_time('mysql')
            ),
            array('%d', '%s', '%s')
        );
        
        return $wpdb->insert_id;
    }
    
    // Get data
    public function get_data($site_id) {
        global $wpdb;
        
        // Retrieve data
        return $wpdb->get_results(
            $wpdb->prepare(
                "SELECT * FROM $this->table_name WHERE site_id = %d",
                $site_id
            )
        );
    }
}
```

### Utility Class

The `class-mainwp-development-extension-utility.php` file contains helper functions and utilities for your extension:

```php
class MainWP_Development_Extension_Utility {
    // Format data for display
    public static function format_data($data) {
        // Format and return data
    }
    
    // Validate input
    public static function validate_input($input) {
        // Validate and sanitize input
    }
    
    // Generate unique ID
    public static function generate_id() {
        // Generate and return unique ID
    }
}
```

### AJAX Class

The `class-mainwp-development-extension-ajax.php` file handles AJAX requests for your extension:

```php
class MainWP_Development_Extension_Ajax {
    // Constructor
    public function __construct() {
        // Register AJAX handlers
        add_action('wp_ajax_mainwp_development_extension_action', array($this, 'ajax_action'));
    }
    
    // Handle AJAX request
    public function ajax_action() {
        // Verify nonce
        check_ajax_referer('mainwp_development_extension_nonce', 'security');
        
        // Process request
        $action = isset($_POST['action_type']) ? sanitize_text_field($_POST['action_type']) : '';
        
        switch ($action) {
            case 'get_data':
                // Handle get_data action
                break;
            case 'save_data':
                // Handle save_data action
                break;
            default:
                // Handle unknown action
                break;
        }
        
        // Return response
        wp_send_json_success(array('message' => 'Action completed'));
    }
}
```

### Overview and Individual Classes

The development extension includes classes for managing site overview and individual site pages:

- `class-mainwp-development-extension-overview.php`: Handles the extension's functionality on the MainWP Overview page
- `class-mainwp-development-extension-individual.php`: Handles the extension's functionality on individual site pages

These classes allow your extension to integrate with MainWP's site management interface.

## Common Integration Points

The development extension demonstrates several common integration points with MainWP:

### Dashboard Menu Integration

```php
add_action('mainwp_admin_menu', array($this, 'init_menu'));
```

### Site Actions

```php
add_filter('mainwp_site_actions', array($this, 'site_actions'), 10, 2);
```

### AJAX Handlers

```php
add_action('wp_ajax_mainwp_development_extension_action', array($this, 'ajax_action'));
```

### Dashboard Widgets

```php
add_action('mainwp_dashboard_widgets', array($this, 'dashboard_widgets'));
```

### Site Sync Data

```php
add_filter('mainwp_site_sync_data', array($this, 'sync_data'), 10, 2);
```

## Customizing the Development Extension

When using the development extension as a template for your own extension, follow these steps:

1. **Rename Files and Classes**: Change all file names and class names to match your extension name
2. **Update Namespaces**: Change the namespace from `MainWP\Dev` to your own namespace
3. **Modify Plugin Information**: Update the plugin header with your extension's details
4. **Customize Functionality**: Modify the classes to implement your extension's specific functionality
5. **Update Text Domain**: Change the text domain for internationalization
6. **Customize UI**: Modify the admin interface to match your extension's needs

## Best Practices

When working with the MainWP Development Extension, follow these best practices:

### Maintain the Structure

The development extension follows a well-organized structure that separates concerns and makes the code maintainable. Try to maintain this structure in your own extension.

### Use Proper Namespacing

Use proper PHP namespaces to avoid conflicts with other plugins and extensions:

```php
namespace MyCompany\MyExtension;
```

### Follow WordPress Coding Standards

Adhere to [WordPress Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/) for consistent, readable code.

### Implement Proper Error Handling

Include robust error handling to ensure your extension gracefully handles unexpected situations:

```php
try {
    // Attempt an operation
} catch (Exception $e) {
    // Handle the error
    error_log('MyExtension Error: ' . $e->getMessage());
    // Display user-friendly message
}
```

### Use Prepared SQL Statements

Always use prepared statements for database queries to prevent SQL injection:

```php
$wpdb->get_results(
    $wpdb->prepare(
        "SELECT * FROM $table_name WHERE site_id = %d",
        $site_id
    )
);
```

### Internationalize Your Extension

Make your extension translatable by using proper internationalization functions:

```php
__('Text to translate', 'your-text-domain');
esc_html__('Text to translate and escape', 'your-text-domain');
```

## Advanced Customization

### Adding Custom Database Tables

If your extension requires custom database tables, modify the Database class:

1. Define your table structure in the `create_table()` method
2. Add methods for CRUD operations on your tables
3. Call `create_table()` during plugin activation

### Creating Custom Admin Pages

To add custom admin pages:

1. Register your pages in the `init_menu()` method of the Admin class
2. Create rendering methods for each page
3. Implement the necessary functionality for each page

### Extending MainWP Dashboard Widgets

To add widgets to the MainWP Dashboard:

1. Hook into the `mainwp_dashboard_widgets` action
2. Register your widget with a unique ID
3. Create a callback function to render the widget content

```php
public function dashboard_widgets() {
    add_meta_box(
        'my_extension_widget',
        __('My Extension Widget', 'my-extension'),
        array($this, 'render_dashboard_widget'),
        'mainwp_dashboard',
        'normal',
        'default'
    );
}

public function render_dashboard_widget() {
    // Widget content
}
```

## Troubleshooting Common Issues

### Class Not Found Errors

If you encounter "Class not found" errors:

1. Check that all file paths in the `includes()` method are correct
2. Ensure you've updated all class references when renaming
3. Verify that your autoloader (if used) is properly configured

### Database Errors

For database-related issues:

1. Check that your table creation SQL is valid
2. Ensure you're using proper data types and prepared statements
3. Verify that your database prefix is correct

### Integration Issues

If your extension doesn't integrate properly with MainWP:

1. Verify that you've registered your extension correctly with the `mainwp_getextensions` filter
2. Check that your callback function returns a valid instance
3. Ensure you're hooking into the correct MainWP actions and filters

## Next Steps

Now that you understand the MainWP Development Extension, you can:

- [Create a Basic MainWP Extension](create-basic-extension.md) using this template
- Learn about [Using MainWP Actions & Filters](actions-filters.md) for deeper integration
- Explore [Building Admin Interfaces](admin-interfaces.md) for your extension

## Related Resources

- [MainWP Development Extension on GitHub](https://github.com/mainwp/mainwp-development-extension)
- [MainWP Dashboard API Documentation](../../source-code/dashboard/)
- [MainWP Dashboard Hooks](../../mainwp-hooks/dashboard/)

# MainWP Dashboard Hooks

This section provides documentation for all hooks (actions and filters) available in the MainWP Dashboard plugin.

## Actions

[Dashboard Actions](actions.md) allow you to add custom functionality at specific points in the MainWP Dashboard execution. Actions are triggered at specific points during the execution of MainWP Dashboard, and you can use them to add your own functionality.

Common use cases for Dashboard actions include:
- Adding custom UI elements to the Dashboard
- Performing additional tasks when sites are added, updated, or removed
- Extending the Dashboard with custom features
- Integrating with other plugins or services

## Filters

[Dashboard Filters](filters.md) allow you to modify data or output at specific points in the MainWP Dashboard execution. Filters are used to modify data before it is used or displayed by MainWP Dashboard.

Common use cases for Dashboard filters include:
- Modifying the output of Dashboard components
- Changing how data is processed or displayed
- Adding or removing items from lists or menus
- Customizing the behavior of Dashboard features

## Examples

### Using Dashboard Actions

```php
// Add a custom section to the Dashboard
add_action('mainwp_after_header', 'my_custom_dashboard_section');

function my_custom_dashboard_section() {
    ?>
    <div class="ui segment">
        <h2 class="ui header">Custom Dashboard Section</h2>
        <p>This is a custom section added to the MainWP Dashboard.</p>
    </div>
    <?php
}
```

### Using Dashboard Filters

```php
// Modify the sites table columns
add_filter('mainwp_sitestable_getcolumns', 'my_custom_sites_table_columns');

function my_custom_sites_table_columns($columns) {
    // Add a custom column
    $columns['custom_column'] = 'Custom Column';
    
    return $columns;
}
```

## Related Resources

- [MainWP Developer Documentation](https://mainwp.dev/)
- [MainWP Dashboard GitHub Repository](https://github.com/mainwp/mainwp)
- [WordPress Plugin Developer Handbook](https://developer.wordpress.org/plugins/)

# MainWP Child Hooks

This section provides documentation for all hooks (actions and filters) available in the MainWP Child plugin.

## Actions

[Child Actions](actions.md) allow you to add custom functionality at specific points in the MainWP Child execution. Actions are triggered at specific points during the execution of MainWP Child, and you can use them to add your own functionality.

Common use cases for Child actions include:
- Adding custom functionality to the Child site
- Performing additional tasks when the Child site is connected to a Dashboard
- Extending the Child plugin with custom features
- Integrating with other plugins or services on the Child site

## Filters

[Child Filters](filters.md) allow you to modify data or output at specific points in the MainWP Child execution. Filters are used to modify data before it is used or sent back to the Dashboard.

Common use cases for Child filters include:
- Modifying the data sent to the Dashboard
- Changing how requests from the Dashboard are processed
- Customizing the behavior of Child features
- Adding or removing functionality from the Child plugin

## Examples

### Using Child Actions

```php
// Add custom functionality after the Child plugin is loaded
add_action('mainwp_child_loaded', 'my_custom_child_functionality');

function my_custom_child_functionality() {
    // Your custom code here
    // This will run after the MainWP Child plugin is fully loaded
}
```

### Using Child Filters

```php
// Modify the site info sent to the Dashboard
add_filter('mainwp_child_site_info', 'my_custom_site_info');

function my_custom_site_info($site_info) {
    // Add custom information to the site info
    $site_info['custom_data'] = 'Custom value';
    
    return $site_info;
}
```

## Security Considerations

When working with MainWP Child hooks, it's important to consider security implications:

1. **Authentication**: Always ensure that requests are properly authenticated before performing sensitive operations.
2. **Data Validation**: Validate and sanitize all data, especially data received from external sources.
3. **Capability Checks**: Use WordPress capability checks to ensure users have appropriate permissions.
4. **Nonce Verification**: Use nonces to protect against CSRF attacks.

## Related Resources

- [MainWP Developer Documentation](https://mainwp.dev/)
- [MainWP Child GitHub Repository](https://github.com/mainwp/mainwp-child)
- [WordPress Plugin Developer Handbook](https://developer.wordpress.org/plugins/)

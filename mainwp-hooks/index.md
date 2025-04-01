---
layout: documentation-single
title: MainWP Hooks Documentation
description: Comprehensive documentation for all hooks available in the MainWP ecosystem.
navigation:
  - title: Hook Types
    items:
      - id: dashboard-hooks
        title: Dashboard Hooks
      - id: child-hooks
        title: Child Hooks
  - title: Usage Guide
    items:
      - id: using-hooks
        title: Using Hooks
      - id: actions
        title: Actions
      - id: filters
        title: Filters
      - id: contributing
        title: Contributing
---

# MainWP Hooks Documentation

This section provides comprehensive documentation for all hooks (actions and filters) available in the MainWP ecosystem.

## Dashboard Hooks

The [MainWP Dashboard](dashboard/index.md) plugin provides hooks that allow you to extend and customize the MainWP Dashboard functionality.

- [Actions](dashboard/actions/index.md) - Dashboard actions allow you to add custom functionality at specific points in the MainWP Dashboard execution.
- [Filters](dashboard/filters/index.md) - Dashboard filters allow you to modify data or output at specific points in the MainWP Dashboard execution.

## Child Hooks

The [MainWP Child](child/index.md) plugin provides hooks that allow you to extend and customize the MainWP Child functionality.

- [Actions](child/actions/index.md) - Child actions allow you to add custom functionality at specific points in the MainWP Child execution.
- [Filters](child/filters/index.md) - Child filters allow you to modify data or output at specific points in the MainWP Child execution.

## Using Hooks

Hooks are the foundation of extending and customizing MainWP. They allow you to add your own functionality or modify existing functionality without modifying the core code.

### Actions

Actions allow you to add custom functionality at specific points in the MainWP execution. To use an action, you use the `add_action()` function:

```php
add_action('action_name', 'your_function_name', 10, 2);

function your_function_name(\$arg1, \$arg2) {
    // Your custom code here
}
```

### Filters

Filters allow you to modify data or output at specific points in the MainWP execution. To use a filter, you use the `add_filter()` function:

```php
add_filter('filter_name', 'your_function_name', 10, 2);

function your_function_name(\$value, \$arg2) {
    // Modify \$value here
    return \$value;
}
```

## Contributing

If you find any issues with the hooks documentation or would like to suggest improvements, please [open an issue](https://github.com/mainwp/mainwp/issues) on the MainWP GitHub repository.

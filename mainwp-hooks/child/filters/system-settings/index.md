# System & Settings Filters

Hooks related to general settings and system configuration.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`deprecated_hook_run`](#deprecated_hook_run) - Support old WP version 4.0.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Add support for the reporting system.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Method do_site_stats()
- [`save_settings_revision_limit_wptc`](#save_settings_revision_limit_wptc) - Save the WP Time Capsule settings - backups section.
- [`mainwp_child_branding_init_options`](#mainwp_child_branding_init_options) - Filter 'mainwp_child_branding_init_options'

## Hook Details

### `deprecated_hook_run`

*Support old WP version 4.0.*

Fires functions attached to a deprecated filter hook.

When a filter hook is deprecated, the apply_filters() call is replaced with
apply_filters_deprecated(), which triggers a deprecation notice and then fires
the original filter hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$hook_name` | `string` | The name of the filter hook.
`$replacement` | `string` | Optional. The hook that should have been used. Default empty.
`$version` | `string` | The version of WordPress that deprecated the hook.
`$message` | `string` | Optional. A message regarding the change. Default empty.

Source: [../sources/mainwp-child/includes/functions.php](includes/functions.php), [line 169](includes/functions.php#L169-L188)



### `mainwp_child_reports_log`

*Add support for the reporting system.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wptimecapsule'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 998](class/class-mainwp-child-timecapsule.php#L998-L1008)



### `mainwp_child_reports_log`

*Method do_site_stats()*

Add support for the reporting system.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wordfence'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-wordfence.php](class/class-mainwp-child-wordfence.php), [line 300](class/class-mainwp-child-wordfence.php#L300-L306)



### `save_settings_revision_limit_wptc`

*Save the WP Time Capsule settings - backups section.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data['revision_limit']` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1674](class/class-mainwp-child-timecapsule.php#L1674-L1702)



### `mainwp_child_branding_init_options`

*Filter 'mainwp_child_branding_init_options'*

Set custom branding setting through the filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$opts` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-branding.php](class/class-mainwp-child-branding.php), [line 106](class/class-mainwp-child-branding.php#L106-L113)




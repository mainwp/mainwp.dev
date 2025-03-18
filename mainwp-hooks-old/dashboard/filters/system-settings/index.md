# System & Settings Filters

Hooks related to general settings and system configuration.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_system_init`](#mainwp_system_init) - MainWP_System constructor.
- [`mainwp_log_system_query`](#mainwp_log_system_query) - Method log_system_query
- [`mainwp_before_save_email_settings`](#mainwp_before_save_email_settings) - Action: mainwp_before_save_email_settings
- [`mainwp_after_save_email_settings`](#mainwp_after_save_email_settings) - Action: mainwp_after_save_email_settings
- [`mainwp_settings_email_settings`](#mainwp_settings_email_settings) - Action: mainwp_settings_email_settings
- [`mainwp_module_cost_tracker_settings_bottom`](#mainwp_module_cost_tracker_settings_bottom) - Render settings content.
- [`mainwp_before_save_general_settings`](#mainwp_before_save_general_settings) - Action: mainwp_before_save_general_settings
- [`mainwp_after_save_general_settings`](#mainwp_after_save_general_settings) - Action: mainwp_after_save_general_settings
- [`mainwp_settings_form_top`](#mainwp_settings_form_top) - Action: mainwp_settings_form_top
- [`mainwp_settings_form_bottom`](#mainwp_settings_form_bottom) - Action: mainwp_settings_form_bottom
- [`mainwp_before_save_advanced_settings`](#mainwp_before_save_advanced_settings) - Action: mainwp_before_save_advanced_settings
- [`mainwp_after_save_advanced_settings`](#mainwp_after_save_advanced_settings) - Action: mainwp_after_save_advanced_settings
- [`mainwp_advanced_settings_form_top`](#mainwp_advanced_settings_form_top) - Action: mainwp_advanced_settings_form_top
- [`mainwp_advanced_settings_form_bottom`](#mainwp_advanced_settings_form_bottom) - Action: mainwp_advanced_settings_form_bottom
- [`mainwp_settings_help_item`](#mainwp_settings_help_item) - Action: mainwp_settings_help_item
- [`mainwp_before_save_email_settings`](#mainwp_before_save_email_settings) - Action: mainwp_before_save_email_settings
- [`mainwp_after_save_email_settings`](#mainwp_after_save_email_settings) - Action: mainwp_after_save_email_settings
- [`mainwp_before_wp_config_section`](#mainwp_before_wp_config_section) - Action: mainwp_before_wp_config_section
- [`mainwp_after_wp_config_section`](#mainwp_after_wp_config_section) - Action: mainwp_after_wp_config_section
- [`mainwp_init_load_all_options`](#mainwp_init_load_all_options) - Method load_all_options()
- [`mainwp_module_cost_tracker_before_save_settings`](#mainwp_module_cost_tracker_before_save_settings) - Settigns Post
- [`mainwp_default_settings_indicator`](#mainwp_default_settings_indicator) - Method render_not_default_indicator().
- [`mainwp_default_settings_indicator`](#mainwp_default_settings_indicator) - Method render_not_default_email_settings_indicator().
- [`mainwp_clear_and_lock_options`](#mainwp_clear_and_lock_options) - Clean and Lock extension options

## Hook Details

### `mainwp_system_init`

*MainWP_System constructor.*

Runs any time class is called.


Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 82](class/class-mainwp-system.php#L82-L135)



### `mainwp_log_system_query`

*Method log_system_query*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | params.
`$sql` | `string` | query.

Source: [../sources/mainwp-dashboard/class/class-mainwp-db.php](class/class-mainwp-db.php), [line 3242](class/class-mainwp-db.php#L3242-L3252)



### `mainwp_before_save_email_settings`

*Action: mainwp_before_save_email_settings*

Fires before save email settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`$update_settings` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 76](class/class-mainwp-notification-settings.php#L76-L83)



### `mainwp_after_save_email_settings`

*Action: mainwp_after_save_email_settings*

Fires after save email settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$emails_settings` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 87](class/class-mainwp-notification-settings.php#L87-L94)



### `mainwp_settings_email_settings`

*Action: mainwp_settings_email_settings*

Fires after the default email settings.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 175](class/class-mainwp-notification-settings.php#L175-L182)



### `mainwp_module_cost_tracker_settings_bottom`

*Render settings content.*

Renders the extension settings page.


Source: [../sources/mainwp-dashboard/modules/cost-tracker/pages/page-cost-tracker-settings.php](modules/cost-tracker/pages/page-cost-tracker-settings.php), [line 88](modules/cost-tracker/pages/page-cost-tracker-settings.php#L88-L343)



### `mainwp_before_save_general_settings`

*Action: mainwp_before_save_general_settings*

Fires before general settings save.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 454](pages/page-mainwp-settings.php#L454-L461)



### `mainwp_after_save_general_settings`

*Action: mainwp_after_save_general_settings*

Fires after save general settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 585](pages/page-mainwp-settings.php#L585-L592)



### `mainwp_settings_form_top`

*Action: mainwp_settings_form_top*

Fires at the top of settings form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 631](pages/page-mainwp-settings.php#L631-L638)



### `mainwp_settings_form_bottom`

*Action: mainwp_settings_form_bottom*

Fires at the bottom of settings form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 906](pages/page-mainwp-settings.php#L906-L913)



### `mainwp_before_save_advanced_settings`

*Action: mainwp_before_save_advanced_settings*

Fires before save advanced settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1319](pages/page-mainwp-settings.php#L1319-L1326)



### `mainwp_after_save_advanced_settings`

*Action: mainwp_after_save_advanced_settings*

Fires after advanced settings save.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1373](pages/page-mainwp-settings.php#L1373-L1380)



### `mainwp_advanced_settings_form_top`

*Action: mainwp_advanced_settings_form_top*

Fires at the top of advanced settings form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1401](pages/page-mainwp-settings.php#L1401-L1408)



### `mainwp_advanced_settings_form_bottom`

*Action: mainwp_advanced_settings_form_bottom*

Fires at the bottom of advanced settings form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1680](pages/page-mainwp-settings.php#L1680-L1687)



### `mainwp_settings_help_item`

*Action: mainwp_settings_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Settings page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 2393](pages/page-mainwp-settings.php#L2393-L2404)



### `mainwp_before_save_email_settings`

*Action: mainwp_before_save_email_settings*

Fires before save email settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`$update_settings` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 1898](pages/page-mainwp-manage-sites.php#L1898-L1905)



### `mainwp_after_save_email_settings`

*Action: mainwp_after_save_email_settings*

Fires after save email settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$settings_emails` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 1911](pages/page-mainwp-manage-sites.php#L1911-L1918)



### `mainwp_before_wp_config_section`

*Action: mainwp_before_wp_config_section*

Fires before the WP Config section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1601](pages/page-mainwp-server-information.php#L1601-L1608)



### `mainwp_after_wp_config_section`

*Action: mainwp_after_wp_config_section*

Fires after the WP Config section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1639](pages/page-mainwp-server-information.php#L1639-L1646)



### `mainwp_init_load_all_options`

*Method load_all_options()*

Load all wp_options data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$options` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 297](class/class-mainwp-system.php#L297-L380)



### `mainwp_module_cost_tracker_before_save_settings`

*Settigns Post*

Handles the save settings post request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$all_opts` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-admin.php](modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 552](modules/cost-tracker/classes/class-cost-tracker-admin.php#L552-L590)



### `mainwp_default_settings_indicator`

*Method render_not_default_indicator().*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$indi` |  | 
`$field` | `string` | setting field to check.
`$indi_value` |  | 
`$current_value` | `mixed` | setting current value.
`$render_indi` | `bool` | to render indication.
`$default_val` | `mixed` | default value directly.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings-indicator.php](pages/page-mainwp-settings-indicator.php), [line 72](pages/page-mainwp-settings-indicator.php#L72-L92)



### `mainwp_default_settings_indicator`

*Method render_not_default_email_settings_indicator().*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$indi` |  | 
`$field` | `string` | setting field to check.
`$def` |  | 
`$current_value` | `mixed` | setting current value.
`$render_indi` | `bool` | to render indication.
`$type` | `string` | setting type to get default value.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings-indicator.php](pages/page-mainwp-settings-indicator.php), [line 99](pages/page-mainwp-settings-indicator.php#L99-L115)



### `mainwp_clear_and_lock_options`

*Clean and Lock extension options*

Adds additional options related to Clean and Lock options in order to avoid conflicts when HTTP Basic auth is set.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-install-bulk.php](pages/page-mainwp-install-bulk.php), [line 379](pages/page-mainwp-install-bulk.php#L379-L386)




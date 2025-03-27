# UI & Display Filters

Hooks for modifying the Dashboard UI, widgets, menus, and display elements.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`deprecated_hook_run`](#deprecated_hook_run) - Display a deprecated notice for old hooks.
- [`mainwp_before_log_data`](#mainwp_before_log_data) - Method log_to_db()
- [`mainwp_before_seclect_sites`](#mainwp_before_seclect_sites) - Action: mainwp_before_seclect_sites
- [`mainwp_after_seclect_sites`](#mainwp_after_seclect_sites) - Action: mainwp_after_seclect_sites
- [`mainwp_overview_screen_options_top`](#mainwp_overview_screen_options_top) - Action: mainwp_overview_screen_options_top
- [`mainwp_overview_screen_options_bottom`](#mainwp_overview_screen_options_bottom) - Action: mainwp_overview_screen_options_bottom
- [`mainwp_before_subheader`](#mainwp_before_subheader) - Action: mainwp_before_subheader
- [`mainwp_subheader_actions`](#mainwp_subheader_actions) - Action: mainwp_subheader_actions
- [`mainwp_after_subheader`](#mainwp_after_subheader) - Action: mainwp_after_subheader
- [`mainwp_before_upload_custom_icon`](#mainwp_before_upload_custom_icon) - Action: mainwp_after_upload_custom_icon
- [`mainwp_after_upload_custom_icon`](#mainwp_after_upload_custom_icon) - Action: mainwp_after_upload_custom_icon
- [`mainwp_screen_options_modal_top`](#mainwp_screen_options_modal_top) - Action: mainwp_screen_options_modal_top
- [`mainwp_screen_options_modal_bottom`](#mainwp_screen_options_modal_bottom) - Action: mainwp_screen_options_modal_bottom
- [`mainwp-sitestable-prepared-items`](#mainwp-sitestable-prepared-items) - Action is being replaced with mainwp_sitestable_prepared_items
- [`mainwp_sitestable_prepared_items`](#mainwp_sitestable_prepared_items) - Action: mainwp_sitestable_prepared_items
- [`mainwp_admin_menu`](#mainwp_admin_menu) - Action: mainwp_admin_menu
- [`mainwp_admin_menu_sub`](#mainwp_admin_menu_sub) - Action: mainwp_admin_menu_sub
- [`before_mainwp_menu`](#before_mainwp_menu) - Action: before_mainwp_menu
- [`after_mainwp_menu`](#after_mainwp_menu) - Action: after_mainwp_menu
- [`before_mainwp_menu`](#before_mainwp_menu) - Action: before_mainwp_menu
- [`after_mainwp_menu`](#after_mainwp_menu) - Action: after_mainwp_menu
- [`mainwp_before_seclect_sites`](#mainwp_before_seclect_sites) - Action: mainwp_before_seclect_sites
- [`mainwp_after_seclect_sites`](#mainwp_after_seclect_sites) - Action: mainwp_after_seclect_sites
- [`mainwp_extensions_top_header_after_tab`](#mainwp_extensions_top_header_after_tab) - Method render_header()
- [`mainwp_removed_extension_menu`](#mainwp_removed_extension_menu) - Remove Extensions menu from MainWP Menu.
- [`mainwp_compact_action`](#mainwp_compact_action) - Create compact logs and erase records from the database.
- [`mainwp_module_dashboard_insights_help_item`](#mainwp_module_dashboard_insights_help_item) - Action: mainwp_module_dashboard_insights_help_item
- [`mainwp_before_overview_widgets`](#mainwp_before_overview_widgets) - Action: mainwp_before_overview_widgets
- [`mainwp_after_overview_widgets`](#mainwp_after_overview_widgets) - Action: 'mainwp_after_overview_widgets'
- [`mainwp_module_log_overview_screen_options_top`](#mainwp_module_log_overview_screen_options_top) - Action: mainwp_module_log_overview_screen_options_top
- [`mainwp_module_log_overview_screen_options_bottom`](#mainwp_module_log_overview_screen_options_bottom) - Action: mainwp_module_log_overview_screen_options_bottom
- [`mainwp_screen_options_modal_top`](#mainwp_screen_options_modal_top) - Action: mainwp_screen_options_modal_top
- [`mainwp_screen_options_modal_bottom`](#mainwp_screen_options_modal_bottom) - Action: mainwp_screen_options_modal_bottom
- [`mainwp_logs_manage_table_top`](#mainwp_logs_manage_table_top) - Action: mainwp_logs_manage_table_top
- [`mainwp_logs_manage_table_bottom`](#mainwp_logs_manage_table_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Actoin: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp_logs_widget_top) - Action: mainwp_logs_widget_top
- [`mainwp_logs_widget_bottom`](#mainwp_logs_widget_bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_before_overview_widgets`](#mainwp_before_overview_widgets) - Action: mainwp_before_overview_widgets
- [`mainwp_after_overview_widgets`](#mainwp_after_overview_widgets) - Action: 'mainwp_after_overview_widgets'
- [`mainwp_module_cost_tracker_summary_screen_options_top`](#mainwp_module_cost_tracker_summary_screen_options_top) - Action: mainwp_module_cost_tracker_summary_screen_options_top
- [`mainwp_module_cost_tracker_summary_screen_options_bottom`](#mainwp_module_cost_tracker_summary_screen_options_bottom) - Action: mainwp_module_cost_tracker_summary_screen_options_bottom
- [`mainwp_screen_options_modal_top`](#mainwp_screen_options_modal_top) - Action: mainwp_screen_options_modal_top
- [`mainwp_screen_options_modal_bottom`](#mainwp_screen_options_modal_bottom) - Action: mainwp_screen_options_modal_bottom
- [`mainwp_module_upcoming_renewals_before_costs_list`](#mainwp_module_upcoming_renewals_before_costs_list) - Action: mainwp_module_upcoming_renewals_before_costs_list
- [`mainwp_module_upcoming_renewals_after_costs_list`](#mainwp_module_upcoming_renewals_after_costs_list) - Action: mainwp_module_upcoming_renewals_after_costs_list
- [`mainwp_module_yearly_renewals_before_costs_list`](#mainwp_module_yearly_renewals_before_costs_list) - Action: mainwp_module_yearly_renewals_before_costs_list
- [`mainwp_module_yearly_renewals_after_costs_list`](#mainwp_module_yearly_renewals_after_costs_list) - Action: mainwp_module_yearly_renewals_after_costs_list
- [`mainwp_module_monthly_renewals_before_costs_list`](#mainwp_module_monthly_renewals_before_costs_list) - Action: mainwp_module_monthly_renewals_before_costs_list
- [`mainwp_module_monthly_renewals_after_costs_list`](#mainwp_module_monthly_renewals_after_costs_list) - Action: mainwp_module_monthly_renewals_after_costs_list
- [`mainwp_module_cost_tracker_widget_top`](#mainwp_module_cost_tracker_widget_top) - Action: mainwp_module_cost_tracker_widget_top
- [`mainwp_module_cost_tracker_widget_bottom`](#mainwp_module_cost_tracker_widget_bottom) - Action: mainwp_module_cost_tracker_widget_bottom
- [`mainwp_module_cost_tracker_widget_top`](#mainwp_module_cost_tracker_widget_top) - Action: mainwp_module_cost_tracker_widget_top
- [`mainwp_module_cost_tracker_widget_bottom`](#mainwp_module_cost_tracker_widget_bottom) - Action: mainwp_module_cost_tracker_widget_bottom
- [`mainwp_module_cost_tracker_widget_top`](#mainwp_module_cost_tracker_widget_top) - Action: mainwp_module_cost_tracker_widget_top
- [`mainwp_module_cost_tracker_widget_bottom`](#mainwp_module_cost_tracker_widget_bottom) - Action: mainwp_module_cost_tracker_widget_bottom
- [`mainwp_reset_admin_pass_modal_top`](#mainwp_reset_admin_pass_modal_top) - Action: mainwp_reset_admin_pass_modal_top
- [`mainwp_reset_admin_pass_modal_bottom`](#mainwp_reset_admin_pass_modal_bottom) - Action: mainwp_reset_admin_pass_modal_bottom
- [`mainwp_before_overview_widgets`](#mainwp_before_overview_widgets) - Action: mainwp_before_overview_widgets
- [`mainwp_after_overview_widgets`](#mainwp_after_overview_widgets) - Action: 'mainwp_after_overview_widgets'
- [`mainwp_before_server_info_table`](#mainwp_before_server_info_table) - Action: mainwp_before_server_info_table
- [`mainwp_after_server_info_table`](#mainwp_after_server_info_table) - Action: mainwp_after_server_info_table
- [`mainwp_before_cron_jobs_table`](#mainwp_before_cron_jobs_table) - Action: mainwp_before_cron_jobs_table
- [`mainwp_after_cron_jobs_table`](#mainwp_after_cron_jobs_table) - Action: mainwp_after_cron_jobs_table
- [`mainwp_before_error_log_table`](#mainwp_before_error_log_table) - Action: mainwp_before_error_log_table
- [`mainwp_after_error_log_table`](#mainwp_after_error_log_table) - Action: mainwp_after_error_log_table
- [`mainwp_before_overview_widgets`](#mainwp_before_overview_widgets) - Action: mainwp_before_overview_widgets
- [`mainwp_after_overview_widgets`](#mainwp_after_overview_widgets) - Action: 'mainwp_after_overview_widgets'
- [`mainwp_screen_options_modal_top`](#mainwp_screen_options_modal_top) - Action: mainwp_screen_options_modal_top
- [`mainwp_screen_options_modal_bottom`](#mainwp_screen_options_modal_bottom) - Action: mainwp_screen_options_modal_bottom
- [`mainwp_added_extension_menu`](#mainwp_added_extension_menu) - Adds Extension to the navigation menu
- [`mainwp_notes_widget_top`](#mainwp_notes_widget_top) - Action: mainwp_notes_widget_top
- [`mainwp_notes_widget_bottom`](#mainwp_notes_widget_bottom) - Action: mainwp_notes_widget_bottom
- [`mainwp_get_started_widget_top`](#mainwp_get_started_widget_top) - Action: mainwp_get_started_widget_top
- [`mainwp_get_started_widget_bottom`](#mainwp_get_started_widget_bottom) - Action: mainwp_get_started_widget_bottom
- [`mainwp_non_mainwp_changes_widget_top`](#mainwp_non_mainwp_changes_widget_top) - Actoin: mainwp_non_mainwp_changes_widget_top
- [`mainwp_non_mainwp_changes_table_top`](#mainwp_non_mainwp_changes_table_top) - Action: mainwp_non_mainwp_changes_table_top
- [`mainwp_non_mainwp_changes_table_bottom`](#mainwp_non_mainwp_changes_table_bottom) - Action: mainwp_non_mainwp_changes_table_bottom
- [`mainwp_non_mainwp_changes_widget_bottom`](#mainwp_non_mainwp_changes_widget_bottom) - Action: mainwp_non_mainwp_changes_widget_bottom
- [`mainwp_disablemenuitems`](#mainwp_disablemenuitems) - Method init()
- [`mainwp_main_menu_disable_menu_items`](#mainwp_main_menu_disable_menu_items) - Filter: mainwp_main_menu_disable_menu_items
- [`mainwp_ui_use_wp_calendar`](#mainwp_ui_use_wp_calendar) - Filter: mainwp_ui_use_wp_calendar
- [`mainwp_all_disablemenuitems`](#mainwp_all_disablemenuitems) - Method admin_footer()
- [`mainwp-getmetaboxes`](#mainwp-getmetaboxes) - Method apply_filter()
- [`mainwp_log_to_db_data`](#mainwp_log_to_db_data) - Method log_to_db()
- [`mainwp_menu_logo_href`](#mainwp_menu_logo_href) - *Arguments*
- [`mainwp_menu_logo_src`](#mainwp_menu_logo_src) - *Arguments*
- [`mainwp_menu_logo_alt`](#mainwp_menu_logo_alt) - *Arguments*
- [`mainwp_header_actions_right`](#mainwp_header_actions_right) - Filter: mainwp_header_actions_right
- [`mainwp_screen_options_pulse_control`](#mainwp_screen_options_pulse_control) - Method render_header_actions()
- [`mainwp_do_widget_boxes_sorted`](#mainwp_do_widget_boxes_sorted) - Method do_widget_boxes()
- [`mainwp_widget_boxes_show_widgets`](#mainwp_widget_boxes_show_widgets) - Method do_widget_boxes()
- [`mainwp-widgets-screen-options`](#mainwp-widgets-screen-options) - Method render_screen_options()
- [`mainwp_widgets_screen_options`](#mainwp_widgets_screen_options) - Filter: mainwp_widgets_screen_options
- [`mainwp-sitestable-item`](#mainwp-sitestable-item) - Filter is being replaced with mainwp_sitestable_item
- [`mainwp_sitestable_item`](#mainwp_sitestable_item) - Filter: mainwp_sitestable_item
- [`mainwp-sitestable-getcolumns`](#mainwp-sitestable-getcolumns) - Filter is being replaced with mainwp_sitestable_getcolumns
- [`mainwp_sitestable_getcolumns`](#mainwp_sitestable_getcolumns) - Filter: mainwp_sitestable_getcolumns
- [`mainwp_sitestable_prepare_extra_view`](#mainwp_sitestable_prepare_extra_view) - Prepare the items to be listed.
- [`mainwp_sitestable_display_row_columns`](#mainwp_sitestable_display_row_columns) - Get table rows.
- [`mainwp_sitestable_render_column`](#mainwp_sitestable_render_column) - Columns for a single row.
- [`mainwp_init_primary_menu_items`](#mainwp_init_primary_menu_items) - Method init_mainwp_menu_items()
- [`mainwp_is_disable_menu_item`](#mainwp_is_disable_menu_item) - Method is_disable_menu_item
- [`mainwp_main_menu`](#mainwp_main_menu) - Filter: mainwp_main_menu
- [`mainwp_main_menu_submenu`](#mainwp_main_menu_submenu) - Filter: mainwp_main_menu_submenu
- [`mainwp_go_back_wpadmin_link`](#mainwp_go_back_wpadmin_link) - Filter: mainwp_go_back_wpadmin_link
- [`mainwp_go_back_wpadmin_link`](#mainwp_go_back_wpadmin_link) - Filter: mainwp_go_back_wpadmin_link
- [`mainwp_insights_getmetaboxes`](#mainwp_insights_getmetaboxes) - Method add_meta_boxes()
- [`mainwp_module_log_overview_enabled_widgets`](#mainwp_module_log_overview_enabled_widgets) - Unset unwanted Widgets
- [`mainwp_module_log_widgets_screen_options`](#mainwp_module_log_widgets_screen_options) - Filter: mainwp_module_log_widgets_screen_options
- [`mainwp_cost_summary_getmetaboxes`](#mainwp_cost_summary_getmetaboxes) - Method add_meta_boxes()
- [`mainwp_module_cost_tracker_summary_enabled_widgets`](#mainwp_module_cost_tracker_summary_enabled_widgets) - Unset unwanted Widgets
- [`mainwp_module_cost_tracker_summary_widgets_screen_options`](#mainwp_module_cost_tracker_summary_widgets_screen_options) - Filter: mainwp_module_cost_tracker_summary_widgets_screen_options
- [`mainwp_module_cost_tracker_upcoming_renewals_widget_title`](#mainwp_module_cost_tracker_upcoming_renewals_widget_title) - *Arguments*
- [`mainwp_module_cost_tracker_yearly_renewals_widget_title`](#mainwp_module_cost_tracker_yearly_renewals_widget_title) - *Arguments*
- [`mainwp_module_cost_tracker_monthly_renewals_widget_title`](#mainwp_module_cost_tracker_monthly_renewals_widget_title) - *Arguments*
- [`mainwp_getmetaboxes`](#mainwp_getmetaboxes) - Method on_load_page_dashboard()
- [`mainwp_overview_enabled_widgets`](#mainwp_overview_enabled_widgets) - Unset unwanted Widgets
- [`mainwp_overview_enabled_widgets`](#mainwp_overview_enabled_widgets) - Unset unwanted Widgets
- [`mainwp_cron_jobs_table_features`](#mainwp_cron_jobs_table_features) - Filter: mainwp_cron_jobs_table_features
- [`mainwp_menu_extensions_left_menu`](#mainwp_menu_extensions_left_menu) - Method init_extensions_menu()
- [`mainwp_notes_widget_title`](#mainwp_notes_widget_title) - *Arguments*
- [`mainwp_widgets_chart_date_format`](#mainwp_widgets_chart_date_format) - Prepare response time for ui chart data.
- [`mainwp_get_started_widget_title`](#mainwp_get_started_widget_title) - *Arguments*
- [`mainwp_non_mainwp_changes_widget_title`](#mainwp_non_mainwp_changes_widget_title) - *Arguments*

## Hook Details

### `deprecated_hook_run`

*Display a deprecated notice for old hooks.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$old_hook` | `string` | Old hook.
`$new_hook` | `string` | New hook.
`$version` |  | 
`$message` | `string` | message.

Source: [class/class-mainwp-deprecated-hooks.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-deprecated-hooks.php), [line 152](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-deprecated-hooks.php#L152)



### `mainwp_before_log_data`

*Method log_to_db()*

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$text` | `string` | Log record text.
`$priority` | `int` | Set priority.
`$log_color` | `int` | Set color.

Source: [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L426)



### `mainwp_before_seclect_sites`

*Action: mainwp_before_seclect_sites*

Fires before the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 72](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L72)



### `mainwp_after_seclect_sites`

*Action: mainwp_after_seclect_sites*

Fires after the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 85](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L85)



### `mainwp_overview_screen_options_top`

*Action: mainwp_overview_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 823](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L823)



### `mainwp_overview_screen_options_bottom`

*Action: mainwp_overview_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 837](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L837)



### `mainwp_before_subheader`

*Action: mainwp_before_subheader*

Fires before the MainWP sub-header element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1152](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1152)



### `mainwp_subheader_actions`

*Action: mainwp_subheader_actions*

Fires at the subheader element to hook available actions.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1188](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1188)



### `mainwp_after_subheader`

*Action: mainwp_after_subheader*

Fires after the MainWP sub-header element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1201](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1201)



### `mainwp_before_upload_custom_icon`

*Action: mainwp_after_upload_custom_icon*

Fires before the modal element.


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1931](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1931)



### `mainwp_after_upload_custom_icon`

*Action: mainwp_after_upload_custom_icon*

Fires after the modal element.


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1961](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1961)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2480](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2480)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2572](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2572)



### `mainwp-sitestable-prepared-items`

*Action is being replaced with mainwp_sitestable_prepared_items*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($websites, $site_ids)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_prepared_items'` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1018](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1018)



### `mainwp_sitestable_prepared_items`

*Action: mainwp_sitestable_prepared_items*

Fires before the Sites table itemes are prepared.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites data.
`$site_ids` | `array` | Array containing IDs of all child sites.

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1025](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1025)



### `mainwp_admin_menu`

*Action: mainwp_admin_menu*

Hooks main navigation menu items.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 303](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L303)



### `mainwp_admin_menu_sub`

*Action: mainwp_admin_menu_sub*

Hooks main navigation sub-menu items.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 450](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L450)



### `before_mainwp_menu`

*Action: before_mainwp_menu*

Fires before the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 709](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L709)



### `after_mainwp_menu`

*Action: after_mainwp_menu*

Fires after the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 951](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L951)



### `before_mainwp_menu`

*Action: before_mainwp_menu*

Fires before the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 1073](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L1073)



### `after_mainwp_menu`

*Action: after_mainwp_menu*

Fires after the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 1271](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L1271)



### `mainwp_before_seclect_sites`

*Action: mainwp_before_seclect_sites*

Fires before the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 96](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L96)



### `mainwp_after_seclect_sites`

*Action: mainwp_after_seclect_sites*

Fires after the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 124](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L124)



### `mainwp_extensions_top_header_after_tab`

*Method render_header()*

Render page header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$shownPage` | `string` | The page slug shown at this moment.

Source: [class/class-mainwp-extensions-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php), [line 50](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php#L50)



### `mainwp_removed_extension_menu`

*Remove Extensions menu from MainWP Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key` |  | 

Source: [class/class-mainwp-post-extension-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-extension-handler.php), [line 408](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-extension-handler.php#L408)



### `mainwp_compact_action`

*Create compact logs and erase records from the database.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'saved'` |  | 
`$year` |  | 
`$year_data` |  | 
`$start_time` | `int` | start time to compact.
`$end_time` | `int` | end time to compact.

Source: [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 205](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L205)



### `mainwp_module_dashboard_insights_help_item`

*Action: mainwp_module_dashboard_insights_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Insights page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [modules/logs/classes/class-log-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php), [line 309](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php#L309)



### `mainwp_before_overview_widgets`

*Action: mainwp_before_overview_widgets*

Fires at the top of the Overview page (before first widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'insights'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 910](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L910)



### `mainwp_after_overview_widgets`

*Action: 'mainwp_after_overview_widgets'*

Fires at the bottom of the Overview page (after the last widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'insights'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 932](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L932)



### `mainwp_module_log_overview_screen_options_top`

*Action: mainwp_module_log_overview_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 969](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L969)



### `mainwp_module_log_overview_screen_options_bottom`

*Action: mainwp_module_log_overview_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 983](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L983)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 1057](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L1057)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 1093](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L1093)



### `mainwp_logs_manage_table_top`

*Action: mainwp_logs_manage_table_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'recent_events'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.4` | 

Source: [modules/logs/pages/page-log-manage-insights-events-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php), [line 186](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php#L186)



### `mainwp_logs_manage_table_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'recent_events'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.4` | 

Source: [modules/logs/pages/page-log-manage-insights-events-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php), [line 200](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php#L200)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'users'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-users-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php#L91)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'users'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-users-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php#L106)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'pages'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-pages-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php#L91)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'pages'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-pages-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php#L106)



### `mainwp_logs_widget_top`

*Actoin: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'recent_events'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-recent-events-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php), [line 85](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php#L85)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'recent_events'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-recent-events-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php), [line 100](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php#L100)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugins'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php#L91)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugins'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php#L106)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wp'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-wp-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php#L76)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wp'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-wp-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php#L91)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-status-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php#L76)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-status-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php#L91)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php#L76)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php#L91)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php#L76)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php#L91)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'php'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-php-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php#L76)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'php'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-php-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php#L91)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'themes'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php#L91)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'themes'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php#L106)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'core'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-sites-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php), [line 92](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php#L92)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'core'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-sites-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php), [line 107](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php#L107)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-tags-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php), [line 78](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php#L78)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'status'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-tags-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php), [line 93](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php#L93)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'posts'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-posts-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php#L91)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'posts'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-posts-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php#L106)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'themes'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php#L76)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'themes'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-graph-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php#L91)



### `mainwp_logs_widget_top`

*Action: mainwp_logs_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'clients'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php#L91)



### `mainwp_logs_widget_bottom`

*Action: mainwp_logs_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'clients'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/widgets/widget-log-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php#L106)



### `mainwp_before_overview_widgets`

*Action: mainwp_before_overview_widgets*

Fires at the top of the Overview page (before first widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'costsummary'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 373](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L373)



### `mainwp_after_overview_widgets`

*Action: 'mainwp_after_overview_widgets'*

Fires at the bottom of the Overview page (after the last widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'costsummary'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 393](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L393)



### `mainwp_module_cost_tracker_summary_screen_options_top`

*Action: mainwp_module_cost_tracker_summary_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 437](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L437)



### `mainwp_module_cost_tracker_summary_screen_options_bottom`

*Action: mainwp_module_cost_tracker_summary_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 451](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L451)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'costsummary'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 515](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L515)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'costsummary'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 551](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L551)



### `mainwp_module_upcoming_renewals_before_costs_list`

*Action: mainwp_module_upcoming_renewals_before_costs_list*

Fires before the list of costs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$tab` | `string` | Tab.
`$cost_data` | `array` | Cost data.

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 185](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L185)



### `mainwp_module_upcoming_renewals_after_costs_list`

*Action: mainwp_module_upcoming_renewals_after_costs_list*

Fires after the list of costs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$tab` | `string` | Tab.
`$cost_data` | `array` | Cost data.

**Changelog**

Version | Description
------- | -----------
`5.0.1` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 223](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L223)



### `mainwp_module_yearly_renewals_before_costs_list`

*Action: mainwp_module_yearly_renewals_before_costs_list*

Fires before the list of costs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$tab` | `string` | Tab.
`$cost_data` | `array` | Cost data.

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 193](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L193)



### `mainwp_module_yearly_renewals_after_costs_list`

*Action: mainwp_module_yearly_renewals_after_costs_list*

Fires after the list of costs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$tab` | `string` | Tab.
`$cost_data` | `array` | Cost data.

**Changelog**

Version | Description
------- | -----------
`5.0.1` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 243](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L243)



### `mainwp_module_monthly_renewals_before_costs_list`

*Action: mainwp_module_monthly_renewals_before_costs_list*

Fires before the list of costs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$tab` | `string` | Tab.
`$cost_data` | `array` | Cost data.

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 190](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L190)



### `mainwp_module_monthly_renewals_after_costs_list`

*Action: mainwp_module_monthly_renewals_after_costs_list*

Fires after the list of costs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$tab` | `string` | Tab.
`$cost_data` | `array` | Cost data.

**Changelog**

Version | Description
------- | -----------
`5.0.1` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 240](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L240)



### `mainwp_module_cost_tracker_widget_top`

*Action: mainwp_module_cost_tracker_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'payment-left-for-this-month'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php), [line 65](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php#L65)



### `mainwp_module_cost_tracker_widget_bottom`

*Action: mainwp_module_cost_tracker_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'payment-left-for-this-month'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php), [line 79](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php#L79)



### `mainwp_module_cost_tracker_widget_top`

*Action: mainwp_module_cost_tracker_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'monthly-totals'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php), [line 65](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php#L65)



### `mainwp_module_cost_tracker_widget_bottom`

*Action: mainwp_module_cost_tracker_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'monthly-totals'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php), [line 79](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php#L79)



### `mainwp_module_cost_tracker_widget_top`

*Action: mainwp_module_cost_tracker_widget_top*

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'category-totals'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php), [line 65](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php#L65)



### `mainwp_module_cost_tracker_widget_bottom`

*Action: mainwp_module_cost_tracker_widget_bottom*

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'category-totals'` |  | 

**Changelog**

Version | Description
------- | -----------
`5.0.2` | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php), [line 79](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php#L79)



### `mainwp_reset_admin_pass_modal_top`

*Action: mainwp_reset_admin_pass_modal_top*

Fires at the top of the Update Admin Passwords modal.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 193](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L193)



### `mainwp_reset_admin_pass_modal_bottom`

*Action: mainwp_reset_admin_pass_modal_bottom*

Fires at the bottom of the Update Admin Passwords modal.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 213](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L213)



### `mainwp_before_overview_widgets`

*Action: mainwp_before_overview_widgets*

Fires at the top of the Overview page (before first widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'dashboard'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 382](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L382)



### `mainwp_after_overview_widgets`

*Action: 'mainwp_after_overview_widgets'*

Fires at the bottom of the Overview page (after the last widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'dashboard'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 395](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L395)



### `mainwp_before_server_info_table`

*Action: mainwp_before_server_info_table*

Fires on the top of the Info page, before the Server Info table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 422](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L422)



### `mainwp_after_server_info_table`

*Action: mainwp_after_server_info_table*

Fires on the bottom of the Info page, after the Server Info table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 567](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L567)



### `mainwp_before_cron_jobs_table`

*Action: mainwp_before_cron_jobs_table*

Renders on the top of the Cron Jobs page, before the Schedules table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1044](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1044)



### `mainwp_after_cron_jobs_table`

*Action: mainwp_after_cron_jobs_table*

Renders on the bottom of the Cron Jobs page, after the Schedules table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1181](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1181)



### `mainwp_before_error_log_table`

*Action: mainwp_before_error_log_table*

Fires before the Error Log table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1449](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1449)



### `mainwp_after_error_log_table`

*Action: mainwp_after_error_log_table*

Fires after the Error Log table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1501](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1501)



### `mainwp_before_overview_widgets`

*Action: mainwp_before_overview_widgets*

Fires at the top of the Overview page (before first widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'clients'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 316](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L316)



### `mainwp_after_overview_widgets`

*Action: 'mainwp_after_overview_widgets'*

Fires at the bottom of the Overview page (after the last widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'clients'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 329](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L329)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 456](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L456)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 492](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L492)



### `mainwp_added_extension_menu`

*Adds Extension to the navigation menu*

Adds Extension instance to the Extensions located in the main MainWP navigation menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$slug` | `string` | Extension slug.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-extensions-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php), [line 345](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php#L345)



### `mainwp_notes_widget_top`

*Action: mainwp_notes_widget_top*

Fires at the top of the Notes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-notes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php), [line 70](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php#L70)



### `mainwp_notes_widget_bottom`

*Action: mainwp_notes_widget_bottom*

Fires at the bottom of the Notes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-notes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php), [line 95](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php#L95)



### `mainwp_get_started_widget_top`

*Action: mainwp_get_started_widget_top*

Fires top the widget.


**Changelog**

Version | Description
------- | -----------
`5.0` | 

Source: [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 93](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L93)



### `mainwp_get_started_widget_bottom`

*Action: mainwp_get_started_widget_bottom*

Fires bottom the widget.


**Changelog**

Version | Description
------- | -----------
`5.0` | 

Source: [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 135](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L135)



### `mainwp_non_mainwp_changes_widget_top`

*Actoin: mainwp_non_mainwp_changes_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 150](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L150)



### `mainwp_non_mainwp_changes_table_top`

*Action: mainwp_non_mainwp_changes_table_top*

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 162](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L162)



### `mainwp_non_mainwp_changes_table_bottom`

*Action: mainwp_non_mainwp_changes_table_bottom*

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 180](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L180)



### `mainwp_non_mainwp_changes_widget_bottom`

*Action: mainwp_non_mainwp_changes_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 205](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L205)



### `mainwp_disablemenuitems`

*Method init()*

Instantiate Plugin.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 584](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L584)



### `mainwp_main_menu_disable_menu_items`

*Filter: mainwp_main_menu_disable_menu_items*

Filters disabled MainWP navigation items.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 600](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L600)



### `mainwp_ui_use_wp_calendar`

*Filter: mainwp_ui_use_wp_calendar*

Filters whether default jQuery datepicker should be used to avoid potential problems with Senatic UI Calendar library.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0.5` | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 821](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L821)



### `mainwp_all_disablemenuitems`

*Method admin_footer()*

Create MainWP admin footer.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 1240](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L1240)



### `mainwp-getmetaboxes`

*Method apply_filter()*

Apply filter

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($value)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getmetaboxes'` |  | 

Source: [class/class-mainwp-system-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php), [line 188](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php#L188)



### `mainwp_log_to_db_data`

*Method log_to_db()*

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L426)



### `mainwp_menu_logo_href`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`admin_url('admin.php?page=mainwp_tab')` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 889](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L889)



### `mainwp_menu_logo_src`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`MAINWP_PLUGIN_URL . 'assets/images/mainwp-icon.svg'` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 901](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L901)



### `mainwp_menu_logo_alt`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'MainWP'` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 912](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L912)



### `mainwp_header_actions_right`

*Filter: mainwp_header_actions_right*

Filters the MainWP header element actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1345](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1345)



### `mainwp_screen_options_pulse_control`

*Method render_header_actions()*

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1273](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1273)



### `mainwp_do_widget_boxes_sorted`

*Method do_widget_boxes()*

Customize WordPress do_meta_boxes() function.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$wgsorted` |  | 
`$page` |  | 
`$client_id` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1605](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1605)



### `mainwp_widget_boxes_show_widgets`

*Method do_widget_boxes()*

Customize WordPress do_meta_boxes() function.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$page` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1605](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1605)



### `mainwp-widgets-screen-options`

*Method render_screen_options()*

Render modal window for Page Settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_widgets_screen_options'` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2421](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2421)



### `mainwp_widgets_screen_options`

*Filter: mainwp_widgets_screen_options*

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2457](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2457)



### `mainwp-sitestable-item`

*Filter is being replaced with mainwp_sitestable_item*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($item, $item)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_item'` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 180](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L180)



### `mainwp_sitestable_item`

*Filter: mainwp_sitestable_item*

Filters the Manage Sites table column items. Allows user to create new column item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item` | `array` | Array containing child site data.
`$column_name` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 187](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L187)



### `mainwp-sitestable-getcolumns`

*Filter is being replaced with mainwp_sitestable_getcolumns*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($columns, $columns)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_getcolumns'` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 322](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L322)



### `mainwp_sitestable_getcolumns`

*Filter: mainwp_sitestable_getcolumns*

Filters the Manage Sites table columns. Allows user to create a new column.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$columns` | `array` | Array containing table columns.
`$columns` | `array` | Array containing table columns.

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 329](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L329)



### `mainwp_sitestable_prepare_extra_view`

*Prepare the items to be listed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 694](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L694)



### `mainwp_sitestable_display_row_columns`

*Get table rows.*

Optimize for shared hosting or big networks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1554](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1554)



### `mainwp_sitestable_render_column`

*Columns for a single row.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` | `mixed` | Child Site.
`$classes` |  | 

Source: [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1971](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1971)



### `mainwp_init_primary_menu_items`

*Method init_mainwp_menu_items()*

Init MainWP menus.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$menus_items` | `array` | menus items.
`$part` | `string` | menus part.

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 332](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L332)



### `mainwp_is_disable_menu_item`

*Method is_disable_menu_item*

Check if $_mainwp_disable_menus_items contains any menu items to hide.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$disabled` |  | 
`$level` | `string` | The level the menu item is on.
`$item` | `array\|string` | The menu items meta data.

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 529](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L529)



### `mainwp_main_menu`

*Filter: mainwp_main_menu*

Filters main navigation menu items

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_leftmenu` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 684](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L684)



### `mainwp_main_menu_submenu`

*Filter: mainwp_main_menu_submenu*

Filters main navigation subt-menu items

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_sub_leftmenu` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 694](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L694)



### `mainwp_go_back_wpadmin_link`

*Filter: mainwp_go_back_wpadmin_link*

Filters URL for the Go to WP Admin button in Main navigation.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$link` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 799](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L799)



### `mainwp_go_back_wpadmin_link`

*Filter: mainwp_go_back_wpadmin_link*

Filters URL for the Go to WP Admin button in Main navigation.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$link` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 1242](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L1242)



### `mainwp_insights_getmetaboxes`

*Method add_meta_boxes()*

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 248](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L248)



### `mainwp_module_log_overview_enabled_widgets`

*Unset unwanted Widgets*

Contains the list of enabled widgets and allows user to unset unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$enable_widgets` |  | 
`null` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 284](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L284)



### `mainwp_module_log_widgets_screen_options`

*Filter: mainwp_module_log_widgets_screen_options*

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 1039](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L1039)



### `mainwp_cost_summary_getmetaboxes`

*Method add_meta_boxes()*

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 195](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L195)



### `mainwp_module_cost_tracker_summary_enabled_widgets`

*Unset unwanted Widgets*

Contains the list of enabled widgets and allows user to unset unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$enable_widgets` |  | 
`null` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 231](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L231)



### `mainwp_module_cost_tracker_summary_widgets_screen_options`

*Filter: mainwp_module_cost_tracker_summary_widgets_screen_options*

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 497](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L497)



### `mainwp_module_cost_tracker_upcoming_renewals_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Renewals', 'mainwp')` |  | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L59)



### `mainwp_module_cost_tracker_yearly_renewals_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Yearly Renewals', 'mainwp')` |  | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L59)



### `mainwp_module_cost_tracker_monthly_renewals_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Monthly Renewals', 'mainwp')` |  | 

Source: [modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L59)



### `mainwp_getmetaboxes`

*Method on_load_page_dashboard()*

Add individual meta boxes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 
`$dashboard_siteid` |  | 

Source: [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1401](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1401)



### `mainwp_overview_enabled_widgets`

*Unset unwanted Widgets*

Contains the list of enabled widgets and allows user to unset unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` | `array` | Array containing enabled widgets.
`$dashboard_siteid` | `int` | Child site (Overview) ID.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1454](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1454)



### `mainwp_overview_enabled_widgets`

*Unset unwanted Widgets*

Contains the list of enabled widgets and allows user to unset unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` | `array` | Array containing enabled widgets.
`null` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 230](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L230)



### `mainwp_cron_jobs_table_features`

*Filter: mainwp_cron_jobs_table_features*

Filters the Cron Schedules table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1155](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1155)



### `mainwp_menu_extensions_left_menu`

*Method init_extensions_menu()*

Initiate left Extensions menus.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extensions_and_leftmenus` |  | 

Source: [pages/page-mainwp-extensions-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php), [line 33](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php#L33)



### `mainwp_notes_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-notes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php), [line 62](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php#L62)



### `mainwp_widgets_chart_date_format`

*Prepare response time for ui chart data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$format_date` |  | 
`$params` | `array` | params.
`$slug` | `string` | for date format hook.

Source: [widgets/widget-mainwp-uptime-monitoring-site-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php), [line 615](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php#L615)



### `mainwp_get_started_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Get Started with MainWP', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 63](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L63)



### `mainwp_non_mainwp_changes_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites Changes', 'mainwp')` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 127](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L127)




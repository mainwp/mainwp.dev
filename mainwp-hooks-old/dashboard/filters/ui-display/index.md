# UI & Display Filters

Hooks for modifying the Dashboard UI, widgets, menus, and display elements.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-activated`](#mainwp-activated) - MainWP_System constructor.
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
- [`mainwp_cronload_action`](#mainwp_cronload_action) - Action: mainwp_cronload_action
- [`mainwp_admin_menu`](#mainwp_admin_menu) - Action: mainwp_admin_menu
- [`mainwp_admin_menu_sub`](#mainwp_admin_menu_sub) - Action: mainwp_admin_menu_sub
- [`before_mainwp_menu`](#before_mainwp_menu) - Action: before_mainwp_menu
- [`after_mainwp_menu`](#after_mainwp_menu) - Action: after_mainwp_menu
- [`before_mainwp_menu`](#before_mainwp_menu) - Action: before_mainwp_menu
- [`after_mainwp_menu`](#after_mainwp_menu) - Action: after_mainwp_menu
- [`mainwp_before_seclect_sites`](#mainwp_before_seclect_sites) - Action: mainwp_before_seclect_sites
- [`mainwp_after_seclect_sites`](#mainwp_after_seclect_sites) - Action: mainwp_after_seclect_sites
- [`mainwp_extensions_top_header_after_tab`](#mainwp_extensions_top_header_after_tab) - Method render_header()
- [`mainwp_before_template_part`](#mainwp_before_template_part) - Action: mainwp_before_template_part
- [`mainwp_after_template_part`](#mainwp_after_template_part) - Action: mainwp_after_template_part
- [`mainwp_removed_extension_menu`](#mainwp_removed_extension_menu) - Remove Extensions menu from MainWP Menu.
- [`mainwp_daily_digest_email_header`](#mainwp_daily_digest_email_header) - Daily Digest Email Header
- [`mainwp_daily_digest_email_footer`](#mainwp_daily_digest_email_footer) - Daily Digest Email Footer
- [`mainwp_module_log_record_insert_error`](#mainwp_module_log_record_insert_error) - Fires on a record insertion error
- [`mainwp_module_log_record_inserted`](#mainwp_module_log_record_inserted) - Fires after a record has been inserted
- [`mainwp_compact_action`](#mainwp_compact_action) - Create compact logs and erase records from the database.
- [`mainwp_log_action`](#mainwp_log_action) - Schedules a purge of records.
- [`mainwp_module_dashboard_insights_help_item`](#mainwp_module_dashboard_insights_help_item) - Action: mainwp_module_dashboard_insights_help_item
- [`mainwp_module_log_after_connectors_registration`](#mainwp_module_log_after_connectors_registration) - Fires after all connectors have been registered.
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
- [`mainwp_admin_enqueue_scripts`](#mainwp_admin_enqueue_scripts) - Method admin_enqueue_scripts()
- [`mainwp_all_disablemenuitems`](#mainwp_all_disablemenuitems) - Method admin_footer()
- [`minwp_notification_template_copy_message`](#minwp_notification_template_copy_message) - Use mainwp_notification_template_copy_message instead.
- [`mainwp_notification_template_copy_message`](#mainwp_notification_template_copy_message) - Filter mainwp_notification_template_copy_message.
- [`mainwp_notification_type_desc`](#mainwp_notification_type_desc) - Get email settings description.
- [`mainwp_notification_types`](#mainwp_notification_types) - Get email notification types.
- [`mainwp_default_emails_fields`](#mainwp_default_emails_fields) - Get default email notifications values.
- [`mainwp-getmetaboxes`](#mainwp-getmetaboxes) - Method apply_filter()
- [`{$filter}`](#filter) - Method apply_filter()
- [`mainwp_log_status`](#mainwp_log_status) - MainWP_Logger constructor.
- [`mainwp_log_specific`](#mainwp_log_specific) - MainWP_Logger constructor.
- [`mainwp_log_to_db_data`](#mainwp_log_to_db_data) - Method log_to_db()
- [`mainwp_file_uploader_size_limit`](#mainwp_file_uploader_size_limit) - Filter: 'mainwp_file_uploader_size_limit'
- [`mainwp_menu_logo_href`](#mainwp_menu_logo_href) - *Arguments*
- [`mainwp_menu_logo_src`](#mainwp_menu_logo_src) - *Arguments*
- [`mainwp_menu_logo_alt`](#mainwp_menu_logo_alt) - *Arguments*
- [`mainwp_header_actions_right`](#mainwp_header_actions_right) - Filter: mainwp_header_actions_right
- [`mainwp_screen_options_pulse_control`](#mainwp_screen_options_pulse_control) - Method render_header_actions()
- [`mainwp_do_widget_boxes_sorted`](#mainwp_do_widget_boxes_sorted) - Method do_widget_boxes()
- [`mainwp_widget_boxes_show_widgets`](#mainwp_widget_boxes_show_widgets) - Method do_widget_boxes()
- [`mainwp-widgets-screen-options`](#mainwp-widgets-screen-options) - Method render_screen_options()
- [`mainwp_widgets_screen_options`](#mainwp_widgets_screen_options) - Filter: mainwp_widgets_screen_options
- [`mainwp_format_email`](#mainwp_format_email) - Method format_email()
- [`mainwp-sitestable-item`](#mainwp-sitestable-item) - Filter is being replaced with mainwp_sitestable_item
- [`mainwp_sitestable_item`](#mainwp_sitestable_item) - Filter: mainwp_sitestable_item
- [`mainwp-sitestable-getcolumns`](#mainwp-sitestable-getcolumns) - Filter is being replaced with mainwp_sitestable_getcolumns
- [`mainwp_sitestable_getcolumns`](#mainwp_sitestable_getcolumns) - Filter: mainwp_sitestable_getcolumns
- [`mainwp_sitestable_prepare_extra_view`](#mainwp_sitestable_prepare_extra_view) - Prepare the items to be listed.
- [`mainwp_sitestable_display_row_columns`](#mainwp_sitestable_display_row_columns) - Get table rows.
- [`mainwp_sitestable_render_column`](#mainwp_sitestable_render_column) - Columns for a single row.
- [`mainwp_open_hide_referrer`](#mainwp_open_hide_referrer) - Filter: mainwp_open_hide_referrer
- [`mainwp_is_enable_schedule_job`](#mainwp_is_enable_schedule_job) - Method init_mainwp_cron()
- [`mainwp_text_format_email`](#mainwp_text_format_email) - Filter: mainwp_text_format_email
- [`mainwp_license_deactivated_alert_plain_text`](#mainwp_license_deactivated_alert_plain_text) - Method cron_deactivated_licenses_alert()
- [`mainwp_register_regular_sequence_process`](#mainwp_register_regular_sequence_process) - Method perform_sequence_process
- [`mainwp_try_visit_follow_location`](#mainwp_try_visit_follow_location) - Method try visit.
- [`mainwp_curl_curlopt_resolve`](#mainwp_curl_curlopt_resolve) - Method try visit.
- [`mainwp_fetch_urls_chunk_size`](#mainwp_fetch_urls_chunk_size) - Method fetch_urls_authed()
- [`mainwp_init_primary_menu_items`](#mainwp_init_primary_menu_items) - Method init_mainwp_menu_items()
- [`mainwp_is_disable_menu_item`](#mainwp_is_disable_menu_item) - Method is_disable_menu_item
- [`mainwp_main_menu`](#mainwp_main_menu) - Filter: mainwp_main_menu
- [`mainwp_main_menu_submenu`](#mainwp_main_menu_submenu) - Filter: mainwp_main_menu_submenu
- [`mainwp_go_back_wpadmin_link`](#mainwp_go_back_wpadmin_link) - Filter: mainwp_go_back_wpadmin_link
- [`mainwp_go_back_wpadmin_link`](#mainwp_go_back_wpadmin_link) - Filter: mainwp_go_back_wpadmin_link
- [`mainwp_get_template`](#mainwp_get_template) - Filter: mainwp_get_template
- [`mainwp_locate_template`](#mainwp_locate_template) - Filer: mainwp_locate_template
- [`mainwp_get_notification_template_name_by_type`](#mainwp_get_notification_template_name_by_type) - Get default template name by email/notification type.
- [`mainwp_default_template_source_dir`](#mainwp_default_template_source_dir) - Method handle_template_file_action()
- [`mainwp_module_log_record_array`](#mainwp_module_log_record_array) - Filter allows modification of record information
- [`mainwp_module_log_query_args`](#mainwp_module_log_query_args) - Filter allows additional arguments to query $args
- [`mainwp_module_log_current_agent`](#mainwp_module_log_current_agent) - Filter the current agent string
- [`mainwp_module_log_agent_label`](#mainwp_module_log_agent_label) - Filter agent labels
- [`mainwp_module_log_connectors`](#mainwp_module_log_connectors) - Allows for adding additional connectors via classes that extend Connector.
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

### `mainwp-activated`

*MainWP_System constructor.*

Runs any time class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`'4.0.7.2'` |  | 
`'mainwp_activated'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 82](class/class-mainwp-system.php#L82-L246)



### `deprecated_hook_run`

*Display a deprecated notice for old hooks.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$old_hook` | `string` | Old hook.
`$new_hook` | `string` | New hook.
`$version` |  | 
`$message` | `string` | message.

Source: [../sources/mainwp-dashboard/class/class-mainwp-deprecated-hooks.php](class/class-mainwp-deprecated-hooks.php), [line 152](class/class-mainwp-deprecated-hooks.php#L152-L166)



### `mainwp_before_log_data`

*Method log_to_db()*

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$text` | `string` | Log record text.
`$priority` | `int` | Set priority.
`$log_color` | `int` | Set color.

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 426](class/class-mainwp-logger.php#L426-L465)



### `mainwp_before_seclect_sites`

*Action: mainwp_before_seclect_sites*

Fires before the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 72](class/class-mainwp-ui.php#L72-L79)



### `mainwp_after_seclect_sites`

*Action: mainwp_after_seclect_sites*

Fires after the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 85](class/class-mainwp-ui.php#L85-L92)



### `mainwp_overview_screen_options_top`

*Action: mainwp_overview_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 823](class/class-mainwp-ui.php#L823-L830)



### `mainwp_overview_screen_options_bottom`

*Action: mainwp_overview_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 837](class/class-mainwp-ui.php#L837-L844)



### `mainwp_before_subheader`

*Action: mainwp_before_subheader*

Fires before the MainWP sub-header element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1152](class/class-mainwp-ui.php#L1152-L1159)



### `mainwp_subheader_actions`

*Action: mainwp_subheader_actions*

Fires at the subheader element to hook available actions.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1188](class/class-mainwp-ui.php#L1188-L1195)



### `mainwp_after_subheader`

*Action: mainwp_after_subheader*

Fires after the MainWP sub-header element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1201](class/class-mainwp-ui.php#L1201-L1208)



### `mainwp_before_upload_custom_icon`

*Action: mainwp_after_upload_custom_icon*

Fires before the modal element.


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1931](class/class-mainwp-ui.php#L1931-L1938)



### `mainwp_after_upload_custom_icon`

*Action: mainwp_after_upload_custom_icon*

Fires after the modal element.


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1961](class/class-mainwp-ui.php#L1961-L1968)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2480](class/class-mainwp-ui.php#L2480-L2487)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2572](class/class-mainwp-ui.php#L2572-L2579)



### `mainwp-sitestable-prepared-items`

*Action is being replaced with mainwp_sitestable_prepared_items*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($websites, $site_ids)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_prepared_items'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1018](class/class-mainwp-manage-sites-list-table.php#L1018-L1023)



### `mainwp_sitestable_prepared_items`

*Action: mainwp_sitestable_prepared_items*

Fires before the Sites table itemes are prepared.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites data.
`$site_ids` | `array` | Array containing IDs of all child sites.

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1025](class/class-mainwp-manage-sites-list-table.php#L1025-L1035)



### `mainwp_cronload_action`

*Action: mainwp_cronload_action*

Hooks MainWP cron jobs actions.


Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 61](class/class-mainwp-system-cron-jobs.php#L61-L68)



### `mainwp_admin_menu`

*Action: mainwp_admin_menu*

Hooks main navigation menu items.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 303](class/class-mainwp-menu.php#L303-L310)



### `mainwp_admin_menu_sub`

*Action: mainwp_admin_menu_sub*

Hooks main navigation sub-menu items.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 450](class/class-mainwp-menu.php#L450-L457)



### `before_mainwp_menu`

*Action: before_mainwp_menu*

Fires before the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 709](class/class-mainwp-menu.php#L709-L716)



### `after_mainwp_menu`

*Action: after_mainwp_menu*

Fires after the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 951](class/class-mainwp-menu.php#L951-L958)



### `before_mainwp_menu`

*Action: before_mainwp_menu*

Fires before the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 1073](class/class-mainwp-menu.php#L1073-L1080)



### `after_mainwp_menu`

*Action: after_mainwp_menu*

Fires after the main navigation element.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 1271](class/class-mainwp-menu.php#L1271-L1278)



### `mainwp_before_seclect_sites`

*Action: mainwp_before_seclect_sites*

Fires before the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui-select-sites.php](class/class-mainwp-ui-select-sites.php), [line 96](class/class-mainwp-ui-select-sites.php#L96-L103)



### `mainwp_after_seclect_sites`

*Action: mainwp_after_seclect_sites*

Fires after the Select Sites box.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui-select-sites.php](class/class-mainwp-ui-select-sites.php), [line 124](class/class-mainwp-ui-select-sites.php#L124-L131)



### `mainwp_extensions_top_header_after_tab`

*Method render_header()*

Render page header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$shownPage` | `string` | The page slug shown at this moment.

Source: [../sources/mainwp-dashboard/class/class-mainwp-extensions-view.php](class/class-mainwp-extensions-view.php), [line 50](class/class-mainwp-extensions-view.php#L50-L99)



### `mainwp_before_template_part`

*Action: mainwp_before_template_part*

Fires before the email template is loaded.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template_name` | `string` | Template name.
`$located` | `resource` | Template file.
`$args` | `array` | Args.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 166](class/class-mainwp-notification-template.php#L166-L177)



### `mainwp_after_template_part`

*Action: mainwp_after_template_part*

Fires after the email template is loaded.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template_name` | `string` | Template name.
`$located` | `resource` | Template file.
`$args` | `array` | Args.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 181](class/class-mainwp-notification-template.php#L181-L192)



### `mainwp_removed_extension_menu`

*Remove Extensions menu from MainWP Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-extension-handler.php](class/class-mainwp-post-extension-handler.php), [line 408](class/class-mainwp-post-extension-handler.php#L408-L427)



### `mainwp_daily_digest_email_header`

*Daily Digest Email Header*

Fires at the top of the daily digest email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/templates/emails/mainwp-daily-digest-email.php](templates/emails/mainwp-daily-digest-email.php), [line 29](templates/emails/mainwp-daily-digest-email.php#L29-L36)



### `mainwp_daily_digest_email_footer`

*Daily Digest Email Footer*

Fires at the bottom of the daily digest email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/templates/emails/mainwp-daily-digest-email.php](templates/emails/mainwp-daily-digest-email.php), [line 177](templates/emails/mainwp-daily-digest-email.php#L177-L184)



### `mainwp_module_log_record_insert_error`

*Fires on a record insertion error*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` | 
`false` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-db.php](modules/logs/classes/class-log-db.php), [line 77](modules/logs/classes/class-log-db.php#L77-L83)



### `mainwp_module_log_record_inserted`

*Fires after a record has been inserted*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record_id` | `int` | 
`$record` | `array` | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-db.php](modules/logs/classes/class-log-db.php), [line 88](modules/logs/classes/class-log-db.php#L88-L94)



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

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-db.php](modules/logs/classes/class-log-db.php), [line 205](modules/logs/classes/class-log-db.php#L205-L266)



### `mainwp_log_action`

*Schedules a purge of records.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'module log :: purge logs schedule start.'` |  | 
`MainWP_Logger::LOGS_AUTO_PURGE_LOG_PRIORITY` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-admin.php](modules/logs/classes/class-log-admin.php), [line 192](modules/logs/classes/class-log-admin.php#L192-L217)



### `mainwp_module_dashboard_insights_help_item`

*Action: mainwp_module_dashboard_insights_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Insights page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-admin.php](modules/logs/classes/class-log-admin.php), [line 309](modules/logs/classes/class-log-admin.php#L309-L320)



### `mainwp_module_log_after_connectors_registration`

*Fires after all connectors have been registered.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$labels` | `array` | All register connectors labels array
`$this` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-connectors.php](modules/logs/classes/class-log-connectors.php), [line 179](modules/logs/classes/class-log-connectors.php#L179-L185)



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

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 910](modules/logs/pages/page-log-insights-page.php#L910-L917)



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

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 932](modules/logs/pages/page-log-insights-page.php#L932-L939)



### `mainwp_module_log_overview_screen_options_top`

*Action: mainwp_module_log_overview_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 969](modules/logs/pages/page-log-insights-page.php#L969-L976)



### `mainwp_module_log_overview_screen_options_bottom`

*Action: mainwp_module_log_overview_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 983](modules/logs/pages/page-log-insights-page.php#L983-L990)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 1057](modules/logs/pages/page-log-insights-page.php#L1057-L1064)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 1093](modules/logs/pages/page-log-insights-page.php#L1093-L1100)



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

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-manage-insights-events-page.php](modules/logs/pages/page-log-manage-insights-events-page.php), [line 186](modules/logs/pages/page-log-manage-insights-events-page.php#L186-L193)



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

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-manage-insights-events-page.php](modules/logs/pages/page-log-manage-insights-events-page.php), [line 200](modules/logs/pages/page-log-manage-insights-events-page.php#L200-L207)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-users-widget.php](modules/logs/widgets/widget-log-users-widget.php), [line 91](modules/logs/widgets/widget-log-users-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-users-widget.php](modules/logs/widgets/widget-log-users-widget.php), [line 106](modules/logs/widgets/widget-log-users-widget.php#L106-L113)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-pages-widget.php](modules/logs/widgets/widget-log-pages-widget.php), [line 91](modules/logs/widgets/widget-log-pages-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-pages-widget.php](modules/logs/widgets/widget-log-pages-widget.php), [line 106](modules/logs/widgets/widget-log-pages-widget.php#L106-L113)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-recent-events-widget.php](modules/logs/widgets/widget-log-recent-events-widget.php), [line 85](modules/logs/widgets/widget-log-recent-events-widget.php#L85-L92)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-recent-events-widget.php](modules/logs/widgets/widget-log-recent-events-widget.php), [line 100](modules/logs/widgets/widget-log-recent-events-widget.php#L100-L107)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-plugins-widget.php](modules/logs/widgets/widget-log-plugins-widget.php), [line 91](modules/logs/widgets/widget-log-plugins-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-plugins-widget.php](modules/logs/widgets/widget-log-plugins-widget.php), [line 106](modules/logs/widgets/widget-log-plugins-widget.php#L106-L113)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-wp-widget.php](modules/logs/widgets/widget-log-graph-wp-widget.php), [line 76](modules/logs/widgets/widget-log-graph-wp-widget.php#L76-L83)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-wp-widget.php](modules/logs/widgets/widget-log-graph-wp-widget.php), [line 91](modules/logs/widgets/widget-log-graph-wp-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-status-widget.php](modules/logs/widgets/widget-log-graph-status-widget.php), [line 76](modules/logs/widgets/widget-log-graph-status-widget.php#L76-L83)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-status-widget.php](modules/logs/widgets/widget-log-graph-status-widget.php), [line 91](modules/logs/widgets/widget-log-graph-status-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-clients-widget.php](modules/logs/widgets/widget-log-graph-clients-widget.php), [line 76](modules/logs/widgets/widget-log-graph-clients-widget.php#L76-L83)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-clients-widget.php](modules/logs/widgets/widget-log-graph-clients-widget.php), [line 91](modules/logs/widgets/widget-log-graph-clients-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-plugins-widget.php](modules/logs/widgets/widget-log-graph-plugins-widget.php), [line 76](modules/logs/widgets/widget-log-graph-plugins-widget.php#L76-L83)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-plugins-widget.php](modules/logs/widgets/widget-log-graph-plugins-widget.php), [line 91](modules/logs/widgets/widget-log-graph-plugins-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-php-widget.php](modules/logs/widgets/widget-log-graph-php-widget.php), [line 76](modules/logs/widgets/widget-log-graph-php-widget.php#L76-L83)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-php-widget.php](modules/logs/widgets/widget-log-graph-php-widget.php), [line 91](modules/logs/widgets/widget-log-graph-php-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-themes-widget.php](modules/logs/widgets/widget-log-themes-widget.php), [line 91](modules/logs/widgets/widget-log-themes-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-themes-widget.php](modules/logs/widgets/widget-log-themes-widget.php), [line 106](modules/logs/widgets/widget-log-themes-widget.php#L106-L113)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-sites-widget.php](modules/logs/widgets/widget-log-sites-widget.php), [line 92](modules/logs/widgets/widget-log-sites-widget.php#L92-L99)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-sites-widget.php](modules/logs/widgets/widget-log-sites-widget.php), [line 107](modules/logs/widgets/widget-log-sites-widget.php#L107-L114)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-tags-widget.php](modules/logs/widgets/widget-log-graph-tags-widget.php), [line 78](modules/logs/widgets/widget-log-graph-tags-widget.php#L78-L85)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-tags-widget.php](modules/logs/widgets/widget-log-graph-tags-widget.php), [line 93](modules/logs/widgets/widget-log-graph-tags-widget.php#L93-L100)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-posts-widget.php](modules/logs/widgets/widget-log-posts-widget.php), [line 91](modules/logs/widgets/widget-log-posts-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-posts-widget.php](modules/logs/widgets/widget-log-posts-widget.php), [line 106](modules/logs/widgets/widget-log-posts-widget.php#L106-L113)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-themes-widget.php](modules/logs/widgets/widget-log-graph-themes-widget.php), [line 76](modules/logs/widgets/widget-log-graph-themes-widget.php#L76-L83)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-graph-themes-widget.php](modules/logs/widgets/widget-log-graph-themes-widget.php), [line 91](modules/logs/widgets/widget-log-graph-themes-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-clients-widget.php](modules/logs/widgets/widget-log-clients-widget.php), [line 91](modules/logs/widgets/widget-log-clients-widget.php#L91-L98)



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

Source: [../sources/mainwp-dashboard/modules/logs/widgets/widget-log-clients-widget.php](modules/logs/widgets/widget-log-clients-widget.php), [line 106](modules/logs/widgets/widget-log-clients-widget.php#L106-L113)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 373](modules/cost-tracker/classes/class-cost-tracker-summary.php#L373-L380)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 393](modules/cost-tracker/classes/class-cost-tracker-summary.php#L393-L400)



### `mainwp_module_cost_tracker_summary_screen_options_top`

*Action: mainwp_module_cost_tracker_summary_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 437](modules/cost-tracker/classes/class-cost-tracker-summary.php#L437-L444)



### `mainwp_module_cost_tracker_summary_screen_options_bottom`

*Action: mainwp_module_cost_tracker_summary_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 451](modules/cost-tracker/classes/class-cost-tracker-summary.php#L451-L458)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 515](modules/cost-tracker/classes/class-cost-tracker-summary.php#L515-L522)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 551](modules/cost-tracker/classes/class-cost-tracker-summary.php#L551-L558)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 185](modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L185-L195)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 223](modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L223-L233)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 193](modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L193-L203)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 243](modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L243-L253)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 190](modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L190-L200)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 240](modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L240-L250)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php](modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php), [line 65](modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php#L65-L72)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php](modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php), [line 79](modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php#L79-L86)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php](modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php), [line 65](modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php#L65-L72)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php](modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php), [line 79](modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php#L79-L86)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php](modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php), [line 65](modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php#L65-L72)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php](modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php), [line 79](modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php#L79-L86)



### `mainwp_reset_admin_pass_modal_top`

*Action: mainwp_reset_admin_pass_modal_top*

Fires at the top of the Update Admin Passwords modal.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-bulk-update-admin-passwords.php](pages/page-mainwp-bulk-update-admin-passwords.php), [line 193](pages/page-mainwp-bulk-update-admin-passwords.php#L193-L200)



### `mainwp_reset_admin_pass_modal_bottom`

*Action: mainwp_reset_admin_pass_modal_bottom*

Fires at the bottom of the Update Admin Passwords modal.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-bulk-update-admin-passwords.php](pages/page-mainwp-bulk-update-admin-passwords.php), [line 213](pages/page-mainwp-bulk-update-admin-passwords.php#L213-L220)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-overview.php](pages/page-mainwp-overview.php), [line 382](pages/page-mainwp-overview.php#L382-L389)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-overview.php](pages/page-mainwp-overview.php), [line 395](pages/page-mainwp-overview.php#L395-L402)



### `mainwp_before_server_info_table`

*Action: mainwp_before_server_info_table*

Fires on the top of the Info page, before the Server Info table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 422](pages/page-mainwp-server-information.php#L422-L429)



### `mainwp_after_server_info_table`

*Action: mainwp_after_server_info_table*

Fires on the bottom of the Info page, after the Server Info table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 567](pages/page-mainwp-server-information.php#L567-L574)



### `mainwp_before_cron_jobs_table`

*Action: mainwp_before_cron_jobs_table*

Renders on the top of the Cron Jobs page, before the Schedules table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1044](pages/page-mainwp-server-information.php#L1044-L1051)



### `mainwp_after_cron_jobs_table`

*Action: mainwp_after_cron_jobs_table*

Renders on the bottom of the Cron Jobs page, after the Schedules table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1181](pages/page-mainwp-server-information.php#L1181-L1188)



### `mainwp_before_error_log_table`

*Action: mainwp_before_error_log_table*

Fires before the Error Log table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1449](pages/page-mainwp-server-information.php#L1449-L1456)



### `mainwp_after_error_log_table`

*Action: mainwp_after_error_log_table*

Fires after the Error Log table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1501](pages/page-mainwp-server-information.php#L1501-L1508)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 316](pages/page-mainwp-client-overview.php#L316-L323)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 329](pages/page-mainwp-client-overview.php#L329-L336)



### `mainwp_screen_options_modal_top`

*Action: mainwp_screen_options_modal_top*

Fires at the top of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 456](pages/page-mainwp-client-overview.php#L456-L463)



### `mainwp_screen_options_modal_bottom`

*Action: mainwp_screen_options_modal_bottom*

Fires at the bottom of the Page Settings modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 492](pages/page-mainwp-client-overview.php#L492-L499)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-handler.php](pages/page-mainwp-extensions-handler.php), [line 345](pages/page-mainwp-extensions-handler.php#L345-L354)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-notes.php](widgets/widget-mainwp-notes.php), [line 70](widgets/widget-mainwp-notes.php#L70-L79)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-notes.php](widgets/widget-mainwp-notes.php), [line 95](widgets/widget-mainwp-notes.php#L95-L104)



### `mainwp_get_started_widget_top`

*Action: mainwp_get_started_widget_top*

Fires top the widget.


**Changelog**

Version | Description
------- | -----------
`5.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-get-started.php](widgets/widget-mainwp-get-started.php), [line 93](widgets/widget-mainwp-get-started.php#L93-L100)



### `mainwp_get_started_widget_bottom`

*Action: mainwp_get_started_widget_bottom*

Fires bottom the widget.


**Changelog**

Version | Description
------- | -----------
`5.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-get-started.php](widgets/widget-mainwp-get-started.php), [line 135](widgets/widget-mainwp-get-started.php#L135-L142)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-actions.php](widgets/widget-mainwp-site-actions.php), [line 150](widgets/widget-mainwp-site-actions.php#L150-L159)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-actions.php](widgets/widget-mainwp-site-actions.php), [line 162](widgets/widget-mainwp-site-actions.php#L162-L171)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-actions.php](widgets/widget-mainwp-site-actions.php), [line 180](widgets/widget-mainwp-site-actions.php#L180-L189)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-actions.php](widgets/widget-mainwp-site-actions.php), [line 205](widgets/widget-mainwp-site-actions.php#L205-L214)



### `mainwp_disablemenuitems`

*Method init()*

Instantiate Plugin.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 584](class/class-mainwp-system.php#L584-L598)



### `mainwp_main_menu_disable_menu_items`

*Filter: mainwp_main_menu_disable_menu_items*

Filters disabled MainWP navigation items.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 600](class/class-mainwp-system.php#L600-L607)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 821](class/class-mainwp-system.php#L821-L828)



### `mainwp_admin_enqueue_scripts`

*Method admin_enqueue_scripts()*

Enqueue all Mainwp Admin Scripts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 1053](class/class-mainwp-system.php#L1053-L1102)



### `mainwp_all_disablemenuitems`

*Method admin_footer()*

Create MainWP admin footer.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 1240](class/class-mainwp-system.php#L1240-L1330)



### `minwp_notification_template_copy_message`

*Use mainwp_notification_template_copy_message instead.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 330](class/class-mainwp-notification-settings.php#L330-L336)



### `mainwp_notification_template_copy_message`

*Filter mainwp_notification_template_copy_message.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$copy_message` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 337](class/class-mainwp-notification-settings.php#L337-L343)



### `mainwp_notification_type_desc`

*Get email settings description.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | Email notification type.

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 378](class/class-mainwp-notification-settings.php#L378-L399)



### `mainwp_notification_types`

*Get email notification types.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$type` | `string` | Email notification type.

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 426](class/class-mainwp-notification-settings.php#L426-L447)



### `mainwp_default_emails_fields`

*Get default email notifications values.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$recipients` |  | 
`$type` | `string` | Email type.
`$field` | `string` | Field name.
`$general` | `bool` | General or individual site settings.

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 551](class/class-mainwp-notification-settings.php#L551-L600)



### `mainwp-getmetaboxes`

*Method apply_filter()*

Apply filter

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($value)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getmetaboxes'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-handler.php](class/class-mainwp-system-handler.php), [line 188](class/class-mainwp-system-handler.php#L188-L203)



### `{$filter}`

*Method apply_filter()*

Apply filter

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` | `array` | Input value.

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-handler.php](class/class-mainwp-system-handler.php), [line 188](class/class-mainwp-system-handler.php#L188-L205)



### `mainwp_log_status`

*MainWP_Logger constructor.*

Run each time the class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$enabled` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 129](class/class-mainwp-logger.php#L129-L141)



### `mainwp_log_specific`

*MainWP_Logger constructor.*

Run each time the class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 129](class/class-mainwp-logger.php#L129-L142)



### `mainwp_log_to_db_data`

*Method log_to_db()*

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 426](class/class-mainwp-logger.php#L426-L495)



### `mainwp_file_uploader_size_limit`

*Filter: 'mainwp_file_uploader_size_limit'*

Filters the maximum upload file size. Default: 8388608 Bytes (B) = 8 Megabytes (MB)

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sizeLimit` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-qq2-file-uploader.php](class/class-mainwp-qq2-file-uploader.php), [line 56](class/class-mainwp-qq2-file-uploader.php#L56-L63)



### `mainwp_menu_logo_href`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`admin_url('admin.php?page=mainwp_tab')` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 889](class/class-mainwp-ui.php#L889-L889)



### `mainwp_menu_logo_src`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`MAINWP_PLUGIN_URL . 'assets/images/mainwp-icon.svg'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 901](class/class-mainwp-ui.php#L901-L901)



### `mainwp_menu_logo_alt`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'MainWP'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 912](class/class-mainwp-ui.php#L912-L912)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1345](class/class-mainwp-ui.php#L1345-L1352)



### `mainwp_screen_options_pulse_control`

*Method render_header_actions()*

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1273](class/class-mainwp-ui.php#L1273-L1428)



### `mainwp_do_widget_boxes_sorted`

*Method do_widget_boxes()*

Customize WordPress do_meta_boxes() function.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$wgsorted` |  | 
`$page` |  | 
`$client_id` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1605](class/class-mainwp-ui.php#L1605-L1663)



### `mainwp_widget_boxes_show_widgets`

*Method do_widget_boxes()*

Customize WordPress do_meta_boxes() function.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$page` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1605](class/class-mainwp-ui.php#L1605-L1670)



### `mainwp-widgets-screen-options`

*Method render_screen_options()*

Render modal window for Page Settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_widgets_screen_options'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2421](class/class-mainwp-ui.php#L2421-L2455)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2457](class/class-mainwp-ui.php#L2457-L2464)



### `mainwp_format_email`

*Method format_email()*

Format email.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mail_send` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-format.php](class/class-mainwp-format.php), [line 212](class/class-mainwp-format.php#L212-L579)



### `mainwp-sitestable-item`

*Filter is being replaced with mainwp_sitestable_item*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($item, $item)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_item'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 180](class/class-mainwp-manage-sites-list-table.php#L180-L185)



### `mainwp_sitestable_item`

*Filter: mainwp_sitestable_item*

Filters the Manage Sites table column items. Allows user to create new column item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item` | `array` | Array containing child site data.
`$column_name` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 187](class/class-mainwp-manage-sites-list-table.php#L187-L196)



### `mainwp-sitestable-getcolumns`

*Filter is being replaced with mainwp_sitestable_getcolumns*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($columns, $columns)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_getcolumns'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 322](class/class-mainwp-manage-sites-list-table.php#L322-L327)



### `mainwp_sitestable_getcolumns`

*Filter: mainwp_sitestable_getcolumns*

Filters the Manage Sites table columns. Allows user to create a new column.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$columns` | `array` | Array containing table columns.
`$columns` | `array` | Array containing table columns.

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 329](class/class-mainwp-manage-sites-list-table.php#L329-L338)



### `mainwp_sitestable_prepare_extra_view`

*Prepare the items to be listed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 694](class/class-mainwp-manage-sites-list-table.php#L694-L719)



### `mainwp_sitestable_display_row_columns`

*Get table rows.*

Optimize for shared hosting or big networks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1554](class/class-mainwp-manage-sites-list-table.php#L1554-L1722)



### `mainwp_sitestable_render_column`

*Columns for a single row.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` | `mixed` | Child Site.
`$classes` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1971](class/class-mainwp-manage-sites-list-table.php#L1971-L2166)



### `mainwp_open_hide_referrer`

*Filter: mainwp_open_hide_referrer*

Filters whether the MainWP should hide referrer when going to child site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-view.php](class/class-mainwp-system-view.php), [line 823](class/class-mainwp-system-view.php#L823-L830)



### `mainwp_is_enable_schedule_job`

*Method init_mainwp_cron()*

Schedual Cron Jobs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$useWPCron` | `mixed` | Wether or not to use WP_Cron.
`$cron_hook` | `mixed` | When cron is going to reoccur.
`$recurrence` | `mixed` | Cron job hook.

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 147](class/class-mainwp-system-cron-jobs.php#L147-L158)



### `mainwp_text_format_email`

*Filter: mainwp_text_format_email*

Filters whether the email shuld bein plain text format.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plain_text` |  | 

**Changelog**

Version | Description
------- | -----------
`3.5` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 629](class/class-mainwp-system-cron-jobs.php#L629-L636)



### `mainwp_license_deactivated_alert_plain_text`

*Method cron_deactivated_licenses_alert()*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plain_text` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 1356](class/class-mainwp-system-cron-jobs.php#L1356-L1377)



### `mainwp_register_regular_sequence_process`

*Method perform_sequence_process*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 1692](class/class-mainwp-system-cron-jobs.php#L1692-L1699)



### `mainwp_try_visit_follow_location`

*Method try visit.*

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 32](class/class-mainwp-connect.php#L32-L76)



### `mainwp_curl_curlopt_resolve`

*Method try visit.*

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`false` |  | 
`$url` | `string` | Child Site URL.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 32](class/class-mainwp-connect.php#L32-L106)



### `mainwp_fetch_urls_chunk_size`

*Method fetch_urls_authed()*

Fetches data from child sites if authenticated.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$chunkSize` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 688](class/class-mainwp-connect.php#L688-L719)



### `mainwp_init_primary_menu_items`

*Method init_mainwp_menu_items()*

Init MainWP menus.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$menus_items` | `array` | menus items.
`$part` | `string` | menus part.

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 332](class/class-mainwp-menu.php#L332-L345)



### `mainwp_is_disable_menu_item`

*Method is_disable_menu_item*

Check if $_mainwp_disable_menus_items contains any menu items to hide.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$disabled` |  | 
`$level` | `string` | The level the menu item is on.
`$item` | `array\|string` | The menu items meta data.

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 529](class/class-mainwp-menu.php#L529-L552)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 684](class/class-mainwp-menu.php#L684-L691)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 694](class/class-mainwp-menu.php#L694-L702)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 799](class/class-mainwp-menu.php#L799-L806)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 1242](class/class-mainwp-menu.php#L1242-L1249)



### `mainwp_get_template`

*Filter: mainwp_get_template*

Filters available templates and adds support for 3rd party templates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template` |  | 
`$template_name` | `string` | Template name.
`$args` | `array` | Args.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 140](class/class-mainwp-notification-template.php#L140-L150)



### `mainwp_locate_template`

*Filer: mainwp_locate_template*

Filters the template location.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template` |  | 
`$template_name` | `string` | Template name.
`$template_path` | `string` | Template path.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 265](class/class-mainwp-notification-template.php#L265-L275)



### `mainwp_get_notification_template_name_by_type`

*Get default template name by email/notification type.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | email/notification type.

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 293](class/class-mainwp-notification-template.php#L293-L309)



### `mainwp_default_template_source_dir`

*Method handle_template_file_action()*

Handle template file action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template_path` |  | 
`$templ_base_name` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 318](class/class-mainwp-notification-template.php#L318-L352)



### `mainwp_module_log_record_array`

*Filter allows modification of record information*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-db.php](modules/logs/classes/class-log-db.php), [line 59](modules/logs/classes/class-log-db.php#L59-L66)



### `mainwp_module_log_query_args`

*Filter allows additional arguments to query $args*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-db.php](modules/logs/classes/class-log-db.php), [line 162](modules/logs/classes/class-log-db.php#L162-L167)



### `mainwp_module_log_current_agent`

*Filter the current agent string*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$agent` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-author.php](modules/logs/classes/class-log-author.php), [line 241](modules/logs/classes/class-log-author.php#L241-L246)



### `mainwp_module_log_agent_label`

*Filter agent labels*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$label` |  | 
`$agent` | `string` | Key representing agent.

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-author.php](modules/logs/classes/class-log-author.php), [line 269](modules/logs/classes/class-log-author.php#L269-L276)



### `mainwp_module_log_connectors`

*Allows for adding additional connectors via classes that extend Connector.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$classes` | `array` | An array of Connector objects.
`$this->manager->log` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-connectors.php](modules/logs/classes/class-log-connectors.php), [line 97](modules/logs/classes/class-log-connectors.php#L97-L102)



### `mainwp_insights_getmetaboxes`

*Method add_meta_boxes()*

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 248](modules/logs/pages/page-log-insights-page.php#L248-L273)



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

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 284](modules/logs/pages/page-log-insights-page.php#L284-L294)



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

Source: [../sources/mainwp-dashboard/modules/logs/pages/page-log-insights-page.php](modules/logs/pages/page-log-insights-page.php), [line 1039](modules/logs/pages/page-log-insights-page.php#L1039-L1046)



### `mainwp_cost_summary_getmetaboxes`

*Method add_meta_boxes()*

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 195](modules/cost-tracker/classes/class-cost-tracker-summary.php#L195-L220)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 231](modules/cost-tracker/classes/class-cost-tracker-summary.php#L231-L241)



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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-summary.php](modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 497](modules/cost-tracker/classes/class-cost-tracker-summary.php#L497-L504)



### `mainwp_module_cost_tracker_upcoming_renewals_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Renewals', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 59](modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L59-L59)



### `mainwp_module_cost_tracker_yearly_renewals_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Yearly Renewals', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 59](modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L59-L59)



### `mainwp_module_cost_tracker_monthly_renewals_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Monthly Renewals', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 59](modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L59-L59)



### `mainwp_getmetaboxes`

*Method on_load_page_dashboard()*

Add individual meta boxes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 
`$dashboard_siteid` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 1401](pages/page-mainwp-manage-sites.php#L1401-L1436)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 1454](pages/page-mainwp-manage-sites.php#L1454-L1464)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-overview.php](pages/page-mainwp-overview.php), [line 230](pages/page-mainwp-overview.php#L230-L240)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1155](pages/page-mainwp-server-information.php#L1155-L1162)



### `mainwp_menu_extensions_left_menu`

*Method init_extensions_menu()*

Initiate left Extensions menus.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extensions_and_leftmenus` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-groups.php](pages/page-mainwp-extensions-groups.php), [line 33](pages/page-mainwp-extensions-groups.php#L33-L824)



### `mainwp_notes_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-notes.php](widgets/widget-mainwp-notes.php), [line 62](widgets/widget-mainwp-notes.php#L62-L62)



### `mainwp_widgets_chart_date_format`

*Prepare response time for ui chart data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$format_date` |  | 
`$params` | `array` | params.
`$slug` | `string` | for date format hook.

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-uptime-monitoring-site-widget.php](widgets/widget-mainwp-uptime-monitoring-site-widget.php), [line 615](widgets/widget-mainwp-uptime-monitoring-site-widget.php#L615-L634)



### `mainwp_get_started_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Get Started with MainWP', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-get-started.php](widgets/widget-mainwp-get-started.php), [line 63](widgets/widget-mainwp-get-started.php#L63-L63)



### `mainwp_non_mainwp_changes_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites Changes', 'mainwp')` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-actions.php](widgets/widget-mainwp-site-actions.php), [line 127](widgets/widget-mainwp-site-actions.php#L127-L127)




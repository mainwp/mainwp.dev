# Site Management Filters

Hooks related to adding, editing, removing, and managing sites and site groups.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_site_suspended`](#mainwp_site_suspended) - Fires immediately after website suspended/unsuspend.
- [`mainwp_site_suspended`](#mainwp_site_suspended) - Fires immediately after website suspended/unsuspend.
- [`mainwp_delete_site`](#mainwp_delete_site) - This action is documented in pages\page-mainwp-manage-sites-handler.php
- [`mainwp_after_notice_sites_uptime_monitoring_admin`](#mainwp_after_notice_sites_uptime_monitoring_admin) - Basic site uptime monitoring.
- [`mainwp_after_notice_sites_uptime_monitoring_individual`](#mainwp_after_notice_sites_uptime_monitoring_individual) - Basic site uptime monitoring.
- [`mainwp_manage_sites_table_columns_defs`](#mainwp_manage_sites_table_columns_defs) - Display the table.
- [`mainwp_site_tag_action`](#mainwp_site_tag_action) - Fires after a new sites tag has been created.
- [`mainwp_added_new_group`](#mainwp_added_new_group) - New Group Added
- [`mainwp_site_tag_action`](#mainwp_site_tag_action) - Fires after a tag has been deleted.
- [`mainwp_ga_delete_site`](#mainwp_ga_delete_site) - Action: mainwp_ga_delete_site
- [`mainwp_after_sync_site_success`](#mainwp_after_sync_site_success) - Fires immediately after website synced successfully.
- [`mainwp_site_suspended`](#mainwp_site_suspended) - Fires immediately after website suspended/unsuspend.
- [`mainwp_managesite_backup`](#mainwp_managesite_backup) - Method backup()
- [`mainwp_before_select_sites_filters`](#mainwp_before_select_sites_filters) - Action: mainwp_before_select_sites_filters
- [`mainwp_after_select_sites_filters`](#mainwp_after_select_sites_filters) - Action: mainwp_after_select_sites_filters
- [`mainwp_before_select_sites_list`](#mainwp_before_select_sites_list) - Action: mainwp_before_select_sites_list
- [`mainwp_after_select_sites_list`](#mainwp_after_select_sites_list) - Action: mainwp_after_select_sites_list
- [`mainwp_before_select_groups_list`](#mainwp_before_select_groups_list) - Action: mainwp_before_select_groups_list
- [`mainwp_after_select_groups_list`](#mainwp_after_select_groups_list) - Action: mainwp_after_select_groups_list
- [`mainwp_quick_sites_shortcut`](#mainwp_quick_sites_shortcut) - Action: mainwp_quick_sites_shortcut
- [`mainwp_before_header`](#mainwp_before_header) - Action: mainwp_before_header
- [`mainwp_after_header`](#mainwp_after_header) - Action: mainwp_after_header
- [`mainwp_managesites_tabletop`](#mainwp_managesites_tabletop) - Action: mainwp_managesites_tabletop
- [`mainwp_before_edit_site_note`](#mainwp_before_edit_site_note) - Action: mainwp_before_edit_site_note
- [`mainwp_after_edit_site_note`](#mainwp_after_edit_site_note) - Action: mainwp_after_edit_site_note
- [`mainwp-site-synced`](#mainwp-site-synced) - Method sync_information_array()
- [`mainwp_site_synced`](#mainwp_site_synced) - Action: mainwp_site_synced
- [`mainwp_site_sync`](#mainwp_site_sync) - Action: mainwp_site_sync
- [`mainwp_before_manage_sites_table`](#mainwp_before_manage_sites_table) - Action: mainwp_before_manage_sites_table
- [`mainwp_after_manage_sites_table`](#mainwp_after_manage_sites_table) - Action: mainwp_after_manage_sites_table
- [`mainwp_manage_sites_table_columns_defs`](#mainwp_manage_sites_table_columns_defs) - Display the table.
- [`mainwp_manage_sites_action`](#mainwp_manage_sites_action) - Action: mainwp_manage_sites_action
- [`mainwp_manage_sites_action`](#mainwp_manage_sites_action) - Action: mainwp_manage_sites_action
- [`mainwp_sync_popup_content`](#mainwp_sync_popup_content) - Method render_footer_content()
- [`mainwp_sync_popup_content`](#mainwp_sync_popup_content) - Method render_footer_content()
- [`mainwp_manage_sites_table_columns_defs`](#mainwp_manage_sites_table_columns_defs) - Display the table.
- [`mainwp_synced_all_sites`](#mainwp_synced_all_sites) - Method cron_updates_check()
- [`mainwp_daily_digest_action`](#mainwp_daily_digest_action) - Action: mainwp_daily_digest_action
- [`mainwp_website_before_updated`](#mainwp_website_before_updated) - Action: mainwp_website_before_updated
- [`mainwp_fetch_url_authed`](#mainwp_fetch_url_authed) - Fires immediately after fetch url action.
- [`mainwp_website_updated`](#mainwp_website_updated) - Action: mainwp_website_updated
- [`mainwp-wordfence-sites`](#mainwp-wordfence-sites) - Method render_scan_site()
- [`mainwp_wordfence_sites`](#mainwp_wordfence_sites) - Action: mainwp_wordfence_sites
- [`mainwp-manage-sites-edit`](#mainwp-manage-sites-edit) - Method render_edit_site()
- [`mainwp-extension-sites-edit`](#mainwp-extension-sites-edit) - Method render_edit_site()
- [`mainwp_manage_sites_edit`](#mainwp_manage_sites_edit) - This action is documented in ../pages/page-mainwp-manage-sites.php
- [`mainwp_extension_sites_edit_tablerow`](#mainwp_extension_sites_edit_tablerow) - Method render_edit_site()
- [`mainwp_manage_sites_email_settings`](#mainwp_manage_sites_email_settings) - Action: mainwp_manage_sites_email_settings
- [`mainwp_site_reconnected`](#mainwp_site_reconnected) - Fires immediately after reconnect website.
- [`mainwp_site_added`](#mainwp_site_added) - Fires immediately after a new website is added.
- [`mainwp_added_new_site`](#mainwp_added_new_site) - New site added
- [`mainwp_synced_all_sites`](#mainwp_synced_all_sites) - Action: mainwp_synced_all_sites
- [`mainwp_site_health_monitoring_email_header`](#mainwp_site_health_monitoring_email_header) - Site Health Monitoring Email Header
- [`mainwp_site_health_monitoring_email_footer`](#mainwp_site_health_monitoring_email_footer) - Site Health Monitoring Email Footer
- [`mainwp_delete_key_file`](#mainwp_delete_key_file) - Method update_compatible_site_api_key
- [`mainwp_ajax_add_action`](#mainwp_ajax_add_action) - Init ajax actions.
- [`mainwp_sync_site_log_install_actions`](#mainwp_sync_site_log_install_actions) - Method sync_log_site_actions().
- [`mainwp_select_sites_box`](#mainwp_select_sites_box) - Render settings
- [`mainwp_check_site_result`](#mainwp_check_site_result) - Method check_site()
- [`mainwp_delete_site`](#mainwp_delete_site) - *Arguments*
- [`mainwp_site_deleted`](#mainwp_site_deleted) - *Arguments*
- [`mainwp-manage-sites-edit`](#mainwp-manage-sites-edit) - Method render_new_site_add_new_site()
- [`mainwp_manage_sites_edit`](#mainwp_manage_sites_edit) - Edit site
- [`mainwp_site_updated`](#mainwp_site_updated) - Update site
- [`mainwp_site_suspended`](#mainwp_site_suspended) - Site suspended changed.
- [`mainwp_managesite_schedule_backup`](#mainwp_managesite_schedule_backup) - Execute the backup task.
- [`mainwp_before_groups_table`](#mainwp_before_groups_table) - Action: mainwp_before_groups_table
- [`mainwp_after_groups_table`](#mainwp_after_groups_table) - Action: mainwp_after_groups_table
- [`mainwp_site_tag_action`](#mainwp_site_tag_action) - Fires after a new sites tag has been created.
- [`mainwp_added_new_group`](#mainwp_added_new_group) - New Group Added
- [`mainwp_added_new_group`](#mainwp_added_new_group) - New Group Added
- [`mainwp_tags_help_item`](#mainwp_tags_help_item) - Action: mainwp_tags_help_item
- [`mainwp_updates_pergroup_before_wp_updates`](#mainwp_updates_pergroup_before_wp_updates) - Action: mainwp_updates_pergroup_before_wp_updates
- [`mainwp_updates_pergroup_after_wp_updates`](#mainwp_updates_pergroup_after_wp_updates) - Action: mainwp_updates_pergroup_after_wp_updates
- [`mainwp_updates_pergroup_before_wp_updates`](#mainwp_updates_pergroup_before_wp_updates) - Action: mainwp_updates_persite_before_wp_updates
- [`mainwp_updates_persite_after_wp_updates`](#mainwp_updates_persite_after_wp_updates) - Action: mainwp_updates_persite_after_wp_updates
- [`mainwp_updates_persite_before_plugin_updates`](#mainwp_updates_persite_before_plugin_updates) - Action: mainwp_updates_persite_before_plugin_updates
- [`mainwp_updates_persite_after_plugin_updates`](#mainwp_updates_persite_after_plugin_updates) - Action: mainwp_updates_persite_after_plugin_updates
- [`mainwp_updates_pergroup_before_plugin_updates`](#mainwp_updates_pergroup_before_plugin_updates) - Action: mainwp_updates_pergroup_before_plugin_updates
- [`mainwp_updates_pergroup_after_plugin_updates`](#mainwp_updates_pergroup_after_plugin_updates) - Action: mainwp_updates_pergroup_after_plugin_updates
- [`mainwp_updates_persite_before_theme_updates`](#mainwp_updates_persite_before_theme_updates) - Action: mainwp_updates_persite_before_theme_updates
- [`mainwp_updates_persite_after_theme_updates`](#mainwp_updates_persite_after_theme_updates) - Action: mainwp_updates_persite_after_theme_updates
- [`mainwp_updates_pergroup_before_theme_updates`](#mainwp_updates_pergroup_before_theme_updates) - Action: mainwp_updates_pergroup_before_theme_updates
- [`mainwp_updates_pergroup_after_theme_updates`](#mainwp_updates_pergroup_after_theme_updates) - Action: mainwp_updates_pergroup_after_theme_updates
- [`mainwp_updates_persite_before_translation_updates`](#mainwp_updates_persite_before_translation_updates) - Action: mainwp_updates_persite_before_translation_updates
- [`mainwp_updates_persite_after_translation_updates`](#mainwp_updates_persite_after_translation_updates) - Action: mainwp_updates_persite_after_translation_updates
- [`mainwp_updates_pergroup_before_translation_updates`](#mainwp_updates_pergroup_before_translation_updates) - Action: mainwp_updates_pergroup_before_translation_updates
- [`mainwp_updates_pergroup_after_translation_updates`](#mainwp_updates_pergroup_after_translation_updates) - Action: mainwp_updates_pergroup_after_translation_updates
- [`mainwp_updates_persite_before_abandoned_plugins`](#mainwp_updates_persite_before_abandoned_plugins) - Action: mainwp_updates_persite_before_abandoned_plugins
- [`mainwp_updates_persite_after_abandoned_plugins`](#mainwp_updates_persite_after_abandoned_plugins) - Action: mainwp_updates_persite_after_abandoned_plugins
- [`mainwp_updates_pergroup_before_abandoned_plugins`](#mainwp_updates_pergroup_before_abandoned_plugins) - Action: mainwp_updates_pergroup_before_abandoned_plugins
- [`mainwp_updates_pergroup_after_abandoned_plugins`](#mainwp_updates_pergroup_after_abandoned_plugins) - Action: mainwp_updates_pergroup_after_abandoned_plugins
- [`mainwp_updates_persite_before_abandoned_themes`](#mainwp_updates_persite_before_abandoned_themes) - Action: mainwp_updates_persite_before_abandoned_themes
- [`mainwp_updates_persite_after_abandoned_themes`](#mainwp_updates_persite_after_abandoned_themes) - Action: mainwp_updates_persite_after_abandoned_themes
- [`mainwp_updates_pergroup_before_abandoned_themes`](#mainwp_updates_pergroup_before_abandoned_themes) - Action: mainwp_updates_pergroup_before_abandoned_themes
- [`mainwp_updates_pergroup_after_abandoned_themes`](#mainwp_updates_pergroup_after_abandoned_themes) - Action: mainwp_updates_pergroup_after_abandoned_themes
- [`mainwp_added_new_site`](#mainwp_added_new_site) - This action is documented in class\class-mainwp-manage-sites-view.php
- [`mainwp_delete_site`](#mainwp_delete_site) - This action is documented in pages\page-mainwp-manage-sites-handler.php
- [`mainwp_added_new_group`](#mainwp_added_new_group) - This action is documented in pages\page-mainwp-manage-groups.php
- [`mainwp_site_info_widget_top`](#mainwp_site_info_widget_top) - Actoin: mainwp_site_info_widget_top
- [`mainwp_site_info_table_top`](#mainwp_site_info_table_top) - Action: mainwp_site_info_table_top
- [`mainwp_site_info_table_bottom`](#mainwp_site_info_table_bottom) - Action: mainwp_site_info_table_bottom
- [`mainwp_site_info_widget_bottom`](#mainwp_site_info_widget_bottom) - Action: mainwp_site_info_widget_bottom
- [`mainwp_connection_status_widget_bottom`](#mainwp_connection_status_widget_bottom) - Action: mainwp_connection_status_widget_bottom
- [`mainwp_connection_status_widget_top`](#mainwp_connection_status_widget_top) - Action: mainwp_connection_status_widget_top
- [`mainwp_connection_status_before_all_sites_list`](#mainwp_connection_status_before_all_sites_list) - Action: mainwp_connection_status_before_all_sites_list
- [`mainwp_connection_status_after_all_sites_list`](#mainwp_connection_status_after_all_sites_list) - Action: mainwp_connection_status_after_all_sites_list
- [`mainwp_connection_status_before_connected_sites_list`](#mainwp_connection_status_before_connected_sites_list) - Action: mainwp_connection_status_before_connected_sites_list
- [`mainwp_connection_status_after_connected_sites_list`](#mainwp_connection_status_after_connected_sites_list) - Action: mainwp_connection_status_after_connected_sites_list
- [`mainwp_connection_status_before_disconnected_sites_list`](#mainwp_connection_status_before_disconnected_sites_list) - Action: mainwp_connection_status_before_disconnected_sites_list
- [`mainwp_connection_status_after_disconnected_sites_list`](#mainwp_connection_status_after_disconnected_sites_list) - Action: mainwp_connection_status_after_disconnected_sites_list
- [`mainwp_connection_status_widget_footer_left`](#mainwp_connection_status_widget_footer_left) - Action: mainwp_connection_status_widget_footer_left
- [`mainwp_connection_status_widget_footer_right`](#mainwp_connection_status_widget_footer_right) - Action: mainwp_connection_status_widget_footer_right
- [`mainwp_clients_overview_websites_widget_top`](#mainwp_clients_overview_websites_widget_top) - Actoin: mainwp_clients_overview_websites_widget_top
- [`mainwp_clients_overview_websites_widget_bottom`](#mainwp_clients_overview_websites_widget_bottom) - Action: mainwp_clients_overview_websites_widget_bottom
- [`mainwp_widget_site_actions_limit_number`](#mainwp_widget_site_actions_limit_number) - Method mainwp_rest_api_non_mainwp_changes_callback()
- [`mainwp_widget_site_actions_limit_number`](#mainwp_widget_site_actions_limit_number) - Method mainwp_rest_api_non_mainwp_changes_count_callback()
- [`mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context) - Get sites by tag id.
- [`mainwp_rest_pre_insert_site_item`](#mainwp_rest_pre_insert_site_item) - Filters an object before it is inserted via the REST API.
- [`mainwp_rest_pre_update_site_item`](#mainwp_rest_pre_update_site_item) - Filters an object before it is inserted via the REST API.
- [`mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context) - *Arguments*
- [`mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context) - Update all items of site.
- [`mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context) - Get sites of client.
- [`mainwp_cron_bulk_update_sites_limit`](#mainwp_cron_bulk_update_sites_limit) - Method handle_cron_batch_updates()
- [`mainwp_currentuserallowedaccessgroups`](#mainwp_currentuserallowedaccessgroups) - Filter: mainwp_currentuserallowedaccessgroups
- [`mainwp_boilerplate_get_tokens`](#mainwp_boilerplate_get_tokens) - Filter: mainwp_boilerplate_get_tokens
- [`mainwp_pro_reports_get_site_tokens`](#mainwp_pro_reports_get_site_tokens) - Filter: mainwp_pro_reports_get_site_tokens
- [`mainwp_client_report_get_site_tokens`](#mainwp_client_report_get_site_tokens) - Filter: mainwp_client_report_get_site_tokens
- [`mainwp_boilerplate_get_tokens`](#mainwp_boilerplate_get_tokens) - This filter is documented in ../class/class-mainwp-notification-settings.php
- [`mainwp_pro_reports_get_site_tokens`](#mainwp_pro_reports_get_site_tokens) - This filter is documented in ../class/class-mainwp-notification-settings.php
- [`mainwp_client_report_get_site_tokens`](#mainwp_client_report_get_site_tokens) - This filter is documented in ../class/class-mainwp-notification-settings.php
- [`mainwp_connect_sign_algo`](#mainwp_connect_sign_algo) - Method get_connect_sign_algorithm().
- [`mainwp_staging_current_user_sites_view`](#mainwp_staging_current_user_sites_view) - Method get_select_staging_view_sites()
- [`mainwp_html_regression_largest_change_scope`](#mainwp_html_regression_largest_change_scope) - Method mainwp_upgrade_plugintheme()
- [`mainwp_log_to_db_priority`](#mainwp_log_to_db_priority) - Method log_to_db()
- [`mainwp_log_do_to_db`](#mainwp_log_do_to_db) - Method log_to_db()
- [`mainwp_logger_to_db`](#mainwp_logger_to_db) - Method log()
- [`mainwp_curl_curlopt_resolve`](#mainwp_curl_curlopt_resolve) - Fetch uptime urls.
- [`mainwp_connect_sites_not_allow_ports`](#mainwp_connect_sites_not_allow_ports) - Method mainwp_testwp()
- [`mainwp_connect_sites_allow_ports`](#mainwp_connect_sites_allow_ports) - Method mainwp_testwp()
- [`mainwp_manage_sites_force_use_ipv4`](#mainwp_manage_sites_force_use_ipv4) - Method mainwp_testwp()
- [`mainwp_postprocess_backup_sites_feedback`](#mainwp_postprocess_backup_sites_feedback) - Method  backup_site()
- [`mainwp_clone_enabled`](#mainwp_clone_enabled) - Filter: mainwp_clone_enabled
- [`mainwp-sync-others-data`](#mainwp-sync-others-data) - Method sync_site()
- [`mainwp_sync_others_data`](#mainwp_sync_others_data) - Filter: mainwp_sync_others_data
- [`mainwp_site_actions_saved_days_number`](#mainwp_site_actions_saved_days_number) - Method sync_site()
- [`mainwp_before_save_sync_result`](#mainwp_before_save_sync_result) - Filter: mainwp_before_save_sync_result
- [`mainwp_sync_site_after_sync_result`](#mainwp_sync_site_after_sync_result) - Method sync_information_array()
- [`mainwp_managesites_getbackuplink`](#mainwp_managesites_getbackuplink) - Filter: mainwp_managesites_getbackuplink
- [`mainwp_managesites_bulk_actions`](#mainwp_managesites_bulk_actions) - Filter: mainwp_managesites_bulk_actions
- [`mainwp_sites_table_features`](#mainwp_sites_table_features) - Filter: mainwp_sites_table_features
- [`mainwp_sitestable_website`](#mainwp_sitestable_website) - Get table rows.
- [`mainwp_sitestable_website`](#mainwp_sitestable_website) - Columns for a single row.
- [`mainwp_monitoringsites_bulk_actions`](#mainwp_monitoringsites_bulk_actions) - Filter: mainwp_monitoringsites_bulk_actions
- [`mainwp_updatescheck_sendmail_for_each_auto_sync_finished`](#mainwp_updatescheck_sendmail_for_each_auto_sync_finished) - Method cron_updates_check()
- [`mainwp_pre_fetch_authed_data`](#mainwp_pre_fetch_authed_data) - Method get_post_data_authed()
- [`mainwp_open_site_login_required_params`](#mainwp_open_site_login_required_params) - Method get_get_data_authed()
- [`mainwp_curl_curlopt_resolve`](#mainwp_curl_curlopt_resolve) - Method fetch_urls_authed()
- [`mainwp_curl_curlopt_resolve`](#mainwp_curl_curlopt_resolve) - Method fetch_url_site()
- [`mainwp_manage_sites_navigation_items`](#mainwp_manage_sites_navigation_items) - Method render_managesites_header()
- [`mainwp-sync-extensions-options`](#mainwp-sync-extensions-options) - Method render_sync_exts_settings()
- [`mainwp_sync_extensions_options`](#mainwp_sync_extensions_options) - Method render_sync_exts_settings()
- [`mainwp_default_template_locate`](#mainwp_default_template_locate) - Render the email notification edit form.
- [`mainwp_manage_sites_force_use_ipv4`](#mainwp_manage_sites_force_use_ipv4) - Method add_site()
- [`mainwp_clients_website_client_tokens`](#mainwp_clients_website_client_tokens) - Method get_website_client_tokens_data()
- [`mainwp_cron_bulk_update_sites_limit`](#mainwp_cron_bulk_update_sites_limit) - Method handle_cron_auto_updates()
- [`mainwp_getwebsite_by_id`](#mainwp_getwebsite_by_id) - Get sites by website ID.
- [`mainwp_updatewebsiteoptions`](#mainwp_updatewebsiteoptions) - Method update_website_option().
- [`mainwp_getwebsiteoptions`](#mainwp_getwebsiteoptions) - Method get_website_options().
- [`mainwp_db_fetch_object`](#mainwp_db_fetch_object) - Method fetch_object().
- [`mainwp_db_free_result`](#mainwp_db_free_result) - Method free_result().
- [`mainwp_module_log_data`](#mainwp_module_log_data) - Log handler
- [`mainwp_module_log_cron_tracking`](#mainwp_module_log_cron_tracking) - Log handler.
- [`mainwp_rest_routes_sites_controller_get_allowed_fields_by_context`](#mainwp_rest_routes_sites_controller_get_allowed_fields_by_context) - *Arguments*
- [`mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context) - Get sites by item.
- [`mainwp_manage_sites_force_use_ipv4`](#mainwp_manage_sites_force_use_ipv4) - Method check_site()
- [`mainwp_posting_selected_groups`](#mainwp_posting_selected_groups) - Method posting_posts()
- [`mainwp_custom_post_types_get_post_connections`](#mainwp_custom_post_types_get_post_connections) - Method posts_search_handler()
- [`mainwp_bulkpost_select_sites_settings`](#mainwp_bulkpost_select_sites_settings) - Renders bulkpost to edit.
- [`mainwp_manage_sites_optimize_loading`](#mainwp_manage_sites_optimize_loading) - Method render_all_sites()
- [`mainwp_open_site_allow_vars`](#mainwp_open_site_allow_vars) - Child Site Dashboard Link redirect handler.
- [`mainwp_html_regression_largest_change_scope`](#mainwp_html_regression_largest_change_scope) - *Arguments*
- [`mainwp_manage_sites_optimize_loading`](#mainwp_manage_sites_optimize_loading) - Method render_all_sites()
- [`mainwp_child_site_info_widget_content`](#mainwp_child_site_info_widget_content) - Filter: mainwp_child_site_info_widget_content
- [`mainwp_site_info_widget_title`](#mainwp_site_info_widget_title) - *Arguments*
- [`mainwp_connection_status_widget_title`](#mainwp_connection_status_widget_title) - *Arguments*
- [`mainwp_connection_status_list_item_title_url`](#mainwp_connection_status_list_item_title_url) - *Arguments*
- [`mainwp_connection_status_list_item_title`](#mainwp_connection_status_list_item_title) - *Arguments*
- [`mainwp_connection_status_list_item_title_url`](#mainwp_connection_status_list_item_title_url) - *Arguments*
- [`mainwp_connection_status_list_item_title`](#mainwp_connection_status_list_item_title) - *Arguments*
- [`mainwp_connection_status_list_item_title_url`](#mainwp_connection_status_list_item_title_url) - *Arguments*
- [`mainwp_connection_status_list_item_title`](#mainwp_connection_status_list_item_title) - *Arguments*
- [`mainwp_clients_overview_websites_widget_title`](#mainwp_clients_overview_websites_widget_title) - *Arguments*
- [`mainwp_widget_site_actions_limit_number`](#mainwp_widget_site_actions_limit_number) - Method render()

## Hook Details

### `mainwp_site_suspended`

*Fires immediately after website suspended/unsuspend.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$suspended` | `int` | The new suspended value.

**Changelog**

Version | Description
------- | -----------
`4.5.2` | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 1444](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L1444-L1452)



### `mainwp_site_suspended`

*Fires immediately after website suspended/unsuspend.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$suspended` | `int` | The new suspended value.

**Changelog**

Version | Description
------- | -----------
`4.5.2` | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 1484](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L1484-L1492)



### `mainwp_delete_site`

*This action is documented in pages\page-mainwp-manage-sites-handler.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-hooks.php](class/class-mainwp-hooks.php), [line 405](class/class-mainwp-hooks.php#L405-L406)



### `mainwp_after_notice_sites_uptime_monitoring_admin`

*Basic site uptime monitoring.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the websites.

Source: [../sources/mainwp-dashboard/class/class-mainwp-monitoring-handler.php](class/class-mainwp-monitoring-handler.php), [line 151](class/class-mainwp-monitoring-handler.php#L151-L182)



### `mainwp_after_notice_sites_uptime_monitoring_individual`

*Basic site uptime monitoring.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-monitoring-handler.php](class/class-mainwp-monitoring-handler.php), [line 151](class/class-mainwp-monitoring-handler.php#L151-L220)



### `mainwp_manage_sites_table_columns_defs`

*Display the table.*


Source: [../sources/mainwp-dashboard/class/class-mainwp-client-list-table.php](class/class-mainwp-client-list-table.php), [line 336](class/class-mainwp-client-list-table.php#L336-L468)



### `mainwp_site_tag_action`

*Fires after a new sites tag has been created.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$group` | `object` | group created.
`'created'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-db-common.php](class/class-mainwp-db-common.php), [line 585](class/class-mainwp-db-common.php#L585-L591)



### `mainwp_added_new_group`

*New Group Added*

Fires after a new sites group has been created.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groupId` | `int` | Group ID.

Source: [../sources/mainwp-dashboard/class/class-mainwp-db-common.php](class/class-mainwp-db-common.php), [line 634](class/class-mainwp-db-common.php#L634-L641)



### `mainwp_site_tag_action`

*Fires after a tag has been deleted.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$group` | `object` | group created.
`'deleted'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-db-common.php](class/class-mainwp-db-common.php), [line 664](class/class-mainwp-db-common.php#L664-L670)



### `mainwp_ga_delete_site`

*Action: mainwp_ga_delete_site*

Fires upon site removal process in order to delete Google Analytics data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websiteid` | `int` | Child site ID.

Source: [../sources/mainwp-dashboard/class/class-mainwp-db.php](class/class-mainwp-db.php), [line 2611](class/class-mainwp-db.php#L2611-L2620)



### `mainwp_after_sync_site_success`

*Fires immediately after website synced successfully.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-site-handler.php](class/class-mainwp-post-site-handler.php), [line 407](class/class-mainwp-post-site-handler.php#L407-L414)



### `mainwp_site_suspended`

*Fires immediately after website suspended/unsuspend.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$suspended` | `int` | The new suspended value.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-site-handler.php](class/class-mainwp-post-site-handler.php), [line 470](class/class-mainwp-post-site-handler.php#L470-L478)



### `mainwp_managesite_backup`

*Method backup()*

Backup Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`array('type' => $pType)` |  | 
`$information` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-backup-handler.php](class/class-mainwp-backup-handler.php), [line 753](class/class-mainwp-backup-handler.php#L753-L937)



### `mainwp_before_select_sites_filters`

*Action: mainwp_before_select_sites_filters*

Fires before the Select Sites box filters.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 190](class/class-mainwp-ui.php#L190-L197)



### `mainwp_after_select_sites_filters`

*Action: mainwp_after_select_sites_filters*

Fires after the Select Sites box filters.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 206](class/class-mainwp-ui.php#L206-L213)



### `mainwp_before_select_sites_list`

*Action: mainwp_before_select_sites_list*

Fires before the Select Sites list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 252](class/class-mainwp-ui.php#L252-L261)



### `mainwp_after_select_sites_list`

*Action: mainwp_after_select_sites_list*

Fires after the Select Sites list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 330](class/class-mainwp-ui.php#L330-L339)



### `mainwp_before_select_groups_list`

*Action: mainwp_before_select_groups_list*

Fires before the Select Groups list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groups` | `object` | Object containing groups info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 419](class/class-mainwp-ui.php#L419-L428)



### `mainwp_after_select_groups_list`

*Action: mainwp_after_select_groups_list*

Fires after the Select Groups list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groups` | `object` | Object containing groups info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 458](class/class-mainwp-ui.php#L458-L467)



### `mainwp_quick_sites_shortcut`

*Action: mainwp_quick_sites_shortcut*

Adds a new shortcut item in the Quick Sites Shortcuts sidebar menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `array` | Array containing the child site data.<br><br>Suggested HTML markup:<br><br><a class="item" href="your custom URL"><br>  <i class="your custom icon"></i><br>  Your custom label  text<br></a>

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 738](class/class-mainwp-ui.php#L738-L754)



### `mainwp_before_header`

*Action: mainwp_before_header*

Fires before the MainWP header element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 866](class/class-mainwp-ui.php#L866-L875)



### `mainwp_after_header`

*Action: mainwp_after_header*

Fires after the MainWP header element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1072](class/class-mainwp-ui.php#L1072-L1081)



### `mainwp_managesites_tabletop`

*Action: mainwp_managesites_tabletop*

Fires at the table top on the Manage Sites and Monitoring page.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1176](class/class-mainwp-ui.php#L1176-L1183)



### `mainwp_before_edit_site_note`

*Action: mainwp_before_edit_site_note*

Fires before the site note content in the Edit Note modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2033](class/class-mainwp-ui.php#L2033-L2040)



### `mainwp_after_edit_site_note`

*Action: mainwp_after_edit_site_note*

Fires after the site note content in the Edit Note modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2051](class/class-mainwp-ui.php#L2051-L2058)



### `mainwp-site-synced`

*Method sync_information_array()*

Grab all Child Site Information.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($pWebsite, $information)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_site_synced'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 221](class/class-mainwp-sync.php#L221-L579)



### `mainwp_site_synced`

*Action: mainwp_site_synced*

Fires upon successful site synchronization.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pWebsite` | `object` | Object containing child site info.
`$information` | `array` | Array containing information returned from child site.

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 581](class/class-mainwp-sync.php#L581-L591)



### `mainwp_site_sync`

*Action: mainwp_site_sync*

Fires upon successful site synchronization.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pWebsite` | `object` | Object containing child site info.
`$information` | `array` | Array containing information returned from child site.
`$act_success` | `bool` | action success or failed.
`$_error` |  | 
`$post_data` | `array` | Addition post data.

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 596](class/class-mainwp-sync.php#L596-L609)



### `mainwp_before_manage_sites_table`

*Action: mainwp_before_manage_sites_table*

Fires before the Manage Sites table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1073](class/class-mainwp-manage-sites-list-table.php#L1073-L1080)



### `mainwp_after_manage_sites_table`

*Action: mainwp_after_manage_sites_table*

Fires after the Manage Sites table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1106](class/class-mainwp-manage-sites-list-table.php#L1106-L1113)



### `mainwp_manage_sites_table_columns_defs`

*Display the table.*


Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1044](class/class-mainwp-manage-sites-list-table.php#L1044-L1204)



### `mainwp_manage_sites_action`

*Action: mainwp_manage_sites_action*

Adds custom manage sites action item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `array` | Array containing website data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1876](class/class-mainwp-manage-sites-list-table.php#L1876-L1885)



### `mainwp_manage_sites_action`

*Action: mainwp_manage_sites_action*

Adds custom manage sites action item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `array` | Array containing website data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 2288](class/class-mainwp-manage-sites-list-table.php#L2288-L2297)



### `mainwp_sync_popup_content`

*Method render_footer_content()*

Render footer content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-view.php](class/class-mainwp-system-view.php), [line 996](class/class-mainwp-system-view.php#L996-L1054)



### `mainwp_sync_popup_content`

*Method render_footer_content()*

Render footer content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-view.php](class/class-mainwp-system-view.php), [line 996](class/class-mainwp-system-view.php#L996-L1071)



### `mainwp_manage_sites_table_columns_defs`

*Display the table.*


Source: [../sources/mainwp-dashboard/class/class-mainwp-monitoring-sites-list-table.php](class/class-mainwp-monitoring-sites-list-table.php), [line 644](class/class-mainwp-monitoring-sites-list-table.php#L644-L917)



### `mainwp_synced_all_sites`

*Method cron_updates_check()*

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.


Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 375](class/class-mainwp-system-cron-jobs.php#L375-L664)



### `mainwp_daily_digest_action`

*Action: mainwp_daily_digest_action*

Hooks the daily digest email notification send process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object conaining child site info.
`$plain_text` | `bool` | Whether plain text email should be sent.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 1038](class/class-mainwp-system-cron-jobs.php#L1038-L1048)



### `mainwp_website_before_updated`

*Action: mainwp_website_before_updated*

Fires before the child site update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.
`$type` | `string` | Type parameter.
`$list` | `string` | List parameter.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1175](class/class-mainwp-connect.php#L1175-L1186)



### `mainwp_fetch_url_authed`

*Fires immediately after fetch url action.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website.
`$information` | `array` | information result data.
`$what` | `string` | action.
`$params` | `array` | params input array.
`$others` | `array` | others input array.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1201](class/class-mainwp-connect.php#L1201-L1212)



### `mainwp_website_updated`

*Action: mainwp_website_updated*

Fires after the child site update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.
`$type` | `string` | Type parameter.
`$list` | `string` | List parameter.
`$information` | `array` | Array containing the information fetched from the child site.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1224](class/class-mainwp-connect.php#L1224-L1236)



### `mainwp-wordfence-sites`

*Method render_scan_site()*

Render Site Hardening sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_wordfence_sites'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 733](class/class-mainwp-manage-sites-view.php#L733-L813)



### `mainwp_wordfence_sites`

*Action: mainwp_wordfence_sites*

Fires on a child site Hardening page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 815](class/class-mainwp-manage-sites-view.php#L815-L826)



### `mainwp-manage-sites-edit`

*Method render_edit_site()*

Render individual Child Site Edit sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_manage_sites_edit'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 834](class/class-mainwp-manage-sites-view.php#L834-L1390)



### `mainwp-extension-sites-edit`

*Method render_edit_site()*

Render individual Child Site Edit sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_manage_sites_edit'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 834](class/class-mainwp-manage-sites-view.php#L834-L1391)



### `mainwp_manage_sites_edit`

*This action is documented in ../pages/page-mainwp-manage-sites.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 1393](class/class-mainwp-manage-sites-view.php#L1393-L1394)



### `mainwp_extension_sites_edit_tablerow`

*Method render_edit_site()*

Render individual Child Site Edit sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 834](class/class-mainwp-manage-sites-view.php#L834-L1395)



### `mainwp_manage_sites_email_settings`

*Action: mainwp_manage_sites_email_settings*

Fires on the Email Settigns page at bottom.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the website info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 1826](class/class-mainwp-manage-sites-view.php#L1826-L1835)



### `mainwp_site_reconnected`

*Fires immediately after reconnect website.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$success` |  | 
`$_error` |  | 

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 1997](class/class-mainwp-manage-sites-view.php#L1997-L2004)



### `mainwp_site_added`

*Fires immediately after a new website is added.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$information` | `array` | The array of information data .

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 2259](class/class-mainwp-manage-sites-view.php#L2259-L2267)



### `mainwp_added_new_site`

*New site added*

Fires after adding a website to MainWP Dashboard.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$id` | `int` | Child site ID.
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 2269](class/class-mainwp-manage-sites-view.php#L2269-L2278)



### `mainwp_synced_all_sites`

*Action: mainwp_synced_all_sites*

Fires upon successfull synchronization process.


**Changelog**

Version | Description
------- | -----------
`3.5.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-handler.php](class/class-mainwp-post-handler.php), [line 605](class/class-mainwp-post-handler.php#L605-L612)



### `mainwp_site_health_monitoring_email_header`

*Site Health Monitoring Email Header*

Fires at the top of the site health monitoring email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/templates/emails/mainwp-site-health-monitoring-email.php](templates/emails/mainwp-site-health-monitoring-email.php), [line 31](templates/emails/mainwp-site-health-monitoring-email.php#L31-L38)



### `mainwp_site_health_monitoring_email_footer`

*Site Health Monitoring Email Footer*

Fires at the bottom of the site health monitoring email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/templates/emails/mainwp-site-health-monitoring-email.php](templates/emails/mainwp-site-health-monitoring-email.php), [line 118](templates/emails/mainwp-site-health-monitoring-email.php#L118-L125)



### `mainwp_delete_key_file`

*Method update_compatible_site_api_key*

Encrypt data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key_file` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-utility.php](modules/api-backups/classes/class-api-backups-utility.php), [line 607](modules/api-backups/classes/class-api-backups-utility.php#L607-L643)



### `mainwp_ajax_add_action`

*Init ajax actions.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'mainwp_api_backups_selected_websites'` |  | 
`array(&$this, 'ajax_backups_selected_websites')` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-handler.php](modules/api-backups/classes/class-api-backups-handler.php), [line 53](modules/api-backups/classes/class-api-backups-handler.php#L53-L58)



### `mainwp_sync_site_log_install_actions`

*Method sync_log_site_actions().*

Sync site actions data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$record_mapping` |  | 
`$object_id` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-manager.php](modules/logs/classes/class-log-manager.php), [line 239](modules/logs/classes/class-log-manager.php#L239-L329)



### `mainwp_select_sites_box`

*Render settings*

Renders the extension settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`'checkbox'` |  | 
`true` |  | 
`true` |  | 
`''` |  | 
`''` |  | 
`$sel_sites` |  | 
`$sel_groups` |  | 
`true` |  | 
`$sel_clients` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/pages/page-cost-tracker-add-edit.php](modules/cost-tracker/pages/page-cost-tracker-add-edit.php), [line 85](modules/cost-tracker/pages/page-cost-tracker-add-edit.php#L85-L507)



### `mainwp_check_site_result`

*Method check_site()*

Check to add site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$_POST` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites-handler.php](pages/page-mainwp-manage-sites-handler.php), [line 26](pages/page-mainwp-manage-sites-handler.php#L26-L93)



### `mainwp_delete_site`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites-handler.php](pages/page-mainwp-manage-sites-handler.php), [line 453](pages/page-mainwp-manage-sites-handler.php#L453-L453)



### `mainwp_site_deleted`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites-handler.php](pages/page-mainwp-manage-sites-handler.php), [line 462](pages/page-mainwp-manage-sites-handler.php#L462-L462)



### `mainwp-manage-sites-edit`

*Method render_new_site_add_new_site()*

Render page managesites add new site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_manage_sites_edit'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 787](pages/page-mainwp-manage-sites.php#L787-L1054)



### `mainwp_manage_sites_edit`

*Edit site*

Fires on the Edit child site page and allows user to hook in new site options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 1056](pages/page-mainwp-manage-sites.php#L1056-L1063)



### `mainwp_site_updated`

*Update site*

Fires after updating a website settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `int` | Child site Ọbject.
`$_POST` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 2071](pages/page-mainwp-manage-sites.php#L2071-L2080)



### `mainwp_site_suspended`

*Site suspended changed.*

Fires after suspended a website changed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `int` | ->id Child site ID.
`$suspended` |  | 

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 2083](pages/page-mainwp-manage-sites.php#L2083-L2092)



### `mainwp_managesite_schedule_backup`

*Execute the backup task.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`array('type' => $task->type)` |  | 
`$_backup_result` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-backups-handler.php](pages/page-mainwp-manage-backups-handler.php), [line 282](pages/page-mainwp-manage-backups-handler.php#L282-L422)



### `mainwp_before_groups_table`

*Action: mainwp_before_groups_table*

Fires before the Manage Groups table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 315](pages/page-mainwp-manage-groups.php#L315-L322)



### `mainwp_after_groups_table`

*Action: mainwp_after_groups_table*

Fires after the Manage Groups table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 463](pages/page-mainwp-manage-groups.php#L463-L470)



### `mainwp_site_tag_action`

*Fires after a new sites tag has been created.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$group` | `object` | tag created.
`'updated'` |  | 
`$data` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 584](pages/page-mainwp-manage-groups.php#L584-L591)



### `mainwp_added_new_group`

*New Group Added*

Fires after a new sites group has been created.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groupId` | `int` | Group ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 684](pages/page-mainwp-manage-groups.php#L684-L691)



### `mainwp_added_new_group`

*New Group Added*

Fires after a new sites group has been created.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groupId` | `int` | Group ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 729](pages/page-mainwp-manage-groups.php#L729-L736)



### `mainwp_tags_help_item`

*Action: mainwp_tags_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Tags page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 789](pages/page-mainwp-manage-groups.php#L789-L800)



### `mainwp_updates_pergroup_before_wp_updates`

*Action: mainwp_updates_pergroup_before_wp_updates*

Fires at the top of the WP updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_wp_upgrades` | `int` | Number of available WP upates.
`$all_groups_sites` | `array` | Array containing all groups and sites.
`$all_groups` | `array` | Array containing all groups.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 874](pages/page-mainwp-updates.php#L874-L887)



### `mainwp_updates_pergroup_after_wp_updates`

*Action: mainwp_updates_pergroup_after_wp_updates*

Fires at the bottom of the WP updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_wp_upgrades` | `int` | Number of available WP upates.
`$all_groups_sites` | `array` | Array containing all groups and sites.
`$all_groups` | `array` | Array containing all groups.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 889](pages/page-mainwp-updates.php#L889-L902)



### `mainwp_updates_pergroup_before_wp_updates`

*Action: mainwp_updates_persite_before_wp_updates*

Fires at the top of the WP updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_wp_upgrades` | `int` | Number of available WP upates.
`$all_groups_sites` | `array` | Array containing all groups and sites.
`$all_groups` | `array` | Array containing all groups.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 904](pages/page-mainwp-updates.php#L904-L917)



### `mainwp_updates_persite_after_wp_updates`

*Action: mainwp_updates_persite_after_wp_updates*

Fires at the bottom of the WP updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_wp_upgrades` | `int` | Number of available WP upates.
`$all_groups_sites` | `array` | Array containing all groups and sites.
`$all_groups` | `array` | Array containing all groups.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 920](pages/page-mainwp-updates.php#L920-L933)



### `mainwp_updates_persite_before_plugin_updates`

*Action: mainwp_updates_persite_before_plugin_updates*

Fires at the top of the Plugin updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1008](pages/page-mainwp-updates.php#L1008-L1024)



### `mainwp_updates_persite_after_plugin_updates`

*Action: mainwp_updates_persite_after_plugin_updates*

Fires at the bottom of the Plugin updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1026](pages/page-mainwp-updates.php#L1026-L1042)



### `mainwp_updates_pergroup_before_plugin_updates`

*Action: mainwp_updates_pergroup_before_plugin_updates*

Fires at the top of the Plugin updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1044](pages/page-mainwp-updates.php#L1044-L1060)



### `mainwp_updates_pergroup_after_plugin_updates`

*Action: mainwp_updates_pergroup_after_plugin_updates*

Fires at the bottom of the Plugin updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1062](pages/page-mainwp-updates.php#L1062-L1078)



### `mainwp_updates_persite_before_theme_updates`

*Action: mainwp_updates_persite_before_theme_updates*

Fires at the top of the Theme updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1181](pages/page-mainwp-updates.php#L1181-L1197)



### `mainwp_updates_persite_after_theme_updates`

*Action: mainwp_updates_persite_after_theme_updates*

Fires at the bottom of the Theme updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1199](pages/page-mainwp-updates.php#L1199-L1215)



### `mainwp_updates_pergroup_before_theme_updates`

*Action: mainwp_updates_pergroup_before_theme_updates*

Fires at the top of the Theme updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1217](pages/page-mainwp-updates.php#L1217-L1233)



### `mainwp_updates_pergroup_after_theme_updates`

*Action: mainwp_updates_pergroup_after_theme_updates*

Fires at the bottom of the Theme updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1235](pages/page-mainwp-updates.php#L1235-L1251)



### `mainwp_updates_persite_before_translation_updates`

*Action: mainwp_updates_persite_before_translation_updates*

Fires at the top of the Translation updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1352](pages/page-mainwp-updates.php#L1352-L1368)



### `mainwp_updates_persite_after_translation_updates`

*Action: mainwp_updates_persite_after_translation_updates*

Fires at the bottom of the Translation updates tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1370](pages/page-mainwp-updates.php#L1370-L1386)



### `mainwp_updates_pergroup_before_translation_updates`

*Action: mainwp_updates_pergroup_before_translation_updates*

Fires at the top of the Translation updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1388](pages/page-mainwp-updates.php#L1388-L1404)



### `mainwp_updates_pergroup_after_translation_updates`

*Action: mainwp_updates_pergroup_after_translation_updates*

Fires at the bottom of the Translation updates tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1406](pages/page-mainwp-updates.php#L1406-L1422)



### `mainwp_updates_persite_before_abandoned_plugins`

*Action: mainwp_updates_persite_before_abandoned_plugins*

Fires at the top of the Abandoned plugins tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1518](pages/page-mainwp-updates.php#L1518-L1532)



### `mainwp_updates_persite_after_abandoned_plugins`

*Action: mainwp_updates_persite_after_abandoned_plugins*

Fires at the bottom of the Abandoned plugins tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1534](pages/page-mainwp-updates.php#L1534-L1548)



### `mainwp_updates_pergroup_before_abandoned_plugins`

*Action: mainwp_updates_pergroup_before_abandoned_plugins*

Fires at the top of the Abandoned plugins tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1550](pages/page-mainwp-updates.php#L1550-L1564)



### `mainwp_updates_pergroup_after_abandoned_plugins`

*Action: mainwp_updates_pergroup_after_abandoned_plugins*

Fires at the bottom of the Abandoned plugins tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1566](pages/page-mainwp-updates.php#L1566-L1580)



### `mainwp_updates_persite_before_abandoned_themes`

*Action: mainwp_updates_persite_before_abandoned_themes*

Fires at the top of the Abandoned themes tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1669](pages/page-mainwp-updates.php#L1669-L1683)



### `mainwp_updates_persite_after_abandoned_themes`

*Action: mainwp_updates_persite_after_abandoned_themes*

Fires at the bottom of the Abandoned themes tab, per Site view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1685](pages/page-mainwp-updates.php#L1685-L1699)



### `mainwp_updates_pergroup_before_abandoned_themes`

*Action: mainwp_updates_pergroup_before_abandoned_themes*

Fires at the top of the Abandoned themes tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1701](pages/page-mainwp-updates.php#L1701-L1715)



### `mainwp_updates_pergroup_after_abandoned_themes`

*Action: mainwp_updates_pergroup_after_abandoned_themes*

Fires at the bottom of the Abandoned themes tab, per Group view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates.php](pages/page-mainwp-updates.php), [line 1717](pages/page-mainwp-updates.php#L1717-L1731)



### `mainwp_added_new_site`

*This action is documented in class\class-mainwp-manage-sites-view.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$id` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-handler.php](pages/page-mainwp-extensions-handler.php), [line 950](pages/page-mainwp-extensions-handler.php#L950-L951)



### `mainwp_delete_site`

*This action is documented in pages\page-mainwp-manage-sites-handler.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clone_site` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-handler.php](pages/page-mainwp-extensions-handler.php), [line 1040](pages/page-mainwp-extensions-handler.php#L1040-L1041)



### `mainwp_added_new_group`

*This action is documented in pages\page-mainwp-manage-groups.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groupId` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-handler.php](pages/page-mainwp-extensions-handler.php), [line 1075](pages/page-mainwp-extensions-handler.php#L1075-L1076)



### `mainwp_site_info_widget_top`

*Actoin: mainwp_site_info_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-info.php](widgets/widget-mainwp-site-info.php), [line 124](widgets/widget-mainwp-site-info.php#L124-L133)



### `mainwp_site_info_table_top`

*Action: mainwp_site_info_table_top*

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-info.php](widgets/widget-mainwp-site-info.php), [line 146](widgets/widget-mainwp-site-info.php#L146-L155)



### `mainwp_site_info_table_bottom`

*Action: mainwp_site_info_table_bottom*

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-info.php](widgets/widget-mainwp-site-info.php), [line 179](widgets/widget-mainwp-site-info.php#L179-L188)



### `mainwp_site_info_widget_bottom`

*Action: mainwp_site_info_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-info.php](widgets/widget-mainwp-site-info.php), [line 194](widgets/widget-mainwp-site-info.php#L194-L203)



### `mainwp_connection_status_widget_bottom`

*Action: mainwp_connection_status_widget_bottom*

Fires at the bottom of the Connection Status widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 103](widgets/widget-mainwp-connection-status.php#L103-L110)



### `mainwp_connection_status_widget_top`

*Action: mainwp_connection_status_widget_top*

Fires at the top of the Connection Status widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 199](widgets/widget-mainwp-connection-status.php#L199-L206)



### `mainwp_connection_status_before_all_sites_list`

*Action: mainwp_connection_status_before_all_sites_list*

Fires before the list of all sites in the connection status widgets


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 264](widgets/widget-mainwp-connection-status.php#L264-L271)



### `mainwp_connection_status_after_all_sites_list`

*Action: mainwp_connection_status_after_all_sites_list*

Fires after the list of all sites in the connection status widgets


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 277](widgets/widget-mainwp-connection-status.php#L277-L284)



### `mainwp_connection_status_before_connected_sites_list`

*Action: mainwp_connection_status_before_connected_sites_list*

Fires before the list of connected sites in the connection status widgets


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 290](widgets/widget-mainwp-connection-status.php#L290-L297)



### `mainwp_connection_status_after_connected_sites_list`

*Action: mainwp_connection_status_after_connected_sites_list*

Fires after the list of connected sites in the connection status widgets


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 303](widgets/widget-mainwp-connection-status.php#L303-L310)



### `mainwp_connection_status_before_disconnected_sites_list`

*Action: mainwp_connection_status_before_disconnected_sites_list*

Fires before the list of disconnected sites in the connection status widgets


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 316](widgets/widget-mainwp-connection-status.php#L316-L323)



### `mainwp_connection_status_after_disconnected_sites_list`

*Action: mainwp_connection_status_after_disconnected_sites_list*

Fires after the list of disconnected sites in the connection status widgets


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 329](widgets/widget-mainwp-connection-status.php#L329-L336)



### `mainwp_connection_status_widget_footer_left`

*Action: mainwp_connection_status_widget_footer_left*

Fires in the left column of the Connection status widget


**Changelog**

Version | Description
------- | -----------
`5.3` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 344](widgets/widget-mainwp-connection-status.php#L344-L351)



### `mainwp_connection_status_widget_footer_right`

*Action: mainwp_connection_status_widget_footer_right*

Fires in the right column of the Connection status widget


**Changelog**

Version | Description
------- | -----------
`5.3` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 356](widgets/widget-mainwp-connection-status.php#L356-L363)



### `mainwp_clients_overview_websites_widget_top`

*Actoin: mainwp_clients_overview_websites_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-sites.php](widgets/widget-mainwp-client-overview-sites.php), [line 124](widgets/widget-mainwp-client-overview-sites.php#L124-L133)



### `mainwp_clients_overview_websites_widget_bottom`

*Action: mainwp_clients_overview_websites_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-sites.php](widgets/widget-mainwp-client-overview-sites.php), [line 149](widgets/widget-mainwp-client-overview-sites.php#L149-L158)



### `mainwp_widget_site_actions_limit_number`

*Method mainwp_rest_api_non_mainwp_changes_callback()*

Callback function for managing the response to API requests made for the endpoint: non-mainwp-changes
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/site/non-mainwp-changes
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10000` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 3448](includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L3448-L3487)



### `mainwp_widget_site_actions_limit_number`

*Method mainwp_rest_api_non_mainwp_changes_count_callback()*

Callback function for managing the response to API requests made for the endpoint: non-mainwp-changes-count
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/site/non-mainwp-changes-count
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10000` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 3513](includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L3513-L3556)



### `mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`

*Get sites by tag id.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php), [line 370](includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php#L370-L390)



### `mainwp_rest_pre_insert_site_item`

*Filters an object before it is inserted via the REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item_fields` | `array` | Site data.
`$request` | `\WP_REST_Request` | Request object.

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2078](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2078-L2086)



### `mainwp_rest_pre_update_site_item`

*Filters an object before it is inserted via the REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 
`$request` | `\WP_REST_Request` | Request object.

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2125](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2125-L2133)



### `mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`'simple_view'` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 828](includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L828-L828)



### `mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`

*Update all items of site.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`'simple_view'` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 792](includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L792-L858)



### `mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`

*Get sites of client.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-clients-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-clients-controller.php), [line 497](includes/rest-api/controller/version2/class-mainwp-rest-clients-controller.php#L497-L521)



### `mainwp_cron_bulk_update_sites_limit`

*Method handle_cron_batch_updates()*

MainWP Cron batch Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-cron-jobs-batch.php](class/class-mainwp-cron-jobs-batch.php), [line 95](class/class-mainwp-cron-jobs-batch.php#L95-L128)



### `mainwp_currentuserallowedaccessgroups`

*Filter: mainwp_currentuserallowedaccessgroups*

Filters allowed groups for the current user.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'all'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-db.php](class/class-mainwp-db.php), [line 1963](class/class-mainwp-db.php#L1963-L1970)



### `mainwp_boilerplate_get_tokens`

*Filter: mainwp_boilerplate_get_tokens*

Enables and filters the Boilerplate extension tokens.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `object` | Object containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 629](class/class-mainwp-notification-settings.php#L629-L638)



### `mainwp_pro_reports_get_site_tokens`

*Filter: mainwp_pro_reports_get_site_tokens*

Enables and filters the Pro Reports extension tokens.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 648](class/class-mainwp-notification-settings.php#L648-L657)



### `mainwp_client_report_get_site_tokens`

*Filter: mainwp_client_report_get_site_tokens*

Enables and filters the Client Reports extension tokens.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 667](class/class-mainwp-notification-settings.php#L667-L676)



### `mainwp_boilerplate_get_tokens`

*This filter is documented in ../class/class-mainwp-notification-settings.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 708](class/class-mainwp-notification-settings.php#L708-L709)



### `mainwp_pro_reports_get_site_tokens`

*This filter is documented in ../class/class-mainwp-notification-settings.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 715](class/class-mainwp-notification-settings.php#L715-L716)



### `mainwp_client_report_get_site_tokens`

*This filter is documented in ../class/class-mainwp-notification-settings.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-settings.php](class/class-mainwp-notification-settings.php), [line 722](class/class-mainwp-notification-settings.php#L722-L723)



### `mainwp_connect_sign_algo`

*Method get_connect_sign_algorithm().*

Get supported sign algorithms.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$alg` |  | 
`$website` | `mixed` | The Website object.

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-utility.php](class/class-mainwp-system-utility.php), [line 1541](class/class-mainwp-system-utility.php#L1541-L1583)



### `mainwp_staging_current_user_sites_view`

*Method get_select_staging_view_sites()*

Get staging options sites view for current users.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$view` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-utility.php](class/class-mainwp-system-utility.php), [line 1654](class/class-mainwp-system-utility.php#L1654-L1669)



### `mainwp_html_regression_largest_change_scope`

*Method mainwp_upgrade_plugintheme()*

Update plugin or theme.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websiteId` |  | 
`false` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-plugin-theme-handler.php](class/class-mainwp-post-plugin-theme-handler.php), [line 525](class/class-mainwp-post-plugin-theme-handler.php#L525-L638)



### `mainwp_log_to_db_priority`

*Method log_to_db()*

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$priority` | `int` | Set priority.
`$website` | `mixed` | website object.

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 426](class/class-mainwp-logger.php#L426-L445)



### `mainwp_log_do_to_db`

*Method log_to_db()*

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$do_log` |  | 
`$website` | `mixed` | website object.

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 426](class/class-mainwp-logger.php#L426-L457)



### `mainwp_logger_to_db`

*Method log()*

Create Log File.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$website` | `mixed` | Site object.

Source: [../sources/mainwp-dashboard/class/class-mainwp-logger.php](class/class-mainwp-logger.php), [line 502](class/class-mainwp-logger.php#L502-L525)



### `mainwp_curl_curlopt_resolve`

*Fetch uptime urls.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$mo_url` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-uptime-monitoring-connect.php](class/class-mainwp-uptime-monitoring-connect.php), [line 350](class/class-mainwp-uptime-monitoring-connect.php#L350-L502)



### `mainwp_connect_sites_not_allow_ports`

*Method mainwp_testwp()*

Test if Child Site can be reached.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$def_not_allow` |  | 
`$url` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-site-handler.php](class/class-mainwp-post-site-handler.php), [line 236](class/class-mainwp-post-site-handler.php#L236-L264)



### `mainwp_connect_sites_allow_ports`

*Method mainwp_testwp()*

Test if Child Site can be reached.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$url` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-site-handler.php](class/class-mainwp-post-site-handler.php), [line 236](class/class-mainwp-post-site-handler.php#L236-L282)



### `mainwp_manage_sites_force_use_ipv4`

*Method mainwp_testwp()*

Test if Child Site can be reached.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$url` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-site-handler.php](class/class-mainwp-post-site-handler.php), [line 236](class/class-mainwp-post-site-handler.php#L236-L292)



### `mainwp_postprocess_backup_sites_feedback`

*Method  backup_site()*

Backup Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$unique` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-backup-handler.php](class/class-mainwp-backup-handler.php), [line 28](class/class-mainwp-backup-handler.php#L28-L513)



### `mainwp_clone_enabled`

*Filter: mainwp_clone_enabled*

Filters whether the Clone feature is enabled or disabled.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 104](class/class-mainwp-sync.php#L104-L111)



### `mainwp-sync-others-data`

*Method sync_site()*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array(), $pWebsite)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sync_others_data'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 62](class/class-mainwp-sync.php#L62-L150)



### `mainwp_sync_others_data`

*Filter: mainwp_sync_others_data*

Filters additional data in the sync request. Allows extensions or 3rd party plugins to hook data to the sync request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$othersData` |  | 
`$pWebsite` | `object` | Object contaning child site data.

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 152](class/class-mainwp-sync.php#L152-L163)



### `mainwp_site_actions_saved_days_number`

*Method sync_site()*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`30` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 62](class/class-mainwp-sync.php#L62-L165)



### `mainwp_before_save_sync_result`

*Filter: mainwp_before_save_sync_result*

Filters data returned from child site before saving to the database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$pWebsite` | `object` | Object containing child site data.

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 267](class/class-mainwp-sync.php#L267-L276)



### `mainwp_sync_site_after_sync_result`

*Method sync_information_array()*

Grab all Child Site Information.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$error` | `bool` | True\|False.
`$pWebsite` | `object` | The website object.
`$information` | `array` | Array contaning information returned from child site.

Source: [../sources/mainwp-dashboard/class/class-mainwp-sync.php](class/class-mainwp-sync.php), [line 221](class/class-mainwp-sync.php#L221-L575)



### `mainwp_managesites_getbackuplink`

*Filter: mainwp_managesites_getbackuplink*

Filters the link for the last backup item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$item['id']` |  | 
`$lastBackup` | `string` | Last backup timestamp for the child site.
`$backup_method` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 104](class/class-mainwp-manage-sites-list-table.php#L104-L114)



### `mainwp_managesites_bulk_actions`

*Filter: mainwp_managesites_bulk_actions*

Filters bulk actions on the Manage Sites page. Allows user to hook in new actions or remove default ones.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$actions` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 504](class/class-mainwp-manage-sites-list-table.php#L504-L511)



### `mainwp_sites_table_features`

*Filter: mainwp_sites_table_features*

Filter the Monitoring table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1136](class/class-mainwp-manage-sites-list-table.php#L1136-L1143)



### `mainwp_sitestable_website`

*Get table rows.*

Optimize for shared hosting or big networks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$this->userExtension` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1554](class/class-mainwp-manage-sites-list-table.php#L1554-L1700)



### `mainwp_sitestable_website`

*Columns for a single row.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `mixed` | Child Site.
`$this->userExtension` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-list-table.php](class/class-mainwp-manage-sites-list-table.php), [line 1971](class/class-mainwp-manage-sites-list-table.php#L1971-L2148)



### `mainwp_monitoringsites_bulk_actions`

*Filter: mainwp_monitoringsites_bulk_actions*

Filters bulk actions on the Monitoring Sites page. Allows user to hook in new actions or remove default ones.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$actions` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-monitoring-sites-list-table.php](class/class-mainwp-monitoring-sites-list-table.php), [line 295](class/class-mainwp-monitoring-sites-list-table.php#L295-L302)



### `mainwp_updatescheck_sendmail_for_each_auto_sync_finished`

*Method cron_updates_check()*

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-cron-jobs.php](class/class-mainwp-system-cron-jobs.php), [line 375](class/class-mainwp-system-cron-jobs.php#L375-L456)



### `mainwp_pre_fetch_authed_data`

*Method get_post_data_authed()*

Get authorized $_POST data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$params` | `null` | Post parameters.
`$what` | `mixed` | What we are posting.
`$website` | `mixed` | Array of Child Site Info.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 361](class/class-mainwp-connect.php#L361-L380)



### `mainwp_open_site_login_required_params`

*Method get_get_data_authed()*

Get authorized $_GET data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$params` |  | 
`$website` | `mixed` | Child Site data.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 525](class/class-mainwp-connect.php#L525-L583)



### `mainwp_curl_curlopt_resolve`

*Method fetch_urls_authed()*

Fetches data from child sites if authenticated.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$website->url` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 688](class/class-mainwp-connect.php#L688-L899)



### `mainwp_curl_curlopt_resolve`

*Method fetch_url_site()*

M Fetch URL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$website->url` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1351](class/class-mainwp-connect.php#L1351-L1494)



### `mainwp_manage_sites_navigation_items`

*Method render_managesites_header()*

Render manage sites header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$renderItems` |  | 
`$site_id` | `int` | Site id.
`$shownPage` | `string` | Current Page.

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 316](class/class-mainwp-manage-sites-view.php#L316-L374)



### `mainwp-sync-extensions-options`

*Method render_sync_exts_settings()*

Render sync extension settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sync_extensions_options'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 566](class/class-mainwp-manage-sites-view.php#L566-L575)



### `mainwp_sync_extensions_options`

*Method render_sync_exts_settings()*

Render sync extension settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sync_extensions_options` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 566](class/class-mainwp-manage-sites-view.php#L566-L576)



### `mainwp_default_template_locate`

*Render the email notification edit form.*

Credits.

Plugin-Name: WooCommerce.
Plugin URI: https://woocommerce.com/.
Author: Automattic.
Author URI: https://woocommerce.com.
License: GPLv3 or later.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$default_file` |  | 
`$template` |  | 
`$default_dir` |  | 
`$type` | `string` | Email type.
`$siteid` | `bool` | Child site ID.

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 1654](class/class-mainwp-manage-sites-view.php#L1654-L1680)



### `mainwp_manage_sites_force_use_ipv4`

*Method add_site()*

Add Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`null` |  | 
`$params['url']` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-manage-sites-view.php](class/class-mainwp-manage-sites-view.php), [line 2020](class/class-mainwp-manage-sites-view.php#L2020-L2039)



### `mainwp_clients_website_client_tokens`

*Method get_website_client_tokens_data()*

Get website client tokens.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_tokens` |  | 
`$websiteid` | `int` | Website ID.
`$clientid` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-client-handler.php](class/class-mainwp-client-handler.php), [line 454](class/class-mainwp-client-handler.php#L454-L530)



### `mainwp_cron_bulk_update_sites_limit`

*Method handle_cron_auto_updates()*

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-cron-jobs-auto-updates.php](class/class-mainwp-cron-jobs-auto-updates.php), [line 104](class/class-mainwp-cron-jobs-auto-updates.php#L104-L115)



### `mainwp_getwebsite_by_id`

*Get sites by website ID.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website_id` | `int` | User ID.
`$selectGroups` | `bool` | Select groups.
`$extra_view` | `array` | get extra option fields.

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-helper.php](modules/api-backups/classes/class-api-backups-helper.php), [line 60](modules/api-backups/classes/class-api-backups-helper.php#L60-L70)



### `mainwp_updatewebsiteoptions`

*Method update_website_option().*

Update the website option.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `object\|int` | website object or ID.
`$opt_name` | `string` | website.
`$opt_value` | `string` | website.

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-helper.php](modules/api-backups/classes/class-api-backups-helper.php), [line 78](modules/api-backups/classes/class-api-backups-helper.php#L78-L88)



### `mainwp_getwebsiteoptions`

*Method get_website_options().*

Get the website options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `object\|int` | website object or ID.
`$options` | `string\|array` | Options name.

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-helper.php](modules/api-backups/classes/class-api-backups-helper.php), [line 91](modules/api-backups/classes/class-api-backups-helper.php#L91-L100)



### `mainwp_db_fetch_object`

*Method fetch_object().*

Handle fetch object db.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$websites` | `mixed` | websites results.

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-helper.php](modules/api-backups/classes/class-api-backups-helper.php), [line 104](modules/api-backups/classes/class-api-backups-helper.php#L104-L114)



### `mainwp_db_free_result`

*Method free_result().*

Handle fetch result db.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$results` | `mixed` | websites results.

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-helper.php](modules/api-backups/classes/class-api-backups-helper.php), [line 118](modules/api-backups/classes/class-api-backups-helper.php#L118-L131)



### `mainwp_module_log_data`

*Log handler*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`compact('connector', 'message', 'args', 'site_id', 'context', 'action', 'state', 'user_id')` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-connector.php](modules/logs/classes/class-log-connector.php), [line 81](modules/logs/classes/class-log-connector.php#L81-L100)



### `mainwp_module_log_cron_tracking`

*Log handler.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$connector` | `\MainWP\Dashboard\Module\Log\Connector` | Connector responsible for logging the event.
`$message` | `string` | sprintf-ready error message string.
`$args` | `array` | sprintf (and extra) arguments to use.
`$site_id` | `int` | Target site id.
`$context` | `string` | Context of the event.
`$action` | `string` | Action of the event.
`$user_id` | `int` | User responsible for the event.
`$state` | `int\|null` | action status: null - N/A, 0 - failed, 1 - success.

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log.php](modules/logs/classes/class-log.php), [line 36](modules/logs/classes/class-log.php#L36-L60)



### `mainwp_rest_routes_sites_controller_get_allowed_fields_by_context`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'view'` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 545](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L545-L545)



### `mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`

*Get sites by item.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 509](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L509-L552)



### `mainwp_manage_sites_force_use_ipv4`

*Method check_site()*

Check to add site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`null` |  | 
`$url` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites-handler.php](pages/page-mainwp-manage-sites-handler.php), [line 26](pages/page-mainwp-manage-sites-handler.php#L26-L56)



### `mainwp_posting_selected_groups`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_groups` |  | 
`$id` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L635)



### `mainwp_custom_post_types_get_post_connections`

*Method posts_search_handler()*

Post page search handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$child_post_ids` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1282](pages/page-mainwp-post.php#L1282-L1325)



### `mainwp_bulkpost_select_sites_settings`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sites_settings` |  | 
`$post` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2275)



### `mainwp_manage_sites_optimize_loading`

*Method render_all_sites()*

Render manage sites content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1` |  | 
`'manage-sites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 1706](pages/page-mainwp-manage-sites.php#L1706-L1717)



### `mainwp_open_site_allow_vars`

*Child Site Dashboard Link redirect handler.*

This method checks to see if the current user is allow to access the
Child Site, then grabs the websiteid, location, openurl & passes it onto
either open_site_location or open_site methods.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allow_vars` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-site-open.php](pages/page-mainwp-site-open.php), [line 27](pages/page-mainwp-site-open.php#L27-L72)



### `mainwp_html_regression_largest_change_scope`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->id` |  | 
`true` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-updates-handler.php](pages/page-mainwp-updates-handler.php), [line 58](pages/page-mainwp-updates-handler.php#L58-L58)



### `mainwp_manage_sites_optimize_loading`

*Method render_all_sites()*

Render monitoring sites content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1` |  | 
`'monitor-sites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-monitoring.php](pages/page-mainwp-monitoring.php), [line 272](pages/page-mainwp-monitoring.php#L272-L285)



### `mainwp_child_site_info_widget_content`

*Filter: mainwp_child_site_info_widget_content*

Filters the Child Info array for the Site Info widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$child_site_info` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-info.php](widgets/widget-mainwp-site-info.php), [line 83](widgets/widget-mainwp-site-info.php#L83-L90)



### `mainwp_site_info_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Site Info', 'mainwp')` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-info.php](widgets/widget-mainwp-site-info.php), [line 116](widgets/widget-mainwp-site-info.php#L116-L116)



### `mainwp_connection_status_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Connection Status', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 156](widgets/widget-mainwp-connection-status.php#L156-L156)



### `mainwp_connection_status_list_item_title_url`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'admin.php?page=managesites&dashboard=' . $website->id` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 407](widgets/widget-mainwp-connection-status.php#L407-L407)



### `mainwp_connection_status_list_item_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->name` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 418](widgets/widget-mainwp-connection-status.php#L418-L418)



### `mainwp_connection_status_list_item_title_url`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'admin.php?page=managesites&dashboard=' . $website->id` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 459](widgets/widget-mainwp-connection-status.php#L459-L459)



### `mainwp_connection_status_list_item_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->name` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 470](widgets/widget-mainwp-connection-status.php#L470-L470)



### `mainwp_connection_status_list_item_title_url`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'admin.php?page=managesites&dashboard=' . $website->id` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 506](widgets/widget-mainwp-connection-status.php#L506-L506)



### `mainwp_connection_status_list_item_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->name` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-connection-status.php](widgets/widget-mainwp-connection-status.php), [line 517](widgets/widget-mainwp-connection-status.php#L517-L517)



### `mainwp_clients_overview_websites_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites', 'mainwp')` |  | 
`$client_info` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-sites.php](widgets/widget-mainwp-client-overview-sites.php), [line 117](widgets/widget-mainwp-client-overview-sites.php#L117-L117)



### `mainwp_widget_site_actions_limit_number`

*Method render()*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`50` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-site-actions.php](widgets/widget-mainwp-site-actions.php), [line 75](widgets/widget-mainwp-site-actions.php#L75-L84)




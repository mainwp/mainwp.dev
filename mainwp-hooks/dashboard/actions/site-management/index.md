# Site Management Actions

Hooks related to adding, editing, removing, and managing sites and site groups.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-extension-sites-edit`](#mainwp-extension-sites-edit) - Method render_edit_site()
- [`mainwp-manage-sites-edit`](#mainwp-manage-sites-edit) - Method render_new_site_add_new_site()
- [`mainwp-site-synced`](#mainwp-site-synced) - Method sync_information_array()
- [`mainwp-sync-extensions-options`](#mainwp-sync-extensions-options) - Method render_sync_exts_settings()
- [`mainwp-sync-others-data`](#mainwp-sync-others-data) - Method sync_site()
- [`mainwp_added_new_group`](#mainwp-added-new-group) - New Group Added
- [`mainwp_added_new_site`](#mainwp-added-new-site) - This action is documented in class\class-mainwp-manage-sites-view.php
- [`mainwp_after_edit_site_note`](#mainwp-after-edit-site-note) - Action: mainwp_after_edit_site_note
- [`mainwp_after_groups_table`](#mainwp-after-groups-table) - Action: mainwp_after_groups_table
- [`mainwp_after_manage_sites_table`](#mainwp-after-manage-sites-table) - Action: mainwp_after_manage_sites_table
- [`mainwp_after_notice_sites_uptime_monitoring_admin`](#mainwp-after-notice-sites-uptime-monitoring-admin) - Basic site uptime monitoring.
- [`mainwp_after_notice_sites_uptime_monitoring_individual`](#mainwp-after-notice-sites-uptime-monitoring-individual) - Basic site uptime monitoring.
- [`mainwp_after_select_groups_list`](#mainwp-after-select-groups-list) - Action: mainwp_after_select_groups_list
- [`mainwp_after_select_sites_filters`](#mainwp-after-select-sites-filters) - Action: mainwp_after_select_sites_filters
- [`mainwp_after_select_sites_list`](#mainwp-after-select-sites-list) - Action: mainwp_after_select_sites_list
- [`mainwp_after_sync_site_success`](#mainwp-after-sync-site-success) - Fires immediately after website synced successfully.
- [`mainwp_ajax_add_action`](#mainwp-ajax-add-action) - Init ajax actions.
- [`mainwp_auto_updates_sync_data_before_run`](#mainwp-auto-updates-sync-data-before-run) - Method handle_cron_auto_updates()
- [`mainwp_before_edit_site_note`](#mainwp-before-edit-site-note) - Action: mainwp_before_edit_site_note
- [`mainwp_before_groups_table`](#mainwp-before-groups-table) - Action: mainwp_before_groups_table
- [`mainwp_before_manage_sites_table`](#mainwp-before-manage-sites-table) - Action: mainwp_before_manage_sites_table
- [`mainwp_before_save_sync_result`](#mainwp-before-save-sync-result) - Filter: mainwp_before_save_sync_result
- [`mainwp_before_select_groups_list`](#mainwp-before-select-groups-list) - Action: mainwp_before_select_groups_list
- [`mainwp_before_select_sites_filters`](#mainwp-before-select-sites-filters) - Action: mainwp_before_select_sites_filters
- [`mainwp_before_select_sites_list`](#mainwp-before-select-sites-list) - Action: mainwp_before_select_sites_list
- [`mainwp_boilerplate_get_tokens`](#mainwp-boilerplate-get-tokens) - This filter is documented in ../class/class-mainwp-notification-settings.php
- [`mainwp_bulkpost_select_sites_settings`](#mainwp-bulkpost-select-sites-settings) - Renders bulkpost to edit.
- [`mainwp_check_site_result`](#mainwp-check-site-result) - Method check_site()
- [`mainwp_child_site_info_widget_content`](#mainwp-child-site-info-widget-content) - Filter: mainwp_child_site_info_widget_content
- [`mainwp_client_report_get_site_tokens`](#mainwp-client-report-get-site-tokens) - Filter: mainwp_client_report_get_site_tokens
- [`mainwp_clients_overview_websites_widget_bottom`](#mainwp-clients-overview-websites-widget-bottom) - Action: mainwp_clients_overview_websites_widget_bottom
- [`mainwp_clients_overview_websites_widget_title`](#mainwp-clients-overview-websites-widget-title) - *Arguments*
- [`mainwp_clients_overview_websites_widget_top`](#mainwp-clients-overview-websites-widget-top) - Actoin: mainwp_clients_overview_websites_widget_top
- [`mainwp_clients_website_client_tokens`](#mainwp-clients-website-client-tokens) - Method get_website_client_tokens_data()
- [`mainwp_connect_sign_algo`](#mainwp-connect-sign-algo) - Method get_connect_sign_algorithm().
- [`mainwp_connect_sites_allow_ports`](#mainwp-connect-sites-allow-ports) - Method mainwp_testwp()
- [`mainwp_connect_sites_not_allow_ports`](#mainwp-connect-sites-not-allow-ports) - Method mainwp_testwp()
- [`mainwp_connection_status_after_all_sites_list`](#mainwp-connection-status-after-all-sites-list) - Action: mainwp_connection_status_after_all_sites_list
- [`mainwp_connection_status_after_connected_sites_list`](#mainwp-connection-status-after-connected-sites-list) - Action: mainwp_connection_status_after_connected_sites_list
- [`mainwp_connection_status_after_disconnected_sites_list`](#mainwp-connection-status-after-disconnected-sites-list) - Action: mainwp_connection_status_after_disconnected_sites_list
- [`mainwp_connection_status_before_all_sites_list`](#mainwp-connection-status-before-all-sites-list) - Action: mainwp_connection_status_before_all_sites_list
- [`mainwp_connection_status_before_connected_sites_list`](#mainwp-connection-status-before-connected-sites-list) - Action: mainwp_connection_status_before_connected_sites_list
- [`mainwp_connection_status_before_disconnected_sites_list`](#mainwp-connection-status-before-disconnected-sites-list) - Action: mainwp_connection_status_before_disconnected_sites_list
- [`mainwp_connection_status_list_item_title`](#mainwp-connection-status-list-item-title) - *Arguments*
- [`mainwp_connection_status_list_item_title_url`](#mainwp-connection-status-list-item-title-url) - *Arguments*
- [`mainwp_connection_status_widget_bottom`](#mainwp-connection-status-widget-bottom) - Action: mainwp_connection_status_widget_bottom
- [`mainwp_connection_status_widget_footer_left`](#mainwp-connection-status-widget-footer-left) - Action: mainwp_connection_status_widget_footer_left
- [`mainwp_connection_status_widget_footer_right`](#mainwp-connection-status-widget-footer-right) - Action: mainwp_connection_status_widget_footer_right
- [`mainwp_connection_status_widget_title`](#mainwp-connection-status-widget-title) - *Arguments*
- [`mainwp_connection_status_widget_top`](#mainwp-connection-status-widget-top) - Action: mainwp_connection_status_widget_top
- [`mainwp_cron_bulk_update_sites_limit`](#mainwp-cron-bulk-update-sites-limit) - Method handle_cron_batch_updates()
- [`mainwp_curl_curlopt_resolve`](#mainwp-curl-curlopt-resolve) - Fetch uptime urls.
- [`mainwp_currentuserallowedaccessgroups`](#mainwp-currentuserallowedaccessgroups) - Filter: mainwp_currentuserallowedaccessgroups
- [`mainwp_custom_post_types_get_post_connections`](#mainwp-custom-post-types-get-post-connections) - Method posts_search_handler()
- [`mainwp_delete_key_file`](#mainwp-delete-key-file) - Method update_compatible_site_api_key
- [`mainwp_delete_site`](#mainwp-delete-site) - *Arguments*
- [`mainwp_extension_sites_edit_tablerow`](#mainwp-extension-sites-edit-tablerow) - Method render_edit_site()
- [`mainwp_fetch_url_authed`](#mainwp-fetch-url-authed) - Fires immediately after fetch url action.
- [`mainwp_getwebsite_by_id`](#mainwp-getwebsite-by-id) - Get sites by website ID.
- [`mainwp_getwebsiteoptions`](#mainwp-getwebsiteoptions) - Method get_website_options().
- [`mainwp_html_regression_largest_change_scope`](#mainwp-html-regression-largest-change-scope) - *Arguments*
- [`mainwp_manage_sites_action`](#mainwp-manage-sites-action) - Action: mainwp_manage_sites_action
- [`mainwp_manage_sites_edit`](#mainwp-manage-sites-edit) - Edit site
- [`mainwp_manage_sites_email_settings`](#mainwp-manage-sites-email-settings) - Action: mainwp_manage_sites_email_settings
- [`mainwp_manage_sites_force_use_ipv4`](#mainwp-manage-sites-force-use-ipv4) - Method check_site()
- [`mainwp_manage_sites_navigation_items`](#mainwp-manage-sites-navigation-items) - Method render_managesites_header()
- [`mainwp_manage_sites_optimize_loading`](#mainwp-manage-sites-optimize-loading) - Method render_all_sites()
- [`mainwp_manage_sites_table_columns_defs`](#mainwp-manage-sites-table-columns-defs) - Display the table.
- [`mainwp_managesite_backup`](#mainwp-managesite-backup) - Method backup()
- [`mainwp_managesite_schedule_backup`](#mainwp-managesite-schedule-backup) - Execute the backup task.
- [`mainwp_managesites_bulk_actions`](#mainwp-managesites-bulk-actions) - Filter: mainwp_managesites_bulk_actions
- [`mainwp_managesites_getbackuplink`](#mainwp-managesites-getbackuplink) - Filter: mainwp_managesites_getbackuplink
- [`mainwp_managesites_tabletop`](#mainwp-managesites-tabletop) - Action: mainwp_managesites_tabletop
- [`mainwp_module_log_cron_tracking`](#mainwp-module-log-cron-tracking) - Log handler.
- [`mainwp_module_log_data`](#mainwp-module-log-data) - Log handler
- [`mainwp_monitoringsites_bulk_actions`](#mainwp-monitoringsites-bulk-actions) - Filter: mainwp_monitoringsites_bulk_actions
- [`mainwp_open_site_allow_vars`](#mainwp-open-site-allow-vars) - Child Site Dashboard Link redirect handler.
- [`mainwp_open_site_login_required_params`](#mainwp-open-site-login-required-params) - Method get_get_data_authed()
- [`mainwp_posting_selected_groups`](#mainwp-posting-selected-groups) - Method posting_posts()
- [`mainwp_postprocess_backup_sites_feedback`](#mainwp-postprocess-backup-sites-feedback) - Method  backup_site()
- [`mainwp_pro_reports_get_site_tokens`](#mainwp-pro-reports-get-site-tokens) - Filter: mainwp_pro_reports_get_site_tokens
- [`mainwp_quick_sites_shortcut`](#mainwp-quick-sites-shortcut) - Action: mainwp_quick_sites_shortcut
- [`mainwp_rest_pre_insert_site_item`](#mainwp-rest-pre-insert-site-item) - Filters an object before it is inserted via the REST API.
- [`mainwp_rest_pre_update_site_item`](#mainwp-rest-pre-update-site-item) - Filters an object before it is inserted via the REST API.
- [`mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`](#mainwp-rest-routes-sites-controller-filter-allowed-fields-by-context) - *Arguments*
- [`mainwp_rest_routes_sites_controller_get_allowed_fields_by_context`](#mainwp-rest-routes-sites-controller-get-allowed-fields-by-context) - *Arguments*
- [`mainwp_select_sites_box`](#mainwp-select-sites-box) - Render settings
- [`mainwp_site_actions_saved_days_number`](#mainwp-site-actions-saved-days-number) - Method sync_site()
- [`mainwp_site_added`](#mainwp-site-added) - Fires immediately after a new website is added.
- [`mainwp_site_changes_table_pages_length`](#mainwp-site-changes-table-pages-length) - Display the table.
- [`mainwp_site_deleted`](#mainwp-site-deleted) - *Arguments*
- [`mainwp_site_health_monitoring_email_footer`](#mainwp-site-health-monitoring-email-footer) - Site Health Monitoring Email Footer
- [`mainwp_site_health_monitoring_email_header`](#mainwp-site-health-monitoring-email-header) - Site Health Monitoring Email Header
- [`mainwp_site_info_table_bottom`](#mainwp-site-info-table-bottom) - Action: mainwp_site_info_table_bottom
- [`mainwp_site_info_table_top`](#mainwp-site-info-table-top) - Action: mainwp_site_info_table_top
- [`mainwp_site_info_widget_bottom`](#mainwp-site-info-widget-bottom) - Action: mainwp_site_info_widget_bottom
- [`mainwp_site_info_widget_title`](#mainwp-site-info-widget-title) - *Arguments*
- [`mainwp_site_info_widget_top`](#mainwp-site-info-widget-top) - Actoin: mainwp_site_info_widget_top
- [`mainwp_site_reconnected`](#mainwp-site-reconnected) - Fires immediately after reconnect website.
- [`mainwp_site_suspended`](#mainwp-site-suspended) - Fires immediately after website suspended/unsuspend.
- [`mainwp_site_sync`](#mainwp-site-sync) - Action: mainwp_site_sync
- [`mainwp_site_synced`](#mainwp-site-synced) - Action: mainwp_site_synced
- [`mainwp_site_tag_action`](#mainwp-site-tag-action) - Fires after a new sites tag has been created.
- [`mainwp_site_updated`](#mainwp-site-updated) - Update site
- [`mainwp_sites_table_features`](#mainwp-sites-table-features) - Filter: mainwp_sites_table_features
- [`mainwp_sitestable_website`](#mainwp-sitestable-website) - Get table rows.
- [`mainwp_staging_current_user_sites_view`](#mainwp-staging-current-user-sites-view) - Method get_select_staging_view_sites()
- [`mainwp_sync_extensions_options`](#mainwp-sync-extensions-options) - Method render_sync_exts_settings()
- [`mainwp_sync_others_data`](#mainwp-sync-others-data) - Filter: mainwp_sync_others_data
- [`mainwp_sync_popup_content`](#mainwp-sync-popup-content) - Method render_footer_content()
- [`mainwp_sync_site_after_sync_result`](#mainwp-sync-site-after-sync-result) - Method sync_information_array()
- [`mainwp_sync_site_log_install_actions`](#mainwp-sync-site-log-install-actions) - Method sync_log_site_actions().
- [`mainwp_synced_all_sites`](#mainwp-synced-all-sites) - Method cron_updates_check()
- [`mainwp_updates_pergroup_after_abandoned_plugins`](#mainwp-updates-pergroup-after-abandoned-plugins) - Action: mainwp_updates_pergroup_after_abandoned_plugins
- [`mainwp_updates_pergroup_after_abandoned_themes`](#mainwp-updates-pergroup-after-abandoned-themes) - Action: mainwp_updates_pergroup_after_abandoned_themes
- [`mainwp_updates_pergroup_after_plugin_updates`](#mainwp-updates-pergroup-after-plugin-updates) - Action: mainwp_updates_pergroup_after_plugin_updates
- [`mainwp_updates_pergroup_after_theme_updates`](#mainwp-updates-pergroup-after-theme-updates) - Action: mainwp_updates_pergroup_after_theme_updates
- [`mainwp_updates_pergroup_after_translation_updates`](#mainwp-updates-pergroup-after-translation-updates) - Action: mainwp_updates_pergroup_after_translation_updates
- [`mainwp_updates_pergroup_after_wp_updates`](#mainwp-updates-pergroup-after-wp-updates) - Action: mainwp_updates_pergroup_after_wp_updates
- [`mainwp_updates_pergroup_before_abandoned_plugins`](#mainwp-updates-pergroup-before-abandoned-plugins) - Action: mainwp_updates_pergroup_before_abandoned_plugins
- [`mainwp_updates_pergroup_before_abandoned_themes`](#mainwp-updates-pergroup-before-abandoned-themes) - Action: mainwp_updates_pergroup_before_abandoned_themes
- [`mainwp_updates_pergroup_before_plugin_updates`](#mainwp-updates-pergroup-before-plugin-updates) - Action: mainwp_updates_pergroup_before_plugin_updates
- [`mainwp_updates_pergroup_before_theme_updates`](#mainwp-updates-pergroup-before-theme-updates) - Action: mainwp_updates_pergroup_before_theme_updates
- [`mainwp_updates_pergroup_before_translation_updates`](#mainwp-updates-pergroup-before-translation-updates) - Action: mainwp_updates_pergroup_before_translation_updates
- [`mainwp_updates_pergroup_before_wp_updates`](#mainwp-updates-pergroup-before-wp-updates) - Action: mainwp_updates_pergroup_before_wp_updates
- [`mainwp_updates_persite_after_abandoned_plugins`](#mainwp-updates-persite-after-abandoned-plugins) - Action: mainwp_updates_persite_after_abandoned_plugins
- [`mainwp_updates_persite_after_abandoned_themes`](#mainwp-updates-persite-after-abandoned-themes) - Action: mainwp_updates_persite_after_abandoned_themes
- [`mainwp_updates_persite_after_plugin_updates`](#mainwp-updates-persite-after-plugin-updates) - Action: mainwp_updates_persite_after_plugin_updates
- [`mainwp_updates_persite_after_theme_updates`](#mainwp-updates-persite-after-theme-updates) - Action: mainwp_updates_persite_after_theme_updates
- [`mainwp_updates_persite_after_translation_updates`](#mainwp-updates-persite-after-translation-updates) - Action: mainwp_updates_persite_after_translation_updates
- [`mainwp_updates_persite_after_wp_updates`](#mainwp-updates-persite-after-wp-updates) - Action: mainwp_updates_persite_after_wp_updates
- [`mainwp_updates_persite_before_abandoned_plugins`](#mainwp-updates-persite-before-abandoned-plugins) - Action: mainwp_updates_persite_before_abandoned_plugins
- [`mainwp_updates_persite_before_abandoned_themes`](#mainwp-updates-persite-before-abandoned-themes) - Action: mainwp_updates_persite_before_abandoned_themes
- [`mainwp_updates_persite_before_plugin_updates`](#mainwp-updates-persite-before-plugin-updates) - Action: mainwp_updates_persite_before_plugin_updates
- [`mainwp_updates_persite_before_theme_updates`](#mainwp-updates-persite-before-theme-updates) - Action: mainwp_updates_persite_before_theme_updates
- [`mainwp_updates_persite_before_translation_updates`](#mainwp-updates-persite-before-translation-updates) - Action: mainwp_updates_persite_before_translation_updates
- [`mainwp_updatescheck_sendmail_for_each_auto_sync_finished`](#mainwp-updatescheck-sendmail-for-each-auto-sync-finished) - Method cron_updates_check()
- [`mainwp_updatewebsiteoptions`](#mainwp-updatewebsiteoptions) - Method update_website_option().
- [`mainwp_website_before_updated`](#mainwp-website-before-updated) - Action: mainwp_website_before_updated
- [`mainwp_website_updated`](#mainwp-website-updated) - Action: mainwp_website_updated
- [`mainwp_widget_site_actions_limit_number`](#mainwp-widget-site-actions-limit-number) - Method mainwp_rest_api_non_mainwp_changes_callback()

---

## Hook Details

<a id='mainwp-extension-sites-edit'></a>
### `mainwp-extension-sites-edit`

* Method render_edit_site()

Render individual Child Site Edit sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_manage_sites_edit'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 831](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L831)

---

<a id='mainwp-manage-sites-edit'></a>
### `mainwp-manage-sites-edit`

* Method render_new_site_add_new_site()

Render page managesites add new site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_manage_sites_edit'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 831](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L831)
- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 787](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L787)

---

<a id='mainwp-site-synced'></a>
### `mainwp-site-synced`

* Method sync_information_array()

Grab all Child Site Information.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($pWebsite, $information)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_site_synced'` |  |

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 221](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L221)

---

<a id='mainwp-sync-extensions-options'></a>
### `mainwp-sync-extensions-options`

* Method render_sync_exts_settings()

Render sync extension settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sync_extensions_options'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 566](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L566)

---

<a id='mainwp-sync-others-data'></a>
### `mainwp-sync-others-data`

* Method sync_site()

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array(), $pWebsite)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sync_others_data'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array(), $pWebsite)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sync_others_data'` |  |

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 62](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L62)

---

<a id='mainwp-added-new-group'></a>
### `mainwp_added_new_group`

* New Group Added

Fires after a new sites group has been created.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groupId` | `int` | Group ID.

**Usage Locations:**

- [class/class-mainwp-db-common.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-common.php), [line 634](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-common.php#L634)
- [pages/page-mainwp-extensions-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php), [line 1080](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php#L1080)
- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 684](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L684)
- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 729](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L729)

---

<a id='mainwp-added-new-site'></a>
### `mainwp_added_new_site`

* This action is documented in class\class-mainwp-manage-sites-view.php

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$id` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$id` |  | 
`$website` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 2267](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L2267)
- [pages/page-mainwp-extensions-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php), [line 955](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php#L955)

---

<a id='mainwp-after-edit-site-note'></a>
### `mainwp_after_edit_site_note`

* Action: mainwp_after_edit_site_note

Fires after the site note content in the Edit Note modal element.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2051](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2051)

---

<a id='mainwp-after-groups-table'></a>
### `mainwp_after_groups_table`

* Action: mainwp_after_groups_table

Fires after the Manage Groups table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 463](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L463)

---

<a id='mainwp-after-manage-sites-table'></a>
### `mainwp_after_manage_sites_table`

* Action: mainwp_after_manage_sites_table

Fires after the Manage Sites table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1106](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1106)

---

<a id='mainwp-after-notice-sites-uptime-monitoring-admin'></a>
### `mainwp_after_notice_sites_uptime_monitoring_admin`

* Basic site uptime monitoring.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the websites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the websites.

**Usage Locations:**

- [class/class-mainwp-monitoring-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-handler.php), [line 151](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-handler.php#L151)

---

<a id='mainwp-after-notice-sites-uptime-monitoring-individual'></a>
### `mainwp_after_notice_sites_uptime_monitoring_individual`

* Basic site uptime monitoring.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site` |  |

**Usage Locations:**

- [class/class-mainwp-monitoring-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-handler.php), [line 151](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-handler.php#L151)

---

<a id='mainwp-after-select-groups-list'></a>
### `mainwp_after_select_groups_list`

* Action: mainwp_after_select_groups_list

Fires after the Select Groups list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groups` | `object` | Object containing groups info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 458](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L458)

---

<a id='mainwp-after-select-sites-filters'></a>
### `mainwp_after_select_sites_filters`

* Action: mainwp_after_select_sites_filters

Fires after the Select Sites box filters.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 206](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L206)

---

<a id='mainwp-after-select-sites-list'></a>
### `mainwp_after_select_sites_list`

* Action: mainwp_after_select_sites_list

Fires after the Select Sites list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 330](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L330)

---

<a id='mainwp-after-sync-site-success'></a>
### `mainwp_after_sync_site_success`

* Fires immediately after website synced successfully.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [class/class-mainwp-post-site-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php), [line 407](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php#L407)

---

<a id='mainwp-ajax-add-action'></a>
### `mainwp_ajax_add_action`

* Init ajax actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'mainwp_api_backups_selected_websites'` |  | 
`array(&$this, 'ajax_backups_selected_websites')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'mainwp_api_backups_selected_websites'` |  | 
`array(&$this, 'ajax_backups_selected_websites')` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-handler.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-handler.php), [line 53](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-handler.php#L53)

---

<a id='mainwp-auto-updates-sync-data-before-run'></a>
### `mainwp_auto_updates_sync_data_before_run`

* Method handle_cron_auto_updates()

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Usage Locations:**

- [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 104](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L104)

---

<a id='mainwp-before-edit-site-note'></a>
### `mainwp_before_edit_site_note`

* Action: mainwp_before_edit_site_note

Fires before the site note content in the Edit Note modal element.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2033](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2033)

---

<a id='mainwp-before-groups-table'></a>
### `mainwp_before_groups_table`

* Action: mainwp_before_groups_table

Fires before the Manage Groups table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 315](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L315)

---

<a id='mainwp-before-manage-sites-table'></a>
### `mainwp_before_manage_sites_table`

* Action: mainwp_before_manage_sites_table

Fires before the Manage Sites table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1073](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1073)

---

<a id='mainwp-before-save-sync-result'></a>
### `mainwp_before_save_sync_result`

* Filter: mainwp_before_save_sync_result

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

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 267](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L267)

---

<a id='mainwp-before-select-groups-list'></a>
### `mainwp_before_select_groups_list`

* Action: mainwp_before_select_groups_list

Fires before the Select Groups list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$groups` | `object` | Object containing groups info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 419](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L419)

---

<a id='mainwp-before-select-sites-filters'></a>
### `mainwp_before_select_sites_filters`

* Action: mainwp_before_select_sites_filters

Fires before the Select Sites box filters.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 190](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L190)

---

<a id='mainwp-before-select-sites-list'></a>
### `mainwp_before_select_sites_list`

* Action: mainwp_before_select_sites_list

Fires before the Select Sites list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 252](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L252)

---

<a id='mainwp-boilerplate-get-tokens'></a>
### `mainwp_boilerplate_get_tokens`

* This filter is documented in ../class/class-mainwp-notification-settings.php

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` |  |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 708](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L708)

---

<a id='mainwp-bulkpost-select-sites-settings'></a>
### `mainwp_bulkpost_select_sites_settings`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sites_settings` |  | 
`$post` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sites_settings` |  | 
`$post` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-check-site-result'></a>
### `mainwp_check_site_result`

* Method check_site()

Check to add site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$_POST` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-sites-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php), [line 26](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php#L26)

---

<a id='mainwp-child-site-info-widget-content'></a>
### `mainwp_child_site_info_widget_content`

* Filter: mainwp_child_site_info_widget_content

Filters the Child Info array for the Site Info widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$child_site_info` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-site-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php), [line 83](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php#L83)

---

<a id='mainwp-client-report-get-site-tokens'></a>
### `mainwp_client_report_get_site_tokens`

* Filter: mainwp_client_report_get_site_tokens

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

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 667](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L667)
- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 722](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L722)

---

<a id='mainwp-clients-overview-websites-widget-bottom'></a>
### `mainwp_clients_overview_websites_widget_bottom`

* Action: mainwp_clients_overview_websites_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-sites.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-sites.php), [line 149](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-sites.php#L149)

---

<a id='mainwp-clients-overview-websites-widget-title'></a>
### `mainwp_clients_overview_websites_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites', 'mainwp')` |  | 
`$client_info` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites', 'mainwp')` |  | 
`$client_info` |  |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-sites.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-sites.php), [line 117](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-sites.php#L117)

---

<a id='mainwp-clients-overview-websites-widget-top'></a>
### `mainwp_clients_overview_websites_widget_top`

* Actoin: mainwp_clients_overview_websites_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-sites.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-sites.php), [line 124](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-sites.php#L124)

---

<a id='mainwp-clients-website-client-tokens'></a>
### `mainwp_clients_website_client_tokens`

* Method get_website_client_tokens_data()

Get website client tokens.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_tokens` |  | 
`$websiteid` | `int` | Website ID.
`$clientid` |  |

**Usage Locations:**

- [class/class-mainwp-client-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-handler.php), [line 454](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-handler.php#L454)

---

<a id='mainwp-connect-sign-algo'></a>
### `mainwp_connect_sign_algo`

* Method get_connect_sign_algorithm().

Get supported sign algorithms.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$alg` |  | 
`$website` | `mixed` | The Website object.

**Usage Locations:**

- [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1541](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1541)

---

<a id='mainwp-connect-sites-allow-ports'></a>
### `mainwp_connect_sites_allow_ports`

* Method mainwp_testwp()

Test if Child Site can be reached.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$url` |  |

**Usage Locations:**

- [class/class-mainwp-post-site-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php), [line 236](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php#L236)

---

<a id='mainwp-connect-sites-not-allow-ports'></a>
### `mainwp_connect_sites_not_allow_ports`

* Method mainwp_testwp()

Test if Child Site can be reached.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$def_not_allow` |  | 
`$url` |  |

**Usage Locations:**

- [class/class-mainwp-post-site-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php), [line 236](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php#L236)

---

<a id='mainwp-connection-status-after-all-sites-list'></a>
### `mainwp_connection_status_after_all_sites_list`

* Action: mainwp_connection_status_after_all_sites_list

Fires after the list of all sites in the connection status widgets

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 277](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L277)

---

<a id='mainwp-connection-status-after-connected-sites-list'></a>
### `mainwp_connection_status_after_connected_sites_list`

* Action: mainwp_connection_status_after_connected_sites_list

Fires after the list of connected sites in the connection status widgets

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 303](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L303)

---

<a id='mainwp-connection-status-after-disconnected-sites-list'></a>
### `mainwp_connection_status_after_disconnected_sites_list`

* Action: mainwp_connection_status_after_disconnected_sites_list

Fires after the list of disconnected sites in the connection status widgets

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 329](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L329)

---

<a id='mainwp-connection-status-before-all-sites-list'></a>
### `mainwp_connection_status_before_all_sites_list`

* Action: mainwp_connection_status_before_all_sites_list

Fires before the list of all sites in the connection status widgets

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 264](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L264)

---

<a id='mainwp-connection-status-before-connected-sites-list'></a>
### `mainwp_connection_status_before_connected_sites_list`

* Action: mainwp_connection_status_before_connected_sites_list

Fires before the list of connected sites in the connection status widgets

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 290](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L290)

---

<a id='mainwp-connection-status-before-disconnected-sites-list'></a>
### `mainwp_connection_status_before_disconnected_sites_list`

* Action: mainwp_connection_status_before_disconnected_sites_list

Fires before the list of disconnected sites in the connection status widgets

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 316](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L316)

---

<a id='mainwp-connection-status-list-item-title'></a>
### `mainwp_connection_status_list_item_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$website->name` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->name` |  | 
`$website` |  |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 418](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L418)
- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 470](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L470)
- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 517](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L517)

---

<a id='mainwp-connection-status-list-item-title-url'></a>
### `mainwp_connection_status_list_item_title_url`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`'admin.php?page=managesites&dashboard=' . $website->id` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'admin.php?page=managesites&dashboard=' . $website->id` |  | 
`$website` |  |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 407](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L407)
- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 459](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L459)
- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 506](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L506)

---

<a id='mainwp-connection-status-widget-bottom'></a>
### `mainwp_connection_status_widget_bottom`

* Action: mainwp_connection_status_widget_bottom

Fires at the bottom of the Connection Status widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 103](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L103)

---

<a id='mainwp-connection-status-widget-footer-left'></a>
### `mainwp_connection_status_widget_footer_left`

* Action: mainwp_connection_status_widget_footer_left

Fires in the left column of the Connection status widget

**Changelog**

Version | Description
------- | -----------
`5.3` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 344](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L344)

---

<a id='mainwp-connection-status-widget-footer-right'></a>
### `mainwp_connection_status_widget_footer_right`

* Action: mainwp_connection_status_widget_footer_right

Fires in the right column of the Connection status widget

**Changelog**

Version | Description
------- | -----------
`5.3` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 356](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L356)

---

<a id='mainwp-connection-status-widget-title'></a>
### `mainwp_connection_status_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Connection Status', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Connection Status', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 156](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L156)

---

<a id='mainwp-connection-status-widget-top'></a>
### `mainwp_connection_status_widget_top`

* Action: mainwp_connection_status_widget_top

Fires at the top of the Connection Status widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-connection-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php), [line 199](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-connection-status.php#L199)

---

<a id='mainwp-cron-bulk-update-sites-limit'></a>
### `mainwp_cron_bulk_update_sites_limit`

* Method handle_cron_batch_updates()

MainWP Cron batch Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  |

**Usage Locations:**

- [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 104](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L104)
- [class/class-mainwp-cron-jobs-batch.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php), [line 95](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php#L95)

---

<a id='mainwp-curl-curlopt-resolve'></a>
### `mainwp_curl_curlopt_resolve`

* Fetch uptime urls.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$mo_url` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$mo_url` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 350](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L350)

---

<a id='mainwp-currentuserallowedaccessgroups'></a>
### `mainwp_currentuserallowedaccessgroups`

* Filter: mainwp_currentuserallowedaccessgroups

Filters allowed groups for the current user.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'all'` |  |

**Usage Locations:**

- [class/class-mainwp-db.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php), [line 1963](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php#L1963)

---

<a id='mainwp-custom-post-types-get-post-connections'></a>
### `mainwp_custom_post_types_get_post_connections`

* Method posts_search_handler()

Post page search handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$child_post_ids` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1282](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1282)

---

<a id='mainwp-delete-key-file'></a>
### `mainwp_delete_key_file`

* Method update_compatible_site_api_key

Encrypt data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key_file` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-utility.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php), [line 607](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php#L607)

---

<a id='mainwp-delete-site'></a>
### `mainwp_delete_site`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  |

**Usage Locations:**

- [class/class-mainwp-hooks.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-hooks.php), [line 409](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-hooks.php#L409)
- [pages/page-mainwp-extensions-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php), [line 1045](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php#L1045)
- [pages/page-mainwp-manage-sites-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php), [line 453](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php#L453)

---

<a id='mainwp-extension-sites-edit-tablerow'></a>
### `mainwp_extension_sites_edit_tablerow`

* Method render_edit_site()

Render individual Child Site Edit sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 831](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L831)

---

<a id='mainwp-fetch-url-authed'></a>
### `mainwp_fetch_url_authed`

* Fires immediately after fetch url action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website.
`$information` | `array` | information result data.
`$what` | `string` | action.
`$params` | `array` | params input array.
`$others` | `array` | others input array.

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

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 1201](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L1201)

---

<a id='mainwp-getwebsite-by-id'></a>
### `mainwp_getwebsite_by_id`

* Get sites by website ID.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website_id` | `int` | User ID.
`$selectGroups` | `bool` | Select groups.
`$extra_view` | `array` | get extra option fields.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website_id` | `int` | User ID.
`$selectGroups` | `bool` | Select groups.
`$extra_view` | `array` | get extra option fields.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 60](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L60)

---

<a id='mainwp-getwebsiteoptions'></a>
### `mainwp_getwebsiteoptions`

* Method get_website_options().

Get the website options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `object\|int` | website object or ID.
`$options` | `string\|array` | Options name.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L91)

---

<a id='mainwp-html-regression-largest-change-scope'></a>
### `mainwp_html_regression_largest_change_scope`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$website->id` |  | 
`true` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->id` |  | 
`true` |  |

**Usage Locations:**

- [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 58](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L58)

---

<a id='mainwp-manage-sites-action'></a>
### `mainwp_manage_sites_action`

* Action: mainwp_manage_sites_action

Adds custom manage sites action item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `array` | Array containing website data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1881](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1881)
- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 2295](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L2295)

---

<a id='mainwp-manage-sites-edit'></a>
### `mainwp_manage_sites_edit`

* Edit site

Fires on the Edit child site page and allows user to hook in new site options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 1391](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L1391)
- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1056](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1056)

---

<a id='mainwp-manage-sites-email-settings'></a>
### `mainwp_manage_sites_email_settings`

* Action: mainwp_manage_sites_email_settings

Fires on the Email Settigns page at bottom.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the website info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 1824](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L1824)

---

<a id='mainwp-manage-sites-force-use-ipv4'></a>
### `mainwp_manage_sites_force_use_ipv4`

* Method check_site()

Check to add site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`null` |  | 
`$url` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 2018](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L2018)
- [class/class-mainwp-post-site-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php), [line 236](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php#L236)
- [pages/page-mainwp-manage-sites-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php), [line 26](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php#L26)

---

<a id='mainwp-manage-sites-navigation-items'></a>
### `mainwp_manage_sites_navigation_items`

* Method render_managesites_header()

Render manage sites header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$renderItems` |  | 
`$site_id` | `int` | Site id.
`$shownPage` | `string` | Current Page.

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 316](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L316)

---

<a id='mainwp-manage-sites-optimize-loading'></a>
### `mainwp_manage_sites_optimize_loading`

* Method render_all_sites()

Render manage sites content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1` |  | 
`'manage-sites'` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1713](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1713)
- [pages/page-mainwp-monitoring.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-monitoring.php), [line 272](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-monitoring.php#L272)

---

<a id='mainwp-manage-sites-table-columns-defs'></a>
### `mainwp_manage_sites_table_columns_defs`

* Display the table.

Source: [../sources/mainwp-dashboard/class/class-mainwp-monitoring-sites-list-table.php](class/class-mainwp-monitoring-sites-list-table.php), [line 644](class/class-mainwp-monitoring-sites-list-table.php#L644-L917)

**Usage Locations:**

- [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 336](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L336)
- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1044](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1044)
- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 644](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L644)

---

<a id='mainwp-managesite-backup'></a>
### `mainwp_managesite_backup`

* Method backup()

Backup Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`array('type' => $pType)` |  | 
`$information` |  |

**Usage Locations:**

- [class/class-mainwp-backup-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-backup-handler.php), [line 753](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-backup-handler.php#L753)

---

<a id='mainwp-managesite-schedule-backup'></a>
### `mainwp_managesite_schedule_backup`

* Execute the backup task.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`array('type' => $task->type)` |  | 
`$_backup_result` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`array('type' => $task->type)` |  | 
`$_backup_result` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php), [line 282](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php#L282)

---

<a id='mainwp-managesites-bulk-actions'></a>
### `mainwp_managesites_bulk_actions`

* Filter: mainwp_managesites_bulk_actions

Filters bulk actions on the Manage Sites page. Allows user to hook in new actions or remove default ones.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$actions` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 504](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L504)

---

<a id='mainwp-managesites-getbackuplink'></a>
### `mainwp_managesites_getbackuplink`

* Filter: mainwp_managesites_getbackuplink

Filters the link for the last backup item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$item['id']` |  | 
`$lastBackup` | `string` | Last backup timestamp for the child site.
`$backup_method` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 104](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L104)

---

<a id='mainwp-managesites-tabletop'></a>
### `mainwp_managesites_tabletop`

* Action: mainwp_managesites_tabletop

Fires at the table top on the Manage Sites and Monitoring page.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1176](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1176)

---

<a id='mainwp-module-log-cron-tracking'></a>
### `mainwp_module_log_cron_tracking`

* Log handler.

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

**Usage Locations:**

- [modules/logs/classes/class-log.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log.php), [line 36](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log.php#L36)

---

<a id='mainwp-module-log-data'></a>
### `mainwp_module_log_data`

* Log handler

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`compact('connector', 'message', 'args', 'site_id', 'context', 'action', 'state', 'user_id')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`compact('connector', 'message', 'args', 'site_id', 'context', 'action', 'state', 'user_id')` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-connector.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connector.php), [line 81](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connector.php#L81)

---

<a id='mainwp-monitoringsites-bulk-actions'></a>
### `mainwp_monitoringsites_bulk_actions`

* Filter: mainwp_monitoringsites_bulk_actions

Filters bulk actions on the Monitoring Sites page. Allows user to hook in new actions or remove default ones.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$actions` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 295](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L295)

---

<a id='mainwp-open-site-allow-vars'></a>
### `mainwp_open_site_allow_vars`

* Child Site Dashboard Link redirect handler.

This method checks to see if the current user is allow to access the
Child Site, then grabs the websiteid, location, openurl & passes it onto
either open_site_location or open_site methods.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allow_vars` |  |

**Usage Locations:**

- [pages/page-mainwp-site-open.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-site-open.php), [line 27](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-site-open.php#L27)

---

<a id='mainwp-open-site-login-required-params'></a>
### `mainwp_open_site_login_required_params`

* Method get_get_data_authed()

Get authorized $_GET data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$params` |  | 
`$website` | `mixed` | Child Site data.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 525](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L525)

---

<a id='mainwp-posting-selected-groups'></a>
### `mainwp_posting_selected_groups`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_groups` |  | 
`$id` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-postprocess-backup-sites-feedback'></a>
### `mainwp_postprocess_backup_sites_feedback`

* Method  backup_site()

Backup Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$unique` |  |

**Usage Locations:**

- [class/class-mainwp-backup-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-backup-handler.php), [line 28](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-backup-handler.php#L28)

---

<a id='mainwp-pro-reports-get-site-tokens'></a>
### `mainwp_pro_reports_get_site_tokens`

* Filter: mainwp_pro_reports_get_site_tokens

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

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 648](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L648)
- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 715](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L715)

---

<a id='mainwp-quick-sites-shortcut'></a>
### `mainwp_quick_sites_shortcut`

* Action: mainwp_quick_sites_shortcut

Adds a new shortcut item in the Quick Sites Shortcuts sidebar menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `array` | Array containing the child site data.<br><br>Suggested HTML markup:<br><br><a class="item" href="your custom URL"><br>  <i class="your custom icon"></i><br>  Your custom label  text<br></a>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 738](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L738)

---

<a id='mainwp-rest-pre-insert-site-item'></a>
### `mainwp_rest_pre_insert_site_item`

* Filters an object before it is inserted via the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item_fields` | `array` | Site data.
`$request` | `\WP_REST_Request` | Request object.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item_fields` | `array` | Site data.
`$request` | `\WP_REST_Request` | Request object.

**Changelog**

Version | Description
------- | -----------
`5.2` |

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2092](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2092)

---

<a id='mainwp-rest-pre-update-site-item'></a>
### `mainwp_rest_pre_update_site_item`

* Filters an object before it is inserted via the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 
`$request` | `\WP_REST_Request` | Request object.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 
`$request` | `\WP_REST_Request` | Request object.

**Changelog**

Version | Description
------- | -----------
`5.2` |

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2139](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2139)

---

<a id='mainwp-rest-routes-sites-controller-filter-allowed-fields-by-context'></a>
### `mainwp_rest_routes_sites_controller_filter_allowed_fields_by_context`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`'simple_view'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`'simple_view'` |  |

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-clients-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-clients-controller.php), [line 497](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-clients-controller.php#L497)
- [includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php), [line 370](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php#L370)
- [includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 792](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L792)
- [includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 828](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L828)
- [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 509](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L509)

---

<a id='mainwp-rest-routes-sites-controller-get-allowed-fields-by-context'></a>
### `mainwp_rest_routes_sites_controller_get_allowed_fields_by_context`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`'view'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'view'` |  |

**Usage Locations:**

- [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 545](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L545)

---

<a id='mainwp-select-sites-box'></a>
### `mainwp_select_sites_box`

* Render settings

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

**Usage Locations:**

- [modules/cost-tracker/pages/page-cost-tracker-add-edit.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-add-edit.php), [line 85](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-add-edit.php#L85)

---

<a id='mainwp-site-actions-saved-days-number'></a>
### `mainwp_site_actions_saved_days_number`

* Method sync_site()

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`30` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`30` |  |

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 62](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L62)

---

<a id='mainwp-site-added'></a>
### `mainwp_site_added`

* Fires immediately after a new website is added.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$information` | `array` | The array of information data .

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$information` | `array` | The array of information data .

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 2257](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L2257)

---

<a id='mainwp-site-changes-table-pages-length'></a>
### `mainwp_site_changes_table_pages_length`

* Display the table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pages_length` |  | 
`$this->table_id_prefix` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pages_length` |  | 
`$this->table_id_prefix` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-events-list-table.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-events-list-table.php), [line 524](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-events-list-table.php#L524)

---

<a id='mainwp-site-deleted'></a>
### `mainwp_site_deleted`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-sites-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php), [line 462](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php#L462)

---

<a id='mainwp-site-health-monitoring-email-footer'></a>
### `mainwp_site_health_monitoring_email_footer`

* Site Health Monitoring Email Footer

Fires at the bottom of the site health monitoring email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-site-health-monitoring-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-site-health-monitoring-email.php), [line 118](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-site-health-monitoring-email.php#L118)

---

<a id='mainwp-site-health-monitoring-email-header'></a>
### `mainwp_site_health_monitoring_email_header`

* Site Health Monitoring Email Header

Fires at the top of the site health monitoring email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-site-health-monitoring-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-site-health-monitoring-email.php), [line 31](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-site-health-monitoring-email.php#L31)

---

<a id='mainwp-site-info-table-bottom'></a>
### `mainwp_site_info_table_bottom`

* Action: mainwp_site_info_table_bottom

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-site-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php), [line 179](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php#L179)

---

<a id='mainwp-site-info-table-top'></a>
### `mainwp_site_info_table_top`

* Action: mainwp_site_info_table_top

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-site-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php), [line 146](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php#L146)

---

<a id='mainwp-site-info-widget-bottom'></a>
### `mainwp_site_info_widget_bottom`

* Action: mainwp_site_info_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-site-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php), [line 194](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php#L194)

---

<a id='mainwp-site-info-widget-title'></a>
### `mainwp_site_info_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Site Info', 'mainwp')` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Site Info', 'mainwp')` |  | 
`$website` |  |

**Usage Locations:**

- [widgets/widget-mainwp-site-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php), [line 116](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php#L116)

---

<a id='mainwp-site-info-widget-top'></a>
### `mainwp_site_info_widget_top`

* Actoin: mainwp_site_info_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-site-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php), [line 124](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-info.php#L124)

---

<a id='mainwp-site-reconnected'></a>
### `mainwp_site_reconnected`

* Fires immediately after reconnect website.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$success` |  | 
`$_error` |  |

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

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 1995](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L1995)

---

<a id='mainwp-site-suspended'></a>
### `mainwp_site_suspended`

* Fires immediately after website suspended/unsuspend.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$suspended` | `int` | The new suspended value.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$suspended` | `int` | The new suspended value.

**Changelog**

Version | Description
------- | -----------
`4.5.2` |

**Usage Locations:**

- [class/class-mainwp-post-site-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php), [line 470](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-site-handler.php#L470)
- [includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 1458](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L1458)
- [includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 1498](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L1498)
- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 2090](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L2090)

---

<a id='mainwp-site-sync'></a>
### `mainwp_site_sync`

* Action: mainwp_site_sync

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

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 596](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L596)

---

<a id='mainwp-site-synced'></a>
### `mainwp_site_synced`

* Action: mainwp_site_synced

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

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 581](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L581)

---

<a id='mainwp-site-tag-action'></a>
### `mainwp_site_tag_action`

* Fires after a new sites tag has been created.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$group` | `object` | tag created.
`'updated'` |  | 
`$data` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$group` | `object` | tag created.
`'updated'` |  | 
`$data` |  |

**Usage Locations:**

- [class/class-mainwp-db-common.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-common.php), [line 585](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-common.php#L585)
- [class/class-mainwp-db-common.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-common.php), [line 664](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-common.php#L664)
- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 584](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L584)

---

<a id='mainwp-site-updated'></a>
### `mainwp_site_updated`

* Update site

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

**Usage Locations:**

- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 2078](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L2078)

---

<a id='mainwp-sites-table-features'></a>
### `mainwp_sites_table_features`

* Filter: mainwp_sites_table_features

Filter the Monitoring table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1136](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1136)

---

<a id='mainwp-sitestable-website'></a>
### `mainwp_sitestable_website`

* Get table rows.

Optimize for shared hosting or big networks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$this->userExtension` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1554](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1554)
- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1976](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1976)

---

<a id='mainwp-staging-current-user-sites-view'></a>
### `mainwp_staging_current_user_sites_view`

* Method get_select_staging_view_sites()

Get staging options sites view for current users.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$view` |  |

**Usage Locations:**

- [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1655](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1655)

---

<a id='mainwp-sync-extensions-options'></a>
### `mainwp_sync_extensions_options`

* Method render_sync_exts_settings()

Render sync extension settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sync_extensions_options` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 566](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L566)

---

<a id='mainwp-sync-others-data'></a>
### `mainwp_sync_others_data`

* Filter: mainwp_sync_others_data

Filters additional data in the sync request. Allows extensions or 3rd party plugins to hook data to the sync request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$othersData` |  | 
`$pWebsite` | `object` | Object contaning child site data.

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 152](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L152)

---

<a id='mainwp-sync-popup-content'></a>
### `mainwp_sync_popup_content`

* Method render_footer_content()

Render footer content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  |

**Usage Locations:**

- [class/class-mainwp-system-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php), [line 996](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php#L996)

---

<a id='mainwp-sync-site-after-sync-result'></a>
### `mainwp_sync_site_after_sync_result`

* Method sync_information_array()

Grab all Child Site Information.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$error` | `bool` | True\|False.
`$pWebsite` | `object` | The website object.
`$information` | `array` | Array contaning information returned from child site.

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 221](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L221)

---

<a id='mainwp-sync-site-log-install-actions'></a>
### `mainwp_sync_site_log_install_actions`

* Method sync_log_site_actions().

Sync site actions data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website data.
`$record_mapping` |  | 
`$object_id` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-manager.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-manager.php), [line 239](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-manager.php#L239)

---

<a id='mainwp-synced-all-sites'></a>
### `mainwp_synced_all_sites`

* Method cron_updates_check()

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Usage Locations:**

- [class/class-mainwp-post-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-handler.php), [line 605](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-handler.php#L605)
- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 375](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L375)

---

<a id='mainwp-updates-pergroup-after-abandoned-plugins'></a>
### `mainwp_updates_pergroup_after_abandoned_plugins`

* Action: mainwp_updates_pergroup_after_abandoned_plugins

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1566](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1566)

---

<a id='mainwp-updates-pergroup-after-abandoned-themes'></a>
### `mainwp_updates_pergroup_after_abandoned_themes`

* Action: mainwp_updates_pergroup_after_abandoned_themes

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1717](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1717)

---

<a id='mainwp-updates-pergroup-after-plugin-updates'></a>
### `mainwp_updates_pergroup_after_plugin_updates`

* Action: mainwp_updates_pergroup_after_plugin_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1062](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1062)

---

<a id='mainwp-updates-pergroup-after-theme-updates'></a>
### `mainwp_updates_pergroup_after_theme_updates`

* Action: mainwp_updates_pergroup_after_theme_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1235](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1235)

---

<a id='mainwp-updates-pergroup-after-translation-updates'></a>
### `mainwp_updates_pergroup_after_translation_updates`

* Action: mainwp_updates_pergroup_after_translation_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1406](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1406)

---

<a id='mainwp-updates-pergroup-after-wp-updates'></a>
### `mainwp_updates_pergroup_after_wp_updates`

* Action: mainwp_updates_pergroup_after_wp_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 889](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L889)

---

<a id='mainwp-updates-pergroup-before-abandoned-plugins'></a>
### `mainwp_updates_pergroup_before_abandoned_plugins`

* Action: mainwp_updates_pergroup_before_abandoned_plugins

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1550](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1550)

---

<a id='mainwp-updates-pergroup-before-abandoned-themes'></a>
### `mainwp_updates_pergroup_before_abandoned_themes`

* Action: mainwp_updates_pergroup_before_abandoned_themes

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1701](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1701)

---

<a id='mainwp-updates-pergroup-before-plugin-updates'></a>
### `mainwp_updates_pergroup_before_plugin_updates`

* Action: mainwp_updates_pergroup_before_plugin_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1044](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1044)

---

<a id='mainwp-updates-pergroup-before-theme-updates'></a>
### `mainwp_updates_pergroup_before_theme_updates`

* Action: mainwp_updates_pergroup_before_theme_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1217](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1217)

---

<a id='mainwp-updates-pergroup-before-translation-updates'></a>
### `mainwp_updates_pergroup_before_translation_updates`

* Action: mainwp_updates_pergroup_before_translation_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1388](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1388)

---

<a id='mainwp-updates-pergroup-before-wp-updates'></a>
### `mainwp_updates_pergroup_before_wp_updates`

* Action: mainwp_updates_pergroup_before_wp_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 874](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L874)
- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 904](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L904)

---

<a id='mainwp-updates-persite-after-abandoned-plugins'></a>
### `mainwp_updates_persite_after_abandoned_plugins`

* Action: mainwp_updates_persite_after_abandoned_plugins

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1534](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1534)

---

<a id='mainwp-updates-persite-after-abandoned-themes'></a>
### `mainwp_updates_persite_after_abandoned_themes`

* Action: mainwp_updates_persite_after_abandoned_themes

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1685](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1685)

---

<a id='mainwp-updates-persite-after-plugin-updates'></a>
### `mainwp_updates_persite_after_plugin_updates`

* Action: mainwp_updates_persite_after_plugin_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1026](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1026)

---

<a id='mainwp-updates-persite-after-theme-updates'></a>
### `mainwp_updates_persite_after_theme_updates`

* Action: mainwp_updates_persite_after_theme_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1199](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1199)

---

<a id='mainwp-updates-persite-after-translation-updates'></a>
### `mainwp_updates_persite_after_translation_updates`

* Action: mainwp_updates_persite_after_translation_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1370](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1370)

---

<a id='mainwp-updates-persite-after-wp-updates'></a>
### `mainwp_updates_persite_after_wp_updates`

* Action: mainwp_updates_persite_after_wp_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 920](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L920)

---

<a id='mainwp-updates-persite-before-abandoned-plugins'></a>
### `mainwp_updates_persite_before_abandoned_plugins`

* Action: mainwp_updates_persite_before_abandoned_plugins

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1518](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1518)

---

<a id='mainwp-updates-persite-before-abandoned-themes'></a>
### `mainwp_updates_persite_before_abandoned_themes`

* Action: mainwp_updates_persite_before_abandoned_themes

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1669](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1669)

---

<a id='mainwp-updates-persite-before-plugin-updates'></a>
### `mainwp_updates_persite_before_plugin_updates`

* Action: mainwp_updates_persite_before_plugin_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1008](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1008)

---

<a id='mainwp-updates-persite-before-theme-updates'></a>
### `mainwp_updates_persite_before_theme_updates`

* Action: mainwp_updates_persite_before_theme_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1181](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1181)

---

<a id='mainwp-updates-persite-before-translation-updates'></a>
### `mainwp_updates_persite_before_translation_updates`

* Action: mainwp_updates_persite_before_translation_updates

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

**Usage Locations:**

- [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1352](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1352)

---

<a id='mainwp-updatescheck-sendmail-for-each-auto-sync-finished'></a>
### `mainwp_updatescheck_sendmail_for_each_auto_sync_finished`

* Method cron_updates_check()

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 375](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L375)

---

<a id='mainwp-updatewebsiteoptions'></a>
### `mainwp_updatewebsiteoptions`

* Method update_website_option().

Update the website option.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `object\|int` | website object or ID.
`$opt_name` | `string` | website.
`$opt_value` | `string` | website.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 78](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L78)

---

<a id='mainwp-website-before-updated'></a>
### `mainwp_website_before_updated`

* Action: mainwp_website_before_updated

Fires before the child site update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.
`$type` | `string` | Type parameter.
`$list` | `string` | List parameter.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 1175](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L1175)

---

<a id='mainwp-website-updated'></a>
### `mainwp_website_updated`

* Action: mainwp_website_updated

Fires after the child site update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.
`$type` | `string` | Type parameter.
`$list` | `string` | List parameter.
`$information` | `array` | Array containing the information fetched from the child site.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 1224](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L1224)

---

<a id='mainwp-widget-site-actions-limit-number'></a>
### `mainwp_widget_site_actions_limit_number`

* Method mainwp_rest_api_non_mainwp_changes_callback()

Callback function for managing the response to API requests made for the endpoint: non-mainwp-changes
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/site/non-mainwp-changes
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10000` |  |

**Usage Locations:**

- [includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 3448](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L3448)
- [includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 3513](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L3513)
- [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 75](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L75)

---


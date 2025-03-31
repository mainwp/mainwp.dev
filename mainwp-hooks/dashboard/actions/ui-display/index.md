# UI & Display Actions

Hooks for modifying the Dashboard UI, widgets, menus, and display elements.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`after_mainwp_menu`](#after-mainwp-menu) - Action: after_mainwp_menu
- [`before_mainwp_menu`](#before-mainwp-menu) - Action: before_mainwp_menu
- [`deprecated_hook_run`](#deprecated-hook-run) - Display a deprecated notice for old hooks.
- [`error_log_mainwp_lines`](#error-log-mainwp-lines) - Filter: error_log_mainwp_lines
- [`mainwp-getmetaboxes`](#mainwp-getmetaboxes) - Method apply_filter()
- [`mainwp-sitestable-getcolumns`](#mainwp-sitestable-getcolumns) - Filter is being replaced with mainwp_sitestable_getcolumns
- [`mainwp-sitestable-item`](#mainwp-sitestable-item) - Filter is being replaced with mainwp_sitestable_item
- [`mainwp-sitestable-prepared-items`](#mainwp-sitestable-prepared-items) - Action is being replaced with mainwp_sitestable_prepared_items
- [`mainwp-widgets-screen-options`](#mainwp-widgets-screen-options) - Method render_screen_options()
- [`mainwp_added_extension_menu`](#mainwp-added-extension-menu) - Adds Extension to the navigation menu
- [`mainwp_admin_menu`](#mainwp-admin-menu) - Action: mainwp_admin_menu
- [`mainwp_admin_menu_sub`](#mainwp-admin-menu-sub) - Action: mainwp_admin_menu_sub
- [`mainwp_after_cron_jobs_table`](#mainwp-after-cron-jobs-table) - Action: mainwp_after_cron_jobs_table
- [`mainwp_after_error_log_table`](#mainwp-after-error-log-table) - Action: mainwp_after_error_log_table
- [`mainwp_after_overview_widgets`](#mainwp-after-overview-widgets) - Action: 'mainwp_after_overview_widgets'
- [`mainwp_after_server_info_table`](#mainwp-after-server-info-table) - Action: mainwp_after_server_info_table
- [`mainwp_after_upload_custom_icon`](#mainwp-after-upload-custom-icon) - Action: mainwp_after_upload_custom_icon
- [`mainwp_all_disablemenuitems`](#mainwp-all-disablemenuitems) - Method admin_footer()
- [`mainwp_before_cron_jobs_table`](#mainwp-before-cron-jobs-table) - Action: mainwp_before_cron_jobs_table
- [`mainwp_before_error_log_table`](#mainwp-before-error-log-table) - Action: mainwp_before_error_log_table
- [`mainwp_before_log_data`](#mainwp-before-log-data) - Method log_to_db()
- [`mainwp_before_overview_widgets`](#mainwp-before-overview-widgets) - Action: mainwp_before_overview_widgets
- [`mainwp_before_server_info_table`](#mainwp-before-server-info-table) - Action: mainwp_before_server_info_table
- [`mainwp_before_upload_custom_icon`](#mainwp-before-upload-custom-icon) - Action: mainwp_after_upload_custom_icon
- [`mainwp_compact_action`](#mainwp-compact-action) - Create compact logs and erase records from the database.
- [`mainwp_cost_summary_getmetaboxes`](#mainwp-cost-summary-getmetaboxes) - Method add_meta_boxes()
- [`mainwp_cron_jobs_list`](#mainwp-cron-jobs-list) - Action: mainwp_cron_jobs_list
- [`mainwp_cron_jobs_table_features`](#mainwp-cron-jobs-table-features) - Filter: mainwp_cron_jobs_table_features
- [`mainwp_disablemenuitems`](#mainwp-disablemenuitems) - Method init()
- [`mainwp_do_widget_boxes_sorted`](#mainwp-do-widget-boxes-sorted) - Method do_widget_boxes()
- [`mainwp_extensions_top_header_after_tab`](#mainwp-extensions-top-header-after-tab) - Method render_header()
- [`mainwp_get_started_widget_bottom`](#mainwp-get-started-widget-bottom) - Action: mainwp_get_started_widget_bottom
- [`mainwp_get_started_widget_title`](#mainwp-get-started-widget-title) - *Arguments*
- [`mainwp_get_started_widget_top`](#mainwp-get-started-widget-top) - Action: mainwp_get_started_widget_top
- [`mainwp_getmetaboxes`](#mainwp-getmetaboxes) - Method on_load_page_dashboard()
- [`mainwp_init_primary_menu_items`](#mainwp-init-primary-menu-items) - Method init_mainwp_menu_items()
- [`mainwp_insights_getmetaboxes`](#mainwp-insights-getmetaboxes) - Method add_meta_boxes()
- [`mainwp_is_disable_menu_item`](#mainwp-is-disable-menu-item) - Method is_disable_menu_item
- [`mainwp_log_do_to_db`](#mainwp-log-do-to-db) - Method log_to_db()
- [`mainwp_log_to_db_data`](#mainwp-log-to-db-data) - Method log_to_db()
- [`mainwp_log_to_db_priority`](#mainwp-log-to-db-priority) - Method log_to_db()
- [`mainwp_logs_manage_table_bottom`](#mainwp-logs-manage-table-bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_manage_table_top`](#mainwp-logs-manage-table-top) - Action: mainwp_logs_manage_table_top
- [`mainwp_logs_widget_bottom`](#mainwp-logs-widget-bottom) - Action: mainwp_logs_widget_bottom
- [`mainwp_logs_widget_top`](#mainwp-logs-widget-top) - Action: mainwp_logs_widget_top
- [`mainwp_main_menu`](#mainwp-main-menu) - Filter: mainwp_main_menu
- [`mainwp_main_menu_disable_menu_items`](#mainwp-main-menu-disable-menu-items) - Filter: mainwp_main_menu_disable_menu_items
- [`mainwp_main_menu_submenu`](#mainwp-main-menu-submenu) - Filter: mainwp_main_menu_submenu
- [`mainwp_menu_extensions_left_menu`](#mainwp-menu-extensions-left-menu) - Method init_extensions_menu()
- [`mainwp_menu_logo_alt`](#mainwp-menu-logo-alt) - *Arguments*
- [`mainwp_menu_logo_href`](#mainwp-menu-logo-href) - *Arguments*
- [`mainwp_menu_logo_src`](#mainwp-menu-logo-src) - *Arguments*
- [`mainwp_module_cost_tracker_actions_bar_left`](#mainwp-module-cost-tracker-actions-bar-left) - Render Actions Bar
- [`mainwp_module_cost_tracker_actions_bar_right`](#mainwp-module-cost-tracker-actions-bar-right) - Render Actions Bar
- [`mainwp_module_cost_tracker_monthly_renewals_widget_title`](#mainwp-module-cost-tracker-monthly-renewals-widget-title) - *Arguments*
- [`mainwp_module_cost_tracker_summary_enabled_widgets`](#mainwp-module-cost-tracker-summary-enabled-widgets) - Unset unwanted Widgets
- [`mainwp_module_cost_tracker_summary_screen_options_bottom`](#mainwp-module-cost-tracker-summary-screen-options-bottom) - Action: mainwp_module_cost_tracker_summary_screen_options_bottom
- [`mainwp_module_cost_tracker_summary_screen_options_top`](#mainwp-module-cost-tracker-summary-screen-options-top) - Action: mainwp_module_cost_tracker_summary_screen_options_top
- [`mainwp_module_cost_tracker_summary_widgets_screen_options`](#mainwp-module-cost-tracker-summary-widgets-screen-options) - Filter: mainwp_module_cost_tracker_summary_widgets_screen_options
- [`mainwp_module_cost_tracker_upcoming_renewals_widget_title`](#mainwp-module-cost-tracker-upcoming-renewals-widget-title) - *Arguments*
- [`mainwp_module_cost_tracker_widget_bottom`](#mainwp-module-cost-tracker-widget-bottom) - Action: mainwp_module_cost_tracker_widget_bottom
- [`mainwp_module_cost_tracker_widget_top`](#mainwp-module-cost-tracker-widget-top) - Action: mainwp_module_cost_tracker_widget_top
- [`mainwp_module_cost_tracker_yearly_renewals_widget_title`](#mainwp-module-cost-tracker-yearly-renewals-widget-title) - *Arguments*
- [`mainwp_module_dashboard_insights_help_item`](#mainwp-module-dashboard-insights-help-item) - Action: mainwp_module_dashboard_insights_help_item
- [`mainwp_module_log_overview_enabled_widgets`](#mainwp-module-log-overview-enabled-widgets) - Unset unwanted Widgets
- [`mainwp_module_log_overview_screen_options_bottom`](#mainwp-module-log-overview-screen-options-bottom) - Action: mainwp_module_log_overview_screen_options_bottom
- [`mainwp_module_log_overview_screen_options_top`](#mainwp-module-log-overview-screen-options-top) - Action: mainwp_module_log_overview_screen_options_top
- [`mainwp_module_log_widgets_screen_options`](#mainwp-module-log-widgets-screen-options) - Filter: mainwp_module_log_widgets_screen_options
- [`mainwp_non_mainwp_changes_table_bottom`](#mainwp-non-mainwp-changes-table-bottom) - Action: mainwp_non_mainwp_changes_table_bottom
- [`mainwp_non_mainwp_changes_table_top`](#mainwp-non-mainwp-changes-table-top) - Action: mainwp_non_mainwp_changes_table_top
- [`mainwp_non_mainwp_changes_widget_bottom`](#mainwp-non-mainwp-changes-widget-bottom) - Action: mainwp_non_mainwp_changes_widget_bottom
- [`mainwp_non_mainwp_changes_widget_title`](#mainwp-non-mainwp-changes-widget-title) - *Arguments*
- [`mainwp_non_mainwp_changes_widget_top`](#mainwp-non-mainwp-changes-widget-top) - Actoin: mainwp_non_mainwp_changes_widget_top
- [`mainwp_notes_widget_bottom`](#mainwp-notes-widget-bottom) - Action: mainwp_notes_widget_bottom
- [`mainwp_notes_widget_title`](#mainwp-notes-widget-title) - *Arguments*
- [`mainwp_notes_widget_top`](#mainwp-notes-widget-top) - Action: mainwp_notes_widget_top
- [`mainwp_overview_enabled_widgets`](#mainwp-overview-enabled-widgets) - Unset unwanted Widgets
- [`mainwp_overview_screen_options_bottom`](#mainwp-overview-screen-options-bottom) - Action: mainwp_overview_screen_options_bottom
- [`mainwp_overview_screen_options_top`](#mainwp-overview-screen-options-top) - Action: mainwp_overview_screen_options_top
- [`mainwp_removed_extension_menu`](#mainwp-removed-extension-menu) - Remove Extensions menu from MainWP Menu.
- [`mainwp_reset_admin_pass_modal_bottom`](#mainwp-reset-admin-pass-modal-bottom) - Action: mainwp_reset_admin_pass_modal_bottom
- [`mainwp_reset_admin_pass_modal_top`](#mainwp-reset-admin-pass-modal-top) - Action: mainwp_reset_admin_pass_modal_top
- [`mainwp_screen_options_modal_bottom`](#mainwp-screen-options-modal-bottom) - Action: mainwp_screen_options_modal_bottom
- [`mainwp_screen_options_modal_top`](#mainwp-screen-options-modal-top) - Action: mainwp_screen_options_modal_top
- [`mainwp_screen_options_pulse_control`](#mainwp-screen-options-pulse-control) - Method render_header_actions()
- [`mainwp_sitestable_display_row_columns`](#mainwp-sitestable-display-row-columns) - Get table rows.
- [`mainwp_sitestable_getcolumns`](#mainwp-sitestable-getcolumns) - Filter: mainwp_sitestable_getcolumns
- [`mainwp_sitestable_item`](#mainwp-sitestable-item) - Filter: mainwp_sitestable_item
- [`mainwp_sitestable_prepare_extra_view`](#mainwp-sitestable-prepare-extra-view) - Prepare the items to be listed.
- [`mainwp_sitestable_prepared_items`](#mainwp-sitestable-prepared-items) - Action: mainwp_sitestable_prepared_items
- [`mainwp_sitestable_render_column`](#mainwp-sitestable-render-column) - Columns for a single row.
- [`mainwp_ui_use_wp_calendar`](#mainwp-ui-use-wp-calendar) - Filter: mainwp_ui_use_wp_calendar
- [`mainwp_widget_boxes_show_widgets`](#mainwp-widget-boxes-show-widgets) - Method do_widget_boxes()
- [`mainwp_widgets_chart_date_format`](#mainwp-widgets-chart-date-format) - Prepare response time for ui chart data.
- [`mainwp_widgets_screen_options`](#mainwp-widgets-screen-options) - Filter: mainwp_widgets_screen_options

---

## Hook Details

<a id='after-mainwp-menu'></a>
### `after_mainwp_menu`

* Action: after_mainwp_menu

Fires after the main navigation element.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 1271](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L1271)
- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 951](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L951)

---

<a id='before-mainwp-menu'></a>
### `before_mainwp_menu`

* Action: before_mainwp_menu

Fires before the main navigation element.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 1073](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L1073)
- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 709](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L709)

---

<a id='deprecated-hook-run'></a>
### `deprecated_hook_run`

* Display a deprecated notice for old hooks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$old_hook` | `string` | Old hook.
`$new_hook` | `string` | New hook.
`$version` |  | 
`$message` | `string` | message.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$old_hook` | `string` | Old hook.
`$new_hook` | `string` | New hook.
`$version` |  | 
`$message` | `string` | message.

**Usage Locations:**

- [class/class-mainwp-deprecated-hooks.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-deprecated-hooks.php), [line 152](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-deprecated-hooks.php#L152)

---

<a id='error-log-mainwp-lines'></a>
### `error_log_mainwp_lines`

* Filter: error_log_mainwp_lines

Limits the number of error log records to be displayed. Default value, 50.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1543](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1543)

---

<a id='mainwp-getmetaboxes'></a>
### `mainwp-getmetaboxes`

* Method apply_filter()

Apply filter

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($value)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getmetaboxes'` |  |

**Usage Locations:**

- [class/class-mainwp-system-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php), [line 188](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php#L188)

---

<a id='mainwp-sitestable-getcolumns'></a>
### `mainwp-sitestable-getcolumns`

* Filter is being replaced with mainwp_sitestable_getcolumns

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($columns, $columns)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_getcolumns'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($columns, $columns)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_getcolumns'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 322](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L322)

---

<a id='mainwp-sitestable-item'></a>
### `mainwp-sitestable-item`

* Filter is being replaced with mainwp_sitestable_item

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($item, $item)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_item'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($item, $item)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_item'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 180](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L180)

---

<a id='mainwp-sitestable-prepared-items'></a>
### `mainwp-sitestable-prepared-items`

* Action is being replaced with mainwp_sitestable_prepared_items

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($websites, $site_ids)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_prepared_items'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($websites, $site_ids)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sitestable_prepared_items'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1018](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1018)

---

<a id='mainwp-widgets-screen-options'></a>
### `mainwp-widgets-screen-options`

* Method render_screen_options()

Render modal window for Page Settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_widgets_screen_options'` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2421](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2421)

---

<a id='mainwp-added-extension-menu'></a>
### `mainwp_added_extension_menu`

* Adds Extension to the navigation menu

Adds Extension instance to the Extensions located in the main MainWP navigation menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$slug` | `string` | Extension slug.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-extensions-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php), [line 345](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-handler.php#L345)

---

<a id='mainwp-admin-menu'></a>
### `mainwp_admin_menu`

* Action: mainwp_admin_menu

Hooks main navigation menu items.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 303](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L303)

---

<a id='mainwp-admin-menu-sub'></a>
### `mainwp_admin_menu_sub`

* Action: mainwp_admin_menu_sub

Hooks main navigation sub-menu items.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 450](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L450)

---

<a id='mainwp-after-cron-jobs-table'></a>
### `mainwp_after_cron_jobs_table`

* Action: mainwp_after_cron_jobs_table

Renders on the bottom of the Cron Jobs page, after the Schedules table.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1187](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1187)

---

<a id='mainwp-after-error-log-table'></a>
### `mainwp_after_error_log_table`

* Action: mainwp_after_error_log_table

Fires after the Error Log table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1507](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1507)

---

<a id='mainwp-after-overview-widgets'></a>
### `mainwp_after_overview_widgets`

* Action: 'mainwp_after_overview_widgets'

Fires at the bottom of the Overview page (after the last widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'dashboard'` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 393](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L393)
- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 932](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L932)
- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 329](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L329)
- [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 395](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L395)

---

<a id='mainwp-after-server-info-table'></a>
### `mainwp_after_server_info_table`

* Action: mainwp_after_server_info_table

Fires on the bottom of the Info page, after the Server Info table.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 567](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L567)

---

<a id='mainwp-after-upload-custom-icon'></a>
### `mainwp_after_upload_custom_icon`

* Action: mainwp_after_upload_custom_icon

Fires after the modal element.

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1961](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1961)

---

<a id='mainwp-all-disablemenuitems'></a>
### `mainwp_all_disablemenuitems`

* Method admin_footer()

Create MainWP admin footer.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 1240](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L1240)

---

<a id='mainwp-before-cron-jobs-table'></a>
### `mainwp_before_cron_jobs_table`

* Action: mainwp_before_cron_jobs_table

Renders on the top of the Cron Jobs page, before the Schedules table.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1044](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1044)

---

<a id='mainwp-before-error-log-table'></a>
### `mainwp_before_error_log_table`

* Action: mainwp_before_error_log_table

Fires before the Error Log table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1455](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1455)

---

<a id='mainwp-before-log-data'></a>
### `mainwp_before_log_data`

* Method log_to_db()

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$text` | `string` | Log record text.
`$priority` | `int` | Set priority.
`$log_color` | `int` | Set color.

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L426)

---

<a id='mainwp-before-overview-widgets'></a>
### `mainwp_before_overview_widgets`

* Action: mainwp_before_overview_widgets

Fires at the top of the Overview page (before first widget).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'dashboard'` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 373](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L373)
- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 910](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L910)
- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 316](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L316)
- [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 382](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L382)

---

<a id='mainwp-before-server-info-table'></a>
### `mainwp_before_server_info_table`

* Action: mainwp_before_server_info_table

Fires on the top of the Info page, before the Server Info table.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 422](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L422)

---

<a id='mainwp-before-upload-custom-icon'></a>
### `mainwp_before_upload_custom_icon`

* Action: mainwp_after_upload_custom_icon

Fires before the modal element.

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1931](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1931)

---

<a id='mainwp-compact-action'></a>
### `mainwp_compact_action`

* Create compact logs and erase records from the database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'saved'` |  | 
`$year` |  | 
`$year_data` |  | 
`$start_time` | `int` | start time to compact.
`$end_time` | `int` | end time to compact.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'saved'` |  | 
`$year` |  | 
`$year_data` |  | 
`$start_time` | `int` | start time to compact.
`$end_time` | `int` | end time to compact.

**Usage Locations:**

- [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 205](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L205)

---

<a id='mainwp-cost-summary-getmetaboxes'></a>
### `mainwp_cost_summary_getmetaboxes`

* Method add_meta_boxes()

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 195](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L195)

---

<a id='mainwp-cron-jobs-list'></a>
### `mainwp_cron_jobs_list`

* Action: mainwp_cron_jobs_list

Renders as the last row of the Schedules table.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1143](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1143)

---

<a id='mainwp-cron-jobs-table-features'></a>
### `mainwp_cron_jobs_table_features`

* Filter: mainwp_cron_jobs_table_features

Filters the Cron Schedules table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1161](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1161)

---

<a id='mainwp-disablemenuitems'></a>
### `mainwp_disablemenuitems`

* Method init()

Instantiate Plugin.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 584](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L584)

---

<a id='mainwp-do-widget-boxes-sorted'></a>
### `mainwp_do_widget_boxes_sorted`

* Method do_widget_boxes()

Customize WordPress do_meta_boxes() function.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$wgsorted` |  | 
`$page` |  | 
`$client_id` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1605](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1605)

---

<a id='mainwp-extensions-top-header-after-tab'></a>
### `mainwp_extensions_top_header_after_tab`

* Method render_header()

Render page header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$shownPage` | `string` | The page slug shown at this moment.

**Usage Locations:**

- [class/class-mainwp-extensions-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php), [line 50](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php#L50)

---

<a id='mainwp-get-started-widget-bottom'></a>
### `mainwp_get_started_widget_bottom`

* Action: mainwp_get_started_widget_bottom

Fires bottom the widget.

**Changelog**

Version | Description
------- | -----------
`5.0` |

**Usage Locations:**

- [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 135](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L135)

---

<a id='mainwp-get-started-widget-title'></a>
### `mainwp_get_started_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Get Started with MainWP', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Get Started with MainWP', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 63](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L63)

---

<a id='mainwp-get-started-widget-top'></a>
### `mainwp_get_started_widget_top`

* Action: mainwp_get_started_widget_top

Fires top the widget.

**Changelog**

Version | Description
------- | -----------
`5.0` |

**Usage Locations:**

- [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 93](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L93)

---

<a id='mainwp-getmetaboxes'></a>
### `mainwp_getmetaboxes`

* Method on_load_page_dashboard()

Add individual meta boxes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 
`$dashboard_siteid` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1408](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1408)

---

<a id='mainwp-init-primary-menu-items'></a>
### `mainwp_init_primary_menu_items`

* Method init_mainwp_menu_items()

Init MainWP menus.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$menus_items` | `array` | menus items.
`$part` | `string` | menus part.

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 332](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L332)

---

<a id='mainwp-insights-getmetaboxes'></a>
### `mainwp_insights_getmetaboxes`

* Method add_meta_boxes()

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  |

**Usage Locations:**

- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 248](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L248)

---

<a id='mainwp-is-disable-menu-item'></a>
### `mainwp_is_disable_menu_item`

* Method is_disable_menu_item

Check if $_mainwp_disable_menus_items contains any menu items to hide.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$disabled` |  | 
`$level` | `string` | The level the menu item is on.
`$item` | `array\|string` | The menu items meta data.

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 529](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L529)

---

<a id='mainwp-log-do-to-db'></a>
### `mainwp_log_do_to_db`

* Method log_to_db()

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$do_log` |  | 
`$website` | `mixed` | website object.

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L426)

---

<a id='mainwp-log-to-db-data'></a>
### `mainwp_log_to_db_data`

* Method log_to_db()

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L426)

---

<a id='mainwp-log-to-db-priority'></a>
### `mainwp_log_to_db_priority`

* Method log_to_db()

Log to database.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$priority` | `int` | Set priority.
`$website` | `mixed` | website object.

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L426)

---

<a id='mainwp-logs-manage-table-bottom'></a>
### `mainwp_logs_manage_table_bottom`

* Action: mainwp_logs_widget_bottom

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'recent_events'` |  |

**Changelog**

Version | Description
------- | -----------
`5.4` |

**Usage Locations:**

- [modules/logs/pages/page-log-manage-insights-events-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php), [line 201](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php#L201)

---

<a id='mainwp-logs-manage-table-top'></a>
### `mainwp_logs_manage_table_top`

* Action: mainwp_logs_manage_table_top

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'recent_events'` |  |

**Changelog**

Version | Description
------- | -----------
`5.4` |

**Usage Locations:**

- [modules/logs/pages/page-log-manage-insights-events-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php), [line 187](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-manage-insights-events-page.php#L187)

---

<a id='mainwp-logs-widget-bottom'></a>
### `mainwp_logs_widget_bottom`

* Action: mainwp_logs_widget_bottom

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'core'` |  |

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/logs/widgets/widget-log-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php#L106)
- [modules/logs/widgets/widget-log-graph-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php#L91)
- [modules/logs/widgets/widget-log-graph-php-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php#L91)
- [modules/logs/widgets/widget-log-graph-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php#L91)
- [modules/logs/widgets/widget-log-graph-status-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php#L91)
- [modules/logs/widgets/widget-log-graph-tags-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php), [line 93](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php#L93)
- [modules/logs/widgets/widget-log-graph-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php#L91)
- [modules/logs/widgets/widget-log-graph-wp-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php#L91)
- [modules/logs/widgets/widget-log-pages-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php#L106)
- [modules/logs/widgets/widget-log-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php#L106)
- [modules/logs/widgets/widget-log-posts-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php#L106)
- [modules/logs/widgets/widget-log-recent-events-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php), [line 100](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php#L100)
- [modules/logs/widgets/widget-log-sites-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php), [line 107](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php#L107)
- [modules/logs/widgets/widget-log-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php#L106)
- [modules/logs/widgets/widget-log-users-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php), [line 106](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php#L106)

---

<a id='mainwp-logs-widget-top'></a>
### `mainwp_logs_widget_top`

* Action: mainwp_logs_widget_top

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'core'` |  |

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/logs/widgets/widget-log-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-clients-widget.php#L91)
- [modules/logs/widgets/widget-log-graph-clients-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-clients-widget.php#L76)
- [modules/logs/widgets/widget-log-graph-php-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-php-widget.php#L76)
- [modules/logs/widgets/widget-log-graph-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-plugins-widget.php#L76)
- [modules/logs/widgets/widget-log-graph-status-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-status-widget.php#L76)
- [modules/logs/widgets/widget-log-graph-tags-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php), [line 78](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-tags-widget.php#L78)
- [modules/logs/widgets/widget-log-graph-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-themes-widget.php#L76)
- [modules/logs/widgets/widget-log-graph-wp-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-graph-wp-widget.php#L76)
- [modules/logs/widgets/widget-log-pages-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-pages-widget.php#L91)
- [modules/logs/widgets/widget-log-plugins-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-plugins-widget.php#L91)
- [modules/logs/widgets/widget-log-posts-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-posts-widget.php#L91)
- [modules/logs/widgets/widget-log-recent-events-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php), [line 85](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-recent-events-widget.php#L85)
- [modules/logs/widgets/widget-log-sites-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php), [line 92](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-sites-widget.php#L92)
- [modules/logs/widgets/widget-log-themes-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-themes-widget.php#L91)
- [modules/logs/widgets/widget-log-users-widget.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php), [line 91](https://github.com/mainwp/mainwp/blob/master/modules/logs/widgets/widget-log-users-widget.php#L91)

---

<a id='mainwp-main-menu'></a>
### `mainwp_main_menu`

* Filter: mainwp_main_menu

Filters main navigation menu items

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_leftmenu` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 684](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L684)

---

<a id='mainwp-main-menu-disable-menu-items'></a>
### `mainwp_main_menu_disable_menu_items`

* Filter: mainwp_main_menu_disable_menu_items

Filters disabled MainWP navigation items.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_mainwp_disable_menus_items` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 600](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L600)

---

<a id='mainwp-main-menu-submenu'></a>
### `mainwp_main_menu_submenu`

* Filter: mainwp_main_menu_submenu

Filters main navigation subt-menu items

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_sub_leftmenu` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 694](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L694)

---

<a id='mainwp-menu-extensions-left-menu'></a>
### `mainwp_menu_extensions_left_menu`

* Method init_extensions_menu()

Initiate left Extensions menus.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extensions_and_leftmenus` |  |

**Usage Locations:**

- [pages/page-mainwp-extensions-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php), [line 33](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php#L33)

---

<a id='mainwp-menu-logo-alt'></a>
### `mainwp_menu_logo_alt`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`'MainWP'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'MainWP'` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 912](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L912)

---

<a id='mainwp-menu-logo-href'></a>
### `mainwp_menu_logo_href`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`admin_url('admin.php?page=mainwp_tab')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`admin_url('admin.php?page=mainwp_tab')` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 889](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L889)

---

<a id='mainwp-menu-logo-src'></a>
### `mainwp_menu_logo_src`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`MAINWP_PLUGIN_URL . 'assets/images/mainwp-icon.svg'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`MAINWP_PLUGIN_URL . 'assets/images/mainwp-icon.svg'` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 901](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L901)

---

<a id='mainwp-module-cost-tracker-actions-bar-left'></a>
### `mainwp_module_cost_tracker_actions_bar_left`

* Render Actions Bar

Renders the actions bar on the Dashboard tab.

**Usage Locations:**

- [modules/cost-tracker/pages/page-cost-tracker-dashboard.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 1110](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L1110)

---

<a id='mainwp-module-cost-tracker-actions-bar-right'></a>
### `mainwp_module_cost_tracker_actions_bar_right`

* Render Actions Bar

Renders the actions bar on the Dashboard tab.

**Usage Locations:**

- [modules/cost-tracker/pages/page-cost-tracker-dashboard.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 1110](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L1110)

---

<a id='mainwp-module-cost-tracker-monthly-renewals-widget-title'></a>
### `mainwp_module_cost_tracker_monthly_renewals_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Monthly Renewals', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Monthly Renewals', 'mainwp')` |  |

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L59)

---

<a id='mainwp-module-cost-tracker-summary-enabled-widgets'></a>
### `mainwp_module_cost_tracker_summary_enabled_widgets`

* Unset unwanted Widgets

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

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 231](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L231)

---

<a id='mainwp-module-cost-tracker-summary-screen-options-bottom'></a>
### `mainwp_module_cost_tracker_summary_screen_options_bottom`

* Action: mainwp_module_cost_tracker_summary_screen_options_bottom

Fires at the bottom of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 451](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L451)

---

<a id='mainwp-module-cost-tracker-summary-screen-options-top'></a>
### `mainwp_module_cost_tracker_summary_screen_options_top`

* Action: mainwp_module_cost_tracker_summary_screen_options_top

Fires at the top of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 437](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L437)

---

<a id='mainwp-module-cost-tracker-summary-widgets-screen-options'></a>
### `mainwp_module_cost_tracker_summary_widgets_screen_options`

* Filter: mainwp_module_cost_tracker_summary_widgets_screen_options

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  |

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 497](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L497)

---

<a id='mainwp-module-cost-tracker-upcoming-renewals-widget-title'></a>
### `mainwp_module_cost_tracker_upcoming_renewals_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Renewals', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Renewals', 'mainwp')` |  |

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L59)

---

<a id='mainwp-module-cost-tracker-widget-bottom'></a>
### `mainwp_module_cost_tracker_widget_bottom`

* Action: mainwp_module_cost_tracker_widget_bottom

Fires at the bottom of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'payment-left-for-this-month'` |  |

**Changelog**

Version | Description
------- | -----------
`5.0.2` |

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php), [line 79](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php#L79)
- [modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php), [line 79](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php#L79)
- [modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php), [line 79](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php#L79)

---

<a id='mainwp-module-cost-tracker-widget-top'></a>
### `mainwp_module_cost_tracker_widget_top`

* Action: mainwp_module_cost_tracker_widget_top

Fires at the top of the widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'payment-left-for-this-month'` |  |

**Changelog**

Version | Description
------- | -----------
`5.0.2` |

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php), [line 65](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-category-totals.php#L65)
- [modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php), [line 65](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-totals.php#L65)
- [modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php), [line 65](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-payment-left-this-month.php#L65)

---

<a id='mainwp-module-cost-tracker-yearly-renewals-widget-title'></a>
### `mainwp_module_cost_tracker_yearly_renewals_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Yearly Renewals', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Upcoming Yearly Renewals', 'mainwp')` |  |

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L59)

---

<a id='mainwp-module-dashboard-insights-help-item'></a>
### `mainwp_module_dashboard_insights_help_item`

* Action: mainwp_module_dashboard_insights_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Insights page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`5.2` |

**Usage Locations:**

- [modules/logs/classes/class-log-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php), [line 309](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php#L309)

---

<a id='mainwp-module-log-overview-enabled-widgets'></a>
### `mainwp_module_log_overview_enabled_widgets`

* Unset unwanted Widgets

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

**Usage Locations:**

- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 284](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L284)

---

<a id='mainwp-module-log-overview-screen-options-bottom'></a>
### `mainwp_module_log_overview_screen_options_bottom`

* Action: mainwp_module_log_overview_screen_options_bottom

Fires at the bottom of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 983](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L983)

---

<a id='mainwp-module-log-overview-screen-options-top'></a>
### `mainwp_module_log_overview_screen_options_top`

* Action: mainwp_module_log_overview_screen_options_top

Fires at the top of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 969](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L969)

---

<a id='mainwp-module-log-widgets-screen-options'></a>
### `mainwp_module_log_widgets_screen_options`

* Filter: mainwp_module_log_widgets_screen_options

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  |

**Changelog**

Version | Description
------- | -----------
`4.6` |

**Usage Locations:**

- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 1039](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L1039)

---

<a id='mainwp-non-mainwp-changes-table-bottom'></a>
### `mainwp_non_mainwp_changes_table_bottom`

* Action: mainwp_non_mainwp_changes_table_bottom

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

- [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 180](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L180)

---

<a id='mainwp-non-mainwp-changes-table-top'></a>
### `mainwp_non_mainwp_changes_table_top`

* Action: mainwp_non_mainwp_changes_table_top

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

- [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 162](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L162)

---

<a id='mainwp-non-mainwp-changes-widget-bottom'></a>
### `mainwp_non_mainwp_changes_widget_bottom`

* Action: mainwp_non_mainwp_changes_widget_bottom

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

- [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 205](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L205)

---

<a id='mainwp-non-mainwp-changes-widget-title'></a>
### `mainwp_non_mainwp_changes_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites Changes', 'mainwp')` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Sites Changes', 'mainwp')` |  | 
`$website` |  |

**Usage Locations:**

- [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 127](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L127)

---

<a id='mainwp-non-mainwp-changes-widget-top'></a>
### `mainwp_non_mainwp_changes_widget_top`

* Actoin: mainwp_non_mainwp_changes_widget_top

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

- [widgets/widget-mainwp-site-actions.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php), [line 150](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-site-actions.php#L150)

---

<a id='mainwp-notes-widget-bottom'></a>
### `mainwp_notes_widget_bottom`

* Action: mainwp_notes_widget_bottom

Fires at the bottom of the Notes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-notes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php), [line 95](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php#L95)

---

<a id='mainwp-notes-widget-title'></a>
### `mainwp_notes_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$website` |  |

**Usage Locations:**

- [widgets/widget-mainwp-notes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php), [line 62](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php#L62)

---

<a id='mainwp-notes-widget-top'></a>
### `mainwp_notes_widget_top`

* Action: mainwp_notes_widget_top

Fires at the top of the Notes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-notes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php), [line 70](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-notes.php#L70)

---

<a id='mainwp-overview-enabled-widgets'></a>
### `mainwp_overview_enabled_widgets`

* Unset unwanted Widgets

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

**Usage Locations:**

- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1461](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1461)
- [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 230](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L230)

---

<a id='mainwp-overview-screen-options-bottom'></a>
### `mainwp_overview_screen_options_bottom`

* Action: mainwp_overview_screen_options_bottom

Fires at the bottom of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 837](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L837)

---

<a id='mainwp-overview-screen-options-top'></a>
### `mainwp_overview_screen_options_top`

* Action: mainwp_overview_screen_options_top

Fires at the top of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 823](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L823)

---

<a id='mainwp-removed-extension-menu'></a>
### `mainwp_removed_extension_menu`

* Remove Extensions menu from MainWP Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key` |  |

**Usage Locations:**

- [class/class-mainwp-post-extension-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-extension-handler.php), [line 408](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-extension-handler.php#L408)

---

<a id='mainwp-reset-admin-pass-modal-bottom'></a>
### `mainwp_reset_admin_pass_modal_bottom`

* Action: mainwp_reset_admin_pass_modal_bottom

Fires at the bottom of the Update Admin Passwords modal.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 213](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L213)

---

<a id='mainwp-reset-admin-pass-modal-top'></a>
### `mainwp_reset_admin_pass_modal_top`

* Action: mainwp_reset_admin_pass_modal_top

Fires at the top of the Update Admin Passwords modal.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 193](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L193)

---

<a id='mainwp-screen-options-modal-bottom'></a>
### `mainwp_screen_options_modal_bottom`

* Action: mainwp_screen_options_modal_bottom

Fires at the bottom of the Page Settings modal element.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2572](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2572)
- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 551](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L551)
- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 1093](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L1093)
- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 492](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L492)

---

<a id='mainwp-screen-options-modal-top'></a>
### `mainwp_screen_options_modal_top`

* Action: mainwp_screen_options_modal_top

Fires at the top of the Page Settings modal element.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2480](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2480)
- [modules/cost-tracker/classes/class-cost-tracker-summary.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php), [line 515](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-summary.php#L515)
- [modules/logs/pages/page-log-insights-page.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php), [line 1057](https://github.com/mainwp/mainwp/blob/master/modules/logs/pages/page-log-insights-page.php#L1057)
- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 456](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L456)

---

<a id='mainwp-screen-options-pulse-control'></a>
### `mainwp_screen_options_pulse_control`

* Method render_header_actions()

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1273](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1273)

---

<a id='mainwp-sitestable-display-row-columns'></a>
### `mainwp_sitestable_display_row_columns`

* Get table rows.

Optimize for shared hosting or big networks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1554](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1554)

---

<a id='mainwp-sitestable-getcolumns'></a>
### `mainwp_sitestable_getcolumns`

* Filter: mainwp_sitestable_getcolumns

Filters the Manage Sites table columns. Allows user to create a new column.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$columns` | `array` | Array containing table columns.
`$columns` | `array` | Array containing table columns.

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 329](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L329)

---

<a id='mainwp-sitestable-item'></a>
### `mainwp_sitestable_item`

* Filter: mainwp_sitestable_item

Filters the Manage Sites table column items. Allows user to create new column item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item` | `array` | Array containing child site data.
`$column_name` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 187](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L187)

---

<a id='mainwp-sitestable-prepare-extra-view'></a>
### `mainwp_sitestable_prepare_extra_view`

* Prepare the items to be listed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 694](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L694)

---

<a id='mainwp-sitestable-prepared-items'></a>
### `mainwp_sitestable_prepared_items`

* Action: mainwp_sitestable_prepared_items

Fires before the Sites table itemes are prepared.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites data.
`$site_ids` | `array` | Array containing IDs of all child sites.

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1025](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1025)

---

<a id='mainwp-sitestable-render-column'></a>
### `mainwp_sitestable_render_column`

* Columns for a single row.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` | `mixed` | Child Site.
`$classes` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$column_name` |  | 
`$website` | `mixed` | Child Site.
`$classes` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 1976](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L1976)

---

<a id='mainwp-ui-use-wp-calendar'></a>
### `mainwp_ui_use_wp_calendar`

* Filter: mainwp_ui_use_wp_calendar

Filters whether default jQuery datepicker should be used to avoid potential problems with Senatic UI Calendar library.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Changelog**

Version | Description
------- | -----------
`4.0.5` |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 821](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L821)

---

<a id='mainwp-widget-boxes-show-widgets'></a>
### `mainwp_widget_boxes_show_widgets`

* Method do_widget_boxes()

Customize WordPress do_meta_boxes() function.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$page` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1605](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1605)

---

<a id='mainwp-widgets-chart-date-format'></a>
### `mainwp_widgets_chart_date_format`

* Prepare response time for ui chart data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$format_date` |  | 
`$params` | `array` | params.
`$slug` | `string` | for date format hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$format_date` |  | 
`$params` | `array` | params.
`$slug` | `string` | for date format hook.

**Usage Locations:**

- [widgets/widget-mainwp-uptime-monitoring-site-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php), [line 615](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php#L615)

---

<a id='mainwp-widgets-screen-options'></a>
### `mainwp_widgets_screen_options`

* Filter: mainwp_widgets_screen_options

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2457](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2457)

---


# MainWP Developer Changelog

This changelog tracks changes to the MainWP core that may affect third-party extensions and developers. The purpose is to provide clear documentation of API changes, deprecations, and breaking changes to help extension developers stay current with MainWP development.

## Color Key
- 🟢 **Added**: New features or capabilities
- 🔵 **Fixed**: Bug fixes
- 🟠 **Changed**: Feature modifications or changes
- ⚫ **Deprecated**: Features planned for removal in future versions
- 🔴 **Removed**: Features that have been removed
- 🟣 **Security**: Security-related fixes or changes
- ⚡ **Performance**: Performance improvements
- 🟡 **Other**: Other changes that don't fit the categories above

Each entry includes:
- The type of change
- A description of what changed
- The expected release version and/or date (when available)
- Any action required by extension developers

---

# March 13, 2025 (Example changelog entry)

## 🔧 Core Changes
- 🟢 **Added** [v5.1 - April 2025]: New filter hook `mainwp_pre_process_site_data` that runs before site data processing
- ⚫ **Deprecated** [v5.2 - June 2025]: The `mainwp_legacy_auth_method` function - update extensions to use the new authentication method
- 🟠 **Changed** [v5.1 - April 2025]: Updated `mainwp_user_login()` implementation to include additional validation checks

## 🔌 API Changes
- 🟠 **Changed** [v5.1 - April 2025]: Site endpoint now requires authentication token in headers - action required: update API calls
- 🟢 **Added** [v5.1 - April 2025]: New parameter `include_metadata` to the GET /sites endpoint

## ⚡ Performance Optimizations
- ⚡ **Performance** [v5.0.4 - March 20, 2025]: Reduced database queries in the main site loop
- ⚡ **Performance** [v5.0.4 - March 20, 2025]: Implemented caching for frequently accessed configuration

## ⚠️ Breaking Changes
- 🔴 **Removed** [v5.1 - April 2025]: Legacy API endpoint `/v1/sites` has been completely removed - action required: migrate to v2 API
- 🟠 **Changed** [v5.1 - April 2025]: Order of execution in the `mainwp_init` hook - action required: review extension hook priorities



# March 13, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Changed** [v5.4.0.2 - March 2025]: Non-MainWP Changes data table changed.

* Previous data table name: 'prefix_mainwp_wp_actions'
  Fields:
    action_id int(11) NOT NULL auto_increment,
    wpid int(11) NOT NULL,
    object_id varchar(20) NOT NULL,
    context varchar(20) NOT NULL,
    action varchar(10) NOT NULL,
    action_user text NOT NULL DEFAULT "",
    created int(11) NOT NULL DEFAULT 0,
    meta_data text NOT NULL DEFAULT "",
    dismiss tinyint(1) NOT NULL DEFAULT 0,
    summary varchar(255) NOT NULL default ""';

* Current data table name: prefix_mainwp_wp_logs, and meta table prefix_mainwp_wp_logs_meta

	prefix_mainwp_wp_logs table's fields:

    log_id bigint(20) NOT NULL auto_increment,
    site_id bigint(20) unsigned NULL,
    object_id varchar(20) NOT NULL DEFAULT '',
    item text NOT NULL,
    user_id int(11) unsigned NOT NULL DEFAULT '0',
    action varchar(100) NOT NULL,
    context varchar(100) NOT NULL,
    connector varchar(100) NOT NULL,
    state tinyint(1) unsigned NULL,
    created int(11) NOT NULL DEFAULT 0,
    duration float(11,4) NOT NULL DEFAULT '0',
    dismiss tinyint(1) NOT NULL DEFAULT 0,

	prefix_mainwp_wp_logs_meta table's fields:

	meta_id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    meta_log_id bigint(20) unsigned NOT NULL,
    meta_key varchar(200) NOT NULL,
    meta_value mediumtext NOT NULL,
    KEY meta_log_id (meta_log_id),
    KEY meta_key (meta_key(191))

- 🟢 **Added** [v5.4.0.3 - March 2025]: New hook  `mainwp_auto_updates_sync_data_before_run` to enable/disable sync site before auto updates process run, default is enable - true. Use the hook to disable sync data before run auto updates for some dashboard have problem with sync site before run auto updates.

### Favorites extension
- 🟢 **Added** [v5.2 - March 2025]: Added new actions
`mainwp_favorites_main_page_top` Run before of the extension's main page.
`mainwp_favorites_main_page_bottom` Run at the bottom of the extension's main page.
`mainwp_favorites_before_items_list` Run before favorites items list.
`mainwp_favorites_after_items_list` Run after favorites items list.
`mainwp_favorites_add_new_top` Run at the top of the "Add New" item popup.
`mainwp_favorites_add_new_bottom` Run at the bottom of the "Add New" item popup.
`mainwp_favorites_add_new_buttons` Run in the buttons sections of add new item popup.
`mainwp_favorites_process_item_before_output` Run before output of process item.

- 🟢 **Added** [v5.2 - March 2025]: Added new filters
`mainwp_favorites_items_list` Applies to items list.
`mainwp_favorites_get_item_result` Applies to get item result.
`mainwp_favorites_get_item_info` Applies to get item return info.
`mainwp_favorites_process_item_data` Applies to process item data.
`mainwp_favorites_save_data_item` Applies when data item saving.


## 🔌 API Changes

### MainWP Dashboard

- 🟢 **Changed** [v5.4.0.2 - March 2025]: The response REST API endpoint: sites/<id_domain>/non-mainwp-changes was changed

    New the REST API response data will be prefix_mainwp_wp_logs fields and those addition fields:

    url => site url
    log_site_name ==> site name
    usermeta => compatible user meta
    user_meta_json ==> json format of array(
          'wp_user_id',
          'display_name',
          'action_user',
          'role',
          'user_role_label',
          'agent',
          'system_user_id',// sometime.
          'system_user_name' // sometime.
    );
    meta_name => meta name field data of changes
    extra_info ==> may some extra info if exit
    view_log_id,

	API data response field changes: 'data'    => $data,

* For example API response:
  {
    "success": 1,
    "total": 8,
    "data": [
        {
            "log_id": "4321",
            "site_id": "159",
            "item": "construction-services-company Theme",
            "user_id": "1",
            "action": "delete",
            "context": "installer",
            "connector": "non-mainwp-changes",
            "state": "1",
            "created": "1741266179",
            "duration": "0.2110",
            "object_id": "17412661791649",
            "dismiss": "0",
            "url": "https://example.com/",
            "log_site_name": "mainwpshop.huedev.com",
            "view_log_id": "4321",
            "meta_name": "construction-services-company",
            "user_meta_json": "{\"wp_user_id\":1,\"display_name\":\"adminuser\",\"action_user\":\"adminuser\",\"role\":\"administrator\",\"user_role_label\":\"Administrator\",\"agent\":\"\"}",
            "usermeta": null,
            "extra_info": null
        },
		{
            "log_id": "4320",
            "site_id": "159",
            "item": "kata Theme",
            "user_id": "1",
            "action": "delete",
            "context": "installer",
            "connector": "non-mainwp-changes",
            "state": "1",
            "created": "1741266157",
            "duration": "1.6536",
            "object_id": "17412661579961",
            "dismiss": "0",
            "url": "https://example.net/",
            "log_site_name": "mainwpshop.huedev.com",
            "view_log_id": "4320",
            "meta_name": "kata",
            "user_meta_json": "{\"wp_user_id\":1,\"display_name\":\"adminuser\",\"action_user\":\"adminuser\",\"role\":\"administrator\",\"user_role_label\":\"Administrator\",\"agent\":\"\"}",
            "usermeta": null,
            "extra_info": null
        },
		.....



# March 14, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.0.3 - March 2025]: Added new filters
`mainwp_site_changes_table_pages_length` To support custom Pages lenght of Site Changes table.


# March 18, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.0.3 - March 2025]: Added new params for non-mainwp-changes REST API endpoint
- 'page' - Page number
- 'per_page' - Items per page.
- 'source' - Source changes: Available values are 'wpadmin', 'dashboard', 'all', or leave empty (default is 'wpadmin').

# March 19, 2025

## ⚡ Performance Optimizations

### MainWP Dashboard
- ⚡ **Performance** [v5.4.0.3 - March 19, 2025]: Make query for non-mainwp-change rest api endpoint faster a bit by reduce a mysql join command.


# March 20, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.0.3 - March 2025]: Added new hooks: mainwp_general_process_update, mainwp_general_process_delete, mainwp_general_process_get_process_by to support update/delete/get the general schedule process.

# March 22, 2025

## ⚡ Performance Optimizations

### MainWP Time Tracker Extension
- ⚡ **Performance** [v5.1 - March 22, 2025]: Imporved DB query for checking table existed.

### MainWP Dashboard
- 🟠 **Changed** [v5.4.0.3 - March 2025]: function name changed `get_none_mainwp_actions_log()` to `get_none_mainwp_actions_log_for_rest_api()` - in the file: class/class-mainwp-db-site-actions.php


# April 3, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.0.4 - April 2025]: Added new hooks: mainwp_connect_http_request_headers to support custom request headers.

- 🟢 **Added** [v5.4.0.4 - April 2025]: Added new hooks: mainwp_uptime_monitor_check_result to support custom uptime monitor results.


# April 7, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.0.5 - April 2025]: Added new params for non-mainwp-changes REST API endpoint
- 'actions' - To support for `action` logs query.
- 'contexts' - To support for `context` logs query.


# April 15, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.0.5 - April 2025]: Excluded the Site Changes count information from REST API endpoints by default, while leaving it as option to optimize the query performance.
- 'total_count' - To support for `total_count` logs query.

- 🟢 **Added** [v5.4.0.5 - April 2025]: Added the `$clients` as the 6th parameter to the `mainwp_getdbsites` filter so extensions can get sites info by clients selection.

# April 16, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.1 - April 2025]: Added hook: mainwp_individual_updates_tabs
 to support generate custom updates tabs.


 # April 23, 2025

## 🔧 Core Changes

### MainWP Lighthouse Extension
- 🟢 **Added** [v5.1.1 - April 2025]: Added hook: mainwp_lighthouse_next_start_timestamp
 to support tweaks next audit start time.


# April 23, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.1 - April 2025]: Added hook: mainwp_log_system_query_params
 to support tweaks log system query params.
 - Added hook: mainwp_module_log_record_inserted
 to support action after insert custom log data.
 - Added hook: mainwp_custom_log_enabled_log_priority
 to support check if custom log enabled by priority.


# April 28, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.1 - April 2025]:
- Added hooks:  mainwp_manage_events_sites_changes_optimize_view too support an optimize view for sites changes
- Added: param optimize_view for non-mainwp-changes rest api enpoint to support an optimize query sites changes data

# May 2, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟢 **Added** [v5.4.1 - May 2025]: Added hooks:
mainwp_get_cron_jobs_init, mainwp_module_log_enable_insert_log_type for development

# May 6, 2025

## 🔧 Core Changes

### MainWP Pro Reports Extension
- 🟢 **Added** [v5.0.6 - May 2025]: Added template hooks: mainwp_pro_reports_template_general_misc_top, mainwp_pro_reports_template_general_misc_bottom,
mainwp_pro_reports_template_summary_top, mainwp_pro_reports_template_summary_bottom, mainwp_pro_reports_template_general_top, mainwp_pro_reports_template_general_bottom
To support custom templates content.



# May 8, 2025

## 🔧 Core Changes

### MainWP Child
- 🟢 **Added** [v5.4.0.7 - May 2025]: Added hook: mainwp_child_prepared_reports_data
To support custom reports data in child sites.



# May 12, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟠 **Changed** [v5.4.0.9 - May 2025]: Correct hook name: mainwp_favorites_enable_schedule_items_update to mainwp_uptime_monitors_enable_schedule_notifications


# May 13, 2025

## 🔌 API Changes

### MainWP Dashboard

- 🟢 **Added** [v5.4.1 - March 2025]: Added new parameters to the non-mainwp-changes REST API endpoint
- 'optimize_with_meta' - Supports retrieving optimization meta data when the 'optimize_view' parameter is set to 1.

# June 4, 2025

## 🔧 Core Changes

### MainWP Pro Reports Extension
- 🟢 **Added** [v5.0.10 - June 2025]: Added template hooks: mainwp_pro_reports_agency_template_summary_bottom to support custom reports template.

# June 9, 2025

## 🔧 Core Changes

### MainWP Dashboard
- 🟠 **Changed** [v5.4.1 - June 2025]:
- Removed: Column `object_id` of the [prefix_]wp_logs, [prefix_]wp_logs_archive tables.
- Added: new columns log_type_id, user_login fields for tables: [prefix_]wp_logs, [prefix_]wp_logs_archive tables.
- Changed: columns changed so the output of REST API endpoint: `non-mainwp-changes` was changed as follow, added new field: `log_type_id`, removed field: `object_id`.


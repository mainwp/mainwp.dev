# Security & Monitoring Filters

Hooks related to security checks, uptime monitoring, and site health.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_secure_request`](#mainwp_secure_request) - Method admin_init()
- [`mainwp_before_system_requirements_check`](#mainwp_before_system_requirements_check) - Action: mainwp_before_system_requirements_check
- [`mainwp_after_system_requirements_check`](#mainwp_after_system_requirements_check) - Action: mainwp_after_system_requirements_check
- [`mainwp_security_issues_widget_top`](#mainwp_security_issues_widget_top) - Action: mainwp_security_issues_widget_top
- [`mainwp_security_issues_widget_top`](#mainwp_security_issues_widget_top) - Action: mainwp_security_issues_widget_top
- [`mainwp_security_issues_list_item_column`](#mainwp_security_issues_list_item_column) - Action: mainwp_security_issues_list_item_column
- [`mainwp_security_issues_widget_bottom`](#mainwp_security_issues_widget_bottom) - Action: mainwp_security_issues_widget_bottom
- [`mainwp_monitoring_sitestable_prepared_items`](#mainwp_monitoring_sitestable_prepared_items) - Action: mainwp_monitoring_sitestable_prepared_items
- [`mainwp_uptime_monitoring_after_check_uptime`](#mainwp_uptime_monitoring_after_check_uptime) - Method handle response fetch uptime.
- [`mainwp-securityissues-sites`](#mainwp-securityissues-sites) - Method render_scan_site()
- [`mainwp_securityissues_sites`](#mainwp_securityissues_sites) - Action: mainwp_securityissues_sites
- [`mainwp-sucuriscan-sites`](#mainwp-sucuriscan-sites) - Method render_scan_site()
- [`mainwp_sucuriscan_sites`](#mainwp_sucuriscan_sites) - Action: mainwp_sucuriscan_sites
- [`mainwp_uptime_monitoring_email_header`](#mainwp_uptime_monitoring_email_header) - Uptime Monitoring Email Header
- [`mainwp_uptime_monitoring_email_footer`](#mainwp_uptime_monitoring_email_footer) - Uptime Monitoring Email Footer
- [`mainwp_http_check_email_header`](#mainwp_http_check_email_header) - HTTP Check Email Header
- [`mainwp_http_check_email_footer`](#mainwp_http_check_email_footer) - HTTP Check Email Footer
- [`mainwp_licenses_deactivated_alert_email_header`](#mainwp_licenses_deactivated_alert_email_header) - Site Health Monitoring Email Header
- [`mainwp_licenses_deactivated_alert_email_footer`](#mainwp_licenses_deactivated_alert_email_footer) - Site Health Monitoring Email Footer
- [`mainwp_secure_request`](#mainwp_secure_request) - Method security_nonce().
- [`mainwp_security_issues_stats`](#mainwp_security_issues_stats) - Filters security issues
- [`mainwp_unset_security_scripts_stylesheets`](#mainwp_unset_security_scripts_stylesheets) - Method Fix Security Issues
- [`mainwp_uptime_monitoring_response_time_widget_title`](#mainwp_uptime_monitoring_response_time_widget_title) - *Arguments*
- [`mainwp_uptime_monitoring_status_widget_title`](#mainwp_uptime_monitoring_status_widget_title) - *Arguments*
- [`mainwp_security_issues_widget_title`](#mainwp_security_issues_widget_title) - *Arguments*
- [`mainwp_security_issues_list_item_title_url`](#mainwp_security_issues_list_item_title_url) - *Arguments*
- [`mainwp_security_issues_list_item_title`](#mainwp_security_issues_list_item_title) - *Arguments*
- [`mainwp_monitoring_sitestable_item`](#mainwp_monitoring_sitestable_item) - Filter: mainwp_monitoring_sitestable_item
- [`mainwp_monitoring_sitestable_getcolumns`](#mainwp_monitoring_sitestable_getcolumns) - Filter: mainwp_monitoring_sitestable_getcolumns
- [`mainwp_monitoring_sitestable_prepare_extra_view`](#mainwp_monitoring_sitestable_prepare_extra_view) - Prepair the items to be listed.
- [`mainwp_monitoring_table_features`](#mainwp_monitoring_table_features) - Filter: mainwp_monitoring_table_features
- [`mainwp_automatic_disable_uptime_monitoring_check`](#mainwp_automatic_disable_uptime_monitoring_check) - Method cron_uptime_check
- [`mainwp_uptime_monitoring_send_notification_limit`](#mainwp_uptime_monitoring_send_notification_limit) - Run schedule uptime notification.
- [`mainwp_uptime_monitoring_get_monitors_to_check_params`](#mainwp_uptime_monitoring_get_monitors_to_check_params) - Get sites monitors to check.
- [`mainwp_security_nonces`](#mainwp_security_nonces) - Method admin_init()
- [`mainwp_create_security_nonces`](#mainwp_create_security_nonces) - Create the security nonces.
- [`mainwp_security_issues_stats`](#mainwp_security_issues_stats) - This filter is documented in ../pages/page-mainwp-security-issues.php
- [`mainwp_logger_keep_days`](#mainwp_logger_keep_days) - Method check_log_daily()
- [`mainwp_uptime_monitoring_allowed_methods`](#mainwp_uptime_monitoring_allowed_methods) - Method get_allowed_methods
- [`mainwp_uptime_monitoring_interval_values`](#mainwp_uptime_monitoring_interval_values) - Method get_interval_values
- [`mainwp_uptime_monitoring_timeout_values`](#mainwp_uptime_monitoring_timeout_values) - Method get_timeout_values
- [`mainwp_stats_scan_dir`](#mainwp_stats_scan_dir) - Method get_post_data_authed()
- [`mainwp_fetch_uptime_disable_check_multi_exec`](#mainwp_fetch_uptime_disable_check_multi_exec) - Apply disable check multi exec.
- [`mainwp_fetch_uptime_chunk_size_urls`](#mainwp_fetch_uptime_chunk_size_urls) - Check uptime monitors.
- [`mainwp_fetch_uptime_chunk_size_urls`](#mainwp_fetch_uptime_chunk_size_urls) - Fetch uptime urls.
- [`mainwp_uptime_monitoring_check_importance`](#mainwp_uptime_monitoring_check_importance) - Method handle response fetch uptime.
- [`mainwp_uptime_monitoring_uptime_data`](#mainwp_uptime_monitoring_uptime_data) - Method handle response fetch uptime.
- [`mainwp_uptime_monitoring_check_url`](#mainwp_uptime_monitoring_check_url) - Get apply monitor url.
- [`mainwp_module_log_check_connector_is_excluded`](#mainwp_module_log_check_connector_is_excluded) - Allows excluded connectors to be overridden and registered.
- [`mainwp_module_cost_tracker_manager_check_status`](#mainwp_module_cost_tracker_manager_check_status) - *Arguments*

## Hook Details

### `mainwp_secure_request`

*Method admin_init()*

Handles the uploading of a file.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'qq_nonce'` |  | 
`'qq_nonce'` |  | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 42](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L42)



### `mainwp_before_system_requirements_check`

*Action: mainwp_before_system_requirements_check*

Fires on the bottom of the System Requirements page, in Quick Setup Wizard.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 911](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L911)



### `mainwp_after_system_requirements_check`

*Action: mainwp_after_system_requirements_check*

Fires on the bottom of the System Requirements page, in Quick Setup Wizard.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 973](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L973)



### `mainwp_security_issues_widget_top`

*Action: mainwp_security_issues_widget_top*

Fires at the bottom of the Security Issues widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 166](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L166)



### `mainwp_security_issues_widget_top`

*Action: mainwp_security_issues_widget_top*

Fires at the bottom of the Security Issues widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 178](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L178)



### `mainwp_security_issues_list_item_column`

*Action: mainwp_security_issues_list_item_column*

Fires before the last (actions) colum in the security issues list.

Preferred HTML structure:

<div class="column middle aligned">
Your content here!
</div>

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 248](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L248)



### `mainwp_security_issues_widget_bottom`

*Action: mainwp_security_issues_widget_bottom*

Fires at the bottom of the Security Issues widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 271](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L271)



### `mainwp_monitoring_sitestable_prepared_items`

*Action: mainwp_monitoring_sitestable_prepared_items*

Fires before the Monitoring Sites table itemes are prepared.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites data.
`$site_ids` | `array` | Array containing IDs of all child sites.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 626](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L626)



### `mainwp_uptime_monitoring_after_check_uptime`

*Method handle response fetch uptime.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$heartbeat` |  | 
`$monitor` | `mixed` | monitor.
`$previous_heartbeat` |  | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 713](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L713)



### `mainwp-securityissues-sites`

*Method render_scan_site()*

Render Site Hardening sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_securityissues_sites'` |  | 

Source: [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 730](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L730)



### `mainwp_securityissues_sites`

*Action: mainwp_securityissues_sites*

Fires on a child site Hardening page at top.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.

Source: [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 772](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L772)



### `mainwp-sucuriscan-sites`

*Method render_scan_site()*

Render Site Hardening sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sucuriscan_sites'` |  | 

Source: [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 730](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L730)



### `mainwp_sucuriscan_sites`

*Action: mainwp_sucuriscan_sites*

Fires on a child site Hardening page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.

Source: [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 792](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L792)



### `mainwp_uptime_monitoring_email_header`

*Uptime Monitoring Email Header*

Fires at the top of the uptime monitoring email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-uptime-monitoring-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php), [line 32](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php#L32)



### `mainwp_uptime_monitoring_email_footer`

*Uptime Monitoring Email Footer*

Fires at the bottom of the uptime monitoring email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-uptime-monitoring-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php), [line 144](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php#L144)



### `mainwp_http_check_email_header`

*HTTP Check Email Header*

Fires at the top of the HTTP check (after update checks) email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-after-update-http-check-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php), [line 29](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php#L29)



### `mainwp_http_check_email_footer`

*HTTP Check Email Footer*

Fires at the bottom of the HTTP check (after update checks) email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-after-update-http-check-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php), [line 94](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php#L94)



### `mainwp_licenses_deactivated_alert_email_header`

*Site Health Monitoring Email Header*

Fires at the top of the site health monitoring email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-licenses-deactivated-alert-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php), [line 31](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php#L31)



### `mainwp_licenses_deactivated_alert_email_footer`

*Site Health Monitoring Email Footer*

Fires at the bottom of the site health monitoring email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-licenses-deactivated-alert-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php), [line 97](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php#L97)



### `mainwp_secure_request`

*Method security_nonce().*

Handle security nonce.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$action` | `string` | security action.

Source: [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 134](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L134)



### `mainwp_security_issues_stats`

*Filters security issues*

Filters the default security checks and enables user to disable certain checks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$information` | `object` | Object containing data from che chid site related to security issues.<br>Available options: 'db_reporting', 'php_reporting'.
`$website` | `object` | Object containing child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-security-issues.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php), [line 293](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php#L293)



### `mainwp_unset_security_scripts_stylesheets`

*Method Fix Security Issues*

Fix the selected security issue.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [pages/page-mainwp-security-issues.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php), [line 312](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php#L312)



### `mainwp_uptime_monitoring_response_time_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Uptime Monitoring', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-uptime-monitoring-site-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php), [line 190](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php#L190)



### `mainwp_uptime_monitoring_status_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Uptime Monitoring', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-uptime-monitoring-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-status.php), [line 51](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-status.php#L51)



### `mainwp_security_issues_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Site Hardening', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 98](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L98)



### `mainwp_security_issues_list_item_title_url`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'admin.php?page=managesites&dashboard=' . $website->id` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 225](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L225)



### `mainwp_security_issues_list_item_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->name` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 236](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L236)



### `mainwp_monitoring_sitestable_item`

*Filter: mainwp_monitoring_sitestable_item*

Filters the Monitoring Sites table column items. Allows user to create new column item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item` | `array` | Array containing child site data.
`$item` | `array` | Array containing child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 99](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L99)



### `mainwp_monitoring_sitestable_getcolumns`

*Filter: mainwp_monitoring_sitestable_getcolumns*

Filters the Monitoring Sites table columns. Allows user to create a new column.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$columns` | `array` | Array containing table columns.
`$columns` | `array` | Array containing table columns.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 185](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L185)



### `mainwp_monitoring_sitestable_prepare_extra_view`

*Prepair the items to be listed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  | 

Source: [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 409](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L409)



### `mainwp_monitoring_table_features`

*Filter: mainwp_monitoring_table_features*

Filter the Monitoring table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 722](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L722)



### `mainwp_automatic_disable_uptime_monitoring_check`

*Method cron_uptime_check*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-uptime-monitoring-schedule.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php), [line 67](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php#L67)



### `mainwp_uptime_monitoring_send_notification_limit`

*Run schedule uptime notification.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  | 

Source: [class/class-mainwp-uptime-monitoring-schedule.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php), [line 173](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php#L173)



### `mainwp_uptime_monitoring_get_monitors_to_check_params`

*Get sites monitors to check.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | params.

Source: [class/class-mainwp-db-uptime-monitoring.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-uptime-monitoring.php), [line 418](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-uptime-monitoring.php#L418)



### `mainwp_security_nonces`

*Method admin_init()*

Do nothing if current user is not an Admin else display the page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 766](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L766)



### `mainwp_create_security_nonces`

*Create the security nonces.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$security_names` |  | 

Source: [class/class-mainwp-post-base-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-base-handler.php), [line 140](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-base-handler.php#L140)



### `mainwp_security_issues_stats`

*This filter is documented in ../pages/page-mainwp-security-issues.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$securityStats` |  | 
`$pWebsite` |  | 

Source: [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 366](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L366)



### `mainwp_logger_keep_days`

*Method check_log_daily()*

Daily checks to clear the log file.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`7` |  | 

Source: [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 749](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L749)



### `mainwp_uptime_monitoring_allowed_methods`

*Method get_allowed_methods*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('useglobal' => esc_html__('Use global settings', 'mainwp'), 'head' => 'HEAD', 'get' => 'GET', 'post' => 'POST', 'push' => 'PUSH', 'patch' => 'PATCH', 'delete' => 'DELETE')` |  | 

Source: [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 705](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L705)



### `mainwp_uptime_monitoring_interval_values`

*Method get_interval_values*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` |  | 
`$flip_values` | `mixed` | flip values.

Source: [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 734](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L734)



### `mainwp_uptime_monitoring_timeout_values`

*Method get_timeout_values*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` |  | 
`$flip_values` | `mixed` | flip values.

Source: [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 767](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L767)



### `mainwp_stats_scan_dir`

*Method get_post_data_authed()*

Get authorized $_POST data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `mixed` | Array of Child Site Info.

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 361](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L361)



### `mainwp_fetch_uptime_disable_check_multi_exec`

*Apply disable check multi exec.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

**Changelog**

Version | Description
------- | -----------
`5.3` | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 61](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L61)



### `mainwp_fetch_uptime_chunk_size_urls`

*Check uptime monitors.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 88](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L88)



### `mainwp_fetch_uptime_chunk_size_urls`

*Fetch uptime urls.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 350](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L350)



### `mainwp_uptime_monitoring_check_importance`

*Method handle response fetch uptime.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$importance` |  | 
`$heartbeat` |  | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 713](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L713)



### `mainwp_uptime_monitoring_uptime_data`

*Method handle response fetch uptime.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$heartbeat` |  | 
`$monitor` | `mixed` | monitor.
`$previous_heartbeat` |  | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 713](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L713)



### `mainwp_uptime_monitoring_check_url`

*Get apply monitor url.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$url` |  | 
`$monitor` | `mixed` | monitor.

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 1008](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L1008)



### `mainwp_module_log_check_connector_is_excluded`

*Allows excluded connectors to be overridden and registered.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_excluded` | `bool` | True if excluded, otherwise false.
`$connector_name` |  | 
`$excluded_connectors` | `array` | An array of all excluded connector slugs.

Source: [modules/logs/classes/class-log-connectors.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php), [line 148](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php#L148)



### `mainwp_module_cost_tracker_manager_check_status`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [modules/cost-tracker/pages/page-cost-tracker-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-settings.php), [line 348](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-settings.php#L348)




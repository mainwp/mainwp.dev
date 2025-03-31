# Security & Monitoring Filters

Hooks related to security checks, uptime monitoring, and site health.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-securityissues-sites`](#mainwp-securityissues-sites) - Method render_scan_site()
- [`mainwp-sucuriscan-sites`](#mainwp-sucuriscan-sites) - Method render_scan_site()
- [`mainwp_after_system_requirements_check`](#mainwp-after-system-requirements-check) - Action: mainwp_after_system_requirements_check
- [`mainwp_automatic_disable_uptime_monitoring_check`](#mainwp-automatic-disable-uptime-monitoring-check) - Method cron_uptime_check
- [`mainwp_before_system_requirements_check`](#mainwp-before-system-requirements-check) - Action: mainwp_before_system_requirements_check
- [`mainwp_create_security_nonces`](#mainwp-create-security-nonces) - Create the security nonces.
- [`mainwp_fetch_uptime_chunk_size_urls`](#mainwp-fetch-uptime-chunk-size-urls) - Check uptime monitors.
- [`mainwp_fetch_uptime_disable_check_multi_exec`](#mainwp-fetch-uptime-disable-check-multi-exec) - Apply disable check multi exec.
- [`mainwp_http_check_email_footer`](#mainwp-http-check-email-footer) - HTTP Check Email Footer
- [`mainwp_http_check_email_header`](#mainwp-http-check-email-header) - HTTP Check Email Header
- [`mainwp_licenses_deactivated_alert_email_footer`](#mainwp-licenses-deactivated-alert-email-footer) - Site Health Monitoring Email Footer
- [`mainwp_licenses_deactivated_alert_email_header`](#mainwp-licenses-deactivated-alert-email-header) - Site Health Monitoring Email Header
- [`mainwp_logger_keep_days`](#mainwp-logger-keep-days) - Method check_log_daily()
- [`mainwp_module_cost_tracker_manager_check_status`](#mainwp-module-cost-tracker-manager-check-status) - *Arguments*
- [`mainwp_module_log_check_connector_is_excluded`](#mainwp-module-log-check-connector-is-excluded) - Allows excluded connectors to be overridden and registered.
- [`mainwp_monitoring_sitestable_getcolumns`](#mainwp-monitoring-sitestable-getcolumns) - Filter: mainwp_monitoring_sitestable_getcolumns
- [`mainwp_monitoring_sitestable_item`](#mainwp-monitoring-sitestable-item) - Filter: mainwp_monitoring_sitestable_item
- [`mainwp_monitoring_sitestable_prepare_extra_view`](#mainwp-monitoring-sitestable-prepare-extra-view) - Prepair the items to be listed.
- [`mainwp_monitoring_sitestable_prepared_items`](#mainwp-monitoring-sitestable-prepared-items) - Action: mainwp_monitoring_sitestable_prepared_items
- [`mainwp_monitoring_table_features`](#mainwp-monitoring-table-features) - Filter: mainwp_monitoring_table_features
- [`mainwp_secure_request`](#mainwp-secure-request) - Method admin_init()
- [`mainwp_security_issues_list_item_column`](#mainwp-security-issues-list-item-column) - Action: mainwp_security_issues_list_item_column
- [`mainwp_security_issues_list_item_title`](#mainwp-security-issues-list-item-title) - *Arguments*
- [`mainwp_security_issues_list_item_title_url`](#mainwp-security-issues-list-item-title-url) - *Arguments*
- [`mainwp_security_issues_stats`](#mainwp-security-issues-stats) - Filters security issues
- [`mainwp_security_issues_widget_bottom`](#mainwp-security-issues-widget-bottom) - Action: mainwp_security_issues_widget_bottom
- [`mainwp_security_issues_widget_title`](#mainwp-security-issues-widget-title) - *Arguments*
- [`mainwp_security_issues_widget_top`](#mainwp-security-issues-widget-top) - Action: mainwp_security_issues_widget_top
- [`mainwp_security_nonces`](#mainwp-security-nonces) - Method admin_init()
- [`mainwp_securityissues_sites`](#mainwp-securityissues-sites) - Action: mainwp_securityissues_sites
- [`mainwp_stats_scan_dir`](#mainwp-stats-scan-dir) - Method get_post_data_authed()
- [`mainwp_sucuriscan_sites`](#mainwp-sucuriscan-sites) - Action: mainwp_sucuriscan_sites
- [`mainwp_unset_security_scripts_stylesheets`](#mainwp-unset-security-scripts-stylesheets) - Method Fix Security Issues
- [`mainwp_uptime_monitoring_after_check_uptime`](#mainwp-uptime-monitoring-after-check-uptime) - Method handle response fetch uptime.
- [`mainwp_uptime_monitoring_allowed_methods`](#mainwp-uptime-monitoring-allowed-methods) - Method get_allowed_methods
- [`mainwp_uptime_monitoring_check_importance`](#mainwp-uptime-monitoring-check-importance) - Method handle response fetch uptime.
- [`mainwp_uptime_monitoring_check_url`](#mainwp-uptime-monitoring-check-url) - Get apply monitor url.
- [`mainwp_uptime_monitoring_email_footer`](#mainwp-uptime-monitoring-email-footer) - Uptime Monitoring Email Footer
- [`mainwp_uptime_monitoring_email_header`](#mainwp-uptime-monitoring-email-header) - Uptime Monitoring Email Header
- [`mainwp_uptime_monitoring_get_monitors_to_check_params`](#mainwp-uptime-monitoring-get-monitors-to-check-params) - Get sites monitors to check.
- [`mainwp_uptime_monitoring_interval_values`](#mainwp-uptime-monitoring-interval-values) - Method get_interval_values
- [`mainwp_uptime_monitoring_response_time_widget_title`](#mainwp-uptime-monitoring-response-time-widget-title) - *Arguments*
- [`mainwp_uptime_monitoring_send_notification_limit`](#mainwp-uptime-monitoring-send-notification-limit) - Run schedule uptime notification.
- [`mainwp_uptime_monitoring_status_widget_title`](#mainwp-uptime-monitoring-status-widget-title) - *Arguments*
- [`mainwp_uptime_monitoring_timeout_values`](#mainwp-uptime-monitoring-timeout-values) - Method get_timeout_values
- [`mainwp_uptime_monitoring_uptime_data`](#mainwp-uptime-monitoring-uptime-data) - Method handle response fetch uptime.

---

## Hook Details

<a id='mainwp-securityissues-sites'></a>
### `mainwp-securityissues-sites`

* Method render_scan_site()

Render Site Hardening sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_securityissues_sites'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 730](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L730)

---

<a id='mainwp-sucuriscan-sites'></a>
### `mainwp-sucuriscan-sites`

* Method render_scan_site()

Render Site Hardening sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_sucuriscan_sites'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 730](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L730)

---

<a id='mainwp-after-system-requirements-check'></a>
### `mainwp_after_system_requirements_check`

* Action: mainwp_after_system_requirements_check

Fires on the bottom of the System Requirements page, in Quick Setup Wizard.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 973](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L973)

---

<a id='mainwp-automatic-disable-uptime-monitoring-check'></a>
### `mainwp_automatic_disable_uptime_monitoring_check`

* Method cron_uptime_check

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-schedule.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php), [line 67](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php#L67)

---

<a id='mainwp-before-system-requirements-check'></a>
### `mainwp_before_system_requirements_check`

* Action: mainwp_before_system_requirements_check

Fires on the bottom of the System Requirements page, in Quick Setup Wizard.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 911](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L911)

---

<a id='mainwp-create-security-nonces'></a>
### `mainwp_create_security_nonces`

* Create the security nonces.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$security_names` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$security_names` |  |

**Usage Locations:**

- [class/class-mainwp-post-base-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-base-handler.php), [line 140](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-base-handler.php#L140)

---

<a id='mainwp-fetch-uptime-chunk-size-urls'></a>
### `mainwp_fetch_uptime_chunk_size_urls`

* Check uptime monitors.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 350](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L350)
- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 88](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L88)

---

<a id='mainwp-fetch-uptime-disable-check-multi-exec'></a>
### `mainwp_fetch_uptime_disable_check_multi_exec`

* Apply disable check multi exec.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Changelog**

Version | Description
------- | -----------
`5.3` |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 61](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L61)

---

<a id='mainwp-http-check-email-footer'></a>
### `mainwp_http_check_email_footer`

* HTTP Check Email Footer

Fires at the bottom of the HTTP check (after update checks) email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-after-update-http-check-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php), [line 94](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php#L94)

---

<a id='mainwp-http-check-email-header'></a>
### `mainwp_http_check_email_header`

* HTTP Check Email Header

Fires at the top of the HTTP check (after update checks) email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-after-update-http-check-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php), [line 29](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-after-update-http-check-email.php#L29)

---

<a id='mainwp-licenses-deactivated-alert-email-footer'></a>
### `mainwp_licenses_deactivated_alert_email_footer`

* Site Health Monitoring Email Footer

Fires at the bottom of the site health monitoring email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-licenses-deactivated-alert-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php), [line 97](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php#L97)

---

<a id='mainwp-licenses-deactivated-alert-email-header'></a>
### `mainwp_licenses_deactivated_alert_email_header`

* Site Health Monitoring Email Header

Fires at the top of the site health monitoring email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-licenses-deactivated-alert-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php), [line 31](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-licenses-deactivated-alert-email.php#L31)

---

<a id='mainwp-logger-keep-days'></a>
### `mainwp_logger_keep_days`

* Method check_log_daily()

Daily checks to clear the log file.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`7` |  |

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 749](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L749)

---

<a id='mainwp-module-cost-tracker-manager-check-status'></a>
### `mainwp_module_cost_tracker_manager_check_status`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [modules/cost-tracker/pages/page-cost-tracker-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-settings.php), [line 348](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-settings.php#L348)

---

<a id='mainwp-module-log-check-connector-is-excluded'></a>
### `mainwp_module_log_check_connector_is_excluded`

* Allows excluded connectors to be overridden and registered.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_excluded` | `bool` | True if excluded, otherwise false.
`$connector_name` |  | 
`$excluded_connectors` | `array` | An array of all excluded connector slugs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_excluded` | `bool` | True if excluded, otherwise false.
`$connector_name` |  | 
`$excluded_connectors` | `array` | An array of all excluded connector slugs.

**Usage Locations:**

- [modules/logs/classes/class-log-connectors.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php), [line 148](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php#L148)

---

<a id='mainwp-monitoring-sitestable-getcolumns'></a>
### `mainwp_monitoring_sitestable_getcolumns`

* Filter: mainwp_monitoring_sitestable_getcolumns

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

**Usage Locations:**

- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 185](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L185)

---

<a id='mainwp-monitoring-sitestable-item'></a>
### `mainwp_monitoring_sitestable_item`

* Filter: mainwp_monitoring_sitestable_item

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

**Usage Locations:**

- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 99](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L99)

---

<a id='mainwp-monitoring-sitestable-prepare-extra-view'></a>
### `mainwp_monitoring_sitestable_prepare_extra_view`

* Prepair the items to be listed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('favi_icon', 'health_site_status')` |  |

**Usage Locations:**

- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 409](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L409)

---

<a id='mainwp-monitoring-sitestable-prepared-items'></a>
### `mainwp_monitoring_sitestable_prepared_items`

* Action: mainwp_monitoring_sitestable_prepared_items

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

**Usage Locations:**

- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 626](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L626)

---

<a id='mainwp-monitoring-table-features'></a>
### `mainwp_monitoring_table_features`

* Filter: mainwp_monitoring_table_features

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

- [class/class-mainwp-monitoring-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php), [line 722](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-monitoring-sites-list-table.php#L722)

---

<a id='mainwp-secure-request'></a>
### `mainwp_secure_request`

* Method admin_init()

Handles the uploading of a file.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'qq_nonce'` |  | 
`'qq_nonce'` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 134](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L134)
- [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 42](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L42)

---

<a id='mainwp-security-issues-list-item-column'></a>
### `mainwp_security_issues_list_item_column`

* Action: mainwp_security_issues_list_item_column

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

**Usage Locations:**

- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 248](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L248)

---

<a id='mainwp-security-issues-list-item-title'></a>
### `mainwp_security_issues_list_item_title`

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

- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 236](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L236)

---

<a id='mainwp-security-issues-list-item-title-url'></a>
### `mainwp_security_issues_list_item_title_url`

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

- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 225](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L225)

---

<a id='mainwp-security-issues-stats'></a>
### `mainwp_security_issues_stats`

* Filters security issues

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

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 366](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L366)
- [pages/page-mainwp-security-issues.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php), [line 293](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php#L293)

---

<a id='mainwp-security-issues-widget-bottom'></a>
### `mainwp_security_issues_widget_bottom`

* Action: mainwp_security_issues_widget_bottom

Fires at the bottom of the Security Issues widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 271](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L271)

---

<a id='mainwp-security-issues-widget-title'></a>
### `mainwp_security_issues_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Site Hardening', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Site Hardening', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 98](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L98)

---

<a id='mainwp-security-issues-widget-top'></a>
### `mainwp_security_issues_widget_top`

* Action: mainwp_security_issues_widget_top

Fires at the bottom of the Security Issues widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 166](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L166)
- [widgets/widget-mainwp-security-issues-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php), [line 178](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-security-issues-widget.php#L178)

---

<a id='mainwp-security-nonces'></a>
### `mainwp_security_nonces`

* Method admin_init()

Do nothing if current user is not an Admin else display the page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 766](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L766)

---

<a id='mainwp-securityissues-sites'></a>
### `mainwp_securityissues_sites`

* Action: mainwp_securityissues_sites

Fires on a child site Hardening page at top.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 772](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L772)

---

<a id='mainwp-stats-scan-dir'></a>
### `mainwp_stats_scan_dir`

* Method get_post_data_authed()

Get authorized $_POST data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `mixed` | Array of Child Site Info.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 361](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L361)

---

<a id='mainwp-sucuriscan-sites'></a>
### `mainwp_sucuriscan_sites`

* Action: mainwp_sucuriscan_sites

Fires on a child site Hardening page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 792](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L792)

---

<a id='mainwp-unset-security-scripts-stylesheets'></a>
### `mainwp_unset_security_scripts_stylesheets`

* Method Fix Security Issues

Fix the selected security issue.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Usage Locations:**

- [pages/page-mainwp-security-issues.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php), [line 312](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php#L312)

---

<a id='mainwp-uptime-monitoring-after-check-uptime'></a>
### `mainwp_uptime_monitoring_after_check_uptime`

* Method handle response fetch uptime.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$heartbeat` |  | 
`$monitor` | `mixed` | monitor.
`$previous_heartbeat` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$heartbeat` |  | 
`$monitor` | `mixed` | monitor.
`$previous_heartbeat` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 713](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L713)

---

<a id='mainwp-uptime-monitoring-allowed-methods'></a>
### `mainwp_uptime_monitoring_allowed_methods`

* Method get_allowed_methods

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('useglobal' => esc_html__('Use global settings', 'mainwp'), 'head' => 'HEAD', 'get' => 'GET', 'post' => 'POST', 'push' => 'PUSH', 'patch' => 'PATCH', 'delete' => 'DELETE')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('useglobal' => esc_html__('Use global settings', 'mainwp'), 'head' => 'HEAD', 'get' => 'GET', 'post' => 'POST', 'push' => 'PUSH', 'patch' => 'PATCH', 'delete' => 'DELETE')` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 705](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L705)

---

<a id='mainwp-uptime-monitoring-check-importance'></a>
### `mainwp_uptime_monitoring_check_importance`

* Method handle response fetch uptime.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$importance` |  | 
`$heartbeat` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$importance` |  | 
`$heartbeat` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 713](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L713)

---

<a id='mainwp-uptime-monitoring-check-url'></a>
### `mainwp_uptime_monitoring_check_url`

* Get apply monitor url.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$url` |  | 
`$monitor` | `mixed` | monitor.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$url` |  | 
`$monitor` | `mixed` | monitor.

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 1008](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L1008)

---

<a id='mainwp-uptime-monitoring-email-footer'></a>
### `mainwp_uptime_monitoring_email_footer`

* Uptime Monitoring Email Footer

Fires at the bottom of the uptime monitoring email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-uptime-monitoring-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php), [line 144](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php#L144)

---

<a id='mainwp-uptime-monitoring-email-header'></a>
### `mainwp_uptime_monitoring_email_header`

* Uptime Monitoring Email Header

Fires at the top of the uptime monitoring email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-uptime-monitoring-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php), [line 32](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-uptime-monitoring-email.php#L32)

---

<a id='mainwp-uptime-monitoring-get-monitors-to-check-params'></a>
### `mainwp_uptime_monitoring_get_monitors_to_check_params`

* Get sites monitors to check.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | params.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | params.

**Usage Locations:**

- [class/class-mainwp-db-uptime-monitoring.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-uptime-monitoring.php), [line 418](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-uptime-monitoring.php#L418)

---

<a id='mainwp-uptime-monitoring-interval-values'></a>
### `mainwp_uptime_monitoring_interval_values`

* Method get_interval_values

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` |  | 
`$flip_values` | `mixed` | flip values.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` |  | 
`$flip_values` | `mixed` | flip values.

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 734](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L734)

---

<a id='mainwp-uptime-monitoring-response-time-widget-title'></a>
### `mainwp_uptime_monitoring_response_time_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Uptime Monitoring', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Uptime Monitoring', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-uptime-monitoring-site-widget.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php), [line 190](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-site-widget.php#L190)

---

<a id='mainwp-uptime-monitoring-send-notification-limit'></a>
### `mainwp_uptime_monitoring_send_notification_limit`

* Run schedule uptime notification.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-schedule.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php), [line 173](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-schedule.php#L173)

---

<a id='mainwp-uptime-monitoring-status-widget-title'></a>
### `mainwp_uptime_monitoring_status_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Uptime Monitoring', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Uptime Monitoring', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-uptime-monitoring-status.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-status.php), [line 51](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-uptime-monitoring-status.php#L51)

---

<a id='mainwp-uptime-monitoring-timeout-values'></a>
### `mainwp_uptime_monitoring_timeout_values`

* Method get_timeout_values

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` |  | 
`$flip_values` | `mixed` | flip values.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` |  | 
`$flip_values` | `mixed` | flip values.

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 767](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L767)

---

<a id='mainwp-uptime-monitoring-uptime-data'></a>
### `mainwp_uptime_monitoring_uptime_data`

* Method handle response fetch uptime.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$heartbeat` |  | 
`$monitor` | `mixed` | monitor.
`$previous_heartbeat` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$heartbeat` |  | 
`$monitor` | `mixed` | monitor.
`$previous_heartbeat` |  |

**Usage Locations:**

- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 713](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L713)

---


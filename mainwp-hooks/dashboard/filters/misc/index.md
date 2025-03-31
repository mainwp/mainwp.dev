# Miscellaneous Filters

Miscellaneous hooks that don't fit into other categories.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`admin_print_styles`](#admin-print-styles) - Method setup_wizard_header()
- [`date_formats`](#date-formats) - *Arguments*
- [`error_log_mainwp_logs`](#error-log-mainwp-logs) - Filter: error_log_mainwp_logs
- [`mainwp_admin_enqueue_scripts`](#mainwp-admin-enqueue-scripts) - Method admin_enqueue_scripts()
- [`mainwp_after_header`](#mainwp-after-header) - Action: mainwp_after_header
- [`mainwp_after_seclect_sites`](#mainwp-after-seclect-sites) - Action: mainwp_after_seclect_sites
- [`mainwp_after_subheader`](#mainwp-after-subheader) - Action: mainwp_after_subheader
- [`mainwp_after_template_part`](#mainwp-after-template-part) - Action: mainwp_after_template_part
- [`mainwp_ajax_add_action`](#mainwp-ajax-add-action) - Init ajax actions.
- [`mainwp_before_header`](#mainwp-before-header) - Action: mainwp_before_header
- [`mainwp_before_seclect_sites`](#mainwp-before-seclect-sites) - Action: mainwp_before_seclect_sites
- [`mainwp_before_subheader`](#mainwp-before-subheader) - Action: mainwp_before_subheader
- [`mainwp_before_template_part`](#mainwp-before-template-part) - Action: mainwp_before_template_part
- [`mainwp_clone_enabled`](#mainwp-clone-enabled) - Filter: mainwp_clone_enabled
- [`mainwp_cronload_action`](#mainwp-cronload-action) - Action: mainwp_cronload_action
- [`mainwp_curl_curlopt_resolve`](#mainwp-curl-curlopt-resolve) - Method try visit.
- [`mainwp_daily_digest_action`](#mainwp-daily-digest-action) - Action: mainwp_daily_digest_action
- [`mainwp_daily_digest_email_footer`](#mainwp-daily-digest-email-footer) - Daily Digest Email Footer
- [`mainwp_daily_digest_email_header`](#mainwp-daily-digest-email-header) - Daily Digest Email Header
- [`mainwp_db_fetch_object`](#mainwp-db-fetch-object) - Method fetch_object().
- [`mainwp_db_free_result`](#mainwp-db-free-result) - Method free_result().
- [`mainwp_default_template_source_dir`](#mainwp-default-template-source-dir) - Method handle_template_file_action()
- [`mainwp_fetch_urls_chunk_size`](#mainwp-fetch-urls-chunk-size) - Method fetch_urls_authed()
- [`mainwp_file_uploader_chunk_size`](#mainwp-file-uploader-chunk-size) - Method render_upload()
- [`mainwp_file_uploader_size_limit`](#mainwp-file-uploader-size-limit) - Filter: 'mainwp_file_uploader_size_limit'
- [`mainwp_format_email`](#mainwp-format-email) - Method format_email()
- [`mainwp_ga_delete_site`](#mainwp-ga-delete-site) - Action: mainwp_ga_delete_site
- [`mainwp_get_notification_template_name_by_type`](#mainwp-get-notification-template-name-by-type) - Get default template name by email/notification type.
- [`mainwp_get_template`](#mainwp-get-template) - Filter: mainwp_get_template
- [`mainwp_go_back_wpadmin_link`](#mainwp-go-back-wpadmin-link) - Filter: mainwp_go_back_wpadmin_link
- [`mainwp_header_actions_right`](#mainwp-header-actions-right) - Filter: mainwp_header_actions_right
- [`mainwp_is_enable_schedule_job`](#mainwp-is-enable-schedule-job) - Method init_mainwp_cron()
- [`mainwp_license_deactivated_alert_plain_text`](#mainwp-license-deactivated-alert-plain-text) - Method cron_deactivated_licenses_alert()
- [`mainwp_locate_template`](#mainwp-locate-template) - Filer: mainwp_locate_template
- [`mainwp_log_action`](#mainwp-log-action) - Schedules a purge of records.
- [`mainwp_log_specific`](#mainwp-log-specific) - MainWP_Logger constructor.
- [`mainwp_log_status`](#mainwp-log-status) - MainWP_Logger constructor.
- [`mainwp_logger_to_db`](#mainwp-logger-to-db) - Method log()
- [`mainwp_module_log_after_connectors_registration`](#mainwp-module-log-after-connectors-registration) - Fires after all connectors have been registered.
- [`mainwp_module_log_agent_label`](#mainwp-module-log-agent-label) - Filter agent labels
- [`mainwp_module_log_connectors`](#mainwp-module-log-connectors) - Allows for adding additional connectors via classes that extend Connector.
- [`mainwp_module_log_current_agent`](#mainwp-module-log-current-agent) - Filter the current agent string
- [`mainwp_module_log_query_args`](#mainwp-module-log-query-args) - Filter allows additional arguments to query $args
- [`mainwp_module_log_record_array`](#mainwp-module-log-record-array) - Filter allows modification of record information
- [`mainwp_module_log_record_insert_error`](#mainwp-module-log-record-insert-error) - Fires on a record insertion error
- [`mainwp_module_log_record_inserted`](#mainwp-module-log-record-inserted) - Fires after a record has been inserted
- [`mainwp_module_monthly_renewals_after_costs_list`](#mainwp-module-monthly-renewals-after-costs-list) - Action: mainwp_module_monthly_renewals_after_costs_list
- [`mainwp_module_monthly_renewals_before_costs_list`](#mainwp-module-monthly-renewals-before-costs-list) - Action: mainwp_module_monthly_renewals_before_costs_list
- [`mainwp_module_upcoming_renewals_after_costs_list`](#mainwp-module-upcoming-renewals-after-costs-list) - Action: mainwp_module_upcoming_renewals_after_costs_list
- [`mainwp_module_upcoming_renewals_before_costs_list`](#mainwp-module-upcoming-renewals-before-costs-list) - Action: mainwp_module_upcoming_renewals_before_costs_list
- [`mainwp_module_yearly_renewals_after_costs_list`](#mainwp-module-yearly-renewals-after-costs-list) - Action: mainwp_module_yearly_renewals_after_costs_list
- [`mainwp_module_yearly_renewals_before_costs_list`](#mainwp-module-yearly-renewals-before-costs-list) - Action: mainwp_module_yearly_renewals_before_costs_list
- [`mainwp_notification_template_copy_message`](#mainwp-notification-template-copy-message) - Filter mainwp_notification_template_copy_message.
- [`mainwp_notification_types`](#mainwp-notification-types) - Get email notification types.
- [`mainwp_open_hide_referrer`](#mainwp-open-hide-referrer) - Filter: mainwp_open_hide_referrer
- [`mainwp_register_regular_sequence_process`](#mainwp-register-regular-sequence-process) - Method perform_sequence_process
- [`mainwp_send_mail_from_header`](#mainwp-send-mail-from-header) - Method send_wp_mail().
- [`mainwp_subheader_actions`](#mainwp-subheader-actions) - Action: mainwp_subheader_actions
- [`mainwp_text_format_email`](#mainwp-text-format-email) - Filter: mainwp_text_format_email
- [`mainwp_tools_form_bottom`](#mainwp-tools-form-bottom) - Action: mainwp_tools_form_bottom
- [`mainwp_tools_form_top`](#mainwp-tools-form-top) - Action: mainwp_tools_form_top
- [`mainwp_try_visit_follow_location`](#mainwp-try-visit-follow-location) - Method try visit.
- [`minwp_notification_template_copy_message`](#minwp-notification-template-copy-message) - Use mainwp_notification_template_copy_message instead.
- [`time_formats`](#time-formats) - *Arguments*
- [`{$filter}`](#filter) - Method apply_filter()

---

## Hook Details

<a id='admin-print-styles'></a>
### `admin_print_styles`

* Method setup_wizard_header()

Render Setup Wizard's header.

**Usage Locations:**

- [pages/page-mainwp-setup-wizard.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-setup-wizard.php), [line 203](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-setup-wizard.php#L203)

---

<a id='date-formats'></a>
### `date_formats`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`array(esc_html__('F j, Y'), 'Y-m-d', 'm/d/Y', 'd/m/Y')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(esc_html__('F j, Y'), 'Y-m-d', 'm/d/Y', 'd/m/Y')` |  |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1139](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1139)

---

<a id='error-log-mainwp-logs'></a>
### `error_log_mainwp_logs`

* Filter: error_log_mainwp_logs

Filters the error log files to show.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($error_log)` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1534](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1534)

---

<a id='mainwp-admin-enqueue-scripts'></a>
### `mainwp_admin_enqueue_scripts`

* Method admin_enqueue_scripts()

Enqueue all Mainwp Admin Scripts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 1053](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L1053)

---

<a id='mainwp-after-header'></a>
### `mainwp_after_header`

* Action: mainwp_after_header

Fires after the MainWP header element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1072](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1072)

---

<a id='mainwp-after-seclect-sites'></a>
### `mainwp_after_seclect_sites`

* Action: mainwp_after_seclect_sites

Fires after the Select Sites box.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 124](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L124)
- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 85](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L85)

---

<a id='mainwp-after-subheader'></a>
### `mainwp_after_subheader`

* Action: mainwp_after_subheader

Fires after the MainWP sub-header element.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1201](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1201)

---

<a id='mainwp-after-template-part'></a>
### `mainwp_after_template_part`

* Action: mainwp_after_template_part

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

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 181](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L181)

---

<a id='mainwp-ajax-add-action'></a>
### `mainwp_ajax_add_action`

* Init ajax actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'vultr_action_create_snapshot'` |  | 
`array(&$this, 'ajax_vultr_action_create_snapshot')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'vultr_action_create_snapshot'` |  | 
`array(&$this, 'ajax_vultr_action_create_snapshot')` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-3rd-party.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php), [line 100](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php#L100)

---

<a id='mainwp-before-header'></a>
### `mainwp_before_header`

* Action: mainwp_before_header

Fires before the MainWP header element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 866](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L866)

---

<a id='mainwp-before-seclect-sites'></a>
### `mainwp_before_seclect_sites`

* Action: mainwp_before_seclect_sites

Fires before the Select Sites box.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 96](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L96)
- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 72](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L72)

---

<a id='mainwp-before-subheader'></a>
### `mainwp_before_subheader`

* Action: mainwp_before_subheader

Fires before the MainWP sub-header element.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1152](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1152)

---

<a id='mainwp-before-template-part'></a>
### `mainwp_before_template_part`

* Action: mainwp_before_template_part

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

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 166](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L166)

---

<a id='mainwp-clone-enabled'></a>
### `mainwp_clone_enabled`

* Filter: mainwp_clone_enabled

Filters whether the Clone feature is enabled or disabled.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-sync.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php), [line 104](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-sync.php#L104)

---

<a id='mainwp-cronload-action'></a>
### `mainwp_cronload_action`

* Action: mainwp_cronload_action

Hooks MainWP cron jobs actions.

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 61](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L61)

---

<a id='mainwp-curl-curlopt-resolve'></a>
### `mainwp_curl_curlopt_resolve`

* Method try visit.

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`false` |  | 
`$url` | `string` | Child Site URL.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 1351](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L1351)
- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 32](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L32)
- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 688](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L688)

---

<a id='mainwp-daily-digest-action'></a>
### `mainwp_daily_digest_action`

* Action: mainwp_daily_digest_action

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

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 1038](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L1038)

---

<a id='mainwp-daily-digest-email-footer'></a>
### `mainwp_daily_digest_email_footer`

* Daily Digest Email Footer

Fires at the bottom of the daily digest email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-daily-digest-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php), [line 177](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php#L177)

---

<a id='mainwp-daily-digest-email-header'></a>
### `mainwp_daily_digest_email_header`

* Daily Digest Email Header

Fires at the top of the daily digest email template.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [templates/emails/mainwp-daily-digest-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php), [line 29](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php#L29)

---

<a id='mainwp-db-fetch-object'></a>
### `mainwp_db_fetch_object`

* Method fetch_object().

Handle fetch object db.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$websites` | `mixed` | websites results.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 104](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L104)

---

<a id='mainwp-db-free-result'></a>
### `mainwp_db_free_result`

* Method free_result().

Handle fetch result db.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$results` | `mixed` | websites results.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-helper.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php), [line 118](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-helper.php#L118)

---

<a id='mainwp-default-template-source-dir'></a>
### `mainwp_default_template_source_dir`

* Method handle_template_file_action()

Handle template file action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template_path` |  | 
`$templ_base_name` |  |

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 318](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L318)

---

<a id='mainwp-fetch-urls-chunk-size'></a>
### `mainwp_fetch_urls_chunk_size`

* Method fetch_urls_authed()

Fetches data from child sites if authenticated.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$chunkSize` |  |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 688](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L688)

---

<a id='mainwp-file-uploader-chunk-size'></a>
### `mainwp_file_uploader_chunk_size`

* Method render_upload()

Renders the upload sub part.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1000000` |  |

**Usage Locations:**

- [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 67](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L67)

---

<a id='mainwp-file-uploader-size-limit'></a>
### `mainwp_file_uploader_size_limit`

* Filter: 'mainwp_file_uploader_size_limit'

Filters the maximum upload file size. Default: 8388608 Bytes (B) = 8 Megabytes (MB)

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sizeLimit` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-qq2-file-uploader.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-qq2-file-uploader.php), [line 56](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-qq2-file-uploader.php#L56)

---

<a id='mainwp-format-email'></a>
### `mainwp_format_email`

* Method format_email()

Format email.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mail_send` |  |

**Usage Locations:**

- [class/class-mainwp-format.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-format.php), [line 212](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-format.php#L212)

---

<a id='mainwp-ga-delete-site'></a>
### `mainwp_ga_delete_site`

* Action: mainwp_ga_delete_site

Fires upon site removal process in order to delete Google Analytics data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websiteid` | `int` | Child site ID.

**Usage Locations:**

- [class/class-mainwp-db.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php), [line 2611](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php#L2611)

---

<a id='mainwp-get-notification-template-name-by-type'></a>
### `mainwp_get_notification_template_name_by_type`

* Get default template name by email/notification type.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | email/notification type.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | email/notification type.

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 293](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L293)

---

<a id='mainwp-get-template'></a>
### `mainwp_get_template`

* Filter: mainwp_get_template

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

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 140](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L140)

---

<a id='mainwp-go-back-wpadmin-link'></a>
### `mainwp_go_back_wpadmin_link`

* Filter: mainwp_go_back_wpadmin_link

Filters URL for the Go to WP Admin button in Main navigation.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$link` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 1242](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L1242)
- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 799](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L799)

---

<a id='mainwp-header-actions-right'></a>
### `mainwp_header_actions_right`

* Filter: mainwp_header_actions_right

Filters the MainWP header element actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1345](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1345)

---

<a id='mainwp-is-enable-schedule-job'></a>
### `mainwp_is_enable_schedule_job`

* Method init_mainwp_cron()

Schedual Cron Jobs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$useWPCron` | `mixed` | Wether or not to use WP_Cron.
`$cron_hook` | `mixed` | When cron is going to reoccur.
`$recurrence` | `mixed` | Cron job hook.

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 147](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L147)

---

<a id='mainwp-license-deactivated-alert-plain-text'></a>
### `mainwp_license_deactivated_alert_plain_text`

* Method cron_deactivated_licenses_alert()

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plain_text` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plain_text` |  |

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 1356](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L1356)

---

<a id='mainwp-locate-template'></a>
### `mainwp_locate_template`

* Filer: mainwp_locate_template

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

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 265](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L265)

---

<a id='mainwp-log-action'></a>
### `mainwp_log_action`

* Schedules a purge of records.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'module log :: purge logs schedule start.'` |  | 
`MainWP_Logger::LOGS_AUTO_PURGE_LOG_PRIORITY` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'module log :: purge logs schedule start.'` |  | 
`MainWP_Logger::LOGS_AUTO_PURGE_LOG_PRIORITY` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-utility.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php), [line 173](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php#L173)
- [modules/logs/classes/class-log-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php), [line 192](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php#L192)

---

<a id='mainwp-log-specific'></a>
### `mainwp_log_specific`

* MainWP_Logger constructor.

Run each time the class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific` |  |

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 129](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L129)

---

<a id='mainwp-log-status'></a>
### `mainwp_log_status`

* MainWP_Logger constructor.

Run each time the class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$enabled` |  |

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 129](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L129)

---

<a id='mainwp-logger-to-db'></a>
### `mainwp_logger_to_db`

* Method log()

Create Log File.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$website` | `mixed` | Site object.

**Usage Locations:**

- [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 502](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L502)

---

<a id='mainwp-module-log-after-connectors-registration'></a>
### `mainwp_module_log_after_connectors_registration`

* Fires after all connectors have been registered.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$labels` | `array` | All register connectors labels array
`$this` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$labels` | `array` | All register connectors labels array
`$this` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-connectors.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php), [line 179](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php#L179)

---

<a id='mainwp-module-log-agent-label'></a>
### `mainwp_module_log_agent_label`

* Filter agent labels

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$label` |  | 
`$agent` | `string` | Key representing agent.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$label` |  | 
`$agent` | `string` | Key representing agent.

**Usage Locations:**

- [modules/logs/classes/class-log-author.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php), [line 269](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php#L269)

---

<a id='mainwp-module-log-connectors'></a>
### `mainwp_module_log_connectors`

* Allows for adding additional connectors via classes that extend Connector.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$classes` | `array` | An array of Connector objects.
`$this->manager->log` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$classes` | `array` | An array of Connector objects.
`$this->manager->log` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-connectors.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php), [line 97](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php#L97)

---

<a id='mainwp-module-log-current-agent'></a>
### `mainwp_module_log_current_agent`

* Filter the current agent string

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$agent` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$agent` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-author.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php), [line 241](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php#L241)

---

<a id='mainwp-module-log-query-args'></a>
### `mainwp_module_log_query_args`

* Filter allows additional arguments to query $args

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 162](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L162)

---

<a id='mainwp-module-log-record-array'></a>
### `mainwp_module_log_record_array`

* Filter allows modification of record information

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` |

**Usage Locations:**

- [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L59)

---

<a id='mainwp-module-log-record-insert-error'></a>
### `mainwp_module_log_record_insert_error`

* Fires on a record insertion error

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` | 
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` | 
`false` |  |

**Usage Locations:**

- [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 77](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L77)

---

<a id='mainwp-module-log-record-inserted'></a>
### `mainwp_module_log_record_inserted`

* Fires after a record has been inserted

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record_id` | `int` | 
`$record` | `array` |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record_id` | `int` | 
`$record` | `array` |

**Usage Locations:**

- [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 88](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L88)

---

<a id='mainwp-module-monthly-renewals-after-costs-list'></a>
### `mainwp_module_monthly_renewals_after_costs_list`

* Action: mainwp_module_monthly_renewals_after_costs_list

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

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 240](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L240)

---

<a id='mainwp-module-monthly-renewals-before-costs-list'></a>
### `mainwp_module_monthly_renewals_before_costs_list`

* Action: mainwp_module_monthly_renewals_before_costs_list

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

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php), [line 190](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-monthly-renewals.php#L190)

---

<a id='mainwp-module-upcoming-renewals-after-costs-list'></a>
### `mainwp_module_upcoming_renewals_after_costs_list`

* Action: mainwp_module_upcoming_renewals_after_costs_list

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

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 223](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L223)

---

<a id='mainwp-module-upcoming-renewals-before-costs-list'></a>
### `mainwp_module_upcoming_renewals_before_costs_list`

* Action: mainwp_module_upcoming_renewals_before_costs_list

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

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php), [line 185](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-upcoming-renewals.php#L185)

---

<a id='mainwp-module-yearly-renewals-after-costs-list'></a>
### `mainwp_module_yearly_renewals_after_costs_list`

* Action: mainwp_module_yearly_renewals_after_costs_list

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

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 243](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L243)

---

<a id='mainwp-module-yearly-renewals-before-costs-list'></a>
### `mainwp_module_yearly_renewals_before_costs_list`

* Action: mainwp_module_yearly_renewals_before_costs_list

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

**Usage Locations:**

- [modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php), [line 193](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/widgets/widget-cost-tracker-yearly-renewals.php#L193)

---

<a id='mainwp-notification-template-copy-message'></a>
### `mainwp_notification_template_copy_message`

* Filter mainwp_notification_template_copy_message.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$copy_message` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$copy_message` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 337](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L337)

---

<a id='mainwp-notification-types'></a>
### `mainwp_notification_types`

* Get email notification types.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$type` | `string` | Email notification type.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$type` | `string` | Email notification type.

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L426)

---

<a id='mainwp-open-hide-referrer'></a>
### `mainwp_open_hide_referrer`

* Filter: mainwp_open_hide_referrer

Filters whether the MainWP should hide referrer when going to child site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-system-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php), [line 823](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php#L823)

---

<a id='mainwp-register-regular-sequence-process'></a>
### `mainwp_register_regular_sequence_process`

* Method perform_sequence_process

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 1692](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L1692)

---

<a id='mainwp-send-mail-from-header'></a>
### `mainwp_send_mail_from_header`

* Method send_wp_mail().

Send email via wp_mail().

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$email` | `string` | send to email.
`$subject` | `string` | email content.

**Usage Locations:**

- [class/class-mainwp-notification.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification.php), [line 317](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification.php#L317)

---

<a id='mainwp-subheader-actions'></a>
### `mainwp_subheader_actions`

* Action: mainwp_subheader_actions

Fires at the subheader element to hook available actions.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1188](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1188)

---

<a id='mainwp-text-format-email'></a>
### `mainwp_text_format_email`

* Filter: mainwp_text_format_email

Filters whether the email shuld bein plain text format.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plain_text` |  |

**Changelog**

Version | Description
------- | -----------
`3.5` |

**Usage Locations:**

- [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 629](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L629)

---

<a id='mainwp-tools-form-bottom'></a>
### `mainwp_tools_form_bottom`

* Action: mainwp_tools_form_bottom

Fires at the bottom of mainwp tools form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 2132](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L2132)

---

<a id='mainwp-tools-form-top'></a>
### `mainwp_tools_form_top`

* Action: mainwp_tools_form_top

Fires at the top of MainWP tools form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1995](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1995)

---

<a id='mainwp-try-visit-follow-location'></a>
### `mainwp_try_visit_follow_location`

* Method try visit.

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 32](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L32)

---

<a id='minwp-notification-template-copy-message'></a>
### `minwp_notification_template_copy_message`

* Use mainwp_notification_template_copy_message instead.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 330](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L330)

---

<a id='time-formats'></a>
### `time_formats`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`array(esc_html__('g:i a'), 'g:i A', 'H:i')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(esc_html__('g:i a'), 'g:i A', 'H:i')` |  |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1179](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1179)

---

<a id='filter'></a>
### `{$filter}`

* Method apply_filter()

Apply filter

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` | `array` | Input value.

**Usage Locations:**

- [class/class-mainwp-system-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php), [line 188](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php#L188)

---


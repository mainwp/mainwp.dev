# API & Remote Communication Filters

Hooks for API endpoints and remote communication with child sites.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-activated`](#mainwp-activated) - MainWP_System constructor.
- [`mainwp_cronload_action`](#mainwp_cronload_action) - Action: mainwp_cronload_action
- [`mainwp_before_template_part`](#mainwp_before_template_part) - Action: mainwp_before_template_part
- [`mainwp_after_template_part`](#mainwp_after_template_part) - Action: mainwp_after_template_part
- [`mainwp_daily_digest_email_header`](#mainwp_daily_digest_email_header) - Daily Digest Email Header
- [`mainwp_daily_digest_email_footer`](#mainwp_daily_digest_email_footer) - Daily Digest Email Footer
- [`cloudways_api_form_top`](#cloudways_api_form_top) - Action: cloudways_api_form_top
- [`cloudways_api_form_bottom`](#cloudways_api_form_bottom) - Action: cloudways_api_form_bottom
- [`gridpane_api_form_top`](#gridpane_api_form_top) - Action: gridpane_api_form_top
- [`gridpane_api_form_bottom`](#gridpane_api_form_bottom) - Action: gridpane_api_form_bottom
- [`vultr_api_form_top`](#vultr_api_form_top) - Action: vultr_api_form_top
- [`vultr_api_form_bottom`](#vultr_api_form_bottom) - Action: vultr_api_form_bottom
- [`linode_api_form_top`](#linode_api_form_top) - Action: linode_api_form_top
- [`linode_api_form_bottom`](#linode_api_form_bottom) - Action: linode_api_form_bottom
- [`digitalocean_api_form_top`](#digitalocean_api_form_top) - Action: digitalocean_api_form_top
- [`digitalocean_api_form_bottom`](#digitalocean_api_form_bottom) - Action: digitalocean_api_form_bottom
- [`cpanel_api_form`](#cpanel_api_form) - Action: cpanel_api_form
- [`cpanel_api_form_bottom`](#cpanel_api_form_bottom) - Action: cpanel_api_form_bottom
- [`plesk_api_form_top`](#plesk_api_form_top) - Action: plesk_api_form_top
- [`plesk_api_form_bottom`](#plesk_api_form_bottom) - Action: plesk_api_form_bottom
- [`kinsta_api_form_top`](#kinsta_api_form_top) - Action: kinsta_api_form_top
- [`kinsta_api_form_bottom`](#kinsta_api_form_bottom) - Action: kinsta_api_form_bottom
- [`mainwp_module_log_record_insert_error`](#mainwp_module_log_record_insert_error) - Fires on a record insertion error
- [`mainwp_module_log_record_inserted`](#mainwp_module_log_record_inserted) - Fires after a record has been inserted
- [`mainwp_log_action`](#mainwp_log_action) - Schedules a purge of records.
- [`mainwp_module_log_after_connectors_registration`](#mainwp_module_log_after_connectors_registration) - Fires after all connectors have been registered.
- [`rest_api_form_top`](#rest_api_form_top) - Action: rest_api_form_top
- [`rest_api_form_bottom`](#rest_api_form_bottom) - Action: rest_api_form_bottom
- [`mainwp_rest_api_help_item`](#mainwp_rest_api_help_item) - Action: mainwp_rest_api_help_item
- [`mainwp_is_rest_api_request`](#mainwp_is_rest_api_request) - Whether this is a REST API request.
- [`mainwp_rest_is_request_to_rest_api`](#mainwp_rest_is_request_to_rest_api) - Check if is request to our REST API.
- [`mainwp_rest_api_v2_enabled`](#mainwp_rest_api_v2_enabled) - Hook into WordPress ready to init the REST API as needed.
- [`mainwp_rest_api_get_rest_namespaces`](#mainwp_rest_api_get_rest_namespaces) - Get API namespaces - new namespaces should be registered here.
- [`mainwp_rest_api_disabled`](#mainwp_rest_api_disabled) - Method is_rest_api_enabled()
- [`mainwp_rest_batch_items_limit`](#mainwp_rest_batch_items_limit) - Check batch limit.
- [`mainwp_rest_{$type}_object_query`](#mainwp_rest_type_object_query) - Filter the query arguments for a request.
- [`mainwp_rest_collection_params`](#mainwp_rest_collection_params) - Filter collection parameters for the controller.
- [`mainwp_rest_batch_items_limit`](#mainwp_rest_batch_items_limit) - Check batch limit.
- [`mainwp_rest_prepare_site`](#mainwp_rest_prepare_site) - Filterobject returned from the REST API.
- [`mainwp_admin_enqueue_scripts`](#mainwp_admin_enqueue_scripts) - Method admin_enqueue_scripts()
- [`minwp_notification_template_copy_message`](#minwp_notification_template_copy_message) - Use mainwp_notification_template_copy_message instead.
- [`mainwp_notification_template_copy_message`](#mainwp_notification_template_copy_message) - Filter mainwp_notification_template_copy_message.
- [`mainwp_notification_type_desc`](#mainwp_notification_type_desc) - Get email settings description.
- [`mainwp_notification_types`](#mainwp_notification_types) - Get email notification types.
- [`mainwp_default_emails_fields`](#mainwp_default_emails_fields) - Get default email notifications values.
- [`{$filter}`](#filter) - Method apply_filter()
- [`mainwp_log_status`](#mainwp_log_status) - MainWP_Logger constructor.
- [`mainwp_log_specific`](#mainwp_log_specific) - MainWP_Logger constructor.
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Fetch uptime urls.
- [`mainwp_file_uploader_size_limit`](#mainwp_file_uploader_size_limit) - Filter: 'mainwp_file_uploader_size_limit'
- [`mainwp_format_email`](#mainwp_format_email) - Method format_email()
- [`mainwp_remote_destination_info`](#mainwp_remote_destination_info) - Method mainwp_backup_upload_checkstatus()
- [`mainwp_open_hide_referrer`](#mainwp_open_hide_referrer) - Filter: mainwp_open_hide_referrer
- [`mainwp_is_enable_schedule_job`](#mainwp_is_enable_schedule_job) - Method init_mainwp_cron()
- [`mainwp_text_format_email`](#mainwp_text_format_email) - Filter: mainwp_text_format_email
- [`mainwp_license_deactivated_alert_plain_text`](#mainwp_license_deactivated_alert_plain_text) - Method cron_deactivated_licenses_alert()
- [`mainwp_register_regular_sequence_process`](#mainwp_register_regular_sequence_process) - Method perform_sequence_process
- [`mainwp_try_visit_follow_location`](#mainwp_try_visit_follow_location) - Method try visit.
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Method try visit.
- [`mainwp_curl_curlopt_resolve`](#mainwp_curl_curlopt_resolve) - Method try visit.
- [`mainwp_fetch_urls_chunk_size`](#mainwp_fetch_urls_chunk_size) - Method fetch_urls_authed()
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Method fetch_urls_authed()
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Method fetch_url_site()
- [`mainwp_get_template`](#mainwp_get_template) - Filter: mainwp_get_template
- [`mainwp_locate_template`](#mainwp_locate_template) - Filer: mainwp_locate_template
- [`mainwp_get_notification_template_name_by_type`](#mainwp_get_notification_template_name_by_type) - Get default template name by email/notification type.
- [`mainwp_default_template_source_dir`](#mainwp_default_template_source_dir) - Method handle_template_file_action()
- [`mainwp_module_log_record_array`](#mainwp_module_log_record_array) - Filter allows modification of record information
- [`mainwp_module_log_query_args`](#mainwp_module_log_query_args) - Filter allows additional arguments to query $args
- [`mainwp_module_log_current_agent`](#mainwp_module_log_current_agent) - Filter the current agent string
- [`mainwp_module_log_agent_label`](#mainwp_module_log_agent_label) - Filter agent labels
- [`mainwp_module_log_connectors`](#mainwp_module_log_connectors) - Allows for adding additional connectors via classes that extend Connector.
- [`mainwp_rest_api_enabled`](#mainwp_rest_api_enabled) - Method init_rest_api()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_all_costs_callback()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_client_costs_callback()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_site_costs_callback()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_costs_callback()
- [`mainwp_rest_cost_collection_params`](#mainwp_rest_cost_collection_params) - Filter collection parameters.
- [`mainwp_rest_prepare_cost`](#mainwp_rest_prepare_cost) - Filter product reviews object returned from the REST API.
- [`https_local_ssl_verify`](#https_local_ssl_verify) - *Arguments*

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

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 82](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L82)



### `mainwp_cronload_action`

*Action: mainwp_cronload_action*

Hooks MainWP cron jobs actions.


Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 61](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L61)



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

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 166](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L166)



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

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 181](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L181)



### `mainwp_daily_digest_email_header`

*Daily Digest Email Header*

Fires at the top of the daily digest email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-daily-digest-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php), [line 29](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php#L29)



### `mainwp_daily_digest_email_footer`

*Daily Digest Email Footer*

Fires at the bottom of the daily digest email template.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [templates/emails/mainwp-daily-digest-email.php](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php), [line 177](https://github.com/mainwp/mainwp/blob/master/templates/emails/mainwp-daily-digest-email.php#L177)



### `cloudways_api_form_top`

*Action: cloudways_api_form_top*

Fires at the top of CloudWays API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 274](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L274)



### `cloudways_api_form_bottom`

*Action: cloudways_api_form_bottom*

Fires at the bottom of CloudWays API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 317](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L317)



### `gridpane_api_form_top`

*Action: gridpane_api_form_top*

Fires at the top of GridPane API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 350](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L350)



### `gridpane_api_form_bottom`

*Action: gridpane_api_form_bottom*

Fires at the bottom of GridPane API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 383](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L383)



### `vultr_api_form_top`

*Action: vultr_api_form_top*

Fires at the top of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 417](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L417)



### `vultr_api_form_bottom`

*Action: vultr_api_form_bottom*

Fires at the bottom of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 450](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L450)



### `linode_api_form_top`

*Action: linode_api_form_top*

Fires at the top of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 483](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L483)



### `linode_api_form_bottom`

*Action: linode_api_form_bottom*

Fires at the bottom of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 518](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L518)



### `digitalocean_api_form_top`

*Action: digitalocean_api_form_top*

Fires at the top of DigitalOcean API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 551](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L551)



### `digitalocean_api_form_bottom`

*Action: digitalocean_api_form_bottom*

Fires at the bottom of DigitalOcean API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 586](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L586)



### `cpanel_api_form`

*Action: cpanel_api_form*

Fires at the top of cPanel API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 618](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L618)



### `cpanel_api_form_bottom`

*Action: cpanel_api_form_bottom*

Fires at the bottom of cPanel API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 685](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L685)



### `plesk_api_form_top`

*Action: plesk_api_form_top*

Fires at the top of Plesk API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 718](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L718)



### `plesk_api_form_bottom`

*Action: plesk_api_form_bottom*

Fires at the bottom of Plesk API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 762](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L762)



### `kinsta_api_form_top`

*Action: kinsta_api_form_top*

Fires at the top of Kinsta API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 795](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L795)



### `kinsta_api_form_bottom`

*Action: kinsta_api_form_bottom*

Fires at the bottom of Kinsta API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 851](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L851)



### `mainwp_module_log_record_insert_error`

*Fires on a record insertion error*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` | 
`false` |  | 

Source: [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 77](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L77)



### `mainwp_module_log_record_inserted`

*Fires after a record has been inserted*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record_id` | `int` | 
`$record` | `array` | 

Source: [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 88](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L88)



### `mainwp_log_action`

*Schedules a purge of records.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'module log :: purge logs schedule start.'` |  | 
`MainWP_Logger::LOGS_AUTO_PURGE_LOG_PRIORITY` |  | 

Source: [modules/logs/classes/class-log-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php), [line 192](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-admin.php#L192)



### `mainwp_module_log_after_connectors_registration`

*Fires after all connectors have been registered.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$labels` | `array` | All register connectors labels array
`$this` |  | 

Source: [modules/logs/classes/class-log-connectors.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php), [line 179](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php#L179)



### `rest_api_form_top`

*Action: rest_api_form_top*

Fires at the top of REST API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 850](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L850)



### `rest_api_form_bottom`

*Action: rest_api_form_bottom*

Fires at the bottom of REST API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 936](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L936)



### `mainwp_rest_api_help_item`

*Action: mainwp_rest_api_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the REST API page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 1260](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L1260)



### `mainwp_is_rest_api_request`

*Whether this is a REST API request.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_rest_api_request` |  | 

**Changelog**

Version | Description
------- | -----------
`5.1.1` | 

Source: [includes/class-mainwp-setup.php](https://github.com/mainwp/mainwp/blob/master/includes/class-mainwp-setup.php), [line 81](https://github.com/mainwp/mainwp/blob/master/includes/class-mainwp-setup.php#L81)



### `mainwp_rest_is_request_to_rest_api`

*Check if is request to our REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_api || $extension_api` |  | 

Source: [includes/rest-api/class-mainwp-rest-authentication.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-authentication.php), [line 89](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-authentication.php#L89)



### `mainwp_rest_api_v2_enabled`

*Hook into WordPress ready to init the REST API as needed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [includes/rest-api/class-mainwp-rest-server.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php), [line 47](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php#L47)



### `mainwp_rest_api_get_rest_namespaces`

*Get API namespaces - new namespaces should be registered here.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('mainwp/v2' => $this->get_v2_controllers())` |  | 

Source: [includes/rest-api/class-mainwp-rest-server.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php), [line 89](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php#L89)



### `mainwp_rest_api_disabled`

*Method is_rest_api_enabled()*

Check if Enabled the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 92](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L92)



### `mainwp_rest_batch_items_limit`

*Check batch limit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 
`$this->get_normalized_rest_base()` |  | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 189](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L189)



### `mainwp_rest_{$type}_object_query`

*Filter the query arguments for a request.*

Enables adding extra arguments or setting defaults for a post
collection request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` | `array` | Key value array of query var to query value.
`$request` | `\WP_REST_Request` | The request used.

Source: [includes/rest-api/controller/version2/class-mainwp-rest-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 406](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L406)



### `mainwp_rest_collection_params`

*Filter collection parameters for the controller.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` |  | 
`$this` |  | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 1384](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L1384)



### `mainwp_rest_batch_items_limit`

*Check batch limit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 
`$this->get_normalized_rest_base()` |  | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php), [line 471](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php#L471)



### `mainwp_rest_prepare_site`

*Filterobject returned from the REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The object.
`$item` | `mixed` | The object used to create response.
`$request` | `\WP_REST_Request` | Request object.

Source: [includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2346](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2346)



### `mainwp_admin_enqueue_scripts`

*Method admin_enqueue_scripts()*

Enqueue all Mainwp Admin Scripts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 1053](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L1053)



### `minwp_notification_template_copy_message`

*Use mainwp_notification_template_copy_message instead.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  | 

Source: [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 330](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L330)



### `mainwp_notification_template_copy_message`

*Filter mainwp_notification_template_copy_message.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$copy_message` |  | 
`$templ` |  | 
`$type` |  | 
`$overrided` |  | 

Source: [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 337](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L337)



### `mainwp_notification_type_desc`

*Get email settings description.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | Email notification type.

Source: [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 378](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L378)



### `mainwp_notification_types`

*Get email notification types.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$type` | `string` | Email notification type.

Source: [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 426](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L426)



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

Source: [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 551](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L551)



### `{$filter}`

*Method apply_filter()*

Apply filter

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` | `array` | Input value.

Source: [class/class-mainwp-system-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php), [line 188](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-handler.php#L188)



### `mainwp_log_status`

*MainWP_Logger constructor.*

Run each time the class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$enabled` |  | 

Source: [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 129](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L129)



### `mainwp_log_specific`

*MainWP_Logger constructor.*

Run each time the class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific` |  | 

Source: [class/class-mainwp-logger.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php), [line 129](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-logger.php#L129)



### `mainwp_curl_http_version`

*Fetch uptime urls.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

Source: [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 350](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L350)



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

Source: [class/class-mainwp-qq2-file-uploader.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-qq2-file-uploader.php), [line 56](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-qq2-file-uploader.php#L56)



### `mainwp_format_email`

*Method format_email()*

Format email.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mail_send` |  | 

Source: [class/class-mainwp-format.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-format.php), [line 212](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-format.php#L212)



### `mainwp_remote_destination_info`

*Method mainwp_backup_upload_checkstatus()*

Check upload status

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`isset($_POST['remote_destination']) ? sanitize_text_field(wp_unslash($_POST['remote_destination'])) : ''` |  | 

Source: [class/class-mainwp-post-backup-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-backup-handler.php), [line 376](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-backup-handler.php#L376)



### `mainwp_open_hide_referrer`

*Filter: mainwp_open_hide_referrer*

Filters whether the MainWP should hide referrer when going to child site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-system-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php), [line 823](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php#L823)



### `mainwp_is_enable_schedule_job`

*Method init_mainwp_cron()*

Schedual Cron Jobs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$useWPCron` | `mixed` | Wether or not to use WP_Cron.
`$cron_hook` | `mixed` | When cron is going to reoccur.
`$recurrence` | `mixed` | Cron job hook.

Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 147](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L147)



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

Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 629](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L629)



### `mainwp_license_deactivated_alert_plain_text`

*Method cron_deactivated_licenses_alert()*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plain_text` |  | 

Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 1356](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L1356)



### `mainwp_register_regular_sequence_process`

*Method perform_sequence_process*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 1692](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L1692)



### `mainwp_try_visit_follow_location`

*Method try visit.*

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 32](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L32)



### `mainwp_curl_http_version`

*Method try visit.*

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`false` |  | 
`$url` | `string` | Child Site URL.

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 32](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L32)



### `mainwp_curl_curlopt_resolve`

*Method try visit.*

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`false` |  | 
`$url` | `string` | Child Site URL.

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 32](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L32)



### `mainwp_fetch_urls_chunk_size`

*Method fetch_urls_authed()*

Fetches data from child sites if authenticated.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$chunkSize` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 688](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L688)



### `mainwp_curl_http_version`

*Method fetch_urls_authed()*

Fetches data from child sites if authenticated.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 688](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L688)



### `mainwp_curl_http_version`

*Method fetch_url_site()*

M Fetch URL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website ? $website->id : false` |  | 
`$url` | `string` | URL to fetch from.

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 1351](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L1351)



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

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 140](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L140)



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

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 265](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L265)



### `mainwp_get_notification_template_name_by_type`

*Get default template name by email/notification type.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | email/notification type.

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 293](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L293)



### `mainwp_default_template_source_dir`

*Method handle_template_file_action()*

Handle template file action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template_path` |  | 
`$templ_base_name` |  | 

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 318](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L318)



### `mainwp_module_log_record_array`

*Filter allows modification of record information*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$record` | `array` | 

Source: [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 59](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L59)



### `mainwp_module_log_query_args`

*Filter allows additional arguments to query $args*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [modules/logs/classes/class-log-db.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php), [line 162](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-db.php#L162)



### `mainwp_module_log_current_agent`

*Filter the current agent string*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$agent` |  | 

Source: [modules/logs/classes/class-log-author.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php), [line 241](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php#L241)



### `mainwp_module_log_agent_label`

*Filter agent labels*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$label` |  | 
`$agent` | `string` | Key representing agent.

Source: [modules/logs/classes/class-log-author.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php), [line 269](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php#L269)



### `mainwp_module_log_connectors`

*Allows for adding additional connectors via classes that extend Connector.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$classes` | `array` | An array of Connector objects.
`$this->manager->log` |  | 

Source: [modules/logs/classes/class-log-connectors.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php), [line 97](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-connectors.php#L97)



### `mainwp_rest_api_enabled`

*Method init_rest_api()*

Adds an action to create the rest API endpoints if activated in the plugin settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 56](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L56)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_all_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-all-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 167](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L167)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_client_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-client-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 195](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L195)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_site_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-site-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 245](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L245)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 285](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L285)



### `mainwp_rest_cost_collection_params`

*Filter collection parameters.*

This filter registers the collection parameter, but does not map the
collection parameter to an internal WP_Comment_Query parameter. Use the
`wc_rest_review_query` filter to set WP_Comment_Query parameters.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | JSON Schema-formatted collection parameters.

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 753](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L753)



### `mainwp_rest_prepare_cost`

*Filter product reviews object returned from the REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The  object.
`$review` |  | 
`$request` | `\WP_REST_Request` | Request object.

Source: [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 947](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L947)



### `https_local_ssl_verify`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [pages/page-mainwp-server-information-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php), [line 704](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php#L704)




# Miscellaneous Actions

Miscellaneous hooks that don't fit into other categories.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_child_site_stats`](#mainwp_child_site_stats) - Get Child Site Stats.
- [`mainwp_child_before_send_feedback_message`](#mainwp_child_before_send_feedback_message) - Action: process send feedback message.
- [`mainwp_child_before_send_close_message`](#mainwp_child_before_send_close_message) - Action: process before send close message.
- [`rt_nginx_helper_purge_all`](#rt_nginx_helper_purge_all) - Purge Nginx Helper cache.
- [`wpfc_clear_all_cache`](#wpfc_clear_all_cache) - Purge WP Fastest Cache.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Record BackWPup MainWP Child Reports log.
- [`{$hook_name}`](#hook_name) - Support old WP version 4.0.
- [`mainwp-site-sync-others-data`](#mainwp-site-sync-others-data) - Get other stats data.
- [`mainwp_site_sync_others_data`](#mainwp_site_sync_others_data) - Get other stats data.
- [`woocommerce_reports_order_statuses`](#woocommerce_reports_order_statuses) - *Arguments*
- [`woocommerce_reports_order_statuses`](#woocommerce_reports_order_statuses) - *Arguments*
- [`mainwp_child_woocom_sync_data`](#mainwp_child_woocom_sync_data) - Sync Woocommerce data.
- [`woocommerce_reports_order_statuses`](#woocommerce_reports_order_statuses) - *Arguments*
- [`woocommerce_reports_order_statuses`](#woocommerce_reports_order_statuses) - *Arguments*
- [`mainwp_child_woocom_report_data`](#mainwp_child_woocom_report_data) - Woocommerce report data.
- [`woocommerce_reports_order_statuses`](#woocommerce_reports_order_statuses) - *Arguments*
- [`woocommerce_dashboard_status_widget_sales_query`](#woocommerce_dashboard_status_widget_sales_query) - *Arguments*
- [`woocommerce_reports_order_statuses`](#woocommerce_reports_order_statuses) - *Arguments*
- [`mainwp_child_woocom_get_data`](#mainwp_child_woocom_get_data) - Get Woocommerce reports old.
- [`mainwp_child_unique_id`](#mainwp_child_unique_id) - Method get_site_unique_id()
- [`mainwp_child_contact_support_mail_headers`](#mainwp_child_contact_support_mail_headers) - Send support email.
- [`sanitize_file_name_chars`](#sanitize_file_name_chars) - Filters the list of characters to remove from a filename.
- [`sanitize_file_name`](#sanitize_file_name) - Filters a sanitized filename string.

## Hook Details

### `mainwp_child_site_stats`

*Get Child Site Stats.*


Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 141](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L141)



### `mainwp_child_before_send_feedback_message`

*Action: process send feedback message.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  | 

**Changelog**

Version | Description
------- | -----------
`5.1` | 

Source: [class/class-mainwp-helper.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php), [line 72](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php#L72)



### `mainwp_child_before_send_close_message`

*Action: process before send close message.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  | 

**Changelog**

Version | Description
------- | -----------
`4.4.0.3` | 

Source: [class/class-mainwp-helper.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php), [line 94](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php#L94)



### `rt_nginx_helper_purge_all`

*Purge Nginx Helper cache.*


Source: [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 716](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L716)



### `wpfc_clear_all_cache`

*Purge WP Fastest Cache.*


Source: [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 818](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L818)



### `mainwp_child_reports_log`

*Record BackWPup MainWP Child Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backwpup'` |  | 

Source: [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 307](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L307)



### `{$hook_name}`

*Support old WP version 4.0.*

Fires functions attached to a deprecated filter hook.

When a filter hook is deprecated, the apply_filters() call is replaced with
apply_filters_deprecated(), which triggers a deprecation notice and then fires
the original filter hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` | `array` | Array of additional function arguments to be passed to apply_filters().

Source: [includes/functions.php](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php), [line 169](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php#L169)



### `mainwp-site-sync-others-data`

*Get other stats data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($information, $othersData)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_site_sync_others_data'` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 466](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L466)



### `mainwp_site_sync_others_data`

*Get other stats data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Child Site Stats array.
`$othersData` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 466](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L466)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 145](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L145)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 168](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L168)



### `mainwp_child_woocom_sync_data`

*Sync Woocommerce data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 113](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L113)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 258](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L258)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 277](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L277)



### `mainwp_child_woocom_report_data`

*Woocommerce report data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 220](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L220)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 522](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L522)



### `woocommerce_dashboard_status_widget_sales_query`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$query` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 527](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L527)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 536](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L536)



### `mainwp_child_woocom_get_data`

*Get Woocommerce reports old.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 490](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L490)



### `mainwp_child_unique_id`

*Method get_site_unique_id()*

Get site unique id.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uniqueId` |  | 

Source: [class/class-mainwp-helper.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php), [line 744](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php#L744)



### `mainwp_child_contact_support_mail_headers`

*Send support email.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$headers` |  | 
`$email` |  | 
`$from` |  | 

Source: [class/class-mainwp-utility.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php), [line 740](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php#L740)



### `sanitize_file_name_chars`

*Filters the list of characters to remove from a filename.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$special_chars` | `string[]` | Array of characters to remove.
`$filename_raw` | `string` | The original filename to be sanitized.

**Changelog**

Version | Description
------- | -----------
`2.8.0` | 

Source: [class/class-mainwp-child-misc.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php), [line 557](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php#L557)



### `sanitize_file_name`

*Filters a sanitized filename string.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$filename` | `string` | Sanitized filename.
`$filename_raw` | `string` | The filename prior to sanitization.

**Changelog**

Version | Description
------- | -----------
`2.8.0` | 

Source: [class/class-mainwp-child-misc.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php), [line 572](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php#L572)




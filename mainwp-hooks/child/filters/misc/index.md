# Miscellaneous Filters

Miscellaneous hooks that don't fit into other categories.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Record BackWPup MainWP Child Reports log.
- [`mainwp_child_site_stats`](#mainwp_child_site_stats) - Get Child Site Stats.
- [`mainwp_child_before_send_feedback_message`](#mainwp_child_before_send_feedback_message) - Action: process send feedback message.
- [`mainwp_child_before_send_close_message`](#mainwp_child_before_send_close_message) - Action: process before send close message.
- [`rt_nginx_helper_purge_all`](#rt_nginx_helper_purge_all) - Purge Nginx Helper cache.
- [`wpfc_clear_all_cache`](#wpfc_clear_all_cache) - Purge WP Fastest Cache.
- [`{$hook_name}`](#hook_name) - Support old WP version 4.0.
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
- [`sanitize_file_name_chars`](#sanitize_file_name_chars) - Filters the list of characters to remove from a filename.
- [`sanitize_file_name`](#sanitize_file_name) - Filters a sanitized filename string.
- [`mainwp-site-sync-others-data`](#mainwp-site-sync-others-data) - Get other stats data.
- [`mainwp_site_sync_others_data`](#mainwp_site_sync_others_data) - Get other stats data.
- [`mainwp_child_unique_id`](#mainwp_child_unique_id) - Method get_site_unique_id()
- [`mainwp_child_contact_support_mail_headers`](#mainwp_child_contact_support_mail_headers) - Send support email.

## Hook Details

### `mainwp_child_reports_log`

*Record BackWPup MainWP Child Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backwpup'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 307](class/class-mainwp-child-back-wp-up.php#L307-L314)



### `mainwp_child_site_stats`

*Get Child Site Stats.*


Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 141](class/class-mainwp-child-stats.php#L141-L358)



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

Source: [../sources/mainwp-child/class/class-mainwp-helper.php](class/class-mainwp-helper.php), [line 72](class/class-mainwp-helper.php#L72-L77)



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

Source: [../sources/mainwp-child/class/class-mainwp-helper.php](class/class-mainwp-helper.php), [line 94](class/class-mainwp-helper.php#L94-L99)



### `rt_nginx_helper_purge_all`

*Purge Nginx Helper cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 716](class/class-mainwp-child-cache-purge.php#L716-L729)



### `wpfc_clear_all_cache`

*Purge WP Fastest Cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 818](class/class-mainwp-child-cache-purge.php#L818-L831)



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

Source: [../sources/mainwp-child/includes/functions.php](includes/functions.php), [line 169](includes/functions.php#L169-L189)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 145](class/class-mainwp-child-woocommerce-status.php#L145-L145)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 168](class/class-mainwp-child-woocommerce-status.php#L168-L168)



### `mainwp_child_woocom_sync_data`

*Sync Woocommerce data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 113](class/class-mainwp-child-woocommerce-status.php#L113-L213)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 258](class/class-mainwp-child-woocommerce-status.php#L258-L258)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 277](class/class-mainwp-child-woocommerce-status.php#L277-L277)



### `mainwp_child_woocom_report_data`

*Woocommerce report data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 220](class/class-mainwp-child-woocommerce-status.php#L220-L319)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 522](class/class-mainwp-child-woocommerce-status.php#L522-L522)



### `woocommerce_dashboard_status_widget_sales_query`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$query` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 527](class/class-mainwp-child-woocommerce-status.php#L527-L527)



### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 536](class/class-mainwp-child-woocommerce-status.php#L536-L536)



### `mainwp_child_woocom_get_data`

*Get Woocommerce reports old.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 490](class/class-mainwp-child-woocommerce-status.php#L490-L585)



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

Source: [../sources/mainwp-child/class/class-mainwp-child-misc.php](class/class-mainwp-child-misc.php), [line 557](class/class-mainwp-child-misc.php#L557-L565)



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

Source: [../sources/mainwp-child/class/class-mainwp-child-misc.php](class/class-mainwp-child-misc.php), [line 572](class/class-mainwp-child-misc.php#L572-L580)



### `mainwp-site-sync-others-data`

*Get other stats data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($information, $othersData)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_site_sync_others_data'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 466](class/class-mainwp-child-stats.php#L466-L482)



### `mainwp_site_sync_others_data`

*Get other stats data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Child Site Stats array.
`$othersData` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 466](class/class-mainwp-child-stats.php#L466-L483)



### `mainwp_child_unique_id`

*Method get_site_unique_id()*

Get site unique id.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uniqueId` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-helper.php](class/class-mainwp-helper.php), [line 744](class/class-mainwp-helper.php#L744-L757)



### `mainwp_child_contact_support_mail_headers`

*Send support email.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$headers` |  | 
`$email` |  | 
`$from` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-utility.php](class/class-mainwp-utility.php), [line 740](class/class-mainwp-utility.php#L740-L774)




# Miscellaneous Filters

Miscellaneous hooks that don't fit into other categories.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`deprecated_hook_run`](#deprecated-hook-run) - Support old WP version 4.0.
- [`mainwp-site-sync-others-data`](#mainwp-site-sync-others-data) - Get other stats data.
- [`mainwp_child_before_send_close_message`](#mainwp-child-before-send-close-message) - Action: process before send close message.
- [`mainwp_child_before_send_feedback_message`](#mainwp-child-before-send-feedback-message) - Action: process send feedback message.
- [`mainwp_child_contact_support_mail_headers`](#mainwp-child-contact-support-mail-headers) - Send support email.
- [`mainwp_child_extra_execution`](#mainwp-child-extra-execution) - Filter 'mainwp_child_extra_execution'
- [`mainwp_child_reports_log`](#mainwp-child-reports-log) - Record BackWPup MainWP Child Reports log.
- [`mainwp_child_site_stats`](#mainwp-child-site-stats) - Get Child Site Stats.
- [`mainwp_child_unique_id`](#mainwp-child-unique-id) - Method get_site_unique_id()
- [`mainwp_child_woocom_get_data`](#mainwp-child-woocom-get-data) - Get Woocommerce reports old.
- [`mainwp_child_woocom_report_data`](#mainwp-child-woocom-report-data) - Woocommerce report data.
- [`mainwp_child_woocom_sync_data`](#mainwp-child-woocom-sync-data) - Sync Woocommerce data.
- [`mainwp_site_sync_others_data`](#mainwp-site-sync-others-data) - Get other stats data.
- [`rt_nginx_helper_purge_all`](#rt-nginx-helper-purge-all) - Purge Nginx Helper cache.
- [`sanitize_file_name`](#sanitize-file-name) - Filters a sanitized filename string.
- [`sanitize_file_name_chars`](#sanitize-file-name-chars) - Filters the list of characters to remove from a filename.
- [`updraftplus_http_to_https_additional_warning`](#updraftplus-http-to-https-additional-warning) - *Arguments*
- [`updraftplus_https_to_http_additional_warning`](#updraftplus-https-to-http-additional-warning) - *Arguments*
- [`updraftplus_migrator_addon_link`](#updraftplus-migrator-addon-link) - *Arguments*
- [`updraftplus_print_active_job_continue`](#updraftplus-print-active-job-continue) - *Arguments*
- [`woocommerce_dashboard_status_widget_sales_query`](#woocommerce-dashboard-status-widget-sales-query) - *Arguments*
- [`woocommerce_reports_order_statuses`](#woocommerce-reports-order-statuses) - *Arguments*
- [`wp_login`](#wp-login) - Method login()
- [`wp_logout`](#wp-logout) - Method login()
- [`wpfc_clear_all_cache`](#wpfc-clear-all-cache) - Purge WP Fastest Cache.
- [`wpvivid_get_mainwp_sync_data`](#wpvivid-get-mainwp-sync-data) - Sync other data from $data[] and merge with $information[]
- [`{$hook_name}`](#hook-name) - Support old WP version 4.0.

---

## Hook Details

<a id='deprecated-hook-run'></a>
### `deprecated_hook_run`

* Support old WP version 4.0.

Fires functions attached to a deprecated filter hook.

When a filter hook is deprecated, the apply_filters() call is replaced with
apply_filters_deprecated(), which triggers a deprecation notice and then fires
the original filter hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$hook_name` | `string` | The name of the filter hook.
`$replacement` | `string` | Optional. The hook that should have been used. Default empty.
`$version` | `string` | The version of WordPress that deprecated the hook.
`$message` | `string` | Optional. A message regarding the change. Default empty.

**Usage Locations:**

- [includes/functions.php](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php), [line 169](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php#L169)

---

<a id='mainwp-site-sync-others-data'></a>
### `mainwp-site-sync-others-data`

* Get other stats data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($information, $othersData)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_site_sync_others_data'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($information, $othersData)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_site_sync_others_data'` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 466](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L466)

---

<a id='mainwp-child-before-send-close-message'></a>
### `mainwp_child_before_send_close_message`

* Action: process before send close message.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  |

**Changelog**

Version | Description
------- | -----------
`4.4.0.3` |

**Usage Locations:**

- [class/class-mainwp-helper.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php), [line 94](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php#L94)

---

<a id='mainwp-child-before-send-feedback-message'></a>
### `mainwp_child_before_send_feedback_message`

* Action: process send feedback message.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  |

**Changelog**

Version | Description
------- | -----------
`5.1` |

**Usage Locations:**

- [class/class-mainwp-helper.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php), [line 72](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php#L72)

---

<a id='mainwp-child-contact-support-mail-headers'></a>
### `mainwp_child_contact_support_mail_headers`

* Send support email.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$headers` |  | 
`$email` |  | 
`$from` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$headers` |  | 
`$email` |  | 
`$from` |  |

**Usage Locations:**

- [class/class-mainwp-utility.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php), [line 740](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php#L740)

---

<a id='mainwp-child-extra-execution'></a>
### `mainwp_child_extra_execution`

* Filter 'mainwp_child_extra_execution'

Additional functions to execute through the filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | An array containing the synchronization information.
`$post` | `mixed` | Contains the POST request.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-child-callable.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-callable.php), [line 745](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-callable.php#L745)

---

<a id='mainwp-child-reports-log'></a>
### `mainwp_child_reports_log`

* Record BackWPup MainWP Child Reports log.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backwpup'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backwpup'` |  |

**Usage Locations:**

- [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 307](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L307)

---

<a id='mainwp-child-site-stats'></a>
### `mainwp_child_site_stats`

* Get Child Site Stats.

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 141](class/class-mainwp-child-stats.php#L141-L358)

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 141](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L141)

---

<a id='mainwp-child-unique-id'></a>
### `mainwp_child_unique_id`

* Method get_site_unique_id()

Get site unique id.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uniqueId` |  |

**Usage Locations:**

- [class/class-mainwp-helper.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php), [line 744](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-helper.php#L744)

---

<a id='mainwp-child-woocom-get-data'></a>
### `mainwp_child_woocom_get_data`

* Get Woocommerce reports old.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Usage Locations:**

- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 490](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L490)

---

<a id='mainwp-child-woocom-report-data'></a>
### `mainwp_child_woocom_report_data`

* Woocommerce report data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Usage Locations:**

- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 220](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L220)

---

<a id='mainwp-child-woocom-sync-data'></a>
### `mainwp_child_woocom_sync_data`

* Sync Woocommerce data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  |

**Usage Locations:**

- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 113](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L113)

---

<a id='mainwp-site-sync-others-data'></a>
### `mainwp_site_sync_others_data`

* Get other stats data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Child Site Stats array.
`$othersData` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Child Site Stats array.
`$othersData` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 466](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L466)

---

<a id='rt-nginx-helper-purge-all'></a>
### `rt_nginx_helper_purge_all`

* Purge Nginx Helper cache.

Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 716](class/class-mainwp-child-cache-purge.php#L716-L729)

**Usage Locations:**

- [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 716](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L716)

---

<a id='sanitize-file-name'></a>
### `sanitize_file_name`

* Filters a sanitized filename string.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$filename` | `string` | Sanitized filename.
`$filename_raw` | `string` | The filename prior to sanitization.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$filename` | `string` | Sanitized filename.
`$filename_raw` | `string` | The filename prior to sanitization.

**Changelog**

Version | Description
------- | -----------
`2.8.0` |

**Usage Locations:**

- [class/class-mainwp-child-misc.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php), [line 572](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php#L572)

---

<a id='sanitize-file-name-chars'></a>
### `sanitize_file_name_chars`

* Filters the list of characters to remove from a filename.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$special_chars` | `string[]` | Array of characters to remove.
`$filename_raw` | `string` | The original filename to be sanitized.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$special_chars` | `string[]` | Array of characters to remove.
`$filename_raw` | `string` | The original filename to be sanitized.

**Changelog**

Version | Description
------- | -----------
`2.8.0` |

**Usage Locations:**

- [class/class-mainwp-child-misc.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php), [line 557](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-misc.php#L557)

---

<a id='updraftplus-http-to-https-additional-warning'></a>
### `updraftplus_http_to_https_additional_warning`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('As long as your web hosting allows http (i.e. non-SSL access) or will forward requests to https (which is almost always the case), this is no problem. If that is not yet set up, then you should set it up, or use %s so that the non-https links are automatically replaced.', 'updraftplus'), apply_filters('<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'))` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('As long as your web hosting allows http (i.e. non-SSL access) or will forward requests to https (which is almost always the case), this is no problem. If that is not yet set up, then you should set it up, or use %s so that the non-https links are automatically replaced.', 'updraftplus'), apply_filters('<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'))` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2636](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2636)

---

<a id='updraftplus-https-to-http-additional-warning'></a>
### `updraftplus_https_to_http_additional_warning`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('This restoration will work if you still have an SSL certificate (i.e. can use https) to access the site. Otherwise, you will want to use %s to search/replace the site address so that the site can be visited without https.', 'updraftplus'), '<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('This restoration will work if you still have an SSL certificate (i.e. can use https) to access the site. Otherwise, you will want to use %s to search/replace the site address so that the site can be visited without https.', 'updraftplus'), '<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>')` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2634](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2634)

---

<a id='updraftplus-migrator-addon-link'></a>
### `updraftplus_migrator_addon_link`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2636](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2636)

---

<a id='updraftplus-print-active-job-continue'></a>
### `updraftplus_print_active_job_continue`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$is_oneshot` |  | 
`$next_resumption` |  | 
`$jobdata` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$is_oneshot` |  | 
`$next_resumption` |  | 
`$jobdata` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3736](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3736)

---

<a id='woocommerce-dashboard-status-widget-sales-query'></a>
### `woocommerce_dashboard_status_widget_sales_query`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$query` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$query` |  |

**Usage Locations:**

- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 527](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L527)

---

<a id='woocommerce-reports-order-statuses'></a>
### `woocommerce_reports_order_statuses`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  |

**Usage Locations:**

- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 145](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L145)
- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 168](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L168)
- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 258](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L258)
- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 277](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L277)
- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 522](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L522)
- [class/class-mainwp-child-woocommerce-status.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php), [line 536](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-woocommerce-status.php#L536)

---

<a id='wp-login'></a>
### `wp_login`

* Method login()

The login process handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user->user_login` |  |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 1021](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L1021)

---

<a id='wp-logout'></a>
### `wp_logout`

* Method login()

The login process handler.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 1021](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L1021)

---

<a id='wpfc-clear-all-cache'></a>
### `wpfc_clear_all_cache`

* Purge WP Fastest Cache.

Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 818](class/class-mainwp-child-cache-purge.php#L818-L831)

**Usage Locations:**

- [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 818](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L818)

---

<a id='wpvivid-get-mainwp-sync-data'></a>
### `wpvivid_get_mainwp_sync_data`

* Sync other data from $data[] and merge with $information[]

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Stores the returned information.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Stores the returned information.

**Usage Locations:**

- [class/class-mainwp-child-wpvivid-backuprestore.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php), [line 91](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php#L91)

---

<a id='hook-name'></a>
### `{$hook_name}`

* Support old WP version 4.0.

Fires functions attached to a deprecated filter hook.

When a filter hook is deprecated, the apply_filters() call is replaced with
apply_filters_deprecated(), which triggers a deprecation notice and then fires
the original filter hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` | `array` | Array of additional function arguments to be passed to apply_filters().

**Usage Locations:**

- [includes/functions.php](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php), [line 169](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php#L169)

---


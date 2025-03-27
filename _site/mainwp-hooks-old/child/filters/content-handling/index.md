# Content Handling Filters

Hooks for managing content on Child sites.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`wphb_clear_page_cache`](#wphb_clear_page_cache) - Purge WP Hummingbird cache.
- [`run_gpi`](#run_gpi) - Method do_check_pages()
- [`mainwp_child_after_newpost`](#mainwp_child_after_newpost) - Build New Post.
- [`comment_email`](#comment_email) - Get recent comments.
- [`mainwp_child_extra_execution`](#mainwp_child_extra_execution) - Filter 'mainwp_child_extra_execution'
- [`wpvivid_handle_mainwp_action`](#wpvivid_handle_mainwp_action) - Post MainWP data.
- [`mainwp-child-init-subpages`](#mainwp-child-init-subpages) - Initiate MainWP Child Plugin pages.
- [`mainwp_child_init_subpages`](#mainwp_child_init_subpages) - Initiate MainWP Child Plugin pages.
- [`error_log_mainwp_logs`](#error_log_mainwp_logs) - Render the error log content.
- [`error_log_mainwp_lines`](#error_log_mainwp_lines) - Render the error log content.

## Hook Details

### `wphb_clear_page_cache`

*Purge WP Hummingbird cache.*


Source: [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 741](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L741)



### `run_gpi`

*Method do_check_pages()*

Check or force re-check pages page speed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$forceRecheck` | `bool` | If true, force recheck process, if false, just regular check.

Source: [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 429](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L429)



### `mainwp_child_after_newpost`

*Build New Post.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  | 

Source: [class/class-mainwp-child-posts.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php), [line 373](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php#L373)



### `comment_email`

*Get recent comments.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$comment->comment_author_email` |  | 

Source: [class/class-mainwp-child-comments.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-comments.php), [line 200](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-comments.php#L200)



### `mainwp_child_extra_execution`

*Filter 'mainwp_child_extra_execution'*

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

Source: [class/class-mainwp-child-callable.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-callable.php), [line 745](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-callable.php#L745)



### `wpvivid_handle_mainwp_action`

*Post MainWP data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$data` | `string` | Data to post.

Source: [class/class-mainwp-child-wpvivid-backuprestore.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php), [line 225](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php#L225)



### `mainwp-child-init-subpages`

*Initiate MainWP Child Plugin pages.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_init_subpages'` |  | 

Source: [class/class-mainwp-pages.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php), [line 230](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php#L230)



### `mainwp_child_init_subpages`

*Initiate MainWP Child Plugin pages.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$all_subpages` |  | 

Source: [class/class-mainwp-pages.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php), [line 230](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php#L230)



### `error_log_mainwp_logs`

*Render the error log content.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($error_log)` |  | 

Source: [class/class-mainwp-child-server-information.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php), [line 1089](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php#L1089)



### `error_log_mainwp_lines`

*Render the error log content.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [class/class-mainwp-child-server-information.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php), [line 1089](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php#L1089)




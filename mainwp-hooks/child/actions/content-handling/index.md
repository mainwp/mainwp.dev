# Content Handling Actions

Hooks for managing content on Child sites.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`comment_email`](#comment-email) - Get recent comments.
- [`error_log_mainwp_lines`](#error-log-mainwp-lines) - Render the error log content.
- [`error_log_mainwp_logs`](#error-log-mainwp-logs) - Render the error log content.
- [`mainwp-child-init-subpages`](#mainwp-child-init-subpages) - Initiate MainWP Child Plugin pages.
- [`mainwp_child_after_newpost`](#mainwp-child-after-newpost) - Build New Post.
- [`mainwp_child_init_subpages`](#mainwp-child-init-subpages) - Initiate MainWP Child Plugin pages.
- [`run_gpi`](#run-gpi) - Method do_check_pages()
- [`wphb_clear_page_cache`](#wphb-clear-page-cache) - Purge WP Hummingbird cache.
- [`wpvivid_handle_mainwp_action`](#wpvivid-handle-mainwp-action) - Post MainWP data.

---

## Hook Details

<a id='comment-email'></a>
### `comment_email`

* Get recent comments.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$comment->comment_author_email` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$comment->comment_author_email` |  |

**Usage Locations:**

- [class/class-mainwp-child-comments.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-comments.php), [line 200](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-comments.php#L200)

---

<a id='error-log-mainwp-lines'></a>
### `error_log_mainwp_lines`

* Render the error log content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Usage Locations:**

- [class/class-mainwp-child-server-information.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php), [line 1089](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php#L1089)

---

<a id='error-log-mainwp-logs'></a>
### `error_log_mainwp_logs`

* Render the error log content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($error_log)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($error_log)` |  |

**Usage Locations:**

- [class/class-mainwp-child-server-information.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php), [line 1089](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information.php#L1089)

---

<a id='mainwp-child-init-subpages'></a>
### `mainwp-child-init-subpages`

* Initiate MainWP Child Plugin pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_init_subpages'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_init_subpages'` |  |

**Usage Locations:**

- [class/class-mainwp-pages.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php), [line 230](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php#L230)

---

<a id='mainwp-child-after-newpost'></a>
### `mainwp_child_after_newpost`

* Build New Post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  |

**Usage Locations:**

- [class/class-mainwp-child-posts.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php), [line 373](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php#L373)

---

<a id='mainwp-child-init-subpages'></a>
### `mainwp_child_init_subpages`

* Initiate MainWP Child Plugin pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$all_subpages` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$all_subpages` |  |

**Usage Locations:**

- [class/class-mainwp-pages.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php), [line 230](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php#L230)

---

<a id='run-gpi'></a>
### `run_gpi`

* Method do_check_pages()

Check or force re-check pages page speed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$forceRecheck` | `bool` | If true, force recheck process, if false, just regular check.

**Usage Locations:**

- [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 429](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L429)

---

<a id='wphb-clear-page-cache'></a>
### `wphb_clear_page_cache`

* Purge WP Hummingbird cache.

Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 741](class/class-mainwp-child-cache-purge.php#L741-L756)

**Usage Locations:**

- [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 741](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L741)

---

<a id='wpvivid-handle-mainwp-action'></a>
### `wpvivid_handle_mainwp_action`

* Post MainWP data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$data` | `string` | Data to post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$data` | `string` | Data to post.

**Usage Locations:**

- [class/class-mainwp-child-wpvivid-backuprestore.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php), [line 225](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php#L225)

---


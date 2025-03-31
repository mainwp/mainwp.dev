# Connection & Authentication Actions

Hooks for establishing and managing connections between Dashboard and Child sites.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`https_local_ssl_verify`](#https-local-ssl-verify) - *Arguments*
- [`mainwp_child_authed_download_params`](#mainwp-child-authed-download-params) - Method where_authed_redirect()
- [`mainwp_create_post_custom_author`](#mainwp-create-post-custom-author) - Update post data.

---

## Hook Details

<a id='https-local-ssl-verify'></a>
### `https_local_ssl_verify`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Usage Locations:**

- [class/class-mainwp-child-server-information-base.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information-base.php), [line 702](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information-base.php#L702)

---

<a id='mainwp-child-authed-download-params'></a>
### `mainwp_child_authed_download_params`

* Method where_authed_redirect()

Safe redirect to wanted location.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$auth_dl` |  |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 821](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L821)

---

<a id='mainwp-create-post-custom-author'></a>
### `mainwp_create_post_custom_author`

* Update post data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$new_post_id` | `string` | New post ID.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$new_post_id` | `string` | New post ID.

**Usage Locations:**

- [class/class-mainwp-child-posts.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php), [line 968](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php#L968)

---


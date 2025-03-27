# Connection & Authentication Actions

Hooks for establishing and managing connections between Dashboard and Child sites.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`wp_logout`](#wp_logout) - Method parse_login_required()
- [`wp_logout`](#wp_logout) - Method parse_login_required()
- [`wp_logout`](#wp_logout) - Method login()
- [`wp_login`](#wp_login) - Method login()
- [`mainwp_child_authed_download_params`](#mainwp_child_authed_download_params) - Method where_authed_redirect()
- [`https_local_ssl_verify`](#https_local_ssl_verify) - *Arguments*
- [`mainwp_create_post_custom_author`](#mainwp_create_post_custom_author) - Update post data.

## Hook Details

### `wp_logout`

*Method parse_login_required()*

Check if the login process is required.


Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 652](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L652)



### `wp_logout`

*Method parse_login_required()*

Check if the login process is required.


Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 652](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L652)



### `wp_logout`

*Method login()*

The login process handler.


Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 1021](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L1021)



### `wp_login`

*Method login()*

The login process handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user->user_login` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 1021](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L1021)



### `mainwp_child_authed_download_params`

*Method where_authed_redirect()*

Safe redirect to wanted location.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$auth_dl` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 821](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L821)



### `https_local_ssl_verify`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [class/class-mainwp-child-server-information-base.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information-base.php), [line 702](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-server-information-base.php#L702)



### `mainwp_create_post_custom_author`

*Update post data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$new_post_id` | `string` | New post ID.

Source: [class/class-mainwp-child-posts.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php), [line 968](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php#L968)




# Connection & Authentication Filters

Hooks for establishing and managing connections between Dashboard and Child sites.

## Navigation

- [Back to All Filters](../index.md)
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


Source: [../sources/mainwp-child/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 652](class/class-mainwp-connect.php#L652-L680)



### `wp_logout`

*Method parse_login_required()*

Check if the login process is required.


Source: [../sources/mainwp-child/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 652](class/class-mainwp-connect.php#L652-L710)



### `wp_logout`

*Method login()*

The login process handler.


Source: [../sources/mainwp-child/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1021](class/class-mainwp-connect.php#L1021-L1058)



### `wp_login`

*Method login()*

The login process handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user->user_login` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1021](class/class-mainwp-connect.php#L1021-L1066)



### `mainwp_child_authed_download_params`

*Method where_authed_redirect()*

Safe redirect to wanted location.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$auth_dl` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 821](class/class-mainwp-connect.php#L821-L847)



### `https_local_ssl_verify`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-server-information-base.php](class/class-mainwp-child-server-information-base.php), [line 702](class/class-mainwp-child-server-information-base.php#L702-L702)



### `mainwp_create_post_custom_author`

*Update post data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$new_post_id` | `string` | New post ID.

Source: [../sources/mainwp-child/class/class-mainwp-child-posts.php](class/class-mainwp-child-posts.php), [line 968](class/class-mainwp-child-posts.php#L968-L1012)




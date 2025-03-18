# User Operations Filters

Hooks related to user management on Child sites.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`nonce_user_logged_out`](#nonce_user_logged_out) - Filter whether the user who generated the nonce is logged out.
- [`nonce_user_logged_out`](#nonce_user_logged_out) - Create security nounce without session.
- [`nonce_user_logged_out`](#nonce_user_logged_out) - Verify nonce without session.
- [`mainwp_child_actions_save_data`](#mainwp_child_actions_save_data) - Log handler.
- [`mainwp_branding_role_cap_enable_contact_form`](#mainwp_branding_role_cap_enable_contact_form) - Filter 'mainwp_branding_role_cap_enable_contact_form'
- [`mainwp_branding_role_cap_enable_contact_form`](#mainwp_branding_role_cap_enable_contact_form) - Filter 'mainwp_branding_role_cap_enable_contact_form'
- [`illegal_user_logins`](#illegal_user_logins) - Edit existing user.
- [`nonce_user_logged_out`](#nonce_user_logged_out) - Method create_nonce_without_session()
- [`nonce_user_logged_out`](#nonce_user_logged_out) - Method verify_nonce_without_session()

## Hook Details

### `nonce_user_logged_out`

*Filter whether the user who generated the nonce is logged out.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` | `int` | ID of the nonce-owning user.
`$action` | `string` | The nonce action.

**Changelog**

Version | Description
------- | -----------
`3.5.0` | 

Source: [../sources/mainwp-child/includes/functions.php](includes/functions.php), [line 34](includes/functions.php#L34-L42)



### `nonce_user_logged_out`

*Create security nounce without session.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` |  | 
`$action` | `int` | Action performing.

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 1074](class/class-mainwp-child-back-wp-up.php#L1074-L1085)



### `nonce_user_logged_out`

*Verify nonce without session.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` |  | 
`$action` | `int` | Action to perform.

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 1093](class/class-mainwp-child-back-wp-up.php#L1093-L1106)



### `mainwp_child_actions_save_data`

*Log handler.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$context` | `string` | Context of the event.
`$action` | `string` | Action of the event.
`$args` | `array` | sprintf (and extra) arguments to use.
`$message` | `string` | sprintf-ready error message string.
`$user_id` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-actions.php](class/class-mainwp-child-actions.php), [line 721](class/class-mainwp-child-actions.php#L721-L761)



### `mainwp_branding_role_cap_enable_contact_form`

*Filter 'mainwp_branding_role_cap_enable_contact_form'*

Manage the support form visibility. Set false to hide the support form page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-branding.php](class/class-mainwp-child-branding.php), [line 560](class/class-mainwp-child-branding.php#L560-L567)



### `mainwp_branding_role_cap_enable_contact_form`

*Filter 'mainwp_branding_role_cap_enable_contact_form'*

Manage the support form visibility. Set false to hide the support form page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-branding.php](class/class-mainwp-child-branding.php), [line 1163](class/class-mainwp-child-branding.php#L1163-L1170)



### `illegal_user_logins`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-users.php](class/class-mainwp-child-users.php), [line 303](class/class-mainwp-child-users.php#L303-L418)



### `nonce_user_logged_out`

*Method create_nonce_without_session()*

Create nonce without session.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` |  | 
`$action` | `mixed` | Action to perform.

Source: [../sources/mainwp-child/class/class-mainwp-utility.php](class/class-mainwp-utility.php), [line 812](class/class-mainwp-utility.php#L812-L825)



### `nonce_user_logged_out`

*Method verify_nonce_without_session()*

Verify nonce without session.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` |  | 
`$action` | `mixed` | Action to perform.

Source: [../sources/mainwp-child/class/class-mainwp-utility.php](class/class-mainwp-utility.php), [line 834](class/class-mainwp-utility.php#L834-L849)




# User Operations Actions

Hooks related to user management on Child sites.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`illegal_user_logins`](#illegal-user-logins) - Edit existing user.
- [`mainwp_branding_role_cap_enable_contact_form`](#mainwp-branding-role-cap-enable-contact-form) - Filter 'mainwp_branding_role_cap_enable_contact_form'
- [`mainwp_child_actions_save_data`](#mainwp-child-actions-save-data) - Log handler.
- [`nonce_user_logged_out`](#nonce-user-logged-out) - Filter whether the user who generated the nonce is logged out.

---

## Hook Details

<a id='illegal-user-logins'></a>
### `illegal_user_logins`

* Edit existing user.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-users.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php#L303)

---

<a id='mainwp-branding-role-cap-enable-contact-form'></a>
### `mainwp_branding_role_cap_enable_contact_form`

* Filter 'mainwp_branding_role_cap_enable_contact_form'

Manage the support form visibility. Set false to hide the support form page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-child-branding.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding.php), [line 1163](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding.php#L1163)
- [class/class-mainwp-child-branding.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding.php), [line 560](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding.php#L560)

---

<a id='mainwp-child-actions-save-data'></a>
### `mainwp_child_actions_save_data`

* Log handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$context` | `string` | Context of the event.
`$action` | `string` | Action of the event.
`$args` | `array` | sprintf (and extra) arguments to use.
`$message` | `string` | sprintf-ready error message string.
`$user_id` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$context` | `string` | Context of the event.
`$action` | `string` | Action of the event.
`$args` | `array` | sprintf (and extra) arguments to use.
`$message` | `string` | sprintf-ready error message string.
`$user_id` |  |

**Usage Locations:**

- [class/class-mainwp-child-actions.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-actions.php), [line 721](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-actions.php#L721)

---

<a id='nonce-user-logged-out'></a>
### `nonce_user_logged_out`

* Filter whether the user who generated the nonce is logged out.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` | `int` | ID of the nonce-owning user.
`$action` | `string` | The nonce action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uid` | `int` | ID of the nonce-owning user.
`$action` | `string` | The nonce action.

**Changelog**

Version | Description
------- | -----------
`3.5.0` |

**Usage Locations:**

- [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 1074](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L1074)
- [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 1093](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L1093)
- [class/class-mainwp-utility.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php), [line 812](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php#L812)
- [class/class-mainwp-utility.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php), [line 834](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-utility.php#L834)
- [includes/functions.php](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php), [line 34](https://github.com/mainwp/mainwp-child/blob/master/includes/functions.php#L34)

---


# System & Settings Filters

Hooks related to general settings and system configuration.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-activated`](#mainwp-activated) - MainWP_System constructor.
- [`mainwp_advanced_settings_form_bottom`](#mainwp-advanced-settings-form-bottom) - Action: mainwp_advanced_settings_form_bottom
- [`mainwp_advanced_settings_form_top`](#mainwp-advanced-settings-form-top) - Action: mainwp_advanced_settings_form_top
- [`mainwp_after_save_advanced_settings`](#mainwp-after-save-advanced-settings) - Action: mainwp_after_save_advanced_settings
- [`mainwp_after_save_email_settings`](#mainwp-after-save-email-settings) - Action: mainwp_after_save_email_settings
- [`mainwp_after_save_general_settings`](#mainwp-after-save-general-settings) - Action: mainwp_after_save_general_settings
- [`mainwp_after_wp_config_section`](#mainwp-after-wp-config-section) - Action: mainwp_after_wp_config_section
- [`mainwp_before_save_advanced_settings`](#mainwp-before-save-advanced-settings) - Action: mainwp_before_save_advanced_settings
- [`mainwp_before_save_email_settings`](#mainwp-before-save-email-settings) - Action: mainwp_before_save_email_settings
- [`mainwp_before_save_general_settings`](#mainwp-before-save-general-settings) - Action: mainwp_before_save_general_settings
- [`mainwp_before_wp_config_section`](#mainwp-before-wp-config-section) - Action: mainwp_before_wp_config_section
- [`mainwp_clear_and_lock_options`](#mainwp-clear-and-lock-options) - Clean and Lock extension options
- [`mainwp_default_emails_fields`](#mainwp-default-emails-fields) - Get default email notifications values.
- [`mainwp_default_settings_indicator`](#mainwp-default-settings-indicator) - Method render_not_default_indicator().
- [`mainwp_init_load_all_options`](#mainwp-init-load-all-options) - Method load_all_options()
- [`mainwp_log_system_query`](#mainwp-log-system-query) - Method log_system_query
- [`mainwp_module_cost_tracker_before_save_settings`](#mainwp-module-cost-tracker-before-save-settings) - Settigns Post
- [`mainwp_module_cost_tracker_settings_bottom`](#mainwp-module-cost-tracker-settings-bottom) - Render settings content.
- [`mainwp_notification_type_desc`](#mainwp-notification-type-desc) - Get email settings description.
- [`mainwp_settings_email_settings`](#mainwp-settings-email-settings) - Action: mainwp_settings_email_settings
- [`mainwp_settings_form_bottom`](#mainwp-settings-form-bottom) - Action: mainwp_settings_form_bottom
- [`mainwp_settings_form_top`](#mainwp-settings-form-top) - Action: mainwp_settings_form_top
- [`mainwp_settings_help_item`](#mainwp-settings-help-item) - Action: mainwp_settings_help_item
- [`mainwp_system_init`](#mainwp-system-init) - MainWP_System constructor.

---

## Hook Details

<a id='mainwp-activated'></a>
### `mainwp-activated`

* MainWP_System constructor.

Runs any time class is called.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`'4.0.7.2'` |  | 
`'mainwp_activated'` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 82](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L82)

---

<a id='mainwp-advanced-settings-form-bottom'></a>
### `mainwp_advanced_settings_form_bottom`

* Action: mainwp_advanced_settings_form_bottom

Fires at the bottom of advanced settings form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1680](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1680)

---

<a id='mainwp-advanced-settings-form-top'></a>
### `mainwp_advanced_settings_form_top`

* Action: mainwp_advanced_settings_form_top

Fires at the top of advanced settings form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1401](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1401)

---

<a id='mainwp-after-save-advanced-settings'></a>
### `mainwp_after_save_advanced_settings`

* Action: mainwp_after_save_advanced_settings

Fires after advanced settings save.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1373](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1373)

---

<a id='mainwp-after-save-email-settings'></a>
### `mainwp_after_save_email_settings`

* Action: mainwp_after_save_email_settings

Fires after save email settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$emails_settings` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 87](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L87)
- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1911](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1911)

---

<a id='mainwp-after-save-general-settings'></a>
### `mainwp_after_save_general_settings`

* Action: mainwp_after_save_general_settings

Fires after save general settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 585](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L585)

---

<a id='mainwp-after-wp-config-section'></a>
### `mainwp_after_wp_config_section`

* Action: mainwp_after_wp_config_section

Fires after the WP Config section.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1639](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1639)

---

<a id='mainwp-before-save-advanced-settings'></a>
### `mainwp_before_save_advanced_settings`

* Action: mainwp_before_save_advanced_settings

Fires before save advanced settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1319](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1319)

---

<a id='mainwp-before-save-email-settings'></a>
### `mainwp_before_save_email_settings`

* Action: mainwp_before_save_email_settings

Fires before save email settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`$update_settings` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 76](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L76)
- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 1898](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L1898)

---

<a id='mainwp-before-save-general-settings'></a>
### `mainwp_before_save_general_settings`

* Action: mainwp_before_save_general_settings

Fires before general settings save.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_POST` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 454](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L454)

---

<a id='mainwp-before-wp-config-section'></a>
### `mainwp_before_wp_config_section`

* Action: mainwp_before_wp_config_section

Fires before the WP Config section.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1601](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1601)

---

<a id='mainwp-clear-and-lock-options'></a>
### `mainwp_clear_and_lock_options`

* Clean and Lock extension options

Adds additional options related to Clean and Lock options in order to avoid conflicts when HTTP Basic auth is set.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 379](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L379)

---

<a id='mainwp-default-emails-fields'></a>
### `mainwp_default_emails_fields`

* Get default email notifications values.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$recipients` |  | 
`$type` | `string` | Email type.
`$field` | `string` | Field name.
`$general` | `bool` | General or individual site settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$recipients` |  | 
`$type` | `string` | Email type.
`$field` | `string` | Field name.
`$general` | `bool` | General or individual site settings.

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 551](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L551)
- [pages/page-mainwp-settings-indicator.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings-indicator.php), [line 216](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings-indicator.php#L216)

---

<a id='mainwp-default-settings-indicator'></a>
### `mainwp_default_settings_indicator`

* Method render_not_default_indicator().

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$indi` |  | 
`$field` | `string` | setting field to check.
`$indi_value` |  | 
`$current_value` | `mixed` | setting current value.
`$render_indi` | `bool` | to render indication.
`$default_val` | `mixed` | default value directly.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$indi` |  | 
`$field` | `string` | setting field to check.
`$indi_value` |  | 
`$current_value` | `mixed` | setting current value.
`$render_indi` | `bool` | to render indication.
`$default_val` | `mixed` | default value directly.

**Usage Locations:**

- [pages/page-mainwp-settings-indicator.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings-indicator.php), [line 72](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings-indicator.php#L72)
- [pages/page-mainwp-settings-indicator.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings-indicator.php), [line 99](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings-indicator.php#L99)

---

<a id='mainwp-init-load-all-options'></a>
### `mainwp_init_load_all_options`

* Method load_all_options()

Load all wp_options data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$options` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 297](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L297)

---

<a id='mainwp-log-system-query'></a>
### `mainwp_log_system_query`

* Method log_system_query

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | params.
`$sql` | `string` | query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | params.
`$sql` | `string` | query.

**Usage Locations:**

- [class/class-mainwp-db.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php), [line 3242](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php#L3242)

---

<a id='mainwp-module-cost-tracker-before-save-settings'></a>
### `mainwp_module_cost_tracker_before_save_settings`

* Settigns Post

Handles the save settings post request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$all_opts` |  |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 552](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php#L552)

---

<a id='mainwp-module-cost-tracker-settings-bottom'></a>
### `mainwp_module_cost_tracker_settings_bottom`

* Render settings content.

Renders the extension settings page.

**Usage Locations:**

- [modules/cost-tracker/pages/page-cost-tracker-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-settings.php), [line 88](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-settings.php#L88)

---

<a id='mainwp-notification-type-desc'></a>
### `mainwp_notification_type_desc`

* Get email settings description.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | Email notification type.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$type` | `string` | Email notification type.

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 378](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L378)

---

<a id='mainwp-settings-email-settings'></a>
### `mainwp_settings_email_settings`

* Action: mainwp_settings_email_settings

Fires after the default email settings.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 175](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L175)

---

<a id='mainwp-settings-form-bottom'></a>
### `mainwp_settings_form_bottom`

* Action: mainwp_settings_form_bottom

Fires at the bottom of settings form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 906](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L906)

---

<a id='mainwp-settings-form-top'></a>
### `mainwp_settings_form_top`

* Action: mainwp_settings_form_top

Fires at the top of settings form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 631](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L631)

---

<a id='mainwp-settings-help-item'></a>
### `mainwp_settings_help_item`

* Action: mainwp_settings_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Settings page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`5.2` |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 2393](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L2393)

---

<a id='mainwp-system-init'></a>
### `mainwp_system_init`

* MainWP_System constructor.

Runs any time class is called.

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 82](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L82)

---


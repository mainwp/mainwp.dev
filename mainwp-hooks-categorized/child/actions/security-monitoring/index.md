# Security & Monitoring Actions

Hooks related to security checks, uptime monitoring, and site health.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`admin_enqueue_scripts`](#admin-enqueue-scripts) - Method is_asset_in_admin()
- [`check_passwords`](#check-passwords) - Edit existing user.
- [`gpi_check_status`](#gpi-check-status) - Method save_settings()
- [`mainwp_child_actions_saved_number_of_days`](#mainwp-child-actions-saved-number-of-days) - Method to check actions data.
- [`mainwp_reports_sucuri_scan`](#mainwp-reports-sucuri-scan) - Save sucuri stream.
- [`mainwp_reports_wordfence_scan`](#mainwp-reports-wordfence-scan) - Method do_reports_log()
- [`phpmailer_init`](#phpmailer-init) - Check destination email.
- [`updraftplus_checkzip_end_{$type}`](#updraftplus-checkzip-end-type) - Restore all downloaded backups from history.
- [`updraftplus_checkzip_{$type}`](#updraftplus-checkzip-type) - Restore all downloaded backups from history.
- [`updraftplus_dbscan_urlchange`](#updraftplus-dbscan-urlchange) - Analyse old database file.
- [`updraftplus_dbscan_urlchange_www_append_warning`](#updraftplus-dbscan-urlchange-www-append-warning) - *Arguments*
- [`updraftplus_dirlist_sanitize_text_field()`](#updraftplus-dirlist-sanitize-text-field) - Check disk space used.
- [`wp_logout`](#wp-logout) - Method parse_login_required()

---

## Hook Details

<a id='admin-enqueue-scripts'></a>
### `admin_enqueue_scripts`

* Method is_asset_in_admin()

Check if the CSS/JS file is loaded in admin or not.

**Usage Locations:**

- [class/class-mainwp-child-html-regression.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-html-regression.php), [line 224](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-html-regression.php#L224)

---

<a id='check-passwords'></a>
### `check_passwords`

* Edit existing user.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($user->user_login, &$pass1, &$pass2)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($user->user_login, &$pass1, &$pass2)` |  |

**Usage Locations:**

- [class/class-mainwp-child-users.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php#L303)

---

<a id='gpi-check-status'></a>
### `gpi_check_status`

* Method save_settings()

Save the plugin settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 252](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L252)
- [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 429](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L429)
- [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 452](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L452)

---

<a id='mainwp-child-actions-saved-number-of-days'></a>
### `mainwp_child_actions_saved_number_of_days`

* Method to check actions data.

Clear old the action info.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$days_number` |  |

**Usage Locations:**

- [class/class-mainwp-child-actions.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-actions.php), [line 251](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-actions.php#L251)

---

<a id='mainwp-reports-sucuri-scan'></a>
### `mainwp_reports_sucuri_scan`

* Save sucuri stream.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  | 
`$scan_status` |  | 
`$scan_data` |  | 
`$scan_time` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  | 
`$scan_status` |  | 
`$scan_data` |  | 
`$scan_time` |  |

**Usage Locations:**

- [class/class-mainwp-client-report.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php), [line 179](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php#L179)

---

<a id='mainwp-reports-wordfence-scan'></a>
### `mainwp_reports_wordfence_scan`

* Method do_reports_log()

Add Wordfence data to the reports reports database table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$ctime` |  | 
`$details` |  | 
`$result` |  |

**Usage Locations:**

- [class/class-mainwp-child-wordfence.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wordfence.php), [line 309](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wordfence.php#L309)

---

<a id='phpmailer-init'></a>
### `phpmailer_init`

* Check destination email.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$phpmailer)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$phpmailer)` |  |

**Usage Locations:**

- [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 1311](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L1311)

---

<a id='updraftplus-checkzip-end-type'></a>
### `updraftplus_checkzip_end_{$type}`

* Restore all downloaded backups from history.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$mess, &$warn, &$err)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$mess, &$warn, &$err)` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)

---

<a id='updraftplus-checkzip-type'></a>
### `updraftplus_checkzip_{$type}`

* Restore all downloaded backups from history.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($updraft_dir . '/' . $file, &$mess, &$warn, &$err)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($updraft_dir . '/' . $file, &$mess, &$warn, &$err)` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)

---

<a id='updraftplus-dbscan-urlchange'></a>
### `updraftplus_dbscan_urlchange`

* Analyse old database file.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('Warning: %s', 'updraftplus'), '<a href="http://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>')` |  | 
`$old_siteurl` |  | 
`$res` | `string` | UpdraftPlus response.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('Warning: %s', 'updraftplus'), '<a href="http://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>')` |  | 
`$old_siteurl` |  | 
`$res` | `string` | UpdraftPlus response.

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2216](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2216)
- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2472](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2472)

---

<a id='updraftplus-dbscan-urlchange-www-append-warning'></a>
### `updraftplus_dbscan_urlchange_www_append_warning`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2639](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2639)

---

<a id='updraftplus-dirlist-sanitize-text-field'></a>
### `updraftplus_dirlist_sanitize_text_field()`

* Check disk space used.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$basedir` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$basedir` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3499](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3499)

---

<a id='wp-logout'></a>
### `wp_logout`

* Method parse_login_required()

Check if the login process is required.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php), [line 652](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-connect.php#L652)

---


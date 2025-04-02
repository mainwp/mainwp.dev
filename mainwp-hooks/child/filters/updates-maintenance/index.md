# Updates & Maintenance Filters

Hooks for managing updates to plugins, themes, and WordPress core.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`active_plugins`](#active-plugins) - *Arguments*
- [`get_backup_before_update_setting_wptc`](#get-backup-before-update-setting-wptc) - Get backup process progress.
- [`mainwp-child-get-total-size`](#mainwp-child-get-total-size) - Get total size of Child Site installation.
- [`mainwp_before_post_update`](#mainwp-before-post-update) - Hook: `mainwp_before_post_update`
- [`mainwp_child_after_update`](#mainwp-child-after-update) - Method to_update_plugins()
- [`mainwp_child_before_update`](#mainwp-child-before-update) - Method to_update_plugins()
- [`mainwp_child_before_update_plugin_theme`](#mainwp-child-before-update-plugin-theme) - Action before update plugin, theme.
- [`mainwp_child_before_update_wp`](#mainwp-child-before-update-wp) - Action before update WP.
- [`mainwp_child_db_updater_sync_data`](#mainwp-child-db-updater-sync-data) - Get sync data.
- [`mainwp_child_deactivation`](#mainwp-child-deactivation) - Method deactivation()
- [`mainwp_child_forced_get_total_size`](#mainwp-child-forced-get-total-size) - Get total size of Child Site installation.
- [`mainwp_child_get_total_size`](#mainwp-child-get-total-size) - Get total size of Child Site installation.
- [`mainwp_child_hide_update_notice`](#mainwp-child-hide-update-notice) - After admin bar render.
- [`mainwp_child_install_plugin_theme`](#mainwp-child-install-plugin-theme) - Method after_installed()
- [`mainwp_child_installPluginTheme`](#mainwp-child-installplugintheme) - Method after_installed()
- [`mainwp_child_mu_plugin_enabled`](#mainwp-child-mu-plugin-enabled) - Method deactivation()
- [`mainwp_child_plugin_action`](#mainwp-child-plugin-action) - Method delete_plugins()
- [`mainwp_child_plugin_health_check_max_plugins_to_batch`](#mainwp-child-plugin-health-check-max-plugins-to-batch) - *Arguments*
- [`mainwp_child_plugin_row_meta`](#mainwp-child-plugin-row-meta) - MainWP Child Plugin meta data.
- [`mainwp_child_theme_action`](#mainwp-child-theme-action) - Method theme_action()
- [`mainwp_child_theme_health_check_max_themes_to_batch`](#mainwp-child-theme-health-check-max-themes-to-batch) - *Arguments*
- [`mainwp_reports_maintenance`](#mainwp-reports-maintenance) - Method maintenance_db()
- [`mwp_premium_perform_update`](#mwp-premium-perform-update) - Method upgrade_plugin()
- [`mwp_premium_update_check`](#mwp-premium-update-check) - Check for premium updates.
- [`mwp_premium_update_notification`](#mwp-premium-update-notification) - Check for premium updates.
- [`plugins_api`](#plugins-api) - Method to_update_plugins()
- [`swis_clear_complete_cache`](#swis-clear-complete-cache) - Purge Swis Performance plugin cache.
- [`update_white_labling_settings_wptc`](#update-white-labling-settings-wptc) - Process the sigin response info.
- [`user_profile_update_errors`](#user-profile-update-errors) - Edit existing user.
- [`woocommerce_hide_{$name}_notice`](#woocommerce-hide-name-notice) - Hide a single notice.

---

## Hook Details

<a id='active-plugins'></a>
### `active_plugins`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`get_option('active_plugins')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`get_option('active_plugins')` |  |

**Usage Locations:**

- [class/class-mainwp-child-wp-seopress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php), [line 59](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php#L59)
- [class/class-mainwp-child-wp-seopress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php), [line 77](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php#L77)

---

<a id='get-backup-before-update-setting-wptc'></a>
### `get_backup_before_update_setting_wptc`

* Get backup process progress.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 497](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L497)

---

<a id='mainwp-child-get-total-size'></a>
### `mainwp-child-get-total-size`

* Get total size of Child Site installation.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(true)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_get_total_size'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(true)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_get_total_size'` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 945](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L945)

---

<a id='mainwp-before-post-update'></a>
### `mainwp_before_post_update`

* Hook: `mainwp_before_post_update`

Runs before creating or updating a post via MainWP dashboard.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$new_post` | `array` | � Post data array.
`$post_custom` | `array` | � Post custom meta data.
`$post_category` | `string` | � Post categories.
`$post_tags` | `string` | � Post tags.
`$others` |  |

**Usage Locations:**

- [class/class-mainwp-child-posts.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php), [line 777](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php#L777)

---

<a id='mainwp-child-after-update'></a>
### `mainwp_child_after_update`

* Method to_update_plugins()

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`$result` |  | 
`$plugins` | `array` | An array containing plugins to be updated.

**Usage Locations:**

- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 356](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L356)
- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 547](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L547)

---

<a id='mainwp-child-before-update'></a>
### `mainwp_child_before_update`

* Method to_update_plugins()

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`$plugins` | `array` | An array containing plugins to be updated.

**Usage Locations:**

- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 356](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L356)
- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 547](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L547)

---

<a id='mainwp-child-before-update-plugin-theme'></a>
### `mainwp_child_before_update_plugin_theme`

* Action before update plugin, theme.

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Usage Locations:**

- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 115](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L115)

---

<a id='mainwp-child-before-update-wp'></a>
### `mainwp_child_before_update_wp`

* Action before update WP.

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Usage Locations:**

- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 1171](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L1171)

---

<a id='mainwp-child-db-updater-sync-data'></a>
### `mainwp_child_db_updater_sync_data`

* Get sync data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-db-updater.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater.php), [line 100](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater.php#L100)

---

<a id='mainwp-child-deactivation'></a>
### `mainwp_child_deactivation`

* Method deactivation()

Deactivate the MainWP Child plugin.

**Usage Locations:**

- [class/class-mainwp-child.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php), [line 460](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php#L460)

---

<a id='mainwp-child-forced-get-total-size'></a>
### `mainwp_child_forced_get_total_size`

* Get total size of Child Site installation.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 945](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L945)

---

<a id='mainwp-child-get-total-size'></a>
### `mainwp_child_get_total_size`

* Get total size of Child Site installation.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$get_file_size` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$get_file_size` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 945](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L945)

---

<a id='mainwp-child-hide-update-notice'></a>
### `mainwp_child_hide_update_notice`

* After admin bar render.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-branding-render.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php), [line 207](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php#L207)
- [class/class-mainwp-child-branding-render.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php), [line 261](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php#L261)

---

<a id='mainwp-child-install-plugin-theme'></a>
### `mainwp_child_install_plugin_theme`

* Method after_installed()

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  |

**Usage Locations:**

- [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 486](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L486)

---

<a id='mainwp-child-installplugintheme'></a>
### `mainwp_child_installPluginTheme`

* Method after_installed()

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($args)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_install_plugin_theme'` |  |

**Usage Locations:**

- [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 486](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L486)

---

<a id='mainwp-child-mu-plugin-enabled'></a>
### `mainwp_child_mu_plugin_enabled`

* Method deactivation()

Deactivate the MainWP Child plugin.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [class/class-mainwp-child.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php), [line 460](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php#L460)
- [class/class-mainwp-child.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php), [line 481](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php#L481)

---

<a id='mainwp-child-plugin-action'></a>
### `mainwp_child_plugin_action`

* Method delete_plugins()

Delete a plugin from the Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  |

**Usage Locations:**

- [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 158](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L158)

---

<a id='mainwp-child-plugin-health-check-max-plugins-to-batch'></a>
### `mainwp_child_plugin_health_check_max_plugins_to_batch`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Usage Locations:**

- [class/class-mainwp-child-plugins-check.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-plugins-check.php), [line 286](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-plugins-check.php#L286)

---

<a id='mainwp-child-plugin-row-meta'></a>
### `mainwp_child_plugin_row_meta`

* MainWP Child Plugin meta data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugin_meta` | `array` | Plugin meta.
`$plugin_file` | `string` | Plugin file.
`$mainWPChild->plugin_slug` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugin_meta` | `array` | Plugin meta.
`$plugin_file` | `string` | Plugin file.
`$mainWPChild->plugin_slug` |  |

**Usage Locations:**

- [class/class-mainwp-pages.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php), [line 295](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php#L295)

---

<a id='mainwp-child-theme-action'></a>
### `mainwp_child_theme_action`

* Method theme_action()

Theme Activate, Deactivate & Delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  |

**Usage Locations:**

- [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 230](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L230)

---

<a id='mainwp-child-theme-health-check-max-themes-to-batch'></a>
### `mainwp_child_theme_health_check_max_themes_to_batch`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  |

**Usage Locations:**

- [class/class-mainwp-child-themes-check.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-themes-check.php), [line 253](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-themes-check.php#L253)

---

<a id='mainwp-reports-maintenance'></a>
### `mainwp_reports_maintenance`

* Method maintenance_db()

Child site database maintenance.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$log_time` |  | 
`$details` |  | 
`$result` |  | 
`$max_revisions` | `int` | Maximum revisions to keep.

**Usage Locations:**

- [class/class-mainwp-child-maintenance.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-maintenance.php), [line 92](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-maintenance.php#L92)

---

<a id='mwp-premium-perform-update'></a>
### `mwp_premium_perform_update`

* Method upgrade_plugin()

Initiate the plugin update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 188](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L188)
- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 464](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L464)

---

<a id='mwp-premium-update-check'></a>
### `mwp_premium_update_check`

* Check for premium updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 685](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L685)

---

<a id='mwp-premium-update-notification'></a>
### `mwp_premium_update_notification`

* Check for premium updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 685](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L685)

---

<a id='plugins-api'></a>
### `plugins_api`

* Method to_update_plugins()

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`'plugin_information'` |  | 
`array('slug' => $plugin)` |  |

**Usage Locations:**

- [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 356](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L356)

---

<a id='swis-clear-complete-cache'></a>
### `swis_clear_complete_cache`

* Purge Swis Performance plugin cache.

Source: [./sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 369](class/class-mainwp-child-cache-purge.php#L369-L389)

**Usage Locations:**

- [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 369](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L369)

---

<a id='update-white-labling-settings-wptc'></a>
### `update_white_labling_settings_wptc`

* Process the sigin response info.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cust_req_info` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cust_req_info` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1233](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1233)

---

<a id='user-profile-update-errors'></a>
### `user_profile_update_errors`

* Edit existing user.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$errors, $update, &$user)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$errors, $update, &$user)` |  |

**Usage Locations:**

- [class/class-mainwp-child-users.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php#L303)

---

<a id='woocommerce-hide-name-notice'></a>
### `woocommerce_hide_{$name}_notice`

* Hide a single notice.

Source: [./sources/mainwp-child/class/class-mainwp-child-db-updater-wc.php](class/class-mainwp-child-db-updater-wc.php), [line 222](class/class-mainwp-child-db-updater-wc.php#L222-L230)

**Usage Locations:**

- [class/class-mainwp-child-db-updater-wc.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater-wc.php), [line 222](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater-wc.php#L222)

---


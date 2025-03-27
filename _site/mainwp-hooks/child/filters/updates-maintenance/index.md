# Updates & Maintenance Filters

Hooks for managing updates to plugins, themes, and WordPress core.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`update_white_labling_settings_wptc`](#update_white_labling_settings_wptc) - Process the sigin response info.
- [`woocommerce_hide_{$name}_notice`](#woocommerce_hide_name_notice) - Hide a single notice.
- [`user_profile_update_errors`](#user_profile_update_errors) - Edit existing user.
- [`swis_clear_complete_cache`](#swis_clear_complete_cache) - Purge Swis Performance plugin cache.
- [`mainwp_reports_maintenance`](#mainwp_reports_maintenance) - Method maintenance_db()
- [`mainwp_child_plugin_action`](#mainwp_child_plugin_action) - Method delete_plugins()
- [`mainwp_child_theme_action`](#mainwp_child_theme_action) - Method theme_action()
- [`mainwp_child_installPluginTheme`](#mainwp_child_installPluginTheme) - Method after_installed()
- [`mainwp_child_install_plugin_theme`](#mainwp_child_install_plugin_theme) - Method after_installed()
- [`mainwp_child_installPluginTheme`](#mainwp_child_installPluginTheme) - Method after_installed()
- [`mainwp_child_install_plugin_theme`](#mainwp_child_install_plugin_theme) - Method after_installed()
- [`mainwp_before_post_update`](#mainwp_before_post_update) - Hook: `mainwp_before_post_update`
- [`mainwp_child_before_update_plugin_theme`](#mainwp_child_before_update_plugin_theme) - Action before update plugin, theme.
- [`mainwp_child_before_update`](#mainwp_child_before_update) - Method to_update_plugins()
- [`mainwp_child_after_update`](#mainwp_child_after_update) - Method to_update_plugins()
- [`mainwp_child_before_update`](#mainwp_child_before_update) - Method to_upgrade_themes()
- [`mainwp_child_after_update`](#mainwp_child_after_update) - Method to_upgrade_themes()
- [`mainwp_child_before_update_wp`](#mainwp_child_before_update_wp) - Action before update WP.
- [`mainwp_child_deactivation`](#mainwp_child_deactivation) - Method deactivation()
- [`mainwp_child_plugin_row_meta`](#mainwp_child_plugin_row_meta) - MainWP Child Plugin meta data.
- [`mwp_premium_update_check`](#mwp_premium_update_check) - Check for premium updates.
- [`mwp_premium_update_notification`](#mwp_premium_update_notification) - Check for premium updates.
- [`mainwp-child-get-total-size`](#mainwp-child-get-total-size) - Get total size of Child Site installation.
- [`mainwp_child_get_total_size`](#mainwp_child_get_total_size) - Get total size of Child Site installation.
- [`mainwp_child_forced_get_total_size`](#mainwp_child_forced_get_total_size) - Get total size of Child Site installation.
- [`get_backup_before_update_setting_wptc`](#get_backup_before_update_setting_wptc) - Get backup process progress.
- [`active_plugins`](#active_plugins) - *Arguments*
- [`active_plugins`](#active_plugins) - *Arguments*
- [`mainwp_child_theme_health_check_max_themes_to_batch`](#mainwp_child_theme_health_check_max_themes_to_batch) - *Arguments*
- [`mainwp_child_db_updater_sync_data`](#mainwp_child_db_updater_sync_data) - Get sync data.
- [`mainwp_child_hide_update_notice`](#mainwp_child_hide_update_notice) - After admin bar render.
- [`mainwp_child_hide_update_notice`](#mainwp_child_hide_update_notice) - Admin footer text.
- [`mainwp_child_plugin_health_check_max_plugins_to_batch`](#mainwp_child_plugin_health_check_max_plugins_to_batch) - *Arguments*
- [`mwp_premium_perform_update`](#mwp_premium_perform_update) - Method upgrade_plugin()
- [`plugins_api`](#plugins_api) - Method to_update_plugins()
- [`mwp_premium_perform_update`](#mwp_premium_perform_update) - Method upgrade_theme()
- [`mainwp_child_mu_plugin_enabled`](#mainwp_child_mu_plugin_enabled) - Method deactivation()
- [`mainwp_child_mu_plugin_enabled`](#mainwp_child_mu_plugin_enabled) - Method delete_connection_data()

## Hook Details

### `update_white_labling_settings_wptc`

*Process the sigin response info.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cust_req_info` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1233](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1233)



### `woocommerce_hide_{$name}_notice`

*Hide a single notice.*


Source: [class/class-mainwp-child-db-updater-wc.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater-wc.php), [line 222](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater-wc.php#L222)



### `user_profile_update_errors`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$errors, $update, &$user)` |  | 

Source: [class/class-mainwp-child-users.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php#L303)



### `swis_clear_complete_cache`

*Purge Swis Performance plugin cache.*


Source: [class/class-mainwp-child-cache-purge.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php), [line 369](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-cache-purge.php#L369)



### `mainwp_reports_maintenance`

*Method maintenance_db()*

Child site database maintenance.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$log_time` |  | 
`$details` |  | 
`$result` |  | 
`$max_revisions` | `int` | Maximum revisions to keep.

Source: [class/class-mainwp-child-maintenance.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-maintenance.php), [line 92](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-maintenance.php#L92)



### `mainwp_child_plugin_action`

*Method delete_plugins()*

Delete a plugin from the Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 158](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L158)



### `mainwp_child_theme_action`

*Method theme_action()*

Theme Activate, Deactivate & Delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 230](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L230)



### `mainwp_child_installPluginTheme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($args)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_install_plugin_theme'` |  | 

Source: [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 491](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L491)



### `mainwp_child_install_plugin_theme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 491](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L491)



### `mainwp_child_installPluginTheme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($args)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_install_plugin_theme'` |  | 

Source: [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 491](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L491)



### `mainwp_child_install_plugin_theme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [class/class-mainwp-child-install.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php), [line 491](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-install.php#L491)



### `mainwp_before_post_update`

*Hook: `mainwp_before_post_update`*

Runs before creating or updating a post via MainWP dashboard.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$new_post` | `array` | � Post data array.
`$post_custom` | `array` | � Post custom meta data.
`$post_category` | `string` | � Post categories.
`$post_tags` | `string` | � Post tags.
`$others` |  | 

Source: [class/class-mainwp-child-posts.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php), [line 777](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-posts.php#L777)



### `mainwp_child_before_update_plugin_theme`

*Action before update plugin, theme.*


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 115](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L115)



### `mainwp_child_before_update`

*Method to_update_plugins()*

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`$plugins` | `array` | An array containing plugins to be updated.

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 356](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L356)



### `mainwp_child_after_update`

*Method to_update_plugins()*

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`$result` |  | 
`$plugins` | `array` | An array containing plugins to be updated.

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 356](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L356)



### `mainwp_child_before_update`

*Method to_upgrade_themes()*

Complete the themes update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 
`$themes` | `array` | An array containing themes to be updated.

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 547](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L547)



### `mainwp_child_after_update`

*Method to_upgrade_themes()*

Complete the themes update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 
`$result` |  | 
`$themes` | `array` | An array containing themes to be updated.

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 547](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L547)



### `mainwp_child_before_update_wp`

*Action before update WP.*


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 1171](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L1171)



### `mainwp_child_deactivation`

*Method deactivation()*

Deactivate the MainWP Child plugin.


Source: [class/class-mainwp-child.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php), [line 460](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php#L460)

## Filters



### `mainwp_child_plugin_row_meta`

*MainWP Child Plugin meta data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugin_meta` | `array` | Plugin meta.
`$plugin_file` | `string` | Plugin file.
`$mainWPChild->plugin_slug` |  | 

Source: [class/class-mainwp-pages.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php), [line 295](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-pages.php#L295)



### `mwp_premium_update_check`

*Check for premium updates.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 685](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L685)



### `mwp_premium_update_notification`

*Check for premium updates.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 685](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L685)



### `mainwp-child-get-total-size`

*Get total size of Child Site installation.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(true)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_get_total_size'` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 945](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L945)



### `mainwp_child_get_total_size`

*Get total size of Child Site installation.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$get_file_size` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 945](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L945)



### `mainwp_child_forced_get_total_size`

*Get total size of Child Site installation.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-child-stats.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php), [line 945](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-stats.php#L945)



### `get_backup_before_update_setting_wptc`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 497](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L497)



### `active_plugins`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`get_option('active_plugins')` |  | 

Source: [class/class-mainwp-child-wp-seopress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php), [line 59](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php#L59)



### `active_plugins`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`get_option('active_plugins')` |  | 

Source: [class/class-mainwp-child-wp-seopress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php), [line 77](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wp-seopress.php#L77)



### `mainwp_child_theme_health_check_max_themes_to_batch`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [class/class-mainwp-child-themes-check.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-themes-check.php), [line 253](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-themes-check.php#L253)



### `mainwp_child_db_updater_sync_data`

*Get sync data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-db-updater.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater.php), [line 100](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-db-updater.php#L100)



### `mainwp_child_hide_update_notice`

*After admin bar render.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-branding-render.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php), [line 207](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php#L207)



### `mainwp_child_hide_update_notice`

*Admin footer text.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-branding-render.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php), [line 261](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding-render.php#L261)



### `mainwp_child_plugin_health_check_max_plugins_to_batch`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [class/class-mainwp-child-plugins-check.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-plugins-check.php), [line 286](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-plugins-check.php#L286)



### `mwp_premium_perform_update`

*Method upgrade_plugin()*

Initiate the plugin update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 188](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L188)



### `plugins_api`

*Method to_update_plugins()*

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`'plugin_information'` |  | 
`array('slug' => $plugin)` |  | 

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 356](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L356)



### `mwp_premium_perform_update`

*Method upgrade_theme()*

Execute themes updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-updates.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php), [line 464](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updates.php#L464)



### `mainwp_child_mu_plugin_enabled`

*Method deactivation()*

Deactivate the MainWP Child plugin.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-child.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php), [line 460](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php#L460)



### `mainwp_child_mu_plugin_enabled`

*Method delete_connection_data()*

Delete connection data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-child.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php), [line 481](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child.php#L481)


<p align="center"><a href="https://github.com/pronamic/wp-documentor"><img src="https://cdn.jsdelivr.net/gh/pronamic/wp-documentor@main/logos/pronamic-wp-documentor.svgo-min.svg" alt="Pronamic WordPress Documentor" width="32" height="32"></a><br><em>Generated by <a href="https://github.com/pronamic/wp-documentor">Pronamic WordPress Documentor</a> <code>1.2.0</code></em><p>




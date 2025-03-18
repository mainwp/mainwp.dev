# Updates & Maintenance Filters

Hooks for managing updates to plugins, themes, and WordPress core.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`update_white_labling_settings_wptc`](#update_white_labling_settings_wptc) - Process the sigin response info.
- [`mainwp_child_plugin_action`](#mainwp_child_plugin_action) - Method delete_plugins()
- [`mainwp_child_theme_action`](#mainwp_child_theme_action) - Method theme_action()
- [`mainwp_child_installPluginTheme`](#mainwp_child_installPluginTheme) - Method after_installed()
- [`mainwp_child_install_plugin_theme`](#mainwp_child_install_plugin_theme) - Method after_installed()
- [`mainwp_child_installPluginTheme`](#mainwp_child_installPluginTheme) - Method after_installed()
- [`mainwp_child_install_plugin_theme`](#mainwp_child_install_plugin_theme) - Method after_installed()
- [`woocommerce_hide_{$name}_notice`](#woocommerce_hide_name_notice) - Hide a single notice.
- [`user_profile_update_errors`](#user_profile_update_errors) - Edit existing user.
- [`mainwp_reports_maintenance`](#mainwp_reports_maintenance) - Method maintenance_db()
- [`mainwp_child_before_update_plugin_theme`](#mainwp_child_before_update_plugin_theme) - Action before update plugin, theme.
- [`mainwp_child_before_update`](#mainwp_child_before_update) - Method to_update_plugins()
- [`mainwp_child_after_update`](#mainwp_child_after_update) - Method to_update_plugins()
- [`mainwp_child_before_update`](#mainwp_child_before_update) - Method to_upgrade_themes()
- [`mainwp_child_after_update`](#mainwp_child_after_update) - Method to_upgrade_themes()
- [`mainwp_child_before_update_wp`](#mainwp_child_before_update_wp) - Action before update WP.
- [`swis_clear_complete_cache`](#swis_clear_complete_cache) - Purge Swis Performance plugin cache.
- [`mainwp_child_deactivation`](#mainwp_child_deactivation) - Method deactivation()
- [`mainwp_before_post_update`](#mainwp_before_post_update) - Hook: `mainwp_before_post_update`
- [`mainwp_child_plugin_health_check_max_plugins_to_batch`](#mainwp_child_plugin_health_check_max_plugins_to_batch) - *Arguments*
- [`active_plugins`](#active_plugins) - *Arguments*
- [`active_plugins`](#active_plugins) - *Arguments*
- [`get_backup_before_update_setting_wptc`](#get_backup_before_update_setting_wptc) - Get backup process progress.
- [`mainwp_child_theme_health_check_max_themes_to_batch`](#mainwp_child_theme_health_check_max_themes_to_batch) - *Arguments*
- [`mainwp_child_hide_update_notice`](#mainwp_child_hide_update_notice) - After admin bar render.
- [`mainwp_child_hide_update_notice`](#mainwp_child_hide_update_notice) - Admin footer text.
- [`mwp_premium_update_check`](#mwp_premium_update_check) - Check for premium updates.
- [`mwp_premium_update_notification`](#mwp_premium_update_notification) - Check for premium updates.
- [`mainwp-child-get-total-size`](#mainwp-child-get-total-size) - Get total size of Child Site installation.
- [`mainwp_child_get_total_size`](#mainwp_child_get_total_size) - Get total size of Child Site installation.
- [`mainwp_child_forced_get_total_size`](#mainwp_child_forced_get_total_size) - Get total size of Child Site installation.
- [`mwp_premium_perform_update`](#mwp_premium_perform_update) - Method upgrade_plugin()
- [`plugins_api`](#plugins_api) - Method to_update_plugins()
- [`mwp_premium_perform_update`](#mwp_premium_perform_update) - Method upgrade_theme()
- [`mainwp_child_plugin_row_meta`](#mainwp_child_plugin_row_meta) - MainWP Child Plugin meta data.
- [`mainwp_child_mu_plugin_enabled`](#mainwp_child_mu_plugin_enabled) - Method deactivation()
- [`mainwp_child_mu_plugin_enabled`](#mainwp_child_mu_plugin_enabled) - Method delete_connection_data()
- [`mainwp_child_db_updater_sync_data`](#mainwp_child_db_updater_sync_data) - Get sync data.

## Hook Details

### `update_white_labling_settings_wptc`

*Process the sigin response info.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cust_req_info` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1233](class/class-mainwp-child-timecapsule.php#L1233-L1257)



### `mainwp_child_plugin_action`

*Method delete_plugins()*

Delete a plugin from the Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 158](class/class-mainwp-child-install.php#L158-L219)



### `mainwp_child_theme_action`

*Method theme_action()*

Theme Activate, Deactivate & Delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 230](class/class-mainwp-child-install.php#L230-L324)



### `mainwp_child_installPluginTheme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($args)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_install_plugin_theme'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 486](class/class-mainwp-child-install.php#L486-L531)



### `mainwp_child_install_plugin_theme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 486](class/class-mainwp-child-install.php#L486-L532)



### `mainwp_child_installPluginTheme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($args)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_install_plugin_theme'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 486](class/class-mainwp-child-install.php#L486-L555)



### `mainwp_child_install_plugin_theme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 486](class/class-mainwp-child-install.php#L486-L556)



### `woocommerce_hide_{$name}_notice`

*Hide a single notice.*


Source: [../sources/mainwp-child/class/class-mainwp-child-db-updater-wc.php](class/class-mainwp-child-db-updater-wc.php), [line 222](class/class-mainwp-child-db-updater-wc.php#L222-L230)



### `user_profile_update_errors`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$errors, $update, &$user)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-users.php](class/class-mainwp-child-users.php), [line 303](class/class-mainwp-child-users.php#L303-L434)



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

Source: [../sources/mainwp-child/class/class-mainwp-child-maintenance.php](class/class-mainwp-child-maintenance.php), [line 92](class/class-mainwp-child-maintenance.php#L92-L198)



### `mainwp_child_before_update_plugin_theme`

*Action before update plugin, theme.*


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 115](class/class-mainwp-child-updates.php#L115-L120)



### `mainwp_child_before_update`

*Method to_update_plugins()*

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`$plugins` | `array` | An array containing plugins to be updated.

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 356](class/class-mainwp-child-updates.php#L356-L374)



### `mainwp_child_after_update`

*Method to_update_plugins()*

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`$result` |  | 
`$plugins` | `array` | An array containing plugins to be updated.

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 356](class/class-mainwp-child-updates.php#L356-L379)



### `mainwp_child_before_update`

*Method to_upgrade_themes()*

Complete the themes update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 
`$themes` | `array` | An array containing themes to be updated.

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 547](class/class-mainwp-child-updates.php#L547-L583)



### `mainwp_child_after_update`

*Method to_upgrade_themes()*

Complete the themes update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 
`$result` |  | 
`$themes` | `array` | An array containing themes to be updated.

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 547](class/class-mainwp-child-updates.php#L547-L589)



### `mainwp_child_before_update_wp`

*Action before update WP.*


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 1171](class/class-mainwp-child-updates.php#L1171-L1176)



### `swis_clear_complete_cache`

*Purge Swis Performance plugin cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 369](class/class-mainwp-child-cache-purge.php#L369-L389)



### `mainwp_child_deactivation`

*Method deactivation()*

Deactivate the MainWP Child plugin.


Source: [../sources/mainwp-child/class/class-mainwp-child.php](class/class-mainwp-child.php), [line 460](class/class-mainwp-child.php#L460-L477)



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

Source: [../sources/mainwp-child/class/class-mainwp-child-posts.php](class/class-mainwp-child-posts.php), [line 777](class/class-mainwp-child-posts.php#L777-L787)

## Filters



### `mainwp_child_plugin_health_check_max_plugins_to_batch`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-plugins-check.php](class/class-mainwp-child-plugins-check.php), [line 286](class/class-mainwp-child-plugins-check.php#L286-L286)



### `active_plugins`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`get_option('active_plugins')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-wp-seopress.php](class/class-mainwp-child-wp-seopress.php), [line 59](class/class-mainwp-child-wp-seopress.php#L59-L59)



### `active_plugins`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`get_option('active_plugins')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-wp-seopress.php](class/class-mainwp-child-wp-seopress.php), [line 77](class/class-mainwp-child-wp-seopress.php#L77-L77)



### `get_backup_before_update_setting_wptc`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 497](class/class-mainwp-child-timecapsule.php#L497-L548)



### `mainwp_child_theme_health_check_max_themes_to_batch`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-themes-check.php](class/class-mainwp-child-themes-check.php), [line 253](class/class-mainwp-child-themes-check.php#L253-L253)



### `mainwp_child_hide_update_notice`

*After admin bar render.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-branding-render.php](class/class-mainwp-child-branding-render.php), [line 207](class/class-mainwp-child-branding-render.php#L207-L211)



### `mainwp_child_hide_update_notice`

*Admin footer text.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-branding-render.php](class/class-mainwp-child-branding-render.php), [line 261](class/class-mainwp-child-branding-render.php#L261-L265)



### `mwp_premium_update_check`

*Check for premium updates.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 685](class/class-mainwp-child-stats.php#L685-L697)



### `mwp_premium_update_notification`

*Check for premium updates.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 685](class/class-mainwp-child-stats.php#L685-L708)



### `mainwp-child-get-total-size`

*Get total size of Child Site installation.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(true)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_get_total_size'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 945](class/class-mainwp-child-stats.php#L945-L955)



### `mainwp_child_get_total_size`

*Get total size of Child Site installation.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$get_file_size` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 945](class/class-mainwp-child-stats.php#L945-L956)



### `mainwp_child_forced_get_total_size`

*Get total size of Child Site installation.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 945](class/class-mainwp-child-stats.php#L945-L957)



### `mwp_premium_perform_update`

*Method upgrade_plugin()*

Initiate the plugin update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 188](class/class-mainwp-child-updates.php#L188-L271)



### `plugins_api`

*Method to_update_plugins()*

Complete the plugins update process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`'plugin_information'` |  | 
`array('slug' => $plugin)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 356](class/class-mainwp-child-updates.php#L356-L393)



### `mwp_premium_perform_update`

*Method upgrade_theme()*

Execute themes updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updates.php](class/class-mainwp-child-updates.php), [line 464](class/class-mainwp-child-updates.php#L464-L521)



### `mainwp_child_plugin_row_meta`

*MainWP Child Plugin meta data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugin_meta` | `array` | Plugin meta.
`$plugin_file` | `string` | Plugin file.
`$mainWPChild->plugin_slug` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-pages.php](class/class-mainwp-pages.php), [line 295](class/class-mainwp-pages.php#L295-L315)



### `mainwp_child_mu_plugin_enabled`

*Method deactivation()*

Deactivate the MainWP Child plugin.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child.php](class/class-mainwp-child.php), [line 460](class/class-mainwp-child.php#L460-L471)



### `mainwp_child_mu_plugin_enabled`

*Method delete_connection_data()*

Delete connection data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child.php](class/class-mainwp-child.php), [line 481](class/class-mainwp-child.php#L481-L491)



### `mainwp_child_db_updater_sync_data`

*Get sync data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-db-updater.php](class/class-mainwp-child-db-updater.php), [line 100](class/class-mainwp-child-db-updater.php#L100-L104)


<p align="center"><a href="https://github.com/pronamic/wp-documentor"><img src="https://cdn.jsdelivr.net/gh/pronamic/wp-documentor@main/logos/pronamic-wp-documentor.svgo-min.svg" alt="Pronamic WordPress Documentor" width="32" height="32"></a><br><em>Generated by <a href="https://github.com/pronamic/wp-documentor">Pronamic WordPress Documentor</a> <code>1.2.0</code></em><p>




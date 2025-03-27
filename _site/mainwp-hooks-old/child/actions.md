# Hooks

- [Actions](#actions)
- [Filters](#filters)

## Actions

### `deprecated_hook_run`

*Support old WP version 4.0.*

Fires functions attached to a deprecated filter hook.

When a filter hook is deprecated, the apply_filters() call is replaced with
apply_filters_deprecated(), which triggers a deprecation notice and then fires
the original filter hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$hook_name` | `string` | The name of the filter hook.
`$replacement` | `string` | Optional. The hook that should have been used. Default empty.
`$version` | `string` | The version of WordPress that deprecated the hook.
`$message` | `string` | Optional. A message regarding the change. Default empty.

Source: [../sources/mainwp-child/includes/functions.php](includes/functions.php), [line 169](includes/functions.php#L169-L188)

### `admin_enqueue_scripts`

*Method is_asset_in_admin()*

Check if the CSS/JS file is loaded in admin or not.


Source: [../sources/mainwp-child/class/class-mainwp-child-html-regression.php](class/class-mainwp-child-html-regression.php), [line 224](class/class-mainwp-child-html-regression.php#L224-L238)

### `mainwp_child_site_stats`

*Get Child Site Stats.*


Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 141](class/class-mainwp-child-stats.php#L141-L358)

### `{$event}`

*Backup now.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`apply_filters($options, array())` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1101](class/class-mainwp-child-updraft-plus-backups.php#L1101-L1136)

### `updraftplus_checkzip_{$type}`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($updraft_dir . '/' . $file, &$mess, &$warn, &$err)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1898](class/class-mainwp-child-updraft-plus-backups.php#L1898-L2036)

### `updraftplus_checkzip_end_{$type}`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$mess, &$warn, &$err)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1898](class/class-mainwp-child-updraft-plus-backups.php#L1898-L2040)

### `mainwp_child_before_send_feedback_message`

*Action: process send feedback message.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  | 

**Changelog**

Version | Description
------- | -----------
`5.1` | 

Source: [../sources/mainwp-child/class/class-mainwp-helper.php](class/class-mainwp-helper.php), [line 72](class/class-mainwp-helper.php#L72-L77)

### `mainwp_child_before_send_close_message`

*Action: process before send close message.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$value` |  | 
`$action` |  | 

**Changelog**

Version | Description
------- | -----------
`4.4.0.3` | 

Source: [../sources/mainwp-child/class/class-mainwp-helper.php](class/class-mainwp-helper.php), [line 94](class/class-mainwp-helper.php#L94-L99)

### `mainwp_child_reports_log`

*Add support for the reporting system.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wptimecapsule'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 998](class/class-mainwp-child-timecapsule.php#L998-L1008)

### `mainwp_reports_wptimecapsule_backup`

*Add WP Time Capsule data to the reports database table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1014](class/class-mainwp-child-timecapsule.php#L1014-L1068)

### `update_white_labling_settings_wptc`

*Process the sigin response info.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cust_req_info` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1233](class/class-mainwp-child-timecapsule.php#L1233-L1257)

### `mainwp_child_reports_log`

*Backupbuddy Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backupbuddy'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-up-buddy.php](class/class-mainwp-child-back-up-buddy.php), [line 163](class/class-mainwp-child-back-up-buddy.php#L163-L170)

### `mainwp_reports_backupbuddy_backup`

*Create BackupBuddy Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backupType` |  | 
`$finish_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-up-buddy.php](class/class-mainwp-child-back-up-buddy.php), [line 176](class/class-mainwp-child-back-up-buddy.php#L176-L267)

### `mainwp_reports_backupbuddy_backup`

*Create BackupBuddy Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backupType` |  | 
`$finish_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-up-buddy.php](class/class-mainwp-child-back-up-buddy.php), [line 176](class/class-mainwp-child-back-up-buddy.php#L176-L291)

### `woocommerce_hide_{$name}_notice`

*Hide a single notice.*


Source: [../sources/mainwp-child/class/class-mainwp-child-db-updater-wc.php](class/class-mainwp-child-db-updater-wc.php), [line 222](class/class-mainwp-child-db-updater-wc.php#L222-L230)

### `mainwp_child_reports_log`

*Add support for the reporting system.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backupwordpress'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-up-wordpress.php](class/class-mainwp-child-back-up-wordpress.php), [line 303](class/class-mainwp-child-back-up-wordpress.php#L303-L313)

### `mainwp_reports_backupwordpress_backup`

*Add BackUpWordPress data to the reports database table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$destination` |  | 
`$message` |  | 
`'finished'` |  | 
`$backup_type` |  | 
`$date` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-up-wordpress.php](class/class-mainwp-child-back-up-wordpress.php), [line 319](class/class-mainwp-child-back-up-wordpress.php#L319-L358)

### `check_passwords`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($user->user_login, &$pass1, &$pass2)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-users.php](class/class-mainwp-child-users.php), [line 303](class/class-mainwp-child-users.php#L303-L395)

### `user_profile_update_errors`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$errors, $update, &$user)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-users.php](class/class-mainwp-child-users.php), [line 303](class/class-mainwp-child-users.php#L303-L434)

### `swis_clear_complete_cache`

*Purge Swis Performance plugin cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 369](class/class-mainwp-child-cache-purge.php#L369-L389)

### `rt_nginx_helper_purge_all`

*Purge Nginx Helper cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 716](class/class-mainwp-child-cache-purge.php#L716-L729)

### `wphb_clear_page_cache`

*Purge WP Hummingbird cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 741](class/class-mainwp-child-cache-purge.php#L741-L756)

### `wpfc_clear_all_cache`

*Purge WP Fastest Cache.*


Source: [../sources/mainwp-child/class/class-mainwp-child-cache-purge.php](class/class-mainwp-child-cache-purge.php), [line 818](class/class-mainwp-child-cache-purge.php#L818-L831)

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

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 491](class/class-mainwp-child-install.php#L491-L536)

### `mainwp_child_install_plugin_theme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 491](class/class-mainwp-child-install.php#L491-L537)

### `mainwp_child_installPluginTheme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($args)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_install_plugin_theme'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 491](class/class-mainwp-child-install.php#L491-L560)

### `mainwp_child_install_plugin_theme`

*Method after_installed()*

After plugin or theme has been installed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-install.php](class/class-mainwp-child-install.php), [line 491](class/class-mainwp-child-install.php#L491-L561)

### `mainwp_reports_sucuri_scan`

*Save sucuri stream.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  | 
`$scan_status` |  | 
`$scan_data` |  | 
`$scan_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-client-report.php](class/class-mainwp-client-report.php), [line 179](class/class-mainwp-client-report.php#L179-L191)

### `mainwp_backup`

*Save backup stream.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$destination` |  | 
`$message` |  | 
`$size` |  | 
`$status` |  | 
`$type` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-client-report.php](class/class-mainwp-client-report.php), [line 195](class/class-mainwp-client-report.php#L195-L208)

### `mainwp_child_after_newpost`

*Build New Post.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-posts.php](class/class-mainwp-child-posts.php), [line 373](class/class-mainwp-child-posts.php#L373-L405)

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

### `mainwp_child_reports_log`

*Method do_site_stats()*

Add support for the reporting system.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wordfence'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-wordfence.php](class/class-mainwp-child-wordfence.php), [line 300](class/class-mainwp-child-wordfence.php#L300-L306)

### `mainwp_reports_wordfence_scan`

*Method do_reports_log()*

Add Wordfence data to the reports reports database table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$ctime` |  | 
`$details` |  | 
`$result` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-wordfence.php](class/class-mainwp-child-wordfence.php), [line 309](class/class-mainwp-child-wordfence.php#L309-L371)

### `run_gpi`

*Method do_check_pages()*

Check or force re-check pages page speed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$forceRecheck` | `bool` | If true, force recheck process, if false, just regular check.

Source: [../sources/mainwp-child/class/class-mainwp-child-pagespeed.php](class/class-mainwp-child-pagespeed.php), [line 429](class/class-mainwp-child-pagespeed.php#L429-L445)

### `mainwp_child_reports_log`

*Record BackWPup MainWP Child Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backwpup'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 307](class/class-mainwp-child-back-wp-up.php#L307-L314)

### `mainwp_reports_backwpup_backup`

*Create BackWPup MainWP Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 320](class/class-mainwp-child-back-wp-up.php#L320-L409)

### `phpmailer_init`

*Check destination email.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$phpmailer)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 1311](class/class-mainwp-child-back-wp-up.php#L1311-L1363)

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

### `mainwp_child_deactivation`

*Method deactivation()*

Deactivate the MainWP Child plugin.


Source: [../sources/mainwp-child/class/class-mainwp-child.php](class/class-mainwp-child.php), [line 460](class/class-mainwp-child.php#L460-L477)

## Filters

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

### `{$hook_name}`

*Support old WP version 4.0.*

Fires functions attached to a deprecated filter hook.

When a filter hook is deprecated, the apply_filters() call is replaced with
apply_filters_deprecated(), which triggers a deprecation notice and then fires
the original filter hook.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` | `array` | Array of additional function arguments to be passed to apply_filters().

Source: [../sources/mainwp-child/includes/functions.php](includes/functions.php), [line 169](includes/functions.php#L169-L189)

### `error_log_mainwp_logs`

*Render the error log content.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($error_log)` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-server-information.php](class/class-mainwp-child-server-information.php), [line 1089](class/class-mainwp-child-server-information.php#L1089-L1107)

### `error_log_mainwp_lines`

*Render the error log content.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-server-information.php](class/class-mainwp-child-server-information.php), [line 1089](class/class-mainwp-child-server-information.php#L1089-L1108)

### `https_local_ssl_verify`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-server-information-base.php](class/class-mainwp-child-server-information-base.php), [line 702](class/class-mainwp-child-server-information-base.php#L702-L702)

### `mainwp-child-init-subpages`

*Initiate MainWP Child Plugin pages.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.1'` |  | 
`'mainwp_child_init_subpages'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-pages.php](class/class-mainwp-pages.php), [line 230](class/class-mainwp-pages.php#L230-L246)

### `mainwp_child_init_subpages`

*Initiate MainWP Child Plugin pages.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$all_subpages` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-pages.php](class/class-mainwp-pages.php), [line 230](class/class-mainwp-pages.php#L230-L247)

### `mainwp_child_plugin_row_meta`

*MainWP Child Plugin meta data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugin_meta` | `array` | Plugin meta.
`$plugin_file` | `string` | Plugin file.
`$mainWPChild->plugin_slug` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-pages.php](class/class-mainwp-pages.php), [line 295](class/class-mainwp-pages.php#L295-L315)

### `mainwp-site-sync-others-data`

*Get other stats data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($information, $othersData)` |  | 
`'4.0.7.1'` |  | 
`'mainwp_site_sync_others_data'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 466](class/class-mainwp-child-stats.php#L466-L482)

### `mainwp_site_sync_others_data`

*Get other stats data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Child Site Stats array.
`$othersData` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-stats.php](class/class-mainwp-child-stats.php), [line 466](class/class-mainwp-child-stats.php#L466-L483)

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

### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 145](class/class-mainwp-child-woocommerce-status.php#L145-L145)

### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 168](class/class-mainwp-child-woocommerce-status.php#L168-L168)

### `mainwp_child_woocom_sync_data`

*Sync Woocommerce data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 113](class/class-mainwp-child-woocommerce-status.php#L113-L213)

### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 258](class/class-mainwp-child-woocommerce-status.php#L258-L258)

### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 277](class/class-mainwp-child-woocommerce-status.php#L277-L277)

### `mainwp_child_woocom_report_data`

*Woocommerce report data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 220](class/class-mainwp-child-woocommerce-status.php#L220-L319)

### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 522](class/class-mainwp-child-woocommerce-status.php#L522-L522)

### `woocommerce_dashboard_status_widget_sales_query`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$query` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 527](class/class-mainwp-child-woocommerce-status.php#L527-L527)

### `woocommerce_reports_order_statuses`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('completed', 'processing', 'on-hold')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 536](class/class-mainwp-child-woocommerce-status.php#L536-L536)

### `mainwp_child_woocom_get_data`

*Get Woocommerce reports old.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-woocommerce-status.php](class/class-mainwp-child-woocommerce-status.php), [line 490](class/class-mainwp-child-woocommerce-status.php#L490-L585)

### `updraft_backupnow_options`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$options` |  | 
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1136](class/class-mainwp-child-updraft-plus-backups.php#L1136-L1136)

### `updraftplus_accept_archivename`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1898](class/class-mainwp-child-updraft-plus-backups.php#L1898-L1980)

### `updraftplus_importforeign_backupable_plus_db`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($backupable_plus_db, array($foreign_known[$backups[$timestamp]['meta_foreign']], &$mess, &$warn, &$err))` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1898](class/class-mainwp-child-updraft-plus-backups.php#L1898-L1996)

### `updraftplus_dbscan_urlchange`

*Analyse old database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('Warning: %s', 'updraftplus'), '<a href="http://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>')` |  | 
`$old_siteurl` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2216](class/class-mainwp-child-updraft-plus-backups.php#L2216-L2367)

### `updraftplus_dbscan_urlchange`

*Analyse old database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('Warning: %s', 'updraftplus'), '<a href="http://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>')` |  | 
`$old_home` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2216](class/class-mainwp-child-updraft-plus-backups.php#L2216-L2377)

### `updraftplus_https_to_http_additional_warning`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('This restoration will work if you still have an SSL certificate (i.e. can use https) to access the site. Otherwise, you will want to use %s to search/replace the site address so that the site can be visited without https.', 'updraftplus'), '<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>')` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2634](class/class-mainwp-child-updraft-plus-backups.php#L2634-L2634)

### `updraftplus_http_to_https_additional_warning`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('As long as your web hosting allows http (i.e. non-SSL access) or will forward requests to https (which is almost always the case), this is no problem. If that is not yet set up, then you should set it up, or use %s so that the non-https links are automatically replaced.', 'updraftplus'), apply_filters('<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'))` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2636](class/class-mainwp-child-updraft-plus-backups.php#L2636-L2636)

### `updraftplus_migrator_addon_link`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2636](class/class-mainwp-child-updraft-plus-backups.php#L2636-L2636)

### `updraftplus_dbscan_urlchange_www_append_warning`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2639](class/class-mainwp-child-updraft-plus-backups.php#L2639-L2639)

### `updraftplus_dbscan_urlchange`

*Analyse database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>'` |  | 
`$old_siteurl` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2472](class/class-mainwp-child-updraft-plus-backups.php#L2472-L2645)

### `updraftplus_com_link`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'https://updraftplus.com/faqs/tell-me-more-about-the-search-and-replace-site-location-in-the-database-option/'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2648](class/class-mainwp-child-updraft-plus-backups.php#L2648-L2648)

### `updraftplus_dbscan_urlchange`

*Analyse database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>'` |  | 
`$old_home` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2472](class/class-mainwp-child-updraft-plus-backups.php#L2472-L2664)

### `updraftplus_accept_archivename`

*Build existing backups table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 3006](class/class-mainwp-child-updraft-plus-backups.php#L3006-L3043)

### `updraftplus_showbackup_date`

*Date label.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pretty_date` | `string` | Pretty date.
`$backup` | `string` | Type of backup.
`$jobdata` | `array` | Job data.
`(int) $key` |  | 
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 3192](class/class-mainwp-child-updraft-plus-backups.php#L3192-L3204)

### `updraftplus_msg_unfinishedbackup`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<br><span title="' . esc_attr(esc_html__('If you are seeing more backups than you expect, then it is probably because the deletion of old backup sets does not happen until a fresh backup completes.', 'updraftplus')) . '">' . esc_html__('(Not finished)', 'updraftplus') . '</span>'` |  | 
`$jobdata` |  | 
`$nonce` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 3206](class/class-mainwp-child-updraft-plus-backups.php#L3206-L3206)

### `updraftplus_dirlist_sanitize_text_field()`

*Check disk space used.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$basedir` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 3499](class/class-mainwp-child-updraft-plus-backups.php#L3499-L3521)

### `updraftplus_print_active_job_continue`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$is_oneshot` |  | 
`$next_resumption` |  | 
`$jobdata` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 3736](class/class-mainwp-child-updraft-plus-backups.php#L3736-L3736)

### `wpvivid_get_mainwp_sync_data`

*Sync other data from $data[] and merge with $information[]*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Stores the returned information.

Source: [../sources/mainwp-child/class/class-mainwp-child-wpvivid-backuprestore.php](class/class-mainwp-child-wpvivid-backuprestore.php), [line 91](class/class-mainwp-child-wpvivid-backuprestore.php#L91-L107)

### `wpvivid_handle_mainwp_action`

*Post MainWP data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$data` | `string` | Data to post.

Source: [../sources/mainwp-child/class/class-mainwp-child-wpvivid-backuprestore.php](class/class-mainwp-child-wpvivid-backuprestore.php), [line 225](class/class-mainwp-child-wpvivid-backuprestore.php#L225-L239)

### `mainwp_child_unique_id`

*Method get_site_unique_id()*

Get site unique id.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$uniqueId` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-helper.php](class/class-mainwp-helper.php), [line 744](class/class-mainwp-helper.php#L744-L757)

### `mainwp_child_actions_saved_number_of_days`

*Method to check actions data.*

Clear old the action info.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$days_number` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-actions.php](class/class-mainwp-child-actions.php), [line 251](class/class-mainwp-child-actions.php#L251-L264)

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

### `mainwp_child_contact_support_mail_headers`

*Send support email.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$headers` |  | 
`$email` |  | 
`$from` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-utility.php](class/class-mainwp-utility.php), [line 740](class/class-mainwp-utility.php#L740-L774)

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

### `is_any_staging_process_going_on`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 497](class/class-mainwp-child-timecapsule.php#L497-L530)

### `get_backup_before_update_setting_wptc`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 497](class/class-mainwp-child-timecapsule.php#L497-L548)

### `get_bbu_note_view`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 497](class/class-mainwp-child-timecapsule.php#L497-L549)

### `staging_status_wptc`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 497](class/class-mainwp-child-timecapsule.php#L497-L550)

### `is_restore_to_staging_wptc`

*Start the restore process.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 615](class/class-mainwp-child-timecapsule.php#L615-L622)

### `get_restore_to_staging_request_wptc`

*Start the restore process.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 615](class/class-mainwp-child-timecapsule.php#L615-L623)

### `check_requirements_auto_backup_wptc`

*Save the WP Time Capsule settings - backups section.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1674](class/class-mainwp-child-timecapsule.php#L1674-L1699)

### `save_settings_revision_limit_wptc`

*Save the WP Time Capsule settings - backups section.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data['revision_limit']` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1674](class/class-mainwp-child-timecapsule.php#L1674-L1702)

### `sanitize_file_name_chars`

*Filters the list of characters to remove from a filename.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$special_chars` | `string[]` | Array of characters to remove.
`$filename_raw` | `string` | The original filename to be sanitized.

**Changelog**

Version | Description
------- | -----------
`2.8.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-misc.php](class/class-mainwp-child-misc.php), [line 557](class/class-mainwp-child-misc.php#L557-L565)

### `sanitize_file_name`

*Filters a sanitized filename string.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$filename` | `string` | Sanitized filename.
`$filename_raw` | `string` | The filename prior to sanitization.

**Changelog**

Version | Description
------- | -----------
`2.8.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-misc.php](class/class-mainwp-child-misc.php), [line 572](class/class-mainwp-child-misc.php#L572-L580)

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

### `itsec_has_external_backup`

*Check if backup exists.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$has_backup` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-ithemes-security.php](class/class-mainwp-child-ithemes-security.php), [line 680](class/class-mainwp-child-ithemes-security.php#L680-L688)

### `itsec_scheduled_external_backup`

*Check if there is a shedualed backup.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sceduled_backup` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-ithemes-security.php](class/class-mainwp-child-ithemes-security.php), [line 691](class/class-mainwp-child-ithemes-security.php#L691-L699)

### `comment_email`

*Get recent comments.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$comment->comment_author_email` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-comments.php](class/class-mainwp-child-comments.php), [line 200](class/class-mainwp-child-comments.php#L200-L229)

### `illegal_user_logins`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-users.php](class/class-mainwp-child-users.php), [line 303](class/class-mainwp-child-users.php#L303-L418)

### `mainwp_child_authed_download_params`

*Method where_authed_redirect()*

Safe redirect to wanted location.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$auth_dl` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 821](class/class-mainwp-connect.php#L821-L847)

### `mainwp_child_theme_health_check_max_themes_to_batch`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-themes-check.php](class/class-mainwp-child-themes-check.php), [line 253](class/class-mainwp-child-themes-check.php#L253-L253)

### `mainwp_child_db_updater_sync_data`

*Get sync data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-db-updater.php](class/class-mainwp-child-db-updater.php), [line 100](class/class-mainwp-child-db-updater.php#L100-L104)

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

### `mainwp_child_plugin_health_check_max_plugins_to_batch`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`10` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-plugins-check.php](class/class-mainwp-child-plugins-check.php), [line 286](class/class-mainwp-child-plugins-check.php#L286-L286)

### `mainwp_create_post_custom_author`

*Update post data.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$new_post_id` | `string` | New post ID.

Source: [../sources/mainwp-child/class/class-mainwp-child-posts.php](class/class-mainwp-child-posts.php), [line 968](class/class-mainwp-child-posts.php#L968-L1012)

### `mainwp_child_branding_init_options`

*Filter 'mainwp_child_branding_init_options'*

Set custom branding setting through the filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$opts` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-branding.php](class/class-mainwp-child-branding.php), [line 106](class/class-mainwp-child-branding.php#L106-L113)

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

### `mainwp_child_extra_execution`

*Filter 'mainwp_child_extra_execution'*

Additional functions to execute through the filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | An array containing the synchronization information.
`$post` | `mixed` | Contains the POST request.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-child/class/class-mainwp-child-callable.php](class/class-mainwp-child-callable.php), [line 745](class/class-mainwp-child-callable.php#L745-L755)

### `gpi_check_status`

*Method save_settings()*

Save the plugin settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-pagespeed.php](class/class-mainwp-child-pagespeed.php), [line 252](class/class-mainwp-child-pagespeed.php#L252-L265)

### `gpi_check_status`

*Method do_check_pages()*

Check or force re-check pages page speed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-pagespeed.php](class/class-mainwp-child-pagespeed.php), [line 429](class/class-mainwp-child-pagespeed.php#L429-L441)

### `gpi_check_status`

*Method get_sync_data()*

Get the Google Pagespeed Insights plugin data and store it in the sync request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-pagespeed.php](class/class-mainwp-child-pagespeed.php), [line 452](class/class-mainwp-child-pagespeed.php#L452-L471)

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


<p align="center"><a href="https://github.com/pronamic/wp-documentor"><img src="https://cdn.jsdelivr.net/gh/pronamic/wp-documentor@main/logos/pronamic-wp-documentor.svgo-min.svg" alt="Pronamic WordPress Documentor" width="32" height="32"></a><br><em>Generated by <a href="https://github.com/pronamic/wp-documentor">Pronamic WordPress Documentor</a> <code>1.2.0</code></em><p>


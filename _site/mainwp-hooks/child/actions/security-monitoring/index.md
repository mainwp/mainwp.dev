# Security & Monitoring Actions

Hooks related to security checks, uptime monitoring, and site health.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`admin_enqueue_scripts`](#admin_enqueue_scripts) - Method is_asset_in_admin()
- [`updraftplus_checkzip_{$type}`](#updraftplus_checkzip_type) - Restore all downloaded backups from history.
- [`updraftplus_checkzip_end_{$type}`](#updraftplus_checkzip_end_type) - Restore all downloaded backups from history.
- [`check_passwords`](#check_passwords) - Edit existing user.
- [`mainwp_reports_sucuri_scan`](#mainwp_reports_sucuri_scan) - Save sucuri stream.
- [`mainwp_reports_wordfence_scan`](#mainwp_reports_wordfence_scan) - Method do_reports_log()
- [`phpmailer_init`](#phpmailer_init) - Check destination email.
- [`updraftplus_dbscan_urlchange`](#updraftplus_dbscan_urlchange) - Analyse old database file.
- [`updraftplus_dbscan_urlchange`](#updraftplus_dbscan_urlchange) - Analyse old database file.
- [`updraftplus_dbscan_urlchange_www_append_warning`](#updraftplus_dbscan_urlchange_www_append_warning) - *Arguments*
- [`updraftplus_dbscan_urlchange`](#updraftplus_dbscan_urlchange) - Analyse database file.
- [`updraftplus_dbscan_urlchange`](#updraftplus_dbscan_urlchange) - Analyse database file.
- [`mainwp_child_actions_saved_number_of_days`](#mainwp_child_actions_saved_number_of_days) - Method to check actions data.
- [`gpi_check_status`](#gpi_check_status) - Method save_settings()
- [`gpi_check_status`](#gpi_check_status) - Method do_check_pages()
- [`gpi_check_status`](#gpi_check_status) - Method get_sync_data()

## Hook Details

### `admin_enqueue_scripts`

*Method is_asset_in_admin()*

Check if the CSS/JS file is loaded in admin or not.


Source: [class/class-mainwp-child-html-regression.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-html-regression.php), [line 224](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-html-regression.php#L224)



### `updraftplus_checkzip_{$type}`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($updraft_dir . '/' . $file, &$mess, &$warn, &$err)` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)



### `updraftplus_checkzip_end_{$type}`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$mess, &$warn, &$err)` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)



### `check_passwords`

*Edit existing user.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($user->user_login, &$pass1, &$pass2)` |  | 

Source: [class/class-mainwp-child-users.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-users.php#L303)



### `mainwp_reports_sucuri_scan`

*Save sucuri stream.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$result` |  | 
`$scan_status` |  | 
`$scan_data` |  | 
`$scan_time` |  | 

Source: [class/class-mainwp-client-report.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php), [line 179](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php#L179)



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

Source: [class/class-mainwp-child-wordfence.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wordfence.php), [line 309](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wordfence.php#L309)



### `phpmailer_init`

*Check destination email.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(&$phpmailer)` |  | 

Source: [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 1311](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L1311)



### `updraftplus_dbscan_urlchange`

*Analyse old database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('Warning: %s', 'updraftplus'), '<a href="http://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>')` |  | 
`$old_siteurl` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2216](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2216)



### `updraftplus_dbscan_urlchange`

*Analyse old database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('Warning: %s', 'updraftplus'), '<a href="http://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>')` |  | 
`$old_home` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2216](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2216)



### `updraftplus_dbscan_urlchange_www_append_warning`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2639](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2639)



### `updraftplus_dbscan_urlchange`

*Analyse database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>'` |  | 
`$old_siteurl` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2472](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2472)



### `updraftplus_dbscan_urlchange`

*Analyse database file.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('This backup set is from a different site - this is not a restoration, but a migration. You need the Migrator add-on in order to make this work.', 'updraftplus') . '</a>'` |  | 
`$old_home` |  | 
`$res` | `string` | UpdraftPlus response.

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2472](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2472)



### `mainwp_child_actions_saved_number_of_days`

*Method to check actions data.*

Clear old the action info.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$days_number` |  | 

Source: [class/class-mainwp-child-actions.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-actions.php), [line 251](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-actions.php#L251)



### `gpi_check_status`

*Method save_settings()*

Save the plugin settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 252](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L252)



### `gpi_check_status`

*Method do_check_pages()*

Check or force re-check pages page speed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 429](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L429)



### `gpi_check_status`

*Method get_sync_data()*

Get the Google Pagespeed Insights plugin data and store it in the sync request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [class/class-mainwp-child-pagespeed.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php), [line 452](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-pagespeed.php#L452)




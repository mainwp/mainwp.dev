# Backups & Restoration Actions

Hooks for backup creation, management, and restoration processes.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`{$event}`](#event) - Backup now.
- [`mainwp_reports_wptimecapsule_backup`](#mainwp_reports_wptimecapsule_backup) - Add WP Time Capsule data to the reports database table.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Backupbuddy Client Reports log.
- [`mainwp_reports_backupbuddy_backup`](#mainwp_reports_backupbuddy_backup) - Create BackupBuddy Client Reports log.
- [`mainwp_reports_backupbuddy_backup`](#mainwp_reports_backupbuddy_backup) - Create BackupBuddy Client Reports log.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Add support for the reporting system.
- [`mainwp_reports_backupwordpress_backup`](#mainwp_reports_backupwordpress_backup) - Add BackUpWordPress data to the reports database table.
- [`mainwp_backup`](#mainwp_backup) - Save backup stream.
- [`mainwp_reports_backwpup_backup`](#mainwp_reports_backwpup_backup) - Create BackWPup MainWP Client Reports log.
- [`updraft_backupnow_options`](#updraft_backupnow_options) - *Arguments*
- [`updraftplus_accept_archivename`](#updraftplus_accept_archivename) - Restore all downloaded backups from history.
- [`updraftplus_importforeign_backupable_plus_db`](#updraftplus_importforeign_backupable_plus_db) - Restore all downloaded backups from history.
- [`updraftplus_https_to_http_additional_warning`](#updraftplus_https_to_http_additional_warning) - *Arguments*
- [`updraftplus_http_to_https_additional_warning`](#updraftplus_http_to_https_additional_warning) - *Arguments*
- [`updraftplus_migrator_addon_link`](#updraftplus_migrator_addon_link) - *Arguments*
- [`updraftplus_com_link`](#updraftplus_com_link) - *Arguments*
- [`updraftplus_accept_archivename`](#updraftplus_accept_archivename) - Build existing backups table.
- [`updraftplus_showbackup_date`](#updraftplus_showbackup_date) - Date label.
- [`updraftplus_msg_unfinishedbackup`](#updraftplus_msg_unfinishedbackup) - *Arguments*
- [`updraftplus_dirlist_sanitize_text_field()`](#updraftplus_dirlist_sanitize_text_field()) - Check disk space used.
- [`updraftplus_print_active_job_continue`](#updraftplus_print_active_job_continue) - *Arguments*
- [`wpvivid_get_mainwp_sync_data`](#wpvivid_get_mainwp_sync_data) - Sync other data from $data[] and merge with $information[]
- [`is_any_staging_process_going_on`](#is_any_staging_process_going_on) - Get backup process progress.
- [`get_bbu_note_view`](#get_bbu_note_view) - Get backup process progress.
- [`staging_status_wptc`](#staging_status_wptc) - Get backup process progress.
- [`is_restore_to_staging_wptc`](#is_restore_to_staging_wptc) - Start the restore process.
- [`get_restore_to_staging_request_wptc`](#get_restore_to_staging_request_wptc) - Start the restore process.
- [`check_requirements_auto_backup_wptc`](#check_requirements_auto_backup_wptc) - Save the WP Time Capsule settings - backups section.
- [`itsec_has_external_backup`](#itsec_has_external_backup) - Check if backup exists.
- [`itsec_scheduled_external_backup`](#itsec_scheduled_external_backup) - Check if there is a shedualed backup.

## Hook Details

### `{$event}`

*Backup now.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`apply_filters($options, array())` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1101](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1101)



### `mainwp_reports_wptimecapsule_backup`

*Add WP Time Capsule data to the reports database table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1014](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1014)



### `mainwp_child_reports_log`

*Backupbuddy Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backupbuddy'` |  | 

Source: [class/class-mainwp-child-back-up-buddy.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php), [line 163](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php#L163)



### `mainwp_reports_backupbuddy_backup`

*Create BackupBuddy Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backupType` |  | 
`$finish_time` |  | 

Source: [class/class-mainwp-child-back-up-buddy.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php), [line 176](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php#L176)



### `mainwp_reports_backupbuddy_backup`

*Create BackupBuddy Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backupType` |  | 
`$finish_time` |  | 

Source: [class/class-mainwp-child-back-up-buddy.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php), [line 176](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php#L176)



### `mainwp_child_reports_log`

*Add support for the reporting system.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backupwordpress'` |  | 

Source: [class/class-mainwp-child-back-up-wordpress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php#L303)



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

Source: [class/class-mainwp-child-back-up-wordpress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php), [line 319](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php#L319)



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

Source: [class/class-mainwp-client-report.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php), [line 195](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php#L195)



### `mainwp_reports_backwpup_backup`

*Create BackWPup MainWP Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  | 

Source: [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 320](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L320)



### `updraft_backupnow_options`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$options` |  | 
`array()` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1136](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1136)



### `updraftplus_accept_archivename`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)



### `updraftplus_importforeign_backupable_plus_db`

*Restore all downloaded backups from history.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($backupable_plus_db, array($foreign_known[$backups[$timestamp]['meta_foreign']], &$mess, &$warn, &$err))` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)



### `updraftplus_https_to_http_additional_warning`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('This restoration will work if you still have an SSL certificate (i.e. can use https) to access the site. Otherwise, you will want to use %s to search/replace the site address so that the site can be visited without https.', 'updraftplus'), '<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>')` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2634](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2634)



### `updraftplus_http_to_https_additional_warning`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`sprintf(esc_html__('As long as your web hosting allows http (i.e. non-SSL access) or will forward requests to https (which is almost always the case), this is no problem. If that is not yet set up, then you should set it up, or use %s so that the non-https links are automatically replaced.', 'updraftplus'), apply_filters('<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'))` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2636](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2636)



### `updraftplus_migrator_addon_link`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<a href="https://updraftplus.com/shop/migrator/">' . esc_html__('the migrator add-on', 'updraftplus') . '</a>'` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2636](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2636)



### `updraftplus_com_link`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'https://updraftplus.com/faqs/tell-me-more-about-the-search-and-replace-site-location-in-the-database-option/'` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2648](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2648)



### `updraftplus_accept_archivename`

*Build existing backups table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3006](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3006)



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

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3192](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3192)



### `updraftplus_msg_unfinishedbackup`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<br><span title="' . esc_attr(esc_html__('If you are seeing more backups than you expect, then it is probably because the deletion of old backup sets does not happen until a fresh backup completes.', 'updraftplus')) . '">' . esc_html__('(Not finished)', 'updraftplus') . '</span>'` |  | 
`$jobdata` |  | 
`$nonce` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3206](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3206)



### `updraftplus_dirlist_sanitize_text_field()`

*Check disk space used.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$basedir` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3499](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3499)



### `updraftplus_print_active_job_continue`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$is_oneshot` |  | 
`$next_resumption` |  | 
`$jobdata` |  | 

Source: [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3736](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3736)



### `wpvivid_get_mainwp_sync_data`

*Sync other data from $data[] and merge with $information[]*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` | `array` | Stores the returned information.

Source: [class/class-mainwp-child-wpvivid-backuprestore.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php), [line 91](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wpvivid-backuprestore.php#L91)



### `is_any_staging_process_going_on`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 497](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L497)



### `get_bbu_note_view`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 497](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L497)



### `staging_status_wptc`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 497](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L497)



### `is_restore_to_staging_wptc`

*Start the restore process.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 615](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L615)



### `get_restore_to_staging_request_wptc`

*Start the restore process.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 615](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L615)



### `check_requirements_auto_backup_wptc`

*Save the WP Time Capsule settings - backups section.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1674](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1674)



### `itsec_has_external_backup`

*Check if backup exists.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$has_backup` |  | 

Source: [class/class-mainwp-child-ithemes-security.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php), [line 680](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php#L680)



### `itsec_scheduled_external_backup`

*Check if there is a shedualed backup.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sceduled_backup` |  | 

Source: [class/class-mainwp-child-ithemes-security.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php), [line 691](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php#L691)




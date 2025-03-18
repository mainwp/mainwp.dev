# Backups & Restoration Filters

Hooks for backup creation, management, and restoration processes.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_reports_backwpup_backup`](#mainwp_reports_backwpup_backup) - Create BackWPup MainWP Client Reports log.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Add support for the reporting system.
- [`mainwp_reports_backupwordpress_backup`](#mainwp_reports_backupwordpress_backup) - Add BackUpWordPress data to the reports database table.
- [`mainwp_reports_wptimecapsule_backup`](#mainwp_reports_wptimecapsule_backup) - Add WP Time Capsule data to the reports database table.
- [`mainwp_child_reports_log`](#mainwp_child_reports_log) - Backupbuddy Client Reports log.
- [`mainwp_reports_backupbuddy_backup`](#mainwp_reports_backupbuddy_backup) - Create BackupBuddy Client Reports log.
- [`mainwp_reports_backupbuddy_backup`](#mainwp_reports_backupbuddy_backup) - Create BackupBuddy Client Reports log.
- [`mainwp_backup`](#mainwp_backup) - Save backup stream.
- [`{$event}`](#event) - Backup now.
- [`itsec_has_external_backup`](#itsec_has_external_backup) - Check if backup exists.
- [`itsec_scheduled_external_backup`](#itsec_scheduled_external_backup) - Check if there is a shedualed backup.
- [`is_any_staging_process_going_on`](#is_any_staging_process_going_on) - Get backup process progress.
- [`get_bbu_note_view`](#get_bbu_note_view) - Get backup process progress.
- [`staging_status_wptc`](#staging_status_wptc) - Get backup process progress.
- [`is_restore_to_staging_wptc`](#is_restore_to_staging_wptc) - Start the restore process.
- [`get_restore_to_staging_request_wptc`](#get_restore_to_staging_request_wptc) - Start the restore process.
- [`check_requirements_auto_backup_wptc`](#check_requirements_auto_backup_wptc) - Save the WP Time Capsule settings - backups section.
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

## Hook Details

### `mainwp_reports_backwpup_backup`

*Create BackWPup MainWP Client Reports log.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-back-wp-up.php](class/class-mainwp-child-back-wp-up.php), [line 320](class/class-mainwp-child-back-wp-up.php#L320-L409)



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



### `mainwp_reports_wptimecapsule_backup`

*Add WP Time Capsule data to the reports database table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 1014](class/class-mainwp-child-timecapsule.php#L1014-L1068)



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



### `{$event}`

*Backup now.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`apply_filters($options, array())` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 1101](class/class-mainwp-child-updraft-plus-backups.php#L1101-L1136)



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



### `is_any_staging_process_going_on`

*Get backup process progress.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-timecapsule.php](class/class-mainwp-child-timecapsule.php), [line 497](class/class-mainwp-child-timecapsule.php#L497-L530)



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



### `updraftplus_com_link`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'https://updraftplus.com/faqs/tell-me-more-about-the-search-and-replace-site-location-in-the-database-option/'` |  | 

Source: [../sources/mainwp-child/class/class-mainwp-child-updraft-plus-backups.php](class/class-mainwp-child-updraft-plus-backups.php), [line 2648](class/class-mainwp-child-updraft-plus-backups.php#L2648-L2648)



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




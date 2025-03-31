# Backups & Restoration Filters

Hooks for backup creation, management, and restoration processes.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`check_requirements_auto_backup_wptc`](#check-requirements-auto-backup-wptc) - Save the WP Time Capsule settings - backups section.
- [`get_bbu_note_view`](#get-bbu-note-view) - Get backup process progress.
- [`get_restore_to_staging_request_wptc`](#get-restore-to-staging-request-wptc) - Start the restore process.
- [`is_any_staging_process_going_on`](#is-any-staging-process-going-on) - Get backup process progress.
- [`is_restore_to_staging_wptc`](#is-restore-to-staging-wptc) - Start the restore process.
- [`itsec_has_external_backup`](#itsec-has-external-backup) - Check if backup exists.
- [`itsec_scheduled_external_backup`](#itsec-scheduled-external-backup) - Check if there is a shedualed backup.
- [`mainwp_backup`](#mainwp-backup) - Save backup stream.
- [`mainwp_child_reports_log`](#mainwp-child-reports-log) - Add support for the reporting system.
- [`mainwp_reports_backupbuddy_backup`](#mainwp-reports-backupbuddy-backup) - Create BackupBuddy Client Reports log.
- [`mainwp_reports_backupwordpress_backup`](#mainwp-reports-backupwordpress-backup) - Add BackUpWordPress data to the reports database table.
- [`mainwp_reports_backwpup_backup`](#mainwp-reports-backwpup-backup) - Create BackWPup MainWP Client Reports log.
- [`mainwp_reports_wptimecapsule_backup`](#mainwp-reports-wptimecapsule-backup) - Add WP Time Capsule data to the reports database table.
- [`staging_status_wptc`](#staging-status-wptc) - Get backup process progress.
- [`updraft_backupnow_options`](#updraft-backupnow-options) - *Arguments*
- [`updraftplus_accept_archivename`](#updraftplus-accept-archivename) - Restore all downloaded backups from history.
- [`updraftplus_importforeign_backupable_plus_db`](#updraftplus-importforeign-backupable-plus-db) - Restore all downloaded backups from history.
- [`updraftplus_msg_unfinishedbackup`](#updraftplus-msg-unfinishedbackup) - *Arguments*
- [`updraftplus_showbackup_date`](#updraftplus-showbackup-date) - Date label.
- [`{$event}`](#event) - Backup now.

---

## Hook Details

<a id='check-requirements-auto-backup-wptc'></a>
### `check_requirements_auto_backup_wptc`

* Save the WP Time Capsule settings - backups section.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1674](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1674)

---

<a id='get-bbu-note-view'></a>
### `get_bbu_note_view`

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

<a id='get-restore-to-staging-request-wptc'></a>
### `get_restore_to_staging_request_wptc`

* Start the restore process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 615](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L615)

---

<a id='is-any-staging-process-going-on'></a>
### `is_any_staging_process_going_on`

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

<a id='is-restore-to-staging-wptc'></a>
### `is_restore_to_staging_wptc`

* Start the restore process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 615](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L615)

---

<a id='itsec-has-external-backup'></a>
### `itsec_has_external_backup`

* Check if backup exists.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$has_backup` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$has_backup` |  |

**Usage Locations:**

- [class/class-mainwp-child-ithemes-security.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php), [line 680](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php#L680)

---

<a id='itsec-scheduled-external-backup'></a>
### `itsec_scheduled_external_backup`

* Check if there is a shedualed backup.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sceduled_backup` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sceduled_backup` |  |

**Usage Locations:**

- [class/class-mainwp-child-ithemes-security.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php), [line 691](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-ithemes-security.php#L691)

---

<a id='mainwp-backup'></a>
### `mainwp_backup`

* Save backup stream.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$destination` |  | 
`$message` |  | 
`$size` |  | 
`$status` |  | 
`$type` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$destination` |  | 
`$message` |  | 
`$size` |  | 
`$status` |  | 
`$type` |  |

**Usage Locations:**

- [class/class-mainwp-client-report.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php), [line 195](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-client-report.php#L195)

---

<a id='mainwp-child-reports-log'></a>
### `mainwp_child_reports_log`

* Add support for the reporting system.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backupwordpress'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'backupwordpress'` |  |

**Usage Locations:**

- [class/class-mainwp-child-back-up-buddy.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php), [line 163](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php#L163)
- [class/class-mainwp-child-back-up-wordpress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php), [line 303](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php#L303)

---

<a id='mainwp-reports-backupbuddy-backup'></a>
### `mainwp_reports_backupbuddy_backup`

* Create BackupBuddy Client Reports log.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backupType` |  | 
`$finish_time` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backupType` |  | 
`$finish_time` |  |

**Usage Locations:**

- [class/class-mainwp-child-back-up-buddy.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php), [line 176](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-buddy.php#L176)

---

<a id='mainwp-reports-backupwordpress-backup'></a>
### `mainwp_reports_backupwordpress_backup`

* Add BackUpWordPress data to the reports database table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$destination` |  | 
`$message` |  | 
`'finished'` |  | 
`$backup_type` |  | 
`$date` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$destination` |  | 
`$message` |  | 
`'finished'` |  | 
`$backup_type` |  | 
`$date` |  |

**Usage Locations:**

- [class/class-mainwp-child-back-up-wordpress.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php), [line 319](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-up-wordpress.php#L319)

---

<a id='mainwp-reports-backwpup-backup'></a>
### `mainwp_reports_backwpup_backup`

* Create BackWPup MainWP Client Reports log.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  |

**Usage Locations:**

- [class/class-mainwp-child-back-wp-up.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php), [line 320](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-back-wp-up.php#L320)

---

<a id='mainwp-reports-wptimecapsule-backup'></a>
### `mainwp_reports_wptimecapsule_backup`

* Add WP Time Capsule data to the reports database table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$message` |  | 
`$backup_type` |  | 
`$backup_time` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1014](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1014)

---

<a id='staging-status-wptc'></a>
### `staging_status_wptc`

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

<a id='updraft-backupnow-options'></a>
### `updraft_backupnow_options`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`$options` |  | 
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$options` |  | 
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1136](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1136)

---

<a id='updraftplus-accept-archivename'></a>
### `updraftplus_accept_archivename`

* Restore all downloaded backups from history.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)
- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3006](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3006)

---

<a id='updraftplus-importforeign-backupable-plus-db'></a>
### `updraftplus_importforeign_backupable_plus_db`

* Restore all downloaded backups from history.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($backupable_plus_db, array($foreign_known[$backups[$timestamp]['meta_foreign']], &$mess, &$warn, &$err))` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($backupable_plus_db, array($foreign_known[$backups[$timestamp]['meta_foreign']], &$mess, &$warn, &$err))` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1898](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1898)

---

<a id='updraftplus-msg-unfinishedbackup'></a>
### `updraftplus_msg_unfinishedbackup`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`'<br><span title="' . esc_attr(esc_html__('If you are seeing more backups than you expect, then it is probably because the deletion of old backup sets does not happen until a fresh backup completes.', 'updraftplus')) . '">' . esc_html__('(Not finished)', 'updraftplus') . '</span>'` |  | 
`$jobdata` |  | 
`$nonce` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'<br><span title="' . esc_attr(esc_html__('If you are seeing more backups than you expect, then it is probably because the deletion of old backup sets does not happen until a fresh backup completes.', 'updraftplus')) . '">' . esc_html__('(Not finished)', 'updraftplus') . '</span>'` |  | 
`$jobdata` |  | 
`$nonce` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3206](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3206)

---

<a id='updraftplus-showbackup-date'></a>
### `updraftplus_showbackup_date`

* Date label.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pretty_date` | `string` | Pretty date.
`$backup` | `string` | Type of backup.
`$jobdata` | `array` | Job data.
`(int) $key` |  | 
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pretty_date` | `string` | Pretty date.
`$backup` | `string` | Type of backup.
`$jobdata` | `array` | Job data.
`(int) $key` |  | 
`false` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 3192](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L3192)

---

<a id='event'></a>
### `{$event}`

* Backup now.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`apply_filters($options, array())` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`apply_filters($options, array())` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 1101](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L1101)

---


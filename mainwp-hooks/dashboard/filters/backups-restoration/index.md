# Backups & Restoration Filters

Hooks for backup creation, management, and restoration processes.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-getprimarybackup-activated`](#mainwp-getprimarybackup-activated) - Method admin_init()
- [`mainwp-getprimarybackup-methods`](#mainwp-getprimarybackup-methods) - Method get_columns()
- [`mainwp_add_backuptask`](#mainwp-add-backuptask) - Add backup task.
- [`mainwp_ajax_add_action`](#mainwp-ajax-add-action) - Init ajax actions.
- [`mainwp_backups_remote_settings`](#mainwp-backups-remote-settings) - Render Backup Options.
- [`mainwp_backuptask_column_destination`](#mainwp-backuptask-column-destination) - Column Destination.
- [`mainwp_backuptask_remotedestinations`](#mainwp-backuptask-remotedestinations) - Get backup tasks and site ID.
- [`mainwp_getprimarybackup_activated`](#mainwp-getprimarybackup-activated) - Method admin_init()
- [`mainwp_getprimarybackup_methods`](#mainwp-getprimarybackup-methods) - This filter is documented in ../pages/page-mainwp-server-information-handler.php

---

## Hook Details

<a id='mainwp-getprimarybackup-activated'></a>
### `mainwp-getprimarybackup-activated`

* Method admin_init()

Do nothing if current user is not an Admin else display the page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($return)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getprimarybackup_activated'` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 766](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L766)

---

<a id='mainwp-getprimarybackup-methods'></a>
### `mainwp-getprimarybackup-methods`

* Method get_columns()

Combine all columns.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($primary_methods)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getprimarybackup_methods'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-backup-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-backup-view.php), [line 63](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-backup-view.php#L63)
- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 311](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L311)
- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 1190](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L1190)
- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 320](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L320)
- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 966](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L966)
- [pages/page-mainwp-server-information-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php), [line 852](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php#L852)

---

<a id='mainwp-add-backuptask'></a>
### `mainwp_add_backuptask`

* Add backup task.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$task->id` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$task->id` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php), [line 211](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php#L211)

---

<a id='mainwp-ajax-add-action'></a>
### `mainwp_ajax_add_action`

* Init ajax actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'cloudways_action_backup'` |  | 
`array(&$this, 'ajax_cloudways_action_backup')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'cloudways_action_backup'` |  | 
`array(&$this, 'ajax_cloudways_action_backup')` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-3rd-party.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php), [line 100](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php#L100)

---

<a id='mainwp-backups-remote-settings'></a>
### `mainwp_backups_remote_settings`

* Render Backup Options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('website' => $website->id)` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('website' => $website->id)` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-backup-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-backup-view.php), [line 135](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-backup-view.php#L135)

---

<a id='mainwp-backuptask-column-destination'></a>
### `mainwp_backuptask_column_destination`

* Column Destination.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$item->id` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$item->id` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 603](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L603)

---

<a id='mainwp-backuptask-remotedestinations'></a>
### `mainwp_backuptask_remotedestinations`

* Get backup tasks and site ID.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$backupTask` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$backupTask` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php), [line 514](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php#L514)

---

<a id='mainwp-getprimarybackup-activated'></a>
### `mainwp_getprimarybackup_activated`

* Method admin_init()

Do nothing if current user is not an Admin else display the page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$return` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 766](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L766)

---

<a id='mainwp-getprimarybackup-methods'></a>
### `mainwp_getprimarybackup_methods`

* This filter is documented in ../pages/page-mainwp-server-information-handler.php

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$primary_methods` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$primary_methods` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-backup-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-backup-view.php), [line 63](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-backup-view.php#L63)
- [class/class-mainwp-manage-sites-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php), [line 348](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-list-table.php#L348)
- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 1190](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L1190)
- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 320](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L320)
- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 966](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L966)
- [pages/page-mainwp-server-information-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php), [line 852](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php#L852)

---


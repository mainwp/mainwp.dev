# System & Settings Filters

Hooks related to general settings and system configuration.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Child Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_child_branding_init_options`](#mainwp-child-branding-init-options) - Filter 'mainwp_child_branding_init_options'
- [`mainwp_child_reports_log`](#mainwp-child-reports-log) - Add support for the reporting system.
- [`save_settings_revision_limit_wptc`](#save-settings-revision-limit-wptc) - Save the WP Time Capsule settings - backups section.
- [`updraftplus_com_link`](#updraftplus-com-link) - *Arguments*

---

## Hook Details

<a id='mainwp-child-branding-init-options'></a>
### `mainwp_child_branding_init_options`

* Filter 'mainwp_child_branding_init_options'

Set custom branding setting through the filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$opts` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-child-branding.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding.php), [line 106](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-branding.php#L106)

---

<a id='mainwp-child-reports-log'></a>
### `mainwp_child_reports_log`

* Add support for the reporting system.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wptimecapsule'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'wptimecapsule'` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 998](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L998)
- [class/class-mainwp-child-wordfence.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wordfence.php), [line 300](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-wordfence.php#L300)

---

<a id='save-settings-revision-limit-wptc'></a>
### `save_settings_revision_limit_wptc`

* Save the WP Time Capsule settings - backups section.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data['revision_limit']` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data['revision_limit']` |  |

**Usage Locations:**

- [class/class-mainwp-child-timecapsule.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php), [line 1674](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-timecapsule.php#L1674)

---

<a id='updraftplus-com-link'></a>
### `updraftplus_com_link`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`'https://updraftplus.com/faqs/tell-me-more-about-the-search-and-replace-site-location-in-the-database-option/'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'https://updraftplus.com/faqs/tell-me-more-about-the-search-and-replace-site-location-in-the-database-option/'` |  |

**Usage Locations:**

- [class/class-mainwp-child-updraft-plus-backups.php](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php), [line 2648](https://github.com/mainwp/mainwp-child/blob/master/class/class-mainwp-child-updraft-plus-backups.php#L2648)

---


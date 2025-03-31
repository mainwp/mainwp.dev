# Client Reports Actions

Hooks for report generation, customization, and delivery.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_after_select_clients_list`](#mainwp-after-select-clients-list) - Action: mainwp_after_select_clients_list
- [`mainwp_before_select_clients_list`](#mainwp-before-select-clients-list) - Action: mainwp_before_select_clients_list
- [`mainwp_client_deleted`](#mainwp-client-deleted) - Delete client
- [`mainwp_client_suspend`](#mainwp-client-suspend) - Fires immediately after update client suspend/unsuspend.
- [`mainwp_clients_getmetaboxes`](#mainwp-clients-getmetaboxes) - Method add_meta_boxes()
- [`mainwp_clients_info_table_bottom`](#mainwp-clients-info-table-bottom) - Action: mainwp_clients_info_table_bottom
- [`mainwp_clients_info_table_top`](#mainwp-clients-info-table-top) - Action: mainwp_clients_info_table_top
- [`mainwp_clients_info_widget_bottom`](#mainwp-clients-info-widget-bottom) - Action: mainwp_clients_info_widget_bottom
- [`mainwp_clients_info_widget_title`](#mainwp-clients-info-widget-title) - *Arguments*
- [`mainwp_clients_info_widget_top`](#mainwp-clients-info-widget-top) - Actoin: mainwp_clients_info_widget_top
- [`mainwp_clients_overview_contact_widget_bottom`](#mainwp-clients-overview-contact-widget-bottom) - Action: mainwp_clients_overview_contact_widget_bottom
- [`mainwp_clients_overview_contact_widget_sutbitle`](#mainwp-clients-overview-contact-widget-sutbitle) - *Arguments*
- [`mainwp_clients_overview_contact_widget_title`](#mainwp-clients-overview-contact-widget-title) - *Arguments*
- [`mainwp_clients_overview_contact_widget_top`](#mainwp-clients-overview-contact-widget-top) - Actoin: mainwp_clients_overview_contact_widget_top
- [`mainwp_clients_overview_enabled_widgets`](#mainwp-clients-overview-enabled-widgets) - Unset unwanted Widgets
- [`mainwp_clients_overview_help_item`](#mainwp-clients-overview-help-item) - Action: mainwp_clients_overview_help_item
- [`mainwp_clients_overview_info_table_bottom`](#mainwp-clients-overview-info-table-bottom) - Action: mainwp_clients_overview_info_table_bottom
- [`mainwp_clients_overview_info_table_top`](#mainwp-clients-overview-info-table-top) - Action: mainwp_clients_overview_info_table_top
- [`mainwp_clients_overview_info_widget_bottom`](#mainwp-clients-overview-info-widget-bottom) - Action: mainwp_clients_overview_info_widget_bottom
- [`mainwp_clients_overview_info_widget_title`](#mainwp-clients-overview-info-widget-title) - *Arguments*
- [`mainwp_clients_overview_info_widget_top`](#mainwp-clients-overview-info-widget-top) - Actoin: mainwp_clients_overview_info_widget_top
- [`mainwp_clients_overview_note_widget_bottom`](#mainwp-clients-overview-note-widget-bottom) - Action: mainwp_clients_overview_note_widget_bottom
- [`mainwp_clients_overview_note_widget_title`](#mainwp-clients-overview-note-widget-title) - *Arguments*
- [`mainwp_clients_overview_note_widget_top`](#mainwp-clients-overview-note-widget-top) - Actoin: mainwp_clients_overview_note_widget_top
- [`mainwp_clients_overview_overview_widget_bottom`](#mainwp-clients-overview-overview-widget-bottom) - Action: mainwp_clients_overview_overview_widget_bottom
- [`mainwp_clients_overview_overview_widget_top`](#mainwp-clients-overview-overview-widget-top) - Actoin: mainwp_clients_overview_overview_widget_top
- [`mainwp_clients_overview_screen_options_bottom`](#mainwp-clients-overview-screen-options-bottom) - Action: mainwp_clients_overview_screen_options_bottom
- [`mainwp_clients_overview_screen_options_top`](#mainwp-clients-overview-screen-options-top) - Action: mainwp_clients_overview_screen_options_top
- [`mainwp_clients_sitestable_getcolumns`](#mainwp-clients-sitestable-getcolumns) - Filter: mainwp_clients_sitestable_getcolumns
- [`mainwp_clients_sitestable_item`](#mainwp-clients-sitestable-item) - Filter: mainwp_clients_sitestable_item
- [`mainwp_clients_table_features`](#mainwp-clients-table-features) - Filter: mainwp_clients_table_features
- [`mainwp_clients_widget_bottom`](#mainwp-clients-widget-bottom) - Action: mainwp_clients_widget_bottom
- [`mainwp_clients_widget_title`](#mainwp-clients-widget-title) - *Arguments*
- [`mainwp_clients_widget_top`](#mainwp-clients-widget-top) - Actoin: mainwp_clients_widget_top
- [`mainwp_clients_widgets_screen_options`](#mainwp-clients-widgets-screen-options) - Filter: mainwp_clients_widgets_screen_options
- [`mainwp_clientstable_prepared_items`](#mainwp-clientstable-prepared-items) - Prepair the items to be listed.
- [`mainwp_manageclients_bulk_actions`](#mainwp-manageclients-bulk-actions) - Filter: mainwp_manageclients_bulk_actions
- [`mainwp_manageclients_tabletop`](#mainwp-manageclients-tabletop) - Method render_second_top_header()
- [`mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`](#mainwp-rest-routes-clients-controller-filter-allowed-fields-by-context) - Get client by tag id.

---

## Hook Details

<a id='mainwp-after-select-clients-list'></a>
### `mainwp_after_select_clients_list`

* Action: mainwp_after_select_clients_list

Fires after the Select Clients list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing Clients info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 405](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L405)

---

<a id='mainwp-before-select-clients-list'></a>
### `mainwp_before_select_clients_list`

* Action: mainwp_before_select_clients_list

Fires before the Select Clients list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing Clients info.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 355](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L355)

---

<a id='mainwp-client-deleted'></a>
### `mainwp_client_deleted`

* Delete client

Fires after delete a client.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$current` | `object` | client deleted.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` |

**Usage Locations:**

- [class/class-mainwp-db-client.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-client.php), [line 1010](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-client.php#L1010)

---

<a id='mainwp-client-suspend'></a>
### `mainwp_client_suspend`

* Fires immediately after update client suspend/unsuspend.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` | `object` | client data.
`$suspended` | `bool` | true\|false.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` | `object` | client data.
`$suspended` | `bool` | true\|false.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` |

**Usage Locations:**

- [class/class-mainwp-post-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-handler.php), [line 1111](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-handler.php#L1111)
- [pages/page-mainwp-client.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php), [line 1353](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php#L1353)

---

<a id='mainwp-clients-getmetaboxes'></a>
### `mainwp_clients_getmetaboxes`

* Method add_meta_boxes()

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  |

**Usage Locations:**

- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 143](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L143)

---

<a id='mainwp-clients-info-table-bottom'></a>
### `mainwp_clients_info_table_bottom`

* Action: mainwp_clients_info_table_bottom

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 168](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L168)

---

<a id='mainwp-clients-info-table-top'></a>
### `mainwp_clients_info_table_top`

* Action: mainwp_clients_info_table_top

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 107](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L107)

---

<a id='mainwp-clients-info-widget-bottom'></a>
### `mainwp_clients_info_widget_bottom`

* Action: mainwp_clients_info_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 183](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L183)

---

<a id='mainwp-clients-info-widget-title'></a>
### `mainwp_clients_info_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Client Info', 'mainwp')` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Client Info', 'mainwp')` |  | 
`$website` |  |

**Usage Locations:**

- [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 78](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L78)

---

<a id='mainwp-clients-info-widget-top'></a>
### `mainwp_clients_info_widget_top`

* Actoin: mainwp_clients_info_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 84](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L84)

---

<a id='mainwp-clients-overview-contact-widget-bottom'></a>
### `mainwp_clients_overview_contact_widget_bottom`

* Action: mainwp_clients_overview_contact_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$contact_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 142](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L142)

---

<a id='mainwp-clients-overview-contact-widget-sutbitle'></a>
### `mainwp_clients_overview_contact_widget_sutbitle`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`__('Contact Information', 'mainwp')` |  | 
`$contact_info` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`__('Contact Information', 'mainwp')` |  | 
`$contact_info` |  |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 76](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L76)

---

<a id='mainwp-clients-overview-contact-widget-title'></a>
### `mainwp_clients_overview_contact_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`__('Client Contact', 'mainwp')` |  | 
`$contact_info` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`__('Client Contact', 'mainwp')` |  | 
`$contact_info` |  |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 73](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L73)

---

<a id='mainwp-clients-overview-contact-widget-top'></a>
### `mainwp_clients_overview_contact_widget_top`

* Actoin: mainwp_clients_overview_contact_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$contact_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 82](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L82)

---

<a id='mainwp-clients-overview-enabled-widgets'></a>
### `mainwp_clients_overview_enabled_widgets`

* Unset unwanted Widgets

Contains the list of enabled widgets and allows user to unset unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$values` | `array` | Array containing enabled widgets.
`null` |  |

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Usage Locations:**

- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 191](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L191)

---

<a id='mainwp-clients-overview-help-item'></a>
### `mainwp_clients_overview_help_item`

* Action: mainwp_clients_overview_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Clients page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`4.3` |

**Usage Locations:**

- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 521](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L521)

---

<a id='mainwp-clients-overview-info-table-bottom'></a>
### `mainwp_clients_overview_info_table_bottom`

* Action: mainwp_clients_overview_info_table_bottom

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 128](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L128)

---

<a id='mainwp-clients-overview-info-table-top'></a>
### `mainwp_clients_overview_info_table_top`

* Action: mainwp_clients_overview_info_table_top

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 89](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L89)

---

<a id='mainwp-clients-overview-info-widget-bottom'></a>
### `mainwp_clients_overview_info_widget_bottom`

* Action: mainwp_clients_overview_info_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 147](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L147)

---

<a id='mainwp-clients-overview-info-widget-title'></a>
### `mainwp_clients_overview_info_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Additional Client Info', 'mainwp')` |  | 
`$client_info` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Additional Client Info', 'mainwp')` |  | 
`$client_info` |  |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 64](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L64)

---

<a id='mainwp-clients-overview-info-widget-top'></a>
### `mainwp_clients_overview_info_widget_top`

* Actoin: mainwp_clients_overview_info_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 71](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L71)

---

<a id='mainwp-clients-overview-note-widget-bottom'></a>
### `mainwp_clients_overview_note_widget_bottom`

* Action: mainwp_clients_overview_note_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-note.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php), [line 100](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php#L100)

---

<a id='mainwp-clients-overview-note-widget-title'></a>
### `mainwp_clients_overview_note_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$client_info` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$client_info` |  |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-note.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php), [line 71](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php#L71)

---

<a id='mainwp-clients-overview-note-widget-top'></a>
### `mainwp_clients_overview_note_widget_top`

* Actoin: mainwp_clients_overview_note_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-note.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php), [line 78](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php#L78)

---

<a id='mainwp-clients-overview-overview-widget-bottom'></a>
### `mainwp_clients_overview_overview_widget_bottom`

* Action: mainwp_clients_overview_overview_widget_bottom

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php), [line 159](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php#L159)

---

<a id='mainwp-clients-overview-overview-widget-top'></a>
### `mainwp_clients_overview_overview_widget_top`

* Actoin: mainwp_clients_overview_overview_widget_top

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [widgets/widget-mainwp-client-overview-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php), [line 82](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php#L82)

---

<a id='mainwp-clients-overview-screen-options-bottom'></a>
### `mainwp_clients_overview_screen_options_bottom`

* Action: mainwp_clients_overview_screen_options_bottom

Fires at the bottom of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 380](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L380)

---

<a id='mainwp-clients-overview-screen-options-top'></a>
### `mainwp_clients_overview_screen_options_top`

* Action: mainwp_clients_overview_screen_options_top

Fires at the top of the Sceen Options modal on the Overview page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 366](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L366)

---

<a id='mainwp-clients-sitestable-getcolumns'></a>
### `mainwp_clients_sitestable_getcolumns`

* Filter: mainwp_clients_sitestable_getcolumns

Filters the Clients table columns. Allows user to create a new column.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$columns` | `array` | Array containing table columns.
`$columns` | `array` | Array containing table columns.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 156](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L156)

---

<a id='mainwp-clients-sitestable-item'></a>
### `mainwp_clients_sitestable_item`

* Filter: mainwp_clients_sitestable_item

Filters the Clients table column items. Allows user to create new column item.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$item` | `array` | Array containing child site data.
`$item` | `array` | Array containing child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 60](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L60)

---

<a id='mainwp-clients-table-features'></a>
### `mainwp_clients_table_features`

* Filter: mainwp_clients_table_features

Filter the Clients table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 409](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L409)

---

<a id='mainwp-clients-widget-bottom'></a>
### `mainwp_clients_widget_bottom`

* Action: mainwp_clients_widget_bottom

Fires at the bottom of the Clients widget on the overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.4` |

**Usage Locations:**

- [widgets/widget-mainwp-clients.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php), [line 161](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php#L161)

---

<a id='mainwp-clients-widget-title'></a>
### `mainwp_clients_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Clients', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Clients', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-clients.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php), [line 55](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php#L55)

---

<a id='mainwp-clients-widget-top'></a>
### `mainwp_clients_widget_top`

* Actoin: mainwp_clients_widget_top

Fires at the top of the Clients widget on the overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing the clients info.

**Changelog**

Version | Description
------- | -----------
`4.4` |

**Usage Locations:**

- [widgets/widget-mainwp-clients.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php), [line 62](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php#L62)

---

<a id='mainwp-clients-widgets-screen-options'></a>
### `mainwp_clients_widgets_screen_options`

* Filter: mainwp_clients_widgets_screen_options

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 438](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L438)

---

<a id='mainwp-clientstable-prepared-items'></a>
### `mainwp_clientstable_prepared_items`

* Prepair the items to be listed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` |  | 
`$clients_ids` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` |  | 
`$clients_ids` |  |

**Usage Locations:**

- [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 290](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L290)

---

<a id='mainwp-manageclients-bulk-actions'></a>
### `mainwp_manageclients_bulk_actions`

* Filter: mainwp_manageclients_bulk_actions

Filters bulk actions on the Clients page. Allows user to hook in new actions or remove default ones.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$actions` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 206](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L206)

---

<a id='mainwp-manageclients-tabletop'></a>
### `mainwp_manageclients_tabletop`

* Method render_second_top_header()

Render second top header.

**Usage Locations:**

- [pages/page-mainwp-client.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php), [line 565](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php#L565)

---

<a id='mainwp-rest-routes-clients-controller-filter-allowed-fields-by-context'></a>
### `mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`

* Get client by tag id.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` |  |

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php), [line 404](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php#L404)
- [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 566](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L566)

---


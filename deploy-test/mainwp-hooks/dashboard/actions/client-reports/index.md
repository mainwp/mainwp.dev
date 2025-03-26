# Client Reports Actions

Hooks for report generation, customization, and delivery.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_clientstable_prepared_items`](#mainwp_clientstable_prepared_items) - Prepair the items to be listed.
- [`mainwp_client_deleted`](#mainwp_client_deleted) - Delete client
- [`mainwp_before_select_clients_list`](#mainwp_before_select_clients_list) - Action: mainwp_before_select_clients_list
- [`mainwp_after_select_clients_list`](#mainwp_after_select_clients_list) - Action: mainwp_after_select_clients_list
- [`mainwp_client_suspend`](#mainwp_client_suspend) - Fires immediately after update client suspend/unsuspend.
- [`mainwp_manageclients_tabletop`](#mainwp_manageclients_tabletop) - Method render_second_top_header()
- [`mainwp_client_suspend`](#mainwp_client_suspend) - Fires immediately after update client suspend/unsuspend.
- [`mainwp_clients_overview_screen_options_top`](#mainwp_clients_overview_screen_options_top) - Action: mainwp_clients_overview_screen_options_top
- [`mainwp_clients_overview_screen_options_bottom`](#mainwp_clients_overview_screen_options_bottom) - Action: mainwp_clients_overview_screen_options_bottom
- [`mainwp_clients_overview_help_item`](#mainwp_clients_overview_help_item) - Action: mainwp_clients_overview_help_item
- [`mainwp_clients_overview_note_widget_top`](#mainwp_clients_overview_note_widget_top) - Actoin: mainwp_clients_overview_note_widget_top
- [`mainwp_clients_overview_note_widget_bottom`](#mainwp_clients_overview_note_widget_bottom) - Action: mainwp_clients_overview_note_widget_bottom
- [`mainwp_clients_overview_contact_widget_top`](#mainwp_clients_overview_contact_widget_top) - Actoin: mainwp_clients_overview_contact_widget_top
- [`mainwp_clients_overview_contact_widget_bottom`](#mainwp_clients_overview_contact_widget_bottom) - Action: mainwp_clients_overview_contact_widget_bottom
- [`mainwp_clients_overview_overview_widget_top`](#mainwp_clients_overview_overview_widget_top) - Actoin: mainwp_clients_overview_overview_widget_top
- [`mainwp_clients_overview_overview_widget_bottom`](#mainwp_clients_overview_overview_widget_bottom) - Action: mainwp_clients_overview_overview_widget_bottom
- [`mainwp_clients_overview_info_widget_top`](#mainwp_clients_overview_info_widget_top) - Actoin: mainwp_clients_overview_info_widget_top
- [`mainwp_clients_overview_info_table_top`](#mainwp_clients_overview_info_table_top) - Action: mainwp_clients_overview_info_table_top
- [`mainwp_clients_overview_info_table_bottom`](#mainwp_clients_overview_info_table_bottom) - Action: mainwp_clients_overview_info_table_bottom
- [`mainwp_clients_overview_info_widget_bottom`](#mainwp_clients_overview_info_widget_bottom) - Action: mainwp_clients_overview_info_widget_bottom
- [`mainwp_clients_widget_top`](#mainwp_clients_widget_top) - Actoin: mainwp_clients_widget_top
- [`mainwp_clients_widget_bottom`](#mainwp_clients_widget_bottom) - Action: mainwp_clients_widget_bottom
- [`mainwp_clients_info_widget_top`](#mainwp_clients_info_widget_top) - Actoin: mainwp_clients_info_widget_top
- [`mainwp_clients_info_table_top`](#mainwp_clients_info_table_top) - Action: mainwp_clients_info_table_top
- [`mainwp_clients_info_table_bottom`](#mainwp_clients_info_table_bottom) - Action: mainwp_clients_info_table_bottom
- [`mainwp_clients_info_widget_bottom`](#mainwp_clients_info_widget_bottom) - Action: mainwp_clients_info_widget_bottom
- [`mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context) - Get client by tag id.
- [`mainwp_clients_sitestable_item`](#mainwp_clients_sitestable_item) - Filter: mainwp_clients_sitestable_item
- [`mainwp_clients_sitestable_getcolumns`](#mainwp_clients_sitestable_getcolumns) - Filter: mainwp_clients_sitestable_getcolumns
- [`mainwp_manageclients_bulk_actions`](#mainwp_manageclients_bulk_actions) - Filter: mainwp_manageclients_bulk_actions
- [`mainwp_clients_table_features`](#mainwp_clients_table_features) - Filter: mainwp_clients_table_features
- [`mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`](#mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context) - Get clients by item.
- [`mainwp_clients_getmetaboxes`](#mainwp_clients_getmetaboxes) - Method add_meta_boxes()
- [`mainwp_clients_overview_enabled_widgets`](#mainwp_clients_overview_enabled_widgets) - Unset unwanted Widgets
- [`mainwp_clients_widgets_screen_options`](#mainwp_clients_widgets_screen_options) - Filter: mainwp_clients_widgets_screen_options
- [`mainwp_clients_overview_note_widget_title`](#mainwp_clients_overview_note_widget_title) - *Arguments*
- [`mainwp_clients_overview_contact_widget_title`](#mainwp_clients_overview_contact_widget_title) - *Arguments*
- [`mainwp_clients_overview_contact_widget_sutbitle`](#mainwp_clients_overview_contact_widget_sutbitle) - *Arguments*
- [`mainwp_clients_overview_info_widget_title`](#mainwp_clients_overview_info_widget_title) - *Arguments*
- [`mainwp_clients_widget_title`](#mainwp_clients_widget_title) - *Arguments*
- [`mainwp_clients_info_widget_title`](#mainwp_clients_info_widget_title) - *Arguments*

## Hook Details

### `mainwp_clientstable_prepared_items`

*Prepair the items to be listed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` |  | 
`$clients_ids` |  | 

Source: [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 290](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L290)



### `mainwp_client_deleted`

*Delete client*

Fires after delete a client.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$current` | `object` | client deleted.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [class/class-mainwp-db-client.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-client.php), [line 1010](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db-client.php#L1010)



### `mainwp_before_select_clients_list`

*Action: mainwp_before_select_clients_list*

Fires before the Select Clients list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing Clients info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 355](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L355)



### `mainwp_after_select_clients_list`

*Action: mainwp_after_select_clients_list*

Fires after the Select Clients list.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing Clients info.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui-select-sites.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php), [line 405](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui-select-sites.php#L405)



### `mainwp_client_suspend`

*Fires immediately after update client suspend/unsuspend.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` | `object` | client data.
`$suspended` | `bool` | true\|false.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [class/class-mainwp-post-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-handler.php), [line 1111](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-handler.php#L1111)



### `mainwp_manageclients_tabletop`

*Method render_second_top_header()*

Render second top header.


Source: [pages/page-mainwp-client.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php), [line 565](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php#L565)



### `mainwp_client_suspend`

*Fires immediately after update client suspend/unsuspend.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$inserted` |  | 
`$new_suspended` | `bool` | true\|false.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [pages/page-mainwp-client.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php), [line 1353](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php#L1353)



### `mainwp_clients_overview_screen_options_top`

*Action: mainwp_clients_overview_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 366](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L366)



### `mainwp_clients_overview_screen_options_bottom`

*Action: mainwp_clients_overview_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 380](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L380)



### `mainwp_clients_overview_help_item`

*Action: mainwp_clients_overview_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Clients page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 521](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L521)



### `mainwp_clients_overview_note_widget_top`

*Actoin: mainwp_clients_overview_note_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-note.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php), [line 78](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php#L78)



### `mainwp_clients_overview_note_widget_bottom`

*Action: mainwp_clients_overview_note_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-note.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php), [line 100](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php#L100)



### `mainwp_clients_overview_contact_widget_top`

*Actoin: mainwp_clients_overview_contact_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$contact_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 82](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L82)



### `mainwp_clients_overview_contact_widget_bottom`

*Action: mainwp_clients_overview_contact_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$contact_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 142](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L142)



### `mainwp_clients_overview_overview_widget_top`

*Actoin: mainwp_clients_overview_overview_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php), [line 82](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php#L82)



### `mainwp_clients_overview_overview_widget_bottom`

*Action: mainwp_clients_overview_overview_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php), [line 159](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-info.php#L159)



### `mainwp_clients_overview_info_widget_top`

*Actoin: mainwp_clients_overview_info_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 71](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L71)



### `mainwp_clients_overview_info_table_top`

*Action: mainwp_clients_overview_info_table_top*

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 89](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L89)



### `mainwp_clients_overview_info_table_bottom`

*Action: mainwp_clients_overview_info_table_bottom*

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 128](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L128)



### `mainwp_clients_overview_info_widget_bottom`

*Action: mainwp_clients_overview_info_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client_info` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 147](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L147)



### `mainwp_clients_widget_top`

*Actoin: mainwp_clients_widget_top*

Fires at the top of the Clients widget on the overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing the clients info.

**Changelog**

Version | Description
------- | -----------
`4.4` | 

Source: [widgets/widget-mainwp-clients.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php), [line 62](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php#L62)



### `mainwp_clients_widget_bottom`

*Action: mainwp_clients_widget_bottom*

Fires at the bottom of the Clients widget on the overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$clients` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.4` | 

Source: [widgets/widget-mainwp-clients.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php), [line 161](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php#L161)



### `mainwp_clients_info_widget_top`

*Actoin: mainwp_clients_info_widget_top*

Fires at the top of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 84](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L84)



### `mainwp_clients_info_table_top`

*Action: mainwp_clients_info_table_top*

Fires at the top of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 107](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L107)



### `mainwp_clients_info_table_bottom`

*Action: mainwp_clients_info_table_bottom*

Fires at the bottom of the Site Info table in Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 168](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L168)



### `mainwp_clients_info_widget_bottom`

*Action: mainwp_clients_info_widget_bottom*

Fires at the bottom of the Site Info widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 183](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L183)



### `mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`

*Get client by tag id.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` |  | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php), [line 404](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php#L404)



### `mainwp_clients_sitestable_item`

*Filter: mainwp_clients_sitestable_item*

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

Source: [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 60](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L60)



### `mainwp_clients_sitestable_getcolumns`

*Filter: mainwp_clients_sitestable_getcolumns*

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

Source: [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 156](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L156)



### `mainwp_manageclients_bulk_actions`

*Filter: mainwp_manageclients_bulk_actions*

Filters bulk actions on the Clients page. Allows user to hook in new actions or remove default ones.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$actions` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 206](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L206)



### `mainwp_clients_table_features`

*Filter: mainwp_clients_table_features*

Filter the Clients table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-client-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php), [line 409](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-client-list-table.php#L409)



### `mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`

*Get clients by item.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` |  | 

Source: [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 566](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L566)



### `mainwp_clients_getmetaboxes`

*Method add_meta_boxes()*

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 143](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L143)



### `mainwp_clients_overview_enabled_widgets`

*Unset unwanted Widgets*

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

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 191](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L191)



### `mainwp_clients_widgets_screen_options`

*Filter: mainwp_clients_widgets_screen_options*

Filters available widgets on the Overview page allowing users to unsent unwanted widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$custom_opts` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-client-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php), [line 438](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client-overview.php#L438)



### `mainwp_clients_overview_note_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$client_info` |  | 

Source: [widgets/widget-mainwp-client-overview-note.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php), [line 71](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-note.php#L71)



### `mainwp_clients_overview_contact_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`__('Client Contact', 'mainwp')` |  | 
`$contact_info` |  | 

Source: [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 73](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L73)



### `mainwp_clients_overview_contact_widget_sutbitle`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`__('Contact Information', 'mainwp')` |  | 
`$contact_info` |  | 

Source: [widgets/widget-mainwp-client-overview-contacts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php), [line 76](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-contacts.php#L76)



### `mainwp_clients_overview_info_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Additional Client Info', 'mainwp')` |  | 
`$client_info` |  | 

Source: [widgets/widget-mainwp-client-overview-custom-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php), [line 64](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-overview-custom-info.php#L64)



### `mainwp_clients_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Clients', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-clients.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php), [line 55](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-clients.php#L55)



### `mainwp_clients_info_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Client Info', 'mainwp')` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-client-info.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php), [line 78](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-client-info.php#L78)




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

Source: [../sources/mainwp-dashboard/class/class-mainwp-client-list-table.php](class/class-mainwp-client-list-table.php), [line 290](class/class-mainwp-client-list-table.php#L290-L330)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-db-client.php](class/class-mainwp-db-client.php), [line 1010](class/class-mainwp-db-client.php#L1010-L1019)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui-select-sites.php](class/class-mainwp-ui-select-sites.php), [line 355](class/class-mainwp-ui-select-sites.php#L355-L364)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui-select-sites.php](class/class-mainwp-ui-select-sites.php), [line 405](class/class-mainwp-ui-select-sites.php#L405-L414)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-handler.php](class/class-mainwp-post-handler.php), [line 1111](class/class-mainwp-post-handler.php#L1111-L1119)



### `mainwp_manageclients_tabletop`

*Method render_second_top_header()*

Render second top header.


Source: [../sources/mainwp-dashboard/pages/page-mainwp-client.php](pages/page-mainwp-client.php), [line 565](pages/page-mainwp-client.php#L565-L576)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client.php](pages/page-mainwp-client.php), [line 1353](pages/page-mainwp-client.php#L1353-L1361)



### `mainwp_clients_overview_screen_options_top`

*Action: mainwp_clients_overview_screen_options_top*

Fires at the top of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 366](pages/page-mainwp-client-overview.php#L366-L373)



### `mainwp_clients_overview_screen_options_bottom`

*Action: mainwp_clients_overview_screen_options_bottom*

Fires at the bottom of the Sceen Options modal on the Overview page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 380](pages/page-mainwp-client-overview.php#L380-L387)



### `mainwp_clients_overview_help_item`

*Action: mainwp_clients_overview_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Clients page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 521](pages/page-mainwp-client-overview.php#L521-L532)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-note.php](widgets/widget-mainwp-client-overview-note.php), [line 78](widgets/widget-mainwp-client-overview-note.php#L78-L87)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-note.php](widgets/widget-mainwp-client-overview-note.php), [line 100](widgets/widget-mainwp-client-overview-note.php#L100-L109)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-contacts.php](widgets/widget-mainwp-client-overview-contacts.php), [line 82](widgets/widget-mainwp-client-overview-contacts.php#L82-L91)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-contacts.php](widgets/widget-mainwp-client-overview-contacts.php), [line 142](widgets/widget-mainwp-client-overview-contacts.php#L142-L151)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-info.php](widgets/widget-mainwp-client-overview-info.php), [line 82](widgets/widget-mainwp-client-overview-info.php#L82-L91)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-info.php](widgets/widget-mainwp-client-overview-info.php), [line 159](widgets/widget-mainwp-client-overview-info.php#L159-L168)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-custom-info.php](widgets/widget-mainwp-client-overview-custom-info.php), [line 71](widgets/widget-mainwp-client-overview-custom-info.php#L71-L80)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-custom-info.php](widgets/widget-mainwp-client-overview-custom-info.php), [line 89](widgets/widget-mainwp-client-overview-custom-info.php#L89-L98)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-custom-info.php](widgets/widget-mainwp-client-overview-custom-info.php), [line 128](widgets/widget-mainwp-client-overview-custom-info.php#L128-L137)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-custom-info.php](widgets/widget-mainwp-client-overview-custom-info.php), [line 147](widgets/widget-mainwp-client-overview-custom-info.php#L147-L156)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-clients.php](widgets/widget-mainwp-clients.php), [line 62](widgets/widget-mainwp-clients.php#L62-L71)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-clients.php](widgets/widget-mainwp-clients.php), [line 161](widgets/widget-mainwp-clients.php#L161-L170)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-info.php](widgets/widget-mainwp-client-info.php), [line 84](widgets/widget-mainwp-client-info.php#L84-L93)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-info.php](widgets/widget-mainwp-client-info.php), [line 107](widgets/widget-mainwp-client-info.php#L107-L116)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-info.php](widgets/widget-mainwp-client-info.php), [line 168](widgets/widget-mainwp-client-info.php#L168-L177)



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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-info.php](widgets/widget-mainwp-client-info.php), [line 183](widgets/widget-mainwp-client-info.php#L183-L192)



### `mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`

*Get client by tag id.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php), [line 404](includes/rest-api/controller/version2/class-mainwp-rest-tags-controller.php#L404-L423)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-client-list-table.php](class/class-mainwp-client-list-table.php), [line 60](class/class-mainwp-client-list-table.php#L60-L69)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-client-list-table.php](class/class-mainwp-client-list-table.php), [line 156](class/class-mainwp-client-list-table.php#L156-L165)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-client-list-table.php](class/class-mainwp-client-list-table.php), [line 206](class/class-mainwp-client-list-table.php#L206-L213)



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

Source: [../sources/mainwp-dashboard/class/class-mainwp-client-list-table.php](class/class-mainwp-client-list-table.php), [line 409](class/class-mainwp-client-list-table.php#L409-L416)



### `mainwp_rest_routes_clients_controller_filter_allowed_fields_by_context`

*Get clients by item.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$client` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 566](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L566-L624)



### `mainwp_clients_getmetaboxes`

*Method add_meta_boxes()*

Add MainWP Overview Page Widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extMetaBoxs` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 143](pages/page-mainwp-client-overview.php#L143-L169)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 191](pages/page-mainwp-client-overview.php#L191-L201)



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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client-overview.php](pages/page-mainwp-client-overview.php), [line 438](pages/page-mainwp-client-overview.php#L438-L445)



### `mainwp_clients_overview_note_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Notes', 'mainwp')` |  | 
`$client_info` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-note.php](widgets/widget-mainwp-client-overview-note.php), [line 71](widgets/widget-mainwp-client-overview-note.php#L71-L71)



### `mainwp_clients_overview_contact_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`__('Client Contact', 'mainwp')` |  | 
`$contact_info` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-contacts.php](widgets/widget-mainwp-client-overview-contacts.php), [line 73](widgets/widget-mainwp-client-overview-contacts.php#L73-L73)



### `mainwp_clients_overview_contact_widget_sutbitle`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`__('Contact Information', 'mainwp')` |  | 
`$contact_info` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-contacts.php](widgets/widget-mainwp-client-overview-contacts.php), [line 76](widgets/widget-mainwp-client-overview-contacts.php#L76-L76)



### `mainwp_clients_overview_info_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Additional Client Info', 'mainwp')` |  | 
`$client_info` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-overview-custom-info.php](widgets/widget-mainwp-client-overview-custom-info.php), [line 64](widgets/widget-mainwp-client-overview-custom-info.php#L64-L64)



### `mainwp_clients_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Clients', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-clients.php](widgets/widget-mainwp-clients.php), [line 55](widgets/widget-mainwp-clients.php#L55-L55)



### `mainwp_clients_info_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Client Info', 'mainwp')` |  | 
`$website` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-client-info.php](widgets/widget-mainwp-client-info.php), [line 78](widgets/widget-mainwp-client-info.php#L78-L78)




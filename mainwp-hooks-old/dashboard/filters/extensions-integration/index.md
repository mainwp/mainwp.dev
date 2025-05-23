# Extensions & Integration Filters

Hooks related to extensions and third-party integrations.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_extension_card_top`](#mainwp_extension_card_top) - Action: mainwp_extension_card_top
- [`mainwp_extension_card_bottom`](#mainwp_extension_card_bottom) - Action: mainwp_extension_card_bottom
- [`mainwp_extensions_help_item`](#mainwp_extensions_help_item) - Action: mainwp_extensions_help_item
- [`mainwp-getextensions`](#mainwp-getextensions) - Method init_menu()
- [`mainwp_getextensions`](#mainwp_getextensions) - Method init_menu()

## Hook Details

### `mainwp_extension_card_top`

*Action: mainwp_extension_card_top*

Fires at the Extension card top

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extension` | `array` | Array containing the Extension information.

**Changelog**

Version | Description
------- | -----------
`4.1.4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-extensions-view.php](class/class-mainwp-extensions-view.php), [line 442](class/class-mainwp-extensions-view.php#L442-L451)



### `mainwp_extension_card_bottom`

*Action: mainwp_extension_card_bottom*

Fires at the Extension card bottom

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extension` | `array` | Array containing the Extension information.

**Changelog**

Version | Description
------- | -----------
`4.1.4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-extensions-view.php](class/class-mainwp-extensions-view.php), [line 530](class/class-mainwp-extensions-view.php#L530-L539)



### `mainwp_extensions_help_item`

*Action: mainwp_extensions_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Extensions page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions.php](pages/page-mainwp-extensions.php), [line 799](pages/page-mainwp-extensions.php#L799-L810)



### `mainwp-getextensions`

*Method init_menu()*

Instantiate Extensions Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($init_extensions)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getextensions'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions.php](pages/page-mainwp-extensions.php), [line 58](pages/page-mainwp-extensions.php#L58-L86)



### `mainwp_getextensions`

*Method init_menu()*

Instantiate Extensions Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$init_extensions` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions.php](pages/page-mainwp-extensions.php), [line 58](pages/page-mainwp-extensions.php#L58-L87)




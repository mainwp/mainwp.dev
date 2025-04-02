# Extensions & Integration Filters

Hooks related to extensions and third-party integrations.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp-getextensions`](#mainwp-getextensions) - Method init_menu()
- [`mainwp_boilerplate_get_tokens`](#mainwp-boilerplate-get-tokens) - Filter: mainwp_boilerplate_get_tokens
- [`mainwp_extension_card_bottom`](#mainwp-extension-card-bottom) - Action: mainwp_extension_card_bottom
- [`mainwp_extension_card_top`](#mainwp-extension-card-top) - Action: mainwp_extension_card_top
- [`mainwp_extensions_help_item`](#mainwp-extensions-help-item) - Action: mainwp_extensions_help_item
- [`mainwp_getextensions`](#mainwp-getextensions) - Method init_menu()

---

## Hook Details

<a id='mainwp-getextensions'></a>
### `mainwp-getextensions`

* Method init_menu()

Instantiate Extensions Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($init_extensions)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getextensions'` |  |

**Usage Locations:**

- [pages/page-mainwp-extensions.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions.php), [line 58](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions.php#L58)

---

<a id='mainwp-boilerplate-get-tokens'></a>
### `mainwp_boilerplate_get_tokens`

* Filter: mainwp_boilerplate_get_tokens

Enables and filters the Boilerplate extension tokens.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` | `object` | Object containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification-settings.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php), [line 629](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-settings.php#L629)

---

<a id='mainwp-extension-card-bottom'></a>
### `mainwp_extension_card_bottom`

* Action: mainwp_extension_card_bottom

Fires at the Extension card bottom

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extension` | `array` | Array containing the Extension information.

**Changelog**

Version | Description
------- | -----------
`4.1.4.1` |

**Usage Locations:**

- [class/class-mainwp-extensions-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php), [line 530](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php#L530)

---

<a id='mainwp-extension-card-top'></a>
### `mainwp_extension_card_top`

* Action: mainwp_extension_card_top

Fires at the Extension card top

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extension` | `array` | Array containing the Extension information.

**Changelog**

Version | Description
------- | -----------
`4.1.4.1` |

**Usage Locations:**

- [class/class-mainwp-extensions-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php), [line 442](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php#L442)

---

<a id='mainwp-extensions-help-item'></a>
### `mainwp_extensions_help_item`

* Action: mainwp_extensions_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Extensions page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`5.2` |

**Usage Locations:**

- [pages/page-mainwp-extensions.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions.php), [line 799](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions.php#L799)

---

<a id='mainwp-getextensions'></a>
### `mainwp_getextensions`

* Method init_menu()

Instantiate Extensions Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$init_extensions` |  |

**Usage Locations:**

- [pages/page-mainwp-extensions.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions.php), [line 58](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions.php#L58)

---


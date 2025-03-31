# API & Remote Communication Actions

Hooks for API endpoints and remote communication with child sites.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`cloudways_api_form_bottom`](#cloudways-api-form-bottom) - Action: cloudways_api_form_bottom
- [`cloudways_api_form_top`](#cloudways-api-form-top) - Action: cloudways_api_form_top
- [`cpanel_api_form`](#cpanel-api-form) - Action: cpanel_api_form
- [`cpanel_api_form_bottom`](#cpanel-api-form-bottom) - Action: cpanel_api_form_bottom
- [`digitalocean_api_form_bottom`](#digitalocean-api-form-bottom) - Action: digitalocean_api_form_bottom
- [`digitalocean_api_form_top`](#digitalocean-api-form-top) - Action: digitalocean_api_form_top
- [`gridpane_api_form_bottom`](#gridpane-api-form-bottom) - Action: gridpane_api_form_bottom
- [`gridpane_api_form_top`](#gridpane-api-form-top) - Action: gridpane_api_form_top
- [`https_local_ssl_verify`](#https-local-ssl-verify) - *Arguments*
- [`kinsta_api_form_bottom`](#kinsta-api-form-bottom) - Action: kinsta_api_form_bottom
- [`kinsta_api_form_top`](#kinsta-api-form-top) - Action: kinsta_api_form_top
- [`linode_api_form_bottom`](#linode-api-form-bottom) - Action: linode_api_form_bottom
- [`linode_api_form_top`](#linode-api-form-top) - Action: linode_api_form_top
- [`mainwp_curl_http_version`](#mainwp-curl-http-version) - Method try visit.
- [`mainwp_decrypt_key_value`](#mainwp-decrypt-key-value) - Method decrypt_api_keys
- [`mainwp_encrypt_key_value`](#mainwp-encrypt-key-value) - Method encrypt_api_keys
- [`mainwp_is_rest_api_request`](#mainwp-is-rest-api-request) - Whether this is a REST API request.
- [`mainwp_remote_destination_info`](#mainwp-remote-destination-info) - Method mainwp_backup_upload_checkstatus()
- [`mainwp_rest_api_disabled`](#mainwp-rest-api-disabled) - Method is_rest_api_enabled()
- [`mainwp_rest_api_enabled`](#mainwp-rest-api-enabled) - Method init_rest_api()
- [`mainwp_rest_api_get_rest_namespaces`](#mainwp-rest-api-get-rest-namespaces) - Get API namespaces - new namespaces should be registered here.
- [`mainwp_rest_api_help_item`](#mainwp-rest-api-help-item) - Action: mainwp_rest_api_help_item
- [`mainwp_rest_api_v2_enabled`](#mainwp-rest-api-v2-enabled) - Hook into WordPress ready to init the REST API as needed.
- [`mainwp_rest_api_validate`](#mainwp-rest-api-validate) - Method cost_tracker_rest_api_get_all_costs_callback()
- [`mainwp_rest_batch_items_limit`](#mainwp-rest-batch-items-limit) - Check batch limit.
- [`mainwp_rest_collection_params`](#mainwp-rest-collection-params) - Filter collection parameters for the controller.
- [`mainwp_rest_cost_collection_params`](#mainwp-rest-cost-collection-params) - Filter collection parameters.
- [`mainwp_rest_is_request_to_rest_api`](#mainwp-rest-is-request-to-rest-api) - Check if is request to our REST API.
- [`mainwp_rest_prepare_cost`](#mainwp-rest-prepare-cost) - Filter product reviews object returned from the REST API.
- [`mainwp_rest_prepare_site`](#mainwp-rest-prepare-site) - Filterobject returned from the REST API.
- [`mainwp_rest_{$type}_object_query`](#mainwp-rest-type-object-query) - Filter the query arguments for a request.
- [`plesk_api_form_bottom`](#plesk-api-form-bottom) - Action: plesk_api_form_bottom
- [`plesk_api_form_top`](#plesk-api-form-top) - Action: plesk_api_form_top
- [`rest_api_form_bottom`](#rest-api-form-bottom) - Action: rest_api_form_bottom
- [`rest_api_form_top`](#rest-api-form-top) - Action: rest_api_form_top
- [`vultr_api_form_bottom`](#vultr-api-form-bottom) - Action: vultr_api_form_bottom
- [`vultr_api_form_top`](#vultr-api-form-top) - Action: vultr_api_form_top

---

## Hook Details

<a id='cloudways-api-form-bottom'></a>
### `cloudways_api_form_bottom`

* Action: cloudways_api_form_bottom

Fires at the bottom of CloudWays API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 317](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L317)

---

<a id='cloudways-api-form-top'></a>
### `cloudways_api_form_top`

* Action: cloudways_api_form_top

Fires at the top of CloudWays API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 274](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L274)

---

<a id='cpanel-api-form'></a>
### `cpanel_api_form`

* Action: cpanel_api_form

Fires at the top of cPanel API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 618](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L618)

---

<a id='cpanel-api-form-bottom'></a>
### `cpanel_api_form_bottom`

* Action: cpanel_api_form_bottom

Fires at the bottom of cPanel API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 685](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L685)

---

<a id='digitalocean-api-form-bottom'></a>
### `digitalocean_api_form_bottom`

* Action: digitalocean_api_form_bottom

Fires at the bottom of DigitalOcean API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 586](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L586)

---

<a id='digitalocean-api-form-top'></a>
### `digitalocean_api_form_top`

* Action: digitalocean_api_form_top

Fires at the top of DigitalOcean API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 551](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L551)

---

<a id='gridpane-api-form-bottom'></a>
### `gridpane_api_form_bottom`

* Action: gridpane_api_form_bottom

Fires at the bottom of GridPane API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 383](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L383)

---

<a id='gridpane-api-form-top'></a>
### `gridpane_api_form_top`

* Action: gridpane_api_form_top

Fires at the top of GridPane API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 350](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L350)

---

<a id='https-local-ssl-verify'></a>
### `https_local_ssl_verify`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php), [line 704](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information-handler.php#L704)

---

<a id='kinsta-api-form-bottom'></a>
### `kinsta_api_form_bottom`

* Action: kinsta_api_form_bottom

Fires at the bottom of Kinsta API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 851](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L851)

---

<a id='kinsta-api-form-top'></a>
### `kinsta_api_form_top`

* Action: kinsta_api_form_top

Fires at the top of Kinsta API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 795](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L795)

---

<a id='linode-api-form-bottom'></a>
### `linode_api_form_bottom`

* Action: linode_api_form_bottom

Fires at the bottom of Vultr API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 518](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L518)

---

<a id='linode-api-form-top'></a>
### `linode_api_form_top`

* Action: linode_api_form_top

Fires at the top of Vultr API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 483](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L483)

---

<a id='mainwp-curl-http-version'></a>
### `mainwp_curl_http_version`

* Method try visit.

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`false` |  | 
`$url` | `string` | Child Site URL.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 1351](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L1351)
- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 32](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L32)
- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 688](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L688)
- [class/class-mainwp-uptime-monitoring-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php), [line 350](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-connect.php#L350)

---

<a id='mainwp-decrypt-key-value'></a>
### `mainwp_decrypt_key_value`

* Method decrypt_api_keys

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$encrypted_data` | `mixed` | encrypted data.
`$def_val` | `string` | default data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$encrypted_data` | `mixed` | encrypted data.
`$def_val` | `string` | default data.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-utility.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php), [line 556](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php#L556)

---

<a id='mainwp-encrypt-key-value'></a>
### `mainwp_encrypt_key_value`

* Method encrypt_api_keys

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$data` | `string` | data.
`$prefix` |  | 
`$file_key` | `string` | file key.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$data` | `string` | data.
`$prefix` |  | 
`$file_key` | `string` | file key.

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-utility.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php), [line 524](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php#L524)

---

<a id='mainwp-is-rest-api-request'></a>
### `mainwp_is_rest_api_request`

* Whether this is a REST API request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_rest_api_request` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_rest_api_request` |  |

**Changelog**

Version | Description
------- | -----------
`5.1.1` |

**Usage Locations:**

- [includes/class-mainwp-setup.php](https://github.com/mainwp/mainwp/blob/master/includes/class-mainwp-setup.php), [line 81](https://github.com/mainwp/mainwp/blob/master/includes/class-mainwp-setup.php#L81)

---

<a id='mainwp-remote-destination-info'></a>
### `mainwp_remote_destination_info`

* Method mainwp_backup_upload_checkstatus()

Check upload status

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`isset($_POST['remote_destination']) ? sanitize_text_field(wp_unslash($_POST['remote_destination'])) : ''` |  |

**Usage Locations:**

- [class/class-mainwp-post-backup-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-backup-handler.php), [line 376](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-backup-handler.php#L376)

---

<a id='mainwp-rest-api-disabled'></a>
### `mainwp_rest_api_disabled`

* Method is_rest_api_enabled()

Check if Enabled the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 92](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L92)

---

<a id='mainwp-rest-api-enabled'></a>
### `mainwp_rest_api_enabled`

* Method init_rest_api()

Adds an action to create the rest API endpoints if activated in the plugin settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 56](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L56)

---

<a id='mainwp-rest-api-get-rest-namespaces'></a>
### `mainwp_rest_api_get_rest_namespaces`

* Get API namespaces - new namespaces should be registered here.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('mainwp/v2' => $this->get_v2_controllers())` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('mainwp/v2' => $this->get_v2_controllers())` |  |

**Usage Locations:**

- [includes/rest-api/class-mainwp-rest-server.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php), [line 89](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php#L89)

---

<a id='mainwp-rest-api-help-item'></a>
### `mainwp_rest_api_help_item`

* Action: mainwp_rest_api_help_item

Fires at the bottom of the help articles list in the Help sidebar on the REST API page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 1260](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L1260)

---

<a id='mainwp-rest-api-v2-enabled'></a>
### `mainwp_rest_api_v2_enabled`

* Hook into WordPress ready to init the REST API as needed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [includes/rest-api/class-mainwp-rest-server.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php), [line 47](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-server.php#L47)

---

<a id='mainwp-rest-api-validate'></a>
### `mainwp_rest_api_validate`

* Method cost_tracker_rest_api_get_all_costs_callback()

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-all-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

**Usage Locations:**

- [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 167](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L167)
- [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 195](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L195)
- [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 245](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L245)
- [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 285](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L285)

---

<a id='mainwp-rest-batch-items-limit'></a>
### `mainwp_rest_batch_items_limit`

* Check batch limit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 
`$this->get_normalized_rest_base()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 
`$this->get_normalized_rest_base()` |  |

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 189](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L189)
- [includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php), [line 471](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php#L471)

---

<a id='mainwp-rest-collection-params'></a>
### `mainwp_rest_collection_params`

* Filter collection parameters for the controller.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` |  | 
`$this` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` |  | 
`$this` |  |

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 1388](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L1388)

---

<a id='mainwp-rest-cost-collection-params'></a>
### `mainwp_rest_cost_collection_params`

* Filter collection parameters.

This filter registers the collection parameter, but does not map the
collection parameter to an internal WP_Comment_Query parameter. Use the
`wc_rest_review_query` filter to set WP_Comment_Query parameters.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` | `array` | JSON Schema-formatted collection parameters.

**Changelog**

Version | Description
------- | -----------
`5.2` |

**Usage Locations:**

- [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 753](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L753)

---

<a id='mainwp-rest-is-request-to-rest-api'></a>
### `mainwp_rest_is_request_to_rest_api`

* Check if is request to our REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_api || $extension_api` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_api || $extension_api` |  |

**Usage Locations:**

- [includes/rest-api/class-mainwp-rest-authentication.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-authentication.php), [line 89](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-authentication.php#L89)

---

<a id='mainwp-rest-prepare-cost'></a>
### `mainwp_rest_prepare_cost`

* Filter product reviews object returned from the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The  object.
`$review` |  | 
`$request` | `\WP_REST_Request` | Request object.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The  object.
`$review` |  | 
`$request` | `\WP_REST_Request` | Request object.

**Usage Locations:**

- [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 947](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L947)

---

<a id='mainwp-rest-prepare-site'></a>
### `mainwp_rest_prepare_site`

* Filterobject returned from the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The object.
`$item` | `mixed` | The object used to create response.
`$request` | `\WP_REST_Request` | Request object.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The object.
`$item` | `mixed` | The object used to create response.
`$request` | `\WP_REST_Request` | Request object.

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2360](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2360)

---

<a id='mainwp-rest-type-object-query'></a>
### `mainwp_rest_{$type}_object_query`

* Filter the query arguments for a request.

Enables adding extra arguments or setting defaults for a post
collection request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` | `array` | Key value array of query var to query value.
`$request` | `\WP_REST_Request` | The request used.

**Usage Locations:**

- [includes/rest-api/controller/version2/class-mainwp-rest-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 410](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L410)

---

<a id='plesk-api-form-bottom'></a>
### `plesk_api_form_bottom`

* Action: plesk_api_form_bottom

Fires at the bottom of Plesk API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 762](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L762)

---

<a id='plesk-api-form-top'></a>
### `plesk_api_form_top`

* Action: plesk_api_form_top

Fires at the top of Plesk API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 718](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L718)

---

<a id='rest-api-form-bottom'></a>
### `rest_api_form_bottom`

* Action: rest_api_form_bottom

Fires at the bottom of REST API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 936](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L936)

---

<a id='rest-api-form-top'></a>
### `rest_api_form_top`

* Action: rest_api_form_top

Fires at the top of REST API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 850](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L850)

---

<a id='vultr-api-form-bottom'></a>
### `vultr_api_form_bottom`

* Action: vultr_api_form_bottom

Fires at the bottom of Vultr API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 450](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L450)

---

<a id='vultr-api-form-top'></a>
### `vultr_api_form_top`

* Action: vultr_api_form_top

Fires at the top of Vultr API form.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 417](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L417)

---


# API & Remote Communication Actions

Hooks for API endpoints and remote communication with child sites.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`cloudways_api_form_top`](#cloudways_api_form_top) - Action: cloudways_api_form_top
- [`cloudways_api_form_bottom`](#cloudways_api_form_bottom) - Action: cloudways_api_form_bottom
- [`gridpane_api_form_top`](#gridpane_api_form_top) - Action: gridpane_api_form_top
- [`gridpane_api_form_bottom`](#gridpane_api_form_bottom) - Action: gridpane_api_form_bottom
- [`vultr_api_form_top`](#vultr_api_form_top) - Action: vultr_api_form_top
- [`vultr_api_form_bottom`](#vultr_api_form_bottom) - Action: vultr_api_form_bottom
- [`linode_api_form_top`](#linode_api_form_top) - Action: linode_api_form_top
- [`linode_api_form_bottom`](#linode_api_form_bottom) - Action: linode_api_form_bottom
- [`digitalocean_api_form_top`](#digitalocean_api_form_top) - Action: digitalocean_api_form_top
- [`digitalocean_api_form_bottom`](#digitalocean_api_form_bottom) - Action: digitalocean_api_form_bottom
- [`cpanel_api_form`](#cpanel_api_form) - Action: cpanel_api_form
- [`cpanel_api_form_bottom`](#cpanel_api_form_bottom) - Action: cpanel_api_form_bottom
- [`plesk_api_form_top`](#plesk_api_form_top) - Action: plesk_api_form_top
- [`plesk_api_form_bottom`](#plesk_api_form_bottom) - Action: plesk_api_form_bottom
- [`kinsta_api_form_top`](#kinsta_api_form_top) - Action: kinsta_api_form_top
- [`kinsta_api_form_bottom`](#kinsta_api_form_bottom) - Action: kinsta_api_form_bottom
- [`rest_api_form_top`](#rest_api_form_top) - Action: rest_api_form_top
- [`rest_api_form_bottom`](#rest_api_form_bottom) - Action: rest_api_form_bottom
- [`mainwp_rest_api_help_item`](#mainwp_rest_api_help_item) - Action: mainwp_rest_api_help_item
- [`mainwp_is_rest_api_request`](#mainwp_is_rest_api_request) - Whether this is a REST API request.
- [`mainwp_rest_is_request_to_rest_api`](#mainwp_rest_is_request_to_rest_api) - Check if is request to our REST API.
- [`mainwp_rest_api_v2_enabled`](#mainwp_rest_api_v2_enabled) - Hook into WordPress ready to init the REST API as needed.
- [`mainwp_rest_api_get_rest_namespaces`](#mainwp_rest_api_get_rest_namespaces) - Get API namespaces - new namespaces should be registered here.
- [`mainwp_rest_api_disabled`](#mainwp_rest_api_disabled) - Method is_rest_api_enabled()
- [`mainwp_rest_batch_items_limit`](#mainwp_rest_batch_items_limit) - Check batch limit.
- [`mainwp_rest_{$type}_object_query`](#mainwp_rest_type_object_query) - Filter the query arguments for a request.
- [`mainwp_rest_collection_params`](#mainwp_rest_collection_params) - Filter collection parameters for the controller.
- [`mainwp_rest_batch_items_limit`](#mainwp_rest_batch_items_limit) - Check batch limit.
- [`mainwp_rest_prepare_site`](#mainwp_rest_prepare_site) - Filterobject returned from the REST API.
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Fetch uptime urls.
- [`mainwp_remote_destination_info`](#mainwp_remote_destination_info) - Method mainwp_backup_upload_checkstatus()
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Method try visit.
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Method fetch_urls_authed()
- [`mainwp_curl_http_version`](#mainwp_curl_http_version) - Method fetch_url_site()
- [`mainwp_rest_api_enabled`](#mainwp_rest_api_enabled) - Method init_rest_api()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_all_costs_callback()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_client_costs_callback()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_site_costs_callback()
- [`mainwp_rest_api_validate`](#mainwp_rest_api_validate) - Method cost_tracker_rest_api_get_costs_callback()
- [`mainwp_rest_cost_collection_params`](#mainwp_rest_cost_collection_params) - Filter collection parameters.
- [`mainwp_rest_prepare_cost`](#mainwp_rest_prepare_cost) - Filter product reviews object returned from the REST API.
- [`https_local_ssl_verify`](#https_local_ssl_verify) - *Arguments*

## Hook Details

### `cloudways_api_form_top`

*Action: cloudways_api_form_top*

Fires at the top of CloudWays API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 274](modules/api-backups/classes/class-api-backups-settings.php#L274-L281)



### `cloudways_api_form_bottom`

*Action: cloudways_api_form_bottom*

Fires at the bottom of CloudWays API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 317](modules/api-backups/classes/class-api-backups-settings.php#L317-L324)



### `gridpane_api_form_top`

*Action: gridpane_api_form_top*

Fires at the top of GridPane API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 350](modules/api-backups/classes/class-api-backups-settings.php#L350-L357)



### `gridpane_api_form_bottom`

*Action: gridpane_api_form_bottom*

Fires at the bottom of GridPane API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 383](modules/api-backups/classes/class-api-backups-settings.php#L383-L390)



### `vultr_api_form_top`

*Action: vultr_api_form_top*

Fires at the top of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 417](modules/api-backups/classes/class-api-backups-settings.php#L417-L424)



### `vultr_api_form_bottom`

*Action: vultr_api_form_bottom*

Fires at the bottom of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 450](modules/api-backups/classes/class-api-backups-settings.php#L450-L457)



### `linode_api_form_top`

*Action: linode_api_form_top*

Fires at the top of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 483](modules/api-backups/classes/class-api-backups-settings.php#L483-L490)



### `linode_api_form_bottom`

*Action: linode_api_form_bottom*

Fires at the bottom of Vultr API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 518](modules/api-backups/classes/class-api-backups-settings.php#L518-L525)



### `digitalocean_api_form_top`

*Action: digitalocean_api_form_top*

Fires at the top of DigitalOcean API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 551](modules/api-backups/classes/class-api-backups-settings.php#L551-L558)



### `digitalocean_api_form_bottom`

*Action: digitalocean_api_form_bottom*

Fires at the bottom of DigitalOcean API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 586](modules/api-backups/classes/class-api-backups-settings.php#L586-L593)



### `cpanel_api_form`

*Action: cpanel_api_form*

Fires at the top of cPanel API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 618](modules/api-backups/classes/class-api-backups-settings.php#L618-L625)



### `cpanel_api_form_bottom`

*Action: cpanel_api_form_bottom*

Fires at the bottom of cPanel API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 685](modules/api-backups/classes/class-api-backups-settings.php#L685-L692)



### `plesk_api_form_top`

*Action: plesk_api_form_top*

Fires at the top of Plesk API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 718](modules/api-backups/classes/class-api-backups-settings.php#L718-L725)



### `plesk_api_form_bottom`

*Action: plesk_api_form_bottom*

Fires at the bottom of Plesk API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 762](modules/api-backups/classes/class-api-backups-settings.php#L762-L769)



### `kinsta_api_form_top`

*Action: kinsta_api_form_top*

Fires at the top of Kinsta API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 795](modules/api-backups/classes/class-api-backups-settings.php#L795-L802)



### `kinsta_api_form_bottom`

*Action: kinsta_api_form_bottom*

Fires at the bottom of Kinsta API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 851](modules/api-backups/classes/class-api-backups-settings.php#L851-L858)



### `rest_api_form_top`

*Action: rest_api_form_top*

Fires at the top of REST API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-rest-api-page.php](pages/page-mainwp-rest-api-page.php), [line 850](pages/page-mainwp-rest-api-page.php#L850-L857)



### `rest_api_form_bottom`

*Action: rest_api_form_bottom*

Fires at the bottom of REST API form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-rest-api-page.php](pages/page-mainwp-rest-api-page.php), [line 936](pages/page-mainwp-rest-api-page.php#L936-L943)



### `mainwp_rest_api_help_item`

*Action: mainwp_rest_api_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the REST API page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-rest-api-page.php](pages/page-mainwp-rest-api-page.php), [line 1260](pages/page-mainwp-rest-api-page.php#L1260-L1271)



### `mainwp_is_rest_api_request`

*Whether this is a REST API request.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$is_rest_api_request` |  | 

**Changelog**

Version | Description
------- | -----------
`5.1.1` | 

Source: [../sources/mainwp-dashboard/includes/class-mainwp-setup.php](includes/class-mainwp-setup.php), [line 81](includes/class-mainwp-setup.php#L81-L86)



### `mainwp_rest_is_request_to_rest_api`

*Check if is request to our REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$mainwp_api || $extension_api` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/class-mainwp-rest-authentication.php](includes/rest-api/class-mainwp-rest-authentication.php), [line 89](includes/rest-api/class-mainwp-rest-authentication.php#L89-L108)



### `mainwp_rest_api_v2_enabled`

*Hook into WordPress ready to init the REST API as needed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/class-mainwp-rest-server.php](includes/rest-api/class-mainwp-rest-server.php), [line 47](includes/rest-api/class-mainwp-rest-server.php#L47-L51)



### `mainwp_rest_api_get_rest_namespaces`

*Get API namespaces - new namespaces should be registered here.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array('mainwp/v2' => $this->get_v2_controllers())` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/class-mainwp-rest-server.php](includes/rest-api/class-mainwp-rest-server.php), [line 89](includes/rest-api/class-mainwp-rest-server.php#L89-L100)



### `mainwp_rest_api_disabled`

*Method is_rest_api_enabled()*

Check if Enabled the REST API.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php](includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php), [line 92](includes/rest-api/controller/version1/class-mainwp-rest-api-v1.php#L92-L99)



### `mainwp_rest_batch_items_limit`

*Check batch limit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 
`$this->get_normalized_rest_base()` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 189](includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L189-L196)



### `mainwp_rest_{$type}_object_query`

*Filter the query arguments for a request.*

Enables adding extra arguments or setting defaults for a post
collection request.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$args` | `array` | Key value array of query var to query value.
`$request` | `\WP_REST_Request` | The request used.

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 406](includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L406-L415)



### `mainwp_rest_collection_params`

*Filter collection parameters for the controller.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$params` |  | 
`$this` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-controller.php), [line 1384](includes/rest-api/controller/version2/class-mainwp-rest-controller.php#L1384-L1390)



### `mainwp_rest_batch_items_limit`

*Check batch limit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 
`$this->get_normalized_rest_base()` |  | 

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php), [line 471](includes/rest-api/controller/version2/class-mainwp-rest-global-batch-controller.php#L471-L478)



### `mainwp_rest_prepare_site`

*Filterobject returned from the REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The object.
`$item` | `mixed` | The object used to create response.
`$request` | `\WP_REST_Request` | Request object.

Source: [../sources/mainwp-dashboard/includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php), [line 2346](includes/rest-api/controller/version2/class-mainwp-rest-sites-controller.php#L2346-L2353)



### `mainwp_curl_http_version`

*Fetch uptime urls.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-uptime-monitoring-connect.php](class/class-mainwp-uptime-monitoring-connect.php), [line 350](class/class-mainwp-uptime-monitoring-connect.php#L350-L497)



### `mainwp_remote_destination_info`

*Method mainwp_backup_upload_checkstatus()*

Check upload status

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`isset($_POST['remote_destination']) ? sanitize_text_field(wp_unslash($_POST['remote_destination'])) : ''` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-post-backup-handler.php](class/class-mainwp-post-backup-handler.php), [line 376](class/class-mainwp-post-backup-handler.php#L376-L391)



### `mainwp_curl_http_version`

*Method try visit.*

Try connecting to Child Site via cURL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`false` |  | 
`$url` | `string` | Child Site URL.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 32](class/class-mainwp-connect.php#L32-L101)



### `mainwp_curl_http_version`

*Method fetch_urls_authed()*

Fetches data from child sites if authenticated.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 688](class/class-mainwp-connect.php#L688-L894)



### `mainwp_curl_http_version`

*Method fetch_url_site()*

M Fetch URL.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website ? $website->id : false` |  | 
`$url` | `string` | URL to fetch from.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 1351](class/class-mainwp-connect.php#L1351-L1486)



### `mainwp_rest_api_enabled`

*Method init_rest_api()*

Adds an action to create the rest API endpoints if activated in the plugin settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 56](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L56-L62)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_all_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-all-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 167](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L167-L180)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_client_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-client-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 195](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L195-L208)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_site_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-site-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 245](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L245-L258)



### `mainwp_rest_api_validate`

*Method cost_tracker_rest_api_get_costs_callback()*

Callback function for managing the response to API requests made for the endpoint: cost-tracker
Can be accessed via a request like: https://yourdomain.com/wp-json/mainwp/v1/cost-tracker/get-costs
API Method: GET

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$request` | `array` | The request made in the API call which includes all parameters.

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php), [line 285](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-v1.php#L285-L298)



### `mainwp_rest_cost_collection_params`

*Filter collection parameters.*

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

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 753](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L753-L763)



### `mainwp_rest_prepare_cost`

*Filter product reviews object returned from the REST API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` | `array` | The  object.
`$review` |  | 
`$request` | `\WP_REST_Request` | Request object.

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 947](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L947-L953)



### `https_local_ssl_verify`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information-handler.php](pages/page-mainwp-server-information-handler.php), [line 704](pages/page-mainwp-server-information-handler.php#L704-L704)




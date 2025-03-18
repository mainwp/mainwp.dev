# User Management Filters

Hooks related to user management, roles, and capabilities.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_admin_pass_before_users_table`](#mainwp_admin_pass_before_users_table) - Action: mainwp_admin_pass_before_users_table
- [`mainwp_admin_pass_after_users_table`](#mainwp_admin_pass_after_users_table) - Action: mainwp_admin_pass_after_users_table
- [`mainwp_users_bulk_action`](#mainwp_users_bulk_action) - Action: mainwp_users_bulk_action
- [`mainwp_users_actions_bar_left`](#mainwp_users_actions_bar_left) - Users actions bar (left)
- [`mainwp_users_actions_bar_right`](#mainwp_users_actions_bar_right) - Users actions bar (right)
- [`mainwp_manage_users_sidebar_top`](#mainwp_manage_users_sidebar_top) - Action: mainwp_manage_users_sidebar_top
- [`mainwp_manage_users_before_select_sites`](#mainwp_manage_users_before_select_sites) - Action: mainwp_manage_users_before_select_sites
- [`mainwp_manage_users_after_select_sites`](#mainwp_manage_users_after_select_sites) - Action: mainwp_manage_users_after_select_sites
- [`mainwp_manage_users_before_search_options`](#mainwp_manage_users_before_search_options) - Action: mainwp_manage_users_before_search_options
- [`mainwp_manage_users_after_search_options`](#mainwp_manage_users_after_search_options) - Action: mainwp_manage_users_after_search_options
- [`mainwp_manage_users_before_submit_button`](#mainwp_manage_users_before_submit_button) - Action: mainwp_manage_users_before_submit_button
- [`mainwp_manage_users_after_submit_button`](#mainwp_manage_users_after_submit_button) - Action: mainwp_manage_users_after_submit_button
- [`mainwp_manage_users_sidebar_bottom`](#mainwp_manage_users_sidebar_bottom) - Action: mainwp_manage_users_sidebar_bottom
- [`mainwp_before_users_table`](#mainwp_before_users_table) - Action: mainwp_before_users_table
- [`mainwp_users_table_header`](#mainwp_users_table_header) - Renders Users Table.
- [`mainwp_after_users_table`](#mainwp_after_users_table) - Action: mainwp_after_users_table
- [`mainwp_users_table_column`](#mainwp_users_table_column) - Renders Search results.
- [`mainwp_users_table_action`](#mainwp_users_table_action) - Action: mainwp_users_table_action
- [`mainwp_before_user_action`](#mainwp_before_user_action) - Action: mainwp_before_user_action
- [`mainwp_user_action`](#mainwp_user_action) - Fires immediately after user action.
- [`mainwp_after_user_action`](#mainwp_after_user_action) - Action: mainwp_after_user_action
- [`mainwp_before_new_user_form`](#mainwp_before_new_user_form) - Action: mainwp_before_new_user_form
- [`mainwp_before_new_user_form_fields`](#mainwp_before_new_user_form_fields) - Action: mainwp_before_new_user_form_fields
- [`mainwp_after_new_user_form_fields`](#mainwp_after_new_user_form_fields) - Action: mainwp_after_new_user_form_fields
- [`mainwp_add_new_user_sidebar_top`](#mainwp_add_new_user_sidebar_top) - Action: mainwp_add_new_user_sidebar_top
- [`mainwp_add_new_user_before_select_sites`](#mainwp_add_new_user_before_select_sites) - Action: mainwp_add_new_user_before_select_sites
- [`mainwp_add_new_user_after_select_sites`](#mainwp_add_new_user_after_select_sites) - Action: mainwp_add_new_user_after_select_sites
- [`mainwp_add_new_user_before_submit_button`](#mainwp_add_new_user_before_submit_button) - Action: mainwp_add_new_user_before_submit_button
- [`mainwp_add_new_user_after_submit_button`](#mainwp_add_new_user_after_submit_button) - Action: mainwp_add_new_user_after_submit_button
- [`mainwp_add_new_user_sidebar_bottom`](#mainwp_add_new_user_sidebar_bottom) - Action: mainwp_add_new_user_sidebar_bottom
- [`mainwp_after_new_user_form`](#mainwp_after_new_user_form) - Action: mainwp_after_new_user_form
- [`mainwp_before_import_users`](#mainwp_before_import_users) - Action: mainwp_before_import_users
- [`mainwp_after_import_users`](#mainwp_after_import_users) - Action: mainwp_after_import_users
- [`mainwp_before_user_create`](#mainwp_before_user_create) - Action: mainwp_before_user_create
- [`mainwp_after_user_create`](#mainwp_after_user_create) - Action: mainwp_after_user_create
- [`mainwp_import_users_modal_top`](#mainwp_import_users_modal_top) - Action: mainwp_import_users_modal_top
- [`mainwp_import_users_modal_bottom`](#mainwp_import_users_modal_bottom) - Action: mainwp_import_users_modal_bottom
- [`mainwp_before_user_create`](#mainwp_before_user_create) - Action: mainwp_before_user_create
- [`mainwp_after_user_create`](#mainwp_after_user_create) - Action: mainwp_after_user_create
- [`mainwp_users_help_item`](#mainwp_users_help_item) - Action: mainwp_users_help_item
- [`mainwp_before_htaccess_section`](#mainwp_before_htaccess_section) - Action: mainwp_before_htaccess_section
- [`mainwp_after_htaccess_section`](#mainwp_after_htaccess_section) - Action: mainwp_after_htaccess_section
- [`mainwp_user_action`](#mainwp_user_action) - Fires immediately after new user action.
- [`mainwp_user_action`](#mainwp_user_action) - Fires immediately after update admin password action.
- [`mainwp_disable_rest_api_access_log`](#mainwp_disable_rest_api_access_log) - This filter enables the exclusion of the most recent access time from being logged for REST API calls.
- [`mainwp_currentusercan`](#mainwp_currentusercan) - Method \mainwp_current_user_can()
- [`mainwp_currentuserallowedaccesssites`](#mainwp_currentuserallowedaccesssites) - Filter: mainwp_currentuserallowedaccesssites
- [`mainwp_alter_login_user`](#mainwp_alter_login_user) - Filter: mainwp_alter_login_user
- [`mainwp_alter_login_user`](#mainwp_alter_login_user) - This filter is documented in ../class/class-mainwp-connect.php
- [`mainwp_module_log_get_role_list_separator`](#mainwp_module_log_get_role_list_separator) - Tries to find a label for the record's user_role.
- [`mainwp_admin_users_table_fatures`](#mainwp_admin_users_table_fatures) - Filter: mainwp_admin_users_table_fatures
- [`mainwp-users-manage-roles`](#mainwp-users-manage-roles) - Renders manage users dashboard.
- [`mainwp_users_manage_roles`](#mainwp_users_manage_roles) - Renders manage users dashboard.
- [`mainwp-users-manage-roles`](#mainwp-users-manage-roles) - Renders Edit Users Modal window.
- [`mainwp_users_manage_roles`](#mainwp_users_manage_roles) - Renders Edit Users Modal window.
- [`mainwp_users_table_fatures`](#mainwp_users_table_fatures) - Renders Users Table.
- [`mainwp_new_user_password_complexity`](#mainwp_new_user_password_complexity) - Filter: mainwp_new_user_password_complexity
- [`mainwp-users-manage-roles`](#mainwp-users-manage-roles) - Renders the Add New user form.
- [`mainwp_users_manage_roles`](#mainwp_users_manage_roles) - Renders the Add New user form.
- [`mainwp-users-manage-roles`](#mainwp-users-manage-roles) - Method do_bulk_add()
- [`mainwp_users_manage_roles`](#mainwp_users_manage_roles) - Method do_bulk_add()

## Hook Details

### `mainwp_admin_pass_before_users_table`

*Action: mainwp_admin_pass_before_users_table*

Fires before the Connected Admin Users mysql_list_tables


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 264](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L264)



### `mainwp_admin_pass_after_users_table`

*Action: mainwp_admin_pass_after_users_table*

Fires after the Connected Admin Users mysql_list_tables


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 309](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L309)



### `mainwp_users_bulk_action`

*Action: mainwp_users_bulk_action*

Adds new Bulk Actions option under on Manage Users.

Suggested HTML Markup:
<option value="Your custom value">Your custom label</option>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 411](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L411)



### `mainwp_users_actions_bar_left`

*Users actions bar (left)*

Fires at the left side of the actions bar on the Users screen, after the Bulk Actions menu.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 426](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L426)



### `mainwp_users_actions_bar_right`

*Users actions bar (right)*

Fires at the right side of the actions bar on the Users screen.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 438](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L438)



### `mainwp_manage_users_sidebar_top`

*Action: mainwp_manage_users_sidebar_top*

Fires on top of the sidebar on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 474](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L474)



### `mainwp_manage_users_before_select_sites`

*Action: mainwp_manage_users_before_select_sites*

Fires before the Select Sites section on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 485](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L485)



### `mainwp_manage_users_after_select_sites`

*Action: mainwp_manage_users_after_select_sites*

Fires after the Select Sites section on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 508](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L508)



### `mainwp_manage_users_before_search_options`

*Action: mainwp_manage_users_before_search_options*

Fires before the Search Options section on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 538](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L538)



### `mainwp_manage_users_after_search_options`

*Action: mainwp_manage_users_after_search_options*

Fires after the Search Options section on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 565](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L565)



### `mainwp_manage_users_before_submit_button`

*Action: mainwp_manage_users_before_submit_button*

Fires before the Submit Button on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 584](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L584)



### `mainwp_manage_users_after_submit_button`

*Action: mainwp_manage_users_after_submit_button*

Fires after the Submit Button on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 595](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L595)



### `mainwp_manage_users_sidebar_bottom`

*Action: mainwp_manage_users_sidebar_bottom*

Fires at the bottom of the sidebar on Manage Users page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 606](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L606)



### `mainwp_before_users_table`

*Action: mainwp_before_users_table*

Fires before the User table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 819](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L819)



### `mainwp_users_table_header`

*Renders Users Table.*


Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 805](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L805)



### `mainwp_after_users_table`

*Action: mainwp_after_users_table*

Fires after the User table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 853](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L853)



### `mainwp_users_table_column`

*Renders Search results.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user` |  | 
`$website` | `object` | Object containing the child site info.

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1207](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1207)



### `mainwp_users_table_action`

*Action: mainwp_users_table_action*

Adds a new item in the Actions menu in Manage Users table.

Suggested HTML markup:
<a class="item" href="Your custom URL">Your custom label</a>

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user` | `array` | Array containing the user data.
`$website` | `array` | Object containing the website data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1257](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1257)



### `mainwp_before_user_action`

*Action: mainwp_before_user_action*

Fires before user edit/delete/update_user/update_password actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pAction` |  | 
`$userId` |  | 
`$extra` |  | 
`$pass` |  | 
`$optimize` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1415](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1415)



### `mainwp_user_action`

*Fires immediately after user action.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$pAction` |  | 
`$data` |  | 
`$extra` |  | 
`$optimize` |  | 

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1440](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1440)



### `mainwp_after_user_action`

*Action: mainwp_after_user_action*

Fires after user edit/delete/update_user/update_password actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$pAction` |  | 
`$userId` |  | 
`$extra` |  | 
`$pass` |  | 
`$optimize` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1451](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1451)



### `mainwp_before_new_user_form`

*Action: mainwp_before_new_user_form*

Fires before the Add New user form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1499](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1499)



### `mainwp_before_new_user_form_fields`

*Action: mainwp_before_new_user_form_fields*

Fires before the Add New user form fields.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1521](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1521)



### `mainwp_after_new_user_form_fields`

*Action: mainwp_after_new_user_form_fields*

Fires after the Add New user form fields.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1621](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1621)



### `mainwp_add_new_user_sidebar_top`

*Action: mainwp_add_new_user_sidebar_top*

Fires at the top of the sidebar on Add New user page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1634](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1634)



### `mainwp_add_new_user_before_select_sites`

*Action: mainwp_add_new_user_before_select_sites*

Fires before the Select Sites section on the Add New user page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1645](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1645)



### `mainwp_add_new_user_after_select_sites`

*Action: mainwp_add_new_user_after_select_sites*

Fires after the Select Sites section on the Add New user page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1664](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1664)



### `mainwp_add_new_user_before_submit_button`

*Action: mainwp_add_new_user_before_submit_button*

Fires before the Submit button on the Add New user page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1677](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1677)



### `mainwp_add_new_user_after_submit_button`

*Action: mainwp_add_new_user_after_submit_button*

Fires after the Submit button on the Add New user page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1694](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1694)



### `mainwp_add_new_user_sidebar_bottom`

*Action: mainwp_add_new_user_sidebar_bottom*

Fires at the bottom of the sidebar on Add New user page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1705](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1705)



### `mainwp_after_new_user_form`

*Action: mainwp_after_new_user_form*

Fires after the Add New user form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1718](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1718)



### `mainwp_before_import_users`

*Action: mainwp_before_import_users*

Fires above the Import Users section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1773](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1773)



### `mainwp_after_import_users`

*Action: mainwp_after_import_users*

Fires under the Import Users section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1813](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1813)



### `mainwp_before_user_create`

*Action: mainwp_before_user_create*

Fires before user create.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 
`$dbwebsites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1952](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1952)



### `mainwp_after_user_create`

*Action: mainwp_after_user_create*

Fires after user create.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output` |  | 
`$post_data` |  | 
`$dbwebsites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1972](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1972)



### `mainwp_import_users_modal_top`

*Action: mainwp_import_users_modal_top*

Fires on the top of the Import Users modal.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 2099](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L2099)



### `mainwp_import_users_modal_bottom`

*Action: mainwp_import_users_modal_bottom*

Fires on the bottom of the Import Users modal.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 2120](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L2120)



### `mainwp_before_user_create`

*Action: mainwp_before_user_create*

Fires before user create.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 
`$dbwebsites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 2278](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L2278)



### `mainwp_after_user_create`

*Action: mainwp_after_user_create*

Fires after user create.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output` |  | 
`$post_data` |  | 
`$dbwebsites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 2298](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L2298)



### `mainwp_users_help_item`

*Action: mainwp_users_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Users page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 2359](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L2359)



### `mainwp_before_htaccess_section`

*Action: mainwp_before_htaccess_section*

Fires before the .htaccess file section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1867](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1867)



### `mainwp_after_htaccess_section`

*Action: mainwp_after_htaccess_section*

Fires after the .htaccess file section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1890](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1890)



### `mainwp_user_action`

*Fires immediately after new user action.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`'created'` |  | 
`$data` |  | 

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [pages/page-mainwp-bulk-add.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-add.php), [line 62](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-add.php#L62)



### `mainwp_user_action`

*Fires immediately after update admin password action.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`'newadminpassword'` |  | 
`$data` |  | 

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [pages/page-mainwp-bulk-add.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-add.php), [line 72](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-add.php#L72)



### `mainwp_disable_rest_api_access_log`

*This filter enables the exclusion of the most recent access time from being logged for REST API calls.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$this->user->key_id` |  | 
`$this->user->user_id` |  | 

**Changelog**

Version | Description
------- | -----------
`5.1.1` | 

Source: [includes/rest-api/class-mainwp-rest-authentication.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-authentication.php), [line 790](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/class-mainwp-rest-authentication.php#L790)



### `mainwp_currentusercan`

*Method \mainwp_current_user_can()*

Check permission level by hook mainwp_currentusercan of Team Control extension.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$cap_type` | `string` | group or type of capabilities.
`$cap` | `string` | capabilities for current user.

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 612](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L612)



### `mainwp_currentuserallowedaccesssites`

*Filter: mainwp_currentuserallowedaccesssites*

Filters allowed sites for the current user.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'all'` |  | 

Source: [class/class-mainwp-db.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php), [line 1892](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-db.php#L1892)



### `mainwp_alter_login_user`

*Filter: mainwp_alter_login_user*

Filters users accounts so it allows you user to jump to child site under alternative administrator account.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$current_user->ID` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 440](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L440)



### `mainwp_alter_login_user`

*This filter is documented in ../class/class-mainwp-connect.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website->id` |  | 
`$current_user->ID` |  | 

Source: [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 611](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L611)



### `mainwp_module_log_get_role_list_separator`

*Tries to find a label for the record's user_role.*

If the user_role exists, use the label associated with it.

Otherwise, if there is a user role label stored as Log meta then use that.
Otherwise, if the user exists, use the label associated with their current role.
Otherwise, use the role slug as the label.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`' - '` |  | 

Source: [modules/logs/classes/class-log-author.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php), [line 155](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-author.php#L155)



### `mainwp_admin_users_table_fatures`

*Filter: mainwp_admin_users_table_fatures*

Filters Admin Users table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 326](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L326)



### `mainwp-users-manage-roles`

*Renders manage users dashboard.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($user_roles)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_users_manage_roles'` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 368](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L368)



### `mainwp_users_manage_roles`

*Renders manage users dashboard.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user_roles` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 368](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L368)



### `mainwp-users-manage-roles`

*Renders Edit Users Modal window.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($editable_roles)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_users_manage_roles'` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 661](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L661)



### `mainwp_users_manage_roles`

*Renders Edit Users Modal window.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$editable_roles` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 661](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L661)



### `mainwp_users_table_fatures`

*Renders Users Table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 805](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L805)



### `mainwp_new_user_password_complexity`

*Filter: mainwp_new_user_password_complexity*

Filters the Password lenght for the Add New user, Password field.

Since 4.1

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'24'` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1486](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1486)



### `mainwp-users-manage-roles`

*Renders the Add New user form.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($user_roles)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_users_manage_roles'` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1481](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1481)



### `mainwp_users_manage_roles`

*Renders the Add New user form.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$user_roles` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1481](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1481)



### `mainwp-users-manage-roles`

*Method do_bulk_add()*

Bulk User addition $_POST Handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($cus_roles)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_users_manage_roles'` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1826](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1826)



### `mainwp_users_manage_roles`

*Method do_bulk_add()*

Bulk User addition $_POST Handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cus_roles` |  | 

Source: [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 1826](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L1826)




# Content Management Actions

Hooks for managing posts, pages, comments, and other content.

## Navigation

- [Back to All Actions](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`add_meta_boxes`](#add-meta-boxes) - Edit bulkpost metaboxes
- [`admin_post_thumbnail_size`](#admin-post-thumbnail-size) - Filters the size used to display the post thumbnail image in the 'Featured Image' meta box.
- [`mainwp-after-posting-bulkpage-result`](#mainwp-after-posting-bulkpage-result) - After posting a new page
- [`mainwp-after-posting-bulkpost-result`](#mainwp-after-posting-bulkpost-result) - After posting a new post
- [`mainwp-bulkposting-done`](#mainwp-bulkposting-done) - Method posting_posts()
- [`mainwp-getcustompage-backups`](#mainwp-getcustompage-backups) - Backups Subpages
- [`mainwp-getsubpages-backups`](#mainwp-getsubpages-backups) - Instantiate Legacy Backups Menu.
- [`mainwp-getsubpages-page`](#mainwp-getsubpages-page) - Method init_menu()
- [`mainwp-getsubpages-post`](#mainwp-getsubpages-post) - Method ini_menu()
- [`mainwp-getsubpages-server`](#mainwp-getsubpages-server) - Filter mainwp_getsubpages_server
- [`mainwp-getsubpages-settings`](#mainwp-getsubpages-settings) - Settings Subpages
- [`mainwp-getsubpages-sites`](#mainwp-getsubpages-sites) - Initiate menu.
- [`mainwp-getsubpages-user`](#mainwp-getsubpages-user) - This hook allows you to add extra sub pages to the User page via the 'mainwp-getsubpages-user' filter.
- [`mainwp-post-posting-page`](#mainwp-post-posting-page) - Method posting()
- [`mainwp-post-posting-post`](#mainwp-post-posting-post) - Method posting_posts()
- [`mainwp-pre-posting-posts`](#mainwp-pre-posting-posts) - Filter is being replaced with mainwp_pre_posting_posts.
- [`mainwp-wordfence-sites`](#mainwp-wordfence-sites) - Method render_scan_site()
- [`mainwp_admin_footer`](#mainwp-admin-footer) - Action: mainwp_admin_footer
- [`mainwp_admin_pass_after_pass_form`](#mainwp-admin-pass-after-pass-form) - Action: mainwp_admin_pass_after_pass_form
- [`mainwp_admin_pass_after_select_sites`](#mainwp-admin-pass-after-select-sites) - Action: mainwp_admin_pass_after_select_sites
- [`mainwp_admin_pass_after_submit_button`](#mainwp-admin-pass-after-submit-button) - Action: mainwp_admin_pass_after_submit_button
- [`mainwp_admin_pass_before_pass_form`](#mainwp-admin-pass-before-pass-form) - Action: mainwp_admin_pass_before_pass_form
- [`mainwp_admin_pass_before_select_sites`](#mainwp-admin-pass-before-select-sites) - Action: mainwp_admin_pass_before_select_sites
- [`mainwp_admin_pass_before_submit_button`](#mainwp-admin-pass-before-submit-button) - Action: mainwp_admin_pass_before_submit_button
- [`mainwp_admin_pass_sidebar_bottom`](#mainwp-admin-pass-sidebar-bottom) - Action: mainwp_admin_pass_sidebar_bottom
- [`mainwp_admin_pass_sidebar_top`](#mainwp-admin-pass-sidebar-top) - Action: mainwp_admin_pass_sidebar_top
- [`mainwp_admin_post_thumbnail_html`](#mainwp-admin-post-thumbnail-html) - Filters the admin post thumbnail HTML markup to return.
- [`mainwp_after_pages_table`](#mainwp-after-pages-table) - Action: mainwp_after_pages_table
- [`mainwp_after_post_action`](#mainwp-after-post-action) - **Arguments**
- [`mainwp_after_posting_bulkpage_result`](#mainwp-after-posting-bulkpage-result) - Method posting()
- [`mainwp_after_posting_bulkpost_result`](#mainwp-after-posting-bulkpost-result) - Method posting_posts()
- [`mainwp_after_posting_delete_bulk_post`](#mainwp-after-posting-delete-bulk-post) - Method posting_posts()
- [`mainwp_after_posts_table`](#mainwp-after-posts-table) - Action: mainwp_after_posts_table
- [`mainwp_before_bulkpost_editor`](#mainwp-before-bulkpost-editor) - Renders bulkpost to edit.
- [`mainwp_before_mainwp_content_wrap`](#mainwp-before-mainwp-content-wrap) - Action: mainwp_before_mainwp_content_wrap
- [`mainwp_before_pages_table`](#mainwp-before-pages-table) - Action: mainwp_before_pages_table
- [`mainwp_before_post_action`](#mainwp-before-post-action) - Action: mainwp_before_post_action
- [`mainwp_before_posts_table`](#mainwp-before-posts-table) - Action: mainwp_before_posts_table
- [`mainwp_before_redirect_posting_bulkpage`](#mainwp-before-redirect-posting-bulkpage) - Action: mainwp_before_redirect_posting_bulkpage
- [`mainwp_before_redirect_posting_bulkpost`](#mainwp-before-redirect-posting-bulkpost) - Action: mainwp_before_redirect_posting_bulkpost
- [`mainwp_bulkpage_before_post`](#mainwp-bulkpage-before-post) - Before Page post action
- [`mainwp_bulkpage_posting`](#mainwp-bulkpage-posting) - Posting new page
- [`mainwp_bulkpost_before_post`](#mainwp-bulkpost-before-post) - Before Post post action
- [`mainwp_bulkpost_categories_handle`](#mainwp-bulkpost-categories-handle) - Method add_categories_handle()
- [`mainwp_bulkpost_edit`](#mainwp-bulkpost-edit) - Edit bulkpost
- [`mainwp_bulkpost_edit_title`](#mainwp-bulkpost-edit-title) - Renders bulkpost to edit.
- [`mainwp_bulkpost_edit_top_side`](#mainwp-bulkpost-edit-top-side) - Renders bulkpost to edit.
- [`mainwp_bulkpost_editor_settings`](#mainwp-bulkpost-editor-settings) - Renders bulkpost to edit.
- [`mainwp_bulkpost_tags_handle`](#mainwp-bulkpost-tags-handle) - Method add_tags_handle()
- [`mainwp_bulkposting_done`](#mainwp-bulkposting-done) - Posting post completed
- [`mainwp_cards_per_row`](#mainwp-cards-per-row) - Filter: mainwp_cards_per_row
- [`mainwp_client_report_generate_content`](#mainwp-client-report-generate-content) - Filter: mainwp_client_report_generate_content
- [`mainwp_custom_post_types_default`](#mainwp-custom-post-types-default) - Default post types
- [`mainwp_custom_render_bulkpost`](#mainwp-custom-render-bulkpost) - Renders bulkpost to edit.
- [`mainwp_daily_digest_content`](#mainwp-daily-digest-content) - Filter: mainwp_daily_digest_content
- [`mainwp_edit_bulkpost_getmetaboxes`](#mainwp-edit-bulkpost-getmetaboxes) - Init custom bulkpost metaboxes.
- [`mainwp_edit_post_get_categories`](#mainwp-edit-post-get-categories) - Method ajax_handle_get_categories()
- [`mainwp_edit_posts_after_submit_button`](#mainwp-edit-posts-after-submit-button) - Action: mainwp_edit_posts_after_submit_button
- [`mainwp_edit_posts_before_submit_button`](#mainwp-edit-posts-before-submit-button) - Action: mainwp_edit_posts_before_submit_button
- [`mainwp_enqueue_script_gridster`](#mainwp-enqueue-script-gridster) - Method admin_init()
- [`mainwp_escape_content`](#mainwp-escape-content) - Edit subscription Post
- [`mainwp_extensions_page_top_header`](#mainwp-extensions-page-top-header) - Method render_header()
- [`mainwp_get_all_pages_data`](#mainwp-get-all-pages-data) - Get all pages data
- [`mainwp_get_all_posts_data`](#mainwp-get-all-posts-data) - Get all posts data
- [`mainwp_get_post_data_authed`](#mainwp-get-post-data-authed) - Method get_post_data_authed()
- [`mainwp_getcustompage_backups`](#mainwp-getcustompage-backups) - Instantiate Legacy Backups Menu.
- [`mainwp_getsubpages_api_backups`](#mainwp-getsubpages-api-backups) - This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.
- [`mainwp_getsubpages_backups`](#mainwp-getsubpages-backups) - Instantiate Legacy Backups Menu.
- [`mainwp_getsubpages_client`](#mainwp-getsubpages-client) - Method init_menu()
- [`mainwp_getsubpages_cost_tracker`](#mainwp-getsubpages-cost-tracker) - This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.
- [`mainwp_getsubpages_page`](#mainwp-getsubpages-page) - Method init_menu()
- [`mainwp_getsubpages_post`](#mainwp-getsubpages-post) - Method ini_menu()
- [`mainwp_getsubpages_restapi`](#mainwp-getsubpages-restapi) - REST API Subpages
- [`mainwp_getsubpages_server`](#mainwp-getsubpages-server) - Method init_menu()
- [`mainwp_getsubpages_settings`](#mainwp-getsubpages-settings) - Instantiate the Settings Menu.
- [`mainwp_getsubpages_sites`](#mainwp-getsubpages-sites) - Initiate menu.
- [`mainwp_getsubpages_tags`](#mainwp-getsubpages-tags) - This hook allows you to add extra sub pages to the Tags page via the 'mainwp-getsubpages-tags' filter.
- [`mainwp_getsubpages_user`](#mainwp-getsubpages-user) - Method init_menu()
- [`mainwp_header_left`](#mainwp-header-left) - Filter: mainwp_header_left
- [`mainwp_header_right`](#mainwp-header-right) - Filter: mainwp_header_right
- [`mainwp_header_title`](#mainwp-header-title) - Filter: mainwp_header_title
- [`mainwp_help_sidebar_content`](#mainwp-help-sidebar-content) - Action: mainwp_help_sidebar_content
- [`mainwp_info_schedules_cron_listing`](#mainwp-info-schedules-cron-listing) - Renders the Cron Schedule page.
- [`mainwp_log_specific_actions`](#mainwp-log-specific-actions) - Renders action logs page.
- [`mainwp_logger_to_db`](#mainwp-logger-to-db) - Renders action logs page.
- [`mainwp_manage_pages_action_item`](#mainwp-manage-pages-action-item) - Method pages_search_handler()
- [`mainwp_manage_pages_after_search_options`](#mainwp-manage-pages-after-search-options) - Action: mainwp_manage_pages_after_search_options
- [`mainwp_manage_pages_after_select_sites`](#mainwp-manage-pages-after-select-sites) - Action: mainwp_manage_pages_after_select_sites
- [`mainwp_manage_pages_after_submit_button`](#mainwp-manage-pages-after-submit-button) - Action: mainwp_manage_pages_after_submit_button
- [`mainwp_manage_pages_before_search_options`](#mainwp-manage-pages-before-search-options) - Action: mainwp_manage_pages_before_search_options
- [`mainwp_manage_pages_before_select_sites`](#mainwp-manage-pages-before-select-sites) - Action: mainwp_manage_pages_before_select_sites
- [`mainwp_manage_pages_before_submit_button`](#mainwp-manage-pages-before-submit-button) - Action: mainwp_manage_pages_before_submit_button
- [`mainwp_manage_pages_bulk_action`](#mainwp-manage-pages-bulk-action) - Renders Bulk Page Manager.
- [`mainwp_manage_pages_sidebar_bottom`](#mainwp-manage-pages-sidebar-bottom) - Action: mainwp_manage_pages_sidebar_bottom
- [`mainwp_manage_pages_sidebar_top`](#mainwp-manage-pages-sidebar-top) - Action: mainwp_manage_pages_sidebar_top
- [`mainwp_manage_posts_action_item`](#mainwp-manage-posts-action-item) - Method posts_search_handler()
- [`mainwp_manage_posts_after_search_options`](#mainwp-manage-posts-after-search-options) - Action: mainwp_manage_posts_after_search_options
- [`mainwp_manage_posts_after_select_sites`](#mainwp-manage-posts-after-select-sites) - Action: mainwp_manage_posts_after_select_sites
- [`mainwp_manage_posts_after_submit_button`](#mainwp-manage-posts-after-submit-button) - Action: mainwp_manage_posts_after_submit_button
- [`mainwp_manage_posts_before_search_options`](#mainwp-manage-posts-before-search-options) - Action: mainwp_manage_posts_before_search_options
- [`mainwp_manage_posts_before_select_sites`](#mainwp-manage-posts-before-select-sites) - Action: mainwp_manage_posts_before_select_sites
- [`mainwp_manage_posts_before_submit_button`](#mainwp-manage-posts-before-submit-button) - Action: mainwp_manage_posts_before_submit_button
- [`mainwp_manage_posts_bulk_action`](#mainwp-manage-posts-bulk-action) - Method render()
- [`mainwp_manage_posts_sidebar_bottom`](#mainwp-manage-posts-sidebar-bottom) - Action: mainwp_manage_posts_sidebar_bottom
- [`mainwp_manage_posts_sidebar_top`](#mainwp-manage-posts-sidebar-top) - Action: mainwp_manage_posts_sidebar_top
- [`mainwp_manageposts_get_post_result`](#mainwp-manageposts-get-post-result) - Method get_post()
- [`mainwp_module_cost_tracker_help_item`](#mainwp-module-cost-tracker-help-item) - Action: mainwp_module_cost_tracker_help_item
- [`mainwp_overview_help_item`](#mainwp-overview-help-item) - Action: mainwp_overview_help_item
- [`mainwp_page_admin_body_class`](#mainwp-page-admin-body-class) - MainWP Admin body CSS class attributes.
- [`mainwp_page_navigation`](#mainwp-page-navigation) - Filter: mainwp_page_navigation
- [`mainwp_page_navigation_menu`](#mainwp-page-navigation-menu) - Method render_page_navigation()
- [`mainwp_pagefooter_extensions`](#mainwp-pagefooter-extensions) - Method render_extensions_groups()
- [`mainwp_pagefooter_settings`](#mainwp-pagefooter-settings) - Render settings
- [`mainwp_pagefooter_sites`](#mainwp-pagefooter-sites) - Render Tabs.
- [`mainwp_pagefooter_tags`](#mainwp-pagefooter-tags) - Sites Page Footer
- [`mainwp_pageheader_extensions`](#mainwp-pageheader-extensions) - Method render_extensions_groups()
- [`mainwp_pageheader_settings`](#mainwp-pageheader-settings) - Render settings
- [`mainwp_pageheader_sites`](#mainwp-pageheader-sites) - Render Tabs.
- [`mainwp_pageheader_tags`](#mainwp-pageheader-tags) - Sites Page header
- [`mainwp_pages_actions_bar_left`](#mainwp-pages-actions-bar-left) - Action: mainwp_pages_actions_bar_left
- [`mainwp_pages_actions_bar_right`](#mainwp-pages-actions-bar-right) - Action: mainwp_pages_actions_bar_right
- [`mainwp_pages_bulk_action`](#mainwp-pages-bulk-action) - Action: mainwp_pages_bulk_action
- [`mainwp_pages_help_item`](#mainwp-pages-help-item) - Action: mainwp_pages_help_item
- [`mainwp_pages_posting_popup_actions`](#mainwp-pages-posting-popup-actions) - Method posting()
- [`mainwp_pages_table_action`](#mainwp-pages-table-action) - Action: mainwp_pages_table_action
- [`mainwp_pages_table_column`](#mainwp-pages-table-column) - Action: mainwp_pages_table_column
- [`mainwp_pages_table_fatures`](#mainwp-pages-table-fatures) - Filter: mainwp_pages_table_fatures
- [`mainwp_pages_table_header`](#mainwp-pages-table-header) - Action: mainwp_pages_table_header
- [`mainwp_post_action`](#mainwp-post-action) - Fires immediately after post action.
- [`mainwp_post_created`](#mainwp-post-created) - Method posting_bulk_handler()
- [`mainwp_post_posting_page`](#mainwp-post-posting-page) - Posting page
- [`mainwp_post_posting_post`](#mainwp-post-posting-post) - Posting post
- [`mainwp_posting_bulkpost_post_status`](#mainwp-posting-bulkpost-post-status) - Post status
- [`mainwp_posting_post_selected_by`](#mainwp-posting-post-selected-by) - Method posting_posts()
- [`mainwp_posting_post_selected_sites`](#mainwp-posting-post-selected-sites) - Method posting_posts()
- [`mainwp_posting_selected_clients`](#mainwp-posting-selected-clients) - Method posting_posts()
- [`mainwp_postprocess_backup_site`](#mainwp-postprocess-backup-site) - Method  backup_site()
- [`mainwp_posts_actions_bar_left`](#mainwp-posts-actions-bar-left) - Action: mainwp_posts_actions_bar_left
- [`mainwp_posts_actions_bar_right`](#mainwp-posts-actions-bar-right) - Action: mainwp_posts_actions_bar_right
- [`mainwp_posts_bulk_action`](#mainwp-posts-bulk-action) - Action: mainwp_posts_bulk_action
- [`mainwp_posts_help_item`](#mainwp-posts-help-item) - Action: mainwp_posts_help_item
- [`mainwp_posts_posting_bulk_sites`](#mainwp-posts-posting-bulk-sites) - Method posting_bulk()
- [`mainwp_posts_posting_popup_actions`](#mainwp-posts-posting-popup-actions) - Method posting()
- [`mainwp_posts_search_bulk_sites`](#mainwp-posts-search-bulk-sites) - Method render()
- [`mainwp_posts_table_action`](#mainwp-posts-table-action) - Action: mainwp_posts_table_action
- [`mainwp_posts_table_column`](#mainwp-posts-table-column) - Action: mainwp_posts_table_column
- [`mainwp_posts_table_fatures`](#mainwp-posts-table-fatures) - Filter: mainwp_posts_table_fatures
- [`mainwp_posts_table_header`](#mainwp-posts-table-header) - Action: mainwp_posts_table_header
- [`mainwp_pre_fetch_authed_data`](#mainwp-pre-fetch-authed-data) - Method get_post_data_authed()
- [`mainwp_pre_posting_posts`](#mainwp-pre-posting-posts) - Filter: mainwp_pre_posting_posts
- [`mainwp_pro_reports_generate_content`](#mainwp-pro-reports-generate-content) - Filter: mainwp_pro_reports_generate_content
- [`mainwp_recent_pages_after_draft_list`](#mainwp-recent-pages-after-draft-list) - Action: mainwp_recent_pages_after_draft_list
- [`mainwp_recent_pages_after_future_list`](#mainwp-recent-pages-after-future-list) - Action: mainwp_recent_pages_after_future_list
- [`mainwp_recent_pages_after_lists`](#mainwp-recent-pages-after-lists) - Action: mainwp_recent_pages_after_lists
- [`mainwp_recent_pages_after_pending_list`](#mainwp-recent-pages-after-pending-list) - Action: mainwp_recent_pages_after_pending_list
- [`mainwp_recent_pages_after_publised_list`](#mainwp-recent-pages-after-publised-list) - Action: mainwp_recent_pages_after_publised_list
- [`mainwp_recent_pages_after_trash_list`](#mainwp-recent-pages-after-trash-list) - Action: mainwp_recent_pages_after_trash_list
- [`mainwp_recent_pages_before_draft_list`](#mainwp-recent-pages-before-draft-list) - Action: mainwp_recent_pages_before_draft_list
- [`mainwp_recent_pages_before_future_list`](#mainwp-recent-pages-before-future-list) - Action: mainwp_recent_pages_before_future_list
- [`mainwp_recent_pages_before_pending_list`](#mainwp-recent-pages-before-pending-list) - Action: mainwp_recent_pages_before_pending_list
- [`mainwp_recent_pages_before_publised_list`](#mainwp-recent-pages-before-publised-list) - Action: mainwp_recent_pages_before_publised_list
- [`mainwp_recent_pages_before_trash_list`](#mainwp-recent-pages-before-trash-list) - Action: mainwp_recent_pages_before_trash_list
- [`mainwp_recent_pages_widget_bottom`](#mainwp-recent-pages-widget-bottom) - Action: mainwp_recent_pages_widget_bottom
- [`mainwp_recent_pages_widget_title`](#mainwp-recent-pages-widget-title) - *Arguments*
- [`mainwp_recent_pages_widget_top`](#mainwp-recent-pages-widget-top) - Action: mainwp_recent_pages_widget_top
- [`mainwp_recent_posts_after_draft_list`](#mainwp-recent-posts-after-draft-list) - Action: mainwp_recent_posts_after_draft_list
- [`mainwp_recent_posts_after_future_list`](#mainwp-recent-posts-after-future-list) - Action: mainwp_recent_posts_after_future_list
- [`mainwp_recent_posts_after_lists`](#mainwp-recent-posts-after-lists) - Action: mainwp_recent_posts_after_lists
- [`mainwp_recent_posts_after_pending_list`](#mainwp-recent-posts-after-pending-list) - Action: mainwp_recent_posts_after_pending_list
- [`mainwp_recent_posts_after_publised_list`](#mainwp-recent-posts-after-publised-list) - Action: mainwp_recent_posts_after_publised_list
- [`mainwp_recent_posts_after_trash_list`](#mainwp-recent-posts-after-trash-list) - Action: mainwp_recent_posts_after_trash_list
- [`mainwp_recent_posts_before_draft_list`](#mainwp-recent-posts-before-draft-list) - Action: mainwp_recent_posts_before_draft_list
- [`mainwp_recent_posts_before_future_list`](#mainwp-recent-posts-before-future-list) - Action: mainwp_recent_posts_before_future_list
- [`mainwp_recent_posts_before_pending_list`](#mainwp-recent-posts-before-pending-list) - Action: mainwp_recent_posts_before_pending_list
- [`mainwp_recent_posts_before_publised_list`](#mainwp-recent-posts-before-publised-list) - Action: mainwp_recent_posts_before_publised_list
- [`mainwp_recent_posts_before_trash_list`](#mainwp-recent-posts-before-trash-list) - Action: mainwp_recent_posts_before_trash_list
- [`mainwp_recent_posts_pages_number`](#mainwp-recent-posts-pages-number) - This filter is documented in ../widgets/widget-mainwp-recent-posts.php
- [`mainwp_recent_posts_widget_bottom`](#mainwp-recent-posts-widget-bottom) - Action: mainwp_recent_posts_widget_bottom
- [`mainwp_recent_posts_widget_title`](#mainwp-recent-posts-widget-title) - *Arguments*
- [`mainwp_recent_posts_widget_top`](#mainwp-recent-posts-widget-top) - Action: mainwp_recent_posts_widget_top
- [`mainwp_register_post_type`](#mainwp-register-post-type) - Method create_post_type()
- [`mainwp_save_bulkpage`](#mainwp-save-bulkpage) - Action: mainwp_save_bulkpage
- [`mainwp_save_bulkpost`](#mainwp-save-bulkpost) - Action: mainwp_save_bulkpost
- [`mainwp_security_post_data`](#mainwp-security-post-data) - Filters security issues from fixing
- [`mainwp_show_qsw`](#mainwp-show-qsw) - Render MainWP Tools SubPage.
- [`mainwp_sidbar_pages`](#mainwp-sidbar-pages) - Method render_header_actions()
- [`mainwp_sidebar_pages`](#mainwp-sidebar-pages) - Method render_header_actions()
- [`mainwp_specific_action_logs`](#mainwp-specific-action-logs) - Renders action logs page.
- [`mainwp_subpages_left_menu`](#mainwp-subpages-left-menu) - Method init_subpages_left_menu
- [`mainwp_tags_help_item`](#mainwp-tags-help-item) - Action: mainwp_tags_help_item
- [`mainwp_top_bulkpost_edit_content`](#mainwp-top-bulkpost-edit-content) - Renders bulkpost to edit.
- [`mainwp_wordfence_sites`](#mainwp-wordfence-sites) - Action: mainwp_wordfence_sites
- [`postmeta_form_keys`](#postmeta-form-keys) - Filters values for the meta key dropdown in the Custom Fields meta box.
- [`postmeta_form_limit`](#postmeta-form-limit) - **Arguments**
- [`redirect_post_location`](#redirect-post-location) - Filter: redirect_post_location

---

## Hook Details

<a id='add-meta-boxes'></a>
### `add_meta_boxes`

* Edit bulkpost metaboxes

Fires after all built-in meta boxes have been added.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_type` | `string` | Post type.
`$post` | `object` | Object containing the Post data.

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2247](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2247)

---

<a id='admin-post-thumbnail-size'></a>
### `admin_post_thumbnail_size`

* Filters the size used to display the post thumbnail image in the 'Featured Image' meta box.

Note: When a theme adds 'post-thumbnail' support, a special 'post-thumbnail'
image size is registered, which differs from the 'thumbnail' image size
managed via the Settings > Media screen. See the `$size` parameter description
for more information on default values.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$size` | `string\|array` | Post thumbnail image size to display in the meta box. Accepts any valid<br>image size, or an array of width and height values in pixels (in that order).<br>If the 'post-thumbnail' size is set, default is 'post-thumbnail'. Otherwise,<br>default is an array with 266 as both the height and width values.
`$thumbnail_id` | `int` | Post thumbnail attachment ID.
`$_post` | `\MainWP\Dashboard\WP_Post` | The post object associated with the thumbnail.

**Changelog**

Version | Description
------- | -----------
`4.4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1704](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1704)

---

<a id='mainwp-after-posting-bulkpage-result'></a>
### `mainwp-after-posting-bulkpage-result`

* After posting a new page

Sets data after the posting process to show the process feedback.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false, $_post, $dbwebsites, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_after_posting_bulkpage_result'` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1650](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1650)

---

<a id='mainwp-after-posting-bulkpost-result'></a>
### `mainwp-after-posting-bulkpost-result`

* After posting a new post

Sets data after the posting process to show the process feedback.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false, $_post, $dbwebsites, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_after_posting_bulkpost_result'` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 850](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L850)

---

<a id='mainwp-bulkposting-done'></a>
### `mainwp-bulkposting-done`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($_post, $website, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_bulkposting_done'` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1385](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1385)
- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-getcustompage-backups'></a>
### `mainwp-getcustompage-backups`

* Backups Subpages

Filters subpages for the Backups page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getcustompage_backups'` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 102](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L102)

---

<a id='mainwp-getsubpages-backups'></a>
### `mainwp-getsubpages-backups`

* Instantiate Legacy Backups Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_backups'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_backups'` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 90](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L90)

---

<a id='mainwp-getsubpages-page'></a>
### `mainwp-getsubpages-page`

* Method init_menu()

Initiate Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_page'` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 81](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L81)

---

<a id='mainwp-getsubpages-post'></a>
### `mainwp-getsubpages-post`

* Method ini_menu()

Initiate Page menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_post'` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 78](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L78)

---

<a id='mainwp-getsubpages-server'></a>
### `mainwp-getsubpages-server`

* Filter mainwp_getsubpages_server

Filters subpages for the Info page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_server'` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 141](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L141)

---

<a id='mainwp-getsubpages-settings'></a>
### `mainwp-getsubpages-settings`

* Settings Subpages

Filters subpages for the Settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_settings'` |  |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 211](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L211)

---

<a id='mainwp-getsubpages-sites'></a>
### `mainwp-getsubpages-sites`

* Initiate menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_sites'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_sites'` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 178](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L178)

---

<a id='mainwp-getsubpages-user'></a>
### `mainwp-getsubpages-user`

* This hook allows you to add extra sub pages to the User page via the 'mainwp-getsubpages-user' filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_user'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_user'` |  |

**Usage Locations:**

- [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 114](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L114)

---

<a id='mainwp-post-posting-page'></a>
### `mainwp-post-posting-page`

* Method posting()

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website, $output->added_id[$website->id], $links)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_post_posting_page'` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1385](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1385)

---

<a id='mainwp-post-posting-post'></a>
### `mainwp-post-posting-post`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website, $output->added_id[$website->id], $links)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_post_posting_post'` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-pre-posting-posts'></a>
### `mainwp-pre-posting-posts`

* Filter is being replaced with mainwp_pre_posting_posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(is_array($params) ? $params : array(), (object) array('id' => $website->id, 'url' => $website->url, 'name' => $website->name))` |  | 
`'4.0.7.2'` |  | 
`// NOSONAR - not IP.
'mainwp_pre_posting_posts'` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(is_array($params) ? $params : array(), (object) array('id' => $website->id, 'url' => $website->url, 'name' => $website->name))` |  | 
`'4.0.7.2'` |  | 
`// NOSONAR - not IP.
'mainwp_pre_posting_posts'` |  |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 784](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L784)

---

<a id='mainwp-wordfence-sites'></a>
### `mainwp-wordfence-sites`

* Method render_scan_site()

Render Site Hardening sub page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_wordfence_sites'` |  |

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 733](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L733)

---

<a id='mainwp-admin-footer'></a>
### `mainwp_admin_footer`

* Action: mainwp_admin_footer

Fires at the bottom of MainWP content.

**Usage Locations:**

- [class/class-mainwp-system-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php), [line 1020](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php#L1020)

---

<a id='mainwp-admin-pass-after-pass-form'></a>
### `mainwp_admin_pass_after_pass_form`

* Action: mainwp_admin_pass_after_pass_form

Fires after the New password form on the Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 423](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L423)

---

<a id='mainwp-admin-pass-after-select-sites'></a>
### `mainwp_admin_pass_after_select_sites`

* Action: mainwp_admin_pass_after_select_sites

Fires after the Select Sites section on the Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 387](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L387)

---

<a id='mainwp-admin-pass-after-submit-button'></a>
### `mainwp_admin_pass_after_submit_button`

* Action: mainwp_admin_pass_after_submit_button

Fires after the Submit button on the Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 452](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L452)

---

<a id='mainwp-admin-pass-before-pass-form'></a>
### `mainwp_admin_pass_before_pass_form`

* Action: mainwp_admin_pass_before_pass_form

Fires before the New password form on the Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 402](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L402)

---

<a id='mainwp-admin-pass-before-select-sites'></a>
### `mainwp_admin_pass_before_select_sites`

* Action: mainwp_admin_pass_before_select_sites

Fires before the Select Sites section on the Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 368](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L368)

---

<a id='mainwp-admin-pass-before-submit-button'></a>
### `mainwp_admin_pass_before_submit_button`

* Action: mainwp_admin_pass_before_submit_button

Fires before the Submit button on the Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 437](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L437)

---

<a id='mainwp-admin-pass-sidebar-bottom'></a>
### `mainwp_admin_pass_sidebar_bottom`

* Action: mainwp_admin_pass_sidebar_bottom

Fires at the bottom of the sidebar on Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 463](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L463)

---

<a id='mainwp-admin-pass-sidebar-top'></a>
### `mainwp_admin_pass_sidebar_top`

* Action: mainwp_admin_pass_sidebar_top

Fires at the top of the sidebar on Admin Passwords page.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 357](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L357)

---

<a id='mainwp-admin-post-thumbnail-html'></a>
### `mainwp_admin_post_thumbnail_html`

* Filters the admin post thumbnail HTML markup to return.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$html` |  | 
`$_post->ID` |  | 
`$thumbnail_id` | `int` | Thumbnail ID.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$html` |  | 
`$_post->ID` |  | 
`$thumbnail_id` | `int` | Thumbnail ID.

**Changelog**

Version | Description
------- | -----------
`4.6.0` | Added the `$thumbnail_id` parameter.
`3.5.0` | Added the `$post_id` parameter.
`2.9.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1761](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1761)

---

<a id='mainwp-after-pages-table'></a>
### `mainwp_after_pages_table`

* Action: mainwp_after_pages_table

Fires after the Manage Pages table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 842](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L842)

---

<a id='mainwp-after-post-action'></a>
### `mainwp_after_post_action`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$type` |  | 
`$pAction` |  | 
`$postId` |  | 
`$website` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$type` |  | 
`$pAction` |  | 
`$postId` |  | 
`$website` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 795](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L795)

---

<a id='mainwp-after-posting-bulkpage-result'></a>
### `mainwp_after_posting_bulkpage_result`

* Method posting()

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$after_posting` |  | 
`$_post` |  | 
`$dbwebsites` |  | 
`$output` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1385](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1385)

---

<a id='mainwp-after-posting-bulkpost-result'></a>
### `mainwp_after_posting_bulkpost_result`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$newExtensions` |  | 
`$_post` |  | 
`$dbwebsites` |  | 
`$output` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-after-posting-delete-bulk-post'></a>
### `mainwp_after_posting_delete_bulk_post`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$posting_succeed` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-after-posts-table'></a>
### `mainwp_after_posts_table`

* Action: mainwp_after_posts_table

Fires after the Manage Posts table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 992](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L992)

---

<a id='mainwp-before-bulkpost-editor'></a>
### `mainwp_before_bulkpost_editor`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-before-mainwp-content-wrap'></a>
### `mainwp_before_mainwp_content_wrap`

* Action: mainwp_before_mainwp_content_wrap

Fires before the #mainwp-content-wrap element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 799](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L799)

---

<a id='mainwp-before-pages-table'></a>
### `mainwp_before_pages_table`

* Action: mainwp_before_pages_table

Fires before the Manage Pages table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 793](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L793)

---

<a id='mainwp-before-post-action'></a>
### `mainwp_before_post_action`

* Action: mainwp_before_post_action

Fires before post/page publish/unpublish/trash/delete/restore actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`$pAction` |  | 
`$postId` |  | 
`$website` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 772](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L772)

---

<a id='mainwp-before-posts-table'></a>
### `mainwp_before_posts_table`

* Action: mainwp_before_posts_table

Fires before the Manage Posts table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 934](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L934)

---

<a id='mainwp-before-redirect-posting-bulkpage'></a>
### `mainwp_before_redirect_posting_bulkpage`

* Action: mainwp_before_redirect_posting_bulkpage

Fires before redirection to posting 'bulk page' page after post submission.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `object` | Object containing post data.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-bulk-post.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php), [line 241](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php#L241)

---

<a id='mainwp-before-redirect-posting-bulkpost'></a>
### `mainwp_before_redirect_posting_bulkpost`

* Action: mainwp_before_redirect_posting_bulkpost

Fires before redirection to posting 'bulk post' page after post submission.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `object` | Object containing post data.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-bulk-post.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php), [line 172](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php#L172)

---

<a id='mainwp-bulkpage-before-post'></a>
### `mainwp_bulkpage_before_post`

* Before Page post action

Fires right before posting the 'bulkpage' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1427](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1427)

---

<a id='mainwp-bulkpage-posting'></a>
### `mainwp_bulkpage_posting`

* Posting new page

Sets Page data to post to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 
`$id` | `int` | Page ID.

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1602](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1602)

---

<a id='mainwp-bulkpost-before-post'></a>
### `mainwp_bulkpost_before_post`

* Before Post post action

Fires right before posting the 'bulkpost' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$p_id` | `int` | Page ID.

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 447](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L447)

---

<a id='mainwp-bulkpost-categories-handle'></a>
### `mainwp_bulkpost_categories_handle`

* Method add_categories_handle()

Handle adding categories.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.
`wp_unslash($_POST['post_category'])` |  |

**Usage Locations:**

- [class/class-mainwp-meta-boxes.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-meta-boxes.php), [line 109](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-meta-boxes.php#L109)

---

<a id='mainwp-bulkpost-edit'></a>
### `mainwp_bulkpost_edit`

* Edit bulkpost

First on the Edit post screen after default fields.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` | `object` | Object containing the Post data.
`$post_type` | `string` | Post type.

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2233](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2233)

---

<a id='mainwp-bulkpost-edit-title'></a>
### `mainwp_bulkpost_edit_title`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note_title` |  | 
`$post` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note_title` |  | 
`$post` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-bulkpost-edit-top-side'></a>
### `mainwp_bulkpost_edit_top_side`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 
`$post_type` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 
`$post_type` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-bulkpost-editor-settings'></a>
### `mainwp_bulkpost_editor_settings`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$post` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$post` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-bulkpost-tags-handle'></a>
### `mainwp_bulkpost_tags_handle`

* Method add_tags_handle()

Add Tags to post array handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.
`$post_type` | `string` | Post type.
`wp_strip_all_tags(wp_unslash($_POST['add_tags']))` |  |

**Usage Locations:**

- [class/class-mainwp-meta-boxes.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-meta-boxes.php), [line 168](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-meta-boxes.php#L168)

---

<a id='mainwp-bulkposting-done'></a>
### `mainwp_bulkposting_done`

* Posting post completed

Fires after the post posting process is completed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `array` | Array containing the post data.
`$website` | `object` | Object containing child site data.
`$output` | `array` | Output data.

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1635](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1635)
- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 835](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L835)

---

<a id='mainwp-cards-per-row'></a>
### `mainwp_cards_per_row`

* Filter: mainwp_cards_per_row

Filters the number of cards per row in MainWP Screenshots page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'five'` |  |

**Changelog**

Version | Description
------- | -----------
`4.1.8` |

**Usage Locations:**

- [pages/page-mainwp-manage-screenshots.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-screenshots.php), [line 247](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-screenshots.php#L247)

---

<a id='mainwp-client-report-generate-content'></a>
### `mainwp_client_report_generate_content`

* Filter: mainwp_client_report_generate_content

Filters the Client Reports available content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$content` |  | 
`$current_email_site->id` |  | 
`$timestamp_from_date` |  | 
`$timestamp_to_date` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 219](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L219)

---

<a id='mainwp-custom-post-types-default'></a>
### `mainwp_custom_post_types_default`

* Default post types

Set default custom post types to exclude from the CPT extension options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 871](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L871)

---

<a id='mainwp-custom-render-bulkpost'></a>
### `mainwp_custom_render_bulkpost`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$post_id` | `mixed` | Post ID.
`$post_type` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$post_id` | `mixed` | Post ID.
`$post_type` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-daily-digest-content'></a>
### `mainwp_daily_digest_content`

* Filter: mainwp_daily_digest_content

Filters the Daily Digest email content and adds support for enabling text/plain emails.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$sites_ids` | `array` | Array of sites IDs.
`$plain_text` | `bool` | Wether plain text mode is enabled.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification.php), [line 210](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification.php#L210)

---

<a id='mainwp-edit-bulkpost-getmetaboxes'></a>
### `mainwp_edit_bulkpost_getmetaboxes`

* Init custom bulkpost metaboxes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 151](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L151)

---

<a id='mainwp-edit-post-get-categories'></a>
### `mainwp_edit_post_get_categories`

* Method ajax_handle_get_categories()

Get categories.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` |  | 
`$_REQUEST` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 156](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L156)

---

<a id='mainwp-edit-posts-after-submit-button'></a>
### `mainwp_edit_posts_after_submit_button`

* Action: mainwp_edit_posts_after_submit_button

Fires right after the Submit button.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2341](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2341)

---

<a id='mainwp-edit-posts-before-submit-button'></a>
### `mainwp_edit_posts_before_submit_button`

* Action: mainwp_edit_posts_before_submit_button

Fires right before the Submit button.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` | `object` | Object containing the Post data.
`$post_type` | `string` | Post type.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2318](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2318)

---

<a id='mainwp-enqueue-script-gridster'></a>
### `mainwp_enqueue_script_gridster`

* Method admin_init()

Do nothing if current user is not an Admin else display the page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$load_gridstack` |  |

**Usage Locations:**

- [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 766](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L766)

---

<a id='mainwp-escape-content'></a>
### `mainwp_escape_content`

* Edit subscription Post

Handles the saving subscription.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note` |  |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 441](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php#L441)
- [modules/cost-tracker/pages/page-cost-tracker-dashboard.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 745](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L745)
- [modules/cost-tracker/pages/page-cost-tracker-dashboard.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 947](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L947)
- [modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-handle-v1.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-handle-v1.php), [line 127](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-handle-v1.php#L127)
- [modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 296](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L296)

---

<a id='mainwp-extensions-page-top-header'></a>
### `mainwp_extensions_page_top_header`

* Method render_header()

Render page header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extension_name` |  | 
`$extension_name_raw` |  |

**Usage Locations:**

- [class/class-mainwp-extensions-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php), [line 50](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-extensions-view.php#L50)

---

<a id='mainwp-get-all-pages-data'></a>
### `mainwp_get_all_pages_data`

* Get all pages data

Set search parameters for the fetch process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  |

**Changelog**

Version | Description
------- | -----------
`3.4` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1047](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1047)

---

<a id='mainwp-get-all-posts-data'></a>
### `mainwp_get_all_posts_data`

* Get all posts data

Set search parameters for the fetch process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  |

**Changelog**

Version | Description
------- | -----------
`3.4` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1221](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1221)

---

<a id='mainwp-get-post-data-authed'></a>
### `mainwp_get_post_data_authed`

* Method get_post_data_authed()

Get authorized $_POST data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 
`$website` | `mixed` | Array of Child Site Info.
`$what` | `mixed` | What we are posting.
`$params` | `null` | Post parameters.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 361](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L361)

---

<a id='mainwp-getcustompage-backups'></a>
### `mainwp_getcustompage_backups`

* Instantiate Legacy Backups Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$customPage` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$customPage` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 90](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L90)

---

<a id='mainwp-getsubpages-api-backups'></a>
### `mainwp_getsubpages_api_backups`

* This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-admin.php), [line 234](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-admin.php#L234)

---

<a id='mainwp-getsubpages-backups'></a>
### `mainwp_getsubpages_backups`

* Instantiate Legacy Backups Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-backups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php), [line 90](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups.php#L90)

---

<a id='mainwp-getsubpages-client'></a>
### `mainwp_getsubpages_client`

* Method init_menu()

Initiate menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-client.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php), [line 79](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php#L79)

---

<a id='mainwp-getsubpages-cost-tracker'></a>
### `mainwp_getsubpages_cost_tracker`

* This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 292](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php#L292)

---

<a id='mainwp-getsubpages-page'></a>
### `mainwp_getsubpages_page`

* Method init_menu()

Initiate Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 81](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L81)

---

<a id='mainwp-getsubpages-post'></a>
### `mainwp_getsubpages_post`

* Method ini_menu()

Initiate Page menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 78](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L78)

---

<a id='mainwp-getsubpages-restapi'></a>
### `mainwp_getsubpages_restapi`

* REST API Subpages

Filters subpages for the REST API page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  |

**Usage Locations:**

- [pages/page-mainwp-rest-api-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php), [line 116](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-rest-api-page.php#L116)

---

<a id='mainwp-getsubpages-server'></a>
### `mainwp_getsubpages_server`

* Method init_menu()

Initiate Info subPage menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 36](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L36)

---

<a id='mainwp-getsubpages-settings'></a>
### `mainwp_getsubpages_settings`

* Instantiate the Settings Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 137](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L137)

---

<a id='mainwp-getsubpages-sites'></a>
### `mainwp_getsubpages_sites`

* Initiate menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 178](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L178)

---

<a id='mainwp-getsubpages-tags'></a>
### `mainwp_getsubpages_tags`

* This hook allows you to add extra sub pages to the Tags page via the 'mainwp-getsubpages-tags' filter.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$subPages` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$subPages` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 85](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L85)

---

<a id='mainwp-getsubpages-user'></a>
### `mainwp_getsubpages_user`

* Method init_menu()

Initiate menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  |

**Usage Locations:**

- [pages/page-mainwp-user.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php), [line 68](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-user.php#L68)

---

<a id='mainwp-header-left'></a>
### `mainwp_header_left`

* Filter: mainwp_header_left

Filter the MainWP header element left side content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$title` |  | 
`$params` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 505](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L505)

---

<a id='mainwp-header-right'></a>
### `mainwp_header_right`

* Filter: mainwp_header_right

Filter the MainWP header element right side content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$right` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 516](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L516)

---

<a id='mainwp-header-title'></a>
### `mainwp_header_title`

* Filter: mainwp_header_title

Filter the MainWP page title in the header element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$title` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 488](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L488)

---

<a id='mainwp-help-sidebar-content'></a>
### `mainwp_help_sidebar_content`

* Action: mainwp_help_sidebar_content

Fires Help sidebar content

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 782](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L782)

---

<a id='mainwp-info-schedules-cron-listing'></a>
### `mainwp_info_schedules_cron_listing`

* Renders the Cron Schedule page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cron_jobs` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cron_jobs` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1000](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1000)

---

<a id='mainwp-log-specific-actions'></a>
### `mainwp_log_specific_actions`

* Renders action logs page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific_logs` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific_logs` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1651](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1651)

---

<a id='mainwp-logger-to-db'></a>
### `mainwp_logger_to_db`

* Renders action logs page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1651](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1651)

---

<a id='mainwp-manage-pages-action-item'></a>
### `mainwp_manage_pages_action_item`

* Method pages_search_handler()

Pages Search handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$page` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1095](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1095)

---

<a id='mainwp-manage-pages-after-search-options'></a>
### `mainwp_manage_pages_after_search_options`

* Action: mainwp_manage_pages_after_search_options

Fires after the Search Options on Manage Pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 610](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L610)

---

<a id='mainwp-manage-pages-after-select-sites'></a>
### `mainwp_manage_pages_after_select_sites`

* Action: mainwp_manage_pages_after_select_sites

Fires after the Select Sites section on Manage pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 565](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L565)

---

<a id='mainwp-manage-pages-after-submit-button'></a>
### `mainwp_manage_pages_after_submit_button`

* Action: mainwp_manage_pages_after_submit_button

Fires after the Submit Button on Manage Pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 640](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L640)

---

<a id='mainwp-manage-pages-before-search-options'></a>
### `mainwp_manage_pages_before_search_options`

* Action: mainwp_manage_pages_before_search_options

Fires before the Search Options on Manage Pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 580](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L580)

---

<a id='mainwp-manage-pages-before-select-sites'></a>
### `mainwp_manage_pages_before_select_sites`

* Action: mainwp_manage_pages_before_select_sites

Fires before the Select Sites section on Manage pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 542](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L542)

---

<a id='mainwp-manage-pages-before-submit-button'></a>
### `mainwp_manage_pages_before_submit_button`

* Action: mainwp_manage_pages_before_submit_button

Fires before the Submit Button on Manage Pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 624](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L624)

---

<a id='mainwp-manage-pages-bulk-action'></a>
### `mainwp_manage_pages_bulk_action`

* Renders Bulk Page Manager.

Source: [./sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 434](pages/page-mainwp-page.php#L434-L474)

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 434](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L434)

---

<a id='mainwp-manage-pages-sidebar-bottom'></a>
### `mainwp_manage_pages_sidebar_bottom`

* Action: mainwp_manage_pages_sidebar_bottom

Fires at the bottom of the sidebar on Manage pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 651](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L651)

---

<a id='mainwp-manage-pages-sidebar-top'></a>
### `mainwp_manage_pages_sidebar_top`

* Action: mainwp_manage_pages_sidebar_top

Fires at the top of the sidebar on Manage pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 531](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L531)

---

<a id='mainwp-manage-posts-action-item'></a>
### `mainwp_manage_posts_action_item`

* Method posts_search_handler()

Post page search handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 
`$child_to_dash_array` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1282](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1282)

---

<a id='mainwp-manage-posts-after-search-options'></a>
### `mainwp_manage_posts_after_search_options`

* Action: mainwp_manage_posts_after_search_options

Fires after the Search Options on Manage Posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 719](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L719)

---

<a id='mainwp-manage-posts-after-select-sites'></a>
### `mainwp_manage_posts_after_select_sites`

* Action: mainwp_manage_posts_after_select_sites

Fires after the Select Sites section on Manage posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 674](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L674)

---

<a id='mainwp-manage-posts-after-submit-button'></a>
### `mainwp_manage_posts_after_submit_button`

* Action: mainwp_manage_posts_after_submit_button

Fires after the Submit Button on Manage Posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 754](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L754)

---

<a id='mainwp-manage-posts-before-search-options'></a>
### `mainwp_manage_posts_before_search_options`

* Action: mainwp_manage_posts_before_search_options

Fires before the Search Options on Manage Posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 689](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L689)

---

<a id='mainwp-manage-posts-before-select-sites'></a>
### `mainwp_manage_posts_before_select_sites`

* Action: mainwp_manage_posts_before_select_sites

Fires before the Select Sites section on Manage posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 651](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L651)

---

<a id='mainwp-manage-posts-before-submit-button'></a>
### `mainwp_manage_posts_before_submit_button`

* Action: mainwp_manage_posts_before_submit_button

Fires before the Submit Button on Manage Posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 738](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L738)

---

<a id='mainwp-manage-posts-bulk-action'></a>
### `mainwp_manage_posts_bulk_action`

* Method render()

Render the page content.

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 539](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L539)

---

<a id='mainwp-manage-posts-sidebar-bottom'></a>
### `mainwp_manage_posts_sidebar_bottom`

* Action: mainwp_manage_posts_sidebar_bottom

Fires at the bottom of the sidebar on Manage posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 765](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L765)

---

<a id='mainwp-manage-posts-sidebar-top'></a>
### `mainwp_manage_posts_sidebar_top`

* Action: mainwp_manage_posts_sidebar_top

Fires at the top of the sidebar on Manage posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 640](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L640)

---

<a id='mainwp-manageposts-get-post-result'></a>
### `mainwp_manageposts_get_post_result`

* Method get_post()

Get post from child site to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$information['my_post']` |  | 
`$websiteId` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 953](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L953)

---

<a id='mainwp-module-cost-tracker-help-item'></a>
### `mainwp_module_cost_tracker_help_item`

* Action: mainwp_module_cost_tracker_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Cost Tracker page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`5.0` |

**Usage Locations:**

- [modules/cost-tracker/classes/class-cost-tracker-admin.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 874](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/classes/class-cost-tracker-admin.php#L874)

---

<a id='mainwp-overview-help-item'></a>
### `mainwp_overview_help_item`

* Action: mainwp_overview_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Overview page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-overview.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php), [line 445](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-overview.php#L445)

---

<a id='mainwp-page-admin-body-class'></a>
### `mainwp_page_admin_body_class`

* MainWP Admin body CSS class attributes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$class_string` | `mixed` | MainWP CSS Class attributes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$class_string` | `mixed` | MainWP CSS Class attributes.

**Usage Locations:**

- [class/class-mainwp-system-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php), [line 944](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php#L944)

---

<a id='mainwp-page-navigation'></a>
### `mainwp_page_navigation`

* Filter: mainwp_page_navigation

Filters MainWP page navigation menu items.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$subitems` |  | 
`$name_caller` |  |

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1449](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1449)

---

<a id='mainwp-page-navigation-menu'></a>
### `mainwp_page_navigation_menu`

* Method render_page_navigation()

Render page navigation.

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1439](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1439)

---

<a id='mainwp-pagefooter-extensions'></a>
### `mainwp_pagefooter_extensions`

* Method render_extensions_groups()

Source: [./sources/mainwp-dashboard/pages/page-mainwp-extensions-groups.php](pages/page-mainwp-extensions-groups.php), [line 921](pages/page-mainwp-extensions-groups.php#L921-L1086)

**Usage Locations:**

- [pages/page-mainwp-extensions-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php), [line 921](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php#L921)

---

<a id='mainwp-pagefooter-settings'></a>
### `mainwp_pagefooter_settings`

* Render settings

Renders the settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L76)
- [modules/logs/classes/class-log-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-settings.php), [line 263](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-settings.php#L263)

---

<a id='mainwp-pagefooter-sites'></a>
### `mainwp_pagefooter_sites`

* Render Tabs.

Renders the page tabs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-overview.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-overview.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-overview.php#L76)
- [pages/page-mainwp-manage-screenshots.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-screenshots.php), [line 446](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-screenshots.php#L446)
- [pages/page-mainwp-monitoring.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-monitoring.php), [line 306](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-monitoring.php#L306)

---

<a id='mainwp-pagefooter-tags'></a>
### `mainwp_pagefooter_tags`

* Sites Page Footer

Renders the footer on the Sites screen.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ManageGroups'` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 474](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L474)

---

<a id='mainwp-pageheader-extensions'></a>
### `mainwp_pageheader_extensions`

* Method render_extensions_groups()

Source: [./sources/mainwp-dashboard/pages/page-mainwp-extensions-groups.php](pages/page-mainwp-extensions-groups.php), [line 921](pages/page-mainwp-extensions-groups.php#L921-L968)

**Usage Locations:**

- [pages/page-mainwp-extensions-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php), [line 921](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-extensions-groups.php#L921)

---

<a id='mainwp-pageheader-settings'></a>
### `mainwp_pageheader_settings`

* Render settings

Renders the settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-settings.php#L76)
- [modules/logs/classes/class-log-settings.php](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-settings.php), [line 164](https://github.com/mainwp/mainwp/blob/master/modules/logs/classes/class-log-settings.php#L164)

---

<a id='mainwp-pageheader-sites'></a>
### `mainwp_pageheader_sites`

* Render Tabs.

Renders the page tabs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  |

**Usage Locations:**

- [modules/api-backups/classes/class-api-backups-overview.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-overview.php), [line 76](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-overview.php#L76)
- [pages/page-mainwp-manage-screenshots.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-screenshots.php), [line 215](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-screenshots.php#L215)
- [pages/page-mainwp-monitoring.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-monitoring.php), [line 291](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-monitoring.php#L291)

---

<a id='mainwp-pageheader-tags'></a>
### `mainwp_pageheader_tags`

* Sites Page header

Renders the tabs on the Sites screen.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ManageGroups'` |  |

**Usage Locations:**

- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 293](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L293)

---

<a id='mainwp-pages-actions-bar-left'></a>
### `mainwp_pages_actions_bar_left`

* Action: mainwp_pages_actions_bar_left

Fires at the left side of the actions bar on the Pages screen, after the Bulk Actions menu.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 494](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L494)

---

<a id='mainwp-pages-actions-bar-right'></a>
### `mainwp_pages_actions_bar_right`

* Action: mainwp_pages_actions_bar_right

Fires at the right side of the actions bar on the Pages screen.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 506](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L506)

---

<a id='mainwp-pages-bulk-action'></a>
### `mainwp_pages_bulk_action`

* Action: mainwp_pages_bulk_action

Adds new action to the Bulk Actions menu on Manage Pages.

Suggested HTML Markup:
<option value="Your custom value">Your custom text</option>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 479](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L479)

---

<a id='mainwp-pages-help-item'></a>
### `mainwp_pages_help_item`

* Action: mainwp_pages_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Pages page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1741](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1741)

---

<a id='mainwp-pages-posting-popup-actions'></a>
### `mainwp_pages_posting_popup_actions`

* Method posting()

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$id` |  |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1385](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1385)

---

<a id='mainwp-pages-table-action'></a>
### `mainwp_pages_table_action`

* Action: mainwp_pages_table_action

Adds a new item in the Actions menu in Manage Pages table.

Suggested HTML markup:
<a class="item" href="Your custom URL">Your custom label</a>

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$page` |  | 
`$website` | `array` | Object containing the website data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1233](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1233)

---

<a id='mainwp-pages-table-column'></a>
### `mainwp_pages_table_column`

* Action: mainwp_pages_table_column

Adds a new column item in the Manage pages table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$page` | `array` | Array containing the page data.
`$website` | `array` | Object containing the website data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1146](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1146)

---

<a id='mainwp-pages-table-fatures'></a>
### `mainwp_pages_table_fatures`

* Filter: mainwp_pages_table_fatures

Filters the Manage Pages table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 862](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L862)

---

<a id='mainwp-pages-table-header'></a>
### `mainwp_pages_table_header`

* Action: mainwp_pages_table_header

Adds new column header to the Manage pages table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 807](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L807)

---

<a id='mainwp-post-action'></a>
### `mainwp_post_action`

* Fires immediately after post action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$pAction` |  | 
`$data` |  | 
`$postId` |  | 
`$type` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$pAction` |  | 
`$data` |  | 
`$postId` |  | 
`$type` |  |

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` |

**Usage Locations:**

- [class/class-mainwp-actions-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php), [line 51](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php#L51)

---

<a id='mainwp-post-created'></a>
### `mainwp_post_created`

* Method posting_bulk_handler()

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | The website object.
`'newpost'` |  | 
`$information['other_data']['new_post_data']` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | The website object.
`'newpost'` |  | 
`$information['other_data']['new_post_data']` |  |

**Usage Locations:**

- [pages/page-mainwp-bulk-add.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-add.php), [line 34](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-add.php#L34)

---

<a id='mainwp-post-posting-page'></a>
### `mainwp_post_posting_page`

* Posting page

Fires while posting page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site data.
`$output->added_id[$website->id]` |  | 
`$links` | `array` | Links.

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1622](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1622)

---

<a id='mainwp-post-posting-post'></a>
### `mainwp_post_posting_post`

* Posting post

Fires while posting post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site data.
`$output->added_id[$website->id]` |  | 
`$links` | `array` | Links.

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 822](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L822)

---

<a id='mainwp-posting-bulkpost-post-status'></a>
### `mainwp_posting_bulkpost_post_status`

* Post status

Sets post status when posting 'bulkpost' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_status` |  | 
`$id` | `int` | Post ID.

**Usage Locations:**

- [pages/page-mainwp-page.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php), [line 1469](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-page.php#L1469)
- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 682](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L682)

---

<a id='mainwp-posting-post-selected-by'></a>
### `mainwp_posting_post_selected_by`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_by` |  | 
`$id` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-posting-post-selected-sites'></a>
### `mainwp_posting_post_selected_sites`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_sites` |  | 
`$id` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-posting-selected-clients'></a>
### `mainwp_posting_selected_clients`

* Method posting_posts()

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_clients` |  | 
`$id` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L588)

---

<a id='mainwp-postprocess-backup-site'></a>
### `mainwp_postprocess_backup_site`

* Method  backup_site()

Backup Child Site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$localBackupFile` |  | 
`$what` |  | 
`$subfolder` | `mixed` | Sub folder to place backup.
`$regexBackupFile` |  | 
`$website` |  | 
`$taskId` |  | 
`$unique` |  |

**Usage Locations:**

- [class/class-mainwp-backup-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-backup-handler.php), [line 28](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-backup-handler.php#L28)

---

<a id='mainwp-posts-actions-bar-left'></a>
### `mainwp_posts_actions_bar_left`

* Action: mainwp_posts_actions_bar_left

Fires at the left side of the actions bar on the Posts screen, after the Bulk Actions menu.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 603](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L603)

---

<a id='mainwp-posts-actions-bar-right'></a>
### `mainwp_posts_actions_bar_right`

* Action: mainwp_posts_actions_bar_right

Fires at the right side of the actions bar on the Posts screen.

**Changelog**

Version | Description
------- | -----------
`4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 615](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L615)

---

<a id='mainwp-posts-bulk-action'></a>
### `mainwp_posts_bulk_action`

* Action: mainwp_posts_bulk_action

Adds new action to the Bulk Actions menu on Manage Posts.

Suggested HTML Markup:
<option value="Your custom value">Your custom text</option>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 588](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L588)

---

<a id='mainwp-posts-help-item'></a>
### `mainwp_posts_help_item`

* Action: mainwp_posts_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Posts page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2743](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2743)

---

<a id='mainwp-posts-posting-bulk-sites'></a>
### `mainwp_posts_posting_bulk_sites`

* Method posting_bulk()

Create bulk posts on sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  |

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 396](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L396)

---

<a id='mainwp-posts-posting-popup-actions'></a>
### `mainwp_posts_posting_popup_actions`

* Method posting()

Create bulk posts on sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post or Page ID.

**Usage Locations:**

- [pages/page-mainwp-post-page-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php), [line 419](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post-page-handler.php#L419)

---

<a id='mainwp-posts-search-bulk-sites'></a>
### `mainwp_posts_search_bulk_sites`

* Method render()

Render the page content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`0` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 539](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L539)

---

<a id='mainwp-posts-table-action'></a>
### `mainwp_posts_table_action`

* Action: mainwp_posts_table_action

Adds a new item in the Actions menu in Manage Posts table.

Suggested HTML markup:
<a class="item" href="Your custom URL">Your custom label</a>

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` | `array` | Array containing the post data.
`$website` | `array` | Object containing the website data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1460](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1460)

---

<a id='mainwp-posts-table-column'></a>
### `mainwp_posts_table_column`

* Action: mainwp_posts_table_column

Adds a new column item in the Manage posts table.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` | `array` | Array containing the post data.
`$website` | `array` | Object containing the website data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1353](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1353)

---

<a id='mainwp-posts-table-fatures'></a>
### `mainwp_posts_table_fatures`

* Filter: mainwp_posts_table_fatures

Filters the Manage Posts table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1012](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1012)

---

<a id='mainwp-posts-table-header'></a>
### `mainwp_posts_table_header`

* Action: mainwp_posts_table_header

Adds new column header to the Manage posts table.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 948](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L948)

---

<a id='mainwp-pre-fetch-authed-data'></a>
### `mainwp_pre_fetch_authed_data`

* Method get_post_data_authed()

Get authorized $_POST data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$params` | `null` | Post parameters.
`$what` | `mixed` | What we are posting.
`$website` | `mixed` | Array of Child Site Info.

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 361](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L361)

---

<a id='mainwp-pre-posting-posts'></a>
### `mainwp_pre_posting_posts`

* Filter: mainwp_pre_posting_posts

Prepares parameters for the authenticated cURL post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`is_array($params) ? $params : array()` |  | 
`(object) array('id' => $website->id, 'url' => $website->url, 'name' => $website->name)` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 803](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L803)

---

<a id='mainwp-pro-reports-generate-content'></a>
### `mainwp_pro_reports_generate_content`

* Filter: mainwp_pro_reports_generate_content

Filters the Pro Reports available content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$content` |  | 
`$current_email_site->id` |  | 
`$timestamp_from_date` |  | 
`$timestamp_to_date` |  |

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 210](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L210)

---

<a id='mainwp-recent-pages-after-draft-list'></a>
### `mainwp_recent_pages_after_draft_list`

* Action: mainwp_recent_pages_after_draft_list

Fires after the list of recent draft Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 381](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L381)

---

<a id='mainwp-recent-pages-after-future-list'></a>
### `mainwp_recent_pages_after_future_list`

* Action: mainwp_recent_pages_after_future_list

Fires after the list of recent future Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 565](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L565)

---

<a id='mainwp-recent-pages-after-lists'></a>
### `mainwp_recent_pages_after_lists`

* Action: mainwp_recent_pages_after_lists

Fires after the recent pages lists, before the bottom actions section.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 139](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L139)

---

<a id='mainwp-recent-pages-after-pending-list'></a>
### `mainwp_recent_pages_after_pending_list`

* Action: mainwp_recent_pages_after_pending_list

Fires after the list of recent pending pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 472](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L472)

---

<a id='mainwp-recent-pages-after-publised-list'></a>
### `mainwp_recent_pages_after_publised_list`

* Action: mainwp_recent_pages_after_publised_list

Fires after the list of recent published Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 289](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L289)

---

<a id='mainwp-recent-pages-after-trash-list'></a>
### `mainwp_recent_pages_after_trash_list`

* Action: mainwp_recent_pages_after_trash_list

Fires after the list of recent trash Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 655](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L655)

---

<a id='mainwp-recent-pages-before-draft-list'></a>
### `mainwp_recent_pages_before_draft_list`

* Action: mainwp_recent_pages_before_draft_list

Fires before the list of recent draft Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 324](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L324)

---

<a id='mainwp-recent-pages-before-future-list'></a>
### `mainwp_recent_pages_before_future_list`

* Action: mainwp_recent_pages_before_future_list

Fires before the list of recent future Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 507](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L507)

---

<a id='mainwp-recent-pages-before-pending-list'></a>
### `mainwp_recent_pages_before_pending_list`

* Action: mainwp_recent_pages_before_pending_list

Fires before the list of recent pending pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 415](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L415)

---

<a id='mainwp-recent-pages-before-publised-list'></a>
### `mainwp_recent_pages_before_publised_list`

* Action: mainwp_recent_pages_before_publised_list

Fires before the list of recent published Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 229](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L229)

---

<a id='mainwp-recent-pages-before-trash-list'></a>
### `mainwp_recent_pages_before_trash_list`

* Action: mainwp_recent_pages_before_trash_list

Fires before the list of recent trash Pages.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPages` | `array` | All pages data.
`$recent_number` | `int` | Number of pages.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 600](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L600)

---

<a id='mainwp-recent-pages-widget-bottom'></a>
### `mainwp_recent_pages_widget_bottom`

* Action: mainwp_recent_pages_widget_bottom

Fires at the bottom of the Recent Pages widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 159](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L159)

---

<a id='mainwp-recent-pages-widget-title'></a>
### `mainwp_recent_pages_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Recent Pages', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Recent Pages', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 185](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L185)

---

<a id='mainwp-recent-pages-widget-top'></a>
### `mainwp_recent_pages_widget_top`

* Action: mainwp_recent_pages_widget_top

Fires at the top of the Recent Pages widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 119](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L119)

---

<a id='mainwp-recent-posts-after-draft-list'></a>
### `mainwp_recent_posts_after_draft_list`

* Action: mainwp_recent_posts_after_draft_list

Fires after the list of recent draft Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 383](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L383)

---

<a id='mainwp-recent-posts-after-future-list'></a>
### `mainwp_recent_posts_after_future_list`

* Action: mainwp_recent_posts_after_future_list

Fires after the list of recent future Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 566](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L566)

---

<a id='mainwp-recent-posts-after-lists'></a>
### `mainwp_recent_posts_after_lists`

* Action: mainwp_recent_posts_after_lists

Fires after the recent posts lists, before the bottom actions section.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 144](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L144)

---

<a id='mainwp-recent-posts-after-pending-list'></a>
### `mainwp_recent_posts_after_pending_list`

* Action: mainwp_recent_posts_after_pending_list

Fires after the list of recent pending Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 474](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L474)

---

<a id='mainwp-recent-posts-after-publised-list'></a>
### `mainwp_recent_posts_after_publised_list`

* Action: mainwp_recent_posts_after_publised_list

Fires after the list of recent published Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 292](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L292)

---

<a id='mainwp-recent-posts-after-trash-list'></a>
### `mainwp_recent_posts_after_trash_list`

* Action: mainwp_recent_posts_after_trash_list

Fires after the list of recent trash Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 656](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L656)

---

<a id='mainwp-recent-posts-before-draft-list'></a>
### `mainwp_recent_posts_before_draft_list`

* Action: mainwp_recent_posts_before_draft_list

Fires before the list of recent draft Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 327](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L327)

---

<a id='mainwp-recent-posts-before-future-list'></a>
### `mainwp_recent_posts_before_future_list`

* Action: mainwp_recent_posts_before_future_list

Fires before the list of recent future Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 509](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L509)

---

<a id='mainwp-recent-posts-before-pending-list'></a>
### `mainwp_recent_posts_before_pending_list`

* Action: mainwp_recent_posts_before_pending_list

Fires before the list of recent pending Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 418](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L418)

---

<a id='mainwp-recent-posts-before-publised-list'></a>
### `mainwp_recent_posts_before_publised_list`

* Action: mainwp_recent_posts_before_publised_list

Fires before the list of recent published Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 233](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L233)

---

<a id='mainwp-recent-posts-before-trash-list'></a>
### `mainwp_recent_posts_before_trash_list`

* Action: mainwp_recent_posts_before_trash_list

Fires before the list of recent trash Posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$allPosts` | `array` | All posts data.
`$recent_number` | `int` | Number of posts.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 601](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L601)

---

<a id='mainwp-recent-posts-pages-number'></a>
### `mainwp_recent_posts_pages_number`

* This filter is documented in ../widgets/widget-mainwp-recent-posts.php

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`5` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`5` |  |

**Usage Locations:**

- [class/class-mainwp-connect.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php), [line 421](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-connect.php#L421)
- [widgets/widget-mainwp-recent-pages.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php), [line 50](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-pages.php#L50)
- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 50](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L50)

---

<a id='mainwp-recent-posts-widget-bottom'></a>
### `mainwp_recent_posts_widget_bottom`

* Action: mainwp_recent_posts_widget_bottom

Fires at the bottom of the Recent Posts widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 163](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L163)

---

<a id='mainwp-recent-posts-widget-title'></a>
### `mainwp_recent_posts_widget_title`

* *Arguments*

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Recent Posts', 'mainwp')` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Recent Posts', 'mainwp')` |  |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 189](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L189)

---

<a id='mainwp-recent-posts-widget-top'></a>
### `mainwp_recent_posts_widget_top`

* Action: mainwp_recent_posts_widget_top

Fires at the top of the Recent Posts widget.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [widgets/widget-mainwp-recent-posts.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php), [line 125](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-recent-posts.php#L125)

---

<a id='mainwp-register-post-type'></a>
### `mainwp_register_post_type`

* Method create_post_type()

Register "Bulkpost" and "Bulkpage" custom post types.

**Usage Locations:**

- [class/class-mainwp-bulk-post.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php), [line 256](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php#L256)

---

<a id='mainwp-save-bulkpage'></a>
### `mainwp_save_bulkpage`

* Action: mainwp_save_bulkpage

Fires when saving the bulk page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.

**Usage Locations:**

- [class/class-mainwp-bulk-post.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php), [line 227](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php#L227)

---

<a id='mainwp-save-bulkpost'></a>
### `mainwp_save_bulkpost`

* Action: mainwp_save_bulkpost

Fires when saving the bulk post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.

**Usage Locations:**

- [class/class-mainwp-bulk-post.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php), [line 158](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php#L158)

---

<a id='mainwp-security-post-data'></a>
### `mainwp_security_post_data`

* Filters security issues from fixing

Filters the default security checks and enables user to disable certain issues from being fixed by using the Fix All button.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$skip_features` | `object` | Object containing data from che chid site related to security issues.<br>Available options: 'db_reporting', 'php_reporting'.
`$website` | `object` | Object containing child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-security-issues.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php), [line 346](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-security-issues.php#L346)

---

<a id='mainwp-show-qsw'></a>
### `mainwp_show_qsw`

* Render MainWP Tools SubPage.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  |

**Usage Locations:**

- [pages/page-mainwp-settings.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php), [line 1953](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-settings.php#L1953)

---

<a id='mainwp-sidbar-pages'></a>
### `mainwp_sidbar_pages`

* Method render_header_actions()

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sidebar_pages` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1273](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1273)
- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2421](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2421)

---

<a id='mainwp-sidebar-pages'></a>
### `mainwp_sidebar_pages`

* Method render_header_actions()

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sidebar_pages` |  |

**Usage Locations:**

- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1273](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1273)
- [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2421](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2421)

---

<a id='mainwp-specific-action-logs'></a>
### `mainwp_specific_action_logs`

* Renders action logs page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific_default` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific_default` |  |

**Usage Locations:**

- [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1651](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1651)

---

<a id='mainwp-subpages-left-menu'></a>
### `mainwp_subpages_left_menu`

* Method init_subpages_left_menu

Build left menu subpages array.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$subPages` | `array` | Array of SubPages.
`$initSubpage` | `array` | Initial SubPage Array.
`$parentKey` | `string` | Parent Menu Slug.
`$slug` | `mixed` | SubPage Slug.

**Usage Locations:**

- [class/class-mainwp-menu.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php), [line 479](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-menu.php#L479)

---

<a id='mainwp-tags-help-item'></a>
### `mainwp_tags_help_item`

* Action: mainwp_tags_help_item

Fires at the bottom of the help articles list in the Help sidebar on the Tags page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>

**Changelog**

Version | Description
------- | -----------
`4.1` |

**Usage Locations:**

- [pages/page-mainwp-manage-groups.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php), [line 789](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-groups.php#L789)

---

<a id='mainwp-top-bulkpost-edit-content'></a>
### `mainwp_top_bulkpost_edit_content`

* Renders bulkpost to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 2009](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L2009)

---

<a id='mainwp-wordfence-sites'></a>
### `mainwp_wordfence_sites`

* Action: mainwp_wordfence_sites

Fires on a child site Hardening page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site info.

**Usage Locations:**

- [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 815](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L815)

---

<a id='postmeta-form-keys'></a>
### `postmeta_form_keys`

* Filters values for the meta key dropdown in the Custom Fields meta box.

Returning a non-null value will effectively short-circuit and avoid a
potentially expensive query against postmeta.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`null` |  | 
`$_post` | `\MainWP\Dashboard\WP_Post` | The current post object.

**Changelog**

Version | Description
------- | -----------
`4.4.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1568](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1568)

---

<a id='postmeta-form-limit'></a>
### `postmeta_form_limit`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`30` |  |

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`30` |  |

**Changelog**

Version | Description
------- | -----------
`2.1.0` |

**Usage Locations:**

- [pages/page-mainwp-post.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php), [line 1582](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-post.php#L1582)

---

<a id='redirect-post-location'></a>
### `redirect_post_location`

* Filter: redirect_post_location

Filters the location for the Edit process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$location` |  | 
`$post_id` | `int` | Post ID.

**Usage Locations:**

- [class/class-mainwp-bulk-post.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php), [line 56](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-bulk-post.php#L56)

---


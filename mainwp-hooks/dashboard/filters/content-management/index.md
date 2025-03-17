# Content Management Filters

Hooks for managing posts, pages, comments, and other content.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`mainwp_bulkpost_categories_handle`](#mainwp_bulkpost_categories_handle) - Method add_categories_handle()
- [`mainwp_bulkpost_tags_handle`](#mainwp_bulkpost_tags_handle) - Method add_tags_handle()
- [`mainwp_post_action`](#mainwp_post_action) - Fires immediately after post action.
- [`mainwp_postprocess_backup_site`](#mainwp_postprocess_backup_site) - Method  backup_site()
- [`mainwp_help_sidebar_content`](#mainwp_help_sidebar_content) - Action: mainwp_help_sidebar_content
- [`mainwp_before_mainwp_content_wrap`](#mainwp_before_mainwp_content_wrap) - Action: mainwp_before_mainwp_content_wrap
- [`mainwp_page_navigation_menu`](#mainwp_page_navigation_menu) - Method render_page_navigation()
- [`mainwp_save_bulkpost`](#mainwp_save_bulkpost) - Action: mainwp_save_bulkpost
- [`mainwp_before_redirect_posting_bulkpost`](#mainwp_before_redirect_posting_bulkpost) - Action: mainwp_before_redirect_posting_bulkpost
- [`mainwp_save_bulkpage`](#mainwp_save_bulkpage) - Action: mainwp_save_bulkpage
- [`mainwp_before_redirect_posting_bulkpage`](#mainwp_before_redirect_posting_bulkpage) - Action: mainwp_before_redirect_posting_bulkpage
- [`mainwp_register_post_type`](#mainwp_register_post_type) - Method create_post_type()
- [`mainwp_admin_footer`](#mainwp_admin_footer) - Action: mainwp_admin_footer
- [`mainwp_pageheader_settings`](#mainwp_pageheader_settings) - Render settings
- [`mainwp_pagefooter_settings`](#mainwp_pagefooter_settings) - Render settings
- [`mainwp_pageheader_sites`](#mainwp_pageheader_sites) - Render Tabs.
- [`mainwp_pagefooter_sites`](#mainwp_pagefooter_sites) - Render Tabs.
- [`mainwp_pageheader_settings`](#mainwp_pageheader_settings) - This action is documented in ../pages/page-mainwp-manage-sites.php
- [`mainwp_pagefooter_settings`](#mainwp_pagefooter_settings) - This action is documented in ../pages/page-mainwp-manage-sites.php
- [`mainwp_module_cost_tracker_help_item`](#mainwp_module_cost_tracker_help_item) - Action: mainwp_module_cost_tracker_help_item
- [`mainwp_module_cost_tracker_actions_bar_left`](#mainwp_module_cost_tracker_actions_bar_left) - Render Actions Bar
- [`mainwp_module_cost_tracker_actions_bar_right`](#mainwp_module_cost_tracker_actions_bar_right) - Render Actions Bar
- [`mainwp_tools_form_top`](#mainwp_tools_form_top) - Action: mainwp_tools_form_top
- [`mainwp_tools_form_bottom`](#mainwp_tools_form_bottom) - Action: mainwp_tools_form_bottom
- [`mainwp_bulkpost_before_post`](#mainwp_bulkpost_before_post) - Before Post post action
- [`mainwp_posts_posting_popup_actions`](#mainwp_posts_posting_popup_actions) - Method posting()
- [`mainwp-post-posting-post`](#mainwp-post-posting-post) - Method posting_posts()
- [`mainwp-bulkposting-done`](#mainwp-bulkposting-done) - Method posting_posts()
- [`mainwp_post_posting_post`](#mainwp_post_posting_post) - Posting post
- [`mainwp_bulkposting_done`](#mainwp_bulkposting_done) - Posting post completed
- [`mainwp_manage_posts_bulk_action`](#mainwp_manage_posts_bulk_action) - Method render()
- [`mainwp_posts_bulk_action`](#mainwp_posts_bulk_action) - Action: mainwp_posts_bulk_action
- [`mainwp_posts_actions_bar_left`](#mainwp_posts_actions_bar_left) - Action: mainwp_posts_actions_bar_left
- [`mainwp_posts_actions_bar_right`](#mainwp_posts_actions_bar_right) - Action: mainwp_posts_actions_bar_right
- [`mainwp_manage_posts_sidebar_top`](#mainwp_manage_posts_sidebar_top) - Action: mainwp_manage_posts_sidebar_top
- [`mainwp_manage_posts_before_select_sites`](#mainwp_manage_posts_before_select_sites) - Action: mainwp_manage_posts_before_select_sites
- [`mainwp_manage_posts_after_select_sites`](#mainwp_manage_posts_after_select_sites) - Action: mainwp_manage_posts_after_select_sites
- [`mainwp_manage_posts_before_search_options`](#mainwp_manage_posts_before_search_options) - Action: mainwp_manage_posts_before_search_options
- [`mainwp_manage_posts_after_search_options`](#mainwp_manage_posts_after_search_options) - Action: mainwp_manage_posts_after_search_options
- [`mainwp_manage_posts_before_submit_button`](#mainwp_manage_posts_before_submit_button) - Action: mainwp_manage_posts_before_submit_button
- [`mainwp_manage_posts_after_submit_button`](#mainwp_manage_posts_after_submit_button) - Action: mainwp_manage_posts_after_submit_button
- [`mainwp_manage_posts_sidebar_bottom`](#mainwp_manage_posts_sidebar_bottom) - Action: mainwp_manage_posts_sidebar_bottom
- [`mainwp_before_posts_table`](#mainwp_before_posts_table) - Action: mainwp_before_posts_table
- [`mainwp_posts_table_header`](#mainwp_posts_table_header) - Action: mainwp_posts_table_header
- [`mainwp_after_posts_table`](#mainwp_after_posts_table) - Action: mainwp_after_posts_table
- [`mainwp_posts_table_column`](#mainwp_posts_table_column) - Action: mainwp_posts_table_column
- [`mainwp_manage_posts_action_item`](#mainwp_manage_posts_action_item) - Method posts_search_handler()
- [`mainwp_posts_table_action`](#mainwp_posts_table_action) - Action: mainwp_posts_table_action
- [`mainwp_top_bulkpost_edit_content`](#mainwp_top_bulkpost_edit_content) - Renders bulkpost to edit.
- [`mainwp_before_bulkpost_editor`](#mainwp_before_bulkpost_editor) - Renders bulkpost to edit.
- [`mainwp_bulkpost_edit`](#mainwp_bulkpost_edit) - Edit bulkpost
- [`add_meta_boxes`](#add_meta_boxes) - Edit bulkpost metaboxes
- [`mainwp_bulkpost_edit_top_side`](#mainwp_bulkpost_edit_top_side) - Renders bulkpost to edit.
- [`mainwp_edit_posts_before_submit_button`](#mainwp_edit_posts_before_submit_button) - Action: mainwp_edit_posts_before_submit_button
- [`mainwp_edit_posts_after_submit_button`](#mainwp_edit_posts_after_submit_button) - Action: mainwp_edit_posts_after_submit_button
- [`mainwp_posts_help_item`](#mainwp_posts_help_item) - Action: mainwp_posts_help_item
- [`mainwp_overview_help_item`](#mainwp_overview_help_item) - Action: mainwp_overview_help_item
- [`mainwp_cron_jobs_list`](#mainwp_cron_jobs_list) - Action: mainwp_cron_jobs_list
- [`mainwp_pageheader_tags`](#mainwp_pageheader_tags) - Sites Page header
- [`mainwp_pagefooter_tags`](#mainwp_pagefooter_tags) - Sites Page Footer
- [`mainwp_post_created`](#mainwp_post_created) - Method posting_bulk_handler()
- [`admin_print_styles`](#admin_print_styles) - Method setup_wizard_header()
- [`mainwp_pageheader_extensions`](#mainwp_pageheader_extensions) - Method render_extensions_groups()
- [`mainwp_pagefooter_extensions`](#mainwp_pagefooter_extensions) - Method render_extensions_groups()
- [`mainwp_manage_pages_bulk_action`](#mainwp_manage_pages_bulk_action) - Renders Bulk Page Manager.
- [`mainwp_pages_bulk_action`](#mainwp_pages_bulk_action) - Action: mainwp_pages_bulk_action
- [`mainwp_pages_actions_bar_left`](#mainwp_pages_actions_bar_left) - Action: mainwp_pages_actions_bar_left
- [`mainwp_pages_actions_bar_right`](#mainwp_pages_actions_bar_right) - Action: mainwp_pages_actions_bar_right
- [`mainwp_manage_pages_sidebar_top`](#mainwp_manage_pages_sidebar_top) - Action: mainwp_manage_pages_sidebar_top
- [`mainwp_manage_pages_before_select_sites`](#mainwp_manage_pages_before_select_sites) - Action: mainwp_manage_pages_before_select_sites
- [`mainwp_manage_pages_after_select_sites`](#mainwp_manage_pages_after_select_sites) - Action: mainwp_manage_pages_after_select_sites
- [`mainwp_manage_pages_before_search_options`](#mainwp_manage_pages_before_search_options) - Action: mainwp_manage_pages_before_search_options
- [`mainwp_manage_pages_after_search_options`](#mainwp_manage_pages_after_search_options) - Action: mainwp_manage_pages_after_search_options
- [`mainwp_manage_pages_before_submit_button`](#mainwp_manage_pages_before_submit_button) - Action: mainwp_manage_pages_before_submit_button
- [`mainwp_manage_pages_after_submit_button`](#mainwp_manage_pages_after_submit_button) - Action: mainwp_manage_pages_after_submit_button
- [`mainwp_manage_pages_sidebar_bottom`](#mainwp_manage_pages_sidebar_bottom) - Action: mainwp_manage_pages_sidebar_bottom
- [`mainwp_before_pages_table`](#mainwp_before_pages_table) - Action: mainwp_before_pages_table
- [`mainwp_pages_table_header`](#mainwp_pages_table_header) - Action: mainwp_pages_table_header
- [`mainwp_after_pages_table`](#mainwp_after_pages_table) - Action: mainwp_after_pages_table
- [`mainwp_pages_table_column`](#mainwp_pages_table_column) - Action: mainwp_pages_table_column
- [`mainwp_manage_pages_action_item`](#mainwp_manage_pages_action_item) - Method pages_search_handler()
- [`mainwp_pages_table_action`](#mainwp_pages_table_action) - Action: mainwp_pages_table_action
- [`mainwp_bulkpage_before_post`](#mainwp_bulkpage_before_post) - Before Page post action
- [`mainwp-post-posting-page`](#mainwp-post-posting-page) - Method posting()
- [`mainwp-bulkposting-done`](#mainwp-bulkposting-done) - Method posting()
- [`mainwp_post_posting_page`](#mainwp_post_posting_page) - Posting page
- [`mainwp_bulkposting_done`](#mainwp_bulkposting_done) - Posting page completed
- [`mainwp_pages_posting_popup_actions`](#mainwp_pages_posting_popup_actions) - Method posting()
- [`mainwp_pages_help_item`](#mainwp_pages_help_item) - Action: mainwp_pages_help_item
- [`mainwp_pageheader_sites`](#mainwp_pageheader_sites) - This action is documented in ../pages/page-mainwp-manage-sites.php
- [`mainwp_pagefooter_sites`](#mainwp_pagefooter_sites) - This action is documented in ../pages/page-mainwp-manage-sites.php
- [`mainwp_pageheader_sites`](#mainwp_pageheader_sites) - Sites Page header
- [`mainwp_pagefooter_sites`](#mainwp_pagefooter_sites) - Sites Page Footer
- [`mainwp_recent_posts_widget_top`](#mainwp_recent_posts_widget_top) - Action: mainwp_recent_posts_widget_top
- [`mainwp_recent_posts_after_lists`](#mainwp_recent_posts_after_lists) - Action: mainwp_recent_posts_after_lists
- [`mainwp_recent_posts_widget_bottom`](#mainwp_recent_posts_widget_bottom) - Action: mainwp_recent_posts_widget_bottom
- [`mainwp_recent_posts_before_publised_list`](#mainwp_recent_posts_before_publised_list) - Action: mainwp_recent_posts_before_publised_list
- [`mainwp_recent_posts_after_publised_list`](#mainwp_recent_posts_after_publised_list) - Action: mainwp_recent_posts_after_publised_list
- [`mainwp_recent_posts_before_draft_list`](#mainwp_recent_posts_before_draft_list) - Action: mainwp_recent_posts_before_draft_list
- [`mainwp_recent_posts_after_draft_list`](#mainwp_recent_posts_after_draft_list) - Action: mainwp_recent_posts_after_draft_list
- [`mainwp_recent_posts_before_pending_list`](#mainwp_recent_posts_before_pending_list) - Action: mainwp_recent_posts_before_pending_list
- [`mainwp_recent_posts_after_pending_list`](#mainwp_recent_posts_after_pending_list) - Action: mainwp_recent_posts_after_pending_list
- [`mainwp_recent_posts_before_future_list`](#mainwp_recent_posts_before_future_list) - Action: mainwp_recent_posts_before_future_list
- [`mainwp_recent_posts_after_future_list`](#mainwp_recent_posts_after_future_list) - Action: mainwp_recent_posts_after_future_list
- [`mainwp_recent_posts_before_trash_list`](#mainwp_recent_posts_before_trash_list) - Action: mainwp_recent_posts_before_trash_list
- [`mainwp_recent_posts_after_trash_list`](#mainwp_recent_posts_after_trash_list) - Action: mainwp_recent_posts_after_trash_list
- [`mainwp_before_post_action`](#mainwp_before_post_action) - Action: mainwp_before_post_action
- [`mainwp_after_post_action`](#mainwp_after_post_action) - 
- [`mainwp_recent_pages_widget_top`](#mainwp_recent_pages_widget_top) - Action: mainwp_recent_pages_widget_top
- [`mainwp_recent_pages_after_lists`](#mainwp_recent_pages_after_lists) - Action: mainwp_recent_pages_after_lists
- [`mainwp_recent_pages_widget_bottom`](#mainwp_recent_pages_widget_bottom) - Action: mainwp_recent_pages_widget_bottom
- [`mainwp_recent_pages_before_publised_list`](#mainwp_recent_pages_before_publised_list) - Action: mainwp_recent_pages_before_publised_list
- [`mainwp_recent_pages_after_publised_list`](#mainwp_recent_pages_after_publised_list) - Action: mainwp_recent_pages_after_publised_list
- [`mainwp_recent_pages_before_draft_list`](#mainwp_recent_pages_before_draft_list) - Action: mainwp_recent_pages_before_draft_list
- [`mainwp_recent_pages_after_draft_list`](#mainwp_recent_pages_after_draft_list) - Action: mainwp_recent_pages_after_draft_list
- [`mainwp_recent_pages_before_pending_list`](#mainwp_recent_pages_before_pending_list) - Action: mainwp_recent_pages_before_pending_list
- [`mainwp_recent_pages_after_pending_list`](#mainwp_recent_pages_after_pending_list) - Action: mainwp_recent_pages_after_pending_list
- [`mainwp_recent_pages_before_future_list`](#mainwp_recent_pages_before_future_list) - Action: mainwp_recent_pages_before_future_list
- [`mainwp_recent_pages_after_future_list`](#mainwp_recent_pages_after_future_list) - Action: mainwp_recent_pages_after_future_list
- [`mainwp_recent_pages_before_trash_list`](#mainwp_recent_pages_before_trash_list) - Action: mainwp_recent_pages_before_trash_list
- [`mainwp_recent_pages_after_trash_list`](#mainwp_recent_pages_after_trash_list) - Action: mainwp_recent_pages_after_trash_list
- [`mainwp_enqueue_script_gridster`](#mainwp_enqueue_script_gridster) - Method admin_init()
- [`mainwp_header_title`](#mainwp_header_title) - Filter: mainwp_header_title
- [`mainwp_header_left`](#mainwp_header_left) - Filter: mainwp_header_left
- [`mainwp_header_right`](#mainwp_header_right) - Filter: mainwp_header_right
- [`mainwp_sidbar_pages`](#mainwp_sidbar_pages) - Method render_header_actions()
- [`mainwp_sidebar_pages`](#mainwp_sidebar_pages) - Method render_header_actions()
- [`mainwp_page_navigation`](#mainwp_page_navigation) - Filter: mainwp_page_navigation
- [`mainwp_sidbar_pages`](#mainwp_sidbar_pages) - Method render_screen_options()
- [`mainwp_sidebar_pages`](#mainwp_sidebar_pages) - Method render_screen_options()
- [`redirect_post_location`](#redirect_post_location) - Filter: redirect_post_location
- [`mainwp_daily_digest_content`](#mainwp_daily_digest_content) - Filter: mainwp_daily_digest_content
- [`mainwp_send_mail_from_header`](#mainwp_send_mail_from_header) - Method send_wp_mail().
- [`mainwp_page_admin_body_class`](#mainwp_page_admin_body_class) - MainWP Admin body CSS class attributes.
- [`mainwp_get_post_data_authed`](#mainwp_get_post_data_authed) - Method get_post_data_authed()
- [`mainwp_recent_posts_pages_number`](#mainwp_recent_posts_pages_number) - This filter is documented in ../widgets/widget-mainwp-recent-posts.php
- [`mainwp-pre-posting-posts`](#mainwp-pre-posting-posts) - Filter is being replaced with mainwp_pre_posting_posts.
- [`mainwp_pre_posting_posts`](#mainwp_pre_posting_posts) - Filter: mainwp_pre_posting_posts
- [`mainwp_subpages_left_menu`](#mainwp_subpages_left_menu) - Method init_subpages_left_menu
- [`mainwp_extensions_page_top_header`](#mainwp_extensions_page_top_header) - Method render_header()
- [`mainwp_pro_reports_generate_content`](#mainwp_pro_reports_generate_content) - Filter: mainwp_pro_reports_generate_content
- [`mainwp_client_report_generate_content`](#mainwp_client_report_generate_content) - Filter: mainwp_client_report_generate_content
- [`mainwp_getsubpages_api_backups`](#mainwp_getsubpages_api_backups) - This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.
- [`mainwp_getsubpages_cost_tracker`](#mainwp_getsubpages_cost_tracker) - This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.
- [`mainwp_escape_content`](#mainwp_escape_content) - Edit subscription Post
- [`mainwp_escape_content`](#mainwp_escape_content) - Get table rows.
- [`mainwp_escape_content`](#mainwp_escape_content) - Method ajax_notes_save()
- [`mainwp_escape_content`](#mainwp_escape_content) - Method get_cost_field_value().
- [`mainwp_escape_content`](#mainwp_escape_content) - Handles the saving item.
- [`mainwp-getsubpages-settings`](#mainwp-getsubpages-settings) - Settings Subpages
- [`mainwp_getsubpages_settings`](#mainwp_getsubpages_settings) - Instantiate the Settings Menu.
- [`date_formats`](#date_formats) - *Arguments*
- [`time_formats`](#time_formats) - *Arguments*
- [`mainwp_show_qsw`](#mainwp_show_qsw) - Render MainWP Tools SubPage.
- [`mainwp_edit_post_get_categories`](#mainwp_edit_post_get_categories) - Method ajax_handle_get_categories()
- [`mainwp_posts_posting_bulk_sites`](#mainwp_posts_posting_bulk_sites) - Method posting_bulk()
- [`mainwp_posting_post_selected_by`](#mainwp_posting_post_selected_by) - Method posting_posts()
- [`mainwp_posting_post_selected_sites`](#mainwp_posting_post_selected_sites) - Method posting_posts()
- [`mainwp_posting_selected_clients`](#mainwp_posting_selected_clients) - Method posting_posts()
- [`mainwp_posting_bulkpost_post_status`](#mainwp_posting_bulkpost_post_status) - Post status
- [`mainwp-after-posting-bulkpost-result`](#mainwp-after-posting-bulkpost-result) - After posting a new post
- [`mainwp_after_posting_bulkpost_result`](#mainwp_after_posting_bulkpost_result) - Method posting_posts()
- [`mainwp_after_posting_delete_bulk_post`](#mainwp_after_posting_delete_bulk_post) - Method posting_posts()
- [`mainwp_manageposts_get_post_result`](#mainwp_manageposts_get_post_result) - Method get_post()
- [`mainwp_getsubpages_client`](#mainwp_getsubpages_client) - Method init_menu()
- [`mainwp_default_emails_fields`](#mainwp_default_emails_fields) - Method get_defaults_email_settings_value().
- [`mainwp-getcustompage-backups`](#mainwp-getcustompage-backups) - Backups Subpages
- [`mainwp_getcustompage_backups`](#mainwp_getcustompage_backups) - Instantiate Legacy Backups Menu.
- [`mainwp-getsubpages-backups`](#mainwp-getsubpages-backups) - Instantiate Legacy Backups Menu.
- [`mainwp_getsubpages_backups`](#mainwp_getsubpages_backups) - Instantiate Legacy Backups Menu.
- [`mainwp-getsubpages-post`](#mainwp-getsubpages-post) - Method ini_menu()
- [`mainwp_getsubpages_post`](#mainwp_getsubpages_post) - Method ini_menu()
- [`mainwp_edit_bulkpost_getmetaboxes`](#mainwp_edit_bulkpost_getmetaboxes) - Init custom bulkpost metaboxes.
- [`mainwp_posts_search_bulk_sites`](#mainwp_posts_search_bulk_sites) - Method render()
- [`mainwp_custom_post_types_default`](#mainwp_custom_post_types_default) - Default post types
- [`mainwp_posts_table_fatures`](#mainwp_posts_table_fatures) - Filter: mainwp_posts_table_fatures
- [`mainwp_get_all_posts_data`](#mainwp_get_all_posts_data) - Get all posts data
- [`postmeta_form_keys`](#postmeta_form_keys) - Filters values for the meta key dropdown in the Custom Fields meta box.
- [`postmeta_form_limit`](#postmeta_form_limit) - 
- [`admin_post_thumbnail_size`](#admin_post_thumbnail_size) - Filters the size used to display the post thumbnail image in the 'Featured Image' meta box.
- [`mainwp_admin_post_thumbnail_html`](#mainwp_admin_post_thumbnail_html) - Filters the admin post thumbnail HTML markup to return.
- [`mainwp_custom_render_bulkpost`](#mainwp_custom_render_bulkpost) - Renders bulkpost to edit.
- [`mainwp_bulkpost_edit_title`](#mainwp_bulkpost_edit_title) - Renders bulkpost to edit.
- [`mainwp_bulkpost_editor_settings`](#mainwp_bulkpost_editor_settings) - Renders bulkpost to edit.
- [`mainwp-getsubpages-sites`](#mainwp-getsubpages-sites) - Initiate menu.
- [`mainwp_getsubpages_sites`](#mainwp_getsubpages_sites) - Initiate menu.
- [`mainwp_getsubpages_restapi`](#mainwp_getsubpages_restapi) - REST API Subpages
- [`mainwp_security_post_data`](#mainwp_security_post_data) - Filters security issues from fixing
- [`mainwp-getsubpages-user`](#mainwp-getsubpages-user) - This hook allows you to add extra sub pages to the User page via the 'mainwp-getsubpages-user' filter.
- [`mainwp_getsubpages_user`](#mainwp_getsubpages_user) - Method init_menu()
- [`mainwp-getsubpages-server`](#mainwp-getsubpages-server) - Filter mainwp_getsubpages_server
- [`mainwp_getsubpages_server`](#mainwp_getsubpages_server) - Method init_menu()
- [`mainwp_info_schedules_cron_listing`](#mainwp_info_schedules_cron_listing) - Renders the Cron Schedule page.
- [`error_log_mainwp_logs`](#error_log_mainwp_logs) - Filter: error_log_mainwp_logs
- [`error_log_mainwp_lines`](#error_log_mainwp_lines) - Filter: error_log_mainwp_lines
- [`mainwp_logger_to_db`](#mainwp_logger_to_db) - Renders action logs page.
- [`mainwp_specific_action_logs`](#mainwp_specific_action_logs) - Renders action logs page.
- [`mainwp_log_specific_actions`](#mainwp_log_specific_actions) - Renders action logs page.
- [`mainwp_logger_to_db`](#mainwp_logger_to_db) - Renders action logs page.
- [`mainwp_getsubpages_tags`](#mainwp_getsubpages_tags) - This hook allows you to add extra sub pages to the Tags page via the 'mainwp-getsubpages-tags' filter.
- [`mainwp-getsubpages-page`](#mainwp-getsubpages-page) - Method init_menu()
- [`mainwp_getsubpages_page`](#mainwp_getsubpages_page) - Method init_menu()
- [`mainwp_pages_table_fatures`](#mainwp_pages_table_fatures) - Filter: mainwp_pages_table_fatures
- [`mainwp_get_all_pages_data`](#mainwp_get_all_pages_data) - Get all pages data
- [`mainwp_posting_bulkpost_post_status`](#mainwp_posting_bulkpost_post_status) - Page status
- [`mainwp_bulkpage_posting`](#mainwp_bulkpage_posting) - Posting new page
- [`mainwp-after-posting-bulkpage-result`](#mainwp-after-posting-bulkpage-result) - After posting a new page
- [`mainwp_after_posting_bulkpage_result`](#mainwp_after_posting_bulkpage_result) - Method posting()
- [`mainwp_cards_per_row`](#mainwp_cards_per_row) - Filter: mainwp_cards_per_row
- [`mainwp_recent_posts_pages_number`](#mainwp_recent_posts_pages_number) - Sets number of recent posts & pages
- [`mainwp_recent_posts_widget_title`](#mainwp_recent_posts_widget_title) - *Arguments*
- [`mainwp_recent_posts_pages_number`](#mainwp_recent_posts_pages_number) - This filter is documented in /widgets/widget-mainwp-recent-posts.php
- [`mainwp_recent_pages_widget_title`](#mainwp_recent_pages_widget_title) - *Arguments*

## Hook Details

### `mainwp_bulkpost_categories_handle`

*Method add_categories_handle()*

Handle adding categories.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.
`wp_unslash($_POST['post_category'])` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-meta-boxes.php](class/class-mainwp-meta-boxes.php), [line 109](class/class-mainwp-meta-boxes.php#L109-L148)



### `mainwp_bulkpost_tags_handle`

*Method add_tags_handle()*

Add Tags to post array handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.
`$post_type` | `string` | Post type.
`wp_strip_all_tags(wp_unslash($_POST['add_tags']))` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-meta-boxes.php](class/class-mainwp-meta-boxes.php), [line 168](class/class-mainwp-meta-boxes.php#L168-L179)



### `mainwp_post_action`

*Fires immediately after post action.*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-actions-handler.php](class/class-mainwp-actions-handler.php), [line 51](class/class-mainwp-actions-handler.php#L51-L56)



### `mainwp_postprocess_backup_site`

*Method  backup_site()*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-backup-handler.php](class/class-mainwp-backup-handler.php), [line 28](class/class-mainwp-backup-handler.php#L28-L512)



### `mainwp_help_sidebar_content`

*Action: mainwp_help_sidebar_content*

Fires Help sidebar content


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 782](class/class-mainwp-ui.php#L782-L789)



### `mainwp_before_mainwp_content_wrap`

*Action: mainwp_before_mainwp_content_wrap*

Fires before the #mainwp-content-wrap element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `array` | Array containing the child site data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 799](class/class-mainwp-ui.php#L799-L808)



### `mainwp_page_navigation_menu`

*Method render_page_navigation()*

Render page navigation.


Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1439](class/class-mainwp-ui.php#L1439-L1519)



### `mainwp_save_bulkpost`

*Action: mainwp_save_bulkpost*

Fires when saving the bulk post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.

Source: [../sources/mainwp-dashboard/class/class-mainwp-bulk-post.php](class/class-mainwp-bulk-post.php), [line 158](class/class-mainwp-bulk-post.php#L158-L167)



### `mainwp_before_redirect_posting_bulkpost`

*Action: mainwp_before_redirect_posting_bulkpost*

Fires before redirection to posting 'bulk post' page after post submission.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `object` | Object containing post data.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-bulk-post.php](class/class-mainwp-bulk-post.php), [line 172](class/class-mainwp-bulk-post.php#L172-L181)



### `mainwp_save_bulkpage`

*Action: mainwp_save_bulkpage*

Fires when saving the bulk page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post ID.

Source: [../sources/mainwp-dashboard/class/class-mainwp-bulk-post.php](class/class-mainwp-bulk-post.php), [line 227](class/class-mainwp-bulk-post.php#L227-L236)



### `mainwp_before_redirect_posting_bulkpage`

*Action: mainwp_before_redirect_posting_bulkpage*

Fires before redirection to posting 'bulk page' page after post submission.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `object` | Object containing post data.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-bulk-post.php](class/class-mainwp-bulk-post.php), [line 241](class/class-mainwp-bulk-post.php#L241-L250)



### `mainwp_register_post_type`

*Method create_post_type()*

Register "Bulkpost" and "Bulkpage" custom post types.


Source: [../sources/mainwp-dashboard/class/class-mainwp-bulk-post.php](class/class-mainwp-bulk-post.php), [line 256](class/class-mainwp-bulk-post.php#L256-L368)



### `mainwp_admin_footer`

*Action: mainwp_admin_footer*

Fires at the bottom of MainWP content.


Source: [../sources/mainwp-dashboard/class/class-mainwp-system-view.php](class/class-mainwp-system-view.php), [line 1020](class/class-mainwp-system-view.php#L1020-L1027)



### `mainwp_pageheader_settings`

*Render settings*

Renders the settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 76](modules/api-backups/classes/class-api-backups-settings.php#L76-L88)



### `mainwp_pagefooter_settings`

*Render settings*

Renders the settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-settings.php](modules/api-backups/classes/class-api-backups-settings.php), [line 76](modules/api-backups/classes/class-api-backups-settings.php#L76-L108)



### `mainwp_pageheader_sites`

*Render Tabs.*

Renders the page tabs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-overview.php](modules/api-backups/classes/class-api-backups-overview.php), [line 76](modules/api-backups/classes/class-api-backups-overview.php#L76-L82)



### `mainwp_pagefooter_sites`

*Render Tabs.*

Renders the page tabs.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ApiBackups'` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-overview.php](modules/api-backups/classes/class-api-backups-overview.php), [line 76](modules/api-backups/classes/class-api-backups-overview.php#L76-L103)



### `mainwp_pageheader_settings`

*This action is documented in ../pages/page-mainwp-manage-sites.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'Insights'` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-settings.php](modules/logs/classes/class-log-settings.php), [line 164](modules/logs/classes/class-log-settings.php#L164-L165)



### `mainwp_pagefooter_settings`

*This action is documented in ../pages/page-mainwp-manage-sites.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'Insights'` |  | 

Source: [../sources/mainwp-dashboard/modules/logs/classes/class-log-settings.php](modules/logs/classes/class-log-settings.php), [line 263](modules/logs/classes/class-log-settings.php#L263-L264)



### `mainwp_module_cost_tracker_help_item`

*Action: mainwp_module_cost_tracker_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Cost Tracker page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`5.0` | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-admin.php](modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 874](modules/cost-tracker/classes/class-cost-tracker-admin.php#L874-L885)



### `mainwp_module_cost_tracker_actions_bar_left`

*Render Actions Bar*

Renders the actions bar on the Dashboard tab.


Source: [../sources/mainwp-dashboard/modules/cost-tracker/pages/page-cost-tracker-dashboard.php](modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 1110](modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L1110-L1125)



### `mainwp_module_cost_tracker_actions_bar_right`

*Render Actions Bar*

Renders the actions bar on the Dashboard tab.


Source: [../sources/mainwp-dashboard/modules/cost-tracker/pages/page-cost-tracker-dashboard.php](modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 1110](modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L1110-L1129)



### `mainwp_tools_form_top`

*Action: mainwp_tools_form_top*

Fires at the top of MainWP tools form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1995](pages/page-mainwp-settings.php#L1995-L2002)



### `mainwp_tools_form_bottom`

*Action: mainwp_tools_form_bottom*

Fires at the bottom of mainwp tools form.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 2132](pages/page-mainwp-settings.php#L2132-L2139)



### `mainwp_bulkpost_before_post`

*Before Post post action*

Fires right before posting the 'bulkpost' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$p_id` | `int` | Page ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 447](pages/page-mainwp-post-page-handler.php#L447-L456)



### `mainwp_posts_posting_popup_actions`

*Method posting()*

Create bulk posts on sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` | `int` | Post or Page ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 419](pages/page-mainwp-post-page-handler.php#L419-L480)



### `mainwp-post-posting-post`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website, $output->added_id[$website->id], $links)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_post_posting_post'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L819)



### `mainwp-bulkposting-done`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($_post, $website, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_bulkposting_done'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L820)



### `mainwp_post_posting_post`

*Posting post*

Fires while posting post.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site data.
`$output->added_id[$website->id]` |  | 
`$links` | `array` | Links.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 822](pages/page-mainwp-post-page-handler.php#L822-L833)



### `mainwp_bulkposting_done`

*Posting post completed*

Fires after the post posting process is completed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `array` | Array containing the post data.
`$website` | `object` | Object containing child site data.
`$output` | `array` | Output data.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 835](pages/page-mainwp-post-page-handler.php#L835-L846)



### `mainwp_manage_posts_bulk_action`

*Method render()*

Render the page content.


Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 539](pages/page-mainwp-post.php#L539-L583)



### `mainwp_posts_bulk_action`

*Action: mainwp_posts_bulk_action*

Adds new action to the Bulk Actions menu on Manage Posts.

Suggested HTML Markup:
<option value="Your custom value">Your custom text</option>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 588](pages/page-mainwp-post.php#L588-L598)



### `mainwp_posts_actions_bar_left`

*Action: mainwp_posts_actions_bar_left*

Fires at the left side of the actions bar on the Posts screen, after the Bulk Actions menu.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 603](pages/page-mainwp-post.php#L603-L610)



### `mainwp_posts_actions_bar_right`

*Action: mainwp_posts_actions_bar_right*

Fires at the right side of the actions bar on the Posts screen.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 615](pages/page-mainwp-post.php#L615-L622)



### `mainwp_manage_posts_sidebar_top`

*Action: mainwp_manage_posts_sidebar_top*

Fires at the top of the sidebar on Manage posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 640](pages/page-mainwp-post.php#L640-L647)



### `mainwp_manage_posts_before_select_sites`

*Action: mainwp_manage_posts_before_select_sites*

Fires before the Select Sites section on Manage posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 651](pages/page-mainwp-post.php#L651-L658)



### `mainwp_manage_posts_after_select_sites`

*Action: mainwp_manage_posts_after_select_sites*

Fires after the Select Sites section on Manage posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 674](pages/page-mainwp-post.php#L674-L681)



### `mainwp_manage_posts_before_search_options`

*Action: mainwp_manage_posts_before_search_options*

Fires before the Search Options on Manage Posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 689](pages/page-mainwp-post.php#L689-L696)



### `mainwp_manage_posts_after_search_options`

*Action: mainwp_manage_posts_after_search_options*

Fires after the Search Options on Manage Posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 719](pages/page-mainwp-post.php#L719-L726)



### `mainwp_manage_posts_before_submit_button`

*Action: mainwp_manage_posts_before_submit_button*

Fires before the Submit Button on Manage Posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 738](pages/page-mainwp-post.php#L738-L745)



### `mainwp_manage_posts_after_submit_button`

*Action: mainwp_manage_posts_after_submit_button*

Fires after the Submit Button on Manage Posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 754](pages/page-mainwp-post.php#L754-L761)



### `mainwp_manage_posts_sidebar_bottom`

*Action: mainwp_manage_posts_sidebar_bottom*

Fires at the bottom of the sidebar on Manage posts.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 765](pages/page-mainwp-post.php#L765-L772)



### `mainwp_before_posts_table`

*Action: mainwp_before_posts_table*

Fires before the Manage Posts table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 934](pages/page-mainwp-post.php#L934-L941)



### `mainwp_posts_table_header`

*Action: mainwp_posts_table_header*

Adds new column header to the Manage posts table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 948](pages/page-mainwp-post.php#L948-L955)



### `mainwp_after_posts_table`

*Action: mainwp_after_posts_table*

Fires after the Manage Posts table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 992](pages/page-mainwp-post.php#L992-L999)



### `mainwp_posts_table_column`

*Action: mainwp_posts_table_column*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1353](pages/page-mainwp-post.php#L1353-L1363)



### `mainwp_manage_posts_action_item`

*Method posts_search_handler()*

Post page search handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 
`$child_to_dash_array` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1282](pages/page-mainwp-post.php#L1282-L1455)



### `mainwp_posts_table_action`

*Action: mainwp_posts_table_action*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1460](pages/page-mainwp-post.php#L1460-L1473)



### `mainwp_top_bulkpost_edit_content`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2108)



### `mainwp_before_bulkpost_editor`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2150)



### `mainwp_bulkpost_edit`

*Edit bulkpost*

First on the Edit post screen after default fields.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` | `object` | Object containing the Post data.
`$post_type` | `string` | Post type.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2233](pages/page-mainwp-post.php#L2233-L2241)



### `add_meta_boxes`

*Edit bulkpost metaboxes*

Fires after all built-in meta boxes have been added.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_type` | `string` | Post type.
`$post` | `object` | Object containing the Post data.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2247](pages/page-mainwp-post.php#L2247-L2257)



### `mainwp_bulkpost_edit_top_side`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post` |  | 
`$post_type` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2287)



### `mainwp_edit_posts_before_submit_button`

*Action: mainwp_edit_posts_before_submit_button*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2318](pages/page-mainwp-post.php#L2318-L2328)



### `mainwp_edit_posts_after_submit_button`

*Action: mainwp_edit_posts_after_submit_button*

Fires right after the Submit button.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2341](pages/page-mainwp-post.php#L2341-L2348)



### `mainwp_posts_help_item`

*Action: mainwp_posts_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Posts page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2743](pages/page-mainwp-post.php#L2743-L2754)



### `mainwp_overview_help_item`

*Action: mainwp_overview_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Overview page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-overview.php](pages/page-mainwp-overview.php), [line 445](pages/page-mainwp-overview.php#L445-L456)



### `mainwp_cron_jobs_list`

*Action: mainwp_cron_jobs_list*

Renders as the last row of the Schedules table.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1137](pages/page-mainwp-server-information.php#L1137-L1144)



### `mainwp_pageheader_tags`

*Sites Page header*

Renders the tabs on the Sites screen.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ManageGroups'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 293](pages/page-mainwp-manage-groups.php#L293-L300)



### `mainwp_pagefooter_tags`

*Sites Page Footer*

Renders the footer on the Sites screen.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'ManageGroups'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 474](pages/page-mainwp-manage-groups.php#L474-L481)



### `mainwp_post_created`

*Method posting_bulk_handler()*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | The website object.
`'newpost'` |  | 
`$information['other_data']['new_post_data']` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-bulk-add.php](pages/page-mainwp-bulk-add.php), [line 34](pages/page-mainwp-bulk-add.php#L34-L57)



### `admin_print_styles`

*Method setup_wizard_header()*

Render Setup Wizard's header.


Source: [../sources/mainwp-dashboard/pages/page-mainwp-setup-wizard.php](pages/page-mainwp-setup-wizard.php), [line 203](pages/page-mainwp-setup-wizard.php#L203-L234)



### `mainwp_pageheader_extensions`

*Method render_extensions_groups()*


Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-groups.php](pages/page-mainwp-extensions-groups.php), [line 921](pages/page-mainwp-extensions-groups.php#L921-L968)



### `mainwp_pagefooter_extensions`

*Method render_extensions_groups()*


Source: [../sources/mainwp-dashboard/pages/page-mainwp-extensions-groups.php](pages/page-mainwp-extensions-groups.php), [line 921](pages/page-mainwp-extensions-groups.php#L921-L1086)



### `mainwp_manage_pages_bulk_action`

*Renders Bulk Page Manager.*


Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 434](pages/page-mainwp-page.php#L434-L474)



### `mainwp_pages_bulk_action`

*Action: mainwp_pages_bulk_action*

Adds new action to the Bulk Actions menu on Manage Pages.

Suggested HTML Markup:
<option value="Your custom value">Your custom text</option>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 479](pages/page-mainwp-page.php#L479-L489)



### `mainwp_pages_actions_bar_left`

*Action: mainwp_pages_actions_bar_left*

Fires at the left side of the actions bar on the Pages screen, after the Bulk Actions menu.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 494](pages/page-mainwp-page.php#L494-L501)



### `mainwp_pages_actions_bar_right`

*Action: mainwp_pages_actions_bar_right*

Fires at the right side of the actions bar on the Pages screen.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 506](pages/page-mainwp-page.php#L506-L513)



### `mainwp_manage_pages_sidebar_top`

*Action: mainwp_manage_pages_sidebar_top*

Fires at the top of the sidebar on Manage pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 531](pages/page-mainwp-page.php#L531-L538)



### `mainwp_manage_pages_before_select_sites`

*Action: mainwp_manage_pages_before_select_sites*

Fires before the Select Sites section on Manage pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 542](pages/page-mainwp-page.php#L542-L549)



### `mainwp_manage_pages_after_select_sites`

*Action: mainwp_manage_pages_after_select_sites*

Fires after the Select Sites section on Manage pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 565](pages/page-mainwp-page.php#L565-L572)



### `mainwp_manage_pages_before_search_options`

*Action: mainwp_manage_pages_before_search_options*

Fires before the Search Options on Manage Pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 580](pages/page-mainwp-page.php#L580-L587)



### `mainwp_manage_pages_after_search_options`

*Action: mainwp_manage_pages_after_search_options*

Fires after the Search Options on Manage Pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 610](pages/page-mainwp-page.php#L610-L617)



### `mainwp_manage_pages_before_submit_button`

*Action: mainwp_manage_pages_before_submit_button*

Fires before the Submit Button on Manage Pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 624](pages/page-mainwp-page.php#L624-L631)



### `mainwp_manage_pages_after_submit_button`

*Action: mainwp_manage_pages_after_submit_button*

Fires after the Submit Button on Manage Pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 640](pages/page-mainwp-page.php#L640-L647)



### `mainwp_manage_pages_sidebar_bottom`

*Action: mainwp_manage_pages_sidebar_bottom*

Fires at the bottom of the sidebar on Manage pages.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 651](pages/page-mainwp-page.php#L651-L658)



### `mainwp_before_pages_table`

*Action: mainwp_before_pages_table*

Fires before the Manage Pages table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 793](pages/page-mainwp-page.php#L793-L800)



### `mainwp_pages_table_header`

*Action: mainwp_pages_table_header*

Adds new column header to the Manage pages table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 807](pages/page-mainwp-page.php#L807-L814)



### `mainwp_after_pages_table`

*Action: mainwp_after_pages_table*

Fires after the Manage Pages table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 842](pages/page-mainwp-page.php#L842-L849)



### `mainwp_pages_table_column`

*Action: mainwp_pages_table_column*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1146](pages/page-mainwp-page.php#L1146-L1156)



### `mainwp_manage_pages_action_item`

*Method pages_search_handler()*

Pages Search handler.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$page` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1095](pages/page-mainwp-page.php#L1095-L1221)



### `mainwp_pages_table_action`

*Action: mainwp_pages_table_action*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1233](pages/page-mainwp-page.php#L1233-L1246)



### `mainwp_bulkpage_before_post`

*Before Page post action*

Fires right before posting the 'bulkpage' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_id` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1427](pages/page-mainwp-page.php#L1427-L1436)



### `mainwp-post-posting-page`

*Method posting()*

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($website, $output->added_id[$website->id], $links)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_post_posting_page'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1385](pages/page-mainwp-page.php#L1385-L1619)



### `mainwp-bulkposting-done`

*Method posting()*

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($_post, $website, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_bulkposting_done'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1385](pages/page-mainwp-page.php#L1385-L1620)



### `mainwp_post_posting_page`

*Posting page*

Fires while posting page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing child site data.
`$output->added_id[$website->id]` |  | 
`$links` | `array` | Links.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1622](pages/page-mainwp-page.php#L1622-L1633)



### `mainwp_bulkposting_done`

*Posting page completed*

Fires after the page posting process is completed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$_post` | `array` | Array containing the post data.
`$website` | `object` | Object containing child site data.
`$output` | `array` | Output data.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1635](pages/page-mainwp-page.php#L1635-L1646)



### `mainwp_pages_posting_popup_actions`

*Method posting()*

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$id` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1385](pages/page-mainwp-page.php#L1385-L1703)



### `mainwp_pages_help_item`

*Action: mainwp_pages_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Pages page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1741](pages/page-mainwp-page.php#L1741-L1752)



### `mainwp_pageheader_sites`

*This action is documented in ../pages/page-mainwp-manage-sites.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'MonitoringSites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-monitoring.php](pages/page-mainwp-monitoring.php), [line 291](pages/page-mainwp-monitoring.php#L291-L292)



### `mainwp_pagefooter_sites`

*This action is documented in ../pages/page-mainwp-manage-sites.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'MonitoringSites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-monitoring.php](pages/page-mainwp-monitoring.php), [line 306](pages/page-mainwp-monitoring.php#L306-L307)



### `mainwp_pageheader_sites`

*Sites Page header*

Renders the tabs on the Sites screen.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'managesites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-screenshots.php](pages/page-mainwp-manage-screenshots.php), [line 215](pages/page-mainwp-manage-screenshots.php#L215-L222)



### `mainwp_pagefooter_sites`

*Sites Page Footer*

Renders the footer on the Sites screen.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'managesites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-screenshots.php](pages/page-mainwp-manage-screenshots.php), [line 446](pages/page-mainwp-manage-screenshots.php#L446-L453)



### `mainwp_recent_posts_widget_top`

*Action: mainwp_recent_posts_widget_top*

Fires at the top of the Recent Posts widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 125](widgets/widget-mainwp-recent-posts.php#L125-L132)



### `mainwp_recent_posts_after_lists`

*Action: mainwp_recent_posts_after_lists*

Fires after the recent posts lists, before the bottom actions section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 144](widgets/widget-mainwp-recent-posts.php#L144-L151)



### `mainwp_recent_posts_widget_bottom`

*Action: mainwp_recent_posts_widget_bottom*

Fires at the bottom of the Recent Posts widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 163](widgets/widget-mainwp-recent-posts.php#L163-L170)



### `mainwp_recent_posts_before_publised_list`

*Action: mainwp_recent_posts_before_publised_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 233](widgets/widget-mainwp-recent-posts.php#L233-L243)



### `mainwp_recent_posts_after_publised_list`

*Action: mainwp_recent_posts_after_publised_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 292](widgets/widget-mainwp-recent-posts.php#L292-L302)



### `mainwp_recent_posts_before_draft_list`

*Action: mainwp_recent_posts_before_draft_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 327](widgets/widget-mainwp-recent-posts.php#L327-L337)



### `mainwp_recent_posts_after_draft_list`

*Action: mainwp_recent_posts_after_draft_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 383](widgets/widget-mainwp-recent-posts.php#L383-L393)



### `mainwp_recent_posts_before_pending_list`

*Action: mainwp_recent_posts_before_pending_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 418](widgets/widget-mainwp-recent-posts.php#L418-L428)



### `mainwp_recent_posts_after_pending_list`

*Action: mainwp_recent_posts_after_pending_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 474](widgets/widget-mainwp-recent-posts.php#L474-L484)



### `mainwp_recent_posts_before_future_list`

*Action: mainwp_recent_posts_before_future_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 509](widgets/widget-mainwp-recent-posts.php#L509-L519)



### `mainwp_recent_posts_after_future_list`

*Action: mainwp_recent_posts_after_future_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 566](widgets/widget-mainwp-recent-posts.php#L566-L576)



### `mainwp_recent_posts_before_trash_list`

*Action: mainwp_recent_posts_before_trash_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 601](widgets/widget-mainwp-recent-posts.php#L601-L611)



### `mainwp_recent_posts_after_trash_list`

*Action: mainwp_recent_posts_after_trash_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 656](widgets/widget-mainwp-recent-posts.php#L656-L666)



### `mainwp_before_post_action`

*Action: mainwp_before_post_action*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 772](widgets/widget-mainwp-recent-posts.php#L772-L779)



### `mainwp_after_post_action`

*Action: mainwp_after_post_action
Fires after post/page publish/unpublish/trash/delete/restore actions.*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 795](widgets/widget-mainwp-recent-posts.php#L795-L801)



### `mainwp_recent_pages_widget_top`

*Action: mainwp_recent_pages_widget_top*

Fires at the top of the Recent Pages widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 119](widgets/widget-mainwp-recent-pages.php#L119-L126)



### `mainwp_recent_pages_after_lists`

*Action: mainwp_recent_pages_after_lists*

Fires after the recent pages lists, before the bottom actions section.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 139](widgets/widget-mainwp-recent-pages.php#L139-L146)



### `mainwp_recent_pages_widget_bottom`

*Action: mainwp_recent_pages_widget_bottom*

Fires at the bottom of the Recent Pages widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 159](widgets/widget-mainwp-recent-pages.php#L159-L166)



### `mainwp_recent_pages_before_publised_list`

*Action: mainwp_recent_pages_before_publised_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 229](widgets/widget-mainwp-recent-pages.php#L229-L239)



### `mainwp_recent_pages_after_publised_list`

*Action: mainwp_recent_pages_after_publised_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 289](widgets/widget-mainwp-recent-pages.php#L289-L299)



### `mainwp_recent_pages_before_draft_list`

*Action: mainwp_recent_pages_before_draft_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 324](widgets/widget-mainwp-recent-pages.php#L324-L334)



### `mainwp_recent_pages_after_draft_list`

*Action: mainwp_recent_pages_after_draft_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 381](widgets/widget-mainwp-recent-pages.php#L381-L391)



### `mainwp_recent_pages_before_pending_list`

*Action: mainwp_recent_pages_before_pending_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 415](widgets/widget-mainwp-recent-pages.php#L415-L425)



### `mainwp_recent_pages_after_pending_list`

*Action: mainwp_recent_pages_after_pending_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 472](widgets/widget-mainwp-recent-pages.php#L472-L482)



### `mainwp_recent_pages_before_future_list`

*Action: mainwp_recent_pages_before_future_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 507](widgets/widget-mainwp-recent-pages.php#L507-L517)



### `mainwp_recent_pages_after_future_list`

*Action: mainwp_recent_pages_after_future_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 565](widgets/widget-mainwp-recent-pages.php#L565-L575)



### `mainwp_recent_pages_before_trash_list`

*Action: mainwp_recent_pages_before_trash_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 600](widgets/widget-mainwp-recent-pages.php#L600-L610)



### `mainwp_recent_pages_after_trash_list`

*Action: mainwp_recent_pages_after_trash_list*

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

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 655](widgets/widget-mainwp-recent-pages.php#L655-L665)

## Filters



### `mainwp_enqueue_script_gridster`

*Method admin_init()*

Do nothing if current user is not an Admin else display the page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$load_gridstack` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-system.php](class/class-mainwp-system.php), [line 766](class/class-mainwp-system.php#L766-L882)



### `mainwp_header_title`

*Filter: mainwp_header_title*

Filter the MainWP page title in the header element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$title` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 488](class/class-mainwp-ui.php#L488-L495)



### `mainwp_header_left`

*Filter: mainwp_header_left*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 505](class/class-mainwp-ui.php#L505-L512)



### `mainwp_header_right`

*Filter: mainwp_header_right*

Filter the MainWP header element right side content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$right` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 516](class/class-mainwp-ui.php#L516-L523)



### `mainwp_sidbar_pages`

*Method render_header_actions()*

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sidebar_pages` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1273](class/class-mainwp-ui.php#L1273-L1286)



### `mainwp_sidebar_pages`

*Method render_header_actions()*

Render header action buttons,
(Sync|Add|Options|Community|User|Updates).

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sidebar_pages` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1273](class/class-mainwp-ui.php#L1273-L1287)



### `mainwp_page_navigation`

*Filter: mainwp_page_navigation*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 1449](class/class-mainwp-ui.php#L1449-L1456)



### `mainwp_sidbar_pages`

*Method render_screen_options()*

Render modal window for Page Settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sidebar_pages` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2421](class/class-mainwp-ui.php#L2421-L2477)



### `mainwp_sidebar_pages`

*Method render_screen_options()*

Render modal window for Page Settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sidebar_pages` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-ui.php](class/class-mainwp-ui.php), [line 2421](class/class-mainwp-ui.php#L2421-L2478)



### `redirect_post_location`

*Filter: redirect_post_location*

Filters the location for the Edit process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$location` |  | 
`$post_id` | `int` | Post ID.

Source: [../sources/mainwp-dashboard/class/class-mainwp-bulk-post.php](class/class-mainwp-bulk-post.php), [line 56](class/class-mainwp-bulk-post.php#L56-L65)



### `mainwp_daily_digest_content`

*Filter: mainwp_daily_digest_content*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification.php](class/class-mainwp-notification.php), [line 210](class/class-mainwp-notification.php#L210-L220)



### `mainwp_send_mail_from_header`

*Method send_wp_mail().*

Send email via wp_mail().

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$email` | `string` | send to email.
`$subject` | `string` | email content.

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification.php](class/class-mainwp-notification.php), [line 317](class/class-mainwp-notification.php#L317-L337)



### `mainwp_page_admin_body_class`

*MainWP Admin body CSS class attributes.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$class_string` | `mixed` | MainWP CSS Class attributes.

Source: [../sources/mainwp-dashboard/class/class-mainwp-system-view.php](class/class-mainwp-system-view.php), [line 944](class/class-mainwp-system-view.php#L944-L991)



### `mainwp_get_post_data_authed`

*Method get_post_data_authed()*

Get authorized $_POST data & build query.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$data` |  | 
`$website` | `mixed` | Array of Child Site Info.
`$what` | `mixed` | What we are posting.
`$params` | `null` | Post parameters.

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 361](class/class-mainwp-connect.php#L361-L393)



### `mainwp_recent_posts_pages_number`

*This filter is documented in ../widgets/widget-mainwp-recent-posts.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`5` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 421](class/class-mainwp-connect.php#L421-L422)



### `mainwp-pre-posting-posts`

*Filter is being replaced with mainwp_pre_posting_posts.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(is_array($params) ? $params : array(), (object) array('id' => $website->id, 'url' => $website->url, 'name' => $website->name))` |  | 
`'4.0.7.2'` |  | 
`// NOSONAR - not IP.
'mainwp_pre_posting_posts'` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 784](class/class-mainwp-connect.php#L784-L801)



### `mainwp_pre_posting_posts`

*Filter: mainwp_pre_posting_posts*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-connect.php](class/class-mainwp-connect.php), [line 803](class/class-mainwp-connect.php#L803-L818)



### `mainwp_subpages_left_menu`

*Method init_subpages_left_menu*

Build left menu subpages array.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$subPages` | `array` | Array of SubPages.
`$initSubpage` | `array` | Initial SubPage Array.
`$parentKey` | `string` | Parent Menu Slug.
`$slug` | `mixed` | SubPage Slug.

Source: [../sources/mainwp-dashboard/class/class-mainwp-menu.php](class/class-mainwp-menu.php), [line 479](class/class-mainwp-menu.php#L479-L497)



### `mainwp_extensions_page_top_header`

*Method render_header()*

Render page header.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$extension_name` |  | 
`$extension_name_raw` |  | 

Source: [../sources/mainwp-dashboard/class/class-mainwp-extensions-view.php](class/class-mainwp-extensions-view.php), [line 50](class/class-mainwp-extensions-view.php#L50-L71)



### `mainwp_pro_reports_generate_content`

*Filter: mainwp_pro_reports_generate_content*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 210](class/class-mainwp-notification-template.php#L210-L217)



### `mainwp_client_report_generate_content`

*Filter: mainwp_client_report_generate_content*

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

Source: [../sources/mainwp-dashboard/class/class-mainwp-notification-template.php](class/class-mainwp-notification-template.php), [line 219](class/class-mainwp-notification-template.php#L219-L226)



### `mainwp_getsubpages_api_backups`

*This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/modules/api-backups/classes/class-api-backups-admin.php](modules/api-backups/classes/class-api-backups-admin.php), [line 234](modules/api-backups/classes/class-api-backups-admin.php#L234-L237)



### `mainwp_getsubpages_cost_tracker`

*This hook allows you to add extra sub pages to the client page via the 'mainwp_getsubpages_cost_tracker' filter.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-admin.php](modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 292](modules/cost-tracker/classes/class-cost-tracker-admin.php#L292-L295)



### `mainwp_escape_content`

*Edit subscription Post*

Handles the saving subscription.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/classes/class-cost-tracker-admin.php](modules/cost-tracker/classes/class-cost-tracker-admin.php), [line 441](modules/cost-tracker/classes/class-cost-tracker-admin.php#L441-L478)



### `mainwp_escape_content`

*Get table rows.*

Optimize for shared hosting or big networks.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/pages/page-cost-tracker-dashboard.php](modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 745](modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L745-L786)



### `mainwp_escape_content`

*Method ajax_notes_save()*

Post handler for save notes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/pages/page-cost-tracker-dashboard.php](modules/cost-tracker/pages/page-cost-tracker-dashboard.php), [line 947](modules/cost-tracker/pages/page-cost-tracker-dashboard.php#L947-L959)



### `mainwp_escape_content`

*Method get_cost_field_value().*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cost->note` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-handle-v1.php](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-handle-v1.php), [line 127](modules/cost-tracker/rest-api/version1/class-cost-tracker-rest-api-handle-v1.php#L127-L190)



### `mainwp_escape_content`

*Handles the saving item.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note` |  | 

Source: [../sources/mainwp-dashboard/modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php), [line 296](modules/cost-tracker/rest-api/version2/class-mainwp-rest-costs-controller.php#L296-L330)



### `mainwp-getsubpages-settings`

*Settings Subpages*

Filters subpages for the Settings page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_settings'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 211](pages/page-mainwp-settings.php#L211-L218)



### `mainwp_getsubpages_settings`

*Instantiate the Settings Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 137](pages/page-mainwp-settings.php#L137-L219)



### `date_formats`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(esc_html__('F j, Y'), 'Y-m-d', 'm/d/Y', 'd/m/Y')` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1139](pages/page-mainwp-settings.php#L1139-L1139)



### `time_formats`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(esc_html__('g:i a'), 'g:i A', 'H:i')` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1179](pages/page-mainwp-settings.php#L1179-L1179)



### `mainwp_show_qsw`

*Render MainWP Tools SubPage.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings.php](pages/page-mainwp-settings.php), [line 1953](pages/page-mainwp-settings.php#L1953-L2004)



### `mainwp_edit_post_get_categories`

*Method ajax_handle_get_categories()*

Get categories.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$website` |  | 
`$_REQUEST` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 156](pages/page-mainwp-post-page-handler.php#L156-L244)



### `mainwp_posts_posting_bulk_sites`

*Method posting_bulk()*

Create bulk posts on sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 396](pages/page-mainwp-post-page-handler.php#L396-L408)



### `mainwp_posting_post_selected_by`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_by` |  | 
`$id` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L626)



### `mainwp_posting_post_selected_sites`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_sites` |  | 
`$id` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L634)



### `mainwp_posting_selected_clients`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$selected_clients` |  | 
`$id` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L636)



### `mainwp_posting_bulkpost_post_status`

*Post status*

Sets post status when posting 'bulkpost' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_status` |  | 
`$id` | `int` | Post ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 682](pages/page-mainwp-post-page-handler.php#L682-L691)



### `mainwp-after-posting-bulkpost-result`

*After posting a new post*

Sets data after the posting process to show the process feedback.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false, $_post, $dbwebsites, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_after_posting_bulkpost_result'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 850](pages/page-mainwp-post-page-handler.php#L850-L861)



### `mainwp_after_posting_bulkpost_result`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$newExtensions` |  | 
`$_post` |  | 
`$dbwebsites` |  | 
`$output` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L866)



### `mainwp_after_posting_delete_bulk_post`

*Method posting_posts()*

Posting posts.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`$posting_succeed` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 588](pages/page-mainwp-post-page-handler.php#L588-L907)



### `mainwp_manageposts_get_post_result`

*Method get_post()*

Get post from child site to edit.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ret` |  | 
`$information['my_post']` |  | 
`$websiteId` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post-page-handler.php](pages/page-mainwp-post-page-handler.php), [line 953](pages/page-mainwp-post-page-handler.php#L953-L1008)



### `mainwp_getsubpages_client`

*Method init_menu()*

Initiate menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-client.php](pages/page-mainwp-client.php), [line 79](pages/page-mainwp-client.php#L79-L141)



### `mainwp_default_emails_fields`

*Method get_defaults_email_settings_value().*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$recipients` |  | 
`$type` | `string` | setting type to get default value.
`$field` | `string` | setting field to get default value.
`$general` | `bool` | general setting.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-settings-indicator.php](pages/page-mainwp-settings-indicator.php), [line 216](pages/page-mainwp-settings-indicator.php#L216-L265)



### `mainwp-getcustompage-backups`

*Backups Subpages*

Filters subpages for the Backups page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getcustompage_backups'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-backups.php](pages/page-mainwp-manage-backups.php), [line 102](pages/page-mainwp-manage-backups.php#L102-L109)



### `mainwp_getcustompage_backups`

*Instantiate Legacy Backups Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$customPage` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-backups.php](pages/page-mainwp-manage-backups.php), [line 90](pages/page-mainwp-manage-backups.php#L90-L110)



### `mainwp-getsubpages-backups`

*Instantiate Legacy Backups Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_backups'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-backups.php](pages/page-mainwp-manage-backups.php), [line 90](pages/page-mainwp-manage-backups.php#L90-L144)



### `mainwp_getsubpages_backups`

*Instantiate Legacy Backups Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-backups.php](pages/page-mainwp-manage-backups.php), [line 90](pages/page-mainwp-manage-backups.php#L90-L145)



### `mainwp-getsubpages-post`

*Method ini_menu()*

Initiate Page menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_post'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 78](pages/page-mainwp-post.php#L78-L123)



### `mainwp_getsubpages_post`

*Method ini_menu()*

Initiate Page menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 78](pages/page-mainwp-post.php#L78-L124)



### `mainwp_edit_bulkpost_getmetaboxes`

*Init custom bulkpost metaboxes.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 151](pages/page-mainwp-post.php#L151-L157)



### `mainwp_posts_search_bulk_sites`

*Method render()*

Render the page content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`0` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 539](pages/page-mainwp-post.php#L539-L732)



### `mainwp_custom_post_types_default`

*Default post types*

Set default custom post types to exclude from the CPT extension options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 871](pages/page-mainwp-post.php#L871-L878)



### `mainwp_posts_table_fatures`

*Filter: mainwp_posts_table_fatures*

Filters the Manage Posts table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1012](pages/page-mainwp-post.php#L1012-L1019)



### `mainwp_get_all_posts_data`

*Get all posts data*

Set search parameters for the fetch process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1221](pages/page-mainwp-post.php#L1221-L1228)



### `postmeta_form_keys`

*Filters values for the meta key dropdown in the Custom Fields meta box.*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1568](pages/page-mainwp-post.php#L1568-L1579)



### `postmeta_form_limit`

*Filters the number of custom fields to retrieve for the drop-down
in the Custom Fields meta box.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`30` |  | 

**Changelog**

Version | Description
------- | -----------
`2.1.0` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1582](pages/page-mainwp-post.php#L1582-L1590)



### `admin_post_thumbnail_size`

*Filters the size used to display the post thumbnail image in the 'Featured Image' meta box.*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1704](pages/page-mainwp-post.php#L1704-L1721)



### `mainwp_admin_post_thumbnail_html`

*Filters the admin post thumbnail HTML markup to return.*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 1761](pages/page-mainwp-post.php#L1761-L1772)



### `mainwp_custom_render_bulkpost`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$post_id` | `mixed` | Post ID.
`$post_type` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2035)



### `mainwp_bulkpost_edit_title`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$note_title` |  | 
`$post` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2078)



### `mainwp_bulkpost_editor_settings`

*Renders bulkpost to edit.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$post` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-post.php](pages/page-mainwp-post.php), [line 2009](pages/page-mainwp-post.php#L2009-L2174)



### `mainwp-getsubpages-sites`

*Initiate menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_sites'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 178](pages/page-mainwp-manage-sites.php#L178-L241)



### `mainwp_getsubpages_sites`

*Initiate menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-sites.php](pages/page-mainwp-manage-sites.php), [line 178](pages/page-mainwp-manage-sites.php#L178-L242)



### `mainwp_getsubpages_restapi`

*REST API Subpages*

Filters subpages for the REST API page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-rest-api-page.php](pages/page-mainwp-rest-api-page.php), [line 116](pages/page-mainwp-rest-api-page.php#L116-L123)



### `mainwp_security_post_data`

*Filters security issues from fixing*

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

Source: [../sources/mainwp-dashboard/pages/page-mainwp-security-issues.php](pages/page-mainwp-security-issues.php), [line 346](pages/page-mainwp-security-issues.php#L346-L358)



### `mainwp-getsubpages-user`

*This hook allows you to add extra sub pages to the User page via the 'mainwp-getsubpages-user' filter.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_user'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-user.php](pages/page-mainwp-user.php), [line 114](pages/page-mainwp-user.php#L114-L119)



### `mainwp_getsubpages_user`

*Method init_menu()*

Initiate menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-user.php](pages/page-mainwp-user.php), [line 68](pages/page-mainwp-user.php#L68-L120)



### `mainwp-getsubpages-server`

*Filter mainwp_getsubpages_server*

Filters subpages for the Info page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_server'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 141](pages/page-mainwp-server-information.php#L141-L148)



### `mainwp_getsubpages_server`

*Method init_menu()*

Initiate Info subPage menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 36](pages/page-mainwp-server-information.php#L36-L149)



### `mainwp_info_schedules_cron_listing`

*Renders the Cron Schedule page.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$cron_jobs` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1000](pages/page-mainwp-server-information.php#L1000-L1042)



### `error_log_mainwp_logs`

*Filter: error_log_mainwp_logs*

Filters the error log files to show.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($error_log)` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1528](pages/page-mainwp-server-information.php#L1528-L1535)



### `error_log_mainwp_lines`

*Filter: error_log_mainwp_lines*

Limits the number of error log records to be displayed. Default value, 50.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`100` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1537](pages/page-mainwp-server-information.php#L1537-L1544)



### `mainwp_logger_to_db`

*Renders action logs page.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1651](pages/page-mainwp-server-information.php#L1651-L1684)



### `mainwp_specific_action_logs`

*Renders action logs page.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific_default` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1651](pages/page-mainwp-server-information.php#L1651-L1703)



### `mainwp_log_specific_actions`

*Renders action logs page.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$specific_logs` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1651](pages/page-mainwp-server-information.php#L1651-L1704)



### `mainwp_logger_to_db`

*Renders action logs page.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-server-information.php](pages/page-mainwp-server-information.php), [line 1651](pages/page-mainwp-server-information.php#L1651-L1759)



### `mainwp_getsubpages_tags`

*This hook allows you to add extra sub pages to the Tags page via the 'mainwp-getsubpages-tags' filter.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`static::$subPages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-groups.php](pages/page-mainwp-manage-groups.php), [line 85](pages/page-mainwp-manage-groups.php#L85-L90)



### `mainwp-getsubpages-page`

*Method init_menu()*

Initiate Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($sub_pages)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_page'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 81](pages/page-mainwp-page.php#L81-L111)



### `mainwp_getsubpages_page`

*Method init_menu()*

Initiate Menu.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 81](pages/page-mainwp-page.php#L81-L112)



### `mainwp_pages_table_fatures`

*Filter: mainwp_pages_table_fatures*

Filters the Manage Pages table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 862](pages/page-mainwp-page.php#L862-L869)



### `mainwp_get_all_pages_data`

*Get all pages data*

Set search parameters for the fetch process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1047](pages/page-mainwp-page.php#L1047-L1054)



### `mainwp_posting_bulkpost_post_status`

*Page status*

Sets page status when posting 'bulkpage' to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_status` |  | 
`$id` | `int` | Page ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1469](pages/page-mainwp-page.php#L1469-L1478)



### `mainwp_bulkpage_posting`

*Posting new page*

Sets Page data to post to child sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 
`$id` | `int` | Page ID.

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1602](pages/page-mainwp-page.php#L1602-L1611)



### `mainwp-after-posting-bulkpage-result`

*After posting a new page*

Sets data after the posting process to show the process feedback.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(false, $_post, $dbwebsites, $output)` |  | 
`'4.0.7.2'` |  | 
`'mainwp_after_posting_bulkpage_result'` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1650](pages/page-mainwp-page.php#L1650-L1661)



### `mainwp_after_posting_bulkpage_result`

*Method posting()*

Render Posting page modal window.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$after_posting` |  | 
`$_post` |  | 
`$dbwebsites` |  | 
`$output` |  | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-page.php](pages/page-mainwp-page.php), [line 1385](pages/page-mainwp-page.php#L1385-L1662)



### `mainwp_cards_per_row`

*Filter: mainwp_cards_per_row*

Filters the number of cards per row in MainWP Screenshots page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'five'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1.8` | 

Source: [../sources/mainwp-dashboard/pages/page-mainwp-manage-screenshots.php](pages/page-mainwp-manage-screenshots.php), [line 247](pages/page-mainwp-manage-screenshots.php#L247-L254)



### `mainwp_recent_posts_pages_number`

*Sets number of recent posts & pages*

Limits the number of recent posts & pages to show in the widget. Min 0, Max 30, Default 5.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`5` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 50](widgets/widget-mainwp-recent-posts.php#L50-L57)



### `mainwp_recent_posts_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Recent Posts', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-posts.php](widgets/widget-mainwp-recent-posts.php), [line 189](widgets/widget-mainwp-recent-posts.php#L189-L189)



### `mainwp_recent_posts_pages_number`

*This filter is documented in /widgets/widget-mainwp-recent-posts.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`5` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 50](widgets/widget-mainwp-recent-pages.php#L50-L51)



### `mainwp_recent_pages_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Recent Pages', 'mainwp')` |  | 

Source: [../sources/mainwp-dashboard/widgets/widget-mainwp-recent-pages.php](widgets/widget-mainwp-recent-pages.php), [line 185](widgets/widget-mainwp-recent-pages.php#L185-L185)


<p align="center"><a href="https://github.com/pronamic/wp-documentor"><img src="https://cdn.jsdelivr.net/gh/pronamic/wp-documentor@main/logos/pronamic-wp-documentor.svgo-min.svg" alt="Pronamic WordPress Documentor" width="32" height="32"></a><br><em>Generated by <a href="https://github.com/pronamic/wp-documentor">Pronamic WordPress Documentor</a> <code>1.2.0</code></em><p>




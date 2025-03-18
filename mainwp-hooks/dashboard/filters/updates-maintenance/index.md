# Updates & Maintenance Filters

Hooks for managing updates to plugins, themes, and WordPress core.

## Navigation

- [Back to All Filters](../index.md)
- [Back to Dashboard Hooks](../../index.md)
- [Back to Main Hooks Documentation](../../../index.md)

## Hooks in this Category

- [`deactivate_{$plugin}`](#deactivate_plugin) - Emulate deactivating, then subsequently reactivating the plugin.
- [`activate_{$plugin}`](#activate_plugin) - Emulate deactivating, then subsequently reactivating the plugin.
- [`mainwp_before_plugin_ignore`](#mainwp_before_plugin_ignore) - Action: mainwp_before_plugin_ignore
- [`mainwp_after_plugin_ignore`](#mainwp_after_plugin_ignore) - Action: mainwp_after_plugin_ignore
- [`mainwp_before_theme_ignore`](#mainwp_before_theme_ignore) - Action: mainwp_before_theme_ignore
- [`mainwp_after_theme_ignore`](#mainwp_after_theme_ignore) - Action: mainwp_after_theme_ignore
- [`mainwp_activated`](#mainwp_activated) - Action: mainwp_activated
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_install_update_actions`](#mainwp_install_update_actions) - Fires immediately after install action.
- [`mainwp_install_plugin_action`](#mainwp_install_plugin_action) - Handle @action mainwp_fetch_url_authed.
- [`mainwp_install_theme_action`](#mainwp_install_theme_action) - Handle @action mainwp_fetch_url_authed.
- [`mainwp_install_theme_action`](#mainwp_install_theme_action) - Handle @action mainwp_fetch_url_authed.
- [`mainwp_prepareinstallplugintheme`](#mainwp_prepareinstallplugintheme) - Method mainwp_ext_prepareinstallplugintheme()
- [`mainwp_performinstallplugintheme`](#mainwp_performinstallplugintheme) - Method mainwp_ext_performinstallplugintheme()
- [`mainwp_header_actions_after_select_themes`](#mainwp_header_actions_after_select_themes) - After select theme actions.
- [`mainwp_before_plugin_theme_install_progress`](#mainwp_before_plugin_theme_install_progress) - Action: mainwp_before_plugin_theme_install_progress
- [`mainwp_after_plugin_theme_install_progress`](#mainwp_after_plugin_theme_install_progress) - Action: mainwp_after_plugin_theme_install_progress
- [`mainwp_install_plugin_theme_modal_action`](#mainwp_install_plugin_theme_modal_action) - Action: mainwp_after_plugin_theme_install_progress
- [`mainwp_select_themes_modal_top`](#mainwp_select_themes_modal_top) - Action: mainwp_select_themes_modal_top
- [`mainwp_select_themes_modal_bottom`](#mainwp_select_themes_modal_bottom) - Action: mainwp_select_themes_modal_bottom
- [`mainwp_widget_updates_actions_top`](#mainwp_widget_updates_actions_top) - Action: mainwp_widget_updates_actions_top
- [`mainwp_updated_site`](#mainwp_updated_site) - Action: mainwp_updated_site
- [`mainwp_install_plugin_card_top`](#mainwp_install_plugin_card_top) - Action: mainwp_install_plugin_card_top
- [`mainwp_install_plugin_card_bottom`](#mainwp_install_plugin_card_bottom) - Action: mainwp_install_plugin_card_bottom
- [`mainwp_db_after_update`](#mainwp_db_after_update) - Method install()
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_delete_key_file`](#mainwp_delete_key_file) - Method update child api key.
- [`mainwp_ajax_add_action`](#mainwp_ajax_add_action) - Init ajax actions.
- [`mainwp_ajax_add_action`](#mainwp_ajax_add_action) - Init ajax actions.
- [`mainwp_module_cost_tracker_email_header`](#mainwp_module_cost_tracker_email_header) - HTTP Check Email Header
- [`mainwp_module_cost_tracker_email_footer`](#mainwp_module_cost_tracker_email_footer) - HTTP Check Email Footer
- [`mainwp_plugins_actions_bar_left`](#mainwp_plugins_actions_bar_left) - Action: mainwp_plugins_actions_bar_left
- [`mainwp_plugins_actions_bar_right`](#mainwp_plugins_actions_bar_right) - Action: mainwp_plugins_actions_bar_right
- [`mainwp_manage_plugins_sidebar_top`](#mainwp_manage_plugins_sidebar_top) - Action: mainwp_manage_plugins_sidebar_top
- [`mainwp_manage_plugins_before_select_sites`](#mainwp_manage_plugins_before_select_sites) - Action: mainwp_manage_plugins_before_select_sites
- [`mainwp_manage_plugins_after_select_sites`](#mainwp_manage_plugins_after_select_sites) - Action: mainwp_manage_plugins_after_select_sites
- [`mainwp_manage_plugins_before_search_options`](#mainwp_manage_plugins_before_search_options) - Action: mainwp_manage_plugins_before_search_options
- [`mainwp_manage_plugins_after_search_options`](#mainwp_manage_plugins_after_search_options) - Action: mainwp_manage_plugins_after_search_options
- [`mainwp_manage_plugins_before_submit_button`](#mainwp_manage_plugins_before_submit_button) - Action: mainwp_manage_plugins_before_submit_button
- [`mainwp_manage_plugins_after_submit_button`](#mainwp_manage_plugins_after_submit_button) - Action: mainwp_manage_plugins_after_submit_button
- [`mainwp_manage_plugins_sidebar_bottom`](#mainwp_manage_plugins_sidebar_bottom) - Action: mainwp_manage_plugins_sidebar_bottom
- [`mainwp_plugins_bulk_action`](#mainwp_plugins_bulk_action) - Action: mainwp_plugins_bulk_action
- [`mainwp_before_plugins_table`](#mainwp_before_plugins_table) - Action: mainwp_before_plugins_table
- [`mainwp_after_plugins_table`](#mainwp_after_plugins_table) - Action: mainwp_after_plugins_table
- [`mainwp_before_plugins_table`](#mainwp_before_plugins_table) - Action: mainwp_before_plugins_table
- [`mainwp_after_plugins_table`](#mainwp_after_plugins_table) - Action: mainwp_after_plugins_table
- [`mainwp_install_plugin_theme_tabs_header_top`](#mainwp_install_plugin_theme_tabs_header_top) - Render Install plugins Table.
- [`mainwp_install_plugins_actions_bar_right`](#mainwp_install_plugins_actions_bar_right) - Install Plugins actions bar (right)
- [`mainwp_install_plugins_actions_bar_left`](#mainwp_install_plugins_actions_bar_left) - Install Plugins actions bar (left)
- [`mainwp_bulk_install_tabs_content`](#mainwp_bulk_install_tabs_content) - Render Install plugins Table.
- [`mainwp_manage_plugins_sidebar_top`](#mainwp_manage_plugins_sidebar_top) - Render Install plugins Table.
- [`mainwp_manage_plugins_before_select_sites`](#mainwp_manage_plugins_before_select_sites) - Render Install plugins Table.
- [`mainwp_manage_plugins_after_select_sites`](#mainwp_manage_plugins_after_select_sites) - Render Install plugins Table.
- [`mainwp_manage_plugins_before_search_options`](#mainwp_manage_plugins_before_search_options) - Render Install plugins Table.
- [`mainwp_manage_plugins_after_search_options`](#mainwp_manage_plugins_after_search_options) - Render Install plugins Table.
- [`mainwp_manage_plugins_before_submit_button`](#mainwp_manage_plugins_before_submit_button) - Render Install plugins Table.
- [`mainwp_manage_plugins_before_submit_button`](#mainwp_manage_plugins_before_submit_button) - Render Install plugins Table.
- [`mainwp_bulk_install_sidebar_submit_bottom`](#mainwp_bulk_install_sidebar_submit_bottom) - Render Install plugins Table.
- [`mainwp_manage_plugins_sidebar_bottom`](#mainwp_manage_plugins_sidebar_bottom) - Render Install plugins Table.
- [`mainwp_plugins_auto_updates_bulk_action`](#mainwp_plugins_auto_updates_bulk_action) - Action: mainwp_plugins_auto_updates_bulk_action
- [`mainwp_manage_plugins_sidebar_top`](#mainwp_manage_plugins_sidebar_top) - Render Autoupdate SubPage.
- [`mainwp_manage_plugins_before_search_options`](#mainwp_manage_plugins_before_search_options) - Render Autoupdate SubPage.
- [`mainwp_manage_plugins_after_search_options`](#mainwp_manage_plugins_after_search_options) - Render Autoupdate SubPage.
- [`mainwp_manage_plugins_before_submit_button`](#mainwp_manage_plugins_before_submit_button) - Render Autoupdate SubPage.
- [`mainwp_manage_plugins_after_submit_button`](#mainwp_manage_plugins_after_submit_button) - Render Autoupdate SubPage.
- [`mainwp_manage_plugins_sidebar_bottom`](#mainwp_manage_plugins_sidebar_bottom) - Render Autoupdate SubPage.
- [`mainwp_plugins_before_auto_updates_table`](#mainwp_plugins_before_auto_updates_table) - Action: mainwp_plugins_before_auto_updates_table
- [`mainwp_plugins_after_auto_updates_table`](#mainwp_plugins_after_auto_updates_table) - Action: mainwp_plugins_after_auto_updates_table
- [`mainwp_plugins_before_ignored_updates`](#mainwp_plugins_before_ignored_updates) - Action: mainwp_plugins_before_ignored_updates
- [`mainwp_plugins_after_ignored_updates`](#mainwp_plugins_after_ignored_updates) - Action: mainwp_plugins_after_ignored_updates
- [`mainwp_plugins_before_ignored_abandoned`](#mainwp_plugins_before_ignored_abandoned) - Action: mainwp_plugins_before_ignored_abandoned
- [`mainwp_plugins_after_ignored_abandoned`](#mainwp_plugins_after_ignored_abandoned) - Action: mainwp_plugins_after_ignored_abandoned
- [`mainwp_plugins_help_item`](#mainwp_plugins_help_item) - Action: mainwp_plugins_help_item
- [`mainwp_applypluginsettings_{$ext_dir_slug}`](#mainwp_applypluginsettings_ext_dir_slug) - Apply plugin settings
- [`mainwp_admin_pass_sidebar_top`](#mainwp_admin_pass_sidebar_top) - Action: mainwp_admin_pass_sidebar_top
- [`mainwp_admin_pass_before_select_sites`](#mainwp_admin_pass_before_select_sites) - Action: mainwp_admin_pass_before_select_sites
- [`mainwp_admin_pass_after_select_sites`](#mainwp_admin_pass_after_select_sites) - Action: mainwp_admin_pass_after_select_sites
- [`mainwp_admin_pass_before_pass_form`](#mainwp_admin_pass_before_pass_form) - Action: mainwp_admin_pass_before_pass_form
- [`mainwp_admin_pass_after_pass_form`](#mainwp_admin_pass_after_pass_form) - Action: mainwp_admin_pass_after_pass_form
- [`mainwp_admin_pass_before_submit_button`](#mainwp_admin_pass_before_submit_button) - Action: mainwp_admin_pass_before_submit_button
- [`mainwp_admin_pass_after_submit_button`](#mainwp_admin_pass_after_submit_button) - Action: mainwp_admin_pass_after_submit_button
- [`mainwp_admin_pass_sidebar_bottom`](#mainwp_admin_pass_sidebar_bottom) - Action: mainwp_admin_pass_sidebar_bottom
- [`mainwp_client_updated`](#mainwp_client_updated) - Add client
- [`mainwp_update_site`](#mainwp_update_site) - Update site
- [`mainwp_before_plugin_ignore`](#mainwp_before_plugin_ignore) - Action: mainwp_before_plugin_ignore
- [`mainwp_after_plugin_ignore`](#mainwp_after_plugin_ignore) - Action: mainwp_after_plugin_ignore
- [`mainwp_before_plugin_action`](#mainwp_before_plugin_action) - Action: mainwp_before_plugin_action
- [`mainwp_after_plugin_action`](#mainwp_after_plugin_action) - Action: mainwp_after_plugin_action
- [`mainwp_cores_before_ignored_updates`](#mainwp_cores_before_ignored_updates) - Action: mainwp_cores_before_ignored_updates
- [`mainwp_cores_after_ignored_updates`](#mainwp_cores_after_ignored_updates) - Action: mainwp_cores_after_ignored_updates
- [`mainwp_update_backuptask`](#mainwp_update_backuptask) - Update backup task.
- [`mainwp_before_plugin_theme_install`](#mainwp_before_plugin_theme_install) - Action: mainwp_before_plugin_theme_install
- [`mainwp_after_plugin_theme_install`](#mainwp_after_plugin_theme_install) - Action: mainwp_after_plugin_theme_install
- [`mainwp_before_plugin_theme_install`](#mainwp_before_plugin_theme_install) - Action: mainwp_before_plugin_theme_install
- [`mainwp_after_plugin_theme_install`](#mainwp_after_plugin_theme_install) - Action: mainwp_after_plugin_theme_install
- [`mainwp_before_plugin_privacy_section`](#mainwp_before_plugin_privacy_section) - Action: mainwp_before_plugin_privacy_section
- [`mainwp_after_plugin_privacy_section`](#mainwp_after_plugin_privacy_section) - Action: mainwp_after_plugin_privacy_section
- [`mainwp_updates_before_wp_updates`](#mainwp_updates_before_wp_updates) - Action: mainwp_updates_before_wp_updates
- [`mainwp_updates_after_wp_updates`](#mainwp_updates_after_wp_updates) - Action: mainwp_updates_after_wp_updates
- [`mainwp_updates_before_plugin_updates`](#mainwp_updates_before_plugin_updates) - Action: mainwp_updates_before_plugin_updates
- [`mainwp_updates_perplugin_before_plugin_updates`](#mainwp_updates_perplugin_before_plugin_updates) - Action: mainwp_updates_perplugin_before_plugin_updates
- [`mainwp_updates_perplugin_after_plugin_updates`](#mainwp_updates_perplugin_after_plugin_updates) - Action: mainwp_updates_perplugin_after_plugin_updates
- [`mainwp_updates_after_plugin_updates`](#mainwp_updates_after_plugin_updates) - Action: mainwp_updates_after_plugin_updates
- [`mainwp_updates_before_theme_updates`](#mainwp_updates_before_theme_updates) - Action: mainwp_updates_before_theme_updates
- [`mainwp_updates_pertheme_before_theme_updates`](#mainwp_updates_pertheme_before_theme_updates) - Action: mainwp_updates_pertheme_before_theme_updates
- [`mainwp_updates_pertheme_after_theme_updates`](#mainwp_updates_pertheme_after_theme_updates) - Action: mainwp_updates_pertheme_after_theme_updates
- [`mainwp_updates_after_theme_updates`](#mainwp_updates_after_theme_updates) - Action: mainwp_updates_after_theme_updates
- [`mainwp_updates_before_translation_updates`](#mainwp_updates_before_translation_updates) - Action: mainwp_updates_before_translation_updates
- [`mainwp_updates_pertranslation_before_translation_updates`](#mainwp_updates_pertranslation_before_translation_updates) - Action: mainwp_updates_pertranslation_before_translation_updates
- [`mainwp_updates_pertranslation_after_translation_updates`](#mainwp_updates_pertranslation_after_translation_updates) - Action: mainwp_updates_pertranslation_after_translation_updates
- [`mainwp_updates_after_translation_updates`](#mainwp_updates_after_translation_updates) - Action: mainwp_updates_after_translation_updates
- [`mainwp_updates_before_abandoned_plugins`](#mainwp_updates_before_abandoned_plugins) - Action: mainwp_updates_before_abandoned_plugins
- [`mainwp_updates_perplugin_before_abandoned_plugins`](#mainwp_updates_perplugin_before_abandoned_plugins) - Action: mainwp_updates_perplugin_before_abandoned_plugins
- [`mainwp_updates_perplugin_after_abandoned_plugins`](#mainwp_updates_perplugin_after_abandoned_plugins) - Action: mainwp_updates_perplugin_after_abandoned_plugins
- [`mainwp_updates_after_abandoned_plugins`](#mainwp_updates_after_abandoned_plugins) - Action: mainwp_updates_after_abandoned_plugins
- [`mainwp_updates_before_abandoned_themes`](#mainwp_updates_before_abandoned_themes) - Action: mainwp_updates_before_abandoned_themes
- [`mainwp_updates_pertheme_before_abandoned_themes`](#mainwp_updates_pertheme_before_abandoned_themes) - Action: mainwp_updates_pertheme_before_abandoned_themes
- [`mainwp_updates_pertheme_after_abandoned_themes`](#mainwp_updates_pertheme_after_abandoned_themes) - Action: mainwp_updates_pertheme_after_abandoned_themes
- [`mainwp_updates_after_abandoned_themes`](#mainwp_updates_after_abandoned_themes) - Action: mainwp_updates_after_abandoned_themes
- [`mainwp_updates_before_nav_tabs`](#mainwp_updates_before_nav_tabs) - Action: mainwp_updates_before_nav_tabs
- [`mainwp_updates_after_nav_tabs`](#mainwp_updates_after_nav_tabs) - Action: mainwp_updates_after_nav_tabs
- [`mainwp_updates_before_actions_bar`](#mainwp_updates_before_actions_bar) - Action: mainwp_updates_before_actions_bar
- [`mainwp_widget_updates_actions_top`](#mainwp_widget_updates_actions_top) - Action: mainwp_widget_updates_actions_top
- [`mainwp_updates_after_actions_bar`](#mainwp_updates_after_actions_bar) - Action: mainwp_updates_after_actions_bar
- [`mainwp_updates_help_item`](#mainwp_updates_help_item) - Action: mainwp_updates_help_item
- [`mainwp_before_theme_action`](#mainwp_before_theme_action) - Action: mainwp_before_theme_action
- [`mainwp_after_theme_action`](#mainwp_after_theme_action) - Action: mainwp_after_theme_action
- [`mainwp_before_theme_ignore`](#mainwp_before_theme_ignore) - Action: mainwp_before_theme_ignore
- [`mainwp_after_theme_ignore`](#mainwp_after_theme_ignore) - Action: mainwp_after_theme_ignore
- [`mainwp_after_upgrade_wp_success`](#mainwp_after_upgrade_wp_success) - Method upgrade_site()
- [`mainwp_before_wp_update`](#mainwp_before_wp_update) - Action: mainwp_before_wp_update
- [`mainwp_after_wp_update`](#mainwp_after_wp_update) - Action: mainwp_after_wp_update
- [`mainwp_before_plugin_ignore`](#mainwp_before_plugin_ignore) - Action: mainwp_before_plugin_ignore
- [`mainwp_after_plugin_ignore`](#mainwp_after_plugin_ignore) - Action: mainwp_after_plugin_ignore
- [`mainwp_before_theme_ignore`](#mainwp_before_theme_ignore) - Action: mainwp_before_theme_ignore
- [`mainwp_after_theme_ignore`](#mainwp_after_theme_ignore) - Action: mainwp_after_theme_ignore
- [`mainwp_before_plugin_theme_unignore`](#mainwp_before_plugin_theme_unignore) - Action: mainwp_before_plugin_theme_unignore
- [`mainwp_before_plugin_unignore`](#mainwp_before_plugin_unignore) - Action: mainwp_before_plugin_unignore
- [`mainwp_after_plugin_unignore`](#mainwp_after_plugin_unignore) - Action: mainwp_after_plugin_unignore
- [`mainwp_before_theme_unignore`](#mainwp_before_theme_unignore) - Action: mainwp_before_theme_unignore
- [`mainwp_after_theme_unignore`](#mainwp_after_theme_unignore) - Action: mainwp_after_theme_unignore
- [`mainwp_before_plugin_unignore`](#mainwp_before_plugin_unignore) - Action: mainwp_before_plugin_unignore
- [`mainwp_after_plugin_unignore`](#mainwp_after_plugin_unignore) - Action: mainwp_after_plugin_unignore
- [`mainwp_before_theme_unignore`](#mainwp_before_theme_unignore) - Action: mainwp_before_theme_unignore
- [`mainwp_after_theme_unignore`](#mainwp_after_theme_unignore) - Action: mainwp_after_theme_unignore
- [`mainwp_before_core_unignore`](#mainwp_before_core_unignore) - Action: mainwp_before_core_unignore
- [`mainwp_before_core_unignore`](#mainwp_before_core_unignore) - Action: mainwp_after_core_unignore
- [`mainwp_before_core_unignore`](#mainwp_before_core_unignore) - Action: mainwp_before_core_unignore
- [`mainwp_after_core_unignore`](#mainwp_after_core_unignore) - Action: mainwp_after_core_unignore
- [`mainwp_before_plugin_theme_translation_update`](#mainwp_before_plugin_theme_translation_update) - Action: mainwp_before_plugin_theme_translation_update
- [`mainwp_after_plugin_theme_translation_update`](#mainwp_after_plugin_theme_translation_update) - Action: mainwp_after_plugin_theme_translation_update
- [`mainwp_themes_actions_bar_left`](#mainwp_themes_actions_bar_left) - Action: mainwp_themes_actions_bar_left
- [`mainwp_themes_actions_bar_right`](#mainwp_themes_actions_bar_right) - Action: mainwp_themes_actions_bar_right
- [`mainwp_manage_themes_sidebar_top`](#mainwp_manage_themes_sidebar_top) - Action: mainwp_manage_themes_sidebar_top
- [`mainwp_manage_themes_before_select_sites`](#mainwp_manage_themes_before_select_sites) - Action: mainwp_manage_themes_before_select_sites
- [`mainwp_manage_themes_after_select_sites`](#mainwp_manage_themes_after_select_sites) - Action: mainwp_manage_themes_after_select_sites
- [`mainwp_manage_themes_before_search_options`](#mainwp_manage_themes_before_search_options) - Action: mainwp_manage_themes_before_search_options
- [`mainwp_manage_themes_after_search_options`](#mainwp_manage_themes_after_search_options) - Action: mainwp_manage_themes_after_search_options
- [`mainwp_manage_themes_before_submit_button`](#mainwp_manage_themes_before_submit_button) - Action: mainwp_manage_themes_before_submit_button
- [`mainwp_manage_themes_after_submit_button`](#mainwp_manage_themes_after_submit_button) - Action: mainwp_manage_themes_after_submit_button
- [`mainwp_manage_themes_sidebar_bottom`](#mainwp_manage_themes_sidebar_bottom) - Action: mainwp_manage_themes_sidebar_bottom
- [`mainwp_before_themes_table`](#mainwp_before_themes_table) - Action: mainwp_before_themes_table
- [`mainwp_after_themes_table`](#mainwp_after_themes_table) - Action: mainwp_after_themes_table
- [`mainwp_before_themes_table`](#mainwp_before_themes_table) - Action: mainwp_before_themes_table
- [`mainwp_after_themes_table`](#mainwp_after_themes_table) - Action: mainwp_after_themes_table
- [`mainwp_themes_bulk_action`](#mainwp_themes_bulk_action) - Action: mainwp_themes_bulk_action
- [`mainwp_install_plugin_theme_tabs_header_top`](#mainwp_install_plugin_theme_tabs_header_top) - Render the Themes table for the Install Themes Tab.
- [`mainwp_install_themes_actions_bar_right`](#mainwp_install_themes_actions_bar_right) - Install Themes actions bar (right)
- [`mainwp_install_themes_actions_bar_left`](#mainwp_install_themes_actions_bar_left) - Install Themes actions bar (left)
- [`mainwp_bulk_install_tabs_content`](#mainwp_bulk_install_tabs_content) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_sidebar_top`](#mainwp_manage_themes_sidebar_top) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_before_select_sites`](#mainwp_manage_themes_before_select_sites) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_after_select_sites`](#mainwp_manage_themes_after_select_sites) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_before_search_options`](#mainwp_manage_themes_before_search_options) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_after_search_options`](#mainwp_manage_themes_after_search_options) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_before_submit_button`](#mainwp_manage_themes_before_submit_button) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_after_submit_button`](#mainwp_manage_themes_after_submit_button) - Render the Themes table for the Install Themes Tab.
- [`mainwp_bulk_install_sidebar_submit_bottom`](#mainwp_bulk_install_sidebar_submit_bottom) - Render the Themes table for the Install Themes Tab.
- [`mainwp_manage_themes_sidebar_bottom`](#mainwp_manage_themes_sidebar_bottom) - Render the Themes table for the Install Themes Tab.
- [`mainwp_install_theme_card_template_bottom`](#mainwp_install_theme_card_template_bottom) - Render the Themes table for the Install Themes Tab.
- [`mainwp_themes_auto_updates_bulk_action`](#mainwp_themes_auto_updates_bulk_action) - Action: mainwp_themes_auto_updates_bulk_action
- [`mainwp_manage_themes_sidebar_top`](#mainwp_manage_themes_sidebar_top) - Render the Themes Auto Update Tab.
- [`mainwp_manage_themes_before_search_options`](#mainwp_manage_themes_before_search_options) - Render the Themes Auto Update Tab.
- [`mainwp_manage_themes_after_search_options`](#mainwp_manage_themes_after_search_options) - Render the Themes Auto Update Tab.
- [`mainwp_manage_themes_before_submit_button`](#mainwp_manage_themes_before_submit_button) - Render the Themes Auto Update Tab.
- [`mainwp_manage_themes_after_submit_button`](#mainwp_manage_themes_after_submit_button) - Render the Themes Auto Update Tab.
- [`mainwp_manage_themes_sidebar_bottom`](#mainwp_manage_themes_sidebar_bottom) - Render the Themes Auto Update Tab.
- [`mainwp_themes_before_auto_updates_table`](#mainwp_themes_before_auto_updates_table) - Action: mainwp_themes_before_auto_updates_table
- [`mainwp_themes_after_auto_updates_table`](#mainwp_themes_after_auto_updates_table) - Action: mainwp_themes_after_auto_updates_table
- [`mainwp_themes_before_ignored_updates`](#mainwp_themes_before_ignored_updates) - Action: mainwp_themes_before_ignored_updates
- [`mainwp_themes_after_ignored_updates`](#mainwp_themes_after_ignored_updates) - Action: mainwp_themes_after_ignored_updates
- [`mainwp_themes_before_ignored_abandoned`](#mainwp_themes_before_ignored_abandoned) - Action: mainwp_themes_before_ignored_abandoned
- [`mainwp_themes_after_ignored_abandoned`](#mainwp_themes_after_ignored_abandoned) - Action: mainwp_themes_after_ignored_abandoned
- [`mainwp_themes_help_item`](#mainwp_themes_help_item) - Action: mainwp_themes_help_item
- [`mainwp_plugins_widget_top`](#mainwp_plugins_widget_top) - Action: mainwp_plugins_widget_top
- [`mainwp_before_active_plugins_list`](#mainwp_before_active_plugins_list) - Action: mainwp_before_active_plugins_list
- [`mainwp_after_active_plugins_list`](#mainwp_after_active_plugins_list) - Action: mainwp_after_active_plugins_list
- [`mainwp_before_inactive_plugins_list`](#mainwp_before_inactive_plugins_list) - Action: mainwp_before_inactive_plugins_list
- [`mainwp_after_inactive_plugins_list`](#mainwp_after_inactive_plugins_list) - Action: mainwp_after_inactive_plugins_list
- [`mainwp_plugins_widget_bottom`](#mainwp_plugins_widget_bottom) - Action: mainwp_plugins_widget_bottom
- [`mainwp_before_plugin_action`](#mainwp_before_plugin_action) - Action: mainwp_before_plugin_action
- [`mainwp_after_plugin_action`](#mainwp_after_plugin_action) - Action: mainwp_after_plugin_action
- [`mainwp_themes_widget_top`](#mainwp_themes_widget_top) - Action: mainwp_themes_widget_top
- [`mainwp_before_inactive_themes_list`](#mainwp_before_inactive_themes_list) - Action: mainwp_before_inactive_themes_list
- [`mainwp_after_inactive_themes_list`](#mainwp_after_inactive_themes_list) - Action: mainwp_after_inactive_themes_list
- [`mainwp_themes_widget_bottom`](#mainwp_themes_widget_bottom) - Action: mainwp_themes_widget_bottom
- [`mainwp_before_theme_action`](#mainwp_before_theme_action) - Action: mainwp_before_theme_action
- [`mainwp_after_theme_action`](#mainwp_after_theme_action) - Action: mainwp_after_theme_action
- [`mainwp_updates_overview_after_update_details`](#mainwp_updates_overview_after_update_details) - Action: mainwp_updates_overview_after_update_details
- [`mainwp_updates_overview_before_total_updates`](#mainwp_updates_overview_before_total_updates) - Action: mainwp_updates_overview_before_total_updates
- [`mainwp_updates_overview_after_total_updates`](#mainwp_updates_overview_after_total_updates) - Action: mainwp_updates_overview_after_total_updates
- [`mainwp_updates_overview_before_update_details`](#mainwp_updates_overview_before_update_details) - Action: mainwp_updates_overview_before_update_details
- [`mainwp_updates_overview_before_wordpress_updates`](#mainwp_updates_overview_before_wordpress_updates) - Action: mainwp_updates_overview_before_wordpress_updates
- [`mainwp_updates_overview_after_wordpress_updates`](#mainwp_updates_overview_after_wordpress_updates) - Action: mainwp_updates_overview_after_wordpress_updates
- [`mainwp_updates_overview_before_plugin_updates`](#mainwp_updates_overview_before_plugin_updates) - Action: mainwp_updates_overview_before_plugin_updates
- [`mainwp_updates_overview_after_plugin_updates`](#mainwp_updates_overview_after_plugin_updates) - Action: mainwp_updates_overview_after_plugin_updates
- [`mainwp_updates_overview_before_theme_updates`](#mainwp_updates_overview_before_theme_updates) - Action: mainwp_updates_overview_before_theme_updates
- [`mainwp_updates_overview_after_theme_updates`](#mainwp_updates_overview_after_theme_updates) - Action: mainwp_updates_overview_after_theme_updates
- [`mainwp_updates_overview_before_translation_updates`](#mainwp_updates_overview_before_translation_updates) - Action: mainwp_updates_overview_before_translation_updates
- [`mainwp_updates_overview_after_translation_updates`](#mainwp_updates_overview_after_translation_updates) - Action: mainwp_updates_overview_after_translation_updates
- [`mainwp_updates_overview_before_abandoned_plugins_themes`](#mainwp_updates_overview_before_abandoned_plugins_themes) - Action: mainwp_updates_overview_before_abandoned_plugins_themes
- [`mainwp_updates_overview_after_abandoned_plugins_themes`](#mainwp_updates_overview_after_abandoned_plugins_themes) - Action: mainwp_updates_overview_after_abandoned_plugins_themes
- [`mainwp_updatesoverview_widget_bottom`](#mainwp_updatesoverview_widget_bottom) - Action: mainwp_updatesoverview_widget_bottom
- [`mainwp_load_text_domain`](#mainwp_load_text_domain) - Method localization()
- [`mainwp_cron_bulk_update_items_limit`](#mainwp_cron_bulk_update_items_limit) - Method handle_cron_batch_updates()
- [`mainwp_api_manager_upgrade_url`](#mainwp_api_manager_upgrade_url) - Get Upgrade URL.
- [`mainwp_update_cached_icons`](#mainwp_update_cached_icons) - Method update_cached_icons().
- [`mainwp_get_plugin_theme_icon`](#mainwp_get_plugin_theme_icon) - Gets a plugin icon via API from WordPress.org
- [`mainwp_forced_get_plugin_theme_icon`](#mainwp_forced_get_plugin_theme_icon) - Gets a plugin icon via API from WordPress.org
- [`mainwp_get_plugin_theme_icon`](#mainwp_get_plugin_theme_icon) - Gets a theme icon via API from WordPress.org
- [`mainwp_forced_get_plugin_theme_icon`](#mainwp_forced_get_plugin_theme_icon) - Gets a theme icon via API from WordPress.org
- [`mainwp_plugin_theme_icon_cache_days`](#mainwp_plugin_theme_icon_cache_days) - Gets a plugin|theme icon to output.
- [`mainwp_cache_icon_expired`](#mainwp_cache_icon_expired) - Gets a plugin|theme icon to output.
- [`mainwp_updates_table_columns_header`](#mainwp_updates_table_columns_header) - Get column info.
- [`mainwp_updates_table_header_content`](#mainwp_updates_table_header_content) - Echo the column headers.
- [`mainwp_updates_table_row_columns`](#mainwp_updates_table_row_columns) - Echo columns.
- [`mainwp_update_plugintheme_max`](#mainwp_update_plugintheme_max) - Filter: mainwp_update_plugintheme_max
- [`mainwp_show_all_updates_button_text`](#mainwp_show_all_updates_button_text) - *Arguments*
- [`mainwp_plugin_information_sslverify`](#mainwp_plugin_information_sslverify) - Sends and receives data to and from the server API.
- [`mainwp_api_manager_upgrade_package_url`](#mainwp_api_manager_upgrade_package_url) - 
- [`mainwp_plugins_install_checks`](#mainwp_plugins_install_checks) - Method get_plugins_install_check()
- [`mainwp_updatescheck_sendmail_at_time`](#mainwp_updatescheck_sendmail_at_time) - Filter: mainwp_updatescheck_sendmail_at_time
- [`mainwp_updatescheck_hours_interval`](#mainwp_updatescheck_hours_interval) - Filter: mainwp_updatescheck_hours_interval
- [`mainwp_detect_premiums_updates`](#mainwp_detect_premiums_updates) - Filter: mainwp_detect_premiums_updates
- [`mainwp_detect_premium_plugins_update`](#mainwp_detect_premium_plugins_update) - Filter: mainwp_detect_premium_plugins_update
- [`mainwp_detect_premium_themes_update`](#mainwp_detect_premium_themes_update) - Filter: mainwp_detect_premium_themes_update
- [`mainwp_request_update_premium_plugins`](#mainwp_request_update_premium_plugins) - Filter: mainwp_request_update_premium_plugins
- [`mainwp_request_update_premium_themes`](#mainwp_request_update_premium_themes) - Filter: mainwp_request_update_premium_themes
- [`mainwp_uptime_monitoring_update_monitor_data`](#mainwp_uptime_monitoring_update_monitor_data) - Method handle_save_settings
- [`mainwp_default_template_source_dir`](#mainwp_default_template_source_dir) - Locate a template and return the path for inclusion.
- [`mainwp_update_uptime_monitor_data`](#mainwp_update_uptime_monitor_data) - Method update_uptime_global_settings
- [`mainwp_available_updates_count_custom_fields_data`](#mainwp_available_updates_count_custom_fields_data) - Method sites_available_updates_count()
- [`mainwp_database_updater_supported_plugins`](#mainwp_database_updater_supported_plugins) - Method sites_available_updates_count()
- [`mainwp_db_install_tables`](#mainwp_db_install_tables) - Method install()
- [`mainwp_cron_bulk_update_items_limit`](#mainwp_cron_bulk_update_items_limit) - Method handle_cron_auto_updates()
- [`mainwp-getsubpages-plugins`](#mainwp-getsubpages-plugins) - Plugins Subpages
- [`mainwp_getsubpages_plugins`](#mainwp_getsubpages_plugins) - Instantiate Main Plugins Menu.
- [`mainwp_manage_plugin_theme_hide_show_updates_per`](#mainwp_manage_plugin_theme_hide_show_updates_per) - Method render_select_manage_view().
- [`file_mod_allowed`](#file_mod_allowed) - Disables plugin installation
- [`mainwp_plugin_auto_updates_table_fatures`](#mainwp_plugin_auto_updates_table_fatures) - Filter: mainwp_plugin_auto_updates_table_fatures
- [`mainwp_update_admin_password_complexity`](#mainwp_update_admin_password_complexity) - Filter: mainwp_update_admin_password_complexity
- [`mainwp_file_uploader_chunk_size`](#mainwp_file_uploader_chunk_size) - Method render_upload()
- [`mainwp_prepare_install_download_url`](#mainwp_prepare_install_download_url) - Method prepare_install()
- [`mainwp_bulk_prepare_install_result`](#mainwp_bulk_prepare_install_result) - Filter: mainwp_bulk_prepare_install_result
- [`mainwp_perform_install_data`](#mainwp_perform_install_data) - Perform insatallation additional data
- [`mainwp_installbulk_prepareupload`](#mainwp_installbulk_prepareupload) - Prepare upload
- [`mainwp_perform_install_data`](#mainwp_perform_install_data) - This filter is documented in pages/page-mainwp-install-bulk.php
- [`mainwp_bulk_upload_install_result`](#mainwp_bulk_upload_install_result) - Filter: mainwp_bulk_upload_install_result
- [`mainwp_sub_leftmenu_updates`](#mainwp_sub_leftmenu_updates) - Initiates Updates menu.
- [`mainwp_updates_translation_sort_by`](#mainwp_updates_translation_sort_by) - Filter: mainwp_updates_translation_sort_by
- [`mainwp_updates_plugins_sort_by`](#mainwp_updates_plugins_sort_by) - Filter: mainwp_updates_plugins_sort_by
- [`mainwp_updates_themes_sort_by`](#mainwp_updates_themes_sort_by) - Filter: mainwp_updates_themes_sort_by
- [`mainwp_updates_abandoned_plugins_sort_by`](#mainwp_updates_abandoned_plugins_sort_by) - Filter: mainwp_updates_abandoned_plugins_sort_by
- [`mainwp_updates_abandoned_themes_sort_by`](#mainwp_updates_abandoned_themes_sort_by) - Filter: mainwp_updates_abandoned_themes_sort_by
- [`mainwp_limit_updates_all`](#mainwp_limit_updates_all) - Limits number of updates to process.
- [`mainwp_pages_updates_render_tabs`](#mainwp_pages_updates_render_tabs) - Renders updates page.
- [`mainwp_updates_table_features`](#mainwp_updates_table_features) - Filter: mainwp_updates_table_features
- [`mainwp_page_hearder_tabs_updates`](#mainwp_page_hearder_tabs_updates) - Renders header tabs
- [`mainwp_updates_hide_show_updates_per`](#mainwp_updates_hide_show_updates_per) - Renders header tabs
- [`mainwp_manage_updates_limit_loading`](#mainwp_manage_updates_limit_loading) - Method handle_limit_sites().
- [`mainwp-getsubpages-themes`](#mainwp-getsubpages-themes) - Themes Subpages
- [`mainwp_getsubpages_themes`](#mainwp_getsubpages_themes) - Method init_menu()
- [`file_mod_allowed`](#file_mod_allowed) - Disables themes installation
- [`mainwp_favorites_themes`](#mainwp_favorites_themes) - Render the Themes table for the Install Themes Tab.
- [`mainwp_theme_auto_updates_table_fatures`](#mainwp_theme_auto_updates_table_fatures) - Filter: mainwp_theme_auto_updates_table_fatures
- [`mainwp_module_cost_tracker_get_total_cost`](#mainwp_module_cost_tracker_get_total_cost) - Method render_sites()
- [`mainwp_plugins_widget_title`](#mainwp_plugins_widget_title) - *Arguments*
- [`mainwp_themes_widget_title`](#mainwp_themes_widget_title) - *Arguments*
- [`mainwp_limit_updates_all`](#mainwp_limit_updates_all) - Filter: mainwp_limit_updates_all
- [`mainwp_updates_overview_widget_title`](#mainwp_updates_overview_widget_title) - *Arguments*
- [`mainwp_update_everything_button_text`](#mainwp_update_everything_button_text) - *Arguments*

## Hook Details

### `deactivate_{$plugin}`

*Emulate deactivating, then subsequently reactivating the plugin.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [tests/test-case.php](https://github.com/mainwp/mainwp/blob/master/tests/test-case.php), [line 11](https://github.com/mainwp/mainwp/blob/master/tests/test-case.php#L11)



### `activate_{$plugin}`

*Emulate deactivating, then subsequently reactivating the plugin.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

Source: [tests/test-case.php](https://github.com/mainwp/mainwp/blob/master/tests/test-case.php), [line 11](https://github.com/mainwp/mainwp/blob/master/tests/test-case.php#L11)



### `mainwp_before_plugin_ignore`

*Action: mainwp_before_plugin_ignore*

Fires before plugin ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 1273](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L1273)



### `mainwp_after_plugin_ignore`

*Action: mainwp_after_plugin_ignore*

Fires after plugin ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 1283](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L1283)



### `mainwp_before_theme_ignore`

*Action: mainwp_before_theme_ignore*

Fires before theme ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredThemes` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 1310](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L1310)



### `mainwp_after_theme_ignore`

*Action: mainwp_after_theme_ignore*

Fires after theme ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$decodedIgnoredThemes` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php), [line 1319](https://github.com/mainwp/mainwp/blob/master/includes/rest-api/controller/version2/class-mainwp-rest-updates-controller.php#L1319)



### `mainwp_activated`

*Action: mainwp_activated*

Fires upon MainWP plugin activation.


Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 248](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L248)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`implode(',', $pluginsToUpdateNow)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-batch.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php), [line 252](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php#L252)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`'plugin'` |  | 
`implode(',', $pluginsToUpdateNow)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-batch.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php), [line 274](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php#L274)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 
`implode(',', $themesToUpdateNow)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-batch.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php), [line 316](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php#L316)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`'theme'` |  | 
`implode(',', $themesToUpdateNow)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-batch.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php), [line 343](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php#L343)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-hooks.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-hooks.php), [line 1427](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-hooks.php#L1427)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$type` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-hooks.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-hooks.php), [line 1445](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-hooks.php#L1445)



### `mainwp_install_update_actions`

*Fires immediately after install action.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$pAction` |  | 
`$data` |  | 
`$type` |  | 
`$post_data` |  | 
`$upload` |  | 

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [class/class-mainwp-actions-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php), [line 94](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php#L94)



### `mainwp_install_plugin_action`

*Handle @action mainwp_fetch_url_authed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website.
`$plugin_act` |  | 
`$params` | `array` | params input array.
`$information['other_data']['plugin_action_data']` |  | 
`$others` | `array` | others input array.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [class/class-mainwp-actions-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php), [line 102](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php#L102)



### `mainwp_install_theme_action`

*Handle @action mainwp_fetch_url_authed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website.
`'deactivate'` |  | 
`$params` | `array` | params input array.
`$information['other_data']['theme_deactivate_data']` |  | 
`$others` | `array` | others input array.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [class/class-mainwp-actions-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php), [line 102](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php#L102)



### `mainwp_install_theme_action`

*Handle @action mainwp_fetch_url_authed.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | website.
`$theme_act` |  | 
`$params` | `array` | params input array.
`$information['other_data']['theme_action_data']` |  | 
`$others` | `array` | others input array.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [class/class-mainwp-actions-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php), [line 102](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-actions-handler.php#L102)



### `mainwp_prepareinstallplugintheme`

*Method mainwp_ext_prepareinstallplugintheme()*

Prepair Installation of plugins & themes,
Page: ManageSites.


Source: [class/class-mainwp-post-plugin-theme-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-plugin-theme-handler.php), [line 451](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-plugin-theme-handler.php#L451)



### `mainwp_performinstallplugintheme`

*Method mainwp_ext_performinstallplugintheme()*

Installation of plugins & themes,
Page: ManageSites.


Source: [class/class-mainwp-post-plugin-theme-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-plugin-theme-handler.php), [line 461](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-plugin-theme-handler.php#L461)



### `mainwp_header_actions_after_select_themes`

*After select theme actions.*


**Changelog**

Version | Description
------- | -----------
`4.5.2` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1365](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1365)



### `mainwp_before_plugin_theme_install_progress`

*Action: mainwp_before_plugin_theme_install_progress*

Fires before the progress list in the install modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1873](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1873)



### `mainwp_after_plugin_theme_install_progress`

*Action: mainwp_after_plugin_theme_install_progress*

Fires after the progress list in the install modal element.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1884](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1884)



### `mainwp_install_plugin_theme_modal_action`

*Action: mainwp_after_plugin_theme_install_progress*

Fires after the progress list in the install modal element.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$what` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1896](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1896)



### `mainwp_select_themes_modal_top`

*Action: mainwp_select_themes_modal_top*

Fires at the top of the modal.


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2602](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2602)



### `mainwp_select_themes_modal_bottom`

*Action: mainwp_select_themes_modal_bottom*

Fires at the bottom of the modal.


**Changelog**

Version | Description
------- | -----------
`4.3` | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 2613](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L2613)



### `mainwp_widget_updates_actions_top`

*Action: mainwp_widget_updates_actions_top*

Updates actions top content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$active_tab` |  | 

**Changelog**

Version | Description
------- | -----------
`5.4.1` | 

Source: [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 710](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L710)



### `mainwp_updated_site`

*Action: mainwp_updated_site*

Fires after updatig the child site options.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->id` |  | 
`$data` | `array` | Child site data.

**Changelog**

Version | Description
------- | -----------
`3.5.1` | 

Source: [class/class-mainwp-manage-sites-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php), [line 2361](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-manage-sites-view.php#L2361)



### `mainwp_install_plugin_card_top`

*Action: mainwp_install_plugin_card_top*

Fires at the plugin card at top on the Install Plugins page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-plugins-install-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-plugins-install-list-table.php), [line 484](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-plugins-install-list-table.php#L484)



### `mainwp_install_plugin_card_bottom`

*Action: mainwp_install_plugin_card_bottom*

Fires at the plugin card at bottom on the Install Plugins page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugin` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-plugins-install-list-table.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-plugins-install-list-table.php), [line 529](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-plugins-install-list-table.php#L529)



### `mainwp_db_after_update`

*Method install()*

Installs the new DB.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$currentVersion` |  | 
`$this->mainwp_db_version` |  | 

Source: [class/class-mainwp-install.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-install.php), [line 64](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-install.php#L64)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 648](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L648)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`'plugin'` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 672](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L672)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 735](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L735)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`'theme'` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 761](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L761)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'translation'` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 817](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L817)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`'translation'` |  | 
`implode(',', $slugs)` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 842](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L842)



### `mainwp_delete_key_file`

*Method update child api key.*

Encrypt data.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$key_file` |  | 

Source: [modules/api-backups/classes/class-api-backups-utility.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php), [line 700](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-utility.php#L700)



### `mainwp_ajax_add_action`

*Init ajax actions.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'cloudways_action_update_ids'` |  | 
`array(&$this, 'ajax_cloudways_action_update_ids')` |  | 

Source: [modules/api-backups/classes/class-api-backups-3rd-party.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php), [line 100](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php#L100)



### `mainwp_ajax_add_action`

*Init ajax actions.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'gridpane_action_update_ids'` |  | 
`array(&$this, 'ajax_gridpane_action_update_ids')` |  | 

Source: [modules/api-backups/classes/class-api-backups-3rd-party.php](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php), [line 100](https://github.com/mainwp/mainwp/blob/master/modules/api-backups/classes/class-api-backups-3rd-party.php#L100)



### `mainwp_module_cost_tracker_email_header`

*HTTP Check Email Header*

Fires at the top of the HTTP check (after update checks) email template.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [modules/cost-tracker/templates/emails/module-cost-tracker-email.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/templates/emails/module-cost-tracker-email.php), [line 29](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/templates/emails/module-cost-tracker-email.php#L29)



### `mainwp_module_cost_tracker_email_footer`

*HTTP Check Email Footer*

Fires at the bottom of the HTTP check (after update checks) email template.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [modules/cost-tracker/templates/emails/module-cost-tracker-email.php](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/templates/emails/module-cost-tracker-email.php), [line 75](https://github.com/mainwp/mainwp/blob/master/modules/cost-tracker/templates/emails/module-cost-tracker-email.php#L75)



### `mainwp_plugins_actions_bar_left`

*Action: mainwp_plugins_actions_bar_left*

Fires at the left side of the actions bar on the Plugins screen, after the Bulk Actions menu.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 447](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L447)



### `mainwp_plugins_actions_bar_right`

*Action: mainwp_plugins_actions_bar_right*

Fires at the right side of the actions bar on the Plugins screen.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 461](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L461)



### `mainwp_manage_plugins_sidebar_top`

*Action: mainwp_manage_plugins_sidebar_top*

Fires at the top of the sidebar on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 505](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L505)



### `mainwp_manage_plugins_before_select_sites`

*Action: mainwp_manage_plugins_before_select_sites*

Fires before the Select Sites elemnt on Manage plugins.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 517](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L517)



### `mainwp_manage_plugins_after_select_sites`

*Action: mainwp_manage_plugins_after_select_sites*

Fires after the Select Sites elemnt on Manage plugins.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 540](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L540)



### `mainwp_manage_plugins_before_search_options`

*Action: mainwp_manage_plugins_before_search_options*

Fires before the Search Options elemnt on Manage plugins.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 555](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L555)



### `mainwp_manage_plugins_after_search_options`

*Action: mainwp_manage_plugins_after_search_options*

Fires after the Search Options elemnt on Manage plugins.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 580](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L580)



### `mainwp_manage_plugins_before_submit_button`

*Action: mainwp_manage_plugins_before_submit_button*

Fires before the Submit Button elemnt on Manage plugins.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 596](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L596)



### `mainwp_manage_plugins_after_submit_button`

*Action: mainwp_manage_plugins_after_submit_button*

Fires after the Submit Button elemnt on Manage plugins.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 607](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L607)



### `mainwp_manage_plugins_sidebar_bottom`

*Action: mainwp_manage_plugins_sidebar_bottom*

Fires at the bottom of the sidebar on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 618](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L618)



### `mainwp_plugins_bulk_action`

*Action: mainwp_plugins_bulk_action*

Adds a new action to the Manage Plugins bulk actions menu.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1132](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1132)



### `mainwp_before_plugins_table`

*Action: mainwp_before_plugins_table*

Fires before the Plugins table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1268](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1268)



### `mainwp_after_plugins_table`

*Action: mainwp_after_plugins_table*

Fires after the Plugins table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1476](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1476)



### `mainwp_before_plugins_table`

*Action: mainwp_before_plugins_table*

Fires before the Plugins table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1553](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1553)



### `mainwp_after_plugins_table`

*Action: mainwp_after_plugins_table*

Fires after the Plugins table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1784](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1784)



### `mainwp_install_plugin_theme_tabs_header_top`

*Render Install plugins Table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_install_plugins_actions_bar_right`

*Install Plugins actions bar (right)*

Fires at the left side of the actions bar on the Install Plugins screen, after the Nav buttons.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1837](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1837)



### `mainwp_install_plugins_actions_bar_left`

*Install Plugins actions bar (left)*

Fires at the left side of the actions bar on the Install Plugins screen, after the Search bar.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1871](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1871)



### `mainwp_bulk_install_tabs_content`

*Render Install plugins Table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_sidebar_top`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_before_select_sites`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_after_select_sites`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_before_search_options`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_after_search_options`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_before_submit_button`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_before_submit_button`

*Render Install plugins Table.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_bulk_install_sidebar_submit_bottom`

*Render Install plugins Table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'plugin'` |  | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_manage_plugins_sidebar_bottom`

*Render Install plugins Table.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'install'` |  | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1803](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1803)



### `mainwp_plugins_auto_updates_bulk_action`

*Action: mainwp_plugins_auto_updates_bulk_action*

Adds new action to the bulk actions menu on Plugins Auto Updates.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2030](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2030)



### `mainwp_manage_plugins_sidebar_top`

*Render Autoupdate SubPage.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1997)



### `mainwp_manage_plugins_before_search_options`

*Render Autoupdate SubPage.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1997)



### `mainwp_manage_plugins_after_search_options`

*Render Autoupdate SubPage.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1997)



### `mainwp_manage_plugins_before_submit_button`

*Render Autoupdate SubPage.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1997)



### `mainwp_manage_plugins_after_submit_button`

*Render Autoupdate SubPage.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1997)



### `mainwp_manage_plugins_sidebar_bottom`

*Render Autoupdate SubPage.*


Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1997)



### `mainwp_plugins_before_auto_updates_table`

*Action: mainwp_plugins_before_auto_updates_table*

Fires before the Auto Update Plugins table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2313](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2313)



### `mainwp_plugins_after_auto_updates_table`

*Action: mainwp_plugins_after_auto_updates_table*

Fires after the Auto Update Plugins table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2398](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2398)



### `mainwp_plugins_before_ignored_updates`

*Action: mainwp_plugins_before_ignored_updates*

Fires on the top of the Ignored Plugin Updates page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredPlugins` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2494](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2494)



### `mainwp_plugins_after_ignored_updates`

*Action: mainwp_plugins_after_ignored_updates*

Fires on the bottom of the Ignored Plugin Updates page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredPlugins` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2515](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2515)



### `mainwp_plugins_before_ignored_abandoned`

*Action: mainwp_plugins_before_ignored_abandoned*

Fires on the top of the Ignored Plugins Abandoned page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredPlugins` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2780](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2780)



### `mainwp_plugins_after_ignored_abandoned`

*Action: mainwp_plugins_after_ignored_abandoned*

Fires on the bottom of the Ignored Plugins Abandoned page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredPlugins` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2801](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2801)



### `mainwp_plugins_help_item`

*Action: mainwp_plugins_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Plugins page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 3018](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L3018)



### `mainwp_applypluginsettings_{$ext_dir_slug}`

*Apply plugin settings*

Fires to apply certain plugin settigns automatically while adding a new site.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site_id` | `int` | Child site ID.

Source: [pages/page-mainwp-manage-sites-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php), [line 276](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites-handler.php#L276)



### `mainwp_admin_pass_sidebar_top`

*Action: mainwp_admin_pass_sidebar_top*

Fires at the top of the sidebar on Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 357](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L357)



### `mainwp_admin_pass_before_select_sites`

*Action: mainwp_admin_pass_before_select_sites*

Fires before the Select Sites section on the Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 368](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L368)



### `mainwp_admin_pass_after_select_sites`

*Action: mainwp_admin_pass_after_select_sites*

Fires after the Select Sites section on the Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 387](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L387)



### `mainwp_admin_pass_before_pass_form`

*Action: mainwp_admin_pass_before_pass_form*

Fires before the New password form on the Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 402](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L402)



### `mainwp_admin_pass_after_pass_form`

*Action: mainwp_admin_pass_after_pass_form*

Fires after the New password form on the Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 423](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L423)



### `mainwp_admin_pass_before_submit_button`

*Action: mainwp_admin_pass_before_submit_button*

Fires before the Submit button on the Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 437](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L437)



### `mainwp_admin_pass_after_submit_button`

*Action: mainwp_admin_pass_after_submit_button*

Fires after the Submit button on the Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 452](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L452)



### `mainwp_admin_pass_sidebar_bottom`

*Action: mainwp_admin_pass_sidebar_bottom*

Fires at the bottom of the sidebar on Admin Passwords page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 463](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L463)



### `mainwp_client_updated`

*Add client*

Fires after add a client.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$inserted` | `object` | client data.
`$add_new` | `bool` | true add new, false updated.

**Changelog**

Version | Description
------- | -----------
`4.5.1.1` | 

Source: [pages/page-mainwp-client.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php), [line 1340](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-client.php#L1340)



### `mainwp_update_site`

*Update site*

Fires after updating a website settings.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website->id` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [pages/page-mainwp-manage-sites.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php), [line 2003](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-sites.php#L2003)



### `mainwp_before_plugin_ignore`

*Action: mainwp_before_plugin_ignore*

Fires before plugin ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php), [line 149](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php#L149)



### `mainwp_after_plugin_ignore`

*Action: mainwp_after_plugin_ignore*

Fires after plugin ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php), [line 160](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php#L160)



### `mainwp_before_plugin_action`

*Action: mainwp_before_plugin_action*

Fires before plugin activate/deactivate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pAction` |  | 
`$plugin` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php), [line 217](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php#L217)



### `mainwp_after_plugin_action`

*Action: mainwp_after_plugin_action*

Fires after plugin activate/deactivate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$pAction` |  | 
`$plugin` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php), [line 235](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins-handler.php#L235)



### `mainwp_cores_before_ignored_updates`

*Action: mainwp_cores_before_ignored_updates*

Fires on the top of the Ignored Plugin Updates page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [pages/page-mainwp-wp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-wp-updates.php), [line 74](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-wp-updates.php#L74)



### `mainwp_cores_after_ignored_updates`

*Action: mainwp_cores_after_ignored_updates*

Fires on the bottom of the Ignored Plugin Updates page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-wp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-wp-updates.php), [line 95](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-wp-updates.php#L95)



### `mainwp_update_backuptask`

*Update backup task.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$task->id` |  | 

Source: [pages/page-mainwp-manage-backups-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php), [line 129](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-manage-backups-handler.php#L129)



### `mainwp_before_plugin_theme_install`

*Action: mainwp_before_plugin_theme_install*

Fires before plugin/theme install.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 457](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L457)



### `mainwp_after_plugin_theme_install`

*Action: mainwp_after_plugin_theme_install*

Fires after plugin/theme install.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output` |  | 
`$post_data` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 483](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L483)



### `mainwp_before_plugin_theme_install`

*Action: mainwp_before_plugin_theme_install*

Fires before plugin/theme install.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 671](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L671)



### `mainwp_after_plugin_theme_install`

*Action: mainwp_after_plugin_theme_install*

Fires after plugin/theme install.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output` |  | 
`$post_data` |  | 
`$websites` |  | 
`$type` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 695](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L695)



### `mainwp_before_plugin_privacy_section`

*Action: mainwp_before_plugin_privacy_section*

Fires before the Plugin Privacy section.


**Changelog**

Version | Description
------- | -----------
`4.2` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1779](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1779)



### `mainwp_after_plugin_privacy_section`

*Action: mainwp_after_plugin_privacy_section*

Fires after the Plugin Privacy section.


**Changelog**

Version | Description
------- | -----------
`4.2` | 

Source: [pages/page-mainwp-server-information.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php), [line 1844](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-server-information.php#L1844)



### `mainwp_updates_before_wp_updates`

*Action: mainwp_updates_before_wp_updates*

Fires at the top of the WP updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_wp_upgrades` | `int` | Number of available WP upates.
`$all_groups_sites` | `array` | Array containing all groups and sites.
`$all_groups` | `array` | Array containing all groups.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 859](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L859)



### `mainwp_updates_after_wp_updates`

*Action: mainwp_updates_after_wp_updates*

Fires at the top of the WP updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_wp_upgrades` | `int` | Number of available WP upates.
`$all_groups_sites` | `array` | Array containing all groups and sites.
`$all_groups` | `array` | Array containing all groups.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 935](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L935)



### `mainwp_updates_before_plugin_updates`

*Action: mainwp_updates_before_plugin_updates*

Fires at the top of the Plugin updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 990](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L990)



### `mainwp_updates_perplugin_before_plugin_updates`

*Action: mainwp_updates_perplugin_before_plugin_updates*

Fires at the top of the Plugin updates tab, per Plugin view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1080](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1080)



### `mainwp_updates_perplugin_after_plugin_updates`

*Action: mainwp_updates_perplugin_after_plugin_updates*

Fires at the bottom of the Plugin updates tab, per Plugin view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1098](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1098)



### `mainwp_updates_after_plugin_updates`

*Action: mainwp_updates_after_plugin_updates*

Fires at the bottom of the Plugin updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_plugin_upgrades` | `int` | Number of available plugin updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPlugins` | `array` | Array of all plugins.
`$pluginsInfo` | `array` | Array of all plugins info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1116](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1116)



### `mainwp_updates_before_theme_updates`

*Action: mainwp_updates_before_theme_updates*

Fires at the top of the Theme updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1163](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1163)



### `mainwp_updates_pertheme_before_theme_updates`

*Action: mainwp_updates_pertheme_before_theme_updates*

Fires at the top of the Theme updates tab, per Theme view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1253](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1253)



### `mainwp_updates_pertheme_after_theme_updates`

*Action: mainwp_updates_pertheme_after_theme_updates*

Fires at the bottom of the Theme updates tab, per Theme view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1271](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1271)



### `mainwp_updates_after_theme_updates`

*Action: mainwp_updates_after_theme_updates*

Fires at the bottom of the Theme updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_theme_upgrades` | `int` | Number of available theme updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemes` | `array` | Array of all themes.
`$themesInfo` | `array` | Array of all themes info.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1289](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1289)



### `mainwp_updates_before_translation_updates`

*Action: mainwp_updates_before_translation_updates*

Fires at the top of the Translation updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1334](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1334)



### `mainwp_updates_pertranslation_before_translation_updates`

*Action: mainwp_updates_pertranslation_before_translation_updates*

Fires at the top of the Translation updates tab, per Translation view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1424](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1424)



### `mainwp_updates_pertranslation_after_translation_updates`

*Action: mainwp_updates_pertranslation_after_translation_updates*

Fires at the bottom of the Translation updates tab, per Translation view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1442](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1442)



### `mainwp_updates_after_translation_updates`

*Action: mainwp_updates_after_translation_updates*

Fires at the bottom of the Translation updates tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$total_translation_upgrades` | `int` | Number of available translation updates.
`$userExtension` | `object` | User extension.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allTranslations` | `array` | Array of all translations.
`$translationsInfo` | `array` | Array of all translations info.
`$mainwp_show_language_updates` |  | 
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1460](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1460)



### `mainwp_updates_before_abandoned_plugins`

*Action: mainwp_updates_before_abandoned_plugins*

Fires at the top of the Abandoned plugins tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1502](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1502)



### `mainwp_updates_perplugin_before_abandoned_plugins`

*Action: mainwp_updates_perplugin_before_abandoned_plugins*

Fires at the top of the Abandoned plugins tab, per Plugin view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1582](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1582)



### `mainwp_updates_perplugin_after_abandoned_plugins`

*Action: mainwp_updates_perplugin_after_abandoned_plugins*

Fires at the bottom of the Abandoned plugins tab, per Plugin view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1598](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1598)



### `mainwp_updates_after_abandoned_plugins`

*Action: mainwp_updates_after_abandoned_plugins*

Fires at the bottom of the Abandoned plugins tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allPluginsOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedPlugins` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1614](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1614)



### `mainwp_updates_before_abandoned_themes`

*Action: mainwp_updates_before_abandoned_themes*

Fires at the top of the Abandoned themes tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1653](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1653)



### `mainwp_updates_pertheme_before_abandoned_themes`

*Action: mainwp_updates_pertheme_before_abandoned_themes*

Fires at the top of the Abandoned themes tab, per Theme view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1733](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1733)



### `mainwp_updates_pertheme_after_abandoned_themes`

*Action: mainwp_updates_pertheme_after_abandoned_themes*

Fires at the bottom of the Abandoned themes tab, per Theme view.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1749](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1749)



### `mainwp_updates_after_abandoned_themes`

*Action: mainwp_updates_after_abandoned_themes*

Fires at the bottom of the Abandoned themes tab.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$websites` | `object` | Object containing child sites info.
`$all_groups_sites` | `array` | Array of all groups and sites.
`$all_groups` | `array` | Array of all groups.
`$allThemesOutdate` | `array` | Array of all abandoned plugins.
`$decodedDismissedThemes` | `array` | Array of dismissed abandoned plugins.
`$site_offset_for_groups` | `int` | Offset value.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1765](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1765)



### `mainwp_updates_before_nav_tabs`

*Action: mainwp_updates_before_nav_tabs*

Fires before the navigation tabs on the Updates page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1931](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1931)



### `mainwp_updates_after_nav_tabs`

*Action: mainwp_updates_after_nav_tabs*

Fires after the navigation tabs on the Updates page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 2003](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L2003)



### `mainwp_updates_before_actions_bar`

*Action: mainwp_updates_before_actions_bar*

Fires before the actions bar on the Updates page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 2012](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L2012)



### `mainwp_widget_updates_actions_top`

*Action: mainwp_widget_updates_actions_top*

Updates actions top content.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$current_tab` |  | 

**Changelog**

Version | Description
------- | -----------
`5.4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 2037](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L2037)



### `mainwp_updates_after_actions_bar`

*Action: mainwp_updates_after_actions_bar*

Fires after the actions bar on the Updates page.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 2066](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L2066)



### `mainwp_updates_help_item`

*Action: mainwp_updates_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Updates page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 2564](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L2564)



### `mainwp_before_theme_action`

*Action: mainwp_before_theme_action*

Fires before theme activate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$pAction` |  | 
`$theme` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php), [line 145](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php#L145)



### `mainwp_after_theme_action`

*Action: mainwp_after_theme_action*

Fires after theme activate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$pAction` |  | 
`$theme` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php), [line 167](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php#L167)



### `mainwp_before_theme_ignore`

*Action: mainwp_before_theme_ignore*

Fires before theme ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$decodedIgnoredThemes` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php), [line 230](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php#L230)



### `mainwp_after_theme_ignore`

*Action: mainwp_after_theme_ignore*

Fires after theme ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$decodedIgnoredThemes` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php), [line 240](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes-handler.php#L240)



### `mainwp_after_upgrade_wp_success`

*Method upgrade_site()*

Check Child Site ID & Update.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$information` |  | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 26](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L26)



### `mainwp_before_wp_update`

*Action: mainwp_before_wp_update*

Fires before WP update.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 99](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L99)



### `mainwp_after_wp_update`

*Action: mainwp_after_wp_update*

Fires after WP update.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 138](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L138)



### `mainwp_before_plugin_ignore`

*Action: mainwp_before_plugin_ignore*

Fires before plugin ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 175](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L175)



### `mainwp_after_plugin_ignore`

*Action: mainwp_after_plugin_ignore*

Fires after plugin ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 209](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L209)



### `mainwp_before_theme_ignore`

*Action: mainwp_before_theme_ignore*

Fires before theme ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredThemes` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 221](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L221)



### `mainwp_after_theme_ignore`

*Action: mainwp_after_theme_ignore*

Fires after theme ignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` |  | 
`$decodedIgnoredThemes` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 252](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L252)



### `mainwp_before_plugin_theme_unignore`

*Action: mainwp_before_plugin_theme_unignore*

Fires after plugin/theme unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`$slug` |  | 
`$id` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 289](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L289)



### `mainwp_before_plugin_unignore`

*Action: mainwp_before_plugin_unignore*

Fires before plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 303](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L303)



### `mainwp_after_plugin_unignore`

*Action: mainwp_after_plugin_unignore*

Fires after plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 314](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L314)



### `mainwp_before_theme_unignore`

*Action: mainwp_before_theme_unignore*

Fires before theme unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 324](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L324)



### `mainwp_after_theme_unignore`

*Action: mainwp_after_theme_unignore*

Fires after theme unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 334](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L334)



### `mainwp_before_plugin_unignore`

*Action: mainwp_before_plugin_unignore*

Fires before plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 352](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L352)



### `mainwp_after_plugin_unignore`

*Action: mainwp_after_plugin_unignore*

Fires after plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredPlugins` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 387](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L387)



### `mainwp_before_theme_unignore`

*Action: mainwp_before_theme_unignore*

Fires before theme unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredThemes` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 400](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L400)



### `mainwp_after_theme_unignore`

*Action: mainwp_after_theme_unignore*

Fires after theme unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$decodedIgnoredThemes` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 437](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L437)



### `mainwp_before_core_unignore`

*Action: mainwp_before_core_unignore*

Fires before plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'_ALL_'` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 474](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L474)



### `mainwp_before_core_unignore`

*Action: mainwp_after_core_unignore*

Fires after plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'_ALL_'` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 484](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L484)



### `mainwp_before_core_unignore`

*Action: mainwp_before_core_unignore*

Fires before plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignored_info` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 504](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L504)



### `mainwp_after_core_unignore`

*Action: mainwp_after_core_unignore*

Fires after plugin unignore.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignored_info` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`5.2` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 526](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L526)



### `mainwp_before_plugin_theme_translation_update`

*Action: mainwp_before_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$type` |  | 
`$list_items` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 1144](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L1144)



### `mainwp_after_plugin_theme_translation_update`

*Action: mainwp_after_plugin_theme_translation_update*

Fires before plugin/theme/translation update actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$type` |  | 
`$list_items` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates-handler.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php), [line 1162](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates-handler.php#L1162)



### `mainwp_themes_actions_bar_left`

*Action: mainwp_themes_actions_bar_left*

Fires at the left side of the actions bar on the Themes screen, after the Bulk Actions menu.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 437](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L437)



### `mainwp_themes_actions_bar_right`

*Action: mainwp_themes_actions_bar_right*

Fires at the right side of the actions bar on the Themes screen.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 451](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L451)



### `mainwp_manage_themes_sidebar_top`

*Action: mainwp_manage_themes_sidebar_top*

Fires at the top of the sidebar on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 494](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L494)



### `mainwp_manage_themes_before_select_sites`

*Action: mainwp_manage_themes_before_select_sites*

Fires before the Select Sites element on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 505](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L505)



### `mainwp_manage_themes_after_select_sites`

*Action: mainwp_manage_themes_after_select_sites*

Fires after the Select Sites element on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 528](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L528)



### `mainwp_manage_themes_before_search_options`

*Action: mainwp_manage_themes_before_search_options*

Fires before the Search Options element on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 543](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L543)



### `mainwp_manage_themes_after_search_options`

*Action: mainwp_manage_themes_after_search_options*

Fires after the Search Options element on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 568](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L568)



### `mainwp_manage_themes_before_submit_button`

*Action: mainwp_manage_themes_before_submit_button*

Fires before the Submit Button element on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 584](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L584)



### `mainwp_manage_themes_after_submit_button`

*Action: mainwp_manage_themes_after_submit_button*

Fires after the Submit Button element on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 595](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L595)



### `mainwp_manage_themes_sidebar_bottom`

*Action: mainwp_manage_themes_sidebar_bottom*

Fires at the bottom of the sidebar on Manage themes.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 606](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L606)



### `mainwp_before_themes_table`

*Action: mainwp_before_themes_table*

Fires before the Themes table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1127](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1127)



### `mainwp_after_themes_table`

*Action: mainwp_after_themes_table*

Fires after the Themes table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1327](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1327)



### `mainwp_before_themes_table`

*Action: mainwp_before_themes_table*

Fires before the Themes table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1402](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1402)



### `mainwp_after_themes_table`

*Action: mainwp_after_themes_table*

Fires after the Themes table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1628](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1628)



### `mainwp_themes_bulk_action`

*Action: mainwp_themes_bulk_action*

Adds a new action to the Manage Themes bulk actions menu.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1679](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1679)



### `mainwp_install_plugin_theme_tabs_header_top`

*Render the Themes table for the Install Themes Tab.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_install_themes_actions_bar_right`

*Install Themes actions bar (right)*

Fires at the right side of the actions bar on the Install Themes screen.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1757](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1757)



### `mainwp_install_themes_actions_bar_left`

*Install Themes actions bar (left)*

Fires at the left side of the actions bar on the Install Themes screen, after the search form.


**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1773](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1773)



### `mainwp_bulk_install_tabs_content`

*Render the Themes table for the Install Themes Tab.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_sidebar_top`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_before_select_sites`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_after_select_sites`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_before_search_options`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_after_search_options`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_before_submit_button`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_after_submit_button`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_bulk_install_sidebar_submit_bottom`

*Render the Themes table for the Install Themes Tab.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'theme'` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_manage_themes_sidebar_bottom`

*Render the Themes table for the Install Themes Tab.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'install'` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_install_theme_card_template_bottom`

*Render the Themes table for the Install Themes Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_themes_auto_updates_bulk_action`

*Action: mainwp_themes_auto_updates_bulk_action*

Adds new action to the bulk actions menu on Themes Auto Updates.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2015](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2015)



### `mainwp_manage_themes_sidebar_top`

*Render the Themes Auto Update Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1978](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1978)



### `mainwp_manage_themes_before_search_options`

*Render the Themes Auto Update Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1978](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1978)



### `mainwp_manage_themes_after_search_options`

*Render the Themes Auto Update Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1978](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1978)



### `mainwp_manage_themes_before_submit_button`

*Render the Themes Auto Update Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1978](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1978)



### `mainwp_manage_themes_after_submit_button`

*Render the Themes Auto Update Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1978](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1978)



### `mainwp_manage_themes_sidebar_bottom`

*Render the Themes Auto Update Tab.*


Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1978](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1978)



### `mainwp_themes_before_auto_updates_table`

*Action: mainwp_themes_before_auto_updates_table*

Fires before the Auto Update Themes table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2273](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2273)



### `mainwp_themes_after_auto_updates_table`

*Action: mainwp_themes_after_auto_updates_table*

Fires before the Auto Update Themes table.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2351](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2351)



### `mainwp_themes_before_ignored_updates`

*Action: mainwp_themes_before_ignored_updates*

Fires on the top of the Ignored Theme Updates page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredThemes` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2446](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2446)



### `mainwp_themes_after_ignored_updates`

*Action: mainwp_themes_after_ignored_updates*

Fires on the bottom of the Ignored Theme Updates page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredThemes` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2467](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2467)



### `mainwp_themes_before_ignored_abandoned`

*Action: mainwp_themes_before_ignored_abandoned*

Fires on the top of the Ignored Themes Abandoned page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredThemes` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2713](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2713)



### `mainwp_themes_after_ignored_abandoned`

*Action: mainwp_themes_after_ignored_abandoned*

Fires on the bottom of the Ignored Themes Abandoned page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$ignoredThemes` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2734](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2734)



### `mainwp_themes_help_item`

*Action: mainwp_themes_help_item*

Fires at the bottom of the help articles list in the Help sidebar on the Themes page.

Suggested HTML markup:

<div class="item"><a href="Your custom URL">Your custom text</a></div>


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2919](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2919)



### `mainwp_plugins_widget_top`

*Action: mainwp_plugins_widget_top*

Fires at the top of the Plugins widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$allPlugins` | `array` | Array containing all detected plugins data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 154](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L154)



### `mainwp_before_active_plugins_list`

*Action: mainwp_before_active_plugins_list*

Fires before the active plugins list in the Plugins widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$actived_plugins` | `array` | Array containing all active plugins data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 168](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L168)



### `mainwp_after_active_plugins_list`

*Action: mainwp_after_active_plugins_list*

Fires after the active plugins list in the Plugins widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$actived_plugins` | `array` | Array containing all active plugins data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 213](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L213)



### `mainwp_before_inactive_plugins_list`

*Action: mainwp_before_inactive_plugins_list*

Fires before the inactive plugins list in the Plugins widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$inactive_plugins` | `array` | Array containing all active plugins data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 228](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L228)



### `mainwp_after_inactive_plugins_list`

*Action: mainwp_after_inactive_plugins_list*

Fires after the inactive plugins list in the Plugins widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$inactive_plugins` | `array` | Array containing all active plugins data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 276](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L276)



### `mainwp_plugins_widget_bottom`

*Action: mainwp_plugins_widget_bottom*

Fires at the bottom of the Plugins widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$allPlugins` | `array` | Array containing all detected plugins data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 297](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L297)



### `mainwp_before_plugin_action`

*Action: mainwp_before_plugin_action*

Fires before plugin activate/deactivate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$action` |  | 
`$plugin` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 383](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L383)



### `mainwp_after_plugin_action`

*Action: mainwp_after_plugin_action*

Fires after plugin activate/deactivate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$action` |  | 
`$plugin` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 401](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L401)



### `mainwp_themes_widget_top`

*Action: mainwp_themes_widget_top*

Fires at the top of the Themes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$allThemes` | `array` | Array containing all detected themes data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 114](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L114)



### `mainwp_before_inactive_themes_list`

*Action: mainwp_before_inactive_themes_list*

Fires before the inactive themes list in the Themes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$inactive_themes` | `array` | Array containing all inactive themes data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 128](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L128)



### `mainwp_after_inactive_themes_list`

*Action: mainwp_after_inactive_themes_list*

Fires after the inactive themes list in the Themes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$inactive_themes` | `array` | Array containing all inactive themes data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 175](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L175)



### `mainwp_themes_widget_bottom`

*Action: mainwp_themes_widget_bottom*

Fires at the bottom of the Themes widget on the Individual site overview page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$website` | `object` | Object containing the child site info.
`$allThemes` | `array` | Array containing all detected themes data.

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 191](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L191)



### `mainwp_before_theme_action`

*Action: mainwp_before_theme_action*

Fires before theme activate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$action` |  | 
`$theme` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 272](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L272)



### `mainwp_after_theme_action`

*Action: mainwp_after_theme_action*

Fires after theme activate/delete actions.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$information` |  | 
`$action` |  | 
`$theme` |  | 
`$website` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 293](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L293)



### `mainwp_updates_overview_after_update_details`

*Action: mainwp_updates_overview_after_update_details*

Fires at the bottom of the Update Details section in the Updates Overview widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$currentSite` |  | 
`$globalView` |  | 
`$userExtension` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 424](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L424)



### `mainwp_updates_overview_before_total_updates`

*Action: mainwp_updates_overview_before_total_updates*

Fires before the total updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 517](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L517)



### `mainwp_updates_overview_after_total_updates`

*Action: mainwp_updates_overview_after_total_updates*

Fires after the total updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 559](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L559)



### `mainwp_updates_overview_before_update_details`

*Action: mainwp_updates_overview_before_update_details*

Fires at the top of the Update Details section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 596](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L596)



### `mainwp_updates_overview_before_wordpress_updates`

*Action: mainwp_updates_overview_before_wordpress_updates*

Fires before the WordPress updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 605](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L605)



### `mainwp_updates_overview_after_wordpress_updates`

*Action: mainwp_updates_overview_after_wordpress_updates*

Fires after the WordPress updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 652](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L652)



### `mainwp_updates_overview_before_plugin_updates`

*Action: mainwp_updates_overview_before_plugin_updates*

Fires before the Plugin updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 687](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L687)



### `mainwp_updates_overview_after_plugin_updates`

*Action: mainwp_updates_overview_after_plugin_updates*

Fires after the Plugin updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 729](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L729)



### `mainwp_updates_overview_before_theme_updates`

*Action: mainwp_updates_overview_before_theme_updates*

Fires before the Theme updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 764](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L764)



### `mainwp_updates_overview_after_theme_updates`

*Action: mainwp_updates_overview_after_theme_updates*

Fires after the Theme updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 806](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L806)



### `mainwp_updates_overview_before_translation_updates`

*Action: mainwp_updates_overview_before_translation_updates*

Fires before the Translation updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 832](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L832)



### `mainwp_updates_overview_after_translation_updates`

*Action: mainwp_updates_overview_after_translation_updates*

Fires after the Translation updates section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 869](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L869)



### `mainwp_updates_overview_before_abandoned_plugins_themes`

*Action: mainwp_updates_overview_before_abandoned_plugins_themes*

Fires at the top of the Abandoned Plugins & Themes section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 899](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L899)



### `mainwp_updates_overview_after_abandoned_plugins_themes`

*Action: mainwp_updates_overview_after_abandoned_plugins_themes*

Fires at the bottom of the Abandoned Plugins & Themes section in the Updates Overview widget.


**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 992](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L992)



### `mainwp_updatesoverview_widget_bottom`

*Action: mainwp_updatesoverview_widget_bottom*

Fires at the bottom of the Updates Overview widgets.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$site_ids` |  | 
`$globalView` | `bool` | Whether it's global or individual site view.

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 1115](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L1115)



### `mainwp_load_text_domain`

*Method localization()*

Loads plugin language files.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 

Source: [class/class-mainwp-system.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php), [line 414](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system.php#L414)



### `mainwp_cron_bulk_update_items_limit`

*Method handle_cron_batch_updates()*

MainWP Cron batch Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  | 

Source: [class/class-mainwp-cron-jobs-batch.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php), [line 95](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-batch.php#L95)



### `mainwp_api_manager_upgrade_url`

*Get Upgrade URL.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$this->upgrade_url` |  | 

Source: [class/class-mainwp-api-manager.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-api-manager.php), [line 91](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-api-manager.php#L91)



### `mainwp_update_cached_icons`

*Method update_cached_icons().*

Update cached icons

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$icon` | `string` | The icon.
`$slug` | `string` | slug.
`$type` | `string` | Type: plugin\|theme.

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1039](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1039)



### `mainwp_get_plugin_theme_icon`

*Gets a plugin icon via API from WordPress.org*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$slug` | `string` | Plugin slug.
`'plugin'` |  | 

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1212](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1212)



### `mainwp_forced_get_plugin_theme_icon`

*Gets a plugin icon via API from WordPress.org*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$forced_get` | `bool` | Forced get icon, default: false.
`$slug` | `string` | Plugin slug.
`'plugin'` |  | 

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1212](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1212)



### `mainwp_get_plugin_theme_icon`

*Gets a theme icon via API from WordPress.org*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`''` |  | 
`$slug` | `string` | Theme slug.
`'theme'` |  | 

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1261](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1261)



### `mainwp_forced_get_plugin_theme_icon`

*Gets a theme icon via API from WordPress.org*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$forced_get` | `bool` | Forced get icon, default: false.
`$slug` | `string` | Theme slug.
`'theme'` |  | 

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1261](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1261)



### `mainwp_plugin_theme_icon_cache_days`

*Gets a plugin|theme icon to output.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`15` |  | 
`$slug` | `string` | Plugin\|Theme slug.
`$type` | `string` | Type icon, plugin\|theme.

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1311](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1311)



### `mainwp_cache_icon_expired`

*Gets a plugin|theme icon to output.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$slug` | `string` | Plugin\|Theme slug.
`'theme'` |  | 

Source: [class/class-mainwp-system-utility.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php), [line 1311](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-utility.php#L1311)



### `mainwp_updates_table_columns_header`

*Get column info.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array($columns, $sortable, $collapsing)` |  | 
`$this->type` |  | 
`$this->view_per` |  | 

Source: [class/class-mainwp-updates-table-helper.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-updates-table-helper.php), [line 96](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-updates-table-helper.php#L96)



### `mainwp_updates_table_header_content`

*Echo the column headers.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$column_display_name` |  | 
`$column_key` |  | 
`$top` | `bool` | true\|false.
`$this` |  | 

Source: [class/class-mainwp-updates-table-helper.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-updates-table-helper.php), [line 141](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-updates-table-helper.php#L141)



### `mainwp_updates_table_row_columns`

*Echo columns.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$columns` | `array` | Array of columns.
`$website` | `object` | The website.
`$this->type` |  | 
`$this->view_per` |  | 

Source: [class/class-mainwp-updates-table-helper.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-updates-table-helper.php), [line 222](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-updates-table-helper.php#L222)



### `mainwp_update_plugintheme_max`

*Filter: mainwp_update_plugintheme_max*

Filters the max number of plugins/themes to be updated in one run in order to improve performance.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$websiteId` | `int` | Child site ID.

Source: [class/class-mainwp-post-plugin-theme-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-plugin-theme-handler.php), [line 567](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-post-plugin-theme-handler.php#L567)



### `mainwp_show_all_updates_button_text`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Show All Updates', 'mainwp')` |  | 

Source: [class/class-mainwp-ui.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php), [line 1997](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-ui.php#L1997)



### `mainwp_plugin_information_sslverify`

*Sends and receives data to and from the server API.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$default` |  | 
`$args` | `array` | Request arguments.

**Changelog**

Version | Description
------- | -----------
`1.0.0` | 

Source: [class/class-mainwp-api-manager-plugin-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-api-manager-plugin-update.php), [line 149](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-api-manager-plugin-update.php#L149)



### `mainwp_api_manager_upgrade_package_url`

*For debugging errors from the API
For errors like: unserialize(): Error at offset 0 of 170 bytes
Comment out $response above first*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$response->package` |  | 
`$response` |  | 

Source: [class/class-mainwp-api-manager-plugin-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-api-manager-plugin-update.php), [line 191](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-api-manager-plugin-update.php#L191)



### `mainwp_plugins_install_checks`

*Method get_plugins_install_check()*

Get plugins for install checking.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$plugins` |  | 

Source: [class/class-mainwp-system-view.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php), [line 1129](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-view.php#L1129)



### `mainwp_updatescheck_sendmail_at_time`

*Filter: mainwp_updatescheck_sendmail_at_time*

Filters the the time when the Daily Digest email will be sent.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 440](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L440)



### `mainwp_updatescheck_hours_interval`

*Filter: mainwp_updatescheck_hours_interval*

Filters the status check interval.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 

**Changelog**

Version | Description
------- | -----------
`3.4` | 

Source: [class/class-mainwp-system-cron-jobs.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php), [line 513](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-system-cron-jobs.php#L513)



### `mainwp_detect_premiums_updates`

*Filter: mainwp_detect_premiums_updates*

Use mainwp_detect_premium_plugins_update instead.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$premiums` |  | 

Source: [class/class-mainwp-premium-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php), [line 90](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php#L90)



### `mainwp_detect_premium_plugins_update`

*Filter: mainwp_detect_premium_plugins_update*

Filters supported premium plugins to fix compatiblity issues with detecting premium plugin updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$premiums` |  | 

Source: [class/class-mainwp-premium-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php), [line 99](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php#L99)



### `mainwp_detect_premium_themes_update`

*Filter: mainwp_detect_premium_themes_update*

Filters supported premium themes to fix compatiblity issues with detecting premium theme updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$premiums` |  | 

Source: [class/class-mainwp-premium-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php), [line 119](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php#L119)



### `mainwp_request_update_premium_plugins`

*Filter: mainwp_request_update_premium_plugins*

Filters supported premium plugins to fix compatibility problmes with updating premium plugins.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$update_premiums` |  | 

Source: [class/class-mainwp-premium-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php), [line 223](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php#L223)



### `mainwp_request_update_premium_themes`

*Filter: mainwp_request_update_premium_themes*

Filters supported premium themes to fix compatibility problmes with updating premium themes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$update_premiums` |  | 

Source: [class/class-mainwp-premium-update.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php), [line 243](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-premium-update.php#L243)



### `mainwp_uptime_monitoring_update_monitor_data`

*Method handle_save_settings*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$update` |  | 
`$site_id` |  | 

Source: [class/class-mainwp-uptime-monitoring-edit.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php), [line 88](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-edit.php#L88)



### `mainwp_default_template_source_dir`

*Locate a template and return the path for inclusion.*

Credits.

Plugin-Name: WooCommerce.
Plugin URI: https://woocommerce.com/.
Author: Automattic.
Author URI: https://woocommerce.com.
License: GPLv3 or later.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$template_path` |  | 
`$template_name` | `string` | Template name.

Source: [class/class-mainwp-notification-template.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php), [line 234](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-notification-template.php#L234)



### `mainwp_update_uptime_monitor_data`

*Method update_uptime_global_settings*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$settings` | `array` | settings.

Source: [class/class-mainwp-uptime-monitoring-handle.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-handle.php), [line 122](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-uptime-monitoring-handle.php#L122)



### `mainwp_available_updates_count_custom_fields_data`

*Method sites_available_updates_count()*

Returns the number of available udpates for sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 
`'updates_count'` |  | 

Source: [class/class-mainwp-common-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-common-handler.php), [line 41](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-common-handler.php#L41)



### `mainwp_database_updater_supported_plugins`

*Method sites_available_updates_count()*

Returns the number of available udpates for sites.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [class/class-mainwp-common-handler.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-common-handler.php), [line 41](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-common-handler.php#L41)



### `mainwp_db_install_tables`

*Method install()*

Installs the new DB.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sql` |  | 
`$currentVersion` |  | 
`$charset_collate` |  | 

Source: [class/class-mainwp-install.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-install.php), [line 64](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-install.php#L64)



### `mainwp_cron_bulk_update_items_limit`

*Method handle_cron_auto_updates()*

MainWP Cron Check Update

This Cron Checks to see if Automatic Daily Updates need to be performed.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`3` |  | 

Source: [class/class-mainwp-cron-jobs-auto-updates.php](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php), [line 104](https://github.com/mainwp/mainwp/blob/master/class/class-mainwp-cron-jobs-auto-updates.php#L104)



### `mainwp-getsubpages-plugins`

*Plugins Subpages*

Filters subpages for the Plugins page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_plugins'` |  | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 150](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L150)



### `mainwp_getsubpages_plugins`

*Instantiate Main Plugins Menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 73](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L73)



### `mainwp_manage_plugin_theme_hide_show_updates_per`

*Method render_select_manage_view().*

Handle render view mode selection.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$which` | `string` | plugin\|theme.

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1167](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1167)



### `file_mod_allowed`

*Disables plugin installation*

Filters whether file modifications are allowed on the Dashboard site. If not, installation process will be disabled too.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`'mainwp_install_plugin'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 1965](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L1965)



### `mainwp_plugin_auto_updates_table_fatures`

*Filter: mainwp_plugin_auto_updates_table_fatures*

Filters the Plugin Auto Updates table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-plugins.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php), [line 2418](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-plugins.php#L2418)



### `mainwp_update_admin_password_complexity`

*Filter: mainwp_update_admin_password_complexity*

Filters the Password lenght for the Update Admin Password, Password field.

Since 4.1

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'24'` |  | 

Source: [pages/page-mainwp-bulk-update-admin-passwords.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php), [line 242](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-bulk-update-admin-passwords.php#L242)



### `mainwp_file_uploader_chunk_size`

*Method render_upload()*

Renders the upload sub part.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`1000000` |  | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 67](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L67)



### `mainwp_prepare_install_download_url`

*Method prepare_install()*

Prepare for the installation.

Grab all the necessary data to make the upload and prepare json response.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$url` |  | 
`$_POST` |  | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 302](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L302)



### `mainwp_bulk_prepare_install_result`

*Filter: mainwp_bulk_prepare_install_result*

Fires after plugin/theme prepare install.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output` |  | 
`$type` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 356](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L356)



### `mainwp_perform_install_data`

*Perform insatallation additional data*

Adds support for additional data such as HTTP User and HTTP Password.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` | `array` | Array containg the post data.

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 437](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L437)



### `mainwp_installbulk_prepareupload`

*Prepare upload*

Prepares upload URLs for the bulk install process.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output['urls']` |  | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 527](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L527)



### `mainwp_perform_install_data`

*This filter is documented in pages/page-mainwp-install-bulk.php*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$post_data` |  | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 649](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L649)



### `mainwp_bulk_upload_install_result`

*Filter: mainwp_bulk_upload_install_result*

Fires after plugin/theme install.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$output` |  | 
`$type` |  | 
`$post_data` |  | 
`$websites` |  | 

**Changelog**

Version | Description
------- | -----------
`4.6` | 

Source: [pages/page-mainwp-install-bulk.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php), [line 704](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-install-bulk.php#L704)



### `mainwp_sub_leftmenu_updates`

*Initiates Updates menu.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$init_sub_subleftmenu` |  | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 142](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L142)



### `mainwp_updates_translation_sort_by`

*Filter: mainwp_updates_translation_sort_by*

Filters the default sorting option for Translation updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'name'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 695](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L695)



### `mainwp_updates_plugins_sort_by`

*Filter: mainwp_updates_plugins_sort_by*

Filters the default sorting option for Plugin updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'name'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 704](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L704)



### `mainwp_updates_themes_sort_by`

*Filter: mainwp_updates_themes_sort_by*

Filters the default sorting option for Theme updates.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'name'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 713](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L713)



### `mainwp_updates_abandoned_plugins_sort_by`

*Filter: mainwp_updates_abandoned_plugins_sort_by*

Filters the default sorting option for Abandoned plugins.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'name'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 722](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L722)



### `mainwp_updates_abandoned_themes_sort_by`

*Filter: mainwp_updates_abandoned_themes_sort_by*

Filters the default sorting option for Abandoned themes.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`'name'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 731](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L731)



### `mainwp_limit_updates_all`

*Limits number of updates to process.*

Limits the number of updates that will be processed in a single run on Update Everything action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`0` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 748](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L748)



### `mainwp_pages_updates_render_tabs`

*Renders updates page.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`$current_tab` |  | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 383](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L383)



### `mainwp_updates_table_features`

*Filter: mainwp_updates_table_features*

Filters the Updates table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1799](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1799)



### `mainwp_page_hearder_tabs_updates`

*Renders header tabs*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$header_tabs` |  | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1916](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1916)



### `mainwp_updates_hide_show_updates_per`

*Renders header tabs*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$hide_show_updates_per` |  | 
`$current_tab` | `string` | current tab.

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 1916](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L1916)



### `mainwp_manage_updates_limit_loading`

*Method handle_limit_sites().*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`false` |  | 
`'updates'` |  | 

Source: [pages/page-mainwp-updates.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php), [line 2250](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-updates.php#L2250)



### `mainwp-getsubpages-themes`

*Themes Subpages*

Filters subpages for the Themes page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array(array())` |  | 
`'4.0.7.2'` |  | 
`'mainwp_getsubpages_themes'` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 147](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L147)



### `mainwp_getsubpages_themes`

*Method init_menu()*

Initiate the MainWP Themes SubMenu page.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$sub_pages` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 68](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L68)



### `file_mod_allowed`

*Disables themes installation*

Filters whether file modifications are allowed on the Dashboard site. If not, installation process will be disabled too.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`true` |  | 
`'mainwp_install_theme'` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1857](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1857)



### `mainwp_favorites_themes`

*Render the Themes table for the Install Themes Tab.*

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`array()` |  | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 1732](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L1732)



### `mainwp_theme_auto_updates_table_fatures`

*Filter: mainwp_theme_auto_updates_table_fatures*

Filters the Theme Auto Updates table features.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`$table_features` |  | 

**Changelog**

Version | Description
------- | -----------
`4.1` | 

Source: [pages/page-mainwp-themes.php](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php), [line 2371](https://github.com/mainwp/mainwp/blob/master/pages/page-mainwp-themes.php#L2371)



### `mainwp_module_cost_tracker_get_total_cost`

*Method render_sites()*

Grab available Child Sites updates a build Widget.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`0` |  | 

Source: [widgets/widget-mainwp-get-started.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php), [line 46](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-get-started.php#L46)



### `mainwp_plugins_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Plugins', 'mainwp')` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-widget-plugins.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php), [line 137](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-plugins.php#L137)



### `mainwp_themes_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Themes', 'mainwp')` |  | 
`$website` |  | 

Source: [widgets/widget-mainwp-widget-themes.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php), [line 107](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-widget-themes.php#L107)



### `mainwp_limit_updates_all`

*Filter: mainwp_limit_updates_all*

Limits the number of updates that will be processed in a single run on Update Everything action.

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`0` |  | 

**Changelog**

Version | Description
------- | -----------
`4.0` | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 373](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L373)



### `mainwp_updates_overview_widget_title`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Updates Overview', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 475](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L475)



### `mainwp_update_everything_button_text`

**Arguments**

Argument | Type | Description
-------- | ---- | -----------
`esc_html__('Update Everything', 'mainwp')` |  | 

Source: [widgets/widget-mainwp-updates-overview.php](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php), [line 551](https://github.com/mainwp/mainwp/blob/master/widgets/widget-mainwp-updates-overview.php#L551)




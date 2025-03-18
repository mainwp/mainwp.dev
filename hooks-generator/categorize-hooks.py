#!/usr/bin/env python3
"""
Script to categorize MainWP hooks documentation and split into smaller files by category.
"""

import os
import re
import shutil
import sys
from collections import defaultdict

# Define categories and their patterns for automatic categorization
DASHBOARD_CATEGORIES = {
    'site-management': [
        r'site[s]?_', r'site[s]?-', r'website', r'group', r'sync', r'connection', r'disconnect',
        r'mainwp_site_', r'mainwp_group_', r'mainwp_sync_', r'mainwp_connect_'
    ],
    'updates-maintenance': [
        r'update[s]?', r'upgrade', r'install', r'theme', r'plugin', r'core', r'maintenance',
        r'mainwp_update_', r'mainwp_upgrade_', r'mainwp_install_', r'mainwp_theme_', r'mainwp_plugin_'
    ],
    'content-management': [
        r'post[s]?', r'page[s]?', r'comment[s]?', r'media', r'attachment', r'content', r'editor',
        r'mainwp_post_', r'mainwp_page_', r'mainwp_comment_', r'mainwp_media_'
    ],
    'user-management': [
        r'user[s]?', r'role[s]?', r'capability', r'permission', r'access', r'login', r'logout',
        r'mainwp_user_', r'mainwp_role_', r'mainwp_login_'
    ],
    'backups-restoration': [
        r'backup[s]?', r'restore', r'recovery', r'mainwp_backup_', r'mainwp_restore_'
    ],
    'security-monitoring': [
        r'security', r'secure', r'monitor', r'uptime', r'scan', r'check', r'health',
        r'mainwp_security_', r'mainwp_monitor_', r'mainwp_scan_', r'mainwp_health_'
    ],
    'client-reports': [
        r'report[s]?', r'client[s]?', r'mainwp_report_', r'mainwp_client_'
    ],
    'ui-display': [
        r'ui', r'display', r'screen', r'widget', r'dashboard', r'menu', r'notice', r'modal', r'tab',
        r'mainwp_ui_', r'mainwp_display_', r'mainwp_widget_', r'mainwp_menu_', r'mainwp_notice_'
    ],
    'extensions-integration': [
        r'extension[s]?', r'addon[s]?', r'integration', r'mainwp_extension_', r'mainwp_addon_'
    ],
    'api-remote': [
        r'api', r'remote', r'rest', r'request', r'response', r'http', r'mainwp_api_', r'mainwp_remote_', r'mainwp_rest_'
    ],
    'system-settings': [
        r'setting[s]?', r'option[s]?', r'config', r'system', r'mainwp_setting_', r'mainwp_option_', r'mainwp_system_'
    ],
    'misc': []  # Catch-all for hooks that don't match any category
}

CHILD_CATEGORIES = {
    'connection-authentication': [
        r'connect', r'connection', r'auth', r'authentication', r'secure', r'verify',
        r'mainwp_child_connect_', r'mainwp_child_auth_'
    ],
    'updates-maintenance': [
        r'update[s]?', r'upgrade', r'install', r'theme', r'plugin', r'core', r'maintenance',
        r'mainwp_child_update_', r'mainwp_child_upgrade_', r'mainwp_child_install_'
    ],
    'content-handling': [
        r'post[s]?', r'page[s]?', r'comment[s]?', r'media', r'attachment', r'content',
        r'mainwp_child_post_', r'mainwp_child_page_', r'mainwp_child_comment_'
    ],
    'user-operations': [
        r'user[s]?', r'role[s]?', r'capability', r'permission', r'mainwp_child_user_', r'mainwp_child_role_'
    ],
    'backups-restoration': [
        r'backup[s]?', r'restore', r'recovery', r'mainwp_child_backup_', r'mainwp_child_restore_'
    ],
    'security-monitoring': [
        r'security', r'secure', r'monitor', r'scan', r'check', r'health',
        r'mainwp_child_security_', r'mainwp_child_monitor_', r'mainwp_child_scan_'
    ],
    'system-settings': [
        r'setting[s]?', r'option[s]?', r'config', r'system', r'mainwp_child_setting_', r'mainwp_child_option_'
    ],
    'misc': []  # Catch-all for hooks that don't match any category
}

# Category display names (for index pages)
CATEGORY_NAMES = {
    'site-management': 'Site Management',
    'updates-maintenance': 'Updates & Maintenance',
    'content-management': 'Content Management',
    'user-management': 'User Management',
    'backups-restoration': 'Backups & Restoration',
    'security-monitoring': 'Security & Monitoring',
    'client-reports': 'Client Reports',
    'ui-display': 'UI & Display',
    'extensions-integration': 'Extensions & Integration',
    'api-remote': 'API & Remote Communication',
    'system-settings': 'System & Settings',
    'connection-authentication': 'Connection & Authentication',
    'content-handling': 'Content Handling',
    'user-operations': 'User Operations',
    'misc': 'Miscellaneous'
}

# Category descriptions
CATEGORY_DESCRIPTIONS = {
    'site-management': 'Hooks related to adding, editing, removing, and managing sites and site groups.',
    'updates-maintenance': 'Hooks for managing updates to plugins, themes, and WordPress core.',
    'content-management': 'Hooks for managing posts, pages, comments, and other content.',
    'user-management': 'Hooks related to user management, roles, and capabilities.',
    'backups-restoration': 'Hooks for backup creation, management, and restoration processes.',
    'security-monitoring': 'Hooks related to security checks, uptime monitoring, and site health.',
    'client-reports': 'Hooks for report generation, customization, and delivery.',
    'ui-display': 'Hooks for modifying the Dashboard UI, widgets, menus, and display elements.',
    'extensions-integration': 'Hooks related to extensions and third-party integrations.',
    'api-remote': 'Hooks for API endpoints and remote communication with child sites.',
    'system-settings': 'Hooks related to general settings and system configuration.',
    'connection-authentication': 'Hooks for establishing and managing connections between Dashboard and Child sites.',
    'content-handling': 'Hooks for managing content on Child sites.',
    'user-operations': 'Hooks related to user management on Child sites.',
    'misc': 'Miscellaneous hooks that don\'t fit into other categories.'
}

def transform_source_links(hook_entry):
    """Transform source links from local file paths to GitHub repository URLs."""
    # Match the source link pattern
    source_pattern = r'Source: \[(.*?)\]\((.*?)\), \[line (\d+)\]\((.*?)(?:#L\d+-L\d+)?\)'
    
    def replace_source_link(match):
        path_text = match.group(1)
        path_url = match.group(2)
        line_num = match.group(3)
        line_url = match.group(4)
        
        # Determine which repository the file belongs to
        if 'mainwp-dashboard' in path_text:
            repo_url = 'https://github.com/mainwp/mainwp/blob/master/'
            # Extract the path relative to the repository root
            rel_path = path_text.split('mainwp-dashboard/', 1)[1] if 'mainwp-dashboard/' in path_text else path_url
        elif 'mainwp-child' in path_text:
            repo_url = 'https://github.com/mainwp/mainwp-child/blob/master/'
            # Extract the path relative to the repository root
            rel_path = path_text.split('mainwp-child/', 1)[1] if 'mainwp-child/' in path_text else path_url
        else:
            # If we can't determine the repository, keep the original link
            return match.group(0)
        
        # Create the new GitHub URLs
        github_url = f"{repo_url}{rel_path}"
        github_line_url = f"{repo_url}{rel_path}#L{line_num}"
        
        # Return the transformed source link
        return f'Source: [{rel_path}]({github_url}), [line {line_num}]({github_line_url})'
    
    # Replace all source links in the hook entry
    return re.sub(source_pattern, replace_source_link, hook_entry)

def parse_hooks_file(file_path):
    """Parse a hooks documentation file and extract hook entries."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split the file into hook entries
    # Each hook entry starts with ### and continues until the next ### or end of file
    hook_entries = re.split(r'(?=^### )', content, flags=re.MULTILINE)[1:]  # Skip the header
    
    # Transform source links in each hook entry
    transformed_entries = [transform_source_links(entry) for entry in hook_entries]
    
    return transformed_entries

def categorize_hook(hook_entry, categories):
    """Assign a hook to a category based on its name and description."""
    # Extract hook name from the entry
    hook_name_match = re.match(r'^### `([^`]+)`', hook_entry)
    if not hook_name_match:
        return 'misc'
    
    hook_name = hook_name_match.group(1)
    
    # Try to match hook name against category patterns
    for category, patterns in categories.items():
        for pattern in patterns:
            if re.search(pattern, hook_name, re.IGNORECASE):
                return category
    
    # If no match found, check the hook description
    for category, patterns in categories.items():
        for pattern in patterns:
            if re.search(pattern, hook_entry, re.IGNORECASE):
                return category
    
    # If still no match, assign to misc category
    return 'misc'

def create_directory_structure(base_dir):
    """Create the directory structure for categorized hooks."""
    # Create main directories
    os.makedirs(os.path.join(base_dir, 'dashboard', 'actions'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'dashboard', 'filters'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'child', 'actions'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'child', 'filters'), exist_ok=True)
    
    # Create category directories for dashboard actions
    for category in DASHBOARD_CATEGORIES.keys():
        os.makedirs(os.path.join(base_dir, 'dashboard', 'actions', category), exist_ok=True)
    
    # Create category directories for dashboard filters
    for category in DASHBOARD_CATEGORIES.keys():
        os.makedirs(os.path.join(base_dir, 'dashboard', 'filters', category), exist_ok=True)
    
    # Create category directories for child actions
    for category in CHILD_CATEGORIES.keys():
        os.makedirs(os.path.join(base_dir, 'child', 'actions', category), exist_ok=True)
    
    # Create category directories for child filters
    for category in CHILD_CATEGORIES.keys():
        os.makedirs(os.path.join(base_dir, 'child', 'filters', category), exist_ok=True)

def generate_hook_index(hook_entry):
    """Generate an index entry for a hook."""
    hook_name_match = re.match(r'^### `([^`]+)`', hook_entry)
    if not hook_name_match:
        return ''
    
    hook_name = hook_name_match.group(1)
    
    # Extract description (first line after the hook name)
    description_match = re.search(r'^### `[^`]+`\s*\n\s*\*([^\n]+)\*', hook_entry)
    description = description_match.group(1).strip() if description_match else ''
    
    return f"- [`{hook_name}`](#{hook_name.replace('$', '').replace('{', '').replace('}', '').replace(':', '').replace('.', '')}) - {description}"

def generate_category_file(category, hooks, hook_type, component, base_dir):
    """Generate a category file with hooks."""
    output_dir = os.path.join(base_dir, component, hook_type, category)
    output_file = os.path.join(output_dir, 'index.md')
    
    with open(output_file, 'w') as f:
        # Write header
        f.write(f"# {CATEGORY_NAMES[category]} {hook_type.capitalize()}\n\n")
        f.write(f"{CATEGORY_DESCRIPTIONS.get(category, '')}\n\n")
        
        # Write navigation
        f.write("## Navigation\n\n")
        f.write(f"- [Back to All {hook_type.capitalize()}](../index.md)\n")
        f.write(f"- [Back to {component.capitalize()} Hooks](../../index.md)\n")
        f.write("- [Back to Main Hooks Documentation](../../../index.md)\n\n")
        
        # Write hook index
        f.write("## Hooks in this Category\n\n")
        for hook in hooks:
            f.write(f"{generate_hook_index(hook)}\n")
        
        # Write hook details
        f.write("\n## Hook Details\n\n")
        for hook in hooks:
            f.write(f"{hook}\n\n")

def generate_index_files(categorized_hooks, base_dir):
    """Generate index files for the hooks documentation."""
    # Generate main index file
    with open(os.path.join(base_dir, 'index.md'), 'w') as f:
        f.write("# MainWP Hooks Documentation\n\n")
        f.write("This section provides comprehensive documentation for all hooks (actions and filters) available in the MainWP ecosystem.\n\n")
        
        # Dashboard section
        f.write("## Dashboard Hooks\n\n")
        f.write("The [MainWP Dashboard](dashboard/index.md) plugin provides hooks that allow you to extend and customize the MainWP Dashboard functionality.\n\n")
        f.write("- [Actions](dashboard/actions/index.md) - Dashboard actions allow you to add custom functionality at specific points in the MainWP Dashboard execution.\n")
        f.write("- [Filters](dashboard/filters/index.md) - Dashboard filters allow you to modify data or output at specific points in the MainWP Dashboard execution.\n\n")
        
        # Child section
        f.write("## Child Hooks\n\n")
        f.write("The [MainWP Child](child/index.md) plugin provides hooks that allow you to extend and customize the MainWP Child functionality.\n\n")
        f.write("- [Actions](child/actions/index.md) - Child actions allow you to add custom functionality at specific points in the MainWP Child execution.\n")
        f.write("- [Filters](child/filters/index.md) - Child filters allow you to modify data or output at specific points in the MainWP Child execution.\n\n")
        
        # Using hooks section
        f.write("## Using Hooks\n\n")
        f.write("Hooks are the foundation of extending and customizing MainWP. They allow you to add your own functionality or modify existing functionality without modifying the core code.\n\n")
        
        # Actions section
        f.write("### Actions\n\n")
        f.write("Actions allow you to add custom functionality at specific points in the MainWP execution. To use an action, you use the `add_action()` function:\n\n")
        f.write("```php\nadd_action('action_name', 'your_function_name', 10, 2);\n\nfunction your_function_name($arg1, $arg2) {\n    // Your custom code here\n}\n```\n\n")
        
        # Filters section
        f.write("### Filters\n\n")
        f.write("Filters allow you to modify data or output at specific points in the MainWP execution. To use a filter, you use the `add_filter()` function:\n\n")
        f.write("```php\nadd_filter('filter_name', 'your_function_name', 10, 2);\n\nfunction your_function_name($value, $arg2) {\n    // Modify $value here\n    return $value;\n}\n```\n\n")
        
        # Contributing section
        f.write("## Contributing\n\n")
        f.write("If you find any issues with the hooks documentation or would like to suggest improvements, please [open an issue](https://github.com/mainwp/mainwp/issues) on the MainWP GitHub repository.\n")
    
    # Generate dashboard index file
    with open(os.path.join(base_dir, 'dashboard', 'index.md'), 'w') as f:
        f.write("# MainWP Dashboard Hooks\n\n")
        f.write("This section provides documentation for all hooks (actions and filters) available in the MainWP Dashboard plugin.\n\n")
        
        # Actions section
        f.write("## Actions\n\n")
        f.write("[Dashboard Actions](actions/index.md) allow you to add custom functionality at specific points in the MainWP Dashboard execution.\n\n")
        f.write("### Action Categories\n\n")
        
        # List action categories
        for category in DASHBOARD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['dashboard']['actions'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}](actions/{category}/index.md) ({count} hooks) - {CATEGORY_DESCRIPTIONS.get(category, '')}\n")
        
        # Misc category
        misc_count = len(categorized_hooks['dashboard']['actions'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](actions/misc/index.md) ({misc_count} hooks) - {CATEGORY_DESCRIPTIONS.get('misc', '')}\n")
        
        # Filters section
        f.write("\n## Filters\n\n")
        f.write("[Dashboard Filters](filters/index.md) allow you to modify data or output at specific points in the MainWP Dashboard execution.\n\n")
        f.write("### Filter Categories\n\n")
        
        # List filter categories
        for category in DASHBOARD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['dashboard']['filters'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}](filters/{category}/index.md) ({count} hooks) - {CATEGORY_DESCRIPTIONS.get(category, '')}\n")
        
        # Misc category
        misc_count = len(categorized_hooks['dashboard']['filters'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](filters/misc/index.md) ({misc_count} hooks) - {CATEGORY_DESCRIPTIONS.get('misc', '')}\n")
    
    # Generate child index file
    with open(os.path.join(base_dir, 'child', 'index.md'), 'w') as f:
        f.write("# MainWP Child Hooks\n\n")
        f.write("This section provides documentation for all hooks (actions and filters) available in the MainWP Child plugin.\n\n")
        
        # Actions section
        f.write("## Actions\n\n")
        f.write("[Child Actions](actions/index.md) allow you to add custom functionality at specific points in the MainWP Child execution.\n\n")
        f.write("### Action Categories\n\n")
        
        # List action categories
        for category in CHILD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['child']['actions'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}](actions/{category}/index.md) ({count} hooks) - {CATEGORY_DESCRIPTIONS.get(category, '')}\n")
        
        # Misc category
        misc_count = len(categorized_hooks['child']['actions'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](actions/misc/index.md) ({misc_count} hooks) - {CATEGORY_DESCRIPTIONS.get('misc', '')}\n")
        
        # Filters section
        f.write("\n## Filters\n\n")
        f.write("[Child Filters](filters/index.md) allow you to modify data or output at specific points in the MainWP Child execution.\n\n")
        f.write("### Filter Categories\n\n")
        
        # List filter categories
        for category in CHILD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['child']['filters'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}](filters/{category}/index.md) ({count} hooks) - {CATEGORY_DESCRIPTIONS.get(category, '')}\n")
        
        # Misc category
        misc_count = len(categorized_hooks['child']['filters'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](filters/misc/index.md) ({misc_count} hooks) - {CATEGORY_DESCRIPTIONS.get('misc', '')}\n")
    
    # Generate dashboard actions index file
    with open(os.path.join(base_dir, 'dashboard', 'actions', 'index.md'), 'w') as f:
        f.write("# MainWP Dashboard Actions\n\n")
        f.write("This section provides documentation for all action hooks available in the MainWP Dashboard plugin.\n\n")
        f.write("## Categories\n\n")
        
        # List categories
        for category in DASHBOARD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['dashboard']['actions'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}]({category}/index.md) ({count} hooks)\n")
        
        # Misc category
        misc_count = len(categorized_hooks['dashboard']['actions'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](misc/index.md) ({misc_count} hooks)\n")
        
        # Alphabetical list
        f.write("\n## All Actions (Alphabetical)\n\n")
        all_hooks = []
        for category, hooks in categorized_hooks['dashboard']['actions'].items():
            for hook in hooks:
                hook_name_match = re.match(r'^### `([^`]+)`', hook)
                if hook_name_match:
                    hook_name = hook_name_match.group(1)
                    description_match = re.search(r'^### `[^`]+`\s*\n\s*\*([^\n]+)\*', hook)
                    description = description_match.group(1).strip() if description_match else ''
                    all_hooks.append((hook_name, description, category))
        
        # Sort hooks alphabetically
        all_hooks.sort(key=lambda x: x[0].lower())
        
        # Write alphabetical list
        for hook_name, description, category in all_hooks:
            f.write(f"- [`{hook_name}`]({category}/index.md#{hook_name.replace('$', '').replace('{', '').replace('}', '').replace(':', '').replace('.', '')}) - {description}\n")
    
    # Generate dashboard filters index file
    with open(os.path.join(base_dir, 'dashboard', 'filters', 'index.md'), 'w') as f:
        f.write("# MainWP Dashboard Filters\n\n")
        f.write("This section provides documentation for all filter hooks available in the MainWP Dashboard plugin.\n\n")
        f.write("## Categories\n\n")
        
        # List categories
        for category in DASHBOARD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['dashboard']['filters'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}]({category}/index.md) ({count} hooks)\n")
        
        # Misc category
        misc_count = len(categorized_hooks['dashboard']['filters'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](misc/index.md) ({misc_count} hooks)\n")
        
        # Alphabetical list
        f.write("\n## All Filters (Alphabetical)\n\n")
        all_hooks = []
        for category, hooks in categorized_hooks['dashboard']['filters'].items():
            for hook in hooks:
                hook_name_match = re.match(r'^### `([^`]+)`', hook)
                if hook_name_match:
                    hook_name = hook_name_match.group(1)
                    description_match = re.search(r'^### `[^`]+`\s*\n\s*\*([^\n]+)\*', hook)
                    description = description_match.group(1).strip() if description_match else ''
                    all_hooks.append((hook_name, description, category))
        
        # Sort hooks alphabetically
        all_hooks.sort(key=lambda x: x[0].lower())
        
        # Write alphabetical list
        for hook_name, description, category in all_hooks:
            f.write(f"- [`{hook_name}`]({category}/index.md#{hook_name.replace('$', '').replace('{', '').replace('}', '').replace(':', '').replace('.', '')}) - {description}\n")
    
    # Generate child actions index file
    with open(os.path.join(base_dir, 'child', 'actions', 'index.md'), 'w') as f:
        f.write("# MainWP Child Actions\n\n")
        f.write("This section provides documentation for all action hooks available in the MainWP Child plugin.\n\n")
        f.write("## Categories\n\n")
        
        # List categories
        for category in CHILD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['child']['actions'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}]({category}/index.md) ({count} hooks)\n")
        
        # Misc category
        misc_count = len(categorized_hooks['child']['actions'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](misc/index.md) ({misc_count} hooks)\n")
        
        # Alphabetical list
        f.write("\n## All Actions (Alphabetical)\n\n")
        all_hooks = []
        for category, hooks in categorized_hooks['child']['actions'].items():
            for hook in hooks:
                hook_name_match = re.match(r'^### `([^`]+)`', hook)
                if hook_name_match:
                    hook_name = hook_name_match.group(1)
                    description_match = re.search(r'^### `[^`]+`\s*\n\s*\*([^\n]+)\*', hook)
                    description = description_match.group(1).strip() if description_match else ''
                    all_hooks.append((hook_name, description, category))
        
        # Sort hooks alphabetically
        all_hooks.sort(key=lambda x: x[0].lower())
        
        # Write alphabetical list
        for hook_name, description, category in all_hooks:
            f.write(f"- [`{hook_name}`]({category}/index.md#{hook_name.replace('$', '').replace('{', '').replace('}', '').replace(':', '').replace('.', '')}) - {description}\n")
    
    # Generate child filters index file
    with open(os.path.join(base_dir, 'child', 'filters', 'index.md'), 'w') as f:
        f.write("# MainWP Child Filters\n\n")
        f.write("This section provides documentation for all filter hooks available in the MainWP Child plugin.\n\n")
        f.write("## Categories\n\n")
        
        # List categories
        for category in CHILD_CATEGORIES.keys():
            if category == 'misc':
                continue
            count = len(categorized_hooks['child']['filters'].get(category, []))
            if count > 0:
                f.write(f"- [{CATEGORY_NAMES[category]}]({category}/index.md) ({count} hooks)\n")
        
        # Misc category
        misc_count = len(categorized_hooks['child']['filters'].get('misc', []))
        if misc_count > 0:
            f.write(f"- [{CATEGORY_NAMES['misc']}](misc/index.md) ({misc_count} hooks)\n")
        
        # Alphabetical list
        f.write("\n## All Filters (Alphabetical)\n\n")
        all_hooks = []
        for category, hooks in categorized_hooks['child']['filters'].items():
            for hook in hooks:
                hook_name_match = re.match(r'^### `([^`]+)`', hook)
                if hook_name_match:
                    hook_name = hook_name_match.group(1)
                    description_match = re.search(r'^### `[^`]+`\s*\n\s*\*([^\n]+)\*', hook)
                    description = description_match.group(1).strip() if description_match else ''
                    all_hooks.append((hook_name, description, category))
        
        # Sort hooks alphabetically
        all_hooks.sort(key=lambda x: x[0].lower())
        
        # Write alphabetical list
        for hook_name, description, category in all_hooks:
            f.write(f"- [`{hook_name}`]({category}/index.md#{hook_name.replace('$', '').replace('{', '').replace('}', '').replace(':', '').replace('.', '')}) - {description}\n")

def main():
    # Check arguments
    if len(sys.argv) != 3:
        print("Usage: python categorize-hooks.py <input_dir> <output_dir>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Check if input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Parse hooks files
    dashboard_actions = parse_hooks_file(os.path.join(input_dir, 'dashboard', 'actions.md'))
    dashboard_filters = parse_hooks_file(os.path.join(input_dir, 'dashboard', 'filters.md'))
    child_actions = parse_hooks_file(os.path.join(input_dir, 'child', 'actions.md'))
    child_filters = parse_hooks_file(os.path.join(input_dir, 'child', 'filters.md'))
    
    # Categorize hooks
    categorized_hooks = {
        'dashboard': {
            'actions': defaultdict(list),
            'filters': defaultdict(list)
        },
        'child': {
            'actions': defaultdict(list),
            'filters': defaultdict(list)
        }
    }
    
    # Categorize dashboard actions
    for hook in dashboard_actions:
        category = categorize_hook(hook, DASHBOARD_CATEGORIES)
        categorized_hooks['dashboard']['actions'][category].append(hook)
    
    # Categorize dashboard filters
    for hook in dashboard_filters:
        category = categorize_hook(hook, DASHBOARD_CATEGORIES)
        categorized_hooks['dashboard']['filters'][category].append(hook)
    
    # Categorize child actions
    for hook in child_actions:
        category = categorize_hook(hook, CHILD_CATEGORIES)
        categorized_hooks['child']['actions'][category].append(hook)
    
    # Categorize child filters
    for hook in child_filters:
        category = categorize_hook(hook, CHILD_CATEGORIES)
        categorized_hooks['child']['filters'][category].append(hook)
    
    # Create directory structure
    create_directory_structure(output_dir)
    
    # Generate category files
    for category, hooks in categorized_hooks['dashboard']['actions'].items():
        if hooks:
            generate_category_file(category, hooks, 'actions', 'dashboard', output_dir)
    
    for category, hooks in categorized_hooks['dashboard']['filters'].items():
        if hooks:
            generate_category_file(category, hooks, 'filters', 'dashboard', output_dir)
    
    for category, hooks in categorized_hooks['child']['actions'].items():
        if hooks:
            generate_category_file(category, hooks, 'actions', 'child', output_dir)
    
    for category, hooks in categorized_hooks['child']['filters'].items():
        if hooks:
            generate_category_file(category, hooks, 'filters', 'child', output_dir)
    
    # Generate index files
    generate_index_files(categorized_hooks, output_dir)
    
    print(f"Hooks documentation successfully categorized and written to {output_dir}")

if __name__ == "__main__":
    main()

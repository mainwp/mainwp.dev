#!/usr/bin/env python3
"""
Script to categorize MainWP hooks documentation and split into smaller files by category.
"""

import os
import re
import shutil
import sys
from collections import defaultdict
import json # Added for potential future use/debugging


# --- Configuration ---

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

# --- Helper Functions ---

def extract_hook_details(hook_entry):
    """Extract structured details from a raw hook entry string."""
    hook_name_match = re.match(r'^### `([^`]+)`', hook_entry)
    hook_name = hook_name_match.group(1).strip() if hook_name_match else None

    if not hook_name:
        return {'name': None, 'full_entry': hook_entry}

    summary_match = re.search(r'^### `[^`]+`\s*\n\s*\*([^\n]+)\*', hook_entry, re.MULTILINE)
    summary = summary_match.group(1).strip() if summary_match else ''

    desc_block_match = re.search(r'^\*.*?\*\s*\n\n(.*?)(?=\n\*\*Arguments\*\*|\n\*\*Changelog\*\*|\nSource:|\Z)', hook_entry, re.DOTALL | re.MULTILINE)
    description = desc_block_match.group(1).strip() if desc_block_match else ''
    if not summary and not description:
         desc_block_match = re.search(r'^### `[^`]+`\s*\n\n(.*?)(?=\n\*\*Arguments\*\*|\n\*\*Changelog\*\*|\nSource:|\Z)', hook_entry, re.DOTALL | re.MULTILINE)
         description = desc_block_match.group(1).strip() if desc_block_match else ''

    args_match = re.search(r'(\*\*Arguments\*\*\s*\n.*?(?=\n\n|\Z))', hook_entry, re.DOTALL | re.MULTILINE)
    params_table = args_match.group(1).strip() if args_match else ''

    changelog_match = re.search(r'(\*\*Changelog\*\*\s*\n.*?(?=\n\n|\Z))', hook_entry, re.DOTALL | re.MULTILINE)
    changelog_table = changelog_match.group(1).strip() if changelog_match else ''

    source_match = re.search(r'(Source: .*)$', hook_entry, re.MULTILINE)
    source_line = source_match.group(1).strip() if source_match else ''

    return {
        'name': hook_name,
        'summary': summary,
        'description': description,
        'params_table': params_table,
        'changelog_table': changelog_table,
        'source_line': source_line,
        'full_entry': hook_entry
    }

def transform_source_links(source_line):
    """Transform source links from local file paths to GitHub repository URLs."""
    if not source_line or not source_line.startswith('Source:'):
        return source_line

    source_pattern = r'Source:\s*\[([^\]]+)\]\(([^)]+)\),\s*\[line\s*(\d+)\]\(([^)]+)\)'
    match = re.search(source_pattern, source_line)

    if not match:
        print(f"Warning: Could not parse source line format: {source_line}")
        return source_line

    path_text = match.group(1).strip()
    path_url = match.group(2).strip()
    line_num = match.group(3).strip()
    line_url = match.group(4).strip()

    if 'mainwp-dashboard' in path_text or 'mainwp-dashboard' in path_url:
        repo_url_base = 'https://github.com/mainwp/mainwp/blob/master/'
        rel_path = path_text.split('mainwp-dashboard/', 1)[-1]
    elif 'mainwp-child' in path_text or 'mainwp-child' in path_url:
        repo_url_base = 'https://github.com/mainwp/mainwp-child/blob/master/'
        rel_path = path_text.split('mainwp-child/', 1)[-1]
    else:
        print(f"Warning: Could not determine repository for source link: {source_line}")
        if not path_url.startswith('http'):
             return f'Source: [{path_text}]({path_url}), [line {line_num}]({line_url})'
        return source_line

    rel_path = rel_path.lstrip('/')
    github_file_url = f"{repo_url_base}{rel_path}"
    github_line_link_url = f"{repo_url_base}{rel_path}#L{line_num}"

    return f'Source: [{rel_path}]({github_file_url}), [line {line_num}]({github_line_link_url})'


def parse_hooks_file(file_path):
    """Parse a hooks documentation file and extract structured hook details."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Warning: Input file not found: {file_path}. Skipping.")
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

    raw_entries = re.split(r'(?=^### `)', content, flags=re.MULTILINE)
    raw_entries = [entry for entry in raw_entries if entry.strip().startswith('### `')]

    parsed_hooks = []
    for entry in raw_entries:
        if entry.strip():
            details = extract_hook_details(entry)
            if details.get('name'):
                details['source_line'] = transform_source_links(details.get('source_line', ''))
                parsed_hooks.append(details)
            else:
                print(f"Warning: Could not extract hook name from entry starting with: {entry[:50]}...")

    return parsed_hooks

def categorize_hook(hook_details, categories):
    """Assign a hook (represented by its details dict) to a category."""
    if not isinstance(hook_details, dict) or 'name' not in hook_details or not hook_details['name']:
        print(f"Warning: Invalid hook_details format for categorization: {hook_details}")
        return 'misc'

    hook_name = hook_details['name']
    hook_content_for_categorization = hook_details.get('summary', '') + '\n' + hook_details.get('description', '')

    for category, patterns in categories.items():
        if category == 'misc': continue
        for pattern in patterns:
            if re.search(pattern, hook_name, re.IGNORECASE):
                return category

    for category, patterns in categories.items():
         if category == 'misc': continue
         for pattern in patterns:
            if hook_content_for_categorization and re.search(pattern, hook_content_for_categorization, re.IGNORECASE):
                 return category

    return 'misc'


# --- Directory and File Generation ---

def create_directory_structure(base_dir):
    """Create the directory structure for categorized hooks."""
    os.makedirs(base_dir, exist_ok=True)
    components = ['dashboard', 'child']
    hook_types = ['actions', 'filters']

    for comp in components:
        for h_type in hook_types:
            comp_type_dir = os.path.join(base_dir, comp, h_type)
            os.makedirs(comp_type_dir, exist_ok=True)
            categories_for_comp = DASHBOARD_CATEGORIES if comp == 'dashboard' else CHILD_CATEGORIES
            for cat in categories_for_comp.keys():
                 cat_dir = os.path.join(comp_type_dir, cat)
                 os.makedirs(cat_dir, exist_ok=True)


def generate_hook_index_entry(hook_name, hook_data):
    """Generate an index list item for a unique hook."""
    description = hook_data.get('summary', '')
    if not description:
        description = hook_data.get('description', '').split('\n')[0]

    anchor = re.sub(r'[^\w\-]+', '', hook_name.lower().replace('_', '-').replace('\\', '-').replace('$', '-').replace('{', '-').replace('}', '-').replace(':', '-').replace('.', '-'))
    anchor = re.sub(r'-+', '-', anchor).strip('-')

    return f"- [`{hook_name}`](#{anchor}) - {description.strip()}"

def generate_category_file(category, hooks_in_category, hook_type, component, base_dir):
    """Generate a category file with aggregated hooks."""
    output_dir = os.path.join(base_dir, component, hook_type, category)
    output_file = os.path.join(output_dir, 'index.md')

    if not isinstance(hooks_in_category, dict):
        print(f"Error: Expected a dictionary for category '{category}', but got {type(hooks_in_category)}. Skipping file generation.")
        return

    sorted_hook_names = sorted(hooks_in_category.keys(), key=str.lower)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {CATEGORY_NAMES.get(category, category.replace('-', ' ').title())} {hook_type.capitalize()}\n\n")
            f.write(f"{CATEGORY_DESCRIPTIONS.get(category, '')}\n\n")
            f.write("## Navigation\n\n")
            f.write(f"- [Back to All {hook_type.capitalize()}](../index.md)\n")
            f.write(f"- [Back to {component.capitalize()} Hooks](../../index.md)\n")
            f.write("- [Back to Main Hooks Documentation](../../../index.md)\n\n")
            f.write("## Hooks in this Category\n\n")

            if not sorted_hook_names:
                f.write("*No hooks found in this category.*\n")
            else:
                for hook_name in sorted_hook_names:
                    hook_data = hooks_in_category.get(hook_name)
                    if hook_data:
                        f.write(f"{generate_hook_index_entry(hook_name, hook_data)}\n")
                    else:
                         print(f"Warning: Missing hook data for '{hook_name}' in category '{category}' during index generation.")

            f.write("\n---\n\n## Hook Details\n\n")
            if not sorted_hook_names:
                f.write("*No hooks found in this category.*\n")
            else:
                for hook_name in sorted_hook_names:
                    hook_data = hooks_in_category.get(hook_name)
                    if not hook_data:
                        print(f"Warning: Missing hook data for '{hook_name}' in category '{category}' during detail generation.")
                        continue

                    anchor = re.sub(r'[^\w\-]+', '', hook_name.lower().replace('_', '-').replace('\\', '-').replace('$', '-').replace('{', '-').replace('}', '-').replace(':', '-').replace('.', '-'))
                    anchor = re.sub(r'-+', '-', anchor).strip('-')

                    f.write(f"<a id='{anchor}'></a>\n")
                    f.write(f"### `{hook_name}`\n\n")

                    if hook_data.get('summary'):
                        f.write(f"* {hook_data['summary']}\n\n")
                    if hook_data.get('description'):
                        f.write(f"{hook_data['description']}\n\n")
                    if hook_data.get('params_table'):
                        f.write(f"{hook_data['params_table']}\n\n")
                    if hook_data.get('changelog_table'):
                        f.write(f"{hook_data['changelog_table']}\n\n")

                    f.write("**Usage Locations:**\n\n")
                    contexts = hook_data.get('contexts', [])
                    if contexts:
                        unique_contexts = sorted(list(set(contexts)))
                        for context_line in unique_contexts:
                            cleaned_context = context_line.replace('Source: ', '').strip()
                            if cleaned_context:
                                f.write(f"- {cleaned_context}\n")
                    else:
                        f.write("- *Usage location information not available.*\n")

                    f.write("\n---\n\n")
    except Exception as e:
       print(f"Error writing category file {output_file}: {e}")


def generate_index_files(aggregated_hooks, base_dir):
    """Generate index files for the hooks documentation using aggregated data."""
    # --- Generate Main Index File ---
    try:
        with open(os.path.join(base_dir, 'index.md'), 'w', encoding='utf-8') as f:
            f.write("# MainWP Hooks Documentation\n\n")
            f.write("This section provides comprehensive documentation for all hooks (actions and filters) available in the MainWP ecosystem.\n\n")
            f.write("## Dashboard Hooks\n\n")
            f.write("The [MainWP Dashboard](dashboard/index.md) plugin provides hooks that allow you to extend and customize the MainWP Dashboard functionality.\n\n")
            f.write("- [Actions](dashboard/actions/index.md) - Dashboard actions allow you to add custom functionality at specific points in the MainWP Dashboard execution.\n")
            f.write("- [Filters](dashboard/filters/index.md) - Dashboard filters allow you to modify data or output at specific points in the MainWP Dashboard execution.\n\n")
            f.write("## Child Hooks\n\n")
            f.write("The [MainWP Child](child/index.md) plugin provides hooks that allow you to extend and customize the MainWP Child functionality.\n\n")
            f.write("- [Actions](child/actions/index.md) - Child actions allow you to add custom functionality at specific points in the MainWP Child execution.\n")
            f.write("- [Filters](child/filters/index.md) - Child filters allow you to modify data or output at specific points in the MainWP Child execution.\n\n")
            f.write("## Using Hooks\n\n")
            f.write("Hooks are the foundation of extending and customizing MainWP. They allow you to add your own functionality or modify existing functionality without modifying the core code.\n\n")
            f.write("### Actions\n\n")
            f.write("Actions allow you to add custom functionality at specific points in the MainWP execution. To use an action, you use the `add_action()` function:\n\n")
            f.write("```php\nadd_action('action_name', 'your_function_name', 10, 2);\n\nfunction your_function_name(\$arg1, \$arg2) {\n    // Your custom code here\n}\n```\n\n")
            f.write("### Filters\n\n")
            f.write("Filters allow you to modify data or output at specific points in the MainWP execution. To use a filter, you use the `add_filter()` function:\n\n")
            f.write("```php\nadd_filter('filter_name', 'your_function_name', 10, 2);\n\nfunction your_function_name(\$value, \$arg2) {\n    // Modify \$value here\n    return \$value;\n}\n```\n\n")
            f.write("## Contributing\n\n")
            f.write("If you find any issues with the hooks documentation or would like to suggest improvements, please [open an issue](https://github.com/mainwp/mainwp/issues) on the MainWP GitHub repository.\n")
    except Exception as e:
        print(f"Error writing main index file: {e}")


    # --- Generate Component Index Files (e.g., dashboard/index.md) ---
    for comp in ['dashboard', 'child']:
        comp_index_path = os.path.join(base_dir, comp, 'index.md')
        categories_for_comp = DASHBOARD_CATEGORIES if comp == 'dashboard' else CHILD_CATEGORIES
        try:
            with open(comp_index_path, 'w', encoding='utf-8') as f:
                f.write(f"# MainWP {comp.capitalize()} Hooks\n\n")
                f.write(f"This section provides documentation for all hooks (actions and filters) available in the MainWP {comp.capitalize()} plugin.\n\n")

                f.write("## Actions\n\n")
                f.write(f"[{comp.capitalize()} Actions](actions/index.md) allow you to add custom functionality at specific points in the MainWP {comp.capitalize()} execution.\n\n")
                f.write("### Action Categories\n\n")
                action_categories = aggregated_hooks[comp]['actions']
                if not action_categories:
                     f.write("*No action hooks found.*\n")
                else:
                    for category in sorted(categories_for_comp.keys(), key=lambda k: (k == 'misc', CATEGORY_NAMES.get(k, k))):
                        count = len(action_categories.get(category, {}))
                        if count > 0:
                            f.write(f"- [{CATEGORY_NAMES.get(category, category.replace('-', ' ').title())}](actions/{category}/index.md) ({count} hooks) - {CATEGORY_DESCRIPTIONS.get(category, '')}\n")

                f.write("\n## Filters\n\n")
                f.write(f"[{comp.capitalize()} Filters](filters/index.md) allow you to modify data or output at specific points in the MainWP {comp.capitalize()} execution.\n\n")
                f.write("### Filter Categories\n\n")
                filter_categories = aggregated_hooks[comp]['filters']
                if not filter_categories:
                    f.write("*No filter hooks found.*\n")
                else:
                    for category in sorted(categories_for_comp.keys(), key=lambda k: (k == 'misc', CATEGORY_NAMES.get(k, k))):
                        count = len(filter_categories.get(category, {}))
                        if count > 0:
                            f.write(f"- [{CATEGORY_NAMES.get(category, category.replace('-', ' ').title())}](filters/{category}/index.md) ({count} hooks) - {CATEGORY_DESCRIPTIONS.get(category, '')}\n")
        except Exception as e:
            print(f"Error writing component index file {comp_index_path}: {e}")


    # --- Generate Component/Type Index Files (e.g., dashboard/actions/index.md) ---
    for comp in ['dashboard', 'child']:
        categories_for_comp = DASHBOARD_CATEGORIES if comp == 'dashboard' else CHILD_CATEGORIES
        for h_type in ['actions', 'filters']:
            index_file_path = os.path.join(base_dir, comp, h_type, 'index.md')
            try:
                with open(index_file_path, 'w', encoding='utf-8') as f:
                    f.write(f"# MainWP {comp.capitalize()} {h_type.capitalize()}\n\n")
                    f.write(f"This section provides documentation for all {h_type} hooks available in the MainWP {comp.capitalize()} plugin.\n\n")
                    f.write("## Categories\n\n")

                    hooks_by_category = aggregated_hooks[comp][h_type]
                    categories_with_hooks = [cat for cat, hooks in hooks_by_category.items() if hooks]

                    if not categories_with_hooks:
                        f.write("*No categories with hooks found.*\n")
                    else:
                        for category in sorted(categories_with_hooks, key=lambda k: (k == 'misc', CATEGORY_NAMES.get(k, k))):
                            count = len(hooks_by_category.get(category, {}))
                            if count > 0:
                                f.write(f"- [{CATEGORY_NAMES.get(category, category.replace('-', ' ').title())}]({category}/index.md) ({count} hooks)\n")

                    f.write(f"\n## All {h_type.capitalize()} (Alphabetical)\n\n")
                    # Use a dictionary to store unique hooks, keyed by hook name
                    unique_hooks = {}
                    # Correctly iterate over all categories for the current component and hook type
                    all_categories_for_comp_type = aggregated_hooks[comp][h_type]
                    for category, hooks_in_category in all_categories_for_comp_type.items():
                        for hook_name, hook_data in hooks_in_category.items():
                            if hook_name not in unique_hooks:
                                description = hook_data.get('summary', '')
                                if not description:
                                    description = hook_data.get('description', '').split('\n')[0]
                                # Store hook name, description, and the first category found
                                unique_hooks[hook_name] = {
                                    'description': description.strip(),
                                    'category': category
                                }

                    if not unique_hooks:
                        f.write(f"*No {h_type} hooks found.*\n")
                    else:
                        # Sort unique hooks alphabetically by name
                        sorted_unique_hook_names = sorted(unique_hooks.keys(), key=str.lower)
                        for hook_name in sorted_unique_hook_names:
                            hook_info = unique_hooks[hook_name]
                            description = hook_info['description']
                            category = hook_info['category'] # Use the stored category for linking
                            anchor = re.sub(r'[^\w\-]+', '', hook_name.lower().replace('_', '-').replace('\\', '-').replace('$', '-').replace('{', '-').replace('}', '-').replace(':', '-').replace('.', '-'))
                            anchor = re.sub(r'-+', '-', anchor).strip('-')
                            f.write(f"- [`{hook_name}`]({category}/index.md#{anchor}) - {description}\n")
            except Exception as e:
                print(f"Error writing component/type index file {index_file_path}: {e}")


# --- Main Execution ---

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

    # --- Data Aggregation ---
    # Simpler initialization using standard dicts
    aggregated_hooks = {
        'dashboard': {'actions': {}, 'filters': {}},
        'child': {'actions': {}, 'filters': {}}
    }

    # Define processing function to avoid repetition
    def process_hooks(file_path, component, hook_type, categories_map):
        parsed_hooks = parse_hooks_file(file_path)
        for hook_details in parsed_hooks:
            if not hook_details or not hook_details.get('name'):
                print(f"Skipping invalid hook_details: {hook_details}")
                continue # Skip if details are invalid or name is missing

            category = categorize_hook(hook_details, categories_map)
            hook_name = hook_details['name']

            # Ensure category exists
            if category not in aggregated_hooks[component][hook_type]:
                aggregated_hooks[component][hook_type][category] = {} # Initialize category dict

            # Ensure hook exists within the category dict
            if hook_name not in aggregated_hooks[component][hook_type][category]:
                # Initialize the hook data only the first time
                aggregated_hooks[component][hook_type][category][hook_name] = {
                    'summary': hook_details.get('summary', ''),
                    'description': hook_details.get('description', ''),
                    'params_table': hook_details.get('params_table', ''),
                    'changelog_table': hook_details.get('changelog_table', ''),
                    'contexts': [] # Initialize contexts list here
                }
                # print(f"First encounter: {component}/{hook_type}/{category}/{hook_name}") # Optional debug

            # Append context (source line) if it's not empty and not already present
            source_line = hook_details.get('source_line', '')
            if source_line and source_line not in aggregated_hooks[component][hook_type][category][hook_name]['contexts']:
                aggregated_hooks[component][hook_type][category][hook_name]['contexts'].append(source_line)
                # print(f"Adding context to {hook_name}: {source_line}") # Optional debug
            # else: # Optional debug
                # if source_line:
                #     print(f"Context already exists for {hook_name}: {source_line}")
                # else:
                #     print(f"Empty source line for {hook_name}")

    # Process all hook files (Corrected indentation)
    process_hooks(os.path.join(input_dir, 'dashboard', 'actions.md'), 'dashboard', 'actions', DASHBOARD_CATEGORIES)
    process_hooks(os.path.join(input_dir, 'dashboard', 'filters.md'), 'dashboard', 'filters', DASHBOARD_CATEGORIES)
    process_hooks(os.path.join(input_dir, 'child', 'actions.md'), 'child', 'actions', CHILD_CATEGORIES)
    process_hooks(os.path.join(input_dir, 'child', 'filters.md'), 'child', 'filters', CHILD_CATEGORIES)


    # --- Output Generation ---

    # Create directory structure
    create_directory_structure(output_dir)

    # Generate category files using aggregated data
    for component in ['dashboard', 'child']:
        categories_for_comp = DASHBOARD_CATEGORIES if component == 'dashboard' else CHILD_CATEGORIES
        for hook_type in ['actions', 'filters']:
            for category in categories_for_comp.keys():
                hooks_in_category = aggregated_hooks[component][hook_type].get(category)
                if hooks_in_category: # Only generate if category has hooks
                    generate_category_file(category, hooks_in_category, hook_type, component, output_dir)

    # Generate index files using aggregated data
    generate_index_files(aggregated_hooks, output_dir)

    # --- Debugging: Print the aggregated structure ---
    print("\n--- Aggregated Hooks Data (Debug) ---")
    try:
        # Use json for pretty printing the complex dictionary
        print(json.dumps(aggregated_hooks, indent=2))
    except Exception as e:
        print(f"Error printing debug data: {e}")
        print("Raw aggregated_hooks structure:")
        print(aggregated_hooks) # Fallback print
    print("--- End Aggregated Hooks Data ---\n")
    # --- End Debugging ---


    print(f"Hooks documentation successfully categorized and written to {output_dir}")

if __name__ == "__main__":
    main()

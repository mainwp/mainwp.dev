---
layout: documentation-single
title: Getting Started with MainWP Development
description: Learn how to set up your development environment and create your first MainWP extension.
navigation:
  - title: Setup
    items:
      - id: prerequisites
        title: Prerequisites
      - id: environment-setup
        title: Environment Setup
      - id: mainwp-installation
        title: MainWP Installation
  - title: First Steps
    items:
      - id: create-extension
        title: Creating Your First Extension
      - id: basic-structure
        title: Extension Structure
      - id: testing
        title: Testing Your Extension
---

## Prerequisites {#prerequisites}

Before you begin developing for MainWP, ensure you have:

- PHP 7.4 or higher
- WordPress 5.6 or higher
- MainWP Dashboard plugin installed
- A code editor (we recommend VS Code)
- Basic knowledge of PHP and WordPress development

## Environment Setup {#environment-setup}

1. Set up a local WordPress development environment:

```bash
# Using Local by Flywheel or similar tool
local-by-flywheel create-site mainwp-dev
```

2. Install required development tools:

```bash
# Install Composer globally
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

# Install Node.js and npm (optional, for build tools)
brew install node
```

## MainWP Installation {#mainwp-installation}

1. Install the MainWP Dashboard plugin:
   - Download from [MainWP.com](https://mainwp.com)
   - Upload and activate in WordPress
   - Complete the setup wizard

2. Install MainWP Child plugin on test sites:
   - Download the Child plugin
   - Install on your test WordPress sites
   - Connect sites to your dashboard

## Creating Your First Extension {#create-extension}

Start with this basic extension structure:

```php
<?php
/*
Plugin Name: My MainWP Extension
Plugin URI: https://yourwebsite.com/mainwp-extension
Description: Description of your extension
Version: 1.0
Author: Your Name
Author URI: https://yourwebsite.com
Documentation URI: https://yourwebsite.com/docs
*/

class My_MainWP_Extension {
    public function __construct() {
        add_action('init', array($this, 'init'));
    }

    public function init() {
        // Your initialization code here
    }
}

new My_MainWP_Extension();
```

## Extension Structure {#basic-structure}

A typical MainWP extension includes:

- Main plugin file
- Admin interface files
- API handlers
- Helper classes
- Assets (CSS/JS)

Example directory structure:

```
my-mainwp-extension/
├── includes/
│   ├── class-admin.php
│   ├── class-api.php
│   └── class-helpers.php
├── assets/
│   ├── css/
│   └── js/
└── my-mainwp-extension.php
```

## Testing Your Extension {#testing}

1. **Local Testing**
   - Activate your extension on your development site
   - Test all features thoroughly
   - Check for conflicts with other extensions

2. **Debug Mode**
   ```php
   define('MAINWP_DEBUG', true);
   ```

3. **Common Test Cases**
   - Extension activation/deactivation
   - Settings saving/loading
   - API interactions
   - User interface elements
   - Error handling

4. **Testing with Multiple Child Sites**
   - Test with various WordPress versions
   - Test with different server configurations
   - Verify performance with many connected sites

Remember to always follow MainWP's coding standards and best practices when developing your extension. For more detailed information, check out our [Extension Development Guide](/guides/extension-development/).

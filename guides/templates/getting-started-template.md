---
layout: documentation-single
title: Getting Started with MainWP Development
description: A comprehensive guide to start building MainWP add-ons and integrations
permalink: /guides/templates/getting-started-template/
---

Getting Started with MainWP Development

Welcome to MainWP development! This guide will walk you through the essential steps to start building add-ons for MainWP whether you're creating a standalone extension or integrating with a third-party service.

## Your Development Journey

Follow these steps to begin your MainWP development journey:

<div class="mermaid">
flowchart LR
    A["1. Setup Environment"] --> B["2. Choose Add-on Type"]
    B --> C1["3a. Create Basic Extension"]
    B --> C2["3b. Create Basic Integration"]
    C1 --> D["4. Test & Deploy"]
    C2 --> D

    style A fill:#4CAF50stroke:#388E3Ccolor:white
    style B fill:#2196F3stroke:#1976D2color:white
    style C1 fill:#FFC107stroke:#FFA000color:white
    style C2 fill:#FFC107stroke:#FFA000color:white
    style D fill:#9C27B0stroke:#7B1FA2color:white
</div>

## Step 1: Set Up Your Development Environment

<div class="progress-indicator">
<strong>You are here:</strong> Step 1 of 4
</div>

Before you start coding you'll need to set up a proper development environment.

### Essential Requirements

- [ ] WordPress installation (local or development server)
- [ ] MainWP Dashboard plugin installed and activated
- [ ] At least one child site connected to your MainWP Dashboard
- [ ] Code editor (VS Code PhpStorm or similar)
- [ ] Basic understanding of PHP and WordPress plugin development

### Quick Setup Instructions

1. Install a local WordPress development environment like:
   - [LocalWP](https://localwp.com/) (recommended for beginners)
   - [XAMPP](https://www.apachefriends.org/)
   - [MAMP](https://www.mamp.info/)

2. Install and activate the MainWP Dashboard plugin:
   - Download from [WordPress.org](https://wordpress.org/plugins/mainwp/)
   - Or install directly from your WordPress admin area

3. Connect at least one child site:
   - Install WordPress on another local site
   - Install and activate the MainWP Child plugin
   - Connect it to your MainWP Dashboard

4. Install the MainWP Development Extension:
   - Clone from [GitHub](https://github.com/mainwp/mainwp-development-extension)
   - Or download the ZIP file and install manually

For detailed instructions see the [Setting Up a Development Environment](../how-to/setup-environment.md) guide.

## Step 2: Choose Your Add-on Type

<div class="progress-indicator">
<strong>Next step:</strong> Step 2 of 4
</div>

MainWP uses specific terminology to distinguish between different types of add-ons:

- **Extension**: An add-on that works WITHOUT requiring a third-party plugin or API
- **Integration**: An add-on that works WITH a third-party plugin or API

### Which Type Should You Build?

Use this decision tree to determine whether you should build an Extension or an Integration:

<div class="mermaid">
flowchart TD
    A[Do you need to connect with a third-party service or plugin?] -->|Yes| B[Integration]
    A -->|No| C[Extension]
    B --> D[Examples: WooCommerce Integration Google Analytics Integration]
    C --> E[Examples: Advanced Uptime Monitor Advanced Reports Extension]

    style A fill:#2196F3stroke:#1976D2color:white
    style B fill:#FFC107stroke:#FFA000color:white
    style C fill:#FFC107stroke:#FFA000color:white
    style D fill:#9E9E9Estroke:#757575color:white
    style E fill:#9E9E9Estroke:#757575color:white
</div>

### Extension Examples

Extensions are standalone add-ons that extend MainWP's functionality without requiring third-party services:

- **Advanced Uptime Monitor**: Monitors website uptime directly through MainWP
- **Advanced Reports**: Generates custom reports based on MainWP data
- **Maintenance Extension**: Schedules and manages maintenance tasks

### Integration Examples

Integrations connect MainWP with third-party plugins or services:

- **WooCommerce Integration**: Manages WooCommerce stores through MainWP
- **Google Analytics Integration**: Displays Google Analytics data in MainWP
- **Yoast SEO Integration**: Manages Yoast SEO settings across sites

## Step 3a: Create a Basic Extension

<div class="progress-indicator">
<strong>Next step (if building an Extension):</strong> Step 3a of 4
</div>

If you're building a standalone extension follow these steps:

1. Start with the MainWP Development Extension template
2. Customize the plugin information
3. Implement your core functionality
4. Create admin pages and settings
5. Test thoroughly

For detailed instructions see the [Creating a Basic Extension](../how-to/create-basic-extension.md) guide.

## Step 3b: Create a Basic Integration

<div class="progress-indicator">
<strong>Next step (if building an Integration):</strong> Step 3b of 4
</div>

If you're building an integration with a third-party service follow these steps:

1. Start with the MainWP Development Extension template
2. Customize the plugin information
3. Implement third-party API connectivity
4. Create admin pages and settings
5. Implement data synchronization
6. Test thoroughly

For detailed instructions see the [Creating a Basic Integration](../how-to/create-basic-integration.md) guide.

## Step 4: Test and Deploy Your Add-on

<div class="progress-indicator">
<strong>Final step:</strong> Step 4 of 4
</div>

Before releasing your add-on make sure to:

1. Test on multiple child sites
2. Check for any errors or warnings
3. Ensure compatibility with different WordPress versions
4. Package your add-on for distribution
5. Create documentation for users

For detailed instructions see the [Packaging and Distribution](../how-to/packaging-distribution.md) guide.

## Essential Resources

### Documentation

- [MainWP Dashboard API Documentation](../../source-code/dashboard/)
- [MainWP Child API Documentation](../../source-code/child/)
- [MainWP Dashboard Hooks](../../mainwp-hooks/dashboard/)
- [MainWP Child Hooks](../../mainwp-hooks/child/)

### Tools and Templates

- [MainWP Development Extension on GitHub](https://github.com/mainwp/mainwp-development-extension)
- [MainWP API Client PHP on GitHub](https://github.com/mainwp/mainwp-api-client-php)

### Community Support

- [MainWP Community Forum](https://mainwp.com/forum/)
- [MainWP Documentation](https://kb.mainwp.com/)
- [MainWP on GitHub](https://github.com/mainwp)

## Next Steps

After completing the getting started process explore these topics to enhance your MainWP development skills:

- [Using MainWP Actions & Filters](../how-to/actions-filters.md)
- [Building Admin Interfaces](../how-to/admin-interfaces.md)
- [Data Storage and Retrieval](../how-to/data-storage.md)
- [Debugging Add-ons](../how-to/debugging.md)
- [Working with Third-Party APIs](../how-to/third-party-apis.md) (for Integrations)

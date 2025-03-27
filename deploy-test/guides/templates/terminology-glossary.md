# MainWP Terminology Glossary

This glossary defines the key terms used throughout the MainWP documentation to ensure consistency and clarity.

## Core Concepts

### Add-on
The umbrella term for all plugins that extend MainWP's functionality, including both extensions and integrations.

### Extension
A type of add-on that works WITHOUT requiring a third-party plugin or API. Extensions add standalone functionality to MainWP.

### Integration
A type of add-on that works WITH a third-party plugin or API. Integrations connect MainWP with external services or plugins.

### Dashboard
The MainWP Dashboard plugin installed on a single WordPress site that manages multiple child sites.

### Child Site
A WordPress site that is managed by a MainWP Dashboard. Child sites have the MainWP Child plugin installed.

### Child Plugin
The MainWP Child plugin that is installed on sites to be managed by a MainWP Dashboard.

### Connection
The secure link established between a MainWP Dashboard and a child site.

## Development Concepts

### Hook
A WordPress concept that allows code to be injected at specific points in the execution flow. Includes both actions and filters.

### Action
A type of hook that allows you to execute custom code at specific points in the execution flow.

### Filter
A type of hook that allows you to modify data at specific points in the execution flow.

### API
Application Programming Interface. In MainWP, this can refer to:
1. The MainWP API for communication between Dashboard and Child sites
2. Third-party APIs that integrations connect with

### Callback
A function that is passed as an argument to another function and is executed at a specific time or in response to a specific event.

### Extension API
The interface that MainWP provides for extensions to register themselves and interact with the MainWP Dashboard.

### MainWP API Client
A PHP library that simplifies communication with the MainWP API.

## User Interface Terms

### Admin Page
A page in the WordPress admin area that is added by a MainWP extension or integration.

### Dashboard Widget
A widget that appears on the MainWP Dashboard overview page, providing quick access to information or functionality.

### Settings Page
A page where users can configure options for a MainWP extension or integration.

### Overview Page
The main page of the MainWP Dashboard that displays summary information about child sites.

### Individual Dashboard
A feature that allows users to create custom dashboards with specific widgets and information.

## Data Management Terms

### Sync
The process of updating information between the MainWP Dashboard and child sites.

### Backup
A copy of a child site's files and/or database that can be used for restoration.

### Restore
The process of reverting a child site to a previous state using a backup.

### Update
The process of upgrading WordPress core, plugins, or themes on child sites.

### Bulk Update
Updating multiple sites, plugins, or themes simultaneously.

## Security Terms

### Connection Key
A unique identifier used to establish a secure connection between the MainWP Dashboard and a child site.

### OpenSSL
A cryptographic library used by MainWP for secure communication between the Dashboard and child sites.

### Capability
A WordPress permission that determines what actions a user can perform.

### Authentication
The process of verifying the identity of a user or system.

### Authorization
The process of determining whether an authenticated user or system has permission to perform a specific action.

## Technical Terms

### Transient
A WordPress feature for temporarily storing cached data with an expiration time.

### REST API
A way of providing API access using HTTP methods and JSON data format.

### Webhook
A user-defined HTTP callback that is triggered by a specific event.

### Cron Job
A scheduled task that runs automatically at specified intervals.

### Background Process
A task that runs in the background without blocking the user interface.

## MainWP-Specific Features

### Extension Page
The page in the MainWP Dashboard where extensions are listed and can be activated or deactivated.

### Site Group
A way to organize child sites into logical groups for easier management.

### Tag
A label that can be applied to child sites for filtering and organization.

### Client Report
A customizable report that can be generated for clients showing work performed on their sites.

### Uptime Monitoring
A feature that checks if child sites are accessible and functioning properly.

### Site Health
A feature that checks the health and performance of child sites.

## Third-Party Integration Terms

### API Key
A unique identifier used to authenticate with a third-party API.

### OAuth
An open standard for access delegation, commonly used for secure API authentication.

### Webhook
A mechanism for a third-party service to notify MainWP when certain events occur.

### Rate Limit
A restriction on the number of API requests that can be made within a certain time period.

### Endpoint
A specific URL in a third-party API that accepts requests and returns responses.

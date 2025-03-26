# MainWP.dev

MainWP.dev is a dedicated platform for developers working with MainWP, offering documentation, code snippets, and technical resources to extend and customize MainWP.

## Project Structure

- `source-code/dashboard/` - Generated API documentation for MainWP Dashboard
- `source-code/child/` - Generated API documentation for MainWP Child
- `mainwp-hooks/` - Generated hooks documentation (actions and filters)
- `phpdoc/` - phpDocumentor configuration files
- `hooks-generator/` - Scripts for generating and categorizing hooks documentation
- `sources/` - Source repositories for documentation generation
- `.github/workflows/` - GitHub Actions workflows for automation

## Setup Instructions

### Prerequisites

- PHP 7.4 or higher
- Composer
- Git

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/mainwp/mainwp.dev.git
   cd mainwp.dev
   ```

2. Install dependencies:
   ```
   composer install
   ```

3. Clone the MainWP repositories into the sources directory:
   ```
   git clone https://github.com/mainwp/mainwp-dashboard.git sources/mainwp-dashboard
   git clone https://github.com/mainwp/mainwp-child.git sources/mainwp-child
   ```

### Generating Documentation

#### API Documentation

To generate API documentation for the MainWP Dashboard:

```
vendor/bin/phpdoc -c phpdoc/dashboard.xml
```

To generate API documentation for the MainWP Child:

```
vendor/bin/phpdoc -c phpdoc/child.xml
```

Or use the provided script to generate both:

```
./generate-docs.sh
```

#### Hooks Documentation

To generate hooks documentation:

1. Install dependencies in the hooks-generator directory:
   ```
   cd hooks-generator
   composer install
   ```

2. Run the hooks generation script:
   ```
   ./generate-hooks.sh
   ```

3. To generate categorized hooks documentation:
   ```
   ./generate-categorized-hooks.sh
   ```

#### Automated Documentation Generation

The documentation is automatically generated and deployed using GitHub Actions:

1. On a weekly schedule (Sunday at midnight UTC)
2. When a new version tag is pushed
3. When manually triggered via the GitHub Actions workflow
4. When changes are detected in the source repositories (via webhook)

## Directory Structure

The documentation is organized as follows:

- `source-code/dashboard/` - API documentation for MainWP Dashboard
- `source-code/child/` - API documentation for MainWP Child
- Future directories will include:
  - `rest-api/` - REST API documentation
  - `mainwp-hooks/` - Documentation for MainWP hooks (actions & filters)
  - `guides/` - Developer guides and tutorials

## Contributing

Contributions to improve the documentation are welcome. Please submit pull requests to the appropriate repository.

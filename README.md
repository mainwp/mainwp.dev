# MainWP.dev

MainWP.dev is a dedicated platform for developers working with MainWP, offering documentation, code snippets, and technical resources to extend and customize MainWP.

## Project Structure

- `source-code/dashboard/` - Generated documentation for MainWP Dashboard
- `source-code/child/` - Generated documentation for MainWP Child
- `phpdoc/` - phpDocumentor configuration files
- `sources/` - Source repositories for documentation generation

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

To generate documentation for the MainWP Dashboard:

```
vendor/bin/phpdoc -c phpdoc/dashboard.xml
```

To generate documentation for the MainWP Child:

```
vendor/bin/phpdoc -c phpdoc/child.xml
```

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

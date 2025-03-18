# Tech Context

## Technologies Used

1. **phpDocumentor 3.7.1**: The primary documentation generation tool that parses PHP source code and generates structured documentation.

2. **GitHub Actions**: CI/CD platform used to automate the documentation generation and deployment process.

3. **GitHub Pages**: Hosting platform for the generated documentation.

4. **PHP**: The primary programming language of the MainWP ecosystem being documented.

5. **HTML/CSS/JavaScript**: Used for the custom home page and additional developer resources.

6. **Markdown**: Used for supplementary documentation and README files.

7. **XML**: Used for phpDocumentor configuration files.

8. **Git**: Version control system for managing source code and documentation.

9. **Pronamic WP Documentor**: Tool used to extract WordPress hooks (actions and filters) from PHP source code.

10. **Python**: Used for the categorization script that organizes hooks into functional categories.

11. **Bash Scripts**: Used for automation of the documentation generation process.

## Development Setup

1. **Local Environment**:
   - PHP 7.4+ installed locally for testing phpDocumentor
   - Git for version control
   - Text editor or IDE (e.g., VSCode, PHPStorm)
   - Python 3.6+ for running the hooks categorization script
   - Composer for PHP dependencies

2. **GitHub Repository**:
   - Repository for the MainWP.dev documentation project
   - Access to the two MainWP source repositories

3. **phpDocumentor Configuration**:
   - Configuration files for each source repository
   - Custom templates if needed

4. **GitHub Actions Configuration**:
   - Workflow files for automating documentation generation
   - Secrets and permissions configured for repository access

5. **Hooks Documentation Setup**:
   - Pronamic WP Documentor installed via Composer
   - Python script for categorizing hooks
   - Bash scripts for automating the hooks documentation process

## Technical Constraints

1. **phpDocumentor Limitations**:
   - Requires properly documented code with PHPDoc comments
   - May have issues with certain PHP language features
   - Performance considerations for large codebases

2. **GitHub Pages Constraints**:
   - Limited to static content
   - No server-side processing
   - Size limitations for repositories

3. **GitHub Actions Constraints**:
   - Limited execution time for workflows
   - Limited storage for artifacts
   - Rate limiting for API calls

4. **Documentation Completeness**:
   - Dependent on the quality of source code documentation
   - May require manual supplementation for poorly documented areas

5. **Hooks Documentation Constraints**:
   - Dependent on consistent hook naming conventions in the source code
   - Categorization accuracy depends on hook names and descriptions
   - Markdown rendering limitations for complex documentation
   - GitHub repository links require consistent repository structure and branch naming

## Dependencies

1. **External Services**:
   - GitHub (for repository hosting, GitHub Actions, and GitHub Pages)

2. **Software Dependencies**:
   - phpDocumentor 3.7.1
   - PHP 7.4+ (for running phpDocumentor)
   - Git (for version control)
   - Python 3.6+ (for hooks categorization script)
   - Composer (for PHP package management)
   - Pronamic WP Documentor (for hooks extraction)

3. **Source Code Dependencies**:
   - Access to the two MainWP source repositories
   - Properly documented source code with PHPDoc comments
   - WordPress hooks in the source code (for hooks documentation)

4. **Workflow Dependencies**:
   - GitHub Actions runners
   - Repository permissions and secrets
   - Hooks documentation generation workflow

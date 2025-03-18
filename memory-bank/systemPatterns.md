# System Patterns

## System Architecture

The MainWP.dev documentation system follows a CI/CD architecture with the following components:

1. **Source Repositories**: Two MainWP source code repositories that contain the code to be documented.

2. **GitHub Actions Workflow**: Automated workflows that monitor source repositories for changes and trigger the documentation generation process.

3. **phpDocumentor Engine**: The core documentation generation tool that parses PHP source code and generates structured documentation.

4. **GitHub Pages**: The hosting platform where the generated documentation is published and made accessible to developers.

5. **Documentation Structure**:
   - Subdirectories for generated API documentation
   - Main directory for custom content and developer resources

## Key Technical Decisions

1. **phpDocumentor 3.7.1**: Selected for its robust PHP documentation capabilities and active maintenance.

2. **GitHub Actions for Automation**: Chosen to provide seamless integration with the source repositories and automated workflow triggers.

3. **Subdirectory Organization**: Decision to place generated documentation in subdirectories to maintain separation from custom content.

4. **Configuration Exclusions**: Configured phpDocumentor to exclude specific dependencies to focus documentation on relevant code.

5. **Error Handling Strategy**: Implemented comprehensive error handling and logging to ensure reliability of the automated process.

6. **GitHub Pages for Hosting**: Selected for its seamless integration with GitHub Actions and zero-cost hosting solution.

7. **Documentation Format Strategy**: Decision to maintain ReStructuredText (RST) for API reference documentation while creating separate Markdown-based developer guides, leveraging the strengths of each format without the complexity of cross-linking.

## Design Patterns in Use

1. **Observer Pattern**: GitHub Actions workflows observe repository changes and trigger documentation updates.

2. **Factory Pattern**: phpDocumentor configuration creates different documentation outputs based on source inputs.

3. **Facade Pattern**: Simplified interface to the complex documentation generation process through GitHub Actions workflows.

4. **Strategy Pattern**: Different documentation strategies applied to different components of the MainWP ecosystem.

5. **Categorization Pattern**: Hooks documentation uses a categorization system to organize hooks by functionality, making them more discoverable for developers.

6. **Extraction Pattern**: Pronamic WP Documentor extracts hooks from source code and generates structured documentation.

7. **Complementary Documentation Pattern**: Using different documentation formats (RST and Markdown) for different types of documentation (API reference vs. conceptual guides) to leverage the strengths of each format.

8. **Optimal Reference Strategy**: Developer guides reference API docs for formal definitions, GitHub for implementation examples, and other guides for conceptual relationships, creating a comprehensive documentation ecosystem.

## Component Relationships

1. **Source Repositories → GitHub Actions**: Source code changes trigger GitHub Actions workflows.

2. **GitHub Actions → phpDocumentor**: Workflows execute phpDocumentor with appropriate configuration.

3. **phpDocumentor → Documentation Output**: phpDocumentor generates HTML/XML documentation from source code.

4. **Documentation Output → GitHub Pages**: Generated documentation is deployed to GitHub Pages.

5. **Custom Content → GitHub Pages**: Manually created content is preserved in the main directory.

6. **Error Logs → Monitoring**: Error handling system captures and reports issues in the documentation process.

7. **Source Repositories → Pronamic WP Documentor**: Source code is analyzed to extract hooks documentation.

8. **Pronamic WP Documentor → Hooks Documentation**: Raw hooks documentation is generated from source code.

9. **Hooks Documentation → Categorization Script**: Raw hooks documentation is processed and categorized.

10. **Categorization Script → Organized Documentation**: Hooks are organized into functional categories for better discoverability.

11. **Source Code → GitHub Repository Links**: Source code references in hooks documentation are transformed into direct links to the GitHub repository, allowing developers to easily view the implementation.

12. **API Reference (RST) ↔ Developer Guides (Markdown)**: Complementary documentation types that reference each other to provide a complete picture of the system.

13. **Developer Guides → Multiple Reference Sources**: Developer guides link to API docs, GitHub source code, and other guides to provide comprehensive context.

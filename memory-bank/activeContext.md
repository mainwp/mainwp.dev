# Active Context

## Current Work Focus

1. **Developer Guides Implementation**: Creating comprehensive Markdown-based developer guides for third-party developers building MainWP add-ons (both extensions and integrations).

2. **Documentation Integration**: Ensuring seamless integration between API reference documentation, hooks documentation, and the new developer guides.

3. **Custom Content Development**: Enhancing the custom home page and navigation to include the new developer guides.

4. **Source Code Verification**: Cross-referencing documentation with source code to ensure accuracy and currency.

5. **Documentation Structure Design**: Implementing a layered documentation approach that serves both new and experienced developers.

6. **Terminology Update**: Implementing the new terminology distinction between "add-ons" (umbrella term), "extensions" (standalone add-ons), and "integrations" (add-ons that work with third-party plugins or APIs).

## Recent Changes

1. **Repository Integration**: Cloned the MainWP Dashboard and Child repositories into the sources directory.

2. **phpDocumentor Configuration Fix**: Fixed the phpDocumentor configuration to correctly locate dependencies by modifying the reflection.yaml file.

3. **Guides Feature Adjustment**: Disabled the guides feature in phpDocumentor configuration as it was causing errors and the source repositories don't have guides documentation.

4. **Documentation Generation Success**: Successfully generated documentation for both MainWP Dashboard and Child repositories.

5. **Custom Home Page**: Created a custom home page (index.html) with navigation to the generated documentation.

6. **Directory Structure Verification**: Confirmed the directory structure is working correctly with source-code/dashboard and source-code/child for the generated documentation.

7. **Hooks Documentation Implementation**: Created a system for generating and categorizing hooks documentation using Pronamic WP Documentor and a custom Python script.

8. **GitHub Actions Workflows**: Implemented GitHub Actions workflows for automating the documentation generation and deployment process.

9. **Functional Categorization**: Organized hooks into developer-friendly functional categories like Site Management, Updates & Maintenance, Content Management, etc.

10. **Hooks Documentation Source Links**: Modified the hooks documentation generation script to transform local file paths to GitHub repository URLs, making the documentation more useful for developers.

11. **Directory Structure Fix**: Corrected an issue with the hooks documentation directory structure to ensure proper organization and accessibility.

12. **Terminology Update Implementation**: Updated documentation to use new terminology distinguishing between add-ons (umbrella term), extensions (standalone add-ons), and integrations (third-party add-ons).

13. **Developer Guides Creation**: Created comprehensive guides for both extension and integration development, including:
    - guides/how-to/create-basic-extension.md: Guide for creating standalone add-ons
    - guides/how-to/create-basic-integration.md: Guide for creating third-party add-ons
    - guides/how-to/third-party-apis.md: Guide for working with third-party APIs
    - guides/best-practices/api-integration.md: Guide for API integration best practices
    - guides/reference/api-integration-patterns.md: Guide for API integration patterns
    - guides/how-to/mainwp-api-client.md: Guide for using the official MainWP API Client PHP

14. **Decision Tree Implementation**: Added a mermaid flowchart to guides/index.md to help developers determine whether to build an Extension or Integration.

15. **Part-Time Developer Focus**: Optimized documentation for developers creating MainWP add-ons as a side project with clear pathways, code snippets, and troubleshooting help.

16. **Link Structure Improvements**: Updated all internal links to use relative paths instead of absolute paths for better portability.

17. **Documentation Terminology Consistency**: Improved guides/index.md to explicitly mention both standalone extensions and third-party integrations in the "Who These Guides Are For" section, ensuring developers immediately understand that the guides apply to both development paths.

18. **Integration-Specific Hooks Documentation**: Enhanced guides/how-to/actions-filters.md with a comprehensive new section specifically about using hooks in third-party integrations, including examples for API communication, error handling, caching responses, and securely handling credentials.

19. **API Integration Documentation Improvements**:
    - Enhanced guides/best-practices/api-integration.md with a real-world MainWP example of Google Analytics integration and a "Common Pitfalls" section
    - Improved guides/reference/api-integration-patterns.md with a decision tree flowchart and simplified explanations for complex patterns
    - Created guides/how-to/mainwp-api-client.md with comprehensive documentation for the official MainWP API Client PHP
    - Updated guides/index.md to include the new MainWP API Client PHP guide

## Next Steps

1. **Complete Developer Guides Implementation**:
   - Create additional guides for specific integration scenarios:
     * WooCommerce Integration Guide
     * Social Media API Integration Guide
   - Add more code snippets and templates for common integration patterns
   - Expand the MainWP API Client PHP guide with more real-world examples

2. **Update Existing Documentation**:
   - Review and update any remaining instances of old terminology
   - Ensure consistent terminology usage across all documentation
   - Add more examples and use cases for both extensions and integrations

3. **Enhance Integration-Specific Content**:
   - Create detailed guides for authentication methods (API keys, OAuth, JWT)
   - Add troubleshooting guides for common API issues
   - Develop best practices for API rate limiting and caching
   - Create security guidelines for handling API credentials

4. **Implement Hook Firing Order Documentation**:
   - Document the general sequence of when major MainWP hooks fire
   - Provide guidance on choosing appropriate priorities
   - Identify hook dependency chains
   - Document common pitfalls related to hook timing

6. **Update Main Navigation**:
   - Modify index.html to include prominent links to developer guides
   - Ensure consistent navigation between all documentation types

7. **Set Up GitHub Pages**: Configure GitHub Pages for hosting the generated documentation.

8. **Enhance Error Handling**: Improve error handling and logging for the automated process.

9. **Test GitHub Actions Workflows**: Test the GitHub Actions workflows to ensure they work correctly.

10. **Verify GitHub Links**: Ensure all GitHub repository links in the hooks documentation are working correctly and pointing to the right files and line numbers.

11. **Evaluate Documentation Format Options**: Assess the benefits of adding Markdown-based API documentation alongside the existing RST format, potentially using a dual documentation approach with separate directories.

## Active Decisions and Considerations

1. **Terminology Update**: Adopted new terminology to distinguish between different types of MainWP add-ons:
   - **Add-on(s)**: Umbrella term for all add-ons
   - **Extension**: An add-on that works WITHOUT a third-party plugin or API
   - **Integration**: An add-on that works WITH a third-party plugin or API

2. **Layered Documentation Strategy**: Implementing a progressive disclosure approach with:
   - Quick Start sections for experienced developers
   - Detailed explanations for new developers
   - Well-organized reference material for all developers

3. **Content Design Principles**:
   - Scannable content with clear headings and structure
   - Progressive complexity from basic to advanced topics
   - Practical, real-world code examples with copy-paste snippets
   - Visual signposting to distinguish content types
   - Contextual cross-references for non-linear exploration

4. **Part-Time Developer Focus**: Optimizing documentation for developers who are creating MainWP add-ons as a side project:
   - Quick start guides that respect time constraints
   - Clear pathways for both Extension and Integration development
   - Ready-to-use code snippets that can be adapted
   - Focused, practical implementation guidance
   - Troubleshooting help for common issues

3. **Source Code Verification**: Ensuring documentation accuracy by cross-referencing with:
   - Current mainwp/mainwp and mainwp/mainwp-child repositories
   - Generated PHPDocumentor output
   - Hooks implementation in source code

4. **Documentation Completeness**: The quality of generated documentation depends on the completeness of PHPDoc comments in the source code. Some areas may need manual enhancement.

5. **Error Handling Strategy**: Need to decide on the best approach for handling and reporting errors in the documentation generation process.

6. **Update Frequency**: Determining how often the documentation should be regenerated - on every commit, daily, or on specific events.

7. **Performance Optimization**: The documentation generation process takes about 20-30 seconds for each repository. This is acceptable for local development but may need optimization for automated workflows.

8. **Diagram Generation**: The class diagram generation is failing due to missing PlantUML binary. Need to decide whether to install PlantUML or disable diagram generation.

9. **File Name Length Issues**: Some files in the Child repository have very long names that cause warnings. May need to implement a solution to handle these cases.

10. **Documentation Format Strategy**: Evaluated options between RST (current) and Markdown (available since phpDocumentor v3.6.0). Decided that RST provides superior structural information for API documentation, while Markdown would be better for narrative documentation. Implementing a dual approach with separate directories rather than a hybrid cross-linked system.

11. **Developer Guides Reference Strategy**: Implementing an optimal reference strategy for developer guides that links to API docs for formal definitions, GitHub for implementation examples, and other guides for conceptual relationships.

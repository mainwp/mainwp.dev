/**
 * MainWP.dev Code Block Functionality
 * Handles code block interaction, including syntax highlighting with Highlight.js
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Highlight.js if it exists
    if (typeof hljs !== 'undefined') {
        hljs.configure({
            ignoreUnescapedHTML: true
        });
        hljs.highlightAll();
    }

    // Find all code blocks with copy buttons
    const copyButtons = document.querySelectorAll('.code-block .copy-button');
    
    if (copyButtons.length === 0) {
        // If no copy buttons found in theme-style blocks, look for pre>code blocks
        // and add copy buttons to them (excluding mermaid diagrams)
        const codeBlocks = document.querySelectorAll('pre:not(.no-copy):not(.mermaid) > code[class*="language-"], pre:not(.no-copy):not(.mermaid) > code[class*="hljs"]');
        
        codeBlocks.forEach(codeBlock => {
            const pre = codeBlock.parentElement;
            
            // Create wrapper if needed
            let wrapper = pre.parentElement;
            if (!wrapper.classList.contains('code-block')) {
                wrapper = document.createElement('div');
                wrapper.className = 'code-block';
                pre.parentNode.insertBefore(wrapper, pre);
                wrapper.appendChild(pre);
                
                // Add header with language label and copy button
                const header = document.createElement('div');
                header.className = 'code-header';
                
                // Try to extract language from class
                let language = 'code';
                const langClass = codeBlock.className.match(/language-(\w+)/) || codeBlock.className.match(/hljs language-(\w+)/);
                if (langClass && langClass[1]) {
                    language = langClass[1].toUpperCase();
                }
                
                const langLabel = document.createElement('span');
                langLabel.className = 'language-label';
                langLabel.textContent = language;
                
                const copyBtn = document.createElement('button');
                copyBtn.className = 'copy-button';
                copyBtn.textContent = 'Copy';
                
                header.appendChild(langLabel);
                header.appendChild(copyBtn);
                wrapper.insertBefore(header, pre);
                
                // Add to our collection
                copyButtons.push(copyBtn);
            }
        });
    }
    
    // Add click event to all copy buttons
    document.addEventListener('click', function(event) {
        if (event.target.matches('.copy-button')) {
            const button = event.target;
            const codeBlock = button.closest('.code-block');
            const codeElement = codeBlock.querySelector('code');
            
            navigator.clipboard.writeText(codeElement.textContent).then(() => {
                button.textContent = 'Copied!';
                button.classList.add('copied');
                
                setTimeout(() => {
                    button.textContent = 'Copy';
                    button.classList.remove('copied');
                }, 2000);
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Mobile navigation toggle
    const navTrigger = document.querySelector('.js-nav-trigger');
    const navWrap = document.querySelector('.c-nav-wrap');
    
    if (navTrigger && navWrap) {
        navTrigger.addEventListener('click', function() {
            navWrap.classList.toggle('is-active');
            navTrigger.classList.toggle('is-active');
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add active class to current navigation item
    const currentPath = window.location.pathname;
    document.querySelectorAll('.c-nav__link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('is-active');
        }
    });

    // Add copy button to code blocks
    document.querySelectorAll('pre code').forEach((block) => {
        const button = document.createElement('button');
        button.className = 'c-copy-button';
        button.innerHTML = 'Copy';
        
        const pre = block.parentNode;
        pre.style.position = 'relative';
        pre.appendChild(button);
        
        button.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(block.textContent);
                button.innerHTML = 'Copied!';
                setTimeout(() => {
                    button.innerHTML = 'Copy';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy text: ', err);
                button.innerHTML = 'Failed';
                setTimeout(() => {
                    button.innerHTML = 'Copy';
                }, 2000);
            }
        });
    });

    // Add anchor links to headings
    document.querySelectorAll('h2, h3, h4').forEach((heading) => {
        if (heading.id) {
            const anchor = document.createElement('a');
            anchor.className = 'c-heading-anchor';
            anchor.href = `#${heading.id}`;
            anchor.innerHTML = '#';
            heading.appendChild(anchor);
        }
    });

    // Handle external links
    document.querySelectorAll('a').forEach(link => {
        const url = new URL(link.href, window.location.origin);
        if (url.host !== window.location.host) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});

// Add styles for new elements
const style = document.createElement('style');
style.textContent = `
    .c-copy-button {
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
        padding: 0.25rem 0.5rem;
        background-color: var(--mainwp-primary);
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 0.8rem;
        opacity: 0;
        transition: opacity 0.2s;
    }

    pre:hover .c-copy-button {
        opacity: 1;
    }

    .c-copy-button:hover {
        background-color: var(--mainwp-primary-dark);
    }

    .c-heading-anchor {
        opacity: 0;
        padding-left: 0.5rem;
        color: var(--mainwp-primary);
        text-decoration: none;
        transition: opacity 0.2s;
    }

    h2:hover .c-heading-anchor,
    h3:hover .c-heading-anchor,
    h4:hover .c-heading-anchor {
        opacity: 1;
    }

    .c-nav__link.is-active {
        color: var(--mainwp-primary);
        font-weight: 600;
    }
`;
document.head.appendChild(style);

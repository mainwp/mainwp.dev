document.addEventListener('DOMContentLoaded', function() {
    // Initialize navigation state from localStorage
    const navState = JSON.parse(localStorage.getItem('navState') || '{}');
    
    // Setup collapsible sections
    const sections = document.querySelectorAll('.c-page-nav__section');
    sections.forEach(section => {
        const heading = section.querySelector('.js-toggle-nav');
        const sectionId = section.dataset.section;
        
        // Restore state from localStorage
        if (navState[sectionId]) {
            section.classList.add('is-expanded');
        }
        
        heading.addEventListener('click', () => {
            section.classList.toggle('is-expanded');
            
            // Save state to localStorage
            navState[sectionId] = section.classList.contains('is-expanded');
            localStorage.setItem('navState', JSON.stringify(navState));
        });
    });

    // Scroll spy functionality
    let scrollTimeout;
    const navLinks = document.querySelectorAll('.c-page-nav__link');
    const contentSections = Array.from(document.querySelectorAll('[id]'));
    
    function updateActiveSection() {
        const scrollPosition = window.scrollY + 100; // Offset for header

        // Find the current section
        const currentSection = contentSections.find(section => {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;
            return scrollPosition >= sectionTop && scrollPosition < sectionBottom;
        });

        if (currentSection) {
            // Remove active class from all items
            navLinks.forEach(link => {
                link.parentElement.classList.remove('is-active');
            });

            // Add active class to current section's nav item
            const activeLink = document.querySelector(`.c-page-nav__link[href="#${currentSection.id}"]`);
            if (activeLink) {
                activeLink.parentElement.classList.add('is-active');
                
                // Expand parent section if collapsed
                const parentSection = activeLink.closest('.c-page-nav__section');
                if (parentSection && !parentSection.classList.contains('is-expanded')) {
                    parentSection.classList.add('is-expanded');
                    const sectionId = parentSection.dataset.section;
                    navState[sectionId] = true;
                    localStorage.setItem('navState', JSON.stringify(navState));
                }
            }
        }
    }

    // Throttle scroll event
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(updateActiveSection);
    });

    // Smooth scroll to section when clicking nav links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile navigation toggle
    const toggleButton = document.createElement('button');
    toggleButton.className = 'c-page-nav__toggle';
    toggleButton.setAttribute('aria-label', 'Toggle navigation');
    toggleButton.innerHTML = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 12H21M3 6H21M3 18H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
    `;

    const pageNav = document.querySelector('.c-page-nav');
    document.body.appendChild(toggleButton);

    toggleButton.addEventListener('click', () => {
        pageNav.classList.toggle('is-visible');
    });

    // Close mobile nav when clicking outside
    document.addEventListener('click', (e) => {
        if (pageNav.classList.contains('is-visible') && 
            !pageNav.contains(e.target) && 
            !toggleButton.contains(e.target)) {
            pageNav.classList.remove('is-visible');
        }
    });

    // Initial update
    updateActiveSection();
});

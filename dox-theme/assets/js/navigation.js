document.addEventListener('DOMContentLoaded', function() {
    // Navigation elements
    const navTrigger = document.querySelector('.js-nav-trigger');
    const navWrap = document.querySelector('.c-nav-wrap');
    const dropdownLinks = document.querySelectorAll('.c-nav__link[data-dropdown]');
    const dropdowns = document.querySelectorAll('.c-nav__dropdown');

    // Mobile menu toggle
    if (navTrigger && navWrap) {
        navTrigger.addEventListener('click', function() {
            console.log('Mobile nav trigger clicked!'); // DEBUG
            const isExpanded = navTrigger.getAttribute('aria-expanded') === 'true';
            navTrigger.setAttribute('aria-expanded', !isExpanded);
            navTrigger.classList.toggle('is-active');
            navWrap.classList.toggle('is-active');
        });
    }

    // Dropdown functionality
    dropdownLinks.forEach(link => {
        const dropdown = link.nextElementSibling;
        
        // Click handler for mobile
        link.addEventListener('click', function(e) {
            console.log('Dropdown link clicked (mobile check)'); // DEBUG
            if (window.innerWidth <= 768) {
                console.log('Mobile detected, toggling dropdown'); // DEBUG
                e.preventDefault();
                const isExpanded = link.getAttribute('aria-expanded') === 'true';

                // Close other dropdowns
                dropdownLinks.forEach(otherLink => {
                    if (otherLink !== link) {
                        otherLink.setAttribute('aria-expanded', 'false');
                        otherLink.nextElementSibling.classList.remove('is-active');
                    }
                });

                // Toggle current dropdown
                link.setAttribute('aria-expanded', !isExpanded);
                dropdown.classList.toggle('is-active');
            }
        });

        // Hover handler for desktop with delay and dropdown hover support
        if (window.innerWidth > 768) {
            const parentItem = link.closest('.c-nav__item');
            let closeTimeout;
            const delay = 500; // milliseconds (Increased from 300ms)

            // Function to open the dropdown
            const openDropdown = () => {
                clearTimeout(closeTimeout); // Clear any pending close timeout
                // Close other open dropdowns immediately
                dropdownLinks.forEach(otherLink => {
                    const otherParent = otherLink.closest('.c-nav__item');
                    if (otherParent !== parentItem) {
                        otherLink.setAttribute('aria-expanded', 'false');
                        if (otherLink.nextElementSibling) {
                           otherLink.nextElementSibling.classList.remove('is-active');
                        }
                    }
                });
                // Open this dropdown
                link.setAttribute('aria-expanded', 'true');
                if (dropdown) {
                    dropdown.classList.add('is-active');
                }
            };

            // Function to start the close timer
            const startCloseTimer = () => {
                clearTimeout(closeTimeout); // Clear existing timer before starting new one
                closeTimeout = setTimeout(() => {
                    console.log('Close timeout executed for:', link.textContent.trim()); // DEBUG
                    link.setAttribute('aria-expanded', 'false');
                    if (dropdown) {
                        dropdown.classList.remove('is-active');
                    }
                }, delay);
            };

            // Add listeners to both parent item and dropdown
            [parentItem, dropdown].forEach(element => {
                if (element) { // Check if dropdown exists
                    element.addEventListener('mouseenter', () => {
                        console.log('Mouseenter on parent or dropdown:', link.textContent.trim()); // DEBUG
                        openDropdown(); // Open or keep open, clear close timer
                    });

                    element.addEventListener('mouseleave', () => {
                        console.log('Mouseleave from parent or dropdown:', link.textContent.trim()); // DEBUG
                        startCloseTimer(); // Start timer to close
                    });
                }
            });
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.c-nav__item')) {
            dropdownLinks.forEach(link => {
                link.setAttribute('aria-expanded', 'false');
                link.nextElementSibling.classList.remove('is-active');
            });
        }
    });

    // Handle keyboard navigation
    dropdownLinks.forEach(link => {
        link.addEventListener('keydown', function(e) {
            const dropdown = link.nextElementSibling;
            const dropdownLinks = dropdown.querySelectorAll('.c-nav__dropdown-link');
            
            switch(e.key) {
                case 'Enter':
                case ' ':
                    e.preventDefault();
                    const isExpanded = link.getAttribute('aria-expanded') === 'true';
                    link.setAttribute('aria-expanded', !isExpanded);
                    dropdown.classList.toggle('is-active');
                    if (!isExpanded && dropdownLinks.length) {
                        dropdownLinks[0].focus();
                    }
                    break;
                case 'Escape':
                    link.setAttribute('aria-expanded', 'false');
                    dropdown.classList.remove('is-active');
                    link.focus();
                    break;
            }
        });
    });

    // Set active states based on current URL
    function setActiveStates() {
        const currentPath = window.location.pathname;
        
        document.querySelectorAll('.c-nav__link, .c-nav__dropdown-link').forEach(link => {
            const href = link.getAttribute('href');
            if (href && currentPath.includes(href)) {
                link.classList.add('is-active');
                
                // If it's a dropdown link, also activate its parent
                const parentItem = link.closest('.c-nav__item');
                if (parentItem) {
                    const parentLink = parentItem.querySelector('.c-nav__link');
                    if (parentLink) {
                        parentLink.classList.add('is-active');
                    }
                }
            }
        });
    }

    // Initialize active states
    setActiveStates();

    // Update active states on navigation
    window.addEventListener('popstate', setActiveStates);
});

/**
 * Mobile Navigation functionality
 */
// Theme toggle functionality removed as light mode is disabled.
document.addEventListener('DOMContentLoaded', function() {
    const navTrigger = document.querySelector('.js-nav-trigger');
    const navWrap = document.querySelector('.c-nav-wrap');
    
    if (navTrigger && navWrap) {
        navTrigger.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            
            this.setAttribute('aria-expanded', !isExpanded);
            this.classList.toggle('is-active');
            navWrap.classList.toggle('is-active');
            
            // Prevent body scroll when menu is open
            document.body.style.overflow = isExpanded ? '' : 'hidden';
        });

        // Close menu on window resize (e.g., when switching to desktop view)
        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                navTrigger.classList.remove('is-active');
                navWrap.classList.remove('is-active');
                navTrigger.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInside = navWrap.contains(event.target) || 
                                navTrigger.contains(event.target);
            
            if (!isClickInside && navWrap.classList.contains('is-active')) {
                navTrigger.classList.remove('is-active');
                navWrap.classList.remove('is-active');
                navTrigger.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
    }
});

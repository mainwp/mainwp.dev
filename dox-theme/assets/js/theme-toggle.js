/**
 * Theme toggle functionality
 */
(function() {
  // DOM elements
  const html = document.documentElement;
  const themeToggle = document.querySelector('.c-theme-toggle');
  
  // Theme constants
  const THEME_KEY = 'dox-theme-preference';
  const DARK_CLASS = 'dark-mode';
  const LIGHT_CLASS = 'light-mode';
  
  /**
   * Get the user's theme preference
   * @returns {string|null} The stored theme preference or null
   */
  function getStoredTheme() {
    return localStorage.getItem(THEME_KEY);
  }
  
  /**
   * Store the user's theme preference
   * @param {string} theme The theme to store ('dark' or 'light')
   */
  function storeTheme(theme) {
    localStorage.setItem(THEME_KEY, theme);
  }
  
  /**
   * Get the system's theme preference
   * @returns {string} The system theme preference ('dark' or 'light')
   */
  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  
  /**
   * Apply the theme
   * @param {string} theme The theme to apply ('dark' or 'light')
   */
  function applyTheme(theme) {
    if (theme === 'dark') {
      html.classList.add(DARK_CLASS);
      html.classList.remove(LIGHT_CLASS);
    } else {
      html.classList.add(LIGHT_CLASS);
      html.classList.remove(DARK_CLASS);
    }
    
    // Update button aria-label
    if (themeToggle) {
      themeToggle.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
  }
  
  /**
   * Initialize the theme
   */
  function initTheme() {
    // Get stored theme or fallback to system preference
    const storedTheme = getStoredTheme();
    const theme = storedTheme || getSystemTheme();
    
    // Apply initial theme
    applyTheme(theme);
    
    // Set up theme toggle button if it exists
    if (themeToggle) {
      themeToggle.addEventListener('click', () => {
        const newTheme = html.classList.contains(DARK_CLASS) ? 'light' : 'dark';
        applyTheme(newTheme);
        storeTheme(newTheme);
      });
    }
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!getStoredTheme()) {
        applyTheme(e.matches ? 'dark' : 'light');
      }
    });
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTheme);
  } else {
    initTheme();
  }
})();

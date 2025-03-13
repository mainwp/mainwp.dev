# MainWP Developer Changelog

This changelog tracks changes to the MainWP core that may affect third-party extensions and developers. The purpose is to provide clear documentation of API changes, deprecations, and breaking changes to help extension developers stay current with MainWP development.

## Color Key
- 🟢 **Added**: New features or capabilities
- 🔵 **Fixed**: Bug fixes
- 🟠 **Changed**: Feature modifications or changes
- ⚫ **Deprecated**: Features planned for removal in future versions
- 🔴 **Removed**: Features that have been removed
- 🟣 **Security**: Security-related fixes or changes
- ⚡ **Performance**: Performance improvements
- 🟡 **Other**: Other changes that don't fit the categories above

Each entry includes:
- The type of change
- A description of what changed
- The expected release version and/or date (when available)
- Any action required by extension developers

---

# March 13, 2025 (Example changelog entry) 

## 🔧 Core Changes
- 🟢 **Added** [v5.1 - April 2025]: New filter hook `mainwp_pre_process_site_data` that runs before site data processing
- ⚫ **Deprecated** [v5.2 - June 2025]: The `mainwp_legacy_auth_method` function - update extensions to use the new authentication method
- 🟠 **Changed** [v5.1 - April 2025]: Updated `mainwp_user_login()` implementation to include additional validation checks

## 🔌 API Changes
- 🟠 **Changed** [v5.1 - April 2025]: Site endpoint now requires authentication token in headers - action required: update API calls
- 🟢 **Added** [v5.1 - April 2025]: New parameter `include_metadata` to the GET /sites endpoint

## ⚡ Performance Optimizations
- ⚡ **Performance** [v5.0.4 - March 20, 2025]: Reduced database queries in the main site loop
- ⚡ **Performance** [v5.0.4 - March 20, 2025]: Implemented caching for frequently accessed configuration

## ⚠️ Breaking Changes
- 🔴 **Removed** [v5.1 - April 2025]: Legacy API endpoint `/v1/sites` has been completely removed - action required: migrate to v2 API
- 🟠 **Changed** [v5.1 - April 2025]: Order of execution in the `mainwp_init` hook - action required: review extension hook priorities

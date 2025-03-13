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

---

# March 13, 2025 (Example changes) 

## 🔧 Core Changes
- 🟢 **Added**: New filter hook `mainwp_pre_process_site_data` that runs before site data processing
- ⚫ **Deprecated**: The `mainwp_legacy_auth_method` function will be removed in v5.2
- 🟠 **Changed**: Updated `mainwp_user_login()` implementation to include additional validation checks

## 🔌 API Changes
- 🟠 **Changed**: Site endpoint now requires authentication token in headers
- 🟢 **Added**: New parameter `include_metadata` to the GET /sites endpoint

## ⚡ Performance Optimizations
- ⚡ **Performance**: Reduced database queries in the main site loop
- ⚡ **Performance**: Implemented caching for frequently accessed configuration

## ⚠️ Breaking Changes
- 🔴 **Removed**: Legacy API endpoint `/v1/sites` has been completely removed
- 🟠 **Changed**: Order of execution in the `mainwp_init` hook - third-party developers should review their hook priorities

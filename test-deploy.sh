#!/bin/bash
# test-deploy.sh - Script to test GitHub Pages deployment process locally

# --- Configuration ---
# Define directories to include in deployment (relative to project root)
DEPLOY_INCLUDE=(
  "index.html"
  "build"
  "guides"
  "mainwp-hooks"
  "source-code"
  "LICENSE"
  "README.md"
  # Add any other files/directories you want to deploy
)

# Define directories explicitly excluded from deployment
DEPLOY_EXCLUDE=(
  "mainwp-hooks-old"
  "mainwp-hooks-temp"
  "hooks-generator"
  "phpdoc"
  "sources"
  "memory-bank"
  ".git"
  ".github"
  ".clineignore"
  "clinerules.md"
  # Add any other files/directories you want to exclude
)

# --- Setup ---
set -e  # Exit immediately if a command fails
ROOT_DIR="$(pwd)"
DEPLOY_DIR="$ROOT_DIR/deploy-test"
LOG_FILE="$ROOT_DIR/deploy-test.log"

# Clear log file
> "$LOG_FILE"

# Helper function for logging
log() {
  echo "$1"
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

log "=== MainWP.dev Documentation Deployment Test ==="
log "Root directory: $ROOT_DIR"

# --- Generate Documentation (optional) ---
if [ "$1" == "--generate" ]; then
  log "Generating hooks documentation..."
  if [ -d "$ROOT_DIR/hooks-generator" ]; then
    (cd "$ROOT_DIR/hooks-generator" && ./generate-categorized-hooks.sh) || {
      log "ERROR: Failed to generate hooks documentation"
      exit 1
    }
    log "Hooks documentation generated successfully"
  else
    log "WARNING: hooks-generator directory not found, skipping documentation generation"
  fi
else
  log "Skipping documentation generation (use --generate to include this step)"
fi

# --- Prepare Deployment Directory ---
log "Preparing clean deployment directory..."
if [ -d "$DEPLOY_DIR" ]; then
  rm -rf "$DEPLOY_DIR"
fi
mkdir -p "$DEPLOY_DIR"

# --- Copy Files for Deployment ---
log "Copying files for deployment..."

# Process each include item
for item in "${DEPLOY_INCLUDE[@]}"; do
  if [ -e "$ROOT_DIR/$item" ]; then
    log "Including: $item"
    if [ -d "$ROOT_DIR/$item" ]; then
      mkdir -p "$DEPLOY_DIR/$item"
      cp -R "$ROOT_DIR/$item"/* "$DEPLOY_DIR/$item/" 2>/dev/null || true
    else
      cp "$ROOT_DIR/$item" "$DEPLOY_DIR/" 2>/dev/null || {
        log "WARNING: Failed to copy $item"
      }
    fi
  else
    log "WARNING: Included item not found: $item"
  fi
done

# --- Verify Deployment ---
log "Verifying deployment..."

# Check for required files
REQUIRED_FILES=("index.html" "guides/index.md" "mainwp-hooks/index.md")
missing=0

for file in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$DEPLOY_DIR/$file" ]; then
    log "ERROR: Required file missing from deployment: $file"
    missing=$((missing + 1))
  fi
done

# Verify excluded directories aren't present
for excluded in "${DEPLOY_EXCLUDE[@]}"; do
  if [ -e "$DEPLOY_DIR/$excluded" ]; then
    log "ERROR: Excluded item found in deployment: $excluded"
    missing=$((missing + 1))
  fi
done

# --- Summary ---
total_files=$(find "$DEPLOY_DIR" -type f | wc -l)
total_dirs=$(find "$DEPLOY_DIR" -type d | wc -l)

log "=== Deployment Summary ==="
log "Total files: $total_files"
log "Total directories: $total_dirs"
log "Excluded directories:"
for excluded in "${DEPLOY_EXCLUDE[@]}"; do
  if [ -e "$ROOT_DIR/$excluded" ]; then
    count=$(find "$ROOT_DIR/$excluded" -type f 2>/dev/null | wc -l)
    log "  - $excluded: $count files (not deployed)"
  fi
done

if [ $missing -eq 0 ]; then
  log "✅ Verification PASSED: All required files present and excluded items not found"
else
  log "❌ Verification FAILED: $missing issues found"
fi

log "Deployment test complete! Review the contents of the '$DEPLOY_DIR' directory"
log "To test the site locally:"
log "  cd $DEPLOY_DIR && python3 -m http.server 8000"
log "Then visit http://localhost:8000 in your browser"
log "A log file has been saved to: $LOG_FILE"

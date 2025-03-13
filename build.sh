#!/bin/bash

# Directory setup - all relative to the script location
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CODE_REF_DIR="$SCRIPT_DIR/tools/code-reference"
MAINWP_DIR="$SCRIPT_DIR/source/mainwp"
MAINWP_CHILD_DIR="$SCRIPT_DIR/source/mainwp-child"
OUTPUT_DIR="$SCRIPT_DIR/code-docs"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to build documentation for a repo
build_docs() {
  REPO_NAME=$1
  REPO_PATH=$2
  IGNORE_PATTERNS=$3
  
  echo "Building documentation for $REPO_NAME..."
  
  # Navigate to code reference tool
  cd "$CODE_REF_DIR"
  
  # Update phpdoc.xml to point to the correct repository
  sed -i '' "s|<directory>.*</directory>|<directory>$REPO_PATH</directory>|" phpdoc.xml
  
  # Update ignore patterns if provided
  if [ ! -z "$IGNORE_PATTERNS" ]; then
    # Remove existing ignore-patterns section
    sed -i '' '/<ignore-patterns>/,/<\/ignore-patterns>/d' phpdoc.xml || true
    
    # Add new ignore-patterns section before the closing </phpdocumentor> tag
    sed -i '' "s|</phpdocumentor>|<ignore-patterns>\n$IGNORE_PATTERNS\n</ignore-patterns>\n</phpdocumentor>|" phpdoc.xml
  fi
  
  # Build the documentation - using a placeholder version since we're not downloading
  ./deploy.sh --source-version "1.0.0" --github-repo "mainwp/$REPO_NAME" --default-package "MainWP" --build-only --no-download
  
  # Copy the built files to the output directory
  if [ -d "$CODE_REF_DIR/build/api" ]; then
    echo "Copying files to $OUTPUT_DIR/$REPO_NAME"
    mkdir -p "$OUTPUT_DIR/$REPO_NAME"
    cp -R "$CODE_REF_DIR/build/api/"* "$OUTPUT_DIR/$REPO_NAME/"
  else
    echo "Error: Build directory not found"
    exit 1
  fi
}

# Define ignore patterns for each repository
MAINWP_IGNORES="<ignore>*/tests/*</ignore>\n<ignore>*/node_modules/*</ignore>\n<ignore>*/vendor/*</ignore>"
MAINWP_CHILD_IGNORES="<ignore>*/tests/*</ignore>\n<ignore>*/node_modules/*</ignore>\n<ignore>*/vendor/*</ignore>\n<ignore>*/assets/*</ignore>\n<ignore>*/libs/external/*</ignore>"

# Update repositories to the latest version
echo "Updating MainWP repositories..."
cd "$MAINWP_DIR" && git pull origin master
cd "$MAINWP_CHILD_DIR" && git pull origin master

# Build documentation for MainWP Dashboard
build_docs "mainwp" "$MAINWP_DIR" "$MAINWP_IGNORES"

# Build documentation for MainWP Child
build_docs "mainwp-child" "$MAINWP_CHILD_DIR" "$MAINWP_CHILD_IGNORES"

# Commit changes to mainwp.dev
cd "$SCRIPT_DIR"
git add .
git commit -m "Update code reference documentation"
git push origin main

echo "Documentation build complete!"
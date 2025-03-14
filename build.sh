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
  DEFAULT_PACKAGE=$4
  
  echo "Building documentation for $REPO_NAME..."
  echo "Source directory: $REPO_PATH"
  
  # Navigate to code reference tool
  cd "$CODE_REF_DIR"
  
  # Create a temporary phpdoc config file based on phpdoc-final.xml
  cp "$CODE_REF_DIR/phpdoc-final.xml" "$CODE_REF_DIR/phpdoc-temp.xml"
  
  # Update the source path in the config
  sed -i '' "s|<source dsn=\"file:///app/source/.*\">|<source dsn=\"file:///app/source/$REPO_NAME\">|" "$CODE_REF_DIR/phpdoc-temp.xml"
  
  # Update the title
  sed -i '' "s|<title>.*</title>|<title>MainWP $REPO_NAME Code Reference</title>|" "$CODE_REF_DIR/phpdoc-temp.xml"
  
  # Update the default package name
  sed -i '' "s|<default-package-name>.*</default-package-name>|<default-package-name>$DEFAULT_PACKAGE</default-package-name>|" "$CODE_REF_DIR/phpdoc-temp.xml"
  
  echo "Updated phpdoc-temp.xml for $REPO_NAME:"
  cat "$CODE_REF_DIR/phpdoc-temp.xml"
  
  # Run PHPDocumentor in Docker with PHP 8.1
  echo "Running PHPDocumentor in Docker with PHP 8.1..."
  docker run --rm -v "$SCRIPT_DIR:/app" -w "/app/tools/code-reference" php:8.1-cli php vendor/bin/phpdoc run --config=phpdoc-temp.xml -v
  
  # Copy the built files to the output directory
  if [ -d "$CODE_REF_DIR/build/api" ]; then
    echo "Copying files to $OUTPUT_DIR/$REPO_NAME"
    mkdir -p "$OUTPUT_DIR/$REPO_NAME"
    cp -R "$CODE_REF_DIR/build/api/"* "$OUTPUT_DIR/$REPO_NAME/"
  else
    echo "Error: Build directory not found"
    exit 1
  fi
  
  # Clean up
  rm "$CODE_REF_DIR/phpdoc-temp.xml"
}

# Build documentation for MainWP Dashboard
build_docs "mainwp" "$MAINWP_DIR" "" "MainWP"

# Build documentation for MainWP Child
build_docs "mainwp-child" "$MAINWP_CHILD_DIR" "" "MainWP"

# Commit changes to mainwp.dev
cd "$SCRIPT_DIR"
git add .
git commit -m "Update code reference documentation"
git push origin main

echo "Documentation build complete!"
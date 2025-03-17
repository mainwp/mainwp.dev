#!/bin/bash

# Script to generate and categorize hooks documentation for MainWP Dashboard and Child repositories

# Set directories
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
TEMP_DIR="$ROOT_DIR/mainwp-hooks-temp"
OUTPUT_DIR="$ROOT_DIR/mainwp-hooks-categorized"

# Create temporary directory for uncategorized hooks
mkdir -p "$TEMP_DIR/dashboard" "$TEMP_DIR/child"

# Step 1: Generate hooks documentation
echo "Step 1: Generating hooks documentation..."
cd "$SCRIPT_DIR"

# Run the hooks generation script
./generate-hooks.sh

# Step 2: Categorize hooks
echo "Step 2: Categorizing hooks documentation..."

# Run the categorization script
python3 categorize-hooks.py "$ROOT_DIR/mainwp-hooks" "$OUTPUT_DIR"

# Step 3: Clean up
echo "Step 3: Cleaning up..."

# Copy the categorized hooks to the main hooks directory
echo "Replacing mainwp-hooks with categorized version..."
rm -rf "$ROOT_DIR/mainwp-hooks-old"
mv "$ROOT_DIR/mainwp-hooks" "$ROOT_DIR/mainwp-hooks-old"
mv "$OUTPUT_DIR" "$ROOT_DIR/mainwp-hooks"

echo "Hooks documentation generation and categorization completed!"
echo "The hooks documentation is available in the mainwp-hooks directory."

#!/bin/bash

# Directory setup - all relative to the script location
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CODE_REF_DIR="$SCRIPT_DIR/tools/code-reference"
MAINWP_CHILD_DIR="$SCRIPT_DIR/source/mainwp-child"

# If source directory doesn't exist, look for it in the parent directory
if [ ! -d "$MAINWP_CHILD_DIR" ]; then
  MAINWP_CHILD_DIR="/Users/denni1/Documents/GitHub/mainwp/mainwp-child"
  echo "Using alternative mainwp-child path: $MAINWP_CHILD_DIR"
fi

echo "Script directory: $SCRIPT_DIR"
echo "Code reference directory: $CODE_REF_DIR"
echo "MainWP Child directory: $MAINWP_CHILD_DIR"

# Navigate to code reference tool
cd "$CODE_REF_DIR"

# Create a backup of the original phpdoc.xml
cp phpdoc.xml phpdoc.xml.backup

# Update phpdoc.xml to point to the correct repository
sed -i '' "s|<directory>.*</directory>|<directory>$MAINWP_CHILD_DIR</directory>|" phpdoc.xml

echo "Updated phpdoc.xml:"
cat phpdoc.xml

echo "Running PHPDocumentor in Docker with PHP 8.1..."
docker run --rm -v /Users/denni1/Documents/GitHub:/Users/denni1/Documents/GitHub -w "$CODE_REF_DIR" php:8.1-cli php vendor/bin/phpdoc --config=phpdoc.xml

echo "PHPDocumentor complete!"
echo "Check build/api directory for output without affecting your code-docs folder."

# Restore the original phpdoc.xml
mv phpdoc.xml.backup phpdoc.xml

echo "Restored original phpdoc.xml configuration."
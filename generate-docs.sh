#!/bin/bash

# Script to generate documentation for MainWP Dashboard and Child repositories

# Create build directory for cache if it doesn't exist
mkdir -p build/cache/dashboard build/cache/child

# Check if source repositories exist
if [ ! -d "sources/mainwp-dashboard" ]; then
  echo "Error: MainWP Dashboard repository not found in sources/mainwp-dashboard"
  echo "Please clone the repository first:"
  echo "git clone https://github.com/mainwp/mainwp.git sources/mainwp-dashboard"
  exit 1
fi

if [ ! -d "sources/mainwp-child" ]; then
  echo "Error: MainWP Child repository not found in sources/mainwp-child"
  echo "Please clone the repository first:"
  echo "git clone https://github.com/mainwp/mainwp-child.git sources/mainwp-child"
  exit 1
fi

# Generate documentation for Dashboard
echo "Generating documentation for MainWP Dashboard..."
vendor/bin/phpdoc -c phpdoc/dashboard.xml

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Error: Failed to generate documentation for MainWP Dashboard"
  exit 1
fi

# Generate documentation for Child
echo "Generating documentation for MainWP Child..."
vendor/bin/phpdoc -c phpdoc/child.xml

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Error: Failed to generate documentation for MainWP Child"
  exit 1
fi

echo "Documentation generation completed successfully!"
echo "Dashboard documentation: source-code/dashboard/index.html"
echo "Child documentation: source-code/child/index.html"

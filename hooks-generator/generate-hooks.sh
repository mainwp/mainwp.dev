#!/bin/bash

# Script to generate hooks documentation for MainWP Dashboard and Child repositories

# Check if source repositories exist relative to the project root
if [ ! -d "./sources/mainwp-dashboard" ]; then
  echo "Error: MainWP Dashboard repository not found in ./sources/mainwp-dashboard"
  echo "Please clone the repository first:"
  echo "git clone https://github.com/mainwp/mainwp.git ./sources/mainwp-dashboard"
  exit 1
fi

if [ ! -d "./sources/mainwp-child" ]; then
  echo "Error: MainWP Child repository not found in ./sources/mainwp-child"
  echo "Please clone the repository first:"
  echo "git clone https://github.com/mainwp/mainwp-child.git ./sources/mainwp-child"
  exit 1
fi

# Create directories relative to the project root (where this script is likely called from)
mkdir -p ./mainwp-hooks/dashboard
mkdir -p ./mainwp-hooks/child

# Generate Dashboard hooks documentation
echo "Generating documentation for MainWP Dashboard actions..."
# Use paths relative to project root
php -d memory_limit=512M ./hooks-generator/vendor/bin/wp-documentor parse ./sources/mainwp-dashboard --format=markdown --output=./mainwp-hooks-temp/dashboard/actions.md --type=actions --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Dashboard actions"
else
  echo "Successfully generated documentation for MainWP Dashboard actions"
fi

echo "Generating documentation for MainWP Dashboard filters..."
# Use paths relative to project root
php -d memory_limit=512M ./hooks-generator/vendor/bin/wp-documentor parse ./sources/mainwp-dashboard --format=markdown --output=./mainwp-hooks-temp/dashboard/filters.md --type=filters --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Dashboard filters"
else
  echo "Successfully generated documentation for MainWP Dashboard filters"
fi

# Generate Child hooks documentation
echo "Generating documentation for MainWP Child actions..."
# Use paths relative to project root
php -d memory_limit=512M ./hooks-generator/vendor/bin/wp-documentor parse ./sources/mainwp-child --format=markdown --output=./mainwp-hooks-temp/child/actions.md --type=actions --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Child actions"
else
  echo "Successfully generated documentation for MainWP Child actions"
fi

echo "Generating documentation for MainWP Child filters..."
# Use paths relative to project root
php -d memory_limit=512M ./hooks-generator/vendor/bin/wp-documentor parse ./sources/mainwp-child --format=markdown --output=./mainwp-hooks-temp/child/filters.md --type=filters --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Child filters"
else
  echo "Successfully generated documentation for MainWP Child filters"
fi

echo "Hooks documentation generation completed!"
echo "Raw Dashboard actions: ./mainwp-hooks-temp/dashboard/actions.md"
echo "Raw Dashboard filters: ./mainwp-hooks-temp/dashboard/filters.md"
echo "Raw Child actions: ./mainwp-hooks-temp/child/actions.md"
echo "Raw Child filters: ./mainwp-hooks-temp/child/filters.md"

# Add step to categorize and structure the documentation
echo ""
echo "Categorizing hooks and generating final structure..."
python3 ./hooks-generator/categorize-hooks.py ./mainwp-hooks-temp ./mainwp-hooks

if [ $? -ne 0 ]; then
  echo "Error: Failed to categorize hooks."
  exit 1
else
  echo "Successfully categorized hooks into ./mainwp-hooks/"
fi

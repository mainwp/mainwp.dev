#!/bin/bash

# Script to generate hooks documentation for MainWP Dashboard and Child repositories

# Check if source repositories exist
if [ ! -d "../sources/mainwp-dashboard" ]; then
  echo "Error: MainWP Dashboard repository not found in ../sources/mainwp-dashboard"
  echo "Please clone the repository first:"
  echo "git clone https://github.com/mainwp/mainwp.git ../sources/mainwp-dashboard"
  exit 1
fi

if [ ! -d "../sources/mainwp-child" ]; then
  echo "Error: MainWP Child repository not found in ../sources/mainwp-child"
  echo "Please clone the repository first:"
  echo "git clone https://github.com/mainwp/mainwp-child.git ../sources/mainwp-child"
  exit 1
fi

# Create directories if they don't exist
mkdir -p ../mainwp-hooks/dashboard
mkdir -p ../mainwp-hooks/child

# Generate Dashboard hooks documentation
echo "Generating documentation for MainWP Dashboard actions..."
php -d memory_limit=512M vendor/bin/wp-documentor parse ../sources/mainwp-dashboard --format=markdown --output=../mainwp-hooks/dashboard/actions.md --type=actions --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Dashboard actions"
else
  echo "Successfully generated documentation for MainWP Dashboard actions"
fi

echo "Generating documentation for MainWP Dashboard filters..."
php -d memory_limit=512M vendor/bin/wp-documentor parse ../sources/mainwp-dashboard --format=markdown --output=../mainwp-hooks/dashboard/filters.md --type=filters --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Dashboard filters"
else
  echo "Successfully generated documentation for MainWP Dashboard filters"
fi

# Generate Child hooks documentation
echo "Generating documentation for MainWP Child actions..."
php -d memory_limit=512M vendor/bin/wp-documentor parse ../sources/mainwp-child --format=markdown --output=../mainwp-hooks/child/actions.md --type=actions --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Child actions"
else
  echo "Successfully generated documentation for MainWP Child actions"
fi

echo "Generating documentation for MainWP Child filters..."
php -d memory_limit=512M vendor/bin/wp-documentor parse ../sources/mainwp-child --format=markdown --output=../mainwp-hooks/child/filters.md --type=filters --exclude=vendor --exclude=libs

# Check if documentation generation was successful
if [ $? -ne 0 ]; then
  echo "Warning: Failed to generate documentation for MainWP Child filters"
else
  echo "Successfully generated documentation for MainWP Child filters"
fi

echo "Hooks documentation generation completed!"
echo "Dashboard actions: ../mainwp-hooks/dashboard/actions.md"
echo "Dashboard filters: ../mainwp-hooks/dashboard/filters.md"
echo "Child actions: ../mainwp-hooks/child/actions.md"
echo "Child filters: ../mainwp-hooks/child/filters.md"

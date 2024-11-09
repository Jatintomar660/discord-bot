#!/bin/bash

TARGET_DIR=".setup_files"
REPO_URL="https://github.com/alfaarghya/alfa-leetcode-api.git"

echo "Removing directory $TARGET_DIR..."
rm -f $TARGET_DIR
echo "Creating directory $TARGET_DIR..."
mkdir "$TARGET_DIR"

echo "Cloning the repository into $TARGET_DIR..."
git clone "$REPO_URL" "$TARGET_DIR"

if [ $? -eq 0 ]; then
  echo "Repository cloned successfully."
else
  echo "Failed to clone the repository. Exiting script."
  exit 1
fi

echo "Setup completed successfully."

#!/bin/bash

# Check if the correct number of arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <commit_message> <file_name_or_dot>"
    exit 1
fi

# Commit message and file name or dot provided as arguments
commit_message="$1"
file_name="$2"

# Check if the provided file exists or if dot is provided
if [ "$file_name" != "." ] && [ ! -e "$file_name" ]; then
    echo "File '$file_name' not found."
    exit 1
fi

# Add changes to the staging area
git add "$file_name"

# Commit the changes with the provided message
git commit -m "$commit_message"

# Push changes to GitHub
git push origin main  # Change 'main' to your branch name if different

# Check if the push was successful
if [ $? -eq 0 ]; then
    echo -e "\e[32mPush successful!\e[0m"
else
    echo -e "\e[31mFailed to push changes. Please check your network connection and try again.\e[0m"
fi

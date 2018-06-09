#!/bin/bash

# STEP 1: Initiate git project - first time
git init

# STEP 2: Add local project to git. This will also add new file to local repo
git add .

# STEP 3: Commit adds to local repo
git commit -m "message"

# STEP 4: Set up new remote repository - First time. This is my github URL
git remote add origin https://github.com/arnabkc/simple-spam-filter.git

# STEP 5: Push code to remote repository
git push -u origin master

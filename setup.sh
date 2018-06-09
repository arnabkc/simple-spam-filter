#!/bin/bash
PROJECT_ROOT=.
APP_DIR=spamfilter

cd $PROJECT_ROOT
mkdir $APP_DIR
touch requirements.txt

cd $APP_DIR
touch __init__.py
mkdir main
mkdir test

touch ./test/__init__.py

cd main
mkdir controller
mkdir model
mkdir service

touch ./controller/__init__.py
touch ./model/__init__.py
touch ./service/__init__.py




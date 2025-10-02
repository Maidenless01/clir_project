#!/usr/bin/env bash
# build.sh - Render build script for ITUS Semantic Document Portal

set -o errexit  # exit on error

echo "Starting build process..."

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Build completed successfully!"
#!/usr/bin/env python3
"""
Simple test script to verify file structure in GitHub Actions
"""
import os

print("Current working directory:", os.getcwd())
print("Contents of current directory:")
for item in os.listdir('.'):
    print(f"  {item}")

print("\nContents of tools directory:")
if os.path.exists('tools'):
    for item in os.listdir('tools'):
        print(f"  {item}")
else:
    print("  tools directory not found!")

print("\nLooking for harvest_arxiv.py:")
for root, dirs, files in os.walk('.'):
    for file in files:
        if 'harvest_arxiv' in file:
            print(f"  Found: {os.path.join(root, file)}")

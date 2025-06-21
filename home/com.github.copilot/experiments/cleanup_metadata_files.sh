#!/bin/bash
# Clean up all intermediate .json and .yaml metadata files in /inbox and subfolders
find /workspaces/21JUN25-research/inbox -type f \( -name '*.metadata.json' -o -name '*.metadata.yaml' \) -delete

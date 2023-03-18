#!/usr/bin/env python

import os
import sys
from tracemalloc import start

from describe_dir import get_directory_tree


def extract_project_architecture(filepath):
    """
    Extracts the text between the "## Project architecture" and the triple backticks.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
        start_index = -1
        end_index = -1
        for i, line in enumerate(lines):
            if line.strip() == "```":
                start_index = i + 1
                break            
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "```":
                end_index = i
                break
        if start_index != -1 and end_index != -1:
            return ''.join(lines[start_index:end_index]).strip()
        else:
            return ""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python update_readme.py <path>")
        sys.exit(1)
        
    startpath = os.path.abspath(sys.argv[1])
    #new_version = get_directory_tree(startpath, is_last=True)
    
    old_version = extract_project_architecture(os.path.join(startpath, 'readme.md'))

    print(old_version)
#!/usr/bin/env python

import os
import sys

def print_directory_tree(startpath, prefix="", is_last=False):
    """
    Recursively prints the directory tree starting from the given startpath.
    """
    if os.path.isdir(startpath):
        dirname = os.path.basename(startpath)
        if prefix == "":
            print(dirname + '/')
        else:
            print(prefix + ("└── " if is_last else "├── ") + dirname + '/')
        prefix += "    " if is_last else "│   "
        contents = os.listdir(startpath)
        for i, file in enumerate(contents):
            is_last = i == len(contents) - 1
            if file != '__pycache__':
                print_directory_tree(os.path.join(startpath, file), prefix, is_last)
    else:
        print(prefix + ("└── " if is_last else "├── ") + os.path.basename(startpath))
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python describe_dir.py <path>")
        sys.exit(1)

    startpath = os.path.abspath(sys.argv[1])
    print_directory_tree(startpath, is_last=True)

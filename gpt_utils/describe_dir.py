#!/usr/bin/env python

import os
import sys
import fnmatch

def get_directory_tree(startpath, prefix="", is_last=False, gitignore_patterns=None):
    """
    Recursively returns the directory tree starting from the given startpath, ignoring files and directories that would be ignored by gitignore, as well as those starting with a dot.
    """
    if gitignore_patterns is None:
        gitignore_patterns = []

    tree = ""
    if os.path.isdir(startpath):
        dirname = os.path.basename(startpath)
        if prefix == "":
            tree += dirname + "/\n"
        else:
            tree += prefix + ("└── " if is_last else "├── ") + dirname + "/\n"
        prefix += "    " if is_last else "│   "

        # get the gitignore patterns for the current directory
        gitignore_file = os.path.join(startpath, '.gitignore')
        if os.path.isfile(gitignore_file):
            with open(gitignore_file, 'r') as f:
                for line in f:
                    pattern = line.strip()
                    if pattern and not pattern.startswith('#'):
                        gitignore_patterns.append(pattern)

        contents = os.listdir(startpath)
        for i, file in enumerate(contents):
            is_last = i == len(contents) - 1
            file_path = os.path.join(startpath, file)

            # check if the file should be ignored
            should_ignore = False
            if file.startswith('.') or any(fnmatch.fnmatch(file, p) for p in gitignore_patterns) or file == '__pycache__':
                should_ignore = True
            elif os.path.isdir(file_path):
                should_ignore = False
            elif os.path.isfile(gitignore_file):
                should_ignore = any(fnmatch.fnmatch(file_path, os.path.join(startpath, p)) for p in gitignore_patterns)

            if should_ignore:
                continue

            if os.path.isdir(file_path):
                tree += get_directory_tree(file_path, prefix, is_last, gitignore_patterns)
            else:
                tree += prefix + ("└── " if is_last else "├── ") + file + "\n"

    return tree

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python describe_dir.py <path>")
        sys.exit(1)

    startpath = os.path.abspath(sys.argv[1])
    print(get_directory_tree(startpath, is_last=True))

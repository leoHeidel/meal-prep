#!/usr/bin/env python

import os
import sys
import fnmatch


IGNORED = [
    '__init__.py',
    '__pycache__',
]
SPECIFIC_DIRECTORIES = [
    'migrations',
    'public',
    ]


def should_ignore(file, startpath, gitignore_patterns, gitignore_file):
    if file.startswith('.'):
        return True
    if any(fnmatch.fnmatch(file, p) for p in gitignore_patterns) or file in IGNORED:
        return True
    file_path = os.path.join(startpath, file)
    if os.path.isfile(gitignore_file):
        return any(fnmatch.fnmatch(file_path, os.path.join(startpath, p)) for p in gitignore_patterns)
    return False

def build_tree_string(contents, startpath, prefix, is_last, gitignore_patterns):
    tree = ""
    for i, file in enumerate(contents):
        is_last = i == len(contents) - 1
        file_path = os.path.join(startpath, file)

        if os.path.isdir(file_path):
            if file in SPECIFIC_DIRECTORIES:
                tree += prefix + ("└── " if is_last else "├── ") + file + "/...\n"
            else:
                tree += get_directory_tree(file_path, prefix, is_last, gitignore_patterns)
        else:
            tree += prefix + ("└── " if is_last else "├── ") + file + "\n"
    return tree

def get_directory_tree(startpath, prefix="", is_last=False, gitignore_patterns=None):
    if gitignore_patterns is None:
        gitignore_patterns = []

    tree = ""
    if os.path.isdir(startpath):
        dirname = os.path.basename(startpath)
        tree += prefix + ("└── " if is_last else "├── ") + dirname + "/\n" if prefix else dirname + "/\n"
        prefix += "    " if is_last else "│   "

        gitignore_file = os.path.join(startpath, '.gitignore')
        if os.path.isfile(gitignore_file):
            with open(gitignore_file, 'r') as f:
                gitignore_patterns += [line.strip() for line in f if line.strip() and not line.startswith('#')]

        contents = os.listdir(startpath)
        contents = [file for file in contents if not should_ignore(file, startpath, gitignore_patterns, gitignore_file)]

        tree += build_tree_string(contents, startpath, prefix, is_last, gitignore_patterns)

    return tree



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python describe_dir.py <path>")
        sys.exit(1)

    startpath = os.path.abspath(sys.argv[1])
    print(get_directory_tree(startpath, is_last=True))

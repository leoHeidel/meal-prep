#!/usr/bin/env python

import os
import sys

import private
import openai

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
        if start_index == -1 or end_index == -1:
            assert False
        return (
                ''.join(lines[start_index:end_index]).strip(),
                ''.join(lines[start_index:end_index]).strip(),
                ''.join(lines[start_index:end_index]).strip(),
            )

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python update_readme.py <path>")
        sys.exit(1)

    startpath = os.path.abspath(sys.argv[1])
    new_version = get_directory_tree(startpath, is_last=True)

    readme_path = os.path.join(startpath, 'readme.md')
    readme_start, old_version, readme_end = extract_project_architecture(readme_path)

    prompt = \
    f"""I have been making change to the architecture of my meal planner app project. Here is the old architecture:
    ```
    {old_version}
    ```
    Here is the new architecure:
    ```
    {new_version}
    ```
    Update the comment at the end of each line for the new architecture, only anwser with that."""
    print(prompt)
    # gpt_querry = {
    #     "model": "gpt-3.5-turbo",
    #     "messages": [{"role": "user", "content": prompt}]
    # }
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages= [{"role": "user", "content": prompt}]
    # )
    # print(response['choices'][0]['message'])
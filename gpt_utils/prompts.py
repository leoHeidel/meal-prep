import re

import yaml
from . import private
import openai

def to_yaml_markdown(data):
    yaml_data = yaml.dump(data, default_flow_style=False, sort_keys=False)
    return f'```yaml\n{yaml_data}```'

def extract_yaml_snippet(text: str) -> str:
    pattern = re.compile(r'(?s)(?<=```yaml).*?(?=```)')
    matches = pattern.findall(text)

    if len(matches) == 0:
        raise ValueError("YAML code snippet not found in the text")
    elif len(matches) > 1:
        raise ValueError("More than one YAML code snippet found in the text")
    else:
        return yaml.safe_load(matches[0].strip())


def make_messages (user_message):
    return [
        {
            "role": "system",
            "content": "You are CookGPT a helpful assistant, helping creating and formatting recipe data."
        },
        {
            "role": "user",
            "content": user_message
        },
    ]


def recipe_prompt(recipe_ideas, recipe_format):
    prompt = f'''
    I am working on a recipe app project. Here is the format of a recipe:
    {to_yaml_markdown(recipe_format)}
    Send me a recipe using the following ideas, and respecting the format:
    recipe ideas: {recipe_ideas}
    '''

    return make_messages(prompt)

def use_gpt(messages):
    return openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens= 1000,
    messages=messages
    )
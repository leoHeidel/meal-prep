import re

import yaml

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


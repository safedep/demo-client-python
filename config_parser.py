import yaml

def load_config():
    """
    Uses an old 'PyYAML==3.13' version to parse a YAML configuration string.
    """
    yaml_data = """
    server: "vulnerable_app"
    version: 1
    features:
      - name: "Data Fetching"
      - name: "Template Rendering"
    """
    config = yaml.safe_load(yaml_data)
    return config



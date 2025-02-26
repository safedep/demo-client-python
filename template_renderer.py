from jinja2 import Template

def render_report(data, config):
    """
    Uses an outdated 'Jinja2==2.10' to render a dynamic report with data.
    """
    template_str = """
    Report for: {{ config.server }} (version: {{ config.version }})
    Features:
    {% for feature in config.features %}
      - {{ feature.name }}
    {% endfor %}
    
    Data Fetched:
    Title: {{ data.title }}
    Body: {{ data.body }}
    """
    template = Template(template_str)
    report = template.render(config=config, data=data)
    return report


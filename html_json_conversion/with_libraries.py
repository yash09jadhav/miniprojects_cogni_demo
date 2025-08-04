from pathlib import Path
import json
from jinja2 import Template

def convert_txt_to_html_json(file_path):
    file_path = Path(file_path)
    lines = file_path.read_text(encoding='utf-8').splitlines()

    title, author = "", ""
    paragraphs = []
    for line in lines:
        line = line.strip()
        if line.lower().startswith("title:"):
            title = line[6:].strip()
        elif line.lower().startswith("author:"):
            author = line[7:].strip()
        elif line:
            paragraphs.append(line)

    # html template for Jinja2
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{{ title or "Untitled" }}</title>
    </head>
    <body>
        {% if title %}<h1>{{ title }}</h1>{% endif %}
        {% if author %}<h3>By {{ author }}</h3>{% endif %}
        {% for para in paragraphs %}
            <p>{{ para }}</p>
        {% endfor %}
    </body>
    </html>
    """

    template = Template(html_template)
    rendered_html = template.render(title=title, author=author, paragraphs=paragraphs)

    html_path = file_path.with_suffix('.html')
    html_path.write_text(rendered_html, encoding='utf-8')

    json_data = {
        "title": title,
        "author": author,
        "paragraphs": paragraphs
    }
    json_path = file_path.with_suffix('.json')
    json_path.write_text(json.dumps(json_data, indent=4), encoding='utf-8')

    print('conversion done finally')

convert_txt_to_html_json("input.txt")

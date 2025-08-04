import os
import json

def convert_txt_to_html_and_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

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

    # o/p
    folder = os.path.dirname(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    html_content = "<html><head><title>{}</title></head><body>\n".format(title or "Untitled")
    html_content += f"<h1>{title}</h1>\n" if title else ""
    html_content += f"<h3>By {author}</h3>\n" if author else ""
    for para in paragraphs:
        html_content += f"<p>{para}</p>\n"
    html_content += "</body></html>"

    with open(os.path.join(folder, base_name + ".html"), 'w', encoding='utf-8') as f:
        f.write(html_content)

    json_data = {
        "title": title,
        "author": author,
        "paragraphs": paragraphs
    }

    with open(os.path.join(folder, base_name + ".json"), 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4)

    print("conversion done finally")

convert_txt_to_html_and_json("input.txt")

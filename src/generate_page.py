from block_markdown import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_content = file.read()
    
    with open(template_path) as file:
        template = file.read()
    
    title = extract_title(from_content)
    node = markdown_to_html_node(from_content)
    html = node.to_html()
    new_page = template.replace("{{ Title }}", title) \
                       .replace("{{ Content }}", html)
    
    with open(dest_path, "w+") as file:
        file.write(new_page)


def generate_content(src_path):
    for item in os.listdir(src_path):
        item_path = os.path.join(src_path, item)
        if os.path.isfile(item_path):
            dest_path = item_path.replace("content", "public", 1)\
                                 .replace(".md", ".html", 1)
            generate_page(item_path, "template.html", dest_path)
        else:
            os.mkdir(item_path.replace("content", "public", 1))
            generate_content(item_path) 
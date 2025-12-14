from textnode import TextNode, TextType
from copy_function import static_to_public
from generate_page import generate_page, generate_content
import os

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

    static_to_public()


    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_content("content")

if __name__ == "__main__":
    main()
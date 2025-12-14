from textnode import TextNode, TextType
from copy_function import static_to_public
from generate_page import generate_page, generate_content
import os
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    static_to_public()
    generate_content("content", basepath)

if __name__ == "__main__":
    main()
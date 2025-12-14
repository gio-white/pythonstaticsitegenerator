import re

def extract_title(markdown):
    h1_block = []
    for block in markdown.split("\n\n"):
        if re.match(r"^# ", block):
            h1_block.append(block)
    if not h1_block:
        raise ValueError("The markdown file doesn't have a title")

    title = h1_block[0].strip().replace("#", "")
    return title


print(extract_title("# Hello"))
        
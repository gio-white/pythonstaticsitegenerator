from typing import List
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes:List[TextNode], delimiter, text_type:TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_shards = node.text.split(delimiter)
        if len(node_shards) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax")
        split_nodes = []
        for idx, shard in enumerate(node_shards):
            if shard == "":
                continue
            if idx % 2 == 0:
                split_nodes.append(TextNode(shard, TextType.TEXT))
            if idx % 2 != 0:
                split_nodes.append(TextNode(shard, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

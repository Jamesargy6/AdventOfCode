from dataclasses import dataclass
from collections import namedtuple
from typing import List


Header = namedtuple("Header", "num_child_nodes num_metadata_entries")


@dataclass
class Node:
    def __init__(self, header):
        self.header: Header = header
        self.children: List[Node] = []
        self.metadata: List[int] = []

    def to_string(self):
        print(self.header)


def build_tree(inputs: List[int]) -> (Node, List[int]):
    root_header = Header(inputs[0], inputs[1])
    remaining_input = inputs[2:]
    root = Node(root_header)
    for children in range(0, root.header.num_child_nodes):
        child, remaining_input = build_tree(remaining_input)
        root.children.append(child)
    for metadata in range(0, root.header.num_metadata_entries):
        root.metadata.append(remaining_input.pop(0))
    return root, remaining_input


def get_metadata_sum(root: Node) -> int:
    result = sum([datum for datum in root.metadata])
    for child in root.children:
        result += get_metadata_sum(child)
    return result


def get_node_value(root: Node) -> int:
    if root.header.num_child_nodes == 0:
        return get_metadata_sum(root)
    else:
        result = 0
        for datum in root.metadata:
            if datum <= root.header.num_child_nodes:
                result += get_node_value(root.children[datum-1])
        return result


if __name__ == '__main__':
    inputs = open('./input.txt').read().split(' ')
    inputs = [int(i) for i in inputs]
    root, _ = build_tree(inputs)
    print(f'part_1: {get_metadata_sum(root)}')
    print(f'part_2: {get_node_value(root)}')

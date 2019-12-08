from typing import List
from dataclasses import dataclass


@dataclass
class Relationship:
    parent: str
    child: str


@dataclass
class Node:
    id: str
    level: int
    parent: 'Node'
    children: List['Node']

    def __init__(self, n_id: str, level: int, parent: 'Node' = None):
        self.id = n_id
        self.level = level
        self.parent = parent
        self.children = []

    @property
    def level_sum(self) -> int:
        return self.level + sum(c.level_sum for c in self.children)

    def find(self, find_id: str) -> 'Node':
        if self.id == find_id:
            return self
        for c in self.children:
            node = c.find(find_id)
            if node is not None:
                return node
        return None


def build_tree(node_id: str, relationships: List[Relationship], level: int = 0) -> Node:
    node_relationships = list(filter(lambda x: x.parent == node_id, relationships))

    node = Node(node_id, level)
    for rel in node_relationships:
        child = build_tree(rel.child, relationships, level + 1)
        child.parent = node
        node.children.append(child)
        relationships.remove(rel)

    return node

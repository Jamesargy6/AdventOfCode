from aoc_lib import file_utils
from typing import List
from collections import namedtuple


Relationship = namedtuple('Relationship', 'parent child')

class Node:
	def __init__(self, id, level, parent):
		self.id = id
		self.level = level
		self.parent = parent
		self.children: List[Node] = []

ROOT = 'COM'
YOU = 'YOU'
SAN = 'SAN'

def get_relationship(raw_str: str) -> Relationship:
	parent, child = raw_str.split(')')
	return Relationship(parent, child)

def build_tree(root_str: str, relationships: List[Relationship], level) -> Node:
	root_relationships = list(filter(lambda x: x.parent == root_str, relationships))

	root = Node(root_str, level, None)
	for rel in root_relationships:
		child = build_tree(rel.child, relationships, level+1)
		child.parent = root
		root.children.append(child)
		relationships.remove(rel)

	return root

def sum_levels(root: Node) -> int:
	return root.level + sum(map(sum_levels, root.children))


def get_common_ancestor(a: Node, b: Node) -> List[Node]:
	while True:
		if a.level > b.level:
			a = a.parent
		elif b.level < a.level:
			b = b.parent
		elif a.id != b.id:
			a = a.parent
			b = b.parent
		else:
			return a


def find(root: Node, find_id: str) -> Node:
	if root.id == find_id:
		return root
	node = None
	for c in root.children:
		node = find(c, find_id)
		if node != None:
			break
	return node

if __name__ == '__main__':
	input_lines = file_utils.read_file_into_str_list('inputs/day6input.txt')
	relationships = list(map(get_relationship, input_lines))
	
	root = build_tree(ROOT, relationships[:], 0)
	print(f'Part 1: {sum_levels(root)}')

	you = find(root, YOU)
	san = find(root, SAN)
	ancestor = get_common_ancestor(you, san)

	moves = (you.level-ancestor.level)+(san.level-ancestor.level)-2
	print(f'Part 2: {moves}')




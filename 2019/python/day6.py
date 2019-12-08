from aoc_lib import file_utils
from aoc_lib.data_structures.tree import Relationship, Node, build_tree
from typing import List


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


if __name__ == '__main__':
	ROOT = 'COM'
	YOU = 'YOU'
	SAN = 'SAN'
	input_lines = file_utils.read_file_into_str_list('inputs/day6input.txt')
	relationships = [Relationship(*line.split(')')) for line in input_lines]
	
	root = build_tree(ROOT, relationships)
	print(f'Part 1: {root.level_sum}')

	you = root.find(YOU)
	san = root.find(SAN)
	ancestor = get_common_ancestor(you, san)
	moves = (you.level-ancestor.level)+(san.level-ancestor.level)-2
	print(f'Part 2: {moves}')




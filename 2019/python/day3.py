from aoc_lib import file_utils
from dataclasses import dataclass
from typing import List, Optional
from collections import namedtuple


Instruction = namedtuple('Instruction', 'direction distance')

Position = namedtuple('Position', 'x y')

LineSegment = namedtuple('LineSegment', 'start end distance')

Intersection = namedtuple('Intersection', 'position steps_taken')


move_dict = {
	'L': lambda x, y, distance: Position(x-distance, y),
	'R': lambda x, y, distance: Position(x+distance, y),
	'U': lambda x, y, distance: Position(x, y+distance),
	'D': lambda x, y, distance: Position(x, y-distance)
}


def get_instruction(raw_ins: str) -> Instruction:
	return Instruction(raw_ins[0], int(raw_ins[1:]))

def generate_wire(instructions: List[Instruction]) -> List[LineSegment]:
	pos = Position(0,0)
	wire: List[LineSegment] = []
	for ins in instructions:
		move = move_dict[ins.direction]
		next_pos = move(pos.x, pos.y, ins.distance)
		wire.append(LineSegment(pos, next_pos, ins.distance))
		pos = next_pos
	return wire

def find_intersections(wire_a: List[LineSegment], wire_b: List[LineSegment]) -> List[Intersection]:
	intersections: List[Intersection] = []

	wire_a_steps_taken: int = 0
	for seg_a in wire_a:
		wire_b_steps_taken: int = 0
		for seg_b in wire_b:
			intersection_position = get_intersection_position(seg_a, seg_b) or get_intersection_position(seg_b, seg_a)
			if intersection_position:
				total_steps_taken = wire_a_steps_taken+wire_b_steps_taken + abs(seg_b.start.x - seg_a.start.x) + abs(seg_b.start.y - seg_a.start.y)
				intersections.append(Intersection(intersection_position, total_steps_taken))
			wire_b_steps_taken += seg_b.distance
		wire_a_steps_taken += seg_a.distance
	return intersections

def get_intersection_position(seg_a: LineSegment, seg_b: LineSegment) -> Position:
	if between(seg_a.start.x, seg_a.end.x, seg_b.start.x) and between(seg_b.start.y, seg_b.end.y, seg_a.start.y):
		return Position(seg_b.start.x, seg_a.start.y)


def between(a: int, b: int, x: int) -> bool:
	return a <= x <= b or a >= x >= b

if __name__ == '__main__':
	raw_wires = file_utils.read_file_into_str_list('inputs/day3input.txt')
	raw_wire_a, raw_wire_b = [raw_wire.split(',') for raw_wire in raw_wires]
	instructions_a = list(map(get_instruction, raw_wire_a))
	instructions_b = list(map(get_instruction, raw_wire_b))
	
	wire_a = generate_wire(instructions_a)
	wire_b = generate_wire(instructions_b)

	intersections = find_intersections(wire_a, wire_b)
	intersections.remove(Intersection(Position(0,0),0))
	
	min_distance = min(map(lambda intersection: abs(intersection.position.x)+abs(intersection.position.y), intersections))
	print(f'Part 1: {min_distance}')
	min_steps = min(map(lambda intersection: intersection.steps_taken, intersections))
	print(f'Part 2: {min_steps}')
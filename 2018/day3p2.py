import sys
from dataclasses import dataclass
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y'])

Size = namedtuple('Size', ['length', 'width'])

@dataclass
class Claim:
	id: str
	start_coord: Coord
	size: Size
	overlaps: bool = False

def ingest_claim(claim: str) -> Claim:
	tokens = claim.split(' ')
	x,y = tokens[2].replace(':', '').split(',')
	length, width = tokens[3].split('x')
	return Claim(tokens[0],
				 Coord(int(x), int(y)), 
				 Size(int(length), int(width)),
				 False)


def get_claimed_coords(claim: Claim) -> list:
	coords = []
	x_start, y_start = claim.start_coord.x, claim.start_coord.y
	length, width = claim.size.length, claim.size.width
	for x in range(length):
		for y in range(width):
			coords.append(Coord(x + x_start, y + y_start))
	return coords


def get_claim_grid(claim_dict: dict) -> dict:
	grid = {}
	for id, claim in claim_dict.items():
		coords = get_claimed_coords(claim)
		for coord in coords:
			if coord not in grid:
				grid[coord] = [id]
			else:
				grid[coord]+=[id]
				for x in grid[coord]:
					claim_dict[x].overlaps = True 
	return grid


if __name__ == '__main__':
	grid = {}
	file = open("./day3input.txt", "r")
	claim_strings = file.read().split("\n")

	claims = [ingest_claim(claim_string) for claim_string in claim_strings]
	claim_dict = { claim.id : claim for claim in claims }

	claim_grid = get_claim_grid(claim_dict)
	overlapping_coords = dict(filter(lambda item: len(item[1]) > 1, claim_grid.items()))
	print(f'Part 1: {len(list(overlapping_coords.keys()))}')
	clean_claims = dict(filter(lambda claim: claim[1].overlaps == False, claim_dict.items()))
	print(f'Part 2: {list(clean_claims.keys())}')

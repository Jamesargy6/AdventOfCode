import sys, math

def ingest_claim(claim: str) -> dict:
	tokens = claim.split(' ')
	print(tokens)
	x,y = tokens[2].replace(':', '').split(',')
	length, width = tokens[3].split('x')
	return dict(coord=(int(x), int(y)), size=(int(length), int(width)))


def get_claimed_coords(claim: dict) -> list:
	tuples = []
	xcoord, ycoord = claim['coord']
	length, width = claim['size']
	for x in range(length):
		for y in range(width):
			tuples.append((x + xcoord, y + ycoord))
	return tuples


def get_coord_grid(claims: list) -> dict:
	grid = {}
	for claim in claims:
		coords = get_claimed_coords(claim)
		for coord in coords:
			grid[coord] = 1 if coord not in grid else grid[coord]+1
	return grid

def get_overlapping_claims(grid: dict) -> list:
	overlapping_claims = {}
	for (coord, value) in grid.items():
	   if value > 1:
	       overlapping_claims[coord] = value
	return overlapping_claims


if __name__ == '__main__':

	file = open("./day3input.txt", "r")
	claim_strings = file.read().split("\n")

	claims = [ingest_claim(claim_string) for claim_string in claim_strings]

	grid = get_coord_grid(claims)
	overlapping_claims = get_overlapping_claims(grid)
	print(len(overlapping_claims))



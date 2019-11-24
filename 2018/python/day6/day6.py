from dataclasses import dataclass
from typing import List, Dict
from collections import namedtuple


Location = namedtuple('Location', 'x y')


@dataclass
class Point:
    location: Location
    closest_id: int = -1
    distance_to_closest: int = 10000
    total_distance: int = 0


@dataclass
class Coordinate:
    id: int
    location: Location


def get_coordinate_list(input: str) -> List[Point]:
    input_list = input.split('\n')
    return [Coordinate(idx, Location(int(tokens[0]), int(tokens[1])))
            for idx, tokens in enumerate([input_str.split(', ')
                                          for input_str in input_list])]


def initialize_grid(coordinates: List[Coordinate]) -> List[Point]:
    x_vals = [coord.location.x for coord in coordinates]
    y_vals = [coord.location.y for coord in coordinates]
    x_min = min(x_vals)
    x_max = max(x_vals)
    y_min = min(y_vals)
    y_max = max(x_vals)

    return [Point(Location(x,y)) for x,y in [(x,y) for x in range(x_min-1, x_max+2) for y in range(y_min-1, y_max+2)]]


def get_manhattan_distance(a: Location, b: Location) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def calculate_closest_coordinate(coordinates: List[Coordinate], points: List[Point]):
    for coord in coordinates:
        for point in points:
            distance = get_manhattan_distance(coord.location, point.location)
            point.total_distance += distance
            if distance < point.distance_to_closest:
                point.closest_id = coord.id
                point.distance_to_closest = distance
            elif distance == point.distance_to_closest:
                point.closest_id = '#'
                point.distance_to_closest = distance


def get_finite_coordinates(coordinates: List[Coordinate], grid: List[Point]) -> List[Coordinate]:
    x_vals = [coord.location.x for coord in coordinates]
    y_vals = [coord.location.y for coord in coordinates]
    x_min = min(x_vals)
    x_max = max(x_vals)
    y_min = min(y_vals)
    y_max = max(x_vals)
    finite_coordinates = []
    for coordinate in coordinates:
        points_closest = list(list(filter(lambda point: point.closest_id == coordinate.id, grid)))
        if len(list(filter(lambda point: point.location.x < x_min
                                      or point.location.x > x_max
                                      or point.location.y < y_min
                                      or point.location.y > y_max, points_closest))) == 0:
            finite_coordinates.append(coordinate)
    return finite_coordinates

if __name__ == '__main__':
    input = open('./input.txt').read()
    coordinates = get_coordinate_list(input)
    grid = initialize_grid(coordinates)
    calculate_closest_coordinate(coordinates, grid)
    finite_coordinates = get_finite_coordinates(coordinates, grid)
    finte_coord_distances = {}
    for coordinate in finite_coordinates:
        finte_coord_distances[coordinate.id] = len(list(filter(lambda point: point.closest_id == coordinate.id, grid)))

    print(f'Part 1: {max(finte_coord_distances.values())}')
    print(f'Part 2: {len(list(filter(lambda point: point.total_distance < 10000, grid)))}')



from dataclasses import dataclass
from collections import namedtuple
from typing import List

Position = namedtuple('Position', 'x y')

Velocity = namedtuple('Velocity', 'x_delta y_delta')

@dataclass
class Point:
    position: Position
    velocity: Velocity

# position=< -9951, -50547> velocity=< 1,  5>


def get_tuple(input: str):
    first, second = input.split(', ')
    return int(first), int(second)


def get_point(input: str) -> Point:
    p_start, p_end =  input.find('<'), input.find('>')
    position = get_tuple(input[p_start + 1:p_end])
    v_start, v_end = input.rfind('<'), input.rfind('>')
    velocity = get_tuple(input[v_start + 1:v_end])
    return Point(Position(position[0], position[1]), Velocity(velocity[0], velocity[1]))

    return points


def iterate_until_message(points: List[Point]) -> int:
    seconds_taken = 0
    while True:
        max_y = max([point.position.y for point in points])
        min_y = min([point.position.y for point in points])
        if max_y-min_y < 10:
            return seconds_taken
        for point in points:
            point.position = Position(point.position.x + point.velocity.x_delta, point.position.y + point.velocity.y_delta)
        seconds_taken += 1


def print_points(points: List[Point]):
    max_y = max([point.position.y for point in points])
    max_x = max([point.position.x for point in points])
    min_x = min([point.position.x for point in points])

    grid: List[List[int]] = [['.' for x in range(max_x-min_x+1)] for y in range(max_y+1)]

    for point in points:
        point.position = Position(point.position.x-min_x, point.position.y)
        grid[point.position.y][point.position.x] = '#'

    for x in grid:
        if '#' in x:
            print(x)



if __name__ == '__main__':
    inputs = open('./input.txt').read().split('\n')
    points = [get_point(input) for input in inputs]

    part_2_result = iterate_until_message(points)
    print_points(points)
    print(part_2_result)
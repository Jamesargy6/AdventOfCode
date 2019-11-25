from collections import namedtuple
from typing import List
import re

SPIGOT = '+'
CLAY = '#'
SAND = '.'
RUNNING_WATER = '|'
STILL_WATER = '~'


Point = namedtuple('Point', 'x y')

class GroundGrid(List[List[str]]):

    def set_point(self, point: Point, value: str):
        self[point.y][point.x] = value

    def get_point(self, point: Point) -> str:
        return self[point.y][point.x]

def get_clay_points(input_str: str) -> List[Point]:
    start, range_str = input_str.split(', ')
    start_axis, start_position = start.split('=')
    start_position = int(start_position)
    range_axis, range_values = range_str.split('=')
    range_start, range_end = range_values.split('..')
    range_start, range_end = int(range_start), int(range_end)


    points: List[Point] = []
    for i in range(range_start, range_end+1):
        points.append(Point(start_position, i))

    if start_axis == 'y':
        points = [Point(y, x) for x, y in points]
    return points


def initialize_ground_grid(input_strings: List[str], spigot: Point) -> (GroundGrid, int, int):
    clay_point_lists = [get_clay_points(input) for input in input_strings]
    clay_points = [point for clay_point_list in clay_point_lists for point in clay_point_list]
    max_x = max([point.x for point in clay_points])+2
    min_y = min([point.y for point in clay_points])
    max_y = max([point.y for point in clay_points])+1

    ground_grid: GroundGrid = GroundGrid()

    for y in range(max_y+1):
        ground_grid.append([])
        for x in range(max_x+2):
            ground_grid[y].append(SAND)

    for point in clay_points:
        ground_grid.set_point(point, CLAY)

    ground_grid.set_point(spigot, SPIGOT)

    return ground_grid, max_x, min_y, max_y



def turn_on_spigot(ground_grid: GroundGrid, spigot: Point, running_water_queue: List[Point]):
    new_running_water = Point(spigot.x, spigot.y+1)
    ground_grid.set_point(new_running_water, RUNNING_WATER)
    running_water_queue.append(new_running_water)

def count_water(ground_grid: GroundGrid, min_y: int, max_y: int, still_only: bool=False) -> int:
    filter_func = lambda x: x == RUNNING_WATER or x == STILL_WATER
    if still_only: 
        filter_func = lambda x:  x == STILL_WATER
    return sum([len(list(filter(filter_func, row))) for row in ground_grid[min_y:max_y]])

def is_valid_point(point: Point, max_x: int, max_y: int) -> bool:
    return point.x < max_x and point.y <= max_y

def process_point(ground_grid: GroundGrid, running_water_queue: List[Point], max_x: int, max_y, point: Point) -> bool:
    if is_valid_point(point, max_x, max_y) and ground_grid.get_point(point) == SAND:
        ground_grid.set_point(point, RUNNING_WATER)
        running_water_queue.append(point)
        return True
    return False

def propogate_running_water(ground_grid: GroundGrid, running_water_queue: List[Point], max_x: int, max_y):

    while len(running_water_queue) > 0:
        running_water_point = running_water_queue.pop()
        point_below = Point(running_water_point.x, running_water_point.y+1)
        point_added = process_point(ground_grid, running_water_queue, max_x, max_y, point_below)
        if not point_added and is_valid_point(point_below, max_x, max_y) and ground_grid.get_point(point_below) is not RUNNING_WATER:
            point_left = Point(running_water_point.x-1, running_water_point.y)
            process_point(ground_grid, running_water_queue, max_x, max_y, point_left)
            point_right = Point(running_water_point.x+1, running_water_point.y)
            process_point(ground_grid, running_water_queue, max_x, max_y, point_right)

def add_running_water_to_queue(ground_grid: GroundGrid, running_water_queue: List[Point], point: Point):
    if point.y > 0 and ground_grid.get_point(point) == RUNNING_WATER:
        running_water_queue.append(point)

def make_still_water(ground_grid: GroundGrid, running_water_queue: List[Point], max_x: int, max_y):
    running_water_match = '#\|+#'
    floor_match = '[#~]+'

    potential_still_water_ranges: List[(Point, Point)] = []
    for y, row in enumerate(ground_grid):
        row_string = ''.join(row)
        potential_still_water_ranges.extend([(Point(m.start(0)+1, y), Point(m.end(0)-1, y)) for m in re.finditer(running_water_match, row_string)])

    for water_range in potential_still_water_ranges:
        range_start, range_end = water_range[0], water_range[1]
        below_start = Point(range_start.x, range_start.y+1)
        below_end = Point(range_end.x, range_end.y+1)
        if is_valid_point(below_start, max_x, max_y):
            below_string = ''.join(ground_grid[below_start.y][below_start.x:below_end.x+1])
            if re.search(floor_match, below_string):
                for x in range(range_start.x, range_end.x):
                    still_water_point = Point(x, range_start.y)
                    ground_grid.set_point(still_water_point, STILL_WATER)
                    point_above = Point(still_water_point.x, still_water_point.y-1)
                    add_running_water_to_queue(ground_grid, running_water_queue, point_above)


def print_grid(ground_grid: GroundGrid, min_x: int, max_x: int, min_y: int, max_y: int):
    for y in range(min_y, max_y+1):
        print(''.join(ground_grid[y][min_x:max_x+1]))
    print()


if __name__ == '__main__':
    input = open('./input.txt').read().split('\n')
    spigot = Point(500, 0)

    ground_grid, max_x, min_y, max_y = initialize_ground_grid(input, spigot)
    current_water_count = 0
    running_water_queue: List[Point] = []

    turn_on_spigot(ground_grid, spigot, running_water_queue)

    while True:
        new_water_count = count_water(ground_grid, 0, max_y)
        if new_water_count == current_water_count:
            break
        current_water_count = new_water_count
        propogate_running_water(ground_grid, running_water_queue, max_x, max_y)
        make_still_water(ground_grid, running_water_queue, max_x, max_y)
    print_grid(ground_grid, 0, max_x, 0, max_y)



    print(count_water(ground_grid, min_y, max_y))
    print(count_water(ground_grid, min_y, max_y, True))



    
    




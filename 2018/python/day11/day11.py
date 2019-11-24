import sys
from typing import List, Dict


def get_hundredths_place(input: int) -> int:
    input = input // 100
    return input % 10


def get_power_level(grid_serial_number: int, x_index: int, y_index: int) -> int:
    rack_id = x_index + 10
    power_level = rack_id * y_index
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = get_hundredths_place(power_level)
    power_level -= 5
    return power_level


def build_grid(grid_serial_number: int) -> List[List[int]]:
    grid: List[List[int]] = []
    for x in range(300):
        grid.append([])
        for y in range(300):
            power_level = get_power_level(grid_serial_number, x+1, y+1)
            grid[x].append(power_level)
    return grid


def get_grid_sum(grid, x, y, grid_size) -> int:
    sum = 0
    for current_x in range(x, x+grid_size):
        for current_y in range(y, y+grid_size):
            sum += grid[current_x][current_y]
    return sum


def part_1(grid: List[List[int]], grid_size: int) -> int:
    max_sum, max_x, max_y = -1, -1, -1
    for x in range(len(grid)-grid_size):
        for y in range(len(grid[x])-grid_size):
            grid_sum = get_grid_sum(grid, x, y, grid_size)
            if(grid_sum > max_sum):
                max_sum = grid_sum
                max_x, max_y = x+1, y+1
    return max_sum, max_x, max_y


def get_grid_perimeter(grid, x_start, y_start, grid_size) -> int:
    horizontal = sum([grid[x][y_start+grid_size-1] for x in range(x_start, x_start+grid_size-1)])
    vertical = sum([grid[x_start+grid_size-1][y] for y in range(y_start, y_start+grid_size)])
    return horizontal + vertical


def part_2(grid: List[List[int]]) -> int:
    coords_grid_size: Dict[(int, int),int] = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            coords_grid_size[(x, y)] = grid[x][y]

    max_sum, max_x, max_y = -1, -1, -1
    max_size: int
    for grid_size in range(2, len(grid)+1):
        for x in range(len(grid) - grid_size):
            for y in range(len(grid[x]) - grid_size):
                grid_sum = coords_grid_size[(x, y)] + get_grid_perimeter(grid, x, y, grid_size)
                coords_grid_size[(x, y)] = grid_sum
                if (grid_sum > max_sum):
                    max_sum = grid_sum
                    max_x, max_y = x + 1, y + 1
                    max_size = grid_size
    return max_x, max_y, max_size

if __name__ == '__main__':
    grid_serial_number = int(sys.argv[1])

    grid = build_grid(grid_serial_number)

    print(part_1(grid, 3))
    print('-------------------')
    print(part_2(grid))
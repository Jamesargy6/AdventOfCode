from typing import List
from collections import namedtuple
from dataclasses import dataclass


Point = namedtuple('Point', 'x y')

HORIZONTAL = '-'
VERTICAL = '-'
TURN_A = '\\'
TURN_B = '/'
FORK = '+'

CART_RIGHT = '>'
CART_UP = '^'
CART_LEFT = '<'
CART_DOWN = 'v'

CARTS = [CART_RIGHT, CART_DOWN, CART_LEFT, CART_UP]

ORIENTATIONS_MOVEMENT = {
    CART_RIGHT: Point(1, 0),
    CART_UP: Point(0, -1),
    CART_LEFT: Point(-1, 0),
    CART_DOWN: Point(0, 1)
}

NEXT_DIRECTION = {
    TURN_A: {
        CART_RIGHT: CART_DOWN,
        CART_UP: CART_LEFT,
        CART_LEFT: CART_UP,
        CART_DOWN: CART_RIGHT
    },
    TURN_B: {
        CART_RIGHT: CART_UP,
        CART_UP: CART_RIGHT,
        CART_LEFT: CART_DOWN,
        CART_DOWN: CART_LEFT
    },
    FORK: {
        'L': {
        CART_RIGHT: CART_UP,
        CART_UP: CART_LEFT,
        CART_LEFT: CART_DOWN,
        CART_DOWN: CART_RIGHT
        },
        'C': {
        CART_RIGHT: CART_RIGHT,
        CART_UP: CART_UP,
        CART_LEFT: CART_LEFT,
        CART_DOWN: CART_DOWN
        },
        'R': {
        CART_RIGHT: CART_DOWN,
        CART_UP: CART_RIGHT,
        CART_LEFT: CART_UP,
        CART_DOWN: CART_LEFT
        },
    }
}

NEXT_FORK_DIRECTION = {
    'L': 'C',
    'C': 'R',
    'R': 'L'
}



@dataclass
class Cart:
    location: Point
    orientation: int
    fork_decision: str = 'L'



def setup_track_grid(input: str) -> (List[List[str]], List[Cart]):
    rows = open('./input.txt').read().split('\n')
    grid: List[List[str]] = []
    carts: List[Cart] = []
    cart_replacements = {
        CART_DOWN: '|',
        CART_UP: '|',
        CART_RIGHT: '-',
        CART_LEFT: '-'
    }
    for row_index in range(len(rows)):
        current_row = rows[row_index]
        carts_in_row = [(index, cart) for index, cart in enumerate(current_row) if current_row[index] in CARTS]
        for index, cart in carts_in_row:
            carts.append(Cart(Point(index, row_index), cart))
            current_row = current_row.replace(cart, cart_replacements[cart])
        grid.append(current_row)
    return grid, carts


def move_cart(cart: Cart, grid: List[List[str]]):
    movement = ORIENTATIONS_MOVEMENT[cart.orientation]
    cart.location = Point(cart.location.x + movement.x, cart.location.y + movement.y)
    next_track = grid[cart.location.y][cart.location.x]
    if next_track in [TURN_A, TURN_B]:
        cart.orientation = NEXT_DIRECTION[next_track][cart.orientation]
    elif next_track == FORK:
        cart.orientation = NEXT_DIRECTION[next_track][cart.fork_decision][cart.orientation]
        cart.fork_decision = NEXT_FORK_DIRECTION[cart.fork_decision]


def remove_collisions(cart: Cart, carts: List[Cart]):
    collision_locations = []
    for other_cart in carts:
        if other_cart.location == cart.location and other_cart.orientation != cart.orientation:
            collision_locations.append(cart.location)
            print(f'Collision at {cart.location}')
            break
    return list(filter(lambda cart: cart.location not in collision_locations, carts))


def tick_until_last_remaining_cart(carts: List[Cart], grid: List[List[str]]) -> Cart:
    carts = sorted(carts, key = lambda cart: (cart.location.y, cart.location.x))
    while len(carts) > 1:
        for cart in carts:
            move_cart(cart, grid)
            carts = remove_collisions(cart, carts)
    return carts[0]


if __name__ == '__main__':
    input = open('./input.txt').read().split('\n')
    grid, carts = setup_track_grid(input)
    print(f'Last Remaining Cart Location: {tick_until_last_remaining_cart(carts, grid).location}')
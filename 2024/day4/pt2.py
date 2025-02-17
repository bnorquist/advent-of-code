# advent of code day 2
from symbol import continue_stmt

import pytest
import argparse


def find_mas(rows):
    # find position of A's first
    xs = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "A":
                xs.append((i, j))
    found = 0
    # print(xs)
    # print(rows)
    for pos in xs:
        i, j = pos
        if visit_neighbors(i, j, rows):
            found += 1
    # i, j = xs[1]
    # found += visit_neighbors(i, j, rows)
    print(f"Founds {found} MASs, gotta live mas")
    return found

def visit_neighbors(i, j, rows) -> int:
    """
    visit up, down, left, right and diagonal neighbors
    if first neighbor is in bounds and equal to M then visit next neighbor in that direction
    :param i:
    :param j:
    :param rows:
    :return:
    """
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    # print(f"visiting {i},{j}")
    for x, y in directions:
        if find_neighbor(i, j, rows, x, y):
            if find_neighbor(i, j, rows, x*-1, y) or find_neighbor(i, j, rows, x, y*-1):
                return True

    return False

def find_neighbor(i, j, rows, x, y) -> bool:
    x_pos = i+x
    y_pos = j+y
    # print(f"checking for M {x_pos}, {y_pos}")
    if x_pos >= len(rows) or y_pos >= len(rows[0]) or x_pos < 0 or y_pos < 0 or rows[x_pos][y_pos] != "M":
        return False
    # print("found M")
    # now check opposite direction for S
    x_pos = i+(x * -1)
    y_pos = j+(y * -1)
    # print(f"checking for S {x_pos}, {y_pos}")
    if x_pos >= len(rows) or y_pos >= len(rows[0]) or x_pos < 0 or y_pos < 0 or rows[x_pos][y_pos] != "S":
        return False
    # print("found a Mas")
    return True


def test() -> None:
    with open("input.txt") as f:
        commands = f.read().split("\n")
        print(find_mas(commands))
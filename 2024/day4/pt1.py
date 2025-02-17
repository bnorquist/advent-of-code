# advent of code day 2
import pytest
import argparse


def find_xmas(rows):
    # find position of X's first
    xs = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == "X":
                xs.append((i, j))
    found = 0
    print(xs)
    print(rows)
    for pos in xs:
        i, j = pos
        found += visit_neighbors(i, j, rows)
    # i, j = xs[0]
    # found += visit_neighbors(i, j, rows)
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
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    for x, y in directions:
        if visit_neighbor_sequence(i, j, rows, x, y):
            count += 1
    return count

def visit_neighbor_sequence(i, j, rows, x, y) -> bool:
    looking_for = ["M", "A", "S"]
    # print(f"direction {x}, {y}")
    for k, char in enumerate(looking_for):
        k += 1
        x_pos = i+(x*k)
        y_pos = j+(y*k)
        # print(f"visiting {x_pos}, {y_pos}")
        if x_pos < len(rows) and y_pos < len(rows[0]) and x_pos >= 0 and y_pos >= 0 and rows[x_pos][y_pos] == char:
            # print(rows[x_pos][y_pos])
            continue
        else:
            return False
    # print("here")
    return True

def test() -> None:
    with open("input.txt") as f:
        commands = f.read().split("\n")
        print(find_xmas(commands))
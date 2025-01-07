# advent of code day 3
import argparse
from typing import List
from typing import Set
from typing import Tuple

import pytest


def draw_lines(dirs: List[str]) -> Set[Tuple[int, int]]:
    x = 0
    y = 0
    wire = set()
    for segment in dirs:
        direction = segment[0]
        amount = int(segment[1:])
        for _ in range(amount):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "D":
                y -= 1
            elif direction == "U":
                y += 1
            else:
                raise Exception("Parsing Direction Error")
            wire.add((x, y))

    return wire


def compute(instructions: str) -> int:
    wires = instructions.split("\n")
    wire1 = wires[0].split(",")
    wire2 = wires[1].split(",")
    path1 = draw_lines(wire1)
    path2 = draw_lines(wire2)
    intersects = path1.intersection(path2)

    # calculate the closest intersection
    closest = (int(999999999), (0, 0))
    for i in intersects:
        distance = abs(i[0]) + abs(i[1])
        if distance < closest[0]:
            closest = (distance, i)

    return closest[0]


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83", 159),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())

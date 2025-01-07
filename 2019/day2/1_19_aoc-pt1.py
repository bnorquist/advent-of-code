# advent of code day 2
import argparse
from typing import List

import pytest


def add(pos: int, ops: List[int]) -> None:
    ops[ops[pos + 3]] = ops[ops[pos + 1]] + ops[ops[pos + 2]]


def multiply(pos: int, ops: List[int]) -> None:
    ops[ops[pos + 3]] = ops[ops[pos + 1]] * ops[ops[pos + 2]]


def adjust_input(ops: List[int]) -> List[int]:
    ops[1] = 12
    ops[2] = 2
    return ops


def compute(operations: str, adjust: bool) -> List[int]:
    ops = []
    for op in operations.split(","):
        ops.append(int(op))

    if adjust:
        ops = adjust_input(ops)

    pos = 0
    while pos <= len(ops):
        if ops[pos] == 1:
            add(pos, ops)
        elif ops[pos] == 2:
            multiply(pos, ops)
        elif ops[pos] == 99:
            return ops
        else:
            print(pos)
            raise Exception("THE COMPUTER BROKE")
        pos += 4
    return []


@pytest.mark.parametrize(
    ("input_s", "adjust", "expected"),
    (
        ("1,0,0,0,99", False, [2, 0, 0, 0, 99]),
        ("2,4,4,5,99,0", False, [2, 4, 4, 5, 99, 9801]),
        ("1,1,1,4,99,5,6,0,99", False, [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ),
)
def test(input_s: str, expected: int, adjust: bool) -> None:
    assert compute(input_s, adjust) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read(), True))

    return 0


if __name__ == "__main__":
    exit(main())

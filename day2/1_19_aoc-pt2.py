# advent of code day 2
import argparse
from typing import List
from typing import Tuple


def add(pos: int, ops: List[int]) -> None:
    ops[ops[pos + 3]] = ops[ops[pos + 1]] + ops[ops[pos + 2]]


def multiply(pos: int, ops: List[int]) -> None:
    ops[ops[pos + 3]] = ops[ops[pos + 1]] * ops[ops[pos + 2]]


def adjust_input(ops: List[int], noun: int, verb: int) -> List[int]:
    ops[1] = noun
    ops[2] = verb
    return ops


def run_computer(ops: List[int], noun: int, verb: int) -> List[int]:
    ops = adjust_input(ops=ops, noun=noun, verb=verb)

    pos = 0
    while pos <= len(ops):
        if ops[pos] == 1:
            add(pos, ops)
        elif ops[pos] == 2:
            multiply(pos, ops)
        elif ops[pos] == 99:
            return ops
        else:
            raise Exception(
                f"THE COMPUTER BROKE at position: {pos}, noun {noun}, verb {verb}, operation {ops[pos]}"
            )
        pos += 4
    return []


def compute(operations: str) -> Tuple[int, int]:
    initial_ops = []
    for op in operations.split(","):
        initial_ops.append(int(op))

    for i in range(0, 100):
        for j in range(0, 100):
            ops = initial_ops.copy()
            result = run_computer(ops, i, j)
            if result[0] == 19690720:
                return result[1], result[2]

    return (0, 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())

# advent of code day 1
import pytest
import argparse

def compute() -> int:
    pass


def test() -> None:
    left = []
    right = []
    distance = 0
    with open("input.txt") as f:
        pairs = f.read().split("\n")
        for p in pairs:
            left.append(int(p.split("   ")[0]))
            right.append(int(p.split("   ")[1]))
    s_left = sorted(left)
    s_right = sorted(right)

    for i in range(len(s_left)):
        distance += abs(s_left[i] - s_right[i])
    print(distance)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())

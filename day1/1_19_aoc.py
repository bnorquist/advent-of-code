# advent of code day 1

import argparse

import pytest

from support import timing

def get_fuel(mass: int) -> int:
    fuel = (mass // 3) - 2
    return fuel

def get_all_fuel(s):

    return fuel_need

def compute(s: str) -> int:
    fuel_need += (get_fuel(int(mass)) for mass in s.splitlines())
    return fuel_need


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ),

)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())

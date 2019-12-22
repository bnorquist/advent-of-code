# advent of code day 1

import argparse

import pytest

from timing import timing


def get_fuel(mass: int) -> int:
    fuel = (mass // 3) - 2
    return fuel


def compute(s: str) -> int:
    total_fuel = 0
    for mass in s.splitlines():
        fuel_need = 0
        fuel_need += get_fuel(int(mass))

        additional_fuel = get_fuel(fuel_need)
        while additional_fuel > 0:
            fuel_need += additional_fuel
            additional_fuel = get_fuel(additional_fuel)
        total_fuel += fuel_need

    return total_fuel


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('14', 2),
        ('100756', 50346),
        ('1969', 966),
        ('14\n100756\n1969', 51314),
    ),

)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())

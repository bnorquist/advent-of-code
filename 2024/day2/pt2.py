# advent of code day 2
import pytest
import argparse

def compute() -> int:
    pass

def validate_report(report: list[int]) -> bool:
    """
    Check that the numbers in the report are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    """
    if report[0] < report[1]:
        increasing = True
    elif report[0] > report[1]:
        increasing = False
    else:
        return False # the first two numbers are the same

    for i, num in enumerate(report):
        if i + 1 < len(report):
            next_num = report[i + 1]
            if increasing:
                if num > next_num:
                    return False
            else:
                if num < next_num:
                    return False
            diff = abs(num - next_num)
            if diff > 3 or diff < 1:
                return False
    return True

def test() -> None:
    count = 0
    with open("input.txt") as f:
        reports = f.read().split("\n")
        for r in reports:
            report = [int(x) for x in r.split(" ")]
            valid = validate_report(report)
            if valid:
                count += 1
            else:
                for i in range(len(report)):
                    valid = validate_report(report[:i] + report[i+1:])
                    if valid:
                        count += 1
                        break
    print(count)
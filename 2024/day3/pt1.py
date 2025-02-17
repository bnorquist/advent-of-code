# advent of code day 2
import pytest
import argparse

def compute() -> int:
    pass


import re


def find_all_mul_expressions_with_positions(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, text)
    results = []

    for match in matches:
        full_match = match.group(0)  # The entire match
        num1 = match.group(1)  # First captured group
        num2 = match.group(2)  # Second captured group
        start_pos = match.start()  # Start position of the match
        end_pos = match.end()  # End position of the match

        results.append({
            "expression": full_match,
            "numbers": (int(num1), int(num2)),
            "position": (start_pos, end_pos)
        })
        # print(int(num1), int(num2))

    return results

def multiply(commands: str) -> int:
    matched_numbers = find_all_mul_expressions_with_positions(commands)
    result = 0
    for match in matched_numbers:
        numbers = match["numbers"]
        result += numbers[0] * numbers[1]

    return result

def test() -> None:
    with open("input.txt") as f:
        commands = f.read()
        print(multiply(commands))

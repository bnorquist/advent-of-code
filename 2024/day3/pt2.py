# advent of code day 2
import pytest
import argparse

def compute() -> int:
    pass


import re


def find_all_mul_expressions_with_positions(text):
    # Pattern now matches either mul(number,number) OR do() OR don't()
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
    matches = re.finditer(pattern, text)

    results = []
    for match in matches:
        if match.group(1):  # This is a mul() match
            num1 = match.group(2)
            num2 = match.group(3)
            results.append({
                "expression": match.group(1),
                "type": "mul",
                "numbers": (int(num1), int(num2))
            })
        elif match.group(4):  # This is a do() match
            results.append({
                "expression": "do()",
                "type": "do"
            })
        elif match.group(5):  # This is a don't() match
            results.append({
                "expression": "don't()",
                "type": "dont"
            })

    return results


def multiply(commands: str) -> int:
    matches = find_all_mul_expressions_with_positions(commands)
    result = 0
    do = True
    for match in matches:
        if match["type"] == "dont":
            do = False
        elif match["type"] == "do":
            do = True
        elif match["type"] == "mul" and do:
            numbers = match["numbers"]
            result += numbers[0] * numbers[1]

    return result

def test() -> None:
    with open("input.txt") as f:
        commands = f.read()
        print(multiply(commands))

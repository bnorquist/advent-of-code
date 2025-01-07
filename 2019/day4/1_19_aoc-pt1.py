# advent of code day 4
import pytest


start = 307237
end = 769058


def is_valid(num: int) -> bool:
    str_num = str(num)
    has_repeating = False
    char = str_num[0]
    for i in range(1, len(str_num)):
        if str_num[i] == char:
            has_repeating = True
        elif int(str_num[i]) < int(char):
            return False
        char = str_num[i]
    return has_repeating


def compute() -> int:
    valid_passwords = []
    for num in range(start, end + 1):
        if is_valid(num):
            valid_passwords.append(num)
    return len(valid_passwords)


@pytest.mark.parametrize(
    ("input_s", "expected"), ((111111, True), (223450, False), (123789, False)),
)
def test(input_s: int, expected: bool) -> None:
    assert is_valid(input_s) == expected


def main() -> int:
    print(compute())

    return 0


if __name__ == "__main__":
    exit(main())

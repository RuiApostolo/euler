#!/usr/bin/python3
"""euler project 0001"""


def main() -> int:
    """returns sum multiples of 3 or 5 under 1000"""

    target = 1000
    result = 0

    for i in range(1, target):
        result += is_multiple(i, [3, 5])
    return result


def is_multiple(number: int, multiples: list) -> int:
    """returns number if it's multiple of any number in the list"""
    if any(number % a == 0 for a in multiples):
        return number
    return 0


if __name__ == "__main__":
    print(main())

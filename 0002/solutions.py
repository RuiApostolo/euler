#!/usr/bin/python3
"""euler project 0002"""


def main() -> int:
    """returns sum of even elements of fibonnaci sequence
    under 4_000_000"""

    target = 4_000_000
    result = 0

    fib = fibonnaci()
    number = next(fib)

    while number < target:
        if number % 2 == 0:
            result += number
        number = next(fib)

    return result


def fibonnaci() -> int:
    """generator that yields next fibonnaci element"""
    first = 0
    second = 1

    while True:
        yield second
        first, second = second, first + second


if __name__ == "__main__":
    print(main())

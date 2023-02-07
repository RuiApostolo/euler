#!/usr/bin/python3
"""euler project 0004"""


def main() -> int:
    """largest palindrom product"""

    start = 999

    return get_largest_palindrome(start)


def get_largest_palindrome(start: int) -> int:
    """get largest palindrome"""

    # initialize variables
    current_max = 0

    for one in range(start, 99, -1):
        for two in range(one, 99, -1):

            onetwo = one * two

            if is_palindrome(onetwo) and onetwo > current_max:
                current_max = onetwo

            if onetwo < current_max and current_max > 0:
                break

        if one * one < current_max and current_max > 0:
            break

    return current_max


def is_palindrome(target: int) -> bool:
    """checks if a number is a palindrome"""
    number = str(target)
    for i in range(len(number)):
        if number[i] != number[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(main())

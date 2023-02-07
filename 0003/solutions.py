#!/usr/bin/python3
"""euler project 0003"""

from itertools import count


def main() -> int:
    """prime factors"""

    target = 600_851_475_143

    return get_divisors(target)[-1]


def get_divisors(candidate: int) -> list:
    """returns divisors, first is guaranteed prime"""

    primes = postponed_sieve()
    while True:
        prime = next(primes)
        if candidate % prime == 0:
            if candidate // prime <= 3:
                return [prime]
            return [prime, *get_divisors(candidate // prime)]


def postponed_sieve() -> int:
    """generates a prime using the sieve of Eratosthenes"""

    yield from (2, 3, 5, 7)

    sieve = {}
    psieve = postponed_sieve()
    next(psieve)
    prime = next(psieve)
    assert prime == 3
    prime_sq = prime * prime
    for i in count(9, 2):
        if i in sieve:  # composite
            step = sieve.pop(i)
        elif i < prime_sq:
            yield i
            continue
        else:
            assert i == prime_sq
            step = 2 * prime
            prime = next(psieve)
            prime_sq = prime * prime
        i += step
        while i in sieve:
            i += step
        sieve[i] = step


if __name__ == "__main__":
    print(main())

#!/usr/bin/python3
"""euler project 0005"""

from functools import reduce
from itertools import combinations


#  def main2() -> int:
#      """naive approach, ~95ms"""
#      target = 20
#      result = 20 * 19 * 17
#      loop = True
#
#      while loop:
#          for i in range(3, target + 1):
#              if result % i != 0:
#                  result += 20 * 19
#                  break
#          else:
#              loop = False
#
#      return result


def gen_primes():
    """Generate an infinite sequence of prime numbers."""
    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.

    primes = {}

    # The running integer that's checked for primeness
    candidate = 2

    while True:
        if candidate not in primes:
            # candidate is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations

            yield candidate
            primes[candidate * candidate] = [candidate]
        else:
            # candidate is composite. primes[candidate] is the list of primes
            # that divide it. Since we've reached candidate, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers

            for prime in primes[candidate]:
                primes.setdefault(prime + candidate, []).append(prime)
            del primes[candidate]

        candidate += 1


def main() -> int:
    """prime decompositions approach, ~65ms"""

    target = 20

    return prod(get_divisors(target))


def prod(lst: list) -> int:
    """returns product of list elements"""
    return reduce((lambda x, y: x * y), lst)


def get_divisors(target: int) -> list:
    """returns divisors"""
    # permutations of all lengths not working

    divisors = []

    for i in range(2, target + 1):
        primes = gen_primes()
        combs = []
        break_outer = False
        break_inner = False

        if len(divisors) > 1:
            for j in range(1, len(divisors) + 1):
                els = [list(x) for x in combinations(divisors, j)]
                combs.extend(els)
            for comb in combs:
                if i == prod(comb):
                    break_outer = True
                    break
        if break_outer:
            continue
        for prime in primes:
            if i == prime:
                divisors.append(i)
                break_outer = True
                break
            for j in range(1, len(divisors) + 1):
                els = [list(x) for x in combinations(divisors + [prime], j)]
                combs.extend(els)
            for comb in combs:
                if i == prod(comb):
                    divisors.append(prime)
                    break_outer = True
                    break_inner = True
                    break
            if break_inner:
                break

        if break_outer:
            continue

    print(divisors)
    return divisors


if __name__ == "__main__":
    RESULT = main()
    assert RESULT == 232792560
    print(RESULT)

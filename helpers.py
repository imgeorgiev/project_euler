import math
import numpy as np

def is_palyndrome(num):
    num_str = str(num)
    if len(num_str)%2 == 0:
        left_side = num_str[:len(num_str)//2]
        right_side = num_str[len(num_str)//2:]
        if left_side == right_side[::-1]:
            return True;
        else:
            return False
    else:
        left_side = num_str[:len(num_str)//2]
        right_side = num_str[len(num_str)//2+1:]
        if left_side == right_side[::-1]:
            return True;
        else:
            return False

def to_binary(n):
    return bin(n)[2:]

def is_prime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0 or n%5 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True

def divisors(n):
    divs = []
    for i in range(1, n//2+1):
        if n % i == 0:
            divs.append(i)
    return divs

def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

def is_pandigital(num, n):
    num_str = str(num)
    for i in range(0, n+1):
        if str(i) not in num_str:
            return False
    return True

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


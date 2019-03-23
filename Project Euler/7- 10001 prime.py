# By answing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10001st prime number?

import prtools


def nprime(max):
    n = 2
    c = 1
    answ = []

    while c <= max:
        if prtools.isprime(n) is True:
            answ.append(n)
            n += 1
            c += 1
        else:
            n += 1
    return answ[len(answ) - 1]


nprime(10001)

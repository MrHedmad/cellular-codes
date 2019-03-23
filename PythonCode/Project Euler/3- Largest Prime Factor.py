# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


import math


def isprime(y):
    x = math.ceil(math.sqrt(y))
    # To check if y is prime, one of its divisors must be less than sqrt y.
    z = 2
    # If y is 1, it's not prime. If it is 3 or less, it is prime.
    if y == 1:
        return False
    if y <= 3:
        return True

    # If there are no other numbers that divide y under x, it is prime.
    while z <= x:
        if y % z == 0:
            return False
        else:
            z += 1
    return True


def prdiv(a):
    answ = []
    count = 2

    while count <= a:
        exp = 0
        if isprime(count) is True:
            # If count is prime, then test if it is a dividend of a
            while a % count == 0:
                # If it is a dividend...
                a = a // count
                # Divide a and return the remainder...
                exp += 1
                # Consider that it divided a once...
                if a == 1:
                    # If a = 1, break the loop
                    answ.append([count, exp])
                    return answ
                # This while loops continues until count cannot divide any more
            if exp != 0:
                answ.append([count, exp])
                # If count divided at least once, it is a prime dividend
            count += 1
        else:
            # If count is not prime, move to the next number.
            count += 1
    print(answ)


prdiv(600851475143)

# Maybe check only prime numbers found in the last steps without re-checking?

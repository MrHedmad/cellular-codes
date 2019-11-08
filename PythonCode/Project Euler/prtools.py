import math


def isprime(y):
    """Return True if input is prime, return False if it is not."""
    x = math.ceil(math.sqrt(y))
    z = 2
    if y <= 3:
        return True
    while z <= x:
        if y % z == 0:
            return False
        else:
            z += 1
    return True


def prdiv(a):
    """Return the prime factorization of input, of form (base, exponent)"""
    answ = []
    count = 2
    while count <= a:
        exp = 0
        if isprime(count) is True:
            while a % count == 0:
                a = a // count
                exp += 1
                if a == 1:
                    answ.append((count, exp))
                    return answ
            if exp != 0:
                answ.append((count, exp))
            count += 1
        else:
            count += 1
    print(answ)


def prunder(max):
    """Return all primes under a certain value in a list"""
    c = 0
    answ = []
    while c <= max:
        if isprime(c) is True:
            answ.append(c)
            c += 1
        else:
            c += 1
    return answ

# Under implementation. Do not use


def b_prunder(number):
    import tqdm
    c = 5
    primes = [2, 3]

    for c in tqdm(range(1, number)):
        for prime in primes:
            if c % prime != 0:
                pass
            else:
                break
        else:
            primes.append(c)

        c += 2

    return primes
    # this works up to 200k. When trying to do it for 2000k, it stops working


sum(prunder(2000000))

prdiv(1236)

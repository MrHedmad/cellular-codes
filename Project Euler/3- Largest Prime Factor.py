# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


import math


def isprime(y):
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
    answ = []
    count = 2
    while count <= a:
        exp = 0
        if isprime(count) is True:
            while a % count == 0:
                a = a // count
                exp += 1
                if a == 1:
                    answ.append([count, exp])
                    return answ
            if exp != 0:
                answ.append([count, exp])
            count += 1
        else:
            count += 1
    print(answ)


prdiv(600851475143)

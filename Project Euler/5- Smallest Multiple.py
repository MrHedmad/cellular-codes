# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
import prtools


def _extract(input_list):
    global terms
    for i in input_list:
        if type(i) is not tuple:
            _extract(i)
        else:
            terms.append(i)
    return terms


def extract(input_list):
    global terms
    terms = []
    return _extract(input_list)


def recprdiv(a):
    return [prtools.prdiv(x) for x in a]


a = recprdiv(list(range(2, 21)))
b = set(extract(a))
b

base = [a[0] for a in b]
base

b = list(b)
b


def mcm(x):
    x = list(x)
    answ = []
    for a in {b[0] for b in x}:
        num = 0
        for c in x:
            if c[0] == a:
                num += 1
            else:
                answ.append(x[num])
    print("end")
    return answ


mcm(b)

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 1234023
a = str(a)
b = list(a)

print(b)
len(b)


def ispali(a):
    a = list(str(a))
    count = 0
    length = len(a) // 2

    while count <= length:
        if a[count] == a[len(a) - count - 1]:
            count += 1
        else:
            return False
    return True


ispali(1234567890987554321)

max([x * y for x in range(1, 999) for y in range(1, 999)
     if ispali(x * y) is True])

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def ispali(a):
    a = list(str(a))
    # A list of characteris is more easely compared
    count = 0
    length = len(a) // 2  # Find the length of half the string

    while count <= length:
        if a[count] == a[len(a) - count - 1]:
            # Check if a and a-last digits are the same
            count += 1
        else:
            return False
    return True


ispali(1234567890987554321)

max([[x * y, x, y] for x in range(1, 999) for y in range(1, 999)
     if ispali(x * y) is True])

# Maybe start at the top and work down, stopping at the first one?

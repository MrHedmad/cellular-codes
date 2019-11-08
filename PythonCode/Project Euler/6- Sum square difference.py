# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def sumsqdiff(x):
    """Find the difference between the sum of the squares and the square of the
     sum."""
    # I have no idea of the efficiency of this
    nums = range(1, x+1)
    squares = []
    sums = sum(nums)**2

    for n in nums:
        squares.append(n**2)

    squares = sum(squares)
    return sums - squares


sumsqdiff(100)

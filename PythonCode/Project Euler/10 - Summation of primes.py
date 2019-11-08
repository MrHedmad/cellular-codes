# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import prtools

print(sum(prtools.prunder(2000000)))

# This takes an enourmous amount of time. Should optimize prunder to only check
# the new number by all the primes found below it already.

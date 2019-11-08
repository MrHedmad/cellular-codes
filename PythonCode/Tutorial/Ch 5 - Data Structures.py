from collections import deque  # Used later

# CTRL + F2 to search for bookmarks
# CTRL + ALT + F2 to toggle bookmarks

#  1 - More on Lists

# Lists have many methods:

x, i, iterable = [], [], range(1, 10)

list.append(x)  # Add x at the end of the list.

list.extend(iterable)  # Add all the items from the iterable to the list's end.

list.remove(x)  # Remove the first item from the list called x

list.pop([i])  # remove the item at position i. If i is not specified, the last
# item is removed and returned.

list.clear()  # Remove every object from the list.

list.index(x)  # Returns the index number of the first element x. After x,
# "start, end" arguments can be provided to slice the list before searching.

list.count(x)  # Finds how many times x occours in the list.

list.sort(key=None, reverse=False)  # Sort the items in the list. See "sorted":
# With no argments, it sorts the items in ascending order.

list.reverse()  # Reverses the elements of the list in place.

list.copy()  # Returns a copy of the list. Same as doing list[:].

# We can use lists as Stacks, by using list.append() and list.pop().
# Stacks are used to insert an item from the start, and remove items from the
# end quickly.

stack = [1, 2, 3]
stack.append(4)
stack.append(5)
stack

stack.pop()
stack.pop()
stack

# We can also use lists as queues.
# Queues are used to insert an item from the start, and then remove it from
# the start. Popping them like a stack is not very efficient.
# To create a fast queue, we can use the module deque, which creates an item
# that can pop items quickly both from the start and the end:

# "from collections import deque" from before is used here,

queue = deque(["First", "Second", "Third"])
queue.append("Fourth")
queue.append("Fifth")
queue.popleft()
queue.popleft()
queue

# List comprehension (LC)
# List comprehension can be used to create lists quickly. When creating a list,
# we can open a square bracket, use a for statement, then zero or more for or
# if statements.

combs = []
for x in [1, 2, 3]:  # This creates/overwrites a variable "x"
    for y in [3, 1, 4]:  # This creates/overwrites a variable "y"
        if x != y:
            combs.append((x, y))
combs

# We can write this quickly using list comprehension:
combs2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs2

combs == combs2

# This method creates/overwrites NO variable x or y.
# The pairs, enclosed in parentheses, are called tuples.
# example:

vector = [-4, -2, 0, 2, 4]
[x*2 for x in vector]
# This LC doubles each element x in vector
[x for x in vector if x >= 0]
# Print x for each x in vec, only if x is greater or equal to zero.
[abs(x) for x in vector]
# Using LC we can apply a function to the whole list.
fruit = ["  banana", "  longberry  ", "passion fruit  "]
[test.strip() for test in fruit]
# We can also apply a method
[(x, x**2) for x in range(10)]
# We create a list of tuples using LC

# We can also "flatten" a list of lists using LC:
listoflists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[number for list in listoflists for number in list]
# Print a number, for each list in listoflists, for each number in the list.

# A LC can contain other LC inside it, and also nested functions:
# Let's say we want to get a list of all the values of the columns from this
# list-matrix:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
# So we want a list containing [[1, 5, 9, 13], [2, 6, 10, 14], ...]
# We can create this quickly using a LC:

[[row[i] for row in matrix] for i in range(4)]
# The first LC (row[i] for row in matrix) doesn't run indipendently, it is
# evaluated with the rest of the LC: so, for each "i" in [0, 1, 2, 3 ...]
# row[i] (so, we select each item from the rows) from each row in matrix.
# So, the first pass would be i = 0, select all items with index "0" in each
# element inside the list matrix.

# There can be functions that do complex tasks like this, for this example the
# zip() function can work:

list(zip(*matrix))
# Create a list, by applying the "zip" function to the unpacked matrix (zip
# needs it to be unpacked)


# We can use the "del" keyword to remove an element from a list by using its
# index, or a slice of a list.
a = [0, 1, 2, 3, 4, 5, 6]
del a[3]
a
del a[1:4]
a
# Remember how slicing works. The "5" is kept outside the slice even though
# it has index of 4.
del a[:]  # We can also delete the entire content of the variable
del a  # Or the entire varible from the environment


# 2 - More on Tuples

# Data types that can be indexed and sliced are called "sequence" data types.
# Sequence data types comprend lists, strings and tuples.
# We encountered tuples before: they consist of a number of value separated by
# commas:

tuple = 12345, 54321, "Python"
# When creating a tuple, enclosing () are not needed, but may be required if
# the tuple creation happens inside another expression
tuple
tuple[0]
nestedtuple = tuple, (1, 2, 3, 4, 5, 6)
nestedtuple

# Like strings, tuples are IMMUTABLE, but they can contain different types of
# items.
# Lists and tuples seem similar, but are used for different things: since
# tuples are immutable, they are mostly used by unpacking them (see later);
# Lists are mostly used by iterating over them by appending and modifing them
# by indexing.

# Tuples can be UNPACKED by assiging each item in the tuple to a variable like
# this:

a, b, c = tuple
a
b
c
# Note that the number of elements in the left, must be the same of the ones
# on the right (inside the tuple).


# 3 - Sets


# Sets are unordered, undiplicated groups of items. They can be made using the
# set() function or curly braces:

basket = {"apple", "apple", "orange", "banana", "banana", "grapes"}
basket
# Notice how duplicate items are automatically removed.

# Sets can be tested:
"orange" in basket
"blueberry" in basket

# Sets also support union, intersection, difference...

a = set("abracadabra")
b = set("alacazam")
a
b
# set() "unpacks" strings, and makes them into sets.

a - b  # Letters in a but not in b
a | b  # Letters in a OR in b or in both
a & b  # Letters in a AND b at the same time
a ^ b  # Letters in a OR b but NOT in both

# Similar to list comprehensions, set comprehensions are also supported.
a = {x for x in "abracadabra" if x not in "abc"}
a  # print x for each x in "abracadabra" if x is not in "abc"

# 3 - Dictionaries

# A dictionary is indexed using keys. Keys can be any type of immutable object,
# like a number, a string, a tuple (containing only other tuples or numbers
# or strings). A dictionary is an unordered set of key:value pairs.
# We can create a dictionary using curly braces {} with key:value pairs
# separated by commas.

tel = {"jack": 231042, "mark": 3124560}

# We can extract a value by using its key, change it (and thus forgetting the
# old value), adding it by specifing a new key and value, or deleting it with
# del.

tel["Gennara"] = 123456
tel
tel["jack"]
del tel["jack"]
tel
tel["evee"] = 432567
list(tel.keys())
sorted(tel.keys())
"Gennara" in tel
"Fabio" in tel
"evee" not in tel

# We can also use the dic() function to create dictionaries from sequences of
# key, data pairs, or even use dictionary comprehensions:

dict([("sape", 123), ("Gennara", 456), ("Stefano", 567)])
{x: x**2 for x in range(1, 5)}

# 4 - Looping techniques

# There are some useful looping techniques to retrieve data from structures:

# To retrieve both key and value in a dictionary:
knights = {"Gallahad": "the pure", "Robin": "the brave"}
knights.items()
for k, v in knights.items():
    print(k, v)

# To retrieve both position index and value in a sequence:
seq = ["Tic", "Tac", "Toe"]
for i, x in enumerate(seq):
    print(i, x)

word = "Python"
for i, l in enumerate(word):
    print(i, l)

tuple = (("A", "B"), ("C", "D"), ("E", "F"))
for i, l in enumerate(tuple):
    print(i, l)

# 5 - Conditions and Sequence comparisons.

# While and if can contain all operators, not just comparisons.
# For example, in and not in check if a value is in a sequence, and is and
# is not can check if two (mutable) objects are the same.
# Comparisons may be further combined using "not", "and" and "or", compared in
# that order: A and not B or C is the same as (A and (not B)) or C.
# And and Or are short-circuit operators: they are evaluated left to right and
# the evaluation stops as soon as a true relationship is found.

# Comparing sequences occurs in order. The first two items are compared, then
# the next, and so on. The comparison continues if the two items are the same
# and *immediately stops* if it finds a difference, returning that difference.
# Lexicographical ordering following the UNICODE convention is used to compare
# non-numbers.
# As long as the two objects have a comparison method defined, every type of
# object can be compared. If no method is present, TypeError is raised.

(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)  # The test is recursive

# These are all true.

[1, 2, 3, 100] < [1, 2, 4, 5]
# Same, Same, Smaller than -> Return True

[100, 1, 1, 1] < [1, 100, 100, 100]
# False -> Return False

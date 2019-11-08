# 1- Using Python as a Calculator

# Sum
2 + 2
# Division and floor division. Returns a FLOAT, returns an INT
17 / 3
17 // 3
# Multiplication / powers of
2 * 6
3 ** 5

# Variable Assignment

width = 12
height = 32
length = 1

width * height * length

# In interactive mode, the last result is stored in the variable "_"
# Other than INT and FLOAT, Python supports DECIMAL and FRACTION. Python also-
# has support for complex numbers, using "j" to denote the imaginary part.

# Using brackets is allowed in calculations:

((height + length) / width) + length

# Python normally follows the usual division and multiplication before addition
# and subtraction rule.

# 2 - Strings

# Strings are enclosed in "" or '', and ' or " are escaped with \
"I'm a string"
'I\'m a string'
"This is a \"Quote\""
'This is a "Quote"'
# Notice the escaped characters
# Using the function print() formats nicely strings, like by omitting the
# quotes they are enclosed in, and concatenating different numerals and
# strings together.

# \n denotes a newline.

length = 13
print("This is the length:", length, "\nIt is quite long.")
# Adding an "r" before the string denotes it as a raw string, escaping every
# character inside it.
print(r"This string is so raw")

# Strings can be concatenated with +, and repeated with *.
# This does not work if the string is inside a variable:

"I am a " + "banana, " + "and I am" + " very delicious."

# Strings are concatenated automatically when next to eachother:
"Hello, " "how are you?"

# This again doesn't work when strings are inside a variable.

# Strings are indexed from 0, and can be selected and sliced.
# Using negative numbers, they can be selected/sliced backwards.
# Strings are immutable: you cannot change them in any way after creation.

word = "Python"
word[0]  # P
word[1]  # Y
word[4]  # o

# In slicing, the START is included, the END is excluded.
word[1:3]  # yt

word[0:2] + word[2:6]  # Py + thon

# This is easy to visualize in this way:
#    0   1   2   3   4   5
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
# When slicing, the sliced part is inbetween the two selected indexes.
# Omitting an index automatically selects the start (0) or the end (len())
# of the word.
# Attempting to use and index too large while selecting results in an error,
# but while slicing, it selects the end or start of the word gracefully.

len(word)  # Len() returns the lenght of the string.


# 3 - Lists


# Lists can contain anything, and each object in a list is indexed just like
# a string. We can select and slice just like a string.
squares = [1, 4, 9, 16, 25]

squares[3]  # 16
squares[2:4]  # 9, 16
squares[:5]  # 1, 4, 9, 16, 25. Same as squares[:]

# All slice operations return a new list.
# Operations like concatenatoins and multiplications are also supported:
squares + [36, 49, 64, 81, 100]
squares * 2

# Lists are mutable, which means we can assign new values to ther selections
# and slices.

fibonacci = [1, 1, 2, 3, 7, 8, 13, 21]  # 7 is wrong, we need to change it to 5
fibonacci[4] = 5
fibonacci

fibonacci[:4] = ["A", "A", "B"]  # This changes 1,1,2,3,7 to "A","A","B"
fibonacci

# We can append objects to a list using the append() method.
fibonacci.append(34)
fibonacci

# len() can be used for lists too, and gives the number of items in the list.
# Lists can contain lists.

a = [1, 2, 3]
b = ["a", "b", "c"]
c = [a, b]
c

# Mutable and immutable objects are handled differently in the memory.
# By using id(), we can get the position of the object in the RAM. If an object
# is immutable, changing it also moves it in the memory to a new place.
# If an object is mutable, its position doesn't change.

text = "This is an immutable string"
textcopy = text
id(text)
id(textcopy)

# The "is" keyword checks wheter or not two objects are the same. It does so
# by comparing their id() positions. If they are the same, it returns True.

text is textcopy

text = "This is a completely new object"
id(text)
id(textcopy)

text is textcopy

mylist = [1, 2, 3]
newlist = mylist
id(newlist)
id(mylist)

mylist is newlist

mylist.append(4)

mylist is newlist

# 4 - Control Flow Tools

# WHILE - While this is true, do this.

a, b = 0, 1  # Notice the multiple assignment
while b < 1000:
    print(b, end=",")
    a, b = b, a+b

# IF - If this is true, do this. Else, if this is true, do this. Else, do this.

x = 12
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("More than one")

# There can be zero or more "elif"s, and "else:" is optional.

# FOR - For each item in something, do this.
words = ["Cat", "Window", "Defenestrate"]
for w in words:
    print(w, len(w))

# Since for loops can modify the list they are reading, sometimes it is useful
# to create new lists and then use those to read through:

for w in words[:]:  # This makes a new list, same as words, and uses that.
    if len(w) > 6:
        words.insert(0, w)
        print(words)

# To create a pseudo-list (an item that can be fed into a for loop) called an
# iterable object, we can use the range() function to create an artimetic
# progression. range(x through y, step length).

for i in range(5):  # Using a single value iterates from 0
    print(i)

# range creates a list of the index number of a list of length(x)

for i in range(10, 23, 4):
    print(i)

# range() Doesn't really create a list, it just makes an object that behaves
# like a list when iterated over.
# Using range(len(x)) can iterate over the indices of a sequence.
# enumerate() does the same thing.

# Other flow tools are break and continue.
# Break stops a loop entirely when it is executed, ending it immediately.
# Continue stops the current cycle of the loop, and moves on to the next.

# pass can be used to do nothing.

while True:
    pass


# 4 - User-defined functions

# We can define a function using the keyword def followed by name, then
# arguments inside a parenthesis:


def fib(x):
    """Print a fibonacci series up to x"""
    a, b = 0, 1
    while b < x:
        print(b, end=",")
        a, b = b, a+b


fib(1000)
# The return keyword returns the result of the function to other functions.
# A function with no return statement always returns None. None is not
# displayed, except for when using print().


def fib2(x):
    result = []
    a, b = 0, 1
    while b < x:
        result.append(a)
        a, b = b, a+b
        return result


fibonacci = fib2(1000)
print(fibonacci)

# The function-object type is a special one, evaluated by python as a user-
# define function. Calling it returns where the function is stored.

fib2

# A function can have default values:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)

# This function has "state", "action" and "type" have a default.
# A function can be called using positional references, or by naming each
# variable. Keyword arguments must always come AFTER positional ones, though.

parrot(500, "bereft of life", "Vooooom!", "Bangladesh yellow")
parrot(state="berefth of life", type="Bangladesh yellow", voltage=20)

# To check an input against many alternatives, the in keyword comes in handy:


def ask(x):
    while True:
        if x in ("y", "yes", "ok", "ye"):
            return True
        elif x in ("no", "n", "nop", "nope"):
            return False
        else:
            print("Input not recognized.")


# The default value is only evaluated once, at the start of the function.
# if the default is mutable by the function, it may change only in subsequent
# calls.

# If a function requires more than one argument, but has to be fed them by a
# variable which has them "bundled up" in a list, we can unpack them by using
# the * operator:

args = [1, 10]
list(range(*args))
# the list() function lists each item in an iterable object.
# If a dictionary has to e unpacked for a function, the ** operator can be used

d = {"voltage": "four million", "state": "bleedin' demised", "action": "voom!"}
parrot(**d)

# The lambda expression returns the sum of its two arguments. It can be used
# to retun a function:

# Usage: lambda a, b : a + b


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(12)
f(1)  # 12 + 1
f(12)  # 12 + 12

# 5 - Doc Strings

# The first line after the definition of a function should be a string.
# This string is called the docstring, and shuld sum up what the function does
# in a single line. After a blank line, more linescan be written, to detail
# the function's workings.

# Since docstrings are usually used by external programs to create documents,
# and the Python parser does not strip indentation inside a multi-line string,
# the indentation of the blank line betwen the first and third line defines
# the indentation to be stripped from the srtat of each line afterwards:


def nothing():
    """Do nothing, but document it.

    No, really, this does nothing. But notice the indentation"""
    pass

# The docstring can be extracted from a function by using print and the method
# __doc__:


print(nothing.__doc)

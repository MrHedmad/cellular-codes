########## 1- VECTORS ##########

# The entities that R creates (functions too), are called objects.
# To get a list of object created use objects()
# To remove (forever) a created object, use rm(OBJ1, OBJ2, ...)

# The basic data storage object is the vector
# The chain c() command creates a vector:

c(1,2,3,4,5) # vector containing the number 1 to 5
c("This is a vector", "Containing only", "Character entities")
c('I\'m very hungry') # Quotes are escaped with \, but \\ is printed as "\\".

# You can assign any object to a variable with "=" or "<-"/"->"

x <- c(1,2,3,4)
c(1,2,3,4) -> x # These are the same

#To print a variable simply type the variable name:

x # [1] 1 2 3 4 5

# A vector must contain the same type of data: Logic, Integer, Numeric, Char...
# To get the mode of the vector use mode(VECTOR)

mode(x)

# To check if a vector is in a certain mode, use is.MODE:

is.numeric(x) # TRUE
is.character(x) # FALSE
is.logical(X) # FALSE
is.double(x) # FALSE

# Trying to set a vector with mutiple modes will try to coerce the modes into -
# an acceptable one, or give out an error:

x <- c("name", 1, 2, 3, "Banana") # Everything is coerced into Char 
x # "name" "1" "2" "3" "Banana" 

x <- c(1, 3, 10+0i, TRUE) # Again, everything is a complex number now. TRUE = 1
x

# You can do basic math with vectors.
# A single number is, in fact, a vector with just a single element.

x <- c(1,2,3)
y <- c(4,5,6)

x + y # 5 7 9
x - y # -3 -3 -3
x * y # 4 10 18
x / y # 0.25 0.40 0.50
x %% y # 1 2 3 (x mod y)
x %/% y # 0 0 0 (integer division)
x ^ y # 1 32 729
x ** y # Same as ^

# Other basic functions are:

max(x)
min(x)
log(x) # Log with, by default, e as base.
exp(x) # Exp with, by default, e as base.
sqrt(x)
mean(x)

length(x) # 3

# -> -> GO LOOK UP WHAT THE RECYCLE RULE IS <- <-
# The recycle rule makes this happen:

c(1, 2, 3) + c(1:12)

# Vectors are "numbered". Each entry has an index number:

x <- c(4, 2, 7, 1, 5)

# Creates a vector with 5 entities, with index number:
# [1] 4 ; [2] 2 ; [3] 7 ; [4] 1 ; [5] 5
# Square brackets can be used to get determined entities out of an object:

x <- c("A", "B", "C", "D", "E")

x[1] # "A"
x[3] # "C"
x[c(1,4,3)] # "A" "D" "C"

# Negative index numbers will be excluded instead:
x[-(c(1,4,3))] # "B" "E"

# If vectors are named (See later), you can use the name to select them:

experiment1 <- c(100, 200, 12.2, 3)
names(experiment1) <- c("Cell count 1", 
                        "Cell count 2", 
                        "Growth Factor", 
                        "Bananas?")

experiment1[c("Bananas?", "Cell count 2")] # 3 200

# Vectors can be generated in various ways.
# Simple 1-entity vectors can be made without c():

x <- 2 # 2
x <- "Ciao" # "Ciao"
x <- -17+0.3i # Complex number - Note: sqrt(-17) is NaN, 
                                     # while sqrt(-17+0i) is computable.
# You can combine multiple vectors with c()

x <- c(1, 2, 3)
y <- c(4, 5, 6)

new.vector <- c(x, y) ; new.vector # [1] 1 2 3 4 5 6

# For number sequences, use A:B, like:
x <- 3:21 # Sequence of integers from 3 to 21, both included (3,4,5,6,...,20,21)
x <- 17:2 # (17,16,15,...,3,2)

# Generally, use seq(from, to, by, lenght.out, along.with, ...) {Do ?seq}

seq(f = 2, t = 4, by = 0.2) # [1] 2.0 2.2 2.4 2.6 2.8 3.0 3.2 3.4 3.6 3.8 4.0

# Or, similarly, rep(X, times)

x <- c(1, 2, 3)
rep(x, times = 5) # 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3

y <- c("A", "B", "C")
rep(y, each = 3) # "A" "A" "A" "B" "B" "B" "C" "C" "C"

# For stitching together characters, use paste(..., sep= " ")

paste(c("A", "T", "C", "G"), 1:5, sep = " banana ")
# "A banana 1" "T banana 2" "C banana 3" "G banana 4" "A banana 5"

# To get some random numbers following a normal distribution, use:

rnorm(n = 20, mean = 0, sd = 1) # Create 20 numbers from a Z

# Logic vectors contain either TRUE or FALSE (Don't use T or F)

logic <- c(TRUE, FALSE, TRUE, TRUE)
logic # TRUE FALSE TRUE TRUE

# Logical vectors can be created by conditions.
# > ; < ; >= ; <= ; == 

x <- 1:10
x > 8 # F F F F F F F F Tr Tr
x <= 2 # Tr Tr F F F F F F F F 

# Or by logical expressions, & (and), | (or), ! (not)

x > 2 & x < 6 # Where x is more than 2 and less than 6: F F Tr Tr Tr F F F F F

# You can use logic expressions to select stuff inside objects
# TRUE are kept, FALSE are omitted:

x <- c(1, 2, 3, 4, 5, NA, NA, 8, 9, NaN, 11)
x[!is.na(x)] # Is a new vector, with: 1 2 3 4 5 8 9 11

y <- c(1, NA, 3, NA, 5)
x[is.na(y)] # 2  4 NA  9 - Notice the recycling

# Missing values can be added by NA. Operations with NA return NA.
# "Not a Number" operations return NaN

Inf - Inf # NaN
0 / 0 # NaN

# is.NA() is TRUE for NA and NaN. is.NaN() is TRUE only for NaN
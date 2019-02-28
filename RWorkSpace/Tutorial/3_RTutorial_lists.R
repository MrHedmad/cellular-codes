###### 3- Lists ######

# A list is an object containing a collections of elements called components.
# A component may be of any mode or type, with no restriction.
# A list is created with the function list(COMP1, COMP2, COMP3, ...)

Lst <- list( c(1,2,3), 
             c("Banana", "Papaya"), 
             matrix(1:20, nr=5), 
             list(c("Inception"), array(1:15, dim=c(3,5))),
             array(1:30, dim=c(2,3,2)))

# Here, we form a list containing a numeric vector, a character vector, a matrix, -
# - another list, and an array.

# length() returns the number of (surface) components.

length(Lst)

# List components may be referred to with [[]].

Lst[[2]] # Returns the vector (as a vector)
Lst[[5]] # Returns the array (as an array)

# Elements inside a list's component can be called using [] after [[]]

Lst[[2]][2] # Returns a vector with "Papaya" inside.
Lst[[3]][3,4] # Returns a vector containing the [3,4] element (14 in this case).
Lst[[5]][1,3,2] # Returns a vector containing the [1,3,2] element of the array (11).

# New lists can be created from an already existing list with []

Lst[2] # Returns a LIST, containing the 2nd component of Lst.
Lst[c(1,4)] # Returns a LIST containing the 1st and 4th component of Lst.

# This said, [] and [[]] are very different. For example:
# You can sum a vector:

sum(Lst[[1]])

# But not a list:

sum(Lst[1]) # Error!

# To name a component inside the list, add it in as the list is created:

Lst <- list( some.numbers    = c(1,2,3), 
             some.characters = c("Banana", "Papaya"), 
             some.matrix     = matrix(1:20, nr=5), 
             some.inception  = list(c("Inception")),
             some.array      = array(1:30, dim=c(2,3,2)))
Lst # Try and look inside the list

# You can select a named item inside a named list using "$"
Lst$some.array # This is the same as:
Lst[["some.array"]]
Lst$some.inception

# You can change names after assigning them using names(Lst)[NUMBER]
names(Lst)[2] <- "Banana" # Change some.characters to Banana

# You can combine lists with c(), or add (or substitute) a specific element with index numbers:
Lst2 <- Lst
Lst1 <- Lst

longLst <- c(Lst1, Lst2)

longLst[5] <- list(c("I was once an array!"))

longLst # Try and look for the changed array!
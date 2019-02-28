###### 2- Arrays and Matrices #####

# Matrixes are bidimensional vectors, made of columns and rows.
# A matrix can only contain one type of element.
# A matrix is defined by a dimensional vector, which specifies its dimensions:

x <- c(1:20) # Matrices need to be created from a vector

dim(x) <- c(4,5) # dim(x) is the dimension vector of x.
                 # If set to two values, it defines x as a matrix.
                 # The numbers indicate ROWS, COLUMNS

# length(x) -must- be equal to prod( dim(x) ). 
# The elements of x are assigned columns-first.

length(x) == prod(dim(x)) # This must always return TRUE.

# To create matrixes easely, use 
# matrix(data = NA, nrow = 1, ncol = 1, byrow = FALSE, ...)

matrix(nr = 3, nc = 5) # This creates and empty (NA - filled) matrix of 
                       # 3 rows and 5 columns.
matrix(nr = 5, nc = 5, data = x) 
              # matrix() ignores the length(x) == prod(dim(x)) requirement.
              # If the vector is too short, the recycle rule applies.

# If one of nr or nc is not specified, then matrix() will generate it trying-
# - to fill it with every object in data = x only once.

# Matrices can be accessed by giving two index numbers:

x[1,3] # Always ROW, COLUMN
x[2,]  # Not giving an index selects the whole row or column
x[,4]

# Using subset() can be useful to select elements of a matrix or array.
# Use ?subset()
# If the matrix (or array) is named, one may access it using "[]":

colnames(x) <- paste(rep("X", 5), 1:5, sep="")
rownames(x) <- paste(rep("Exp", dim(x)[1]), c(1:dim(x)[1]), sep="") 
                                # Creative use of dim()!
x #Try and call x

x[,"X2"] # This returns a vector with column 2 inside
x["Exp1",] # This returns a vector with row 2 inside.
x["Exp3", "X5"]
x[c("Exp3", "Exp4"), "X3"]

# If a matrix has more than 2 dimensions it is called an Array. 
# Matrices are, in fact, 2-dimensional arrays.
# "dim" dimensional arrays are created by assigning dim(), - 
# or by the array() function.
# As before, assigning dim() needs to follow the -
# length(x) == prod(dim(x)) requirement.

x <- c(1:40)

dim(x) <- c(2,5,4)

array(x, dim = c(2,5,2))

# Value assignment and indexes for arrays are the same as matrices.

# Assigning names to dimensions larger than 2 is tricky:
# Change the value of dimnames(ARRAY)[[DIMENSION]], -
# - or just specift dimnames while using array().

named <- array( data     = 1:12,
                dim      = c(3, 3, 3),
                dimnames = list( c("A", "B", "C"), # column names...
                                 c("D", "E", "F"), # 
                                 c("G", "H", "I")
                                 ))

# If a vector and an array are multiplied, the element-by-element rule is followed.
# If a vector is longer than the array, an error occours.
# If the operation's arrays have different dim() attributes, an error occours.

# Linking of vectors or arrays can be done with rbind() or cbind().
# rbind() links rows together, cbind() binds columns.
# Binding two vectors will create an array.

a <- array("A", dim= c(2,3))
b <- array("B", dim= c(2,3))

cbind(a,b)
cbind(b,a) # Order is important.

rbind(a,b)
rbind(b,a) # ORDER IS IMPORTANT!

# As with vectors, we can put labels on columns and rows:

x <- array(1:12, dim=c(3:4))

rownames(x) <- c("Name 1", "Name 2", "Name 3")
colnames(x) <- c("Col 1", "Col 2", "Col 3", "Col 4")

x

# After setting names, we can use those instead of access numbers.

####### Working with arrays ######

# We can use basic math, as we've seen for vectors.
# If two matrixes are not of the same dimensions, math operations give an error.
# Matrix multiplication can be done using %*%.
# Using "*" is a element-by-element multiplication.

a <- array(1:20, dim = c(2,4))
b <- array(45:1, dim = c(2,4))

a+b ; a*b ; a / b ; a ^ b # Since a and b have the same dim(), this is doable.

c <- array(20:25, dim = c(3,2))

a + c ; b * c ; c ^ b # Error, error, error. 
                      # c has different dim() from either a or b.

# Applying a function to the array returns element-by-element results:

a <- array(1:6, dim=c(2,3))
mean(a)
prod(a)
log(a)

# To apply a function to each row or column, use apply()
# apply(array, MARGIN, FUN, ...) MARGIN is 1 for rows and 2 for columns.

apply(a, 1, sum)
apply(a, 2, sum)
apply(a, 1, prod)
apply(a, 2, mean)

  ###### Vectors ######

# Generate a vector X containing 3 numbers.

X <- c(1, 2.43, 54)

# Assing to X a vector containing 3 characters and print X.

X <- c("Comquats", "3.14", "Banana") ; X

# Generate a vector of 20 positive integers using seq() and assign it to X

X <- seq(from = 1, to = 20, by = 1)

# Calculate the mean, max and mix of X.

mean(X) ; max(X) ; min(X)

# Sum X to Z, a vector containing 20 4s. Use rep() to generate Z.
# Assign the result to K.

Z <- rep(x = 4, times = 20)
K <- Z + X

# Sum two vectors of different lengths and explain the result, -
# mentioning the recycling rule.

c(1, 2, 3) + c(1:12) # The first vector is recycled four times.

# Create two different vectors and concatenate them together in the variable G.

G <- c(c(3, 7, 12, 3),
       c(1, 9, 13, 4, 20))

# Order the variable G and assign it to F

sort(G) -> F

# Calculate the logarithm and the square root of the elements in F

log(F)
sqrt(F)

# Generate a vector containing the first 20 integers (using :) and assign it to X

X <- 1:20

# Generate a numeric vector x of four values. Assign the names cell1, cell2...
# To each element. Print the elements using names(). Assign to the second - 
# element the value 5 using as index its name. Change the names of the vector -
# to first, second...

x <- 1:4
names(x) <- c(paste(rep("cell", 4), 1:4, sep = ""))
names(x)
x["cell2"] <- 5
names(x) <- c("first", "second", "third", "fourth")

# Assign a 10 elements vector to z. Reduce z's lenght to 7 using one -
# assignment. Use length() to actually see if the length has varied.

z <- 1:10
length(z) <- 7
length(z)

# Generate a vector containing 100 numbers generated in a normal fashion. 
# Assign all elements except 10 and 90 in the variable y.

y <- rnorm(100)[-c(10, 90)]

# Generate a vector containing 1000 numbers with an uniform distribution from 10 -
# to 20 using runif(). Select the cells containing values from 15 to 18 and -
# save them into a vector k. Show the length of k.

k <- runif(1000, min = 10, max = 20)
k <- k[k >= 15 & k <= 18]

length(k)

# Change the values in the first three cells in k to 1, 2, 3, using only one -
# command.

k[c(1,2,3)] <- c(1,2,3)


###### Matrices ######

# Create a 10x10 matrix with the first 100 integers using both the array() and -
# matrix() functions.

matrix(1:100, ncol = 10, nrow = 10)
array(1:100, dim = c(10,10))

# Create the same matrix, but arranging the values by row, and not by column.

matrix(1:100, ncol = 10, nrow = 10, byrow = TRUE)

# Create a matrix by using cbind and rbind from three vectors of the same length.

x <- 1:5 ; y <- 6:10 ; z <- 11:15

cbind(x,y,z)
rbind(x,y,z)

# Create two square matrixes and calculate the following: sum, difference, -
# product.

mat1 <- matrix(1:9, ncol = 3) ; mat2 <- matrix(9:17, ncol = 3)

mat1 + mat2 ; mat1 - mat2 ; mat1 * mat2

# Calculate the sum by row and by column of the first square matrix.

apply(mat1, 1, sum) # rows
apply(mat1, 2, sum) # columns

# Calculate max by row and by column of the second square matrix.

apply(mat2, 1, max)
apply(mat2, 2, max)

# Try accesing the elements of a matrix by using both psitive and negative -
# index numbers.

mat1[-1,-2] ; mat2[1,] ; mat1[,-3]

# Generate 100 numbers using rnorm, then create a 10x10 matrix, a 2x5x10 array -
# and a 5x10x2 array.

x <- rnorm(100) ; y <- rnorm(100) ; z <- rnorm(100)
dim(x) <- c(10,10) ; dim(y) <- c(2,5,10) ; dim(z) <- c(5,10,2)
x ; y ; z

# Using the following matrix:

  conc <- c(0.02, 0.02, 0.06, 0.06, 0.11, 0.11, 0.22, 0.22, 0.56, 0.56, 1.10,
           1.10, 0.02, 0.02, 0.06, 0.06, 0.11, 0.11, 0.22, 0.22, 0.56, 0.56,
           1.10)
  rate <- c(76, 47, 97, 107, 123, 139, 159, 152, 191, 201, 207, 200, 67, 51, 84, 
           86, 98, 115, 131, 124, 144, 158, 160)
  state <- c(rep(1, 12), rep(0, 11))

  cbind(conc, rate, state) -> data

# Create two matrices, once called "T" containing treated cells (state = 1), and
# another called NT with untreated cells (state = 0).

T <- subset(data, data[,3]==1)
NT <- subset(data, data[,3]==0)

# Calculate the mean of "rate" of the two matrices, then calculate the mean of -
# "rate" of all cells with "conc" between 0.02 and 0.11 in both matrices.

mean(T[,2])
mean(NT[,2])

mean(subset(T, T[,1] >= 0.02 & T[,1] <= 0.11)[,2])
mean(subset(NT, NT[,1] >= 0.02 & NT[,1] <= 0.11)[,2])


###### Data Frames ######

# Load the defualt data frame "Formaldehyde" from R data banks, and visualize
# its contents.

data("Formaldehyde")
Formaldehyde

# Use the $ operator to select the "carb" variable.

Formaldehyde$carb

# Use the [] operator to select the first row.

Formaldehyde[1,]

# Use the summary and str functions on the data frame.

summary(Formaldehyde)
str(Formaldehyde)

# Load and visualize the data frame "CO2" from R data banks, then select the -
# values in which "Type" equals "Missisipi" and "Treatment" equals "chilled".
# Save the selected values in the variable M.

data("CO2") ; CO2
subset(CO2, CO2$Type == "Mississippi" & CO2$Treatment == "chilled") -> M

# Calculate the max, sd and mean of the coloumn called "conc" of the variable M.

max(M$conc)
mean(M$conc)
sd(M$conc)

# Add to the M data frame a new coloumn with 21 numbers from a negative -
# exponential distribution with a rate of 3.

cbind(M, rexp(21, rate = 3)) -> M

# Using the following data frame:

data <- data.frame(
  "Dati:" = c(paste("Dato", 1:8, sep = "")),
  val.num = c(3.45, 5.67, 1.45, 4.56, 8.09, 3.11, 1.40, 7.73),
  val.car. = c("ATTA", "TGAT", "TATA", "TGAG", "CCCG", "CATG", "TGAG", "GGAC"),
  val.log. = c(TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE),
  val.num = c(0.45, 0.91, 3.78, 8.03, 8.09, 4.56, 1.80, 5.90),
  val.car = c("CCAT", "TATT", "CCCC", "GAGA", "AGAG", "ATAT", "GCTA", "TGAT")
)

# Extract from it the last column and the rows for which the values in the -
# fifth column are greater than 2. Add a new column in the data frame -
# containing the sum by row of the second and fifth columns.

data[, 6]
subset(data, data$val.num.1 > 2)


###### Lists #####

# Create a list called "li" containing a 4x4 numeric matrix, a character vector -
# containing 32 elements, a string containing "topo", and another list -
# containing a numeric vector with 10 elements and the logic value FALSE.

li <- list(
  matrix(1:4, ncol = 2, nrow = 2),
  paste("A", 32),
  "topo",
  list(
    1:9,
    FALSE
  )
)

# Extract from the following list:

li<-list(m=matrix(rnorm(64),nrow=8),s=c(rep("T",3),rep("G",5)))

# The second column of the matrix and the "G"s in the vector. Then, add to the
# list a vector containing 10 random numbers.

li$m[,2] ; li$s[li$s == "G"]

li[[3]] <- rnorm(10)


##### Read & Write #####

#' Build a data frame called D1, of 4 rows, with 8 variables, of which 4 numeric
#' ones and 4 strings. Save this data frame in a file. Read this file, and 
#' assign its contents to the variable D2.

D1 <- data.frame(
  c(1, 2),
  c(3, 4),
  c("Banana", "Papaya"),
  c("Guava", "Potato")
)

write.table(D1, file = "MyDataframe.txt")
D2 <- read.table(file = "MyDataframe.txt")

#' Write on a file the dataframe D1, but using "," to separate decimal places 
#' and assign a name to each variable (using paste).

write.table(D1, file = "MyDataframe.txt", col.names = paste("Num", 1:4), sep = "")

#' Optional: Create with a text editor a file, then read it using read.table.

#' Read the built-in dataframe Titanic, analyze it using str() and summary(), -
#' then save it in both a text file called Titanic.txt, and in a binary file -
#' called Titanic.bin.

data("Titanic")
str(Titanic)
summary(Titanic)

write.table(Titanic, file = "Titanic.txt")
save(Titanic, file = "Titanic.bin")

##### Plots #####

# No excercises for plots.
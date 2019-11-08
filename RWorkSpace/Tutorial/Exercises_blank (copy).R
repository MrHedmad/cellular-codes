###### Vectors ######

# Generate a vector X containing 3 numbers.



# Assing to X a vector containing 3 characters and print X.



# Generate a vector of 20 positive integers using seq() and assign it to X



# Calculate the mean, max and mix of X.



# Sum X to Z, a vector containing 20 4s. Use rep() to generate Z.
# Assign the result to K.



# Sum two vectors of different lengths and explain the result, -
# mentioning the recycling rule.



# Create two different vectors and concatenate them together in the variable G.



# Order the variable G and assign it to F



# Calculate the logarithm and the square root of the elements in F



# Generate a vector containing the first 20 integers (using :) and assign it to X



# Generate a numeric vector x of four values. Assign the names cell1, cell2...
# To each element. Print the elements using names(). Assign to the second - 
# element the value 5 using as index its name. Change the names of the vector -
# to first, second...



# Assign a 10 element vector to z. Reduce z's lenght to 7 using one -
# assignment. Use length() to actually see if the length has varied.



# Generate a vector containing 100 numbers generated in a normal fashion. 
# Assign all elements except 10 and 90 in the variable y.



# Generate a vector containing 1000 numbers with an uniform distribution from 10 -
# to 20 using runif(). Select the cells containing values from 15 to 18 and -
# save them into a vector k. Show the length of k.



# Change the values in the first three cells in k to 1, 2, 3, using only one -
# command.




###### Matrices ######

# Create a 10x10 matrix with the first 100 integers using both the array() and -
# matrix() functions.



# Create the same matrix, but arranging the values by row, and not by column.



# Create a matrix by using cbind and rbind from three vectors of the same length.



# Create two square matrixes and calculate the following: sum, difference, -
# product.


# Calculate the sum by row and by column of the first square matrix.



# Calculate max by row and by column of the second square matrix.



# Try accesing the elements of a matrix by using both psitive and negative -
# index numbers.



# Generate 100 numbers using rnorm, then create a 10x10 matrix, a 2x5x10 array -
# and a 5x10x2 array.



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



# Calculate the mean of "rate" of the two matrices, then calculate the mean of -
# "rate" of all cells with "conc" between 0.02 and 0.11 in both matrices.




###### Data Frames ######

# Load the default data frame "Formaldehyde" from R data banks, and visualize
# its contents.



# Use the $ operator to select the "carb" variable.



# Use the [] operator to select the first row.



# Use the summary and str functions on the data frame.



# Load and visualize the data frame "CO2" from R data banks, then select the -
# values in which "Type" equals "Missisipi" and "Treatment" equals "chilled".
# Save the selected values in the variable M.



# Calculate the max, sd and mean of the coloumn called "conc" of the variable M.



# Add to the M data frame a new coloumn with 21 numbers from a negative -
# exponential distribution with a rate of 3.



# Using the following data frame:

data <- data.frame(
  "Dati:" = c(paste("Dato", 1:8, sep = "")),
  val.num = c(3.45, 5.67, 1.45, 4.56, 8.09, 3.11, 1.40, 7.73),
  val.car. = c("ATTA", "TGAT", "TATA", "TGAG", "CCCG", "CATG", "TGAG", "GGAC"),
  val.log. = c(TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE),
  val.num = c(0.45, 0.91, 3.78, 8.03, 8.09, 4.56, 1.80, 5.90),
  val.car = c("CCAT", "TATT", "CCCC", "GAGA", "AGAG", "ATAT", "GCTA", "TGAT")
)

# Extract from it the last coloumn and the rows for which the values in the -
# fifth coloumn are greater than 2. Add a new coloumn in the data frame -
# containing the sum by row of the second and fifth columns.




###### Lists #####

# Create a list called "li" containing a 4x4 numeric matrix, a character vector -
# containing 32 elements, a string containing "topo", and another list -
# containing a numeric vector with 10 elements and the logic value FALSE.



# Extract from the following list:

li<-list(m=matrix(rnorm(64),nrow=8),s=c(rep("T",3),rep("G",5)))

# The second column of the matrix and the "G"s in the vector. Then, add to the
# list a vector containing 10 random numbers.



##### Read & Write #####

#' Build a data frame called D1, of 4 rows, with 8 variables, of which 4 numeric
#' ones and 4 strings. Save this data frame in a file. Read this file, and 
#' assign its contents to the variable D2.



#' Write on a file the dataframe D1, but using "," to separate decimal places 
#' and assign a name to each variable (using paste).



#' Optional: Create with a text editor a file, then read it using read.table.

#' Read the built-in dataframe Titanic, analyze it using str() and summary(), -
#' then save it in both a text file called Titanic.txt, and in a binary file -
#' called Titanic.bin.



##### Plots #####

# No excercises for plots.


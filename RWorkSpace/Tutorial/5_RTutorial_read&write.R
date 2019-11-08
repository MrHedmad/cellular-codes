###### 5. Read and Write files ######

# You can easely read data from a file.
# The files must be in the workspace by default, or their path has to be -
# specified. 
# Using read.table(file="FILENAME"), you can read a text file and save the data-
# frame inside. The formatting for the data frame is strict:

read.table("Myfile.txt")

# By default:
# The first line contains the name(s) of the column(s), separated by spaces.
# The second line and further lines start with the name of the line, -
# then the line's values, separated by spaces. Decimals are separated with dots.
# The lastline of the file must be an empty line (add a new line after the last).
# Note: All char strings are quoted in the file too ("Banana")

myDF <- data.frame(matrix(1:40, nrow = 5))

# To store in a (correctly formatted) file this "myDF" data frame, use:

write.table(myDF, file="MyDataframe.txt")

# Additional arguments (used in both write. and read.table) can specify what -
# separator and decimal separator to be used.
# sep = " ", and dec = "." 
# Use ?read.table for more info.

write.table(myDF, file = "MyDataframe.txt", sep = "-", dec = ":")

# This writes a table using "-" as separator and : as decimal separator.
# We can also write names in our file, which can be then read using row.names -
# and/or col.names:

write.table(myDF, file = "MyDataframe.txt", row.names = paste("A", 1:8, sep = ""))

# col.names and row.names can also be TRUE or FALSE. If they are TRUE, then R
# will search for col/row names in the file, or write col/row names already - 
# assigned to the variable. If they are FALSE, then R will ignore them as it -
# writes or reads them.

read.table(file = "MyDataframe.txt", row.names = FALSE)

# To read MyDataframe.txt we need to specify sep and dec:

read.table(file = "MyDataframe.txt", sep = "-", dec = ":")

# read.table() needs to be assigned into a variable to be stored.

# We can also use save() and load() to save a variable (and it needs to be a -
# variable), in a binary file.

foo = c(1.00, 2.40, 3.10, 4.56, 12.00)
save(foo, file = "foo.bin")
load(file = "foo.bin")

# Load returns the name of the variable loaded, in this case "foo", NOT the -
# content of the variable that is loaded.

myvar <- load(file= "foo.bin")
myvar ; foo # This returns a vector "foo", but the variable foo is still loaded
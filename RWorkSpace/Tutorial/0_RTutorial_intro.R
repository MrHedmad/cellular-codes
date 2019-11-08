###################################
#########   R Tutorial    #########
###################################

# NOTE ON GUIDE FORMATTING
# Comments that exceed 80 characters per line are usually stopped with a -
# and then resumed at the next line.

# R is a high-level programming language, mostly used in statistical computing.
# Comments are signaled in the code by adding a "#" beforehand.
# Comments are not run. R simply ignores what is after a # (until a new line).

# On a command prompt, open the R console using the command "R".

# The console allows for interactive use of R.
# The default console prompt is ">". If a command is detected to be incomplete,
# a "+" prompt will appear, until the command is completed.
# Esc escapes from the + prompt. 

my.variable <- list(c("I'm some text"), c(1, 2, 3, 4))
my.variable
mean(my.variable[[2]]) -> my.mean ; my.mean # Notice the semicolon

# Running more than one command per line is allowed, if they are separated - 
# with a semicolon ";".

# Spaces are completely ignored by R.

# Help is available for most functions.
# You can get help by using ? or ??

?median
??logarithm

# ?FUN gets help for the specific function FUN
# ??QUERY serches the manual for QUERY

# The workspace (or working directory, W.D.) is where R stores data it creates.
# To change the W.D. use wd()

setwd("c:/Users/Luca/RWorkspace")

# Note the use of forwardslashes instead of backslashes.
# To get the curred W.D. use

getwd()

# R stores information like variables created and command history at the end of-
# the session in a file called .RData and .RHistory, saved in the W.D.

# In RStudio, to change the default working directory, go to:
# Tools > Global Options > General and change the default path.
# Files are read ond wirtten from / to the W.D. (See "Writing and reading files")

# R is case-sensitive. A and a are different characters.

a <- c("This is the variable a") ; a
A <- c("This is a new variable A") ; A

# For all intents and purposes, A and a are two different objects.

###### FUNCTIONS & ASSIGNMENTS ######

# A function is a set of directions that R follows to get a result.
# A function can be called with FUN_NAME( arg1, arg2, arg3, ...)
# FUN_NAME is the name of the function, while arg1,... are its arguments.
# A function RETURNS its result after it is run.

rep(x = 1:3, times = 4)

# In this case, we use the function named rep, which repeats its "x" argument -
# a "times" times. 

# We can omit the name of the arguments if we follow the order of the arguments
# as shown in ?rep()

?rep() # We see that the default order is rep(x, times)

rep(x = 1:3, times = 3) # These three are the same
rep(1:3, 3)             # 
rep(times = 3, x = 1:3) # We can change the order of the args, if we specify them.

# Commands can be nested inside eachother. R will run them in the correct order
# that is, from the inner-most to the outer-most.

sum( rep(1:5, 5) ) # This runs rep(), then sum() on whatever rep() returned.

# We can assign what a function returns to a variable for storage.
# After we assign, calling the variable will be the same of running the function.
# The assigment operator is <- (or ->). = is the same as <-, but <- is preferred.

x <- rep(1:5, 5) # Assignments don't return anything in the console (if working)
sum(x)           # This is the same as sum( rep(1:5, 5) ) from before.

x # Just writing the variable name will print its contents out.

###### OBJECTS ######

# All variables (called "objects") can be listed with objects() or ls()

objects()

# Every object, even what is printed with "objects()", is itself an object.
# If an object is not assigned as it is created, it is printed out and then lost.

# We can remove assigned objects using rm()

x <- c("Banana", "Papaya", "Guava") 
y <- c(1, 2, 3, 4, 5)

objects()

rm("x") # This will delete (PERMANENTLY) the object x from the environment.

# Objects have a set of characteristics:
# mode() shows us what type of data is inside the object.
# This can be "numeric", "logical", "character", "list"...

mode(y) # Since y is a set of numbers, this returns "numeric".

# As we will see later, we can set additional attributes to out objects.
# The names() is a type of attribute. We can list user-set attributes with:

attributes(y) # Since we set none, it returns NULL

# You can get what type of data structure (more or less) an object is:

class(y) # This returns "numeric"
class(data.frame(y)) # This returns "data.frame" as data.frame(y) is a data frame.

# Functions are objects too!
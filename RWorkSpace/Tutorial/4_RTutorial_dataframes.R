###### 4- Data frames ######

# A data frame is a list, with class "data.frame".
# A data frame is, more or less, a matrix, but without the type restriction.
# A list which components are exclusively vectors (of any type), factors, -
# -numeric matrices, lists, or other data frames can be made into a data frame.

# NOTE: Vectors in the list must all have the same, or multiple of the same, length(). 
# NOTE: Matrices in the list must all have the same, or multiple of, number of rows.

# NOTE: While creating a data frame, a character vector will be coerced into a factor.
# See Appendix A for more information on factors.

# We can create a data frame using the function data.frame()

Lst <- list( X1 = c(1,2,3,4,5),
             X2 = c(1,2,3,NA,"Guava"),
             X3 = c("Null",2,3,4,NaN),
             X4 = c("Papaya", "Banana", "Guava", "2", 123)
            )
              # X1, X2, X3 and X4 have all the same length (5)!

Dframe <-  data.frame(Lst)
Dframe # Try and print the Data frame out. See how data.frame fills in columns first.

# Let's try and use matrices and vectors, and make R need to use the recycle rule:
# NOTE: you can skip creating a list before turning it into a dataframe. -
# data.frame() will do that for you.

Dframe <- data.frame( X1 = c(1,2,3,4,5,6),
                      X2 = matrix(1:4, nr = 2, nc = 2),
                      X3 = matrix(1:2, nr = 1, nc = 2),
                      X4 = c("A", "B", "C")
                      )
# Here, X1 gives 6 as length, so the others, being 6 a multiple of their length, - 
# conform as such: X2 is tripled, X3 is sixtupled, X4 is doubled.

# You can select, set, view ... in data frames in the same way we did for matrices.
# Names are set using colnames() and rownames(), same as matrices.
# Names can be viewed, again, with colnames() and rownames().

# You can select stuff using $, same as matrices. ($ selects columns!)
# subset() is also an option, and it's used in the same way as matrices.

# str() can be used to see a little snipped of data inside an object.
# NOTE: some pre-made data frames will be used here, data(name) loads them.

data(iris)
str(iris)

# In Rstudio, str() info can also be seen in the Environment tab.
# summary() is also a way to get a more detailed snippet of information:

summary(iris)

# To select something from a data set, use subset()
# subset(dataset, logical statement)

data(CO2)
subset(CO2, CO2$Type == "Quebec")
subset(CO2, CO2$Type == "Quebec" & CO2$Treatment == "nonchilled")

data(iris)

iris
head(iris)
str(iris)

iris[,"Sepal.Length"]
iris[c(1,12,34),c(1, 4)]
iris$Sepal.Length[c(1,12,34)]

min(iris$Petal.Length)

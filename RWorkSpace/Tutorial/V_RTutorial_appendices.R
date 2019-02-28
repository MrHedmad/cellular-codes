###### Appendix A - Factors ######

# A factor is a collection of data, where each element is called a level.
# A very large factor containing few levels can be more cheapely stored in memory.
# Factors can be created from a vector using factor()

x <- c(1,1,1,1,2,2,2,3,3,3,3,1,1,1,2,1,1,3,3,3,3,3,1,1,1,1,2,2,2,3,3,3,3,2,2,1,2,2,1,1,1)

fx <- factor(x)

fx # Printing out the factor specifies its levels

# Factors are very important when it comes to statistical computing, namely model formulae.
# A factor, though, is different from a vector, since the level's names are stored.
# Thus, mean(fx) will return an error. To return from a factor to a vector, use as.numeric()

mean(fx)

mean(as.numeric(fx))

# Note that as.numeric() is touchy. Be careful.

# Example on how to use a factor:
# Let's say we have a vector containing the values of a certain experiment.
# In this experiment, cells have been randomly modified to have:
# More expression of a certain factor ("more"), less of the same ("less"), or no change ("same").

# We stored this data in an ordered form, from sample 1 to sample 10:

sample.type <- c("same", "same", "more", "same", "less", "more", "less", "more", "more", "less")

# We also stored, in the same order, the cell counts:

sample.count <- c(120, 112, 320, 125, 61, 118, 73, 280, 250, 69)

# Now,we'd like to know some parameters of each type of modified cells. We can:

f.sample.type <- factor(sample.type)  # First turn the sample types into a factor,
sample.means <- tapply(sample.count, f.sample.type, mean)

# tapply() applies a certain function to each group of the first argument, -
# defined by the levels of the second argument.

sample.means # We print out the result

# Any sensible function can be applied this way:

tapply(sample.count, f.sample.type, max)
tapply(sample.count, f.sample.type, min)


library(ggplot2)

data <- read.csv('~/Documents/Projects/cellular-codes/PythonCode/.results.csv')
head(data)
data[1] <- NULL
data = data[-1,]

head(data)

hist(data$one_d20, breaks = 0:20)
hist(data$three_d6, breaks = 2:18)
hist(data$weighted_three_d6, breaks = 2:18)
hist(data$weighted_d20, 0:20)
hist(data$mean_d20, 0:20)
hist(data$five_d4, 4:20)
hist(data$two_d10, 1:20)
hist(data$d10_d8, 1:18)

means <- lapply(data, mean)
sds <- lapply(data, sd)

getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

modes <- lapply(data, getmode)
medians <- lapply(data, median)

stats <- cbind(means, sds, modes, medians)

t.test(data$weighted_three_d6, data$five_d4)

# Introduction to statistical learning chapter 2 exercises

library("ISLR")

# Exercise 8
fix(College)
summary(College)
pairs(College[,1:10]) # This is unreadable tho!
pairs(College[,1:5]) # Same as plot(College[,1:5])

plot(College$Outstate, College$Private)

Elite <- rep("No", nrow(College))
Elite[College$Top10perc > 50] <- "Yes"
Elite <- as.factor(Elite)
College2 <- cbind(College, Elite)
summary(College2)
plot(College2$Outstate, College2$Elite)

par(mfrow=c(2,2))
hist(College$Accept)
hist(College$Outstate)
hist(College$PhD)
hist(College$Books)

par(mfrow=c(1,2))
percAccepted <- College$Accept/College$Apps
percEnrolled <- College$Enroll/College$Apps
boxplot(percAccepted, ylim = c(0, 1), main = "Accepted")
boxplot(percEnrolled, ylim = c(0, 1), main = "Enrolled")

par(mfrow=c(1,1))
boxplot(cbind(percAccepted, percEnrolled), ylim = c(0, 1))

# Exercise 9

fix(Auto)

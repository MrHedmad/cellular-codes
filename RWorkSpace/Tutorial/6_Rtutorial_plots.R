###### Plots ######
 
# We can create plots using high-level functions, that create a new plot -
# from a set of data. Once created, we can add "pieces" to the plot using -
# low-level functions.

# Interactive functions can add or get data from a plot.
# Using

demo(graphics)

# gets us some example plots we will be able to create.

# x11() can create additional windows on where to see plots. 
# RStudio has a "plot" window to show us created plots.

# Some high functions are:

plot() # This can crate many different plots.

qqnorm()
qqplot() # All these three can be used to confront different distributions.
qqline()

hist() # For histograms.
barplot() # For a barplot.
pie() # Pie charts.

# Let's see what plot() can do.

x <- rnorm(100)
y <- rnorm(100)

plot(x) # This plots a scatterplot with x as the "Y" axis, and the index of x
        # as the "X" axis.

x <- -10:10
y <- x^3 - 3*x -10

plot(x,y)

# Let's say we want to add to that simple plot a line that links all points.
# We can use type = "..." ... can be p for points, l for lines, b for both...
# Use ?plot for a list.

plot(x,y, type = "b")
plot(x,y, type = "l")

# To label our axis, use xlab="mylabel" and ylab="mylabel"

plot(x,y, type = "b", xlab="X axis", ylab="Y axis")

# To title a plot, use main = "plotname"

plot(x,y, main="My awesome plot!")

# plot() works also for datasets:

plot(iris)

# These plots can be read by assigning x/y axis information to what is said -
# in the diagonal. Note that plots as symmetrical to the diagonal, since -
# simmetrical plots are the same plots but with x/y axes switched.

# We can create boxplots using boxplot()
# A boxplot shows us many things. The "wigs" are max and min.
# The upper and lower lines are the 3rd quartile and 1st quartile (75% and 25%).
# Dots over and below the two wigs are outliers.

boxplot(iris[c(1,2)], col = c("red", "blue")) 

# This command takes the first 2 columns of iris and plots them in a boxplot, 
# setting the color of the first box to "red" and the second to "blue".

# hist() creates an histogram from supplied data.

hist(iris[[2]])

# Using lines() can add lines to an already plotted plot():

z <- 20*(x^2)

plot(x,y, main= "My plot!", type = "b") # col can be used to color lines too!
lines(x,z, type = "b", col = "red")

# Some data may be "cut" in a plot, since the x and y axes are not "reset" -
# when a new line is added. In the above example, the values of the line -
# after 7 and before -7 are "cut". If we inverse the order:

plot(x,z, main= "My plot!", type = "b")
lines(x,y, type = "b", col = "red")

# Now the whole of "z" is shown, but "y" is cut.
# To fit the new line in the graph, specify max and min of the axes when you -
# create the plot:

plot(x,y, type = "b", ylim = c(-2000, 2000))

lines(x,z, type = "b", col = "red")

# Now everthing fits inside our plot nicely. We can also use min() and max()
# to automatically calculate the boundaries of our plots.

# Similarly to lines(), other low functions can be used to modify a plot:

x <- 1 ; y <- 2

lines()
points(x,y) # Adds a point in x,y
text(x,y, label = "Banana") # Adds text in the coordinates x,y
abline(a,b) # Adds a line of inclination a that intercepts b.
polygon(x,y,z,...) # Adds a polygon with vertices x,y,z...
legend(x,y,legend) # Adds a legend at the x,y coordinates
title(main, sub) # Adds a main title and a sub subtitle
axis(side,...) # Adds a new axis in the "side" position

# A complete example:

x=1:40
y=x^2
z=x^2+3*x # Setting some variables

plot(x,y,t="l") # Create the plot

lines(x,z,col="red") # Add a red line, with x and y coordinates.

points(40,500,col="blue",t="p") # Add a single blue point @ 40,500 
                                # t="p" specifies to its "point" type

text(20,1000,"Label",col="green") # Add a green "label" @ 20, 1000
                                  # 20, 1000 are its top-left coordinates

polygon(c(10,20,30),c(1000,1200,1500),col="pink")
                                # Add a pink polygon, of vertices 10,1000 ;
                                # 20,1200 ; 30, 1500

legend(10,1500,              # Add a legend @ top-left coordinates 10,1500,with
       c("Line 1","Line 2"), # two line types of names "Line 1" and "line 2",
       lty=c(1,1),           # of line types (lty) 1 and 1, 
       col=c("red","black")) # of colour red and black.

title("Test1") # Set the title of the plot to "Test1"

axis(4, col = "gold", lty = 2, lwd = 0.5) # Add a new axes, of linetype 2

# Other useful variables are pch = x, to set what type of dot is displayed

# To save a plot, before starting to create a plot, tell R to save the next -
# commands in a file, instead of a graphical interface.

jpeg("mygraph.jpg") # or png()

plot(y) # All the plot stuff goes here

dev.off() # This tells R that the plot creation is complete, 
          # and the file needs to be saved to what was specified in jpeg()
          # Each jpeg() needs to be closed with its own dev.off()
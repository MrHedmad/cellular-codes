library("devtools")
library(roxygen2)

setwd("C:/Users/hedma/Data/RWorkSpace/mypackage") ; document()

setwd(".."); install("mypackage")

library("mypackage")

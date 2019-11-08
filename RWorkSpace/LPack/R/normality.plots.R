#' Normal qqplots for more than one variable
#'
#' This function allows you to create many qqnorm plots at once, with qqlines added.
#' @param x A data.frame with the variables to plot.
#' @param rows The number of rows the plots need to be arranged in. Default = 1
#' @keywords qqplot qqnorm qqline plots normality
#' @export
#' @examples
#' norm.plot()

norm.plot <- function(x, rows = 1){
  if(length(names(x)) > 10){
    stop("Too many plots to show!")
  }
  if(rows > length(names(x))){
    stop("Rows is too large!")
  }
  if(!length(names(x))%%rows == 0){
    stop("Rows is not a multiple of variable length!")
  }
  col <- floor(length(names(x))/rows)
  par(mfrow=c(rows, col))

  plotting <- function(x, num){
    qqnorm(x, main = num)
    qqline(x)
  }
    for(i in names(x)){
  lapply(x , plotting, num = i)
    }
  invisible()
}

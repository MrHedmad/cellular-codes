#' Analizing a quantitative variable
#'
#' This function shows length, summary, sd and CV of the variable.
#' @param x A vector or data.frame with the variables to analize.
#' @keywords summary analize
#' @export
#' @examples
#' analize()

analize <- function(x){
  return(c(length = length(x),
           summary(x),
           sd = sd(x),
           CV = CV(x)
  ))
}

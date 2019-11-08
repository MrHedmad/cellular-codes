#' Variance coefficent
#'
#' This function calculates the variance coefficient, sd / mean.
#' @param x A vector or data frame to calculate the variance coefficent.
#' @keywords coefficient
#' @export
#' @examples
#' CV()

CV <- function(x){
  return(sd(x, na.rm = TRUE)/mean(x, na.rm = TRUE))
}

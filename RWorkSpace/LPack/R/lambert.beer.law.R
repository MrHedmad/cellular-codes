#' Lambert-Beer Model Application
#'
#' Create an Absorbance-Concentration plot
#' @param conc A vector containing the standard curve concentration.
#' @param abs A vector containing the standard curve absorbance.
#' @param inter A logical value: if FALSE, intercept is set to 0, otherwise intercept is calculated. Defaults to FALSE.
#' @keywords Lambert-Beer concentration absorbance
#' @examples c -> c(5, 10, 20, 40); a -> c(0.258, 0.489, 0.896, 1.429)
#' lb.model(c, a, TRUE)
#'

lb.model <- function(conc, abs, inter = FALSE){
  plot(conc,abs, xlab = "Concentration", ylab = "Absorbance", main = "Absorbance-Concentration Correlation")
  cor.test(conc,abs) -> cor
  # Calculate or not the model with the intercept
  if(inter == FALSE){
      lm(abs~conc-1) -> mo
      print("Intercept set to 0", quote = FALSE)
      print(c("Coefficient is", round(as.numeric(mo$coefficients), 5)),
            quote = FALSE)
  }else{
    lm(abs~conc) -> mo
    print(c("Intercept is", round(as.numeric(mo$coefficients[1]), 5)),
          quote = FALSE)
    print(c("Coefficient is", round(as.numeric(mo$coefficients[2]), 5)),
          quote = FALSE)
  }

  abline(mo)
  print(c("Model quality (R-squared):", round(as.numeric(cor$estimate), 5)),
        quote = FALSE)

  invisible()}

curva <- data.frame(
  conc = c(0, 5, 10, 20, 40),
  abs.1 = c(0.478, 0.814, 1.012, 1.328, 1.659),
  abs.2 = c(0.470, 0.851, 1.041, 1.358, 1.659)
)

sample <- data.frame(
  labels = c("t1", "t3", "t5"),
  abs.1 = c(0.891, 1.249, 1.504),
  abs.2 = c(0.960, 1.249, 1.550)
)

curva.mean <- apply(curva[-1,-1], 1, mean, na.rm = TRUE) - 0.474
K <- c(5,10,20,40)/curva.mean

0.474

curva.blk <- 

plot(curva$conc, curva.mean)

cor.test(curva$conc, curva.mean)
model <- lm(curva.mean~curva$conc -1) # p-value decent, R-sq good enough
summary(model)

abline(model) # line is pretty bad

shapiro.test(resid(model)) # Residuals are not normal
plot(fitted(model),resid(model)) # Residuals do not seem random

abs.conc <- function(abs, BSA, blank = "calculate", volume){
  if(blank == "calculate"){
    blk <- mean(abs[-1, 1])
  }else if(is.numeric(blank) == TRUE){
    if(! length(abs) == length(BSA) & !length(abs) == length(blk)){
      stop("Blank, BSA and abs lengths not equal to eachother.")
    }else{
      blk <- mean(blank)
    }
  }else if(blank == "zero" | blank == 0){
    blk <- 0
  }else{
    stop("Blank values unsupported.")
  }

  
  mean = apply(abs[,-1], 1, mean, na.rm = TRUE)
  k <- mean * BSA / (mean - blk)
  k. <- sum(k/4)
  conc <- k. * (mean - blk)/volume
  print("Blank value:")
  blk
  print("Volume used for reading:")
  volume
  print("Concentration of samples:")
  conc
}

bsa.conc <- c(5, 10, )

#' media di due abs
#' media - abs bianco
#' k = conc curva / media-bianco
#' k media (media delle K)
#' correlazione tra media-B e le k
#'
#'  media dei 2 abs campioni medcamp
#'  medcamp - media abs bianco medblk
#'  
#'  medblk * k media (ug totali)
#'  ug/ul di presa (1,3,5,)
#'  


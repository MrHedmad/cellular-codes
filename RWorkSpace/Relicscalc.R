relics <- function(
  stage,
  bos = 0
){
  relicsMult1  <- 3
  relicsBase1  <- 1.21
  relicsExpo1  <- 0.48
  relicsOffset <- -110
  relicsMult2  <- 1.5
  relicsBase2  <- 1.002
  relicsExpo2  <- 1.005
  relicsExpo3  <- 1.1
  relicsMult3  <- 5e-7
  
  bos.relicsPerLevel <- 0.05
  bos.growthMax      <- 0.12
  bos.growthRate     <- 1e-4
  bos.growthExpo     <- 0.5
  bos.costExpo       <- 2.5
  
  T1 <- relicsMult1*(relicsBase1^(stage^relicsExpo1))
  T2 <- relicsMult2*(stage+relicsOffset)
  T3 <- relicsBase2^(stage^(relicsExpo2*((stage^relicsExpo3)*relicsMult3+1)))
                      
  R1 <- max(round(T1 + T2 + T3), 0)
  
  Rb <- bos.relicsPerLevel*bos^(
    (1+(bos.costExpo-1)*((min((bos.growthRate*bos), bos.growthMax))^bos.growthExpo
    )))
  
  R2 <- max(round(R1 * Rb/2), 0)
  
  Total <- R1 + R2
  
  return(c(Total = Total, FromStage = R1, FromBook = R2, BookMult = Rb))
}

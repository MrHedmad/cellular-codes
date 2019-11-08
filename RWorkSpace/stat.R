senators <- function(Fem = 13, 
                     Mal = 87, 
                     sample.size = 10, 
                     sample.number = 100){

pop <- c(rep("F", Fem), rep("M", Mal)) # I create the population base

for(i in 1:sample.number){
  popsa[[i]] <- sample(pop, sample.size, replace = TRUE)
  popsa.factor[[i]] <- table(factor(popsa[[i]], levels = c("M", "F")))
  popsa.proportion[[i]] <- popsa.factor[[i]][2]/sample.size
  }

popsa.unlisted <- unlist(popsa.proportion)
popsa.frequency <- table(popsa.unlisted)

popsa.frame <- data.frame(Level = as.numeric(names(popsa.frequency)), 
                          Freq =  as.numeric(popsa.frequency))
return(popsa.frame)
}



senators <- function(Fem = 13, 
                     Mal = 87, 
                     sample.size = 10, 
                     sample.number = 100){
  
  pop <- c(rep("F", Fem), rep("M", Mal)) # I create the population base
  
  answer<-sapply(1:sample.number, function(x){
    popsa <- sample(pop, sample.size, replace = TRUE);
    length(popsa[popsa=="F"])/sample.size
    })
  
  popsa.frequency <- table(answer)
  
  popsa.frame <- data.frame(Level = as.numeric(names(popsa.frequency)), 
                            Freq =  as.numeric(popsa.frequency))
  return(popsa.frame)
} 

senators() 
plot(df, type="h", lwd = 5, lend=1)

result <- senators(Fem=13,Mal=87,sample.size=50,sample.number=10000)

raw <- sapply(1:length(result$Level), function(x){
  rep(result$Level, result$Freq)
})

hist(raw)

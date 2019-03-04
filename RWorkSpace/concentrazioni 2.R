curva <- data.frame(
  conc = c(0, 5, 10, 20, 40),
  abs.1 = c(0.478, 0.814, 1.012, 1.328, 1.659),
  abs.2 = c(0.470, 0.851, 1.041, 1.358, 1.659),
  abs.3 = c(0.452, 0.778, 1.097, 1.363, 1.778),
  abs.4 = c(0.481, 0.854, 1.079, 1.398, 1.778)
)

analyze(sample <- data.frame(
  labels = c("t1", "t3", "t5"),
  abs.1 = c(0.891, 1.249, 1.504),
  abs.2 = c(0.960, 1.249, 1.550),
  abs.3 = c(0.796, 1.222, 1.523),
  abs.4 = c(0.834, 1.222, 1.523)
)

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

blk.mean <- mean(as.numeric(curva[1,-1]))

cur.abs <- as.numeric( apply(curva[-1,-1], 1, mean, na.rm = TRUE))
adj.cur.abs <-as.numeric(cur.abs - mean(as.numeric(curva[1,-1])))

k <- curva[-1, 1] / adj.cur.abs
k.mean <- mean(as.numeric(k))

cor.test(as.numeric(k), adj.cur.abs)
plot(as.numeric(k), adj.cur.abs)
model <- lm(adj.cur.abs~k)
abline(model)
summary(model)

medcap <- as.numeric(apply(sample[,-1], 1, mean, na.rm = TRUE))
medblk <- medcap - blk.mean

tot.ug <- medblk * k.mean ; tot.ug
tot.ug / c(1, 3, 5) -> result

#########

C <- c(5, 10, 20, 40)

plot(adj.cur.abs, C)
cor.test(adj.cur.abs, C)
model2 <- lm(C~adj.cur.abs)
summary(model2)
abline(model2)

medcap <- data.frame(
  adj.cur.abs = apply(sample[,-1], 1, mean, na.rm = TRUE)
  )

predicted.conc <- predict(model2, medcap) ; predicted.conc

dil.factor <- c(20, 6.666, 4)

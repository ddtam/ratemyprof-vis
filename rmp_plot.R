library('ggplot2')
library('ggthemes')

raw <- read.csv(file="data.csv")

plot(raw$rating, raw$difficulty,
     xlab = "Professor Rating",
     ylab = "Professor Difficulty")

ggplot(raw, aes(x=rating, y=difficulty)) +
  geom_point(alpha=0.1) +
  theme_minimal()

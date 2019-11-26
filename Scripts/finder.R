library(dplyr)
library(ggplot2)


df <- read.csv("./DataExtract/Data/processed.json_partial.csv")
df <- as.data.frame(df)

table(df$brand)

df[which(regexpr("L'" , df$brand) >= 0), ]$brand <- "L'Oreal"

## Estimated bands
df %>% 
  group_by(brand) %>%
  summarise(meanprice = mean(price))

## Price
ggplot(data = df , aes(x = df$price)) + geom_density()

df$priceband <- case_when( df$price < 7.5 ~ "Low"
                           , df$price < 12.5 ~ "Medium"
                           ,TRUE ~ "High")

## Ratings
ggplot(data = df , aes(x = df$stars)) + 
  geom_density() + 
  scale_x_continuous(breaks = seq(2.5,  5 , 0.1))

df$starsBand <- case_when( df$stars < 3.9 ~ "Poor"
                          ,df$stars < 4.3 ~ "Good"
                          ,TRUE ~ "Excellent")

table(df$starsBand , df$priceband)




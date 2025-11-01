df<-data.frame(
  id=c(1,2,3,4,5),
  name=c("AAA","BBB","CCC","DDD","EEE"),
  s1=c(56,70,90,65,96),
  s2=c(57,70,80,70,97),
  s3=c(58,70,70,50,98)
)
df$tot<-rowSums(df[,3:5])
df$avg<-rowMeans(df[,3:5])
df$grade<-with(df,
                ifelse(avg>=90,"O",
                  ifelse(avg>=80,"A",
                    ifelse(avg>=70,"B",
                      ifelse(avg>=80,"C",
                        ifelse(avg>=70,"D","F"))))))
cat("Dataframe is:-\n")
print(df)
df_sort<-df[order(df$avg),]
cat("Sorrted dataframe is:-\n")
print(df_sort)

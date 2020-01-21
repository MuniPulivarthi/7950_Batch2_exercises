library('readxl')
library('dplyr')
#print(excel_sheets('/Dowloads/SaleData.xlsx'))
df<-read_excel('C:/Users/muni.pulivarthi/Downloads/SaleData.xlsx')
print(head(df)
)
#Question 1
df1<-df %>% group_by(Item) %>% summarise(sum_amt=sum(Sale_amt))
print(min(df1$sum_amt))

#Question 2
df_temp<-df
df_temp$OrderDate<-format(as.Date(df_temp$OrderDate, format="%Y-%m-%d"),"%Y")
print(df_temp)
df2<-df_temp %>% group_by(OrderDate,Region) %>% summarise(totalsales=sum(Units))
print(df2)

#Question 3
ref_date<-"2018-07-02"
days_diff<- as.Date(as.character(df$OrderDate), format="%Y-%m-%d")-
  as.Date(as.character(ref_date), format="%Y-%m-%d")
days_diff<-abs(days_diff)
df3<-cbind(df,days_diff)
print(head(df3))

#Question 4
df4<-df %>% group_by(Manager) %>% summarise(list_of_Salesman=list(unique(SalesMan)))
print(df4)

#Question 5
df5<-df %>% group_by(Region) %>% summarise(sales=sum(Units))
df7<-df %>% group_by(Region) %>% summarise(SalesMan=length(unique(SalesMan)))
salesmen_count=df7['SalesMan']
region=df7['Region']
total_sales=df5['sales']
dffinal=data.frame(region,salesmen_count,total_sales)
print(dffinal)

#Question 6
total_sale_amt<-sum(df$Sale_amt)
print(total_sale_amt)
df6<-df %>% group_by(Manager) %>% summarise(percent_Sales=((sum(Sale_amt))/total_sale_amt)*100)
print(df6)

#imdb dataset
df2<-read.csv('C:/Users/muni.pulivarthi/Downloads/imdb.csv')

#Question 7
print(paste("Imdb rating of the 5th movie is:",df2[5,'imdbRating']))

#Question8
print(min(as.numeric(as.character(df2$duration)),na.rm=TRUE))
print(max(as.numeric(as.character(df2$duration)),na.rm=TRUE))

#Question9
l1<-df2[order(df2[,'year'],-as.numeric(df2[,'imdbRating'])),]
print(l1)

#Question10
l2<-df2[(as.numeric(as.character(df2$duration)))>1800 & (as.numeric(as.character(df2$duration)))<=10800,]
print(l2)

#diamonds dataset
df3<-read.csv('C:/Users/muni.pulivarthi/Downloads/diamonds.csv')
#Quetsion11
s1<-nrow(df3)
s2<-nrow(distinct(df3))
print(s1-s2)

#Question12
na.omit(df3$carat,df3$cut)
print(df3)

#Question13
nums <- unlist(lapply(df3, is.numeric)) 
print(df3[,nums])

#Question14
df3$z_new=as.numeric(df3$z)
df3new<-ifelse(df3$depth>60,df3$x*df3$y*df3$z_new,8)
print(df3new)


#Question15
df3$price<-as.numeric(df3$price)
df3[is.na(df3$price)]<-mean(df3$price)
#print(df3)

library(randomForest)
library(miscTools)
library(ggplot2)
library(lubridate)

df1 = data.frame(q2_buy_tot)

df1$issueDate = dmy(df1$issueDate)
df1$issueDate[is.na(df1$issueDate)] = min(df1$issueDate,na.rm=TRUE)

df1$maturity= dmy(df1$maturity)
df1$maturity[is.na(df1$maturity)] = max(df1$maturity,na.rm=TRUE)
df1$bondage = year(df1$maturity)-year(df1$issueDate)

df1$date=NULL
df1$datetime=NULL
df1$X=NULL
df1$dat=NULL

df1$ratingAgency1EffectiveDate = NULL
df1$ratingAgency2EffectiveDate = NULL
df1$time2=as.numeric(ymd_hms(df1$time))
df1$time =q2_buy_tot$time
df1$industrySubgroup = NULL
df1$industryGroup = NULL
df1$issuer=NULL
df1$day=NULL

df1$isin=NULL
df1$collateralType=NULL
df1$time2 = NULL
df1$ratingAgency1Rating  = q2_buy_tot$ratingAgency1Rating
df1$ratingAgency2Rating  = q2_buy_tot$ratingAgency2Rating  
df1$ratingAgency1Rating=as.numeric(gsub("rating([0-9]+)","\\1",df1$ratingAgency1Rating))
df1$ratingAgency2Rating=as.numeric(gsub("rating([0-9]+)","\\1",df1$ratingAgency2Rating))
df1$couponFrequency[is.na(df1$couponFrequency)] = mean(df1$couponFrequency, na.rm=TRUE) #filling NAs
set.seed(415)
rf = randomForest(volume ~ ., data=df2,ntree=10,importance=TRUE,mtry=5)

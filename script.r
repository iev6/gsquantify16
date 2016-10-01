library(randomForest)
library(miscTools)
library(ggplot2)
library(lubridate)
df1 = data.frame(q2_buy_tot)
df1$issueDate = NULL
df1$date=NULL
df1$datetime=NULL
df1$X=NULL
df1$dat=NULL
df1$ratingAgency1EffectiveDate = NULL
df1$ratingAgency2EffectiveDate = NULL
df1$time2=as.numeric(ymd_hms(df1$time))
df1$time =NULL
df1$industrySubgroup = NULL
df1$industryGroup = NULL
df1$issuer=NULL
df1$day=NULL
df1$maturity=NULL
df1$isin=NULL
df1$collateralType=NULL
df1$ratingAgency1Rating  = q2_buy_tot$ratingAgency1Rating
df1$ratingAgency2Rating  = q2_buy_tot$ratingAgency2Rating  
df1$ratingAgency1Rating=as.numeric(gsub("rating([0-9]+)","\\1",df1$ratingAgency1Rating))
df1$ratingAgency2Rating=as.numeric(gsub("rating([0-9]+)","\\1",df1$ratingAgency2Rating))
df1$couponFrequency[is.na(df1$couponFrequency)] = mean(df1$couponFrequency, na.rm=TRUE) #filling NAs
set.seed(415)
rf = randomForest(volume ~ ., data=df1,ntree=10,importance=TRUE,mtry=5)
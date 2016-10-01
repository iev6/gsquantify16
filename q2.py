import pandas as pd
import numpy as np

df_metadata = pd.read_csv('ML_Bond_metadata_corrected_dates.csv');
df_transdata = pd.read_csv('dataset.csv');

days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun',np.NaN:'NaN'}
df_transdata['day'] = pd.to_datetime(df_transdata['date'],format='%d%b%Y')

df_totdata = df_transdata.merge(df_metadata,on ='isin',how = 'left');

df_buy_trans = df_totdata.loc(df_totdata['side']=='B');
df_sell_trans = df_totdata.loc(df_totdata['side']=='S');

df_buy_trans.to_csv('q2_buy_tot.csv');
df_sell_trans.to_csv('q2_sell_tot.csv');

#we need to build 4 models, one for buyvolume, one for sellvolume, one for each of the two amounts
"""
['isin', 'time', 'price', 'side', 'volume', 'timeofday', 'date',
       'datetime', 'day', 'issuer', 'issueDate', 'market', 'amtIssued',
       'amtOutstanding', 'collateralType', 'coupon', 'couponFrequency',
       'couponType', 'industryGroup', 'industrySector', 'industrySubgroup',
       'maturity', 'maturityType', 'securityType', 'paymentRank',
       '144aFlag', 'ratingAgency1Rating', 'ratingAgency1Watch',
       'ratingAgency1EffectiveDate', 'ratingAgency2Rating',
       'ratingAgency2Watch', 'ratingAgency2EffectiveDate']
"""
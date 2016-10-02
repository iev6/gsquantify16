# coding: utf-8
get_ipython().magic(u'cd "D:\\Contests\\Quantify16"')
import graphlab.aggregate as agg
import graphlab as gl
from graphlab import SFrame
from datetime import datetime
import datetime as dt
def age(x):
    if(x['maturity']==None or x['issueDate']==None): 
        return None
    b = datetime.strptime(x['maturity'], "%d-%m-%Y")
    a = datetime.strptime(x['issueDate'], "%d-%m-%Y")
    days = b-a
    return days.days


p_vol_data = SFrame(data='dataset.csv')
bond_char_data = SFrame(data='ML_Bond_metadata_corrected_dates.csv')
bond_char_data = bond_char_data.remove_columns(['ratingAgency1EffectiveDate','ratingAgency2EffectiveDate'])
bond_char_data = bond_char_data.fillna('couponFrequency',2)

bond_char_data['age'] = bond_char_data.apply(age,dtype=int)
bond_char_data = bond_char_data.fillna('age',4565)
bond_char_data['age'] = bond_char_data['age'].apply(lambda x:max(x,0))
bond_char_data['age'].sketch_summary()
bond_char_data.remove_column('issueDate')
bond_char_data.remove_column('maturity');
bond_char_data.remove_column('industrySubgroup');

bond_char_data.save('bond_char_data.csv', format='csv')
b_tot_data  = tot_data[tot_data['side']=='B']
s_tot_data  = tot_data[tot_data['side']=='S']
s_tot_data = s_tot_data.remove_column('side')
b_tot_data = b_tot_data.remove_column('side')
b_tot_data['date'] = b_tot_data['date'].apply(lambda x: dt.datetime.strptime(x, '%d%b%Y'))
s_tot_data['date'] = s_tot_data['date'].apply(lambda x: dt.datetime.strptime(x, '%d%b%Y'))
s_tot_data['date'] = s_tot_data['date'].apply(lambda x: dt.datetime.weekday(x))
b_tot_data['date'] = b_tot_data['date'].apply(lambda x: dt.datetime.weekday(x))
train_b, test_b = b_tot_data.random_split(0.7)
b_boosted_trees_model = gl.boosted_trees_regression.create(train_b,target='volume')
results = boosted_trees_model.evaluate(test_b)
results
len(results)
bond_char_day_2['date'] = 0
bond_char_day_3['date'] = 1
bond_char_day_1['date'] = 4
bond_char_day_1 = bond_char_data
bond_char_day_2['date'] = 0
bond_char_day_3['date'] = 1
bond_char_day_1['date'] = 4
bond_price = SFrame()
price = SFrame.groupby(tot_data,key_columns='isin',operations={'price':agg.MEAN('price')});
bond_char_day_1 = bond_char_day_1.join(price,how='inner',on='isin');
bond_char_day_2 = bond_char_day_2.join(price,how='inner',on='isin');
bond_char_day_3 = bond_char_day_3.join(price,how='inner',on='isin');
buy_vol_1 = b_boosted_trees_model.predict(bond_char_day_1);
buy_vol_2 = b_boosted_trees_model.predict(bond_char_day_2);
buy_vol_3 = b_boosted_trees_model.predict(bond_char_day_3);
train_s, test_s = s_tot_data.random_split(0.7)
s_boosted_trees_model = gl.boosted_trees_regression.create(train_s,target='volume')
sell_vol_3 = s_boosted_trees_model.predict(bond_char_day_3);
sell_vol_2 = s_boosted_trees_model.predict(bond_char_day_2);
sell_vol_1 = s_boosted_trees_model.predict(bond_char_day_1);
bond_char_day_2['buyvolume'] = buy_vol_2
bond_char_day_3['buyvolume'] = buy_vol_3
bond_char_day_1['buyvolume'] = buy_vol_1
bond_char_day_1['sellvolume'] = sell_vol_1
bond_char_day_2['sellvolume'] = sell_vol_2
bond_char_day_3['sellvolume'] = sell_vol_3
tot_bs['isin']= buy_vol_1['isin']
tot_bs = SFrame()
tot_bs['isin']= bond_char_day_1['isin']
tot_bs['buyvolume'] = bond_char_day_1['buyvolume']+bond_char_day_2['buyvolume']+bond_char_day_3['buyvolume']
tot_bs['sellvolume'] = bond_char_day_1['sellvolume']+bond_char_day_2['sellvolume']+bond_char_day_3['sellvolume']
tot_bs.save('total_buy_sell.csv',format='csv')
tot_bs.sketch_summary()
tot_bs
bond_char_day_1
len(buy_vol_1)
len(price)
len(tot_data['isin'])
tot_data['isin'].sketch_summary()
bond_char_data['isin'].sketch_summary()
tot_data = bond_char_data.join(p_vol_data,how='left',on='isin')
b_tot_data  = tot_data[tot_data['side']=='B']
s_tot_data  = tot_data[tot_data['side']=='S']
tot_bs['isin']
tot_bs['buyvolume'].sketch_summary()
tot_bs['sellvolume'].sketch_summary()
tot_bs['sellvolume'] = tot_bs['sellvolume'].apply(lambda x : max(x,0),dtype=int);
tot_bs['sellvolume'].sketch_summary()
new_tot_data = tot_bs.join(bond_char_data,on='isin',how='right');
new_tot_data['isin'].sketch_summary()
new_tot_data.column_names()
new_tot_data.remove_columns(['issuer', 'market', 'amtIssued', 'amtOutstanding', 'collateralType', 'coupon', 'couponFrequency', 'couponType', 'industryGroup', 'industrySector', 'maturityType', 'securityType', 'paymentRank', '144aFlag', 'ratingAgency1Rating', 'ratingAgency1Watch', 'ratingAgency2Rating', 'ratingAgency2Watch', 'age', 'date']);
new_tot_data.column_name()
new_tot_data.column_names()
new_tot_data = new_tot_data.fillna('buyvolume',245016); #flooring
new_tot_data = new_tot_data.fillna('sellvolume',0); #flooring
new_tot_data['buyvolume'].sketch_summary()
new_tot_data['buyvolume'] = new_tot_data['buyvolume'].apply(lambda x : int(x));
new_tot_data.save('tot_sub.csv',format='csv');
get_ipython().magic(u'save q2.py 1-182')

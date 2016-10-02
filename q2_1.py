import graphlab as gl
from graphlab import SFrame
from datetime import datetime

p_vol_data = SFrame(data='dataset.csv')

bond_char_data = SFrame(data='ML_Bond_metadata_corrected_dates.csv')
bond_char_data = bond_char_data.remove_columns(['ratingAgency1EffectiveDate','ratingAgency2EffectiveDate'])

# 2 is floor(mean(couponFrequency))
bond_char_data = bond_char_data.fillna('couponFrequency',2)

def age(x):
    if(x['maturity']==None or x['issueDate']==None): 
        return None
    b = datetime.strptime(x['maturity'], "%d-%m-%Y")
    a = datetime.strptime(x['issueDate'], "%d-%m-%Y")
    days = b-a
    return days.days

bond_char_data['age'] = bond_char_data.apply(age,dtype=int)

# 4565 is floor(mean(age))
bond_char_data = bond_char_data.fillna('age',4565)

bond_char_data = bond_char_data.remove_column('maturity')
bond_char_data = bond_char_data.dropna()
bond_char_data = bond_char_data[bond_char_data['age']>=0]

bond_char_data.save('bond_char_data.csv', format='csv')

tot_data = bond_char_data.join(p_vol_data,how='inner',on='isin')

b_tot_data  = tot_data[tot_data['side']=='B']
s_tot_data  = tot_data[tot_data['side']=='S']

s_tot_data = s_tot_data.remove_column('side')
b_tot_data = b_tot_data.remove_column('side')

s_tot_data = s_tot_data.remove_column('time')
b_tot_data = b_tot_data.remove_column('time')

s_tot_data = s_tot_data.unique()
b_tot_data = b_tot_data.unique()

s_tot_data.save('s_tot_data.csv', format='csv')
b_tot_data.save('b_tot_data.csv', format='csv')

train_b, test_b = b_tot_data.random_split(0.7)

random_forest_model = gl.random_forest_regression.create(train_b, target='volume')
results = random_forest_model.evaluate(test_b)
print results

boosted_trees_model = gl.boosted_trees_regression.create(train_b,target='volume')
results = boosted_trees_model.evaluate(test_b)
print results

random_forest_model.save('random_forest_model')
boosted_trees_model.save('boosted_trees_model')

import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split

import xgboost as xgb
import pickle

df = pd.read_csv('heart_attack_prediction_dataset.csv') 
df.columns=df.columns.str.lower().str.replace(' ','_')

strings=df.dtypes[df.dtypes=='object'].index

for s in strings:
    df[s] = df[s].str.lower().str.replace(" ","_")

blood_pressure = df['blood_pressure'].values
blood_pressure_max = []
blood_pressure_min = []

for i in range(0,len(df)): 
    blood_pressure_max.append(int(blood_pressure[i].split('/')[0]))
    blood_pressure_min.append(int(blood_pressure[i].split('/')[1]))
    
df['blood_pressure_min'] = blood_pressure_min
df['blood_pressure_max'] = blood_pressure_max

exercise_hours_per_week = []
sedentary_hours_per_day = []

for i in range(0,len(df)): 
    exercise_hours_per_week.append(round(df['exercise_hours_per_week'][i]))
    sedentary_hours_per_day.append(round(df['sedentary_hours_per_day'][i]))
    
df['exercise_hours_per_week'] = exercise_hours_per_week
df['sedentary_hours_per_day'] = sedentary_hours_per_day

income_30k = []

for i in range(0,len(df)): 
    income_30k.append(int(df['income'][i]/30000))
    
df['income_30k'] = income_30k
del df['income']

cholesterol = []
triglycerides = []
bmi = []

for i in range(0,len(df)): 
    cholesterol.append(round(df['cholesterol'][i]/10)*10)
    triglycerides.append(round(df['triglycerides'][i]/10)*10)
    bmi.append(int(df['bmi'][i].round()))
    
df['cholesterol'] = cholesterol
df['triglycerides'] = cholesterol
df['bmi']= bmi


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1) 

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

df_full_train = df_full_train.reset_index(drop=True) 


y_train = df_train.heart_attack_risk.values
y_val = df_val.heart_attack_risk.values
y_test = df_test.heart_attack_risk.values

y_full_train = df_full_train.heart_attack_risk.values


del df_train['heart_attack_risk']  
del df_val['heart_attack_risk']
del df_test['heart_attack_risk']

del df_full_train['heart_attack_risk']

numerical = ['age','cholesterol','heart_rate','diabetes',
             'family_history','smoking','obesity',
             'alcohol_consumption','exercise_hours_per_week',
             'previous_heart_problems','medication_use',
             'stress_level','sedentary_hours_per_day',
             'bmi','triglycerides','physical_activity_days_per_week',
             'sleep_hours_per_day','blood_pressure_min',
             'blood_pressure_max','income_30k'
            ]

categorical = ['sex','diet','country','continent','hemisphere']


dicts_df_full_train = df_full_train[categorical + numerical].to_dict(orient='records')

dv=DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_df_full_train)

dicts_test = df_test[categorical + numerical].to_dict(orient='records')
X_test = dv.transform(dicts_test)

dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=dv.get_feature_names_out())
dtest = xgb.DMatrix(X_test, feature_names=dv.get_feature_names_out())

xgb_params = {
    'eta':0.05,               
    'max_depth' : 6,
    'min_child_weight': 1,   
    'objective':'binary:logistic',
    'eval_metric':'auc',
    'nthread':8,
    'seed':1,
    'verbosity':1                               
}

model = xgb.train(xgb_params, dfulltrain,num_boost_round = 125)


output_file = 'model_xgb.bin'

f_out = open(output_file, 'wb')
pickle.dump((model, dv), f_out)   
f_out.close() 


import pandas as pd
import numpy as np
import pickle
from collections import Counter
import re
import csv


# Change dates to datetime objects
df = pd.DataFrame(listofrecords)
df['AwardEffdt']= pd.to_datetime(df[1])
df['AwardExp_dt']= pd.to_datetime(df[2])
df['Award_amt']= df[3].astype(int)
df['Min_amend_dt']= pd.to_datetime(df[7])
df['Max_amend_dt']= pd.to_datetime(df[8])
df['Grant_length']=df['AwardExp_dt']-df['AwardEffdt']
df['Amend_length'] = df['Max_amend_dt']-df['Min_amend_dt']


# Change grant length from timestamp to length in days
gl_days=[]
for i,x in enumerate(df['Grant_length']):
    gl_days.append(df['Grant_length'][i].days)
df['Gl_days']= gl_days

# Change amended days to length in days
am_days = []
for i,x in enumerate(df['Amend_length']):
    am_days.append(df['Amend_length'][i].days)
df['Am_days']=am_days


# Count the number of words in the abstract 
abs_words = []
for x in range(0, len(df)):
    try:
        abs_words.append(len(df[5][x]))
    except:
        abs_words.append('0')
df['Abstract_length']=abs_words
df['Abstract_length']=df['Abstract_length'].astype(int)


# Get dummies for categorical data
S = pd.get_dummies(df['State'])
df2=df.join(S)

with open('finalized_data.pickle', 'wb') as f:
    pickle.dump(df2, f)

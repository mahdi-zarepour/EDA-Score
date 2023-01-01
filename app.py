import os
import statistics as st

import pandas as pd
import numpy as np


def standard_score(data):
    mean = st.mean(data)
    std = st.stdev(data)
    zdata = []
    for i in data:
        zdata.append((i - mean)/std)
    
    return zdata


df_path = os.path.dirname(__file__) + '\score_a.csv'
df = pd.read_csv(df_path, index_col=0)


sa_mean = np.mean(df['SA'])
pa_mean = np.mean(df['PA'])
# print(sa_mean)
# print(pa_mean)

# print('------')

sa_var = np.var(df['SA'])
pa_var = np.var(df['PA'])
# print(sa_var)
# print(pa_var)

sa_std = np.std(df['SA'])
pa_std = np.std(df['PA'])
# print(sa_std)
# print(pa_std)

pa_z_score = standard_score(df['PA'])
sa_z_score = standard_score(df['SA'])
# print(pa_z_score)
# print(sa_z_score)

# print(df['SA'].describe())
# print(df['PA'].describe())

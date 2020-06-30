# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:31:30 2020

@author: chupp
"""

import pandas as pd
import numpy as np

df=pd.DataFrame({'id':[1,1,2,2,2,2,2,3,3,3,3,3,3,4]})

f_idx=np.unique(df.id.values,return_index=1)[1]
l_idx=f_idx-1
l_idx=l_idx[1:]
l_idx=np.append(l_idx,len(df)-1)


df.index.to_series().groupby(df['id']).first().reset_index()
df.index.to_series().groupby(df['id']).last()
df2=df.index.to_series().groupby(df['id']).agg(['first','last'])

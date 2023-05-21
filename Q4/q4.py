#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

if __name__ == '__main__':
    
    df = pd.read_csv("gender2.csv", index_col = 0, encoding = 'CP949')
    
    new = df.loc[:, ['2022년_계_총인구수', '2022년_남_총인구수', '2022년_여_총인구수']]
    new = new.rename(columns = {'2022년_계_총인구수':'Total',
                               '2022년_남_총인구수':'Male',
                               '2022년_여_총인구수':'Female'})
    
    print(new)


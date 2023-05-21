#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd

if __name__ == '__main__':
    
    df = pd.DataFrame([[100, 25], [280, 120], [900, 30]],
                     index = ['store1', 'store2', 'store3'],
                     columns = ['unit price', 'number'])
    
    df['total price'] = df['unit price'] * df['number']
    
    #total price 높은 순으로 정렬
    df2 = df.sort_values('total price', ascending = False)
    
    print("*** 가격이 비싼 가게 2개 ***")
    print(df2[:2])


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

if __name__ == '__main__':
    
    docs = np.array([[1, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1, 0],
                    [1, 1, 0, 1, 0, 0]])
    query = np.array([1, 1, 0, 0, 1, 0])
    
    def cos(a, b):
        for i in range(len(a)):
            doc = a[i][:]
            cos_sim = np.dot(doc, b.transpose()) / (np.linalg.norm(doc)*np.linalg.norm(b))
            print("doc{0:d}={1:0.2f}".format(i+1, cos_sim))
            
    cos(docs, query)


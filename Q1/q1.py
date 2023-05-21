#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

if __name__ == '__main__':

    arr = np.array([[1, 2],
        [3, 4]])
    
    eigval, eigvec = np.linalg.eig(arr)
    det = np.linalg.det(arr)
    
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    
    a = np.array([[1, 2, -2],
                 [2, 1, -5],
                 [1, -4, 1]])
    b = np.array([-15, -21, 18])
    x = np.linalg.solve(a, b)
    
    print("Eigenvalues:", eigval[0], ",", eigval[1])
    print("Eigenvectors:", eigvec[0], ",", eigvec[1])
    print("Determinant:", det)
    print("Cross product:", np.cross(vec1, vec2))
    print("Solution:",x)


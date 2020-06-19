#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def plus_minus(a):
    a = np.array(a)
    sum = 0
    for i in a:
        if i > 0:
            sum += i - 1
        else:
            sum += i + 1
    return(sum)


#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "[]{}()*,._-"
 
    


# In[12]:


all = (lower+upper+number+symbols)
lenght = 16
password = "".join(random.sample(all, lenght))
        


# In[13]:


print(password)


# In[ ]:





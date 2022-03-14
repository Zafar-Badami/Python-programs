#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[19]:


df = pd.read_csv("car_fleet3.csv")


# In[20]:


df


# In[21]:


df.shape


# In[22]:


df.info()


# In[25]:


df.head(2)


# In[31]:


type(df)


# In[ ]:


jupyter nbconvert --to script untitled.ipynb


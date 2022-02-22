#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


data = {'Tool':['Python','JavaScript','Twitter','GitHub', 'Gephi','GeoNames','Transkribus','Excel','MySQL'],'2015':[9,8,10,2,11,2,0,5,0],'2016':[22,18,18,6,16,4,1,9,6],'2017':[27,12,26,17,14,3,2,3,9],'2018':[32,6,16,5,10,1,1,6,5],'2019':[35,15,12,10,9,8,8,7,7]}


# In[23]:


df = pd.DataFrame(data, columns = ['Tool','2015','2016','2017','2018','2019'])
df.head()


# In[31]:


df['Cumulative'] = df['2015'] + df['2016'] + df['2017'] + df['2018'] + df['2019']
print(df[['Tool','2015','2016','2017','2018','2019','Cumulative']])


#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd


# In[5]:


jane = "The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."


# In[10]:


jane = jane.split('EBOOK PRIDE AND PREJUDICE')
jane


# In[22]:


jane = 'Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single person in possession of a good fortune, must be in want of a wife.'


# In[23]:


jane_cleaned = jane.replace('man', 'person')
jane_cleaned = jane.replace('wife','partner')
jane_cleaned 


# In[26]:


df = pd.read_csv('tools_dh_proceedings.csv')
df.head()


# In[30]:


df.sort_values(by='2019', ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:





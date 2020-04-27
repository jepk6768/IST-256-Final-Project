#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
import json
import pandas as pd
import warnings
import csv

#hile True:
ing = input("Enter ingredients in your house: ")
    #f ing =='STOP':

with open('all_drinks.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for column in reader:
        if ing  == column[13]:
            print(column)
            


# In[ ]:





# In[ ]:





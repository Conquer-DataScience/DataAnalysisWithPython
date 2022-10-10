#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


application_record_df = pd.read_csv("application_record.csv")


# In[3]:


type(application_record_df)


# In[4]:


application_record_df.head()


# In[5]:


application_record_df.tail()


# ### Read Excel file in Pandas

# In[2]:


app_rec_excel_df = pd.read_excel("D:\LDS\DataAnalysisWithPython\Credit_Analysis_Spreadsheet.xls")


# In[3]:


app_rec_excel_df.head()


# In[4]:


app_rec_excel_df.tail()


# In[5]:


credit_info_df = pd.read_excel("D:\LDS\DataAnalysisWithPython\Credit_Analysis_Spreadsheet.xls", sheet_name = "credit_record")


# In[7]:


credit_info_df.head(10)


# In[8]:


app_rec_excel_df.info()


# In[9]:


credit_info_df.info()


# In[10]:


app_rec_excel_df.columns


# In[13]:


credit_info_df.shape


# In[14]:


credit_info_df.index


# In[15]:


credit_info_df.columns


# In[ ]:





# In[ ]:





# In[ ]:





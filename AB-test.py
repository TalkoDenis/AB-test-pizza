#!/usr/bin/env python
# coding: utf-8

# # A/B-tests

# In[1]:


import pandas as pd
import scipy.stats


# In[2]:


df = pd.read_csv('experiment_lesson_4.csv')


# In[3]:


df.head()


# In[4]:


df.district.unique()


# In[5]:


df.experiment_group.unique()


# There are two groups: test and control. I do the distribution of these groups, and then build graphs.

# In[6]:


# Control group
df.query('experiment_group == "control"').groupby('district').agg({'delivery_time': 'sum'})


# In[7]:


# Test group
test_df = df.query('experiment_group == "test"').groupby('district').agg({'delivery_time': 'sum'})


# In[8]:


test_df.head()


# In[9]:


df_test = df.query('experiment_group == "test"').groupby('district').agg({'delivery_time': 'sum'})


# In[10]:


df.district.hist()


# In[11]:


df.query('experiment_group == "test"').groupby('district').hist('delivery_time')


# In[12]:


# Distribution in the test group
df.query('experiment_group == "test"').groupby('district').delivery_time.hist()


# In[13]:


# Distribution in the control group
df.query('experiment_group == "control"').groupby('district').delivery_time.hist()


# In[14]:


df.head()


# In[15]:


# Count the number of observations
# Control group
df_count_control = df.query('experiment_group == "control"').order_id.count()


# In[16]:


# Count the number of observations
# Test group
df_count_test = df.query('experiment_group == "test"').order_id.count()


# In[17]:


# The module - how much one group differs from another.
df_count_control - df_count_test


# In[20]:


# Sampling, test group
semple_test_df = df[df['experiment_group'] == 'test']['delivery_time'].sample(1000, random_state=17)


# In[21]:


scipy.stats.shapiro(semple_test_df)


# In[22]:


# Sampling, control group
semple_control_df = df[df['experiment_group'] == 'control']['delivery_time'].sample(1000, random_state=17)


# In[23]:


scipy.stats.shapiro(semple_control_df)


# In[24]:


# Считаем ДО сэмплирования


# In[25]:


df_delivery_time_test = df[df['experiment_group'] == 'test']['delivery_time']


# In[26]:


scipy.stats.shapiro(df_delivery_time_test)


# In[27]:


df_delivery_time_test.std()


# In[28]:


df_delivery_time_control = df[df['experiment_group'] == 'control']['delivery_time']


# In[29]:


scipy.stats.shapiro(df_delivery_time_control)


# In[30]:


df_delivery_time_control.std()


# In order to check if the distribution is normal, I use the SHAPIRO-WILK TEST. This test shows that the values in the test group are normally distributed. In the control group, the distribution is normal. The standard deviation of the delivery time in the test is (round to the nearest hundredth) 9.88. The standard deviation of delivery time in the control is (round to the nearest hundredth) 9.99.

# In[31]:


# Comparing test and control
scipy.stats.ttest_ind(df_delivery_time_test, df_delivery_time_control)


# In[32]:


# Calculate the average time of change as a percentage
# test
df_test_mean_time = df.query('experiment_group == "test"').delivery_time.mean()
# test
df_control_mean_time = df.query('experiment_group == "control"').delivery_time.mean()


# In[33]:


(df_test_mean_time / df_control_mean_time - 1) * 100


# What are the conclusions?
# The new algorithm works well, and the average delivery time in the test has changed down to 13.35

# In[ ]:





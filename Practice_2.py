#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[ ]:


#1


# In[6]:


a = np.array([[1, 6],
            [2, 8],
            [3, 11],
            [3, 10],
            [1, 7]])


# In[10]:


print(a.mean())


# In[11]:


print(a.mean(axis=0))


# In[17]:


print(a.mean(axis=1))


# In[18]:


mean_a = a.mean(axis=0)


# In[27]:


#2


# In[20]:


print(mean_a[0])


# In[24]:


a_centered = a - mean_a


# In[25]:


print(a_centered)


# In[26]:


#3


# In[40]:


a[:,0]


# In[41]:


a.shape


# In[43]:


a[:,1]


# In[50]:


a_centered_sp = a[:,0].dot(a[:,1])
a_centered_sp


# In[47]:


a_centered_sp/len(a-1)


# In[ ]:


#4


# In[51]:


a.transpose()


# In[54]:


cov_a = np.cov(a.transpose())


# In[55]:


cov_a


# In[56]:


cov_a[1,0]


# In[ ]:





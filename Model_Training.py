#!/usr/bin/env python
# coding: utf-8

# ## Model Training

# Dataset - Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images. Dataset can be used for Binary Classification sample problems

# In[8]:


import numpy as np
import pandas as pd
import sklearn


# In[3]:


df = pd.read_csv("BankNote_Authentication.csv")
df.head()


# In[4]:


# splitting variables

x = df.iloc[:,:-1]
y = df.iloc[:,-1]


# In[5]:


x.head()


# In[6]:


y.head()


# In[7]:


# Train test split
from sklearn.model_selection import train_test_split


# In[17]:


X_train, x_test , Y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)


# In[18]:


# Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train,Y_train)


# In[19]:


y_pred = classifier.predict(x_test)


# In[20]:


#check accuracy
from sklearn.metrics import accuracy_score 


# In[21]:


score = accuracy_score(y_pred,y_test)
score

#classifier.predict([[2,3,4,1]])
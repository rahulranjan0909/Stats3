#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import scipy.stats as sts
from scipy.stats import norm
import math
import numpy as np
p_mean = 100
p_std = 15
n = 36
sample_mean = 108
alpha = 0.05

SE = p_std/n**0.5
print(f"SE: {SE}")
Z = (sample_mean-p_mean)/SE
print(f"Z_score: {Z}")


# In[2]:


#2
n1 = 100
n2 = 100
R1 = 0.52            #Republicans from state 1
D1 = 0.48            #Democrats from state 1
R2 = 0.47            #Republicans from state 2
D2 = 0.53            #Democrats from state 2

mu = R1 - R2
print(f"mu: {mu}")
std = math.sqrt(((R1 * D1 ) / n1) + ((R2 * D2) /n2))
print(f"std: {std}")
Z_R1_R2 = ( x - mu)/std
print(f"Z_p1_p2 : {Z_R1_R2}")


# In[3]:


#3
x = 1100 #
mu = 1026 # Population Mean
sd = 209 #population standard deviation
z = ( x - mu)/sd
print("Z Score : ",z)
#the above calculation shows that my score is 0.35 standard deviations above the mean
print("My Score is in the range {} - {}  with a  zscore {:.2f}".format(mu - sd,mu + sd,z))


# In[ ]:





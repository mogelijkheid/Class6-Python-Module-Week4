#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
ebob = list()
number=int(input('Please enter the numbers of the inputs'))
i=0
while i<int(number):
    y=input('Enter the numbers')
    try:
        y = int(y)
        ebob.append(y)
        i+=1
    except Exception:
        print("do not enter Nan or non numerical inputs")
                               
print(ebob)
print(math.gcd(*ebob))


# ### 

# In[ ]:





# In[ ]:





# In[ ]:





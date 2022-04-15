#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
dice = [0, 0, 0, 0, 0, 0]
for i in range(5000):
    x = random.randint(1, 6)
    dice[x-1]+=1 
for i in range(1,7):
    print("Percentace of throws of value {} : {:0.2f} % ".format(i, dice[i-1]/5000*100))


# In[ ]:





# In[ ]:





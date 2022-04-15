#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
def rollDice(number):  
    dice=[0,0,0,0,0,0]
    for i in range(number):
       x=random.randint(1,6)
       x+=1
    for i in range (1,7):
       print("The probability of {} : {:0.2f}  ".format(i, dice[i-1]/number*100))


# In[ ]:


from my_dice import rollDice

repetation=int(input("Enter repetition number: "))

rollDice(repetation)


# In[ ]:





# In[ ]:





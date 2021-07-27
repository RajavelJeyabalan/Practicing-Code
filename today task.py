#!/usr/bin/env python
# coding: utf-8

# In[2]:


res=[]
for x in range(2000,3201):
    if(x%7==0) and (x%5!=0):
        res.append(x)
print(res)


# In[5]:


number = input("Enter the comma seperated number: ")
l = number.split(",")
t = tuple(l)
print(l)
print(t)


# In[ ]:


my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even_list=[]
add_list=[]
for var in my_list:
    if (var%2==0):
        even_list.append(var)
        print("Even numbers: ".format(even_list))
    elif (var%2!=0):
        add_list.append(var)
        print("Even numbers: ".format(add_list))


#!/usr/bin/env python
# coding: utf-8

# In[3]:


#the function table(n) prints the table of n    
def table(n):    
    return lambda a:a*n # a will contain the iteration variable i and a multiple of n is returned at each function call    
n = int(input("Enter the number:"))    
b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i    
for i in range(1,11):    
    print(n,"X",i,"=",b(i)) #the lambda function b is called with the iteration variable i  


# In[4]:


class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)


class MarsRover(Rocket): # inheriting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.name, self.maker)


if __name__ == "__main__":
    x = Rocket("simple rocket", "till stratosphere")
    y = MarsRover("mars_rover", "till Mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())


# In[5]:


def reverse(str):   
    if len(str) == 0: # Checking the lenght of string  
        return str   
    else:   
        return reverse(str[1:]) + str[0]   
    
str = "Devansh Sharma"   
print ("The original string  is : ", str)     
print ("The reversed string(using recursion) is : ", reverse(str))  


# In[6]:


str = "Devansh Sharma"   
print ("The original string  is : ", str)     
print ("The reversed string(using recursion) is : ", reverse(str))  


# In[ ]:





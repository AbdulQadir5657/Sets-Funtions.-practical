#!/usr/bin/env python
# coding: utf-8

# # Sets 

# In[1]:


set1 = {"UK", "USA", "Germany"}
print(set1)


# In[2]:


# we cannot have duplicates in sets
set1 = {"UK", "USA", "Germany","Germany"}
print(set1)


# In[3]:


# we cannot have duplicates in sets and also not include iin length 
set1 = {"UK", "USA", "Germany","Germany"}
print(len(set1))


# In[4]:


# sets contructor
set1 = set(("UK", "USA", "Germany")) 
print(set1)


# In[6]:


set1 = {"UK", "USA", "Germany"}
set2 = {10, 20, 30, 40}
#union

set3 = set1.union(set2)

print(set3)


# In[8]:


set1 = {"apple", "orange", "banana"}
set2 = {10, 20, 30, 40}
 
set3 = set1.union(set2)
print(set3)


# In[11]:


set1 = {"apple", "orange", "banana"}
set2 = {10, 20, 30, 40}
 
set3 = set2.union(set1)
print(set3)


# In[13]:


set1 = {"UK", "USA", "Germany"}
set2 = {10, 20, 30, 40}

#update
set1.update(set2)

print(set1)


# In[16]:


# I just to keep only the duplicate
set1 = {"UK", "USA", "Germany"}
set2 = {"UK", "KSA", "Germany", "Russia"}

set1.intersection_update(set2)

print(set1)


# In[18]:


set1 = {20, 30, 40 ,50}
set2 = {30, 40, 50, 60}

set1.intersection_update(set2)
print(set1)


# In[1]:


set1 = {"UK", "USA", "Germany"}
set2 = {"UK", "KSA", "Germany", "Russia"}

set3 = set1.intersection(set2)

print(set3)


# In[3]:


set1 = {"black", "red", "blue"}
set2 = {"green", "orange", "black", "white"}

set1.intersection_update(set2)

print(set1)


# In[4]:


set1 = {"black", "red", "blue"}
set2 = {"green", "orange", "black", "white"}

set3 = set1.intersection(set2)

print(set3)


# In[5]:


# in this case it only take the output which is not duplicate
set1 = {"black", "red", "blue"}
set2 = {"green", "orange", "black", "white"}

set1.symmetric_difference_update(set2)

print(set1)


# In[15]:


set1 = {"black", "red", "blue"}
set2 = {"green", "orange", "black", "white"}

set1.symmetric_difference_update(set2)

print(len(set1))


# In[16]:


set1 = {"black", "red", "blue"}
set2 = {"green", "orange", "black", "white"}

set1.symmetric_difference_update(set2)

print(type(set1))


# In[6]:


team1 = {"Abdul", "Saquib", "Faisal", "Aqib", "Saddam"}

for i in team1:
    print(i)


# In[7]:


# Data Dictinary
d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}
print(d1)


# In[8]:


print(d1["city"])


# In[13]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal", "city" : "Sambhal"}
print(len(d1))


# In[14]:


print(type(d1))


# In[17]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}
ky = d1.keys()

for k in ky:
    print(k)


# In[19]:


# dict() constructor

d1 = dict(name = "Abdul", Age = 22)
print(d1)


# In[21]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

d1 ["name"] = "Merry"
print(d1)


# In[22]:


# Using update

d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

d1.update({"city": "Amroha"})

print(d1)


# In[27]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

d1["grade"] = "A"
d1["total student"] = 26

print(d1)


# In[26]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

d1.update({"grade": "A", "total student": 26})

print(d1)


# In[29]:


# pop for delete
d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

d1.pop("age")

print(d1)


# In[32]:


# we also use del in plase of pop del
d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

del d1["name"]

print(d1)


# In[33]:


# its show error because we delete the key(d1)
del d1
print(d1)


# In[34]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

print(d1)

#d1.pop("age")
d1.clear()

print(d1)


# In[35]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal"}

for i in d1:
    print(i)


# In[41]:


for i in d1.values():
    print(i)


# In[43]:


d1 = {"name": "Abdul", "age": "25", "city": "Sambhal", "Designation": "Manager"}

d2 = d1.copy()

print(d2)


# In[47]:


d = {"d1": {"name": "Abdul", "age": "25"}, "d2": {"name": "Abdul", "age": "25"}, "d3": {"name": "Abdul", "age": "25"}}
print(d)


# In[ ]:


# function


# In[48]:


# def

def MyFirstFunction():
    print("This is our 3rd week and i am still struck here")
    
MyFirstFunction()


# In[54]:


# arguments
def MysecondFunction(name):
    print(name + " is a very smart and kind hearted person")
# calling   
MysecondFunction("Abdul")


# In[ ]:





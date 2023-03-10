#!/usr/bin/env python
# coding: utf-8

# In[1]:


countries=["Japan","India","Algeria","Brazil","Angola","England","Argentina","Portugal","China","Australia","Austria","Ghana","Bahamas","Bangladesh","Belgium","Bhutan","Bosnia","Cameroon","Canada","Denmark"]


# In[2]:


print(countries[2],countries[-1])


# In[3]:


print(countries[3],countries[-3])


# In[4]:


print(countries[18],countries[16])


# In[5]:


print(len(countries))


# In[6]:


print(countries[-1],countries[19])


# In[7]:


print(countries.index("Cameroon"))


# In[8]:


print(countries.index("Ghana"))


# In[9]:


print(countries.index(countries[10]))


# In[10]:


print(countries[len(countries)-1],countries[-1])


# In[11]:


print(countries[0].upper())


# In[13]:


countries[0]=countries[0].lower()
print(countries[0])


# In[14]:


countries.insert(5,"Germany")
print(countries[5])


# In[15]:


countries.append("Nigeria")
print(countries[20])


# In[16]:


countries.insert(11,"Nepal")
print(countries.index("Ghana"))


# In[17]:


del countries[4]
print(countries[4])


# In[18]:


del countries[3]
print(countries.index("Argentina"))


# In[19]:


print(countries[2:5])


# In[20]:


print(countries[-1:4])


# In[21]:


print(countries[-5:-2])


# In[22]:


print(countries[4:-1])


# In[23]:


print(countries[:10])


# In[24]:


print(countries[10:])


# In[25]:


print(countries[-3:])


# In[26]:


print(countries[:-1])


# In[27]:


print(countries[3:3])


# In[28]:


print(countries[-1:-4])


# In[29]:


print(countries[1:10][2])


# In[30]:


print(countries[2:len(countries)])


# In[31]:


print(countries[:][5])


# In[32]:


print(countries[-4][-4])


# In[34]:


print(len(countries[10:20]))


# In[35]:


print(len(countries[-20:]))


# In[36]:


print(len([]))


# In[37]:


print(len(countries[:]))


# In[38]:


print(len(countries[1:-1]))


# In[39]:


print(len(countries[2:-2]))


# In[41]:


countries.extend(["Algeria","Cuba"])
print(countries[-3:])


# In[42]:


countries.append(["New Zealand","Norway"])
print(countries[-3:])


# In[43]:


del countries[-2]
countries.insert(-1,"Mangolia")
print(countries[-3:])


# In[44]:


countries[1]="Poland"
print(countries[:3])


# In[ ]:





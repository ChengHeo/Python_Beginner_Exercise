#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)


# In[2]:


import numpy as np
l=[12.23,13.32,100,36.32]
print("Original List:",1)
a=np.array(1)
print("One-dimensional Numpy array: ",a)


# In[4]:


import numpy as np
x=np.arange(12,38)
print(x)


# In[6]:


import numpy as np
x=np.ones((3,3))
print("Original array:")
print(x)
print("0 on the border and 1 inside in the array")
x=np.pad(x,pad_width=1,mode='constant',constant_values=0)
print(x)


# In[7]:


import numpy as np
x=[10,20,30]
print("Original array:")
print(x)
x=np.append(x,[[40,50,60],[70,80,90]])
print("After append values to the end of the array:")
print(x)


# In[8]:


import numpy as np
x=np.sqrt([1+0j])
y=np.sqrt([0+1j])
print("Original array:x",x)
print("Original array:y",y)
print("Real part of the array:")
print(x.real)
print(y.real)
print("Imaginary part of the array:")
print(x.imag)
print(y.imag)


# In[9]:


import numpy as np
array1=np.array([0,10,20,40,60,80])
print("Array1: ",array1)
array2=[10,30,40,50,70]
print("Array2: ",array2)
print("Unique values in array1 that are not in array2")
print(np.setdiff1d(array1,array2))


# In[10]:


import numpy as np
a=[1,2,3,4]
print("Original array")
print(a)
print("Rapeating 2 times")
x=np.tile(a,2)
print(x)
print("Repeating 3 times")
x=np.tile(a,3)
print(x)


# In[11]:


import numpy as np
x=np.array([[10,20,30],[20,40,50]])
print("Original array:")
print(x)
y=np.ravel(x)
print("New flattend array:")
print(y)


# In[12]:


import numpy as np
#using no.full
x=np.full((3,5),2,dtype=np.uint)
print(x)
#using no.ones
y=np.ones([3,5],dtype=np.uint)*2
print(y)


# In[ ]:





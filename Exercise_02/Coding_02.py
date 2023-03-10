#!/usr/bin/env python
# coding: utf-8

# In[6]:


num=4
if num<=9:
    print("Less than ten.")
elif num==4:
    print("Equal to four.")


# In[7]:


change = 356
if change >= 100:
    print("Your change contains", change//100, "dollars.")
else:
    print("Your change contains no dollars.")


# In[8]:


a=2
b=3
c=7
if (a*b)<c:
    b=a
else:
    c=a+b+c
print(a,b,c)


# In[9]:


length=eval(input("Enter length of cloth in yards:"))
if length<1:
    cost=3.00 #cost in dollars
else:
    cost=3.00+((length-1)*2.50)
result="Cost of cloth is ${0:0.2f}.".format(cost)
print(result)


# In[12]:


number=5
if number<0:
    print("negative")
else:
    if number==0:
        print("zero")
    else:
        print("positive")


# In[14]:


major="Computer Science"
if major=="Business" or "Computer Science":
    print("Yes")


# In[16]:


if a != b:
    print("Both are unequal")
else:
    print("Both are equal")


# In[18]:


Bill=float(input("Enter amount of bill: "))
Percentage=float(input("Enter percentage tip: "))
Tip=(Bill*Percentage)/100
if Tip<2:
    print("Tip is $2")
else:
    print("Tip is" ,'$'+"{:.2f}".format(Tip))


# In[ ]:





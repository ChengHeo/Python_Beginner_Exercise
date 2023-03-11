#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot(range(1,12), sales1,'--')
line_chart2 = plt.plot(range(1,12), sales2,':')
plt.title('Monthly sales of 2016 and 2017')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.legend(['year2016', 'year 2017'], loc=4)
plt.show()


# In[11]:


import matplotlib.pyplot as plt

values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='bar', align='mid', color='g', edgecolor='black')
plt.legend()
plt.title('Histogram of score')
plt.show()


# In[9]:


import matplotlib.pyplot as plt

weight1=[63.3,57,64.3,63,71,61.8,62.9,65.6,64.8,63.1,68.3,69.7,65.4,66.3,60.7]
height1=[156.3,100.7,114.8,156.3,237.1,123.9,151.8,164.7,105.4,136.1,175.2,137.4,164.2,151,124.3]

plt.scatter(weight1,height1,c='b',marker='o')
plt.xlabel('weight', fontsize=10)
plt.ylabel('height',fontsize=10)
plt.title('scatter plot - height vs weight',fontsize=10)
plt.show()


# In[10]:


import matplotlib.pyplot as plt
import numpy as np

city=['Delhi','Beijing','Washington','Tokyo','Moscow']
pos = np.arange(len(city))
Happiness_Index=[60,40,70,65,85]

plt.bar(pos,Happiness_Index,color='blue',edgecolor='black')
plt.xticks(pos, city)
plt.xlabel('City', fontsize=10)
plt.ylabel('Happiness_Index', fontsize=10)
plt.title('Barchart - Happiness index across cities', fontsize=10)
plt.show()


# In[12]:


import matplotlib.pyplot as plt
import numpy as np

city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Gender=['Male','Female']
pos = np.arange(len(city))
Happiness_Index_Male=[60,40,70,65,85]
Happiness_Index_Female=[30,60,70,55,75]

plt.bar(pos,Happiness_Index_Male,color='blue',edgecolor='black')
plt.bar(pos,Happiness_Index_Female,color='pink',edgecolor='black',bottom=Happiness_Index_Male)
plt.xticks(pos, city)
plt.xlabel('City', fontsize=10)
plt.ylabel('Happiness_Index', fontsize=10)
plt.title('Stacked Barchart - Happiness index across cities', fontsize=10)
plt.legend(Gender,loc=2)
#plt.savefig('sample.png')
plt.show()


# In[ ]:





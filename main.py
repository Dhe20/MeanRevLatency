#!/usr/bin/env python
# coding: utf-8

# In[124]:


from sys import stdin
import numpy as np

prediction=[]

for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    
    Mean=np.mean(d)
    if Mean<d[499]:
        prediction.append(0)
    if Mean>d[499]:
        prediction.append(1)

np.savetxt('predictions.csv', prediction, delimiter=',')




# In[ ]:






    



# In[ ]:





# In[ ]:





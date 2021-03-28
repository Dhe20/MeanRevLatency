


from sys import stdin
import numpy as np

prediction=[]

for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    
    Mean=np.mean(d)
    if Mean<d[499]:
        print(0)
    if Mean>d[499]:
        print(1)
       

#np.savetxt('predictions.csv', prediction, delimiter=',')










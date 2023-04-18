
#Aufgabe 4

import numpy as np

#1.
u=np.full((42,),42)
l=list(range(0,10))

#2.
v=np.array(range(0,10))
print(v.dtype)

#3.
m=np.reshape(v,(5,2))


#4.
m=m*3.1
print(m.dtype)

#5.
m=m.astype(int)

#6.
h=m*m
print(h)
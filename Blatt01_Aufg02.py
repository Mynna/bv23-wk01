
#Aufgabe 2

#1.
l='toarmumiknif'
l=list(l)

#2.
a=l[0:5]
b=l[5:7]
c=l[7:]


#3.
erg=c+a
print(erg)
d=erg[0::2]

e=erg[1::2]



#4.
e=erg[::-1]


#5.
codewort=d+e+b
print(codewort)
print('Das Codewort ist '+ ''.join(codewort))



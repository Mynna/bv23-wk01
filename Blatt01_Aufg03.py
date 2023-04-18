
#Aufgabe 3

#1.
l=list(range(101,200,1))

#2.
def summe(list):
    a= 0
    for i in l:
        a += i
    return a

#3. 
def mittel(list):
    return summe(list)/len(list)

#4.
def teilbar5(list):
    a=[]
    for element in list:
        if element %5 ==0:
            b=element
            a.append(b)
    return len(a)  

print(teilbar5(l)) 
 
 #5.
def primL(list):
    count =0
    for i in list:
        prime = True
        for j in range(2,i):
            if (i% j)==0:
                prime=False
        if prime:
            count += 1
    return count    

#Überprüfen der Methoden
print(summe(l)) 
print(mittel(l))
print(teilbar5(l))
print(primL(l))      



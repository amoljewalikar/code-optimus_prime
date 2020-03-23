
#print even indexed numbers
l1 = [2,3,4,5,6,7,8,9,10]
i=0
len_l1 = len(l1)
print("Even indexed numbers:")
while i<len_l1:        
    if i%2==0:
        print(l1[i],end=" ")
        i+=1
    else:
        i+=1
#using slicing
print("\nEven:",l1[::2])

#print odd indexed numbers
j=0
print("\nOdd indexed numbers:")
while j<len_l1:        
    if j%2==0:
        j+=1
    else:
        print(l1[j],end=" ")
        j+=1
#using slicing
print("\nOdd:",l1[1::2])

#max from list using slicing
mymax=l1[0]
for k in l1[1:]:
    if k>mymax:
        mymax=k
else:
    print("\nMax number:",mymax)

    
#squares of numbers from list
l2 = [44,55,66,77,88]
for i in range(len(l2)):
    l2[i]=l2[i]**2
    
print("Squares of elements of list : ",l2)    






    

str1=input("enter a string:")
l1=['banana','grapes','orange']
#if str1 in l1:
#        print('yes')
lenst=len(l1)
i=0
while i<lenst:
    if l1[i]==str1:
        print(str1,'present in l1')
        break#if we dont put break here,it will iterate whole list and else
    i+=1     #part also gets executed.
else:
    print(str1,'NOT present in l1')
             
         

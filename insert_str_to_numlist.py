
str1 = input("Enter string to apply on list : ")
lst1 = [1,2,3,4]
j=0
lst2 =[]
for i in lst1:
    j=str1+str(i)
    lst2.append(j)
print(lst2)


#one-liner

#print(list(map(lambda x : str1+str(x),lst1)))

>>> q = ' '.join(lst2)
>>> q
'amol1 amol2 amol3 amol4'
>>> q.replace(' ','#')
'amol1#amol2#amol3#amol4'


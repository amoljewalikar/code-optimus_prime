
'''def dict1(d1):
    return list(d1.keys()),list(d1.values())

print(dict1(d1))
'''
#without using keys n values
d1={'A':'amol','R':'rahul','G':'amol g'}
def seperate(d1):
    l1=[]
    l2=[]
    for i in d1:
        l1.append(i)
        l2.append(d1[i])
    return l1,l2
print("(keys,values)=",seperate(d1))

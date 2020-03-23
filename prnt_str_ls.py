str1="My name is Amol"
lstr=str1.split() #take into list
j=[]
n=[]
for i in lstr:
    if len(i)==4:
        j.append(i)
for k in j:
    for m in range (0,len(j)+1):
        #print(k[:m+1],end=' ')
        n.append(k[:m+1])
print(n)

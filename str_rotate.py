name = input("Enter a string : ")
c=1
while c<len(name):
    for i in range(len(name)):
        if name[i:]+name[:i]==name:
            c+=1
print(c)


'''
count=1
for i in range(len(name)):
    if name==name[i+1:]+name[:i+1]:
        break
    else:
        count+=1
print(count)
'''

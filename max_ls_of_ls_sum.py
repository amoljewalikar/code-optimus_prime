ls=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
lsum=[]
for i in ls:
    lsum.append(sum(i))
print("By Program, max sum from list of lists:",max(lsum))


#one liner

print("By One liner : ",max(list(map(sum,ls))))



>>> [x**2 for x in ls]
[1, 4, 9, 49, 64, 81]
>>> list(map(lambda x:x**2,ls))
[1, 4, 9, 49, 64, 81]


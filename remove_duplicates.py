from itertools import groupby 
ls = [1,2,2,2,4,5,6,6,7,2,2,4,4]

for i,j in groupby(ls):
    print(i,list(j))
    

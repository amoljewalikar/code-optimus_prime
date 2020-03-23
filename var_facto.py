#with var args
def facto(*n):
    l1=[]
    for i in n:
        f=1
        while i>0:
            f*=i
            i-=1
        l1.append(f)
    return l1
print("Facto's are:",facto(3,4,5,6,8,9,12))

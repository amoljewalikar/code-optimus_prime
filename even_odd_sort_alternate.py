def even_odd_sort(n,l):
    ls = sorted(l)
    res = []
    odd = []
    even = []
    res.append(min(ls))
    ls.remove(min(ls))
    for e in ls:
        if e%2 == 0:
            even.append(e)
        else:
            odd.append(e)
    lss = even+odd[::-1]
    for e in range(len(lss)):
        if res[-1]%2==0:
            res.append(lss.pop(-1))
        else:
            res.append(lss.pop(0))
        
    return res
        
    


print(even_odd_sort(10,[77, 15, 96, 45, 42, 18, 25, 12, 48,7]))







'''


ls = l #[int(x) for x in input().split()][:n]
    t = min(ls)
    ls.remove(t)
    r = []
    r.append(t)
    t = r[-1]
    print(ls,'=',len(ls), len(r))
    for i in range(0,len(ls)-1):
        t = r[-1]
        if t%2 == 0:
            if ls[i]%2 != 0:
                r.append(ls[i])
                print("odd :",ls[i])
        if t%2 != 0:
            if ls[i]%2 == 0:
                r.append(ls[i])
                print("even :",ls[i])
        
    return r,len(r)

'''

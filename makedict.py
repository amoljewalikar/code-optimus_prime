l1=['A','B','C','D','E']
l2=['a','b','C','d','e']
def make_dict(l1,l2):
    d1={}
    ls1=set(l1)
    ls2=set(l2)
    lnlst=len(ls1)
    if len(ls1)==len(ls2):
        print("Lengths are same")
        for i in range(0,lnlst):
            if l1[i]==l2[i]:
                print("Found Duplicates")
                break
            d1[l1[i]]=l2[i]
    else:
        print("Dictionary is NOT possible")
    return d1
print("Dictionary is :\n",make_dict(l1,l2))

        

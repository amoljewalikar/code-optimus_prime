l1=[15,[44,[99,89]],[[11,22,33,[3,6,65]],99,[105,200,201],200]]
def rec_sum(l1):
    total=0
    tmp=[]
    for i in l1:
        if type(i)==int:
            total+=i
        else:
            total+=rec_sum(i)        
    return total        
print("Total :",rec_sum(l1))

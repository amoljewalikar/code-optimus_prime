n = int(input("Enter a number,to print first N PRIMES : "))
print("Primes are :")

for i in range(2,n+1):
    j=i
    k=1
    m=0
    while k<=j:
        if j%k==0:
            m+=1
            if m>2:
                break
        k+=1
    if m==2:
        print(i,end=" ")

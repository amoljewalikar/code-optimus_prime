n=int(input("Enter a num to calculate factorial : "))
def facto(n):
    f=1
    while n>0:
        f*=n
        n-=1
    return f
print("factorial of ",n,"is : ",facto(n))  

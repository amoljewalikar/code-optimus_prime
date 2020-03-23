n = int(input("Enter a number,to print first N PRIMES : "))
i=1
j=0

while i<=n//2:
    if n%i==0:
        j+=1
    i+=1
    
if(j>1):
    print(n,"is NOT a prime number")
else:
    print(n,"is a prime number")
            

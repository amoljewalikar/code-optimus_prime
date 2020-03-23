num = int(input("Enter a number to check prime : "))

def prime(num):
    i=2
    j=0
    while i<=num//2+1:
        if num%i==0:
            return num,False      
        i+=1
    else:
        return num,True
print(num,"Is prime? : ",prime(num))        


'''
#using for loop
def prime():
    for i in range(2,num//2+1):
        if num%i==0:
            return num,False
    else:
        return num,False
'''

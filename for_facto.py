
#Factorial of a number, using FOR LOOP

num=int(input("Enter a num : "))
j=1
for i in range(2,num+1):
    j*=i
print('Factorial of ',num,'is : ',j)



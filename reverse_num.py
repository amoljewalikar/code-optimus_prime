num=int(input("Enter a number : "))
rev_num=0
while num>0:
    val=num%10
    rev_num=(rev_num*10)+val
    num=num//10
print(rev_num)

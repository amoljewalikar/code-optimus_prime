
#Print single digit addition of given any number
num= int(input("Enter a number : "))
def foo(num):
    summ=0
    while num>0:
        val=divmod(num,10)
        num=val[0]
        summ+=val[1]
    else:
        if summ>9:
            foo(summ)
        else:
            print(summ)
foo(num)

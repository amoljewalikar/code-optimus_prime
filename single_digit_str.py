num=input("Enter a number : ")
def foo(num):
    t=0
    for i in num:
        t+=(int(i))
    if(len(str(t))>1):
       foo(str(t))
    else:
        print(t)
       
foo(num)

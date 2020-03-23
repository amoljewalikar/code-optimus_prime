stack = []
while True:
    print("===== Stack Implementation in LIST =====")
    print("\n1.Push\n2.Pop\n3.Peek/Top\n4.IsEmpty\n5.Exit")
    ch = int(input("\nEnter your choice : "))
    if ch == 1:
        n = int(input("\nEnter how many numbers you want to push : "))
        for i in range(n):
            a = int(input("Enter a num : "))
            stack.append(a)
        print("\nStack is : ",stack)
    if ch == 2:
        if stack != []:
            print("\nPopped element",stack.pop(),"from stack.")
        else :
            ch = 4
    if ch == 3:
        if stack != []:
            print("\nPeek or Top Element is : ",stack[-1])
        else:
            ch = 4
    if ch == 4:
        if stack == []:
            print("\nStack is Empty !!")
        else:
            print("\nStack is NOT empty!!")
    if ch == 5:
        break
            

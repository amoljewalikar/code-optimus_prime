#using slicing
name = (input("Enter a string : "))

if name==name[::1]:
    print(name,"is a palindrome")
else:
    print(name,"is not a palindrome")


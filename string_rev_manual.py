#1)take a string as input and print reverse manually

name = input("Enter a string : ")
l = len(name)-1
name1=''
while l>=0:
    name1+=name[l]
    l-=1
print(name1)


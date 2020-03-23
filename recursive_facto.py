#recursive
num=int(input("Enter a num : "))
def rec_facto(num):
    if num==1:
        return 1
    else:
        return num*(num-1)

print("Facto is : ",rec_facto(num))

s='999Ni  12 $ t4901 # i  $ n 44'
s1=''
for i in s:
    if i.isalpha():
        s1+=i
print("Filtered String : ",s1)
#if s1.islower()==s1.islower()[::-1]:
if s1.islower()==(s1[::-1]).islower():
    print(s1,"is Palindrome")
else:
    print(s1,"is NOT Palindrome")




'''
example 1:

l1=[2,3,5,55]
l1.append(99)[-3:]
   -is not possible coz append throws 'None'
   -slicing can be done where function returns something str/num

example 2:
l1,l2,l3

l1.extend(l2.extend(l3))
   -is not possible coz extend throws 'None'

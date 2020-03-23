#variable arguments... symbol used , '*' and it takes as a Tuple
#a=int(input("Enter number(s): "))
a=(12,43,55,87)
def square_var_args(*a):
    l1=[]
    for i in a:
        l1.append(i**2)
    return l1
print("\nSquare(s) of given argument(s)",square_var_args(*a))
    
'''
l1=[2,4,6,8]
l2=[1,2,]
l3=[66,5]
def addlist(*a):
    for i in a:
        i.append(99)
'''

'''
'**' takes var_args as dictionary
def display(**a):
	for i in a:
		print(i,a[i])

o/p		
>>>display(name='amol',roll=5)
name amol
roll 5
'''

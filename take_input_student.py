#ideal Structure

d1={}
for i in range(1,4):
    roll=int(input("Enter Roll Number : "))
    d1[roll]={}
    d1[roll]['Name']=input("Enter name of Student : ")
    d1[roll]['Marks']={}
    d1[roll]['Marks']['Maths'] = int(input("Enter marks of Maths Subject : "))
    d1[roll]['Marks']['English'] = int(input("Enter marks of English Subject : "))
print(d1)

'''
d1={}
roll=int(input("Enter Roll Number : "))
d1[roll]={}
d1[roll]['Name']=input("Enter name of Student : ")
d1[roll]['Marks']={}
d1[roll]['Marks']['Maths'] = int(input("Enter marks of Maths Subject : "))
d1[roll]['Marks']['English'] = int(input("Enter marks of English Subject : "))

#print(d1)

d2={}
roll=int(input("Enter Roll Number : "))
d2[roll]={}
d2[roll]['Name']=input("Enter name of Student : ")
d2[roll]['Marks']={}
d2[roll]['Marks']['Maths'] = int(input("Enter marks of Maths Subject : "))
d2[roll]['Marks']['English'] = int(input("Enter marks of English Subject : "))

#print(d1)

d3={}
roll=int(input("Enter Roll Number : "))
d3[roll]={}
d3[roll]['Name']=input("Enter name of Student : ")
d3[roll]['Marks']={}
d3[roll]['Marks']['Maths'] = int(input("Enter marks of Maths Subject : "))
d3[roll]['Marks']['English'] = int(input("Enter marks of English Subject : "))

print(d1[roll]['Name'])
'''

class Student:
    count=0     #-> this is a class variable
    def __init__(self,gname,groll,gnation='India'):
        self.name = gname
        self.roll = groll
        self.nation = gnation  #name,roll,nation are object variables
        Student.count+=1
    def display(self):
        #print('Name: ',self.name)
        #print('Roll: ',self.roll)
        #print('Roll: ',self.nation)
        return self.name,self.roll,self.nation

s1 = Student("Amol",101,'NewZeland')
s2 = Student("Rahul",102)
s3 = Student("Amol G",103,"Australia")
print(s1.display())
print(s2.display())
print(s3.display())
print(Student.count)

'''
for i in range(1,3):
    arg =list((input(),input(),input()))
    s = Student(arg[0],arg[1],arg[2])
    s.display()

'''

from ClassObjCreation import Employee
class Programmer(Employee):
    def __init__(self,getname,getsal,getproject):
        Employee.__init__(self, getname,getsal)
        self.project=getproject
    def displayEmployee(self):
        super(Programmer,self).displayEmployee()
        print("Project:", self.project)
class Manager(Employee):
    pass
p1=Programmer('Jatin',50000,'TMO')
m1=Manager('Pradeep',100000)
p1.displayEmployee()
m1.displayEmployee()
Employee.displayCount()
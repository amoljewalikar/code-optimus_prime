class Employee:
	empCount = 0
	empNation = 'India'
	def __init__(self,getname,getsalary=20000):
		self.name = getname
		self.salary = getsalary
		Employee.empCount += 1
	def displayEmployee(self):
		print("Name :",self.name,"\nSalary :",self.salary)
		print('Country : ',self.empNation)
	@classmethod
	def displayCount(cls):
		print("Total Employee:", cls.empCount)
		print("Nation : ",cls.empNation)
	@staticmethod
	def sample():
		print("Asach!!!")

e1 = Employee('Amol',100000)
e1.displayEmployee()
e1.displayCount()
Employee.sample()
Employee.displayCount()

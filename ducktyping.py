class Pycharm:
	def execute(self):
		print('Compiling')
		print('Running')
class Mycharm:
    def execute(self):
        print('SpellCheck')
        print ('Compiling')
        print ('Running')
class Laptop:
	def code(self,a):
		a.execute()
l1=Laptop()
p1=Pycharm()
m1=Mycharm()
print("Passing Object of Mycharm Class:\n")
l1.code(m1)
print("\nPassing Object of Pycharm Class:\n")
l1.code(p1)

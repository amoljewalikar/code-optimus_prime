class A:
    def __init__(self, geta):
        self.a = geta
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob5= A(3)
ob6= A(3)
#ob1.a+ob2.a
print(ob1+ob2) #ob1.__add__(ob2)
ob3 = A("I'm")
ob4 = A(" a boy")
#print(ob3 + ob4)
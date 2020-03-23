class Student:
    def hello(self, name=None,roll=123):
        if name is not None:
            print('Hey ' + name)
        else:
            print('Hey ')
        print(roll)
std = Student()
std.hello()
std.hello('Nicholas')
std.hello('Amit',567)
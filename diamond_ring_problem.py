"""
Diamond Ring Problem
Multiple inheritance problem
"""

class A:
    def print_something(self):
        print("I am from class A")
class B(A):
    # def print_something(self):
    #     print("I am from class B")
    pass
class C(A):
    def print_something(self):
        print("I am from class C")
class D(B, C):
    # def print_something(self):
    #     print("I am from class D")
    pass


obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_something() # I am from class A
obj2.print_something() # I am from class A
obj3.print_something() # I am from class C
obj4.print_something() # I am from class C
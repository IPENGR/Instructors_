'''
single inherintance
multi level inheritance
multiple inheritance
hierachical inheritance

'''

#single inheritance
'''
class parent():
    def a(self):
        print("iam the parent")
class child(parent):
    def b(self):
        print("iam the child")

c=child()
c.a()
c.b()

'''

#multilevel inheritance

'''
class grandmother():
    def a(self):
        print("iam the grandmother")
class parent(grandmother):
    def b(self):
        print("iam the parent")
class child(parent):
    def c(self):
        print("iam the child")

d=child()
d.a()
d.b()
d.c()

'''

#multiple inheritance

'''
class mother():
    def a(self):
        print("iam the mother")
class father():
    def b(self):
        print("iam the father")
class child(mother,father):
    def c(self):
        print("iam the child")

d=child()
d.c()
d.a()
d.b()

'''

#hierachical inheritance

class mother():
    def a(self):
        print("iam the mother")
class child1(mother):
    def b(self):
        print("iam the child1")
class child2(mother):
    def c(self):
        print("iam the child2")

d=child1()
d.b()
d.a()
e=child2()
e.a()
e.c()

class B:
    """类B"""
    VarB = 0
    def __init__(self,name):
        self.name = name
        print('调用B类构造函数')

    def handle(self):
        print("B.handle")


class A(B):
    """类A"""
    VarA = 1
    def __init__(self,age):
        self.age = age
        super().__init__('abc')2
        print('调用A类构造函数')

    def handle(self):
        super().handle()
a = A(25)
print(a.VarB)
print(a.VarA)
print(a.name)
print(a.age)
a.handle()
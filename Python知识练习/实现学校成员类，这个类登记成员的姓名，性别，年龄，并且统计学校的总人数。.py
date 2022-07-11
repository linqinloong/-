class SchoolMember:
    #总人数，这个是类的变量
    sum_member = 0
    name = ''
    sex = ''
    age = 0
    #__init__方法在类的对象被创建时执行
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
        SchoolMember.sum_member += 1
        print("学校新加入一个成员:%s"%self.name)
        print("现在有成员%d人"%SchoolMember.sum_member)
    #自我介绍
    def say_hello(self):
        print("大家好，我叫:%s,%d岁"%(self.name,self.age))
    #__del__方法在对象不使用的时候运行
    def __del__(self):
        SchoolMember.sum_member -= 1
        print("%s离开了，学校还有%d人"%(self.name,SchoolMember.sum_member))


    #老师类继承学校成员类
class Teacher(SchoolMember):
    def __init__(self,name,sex,age,zhicheng):
        #SchoolMember.__init__(self,name,sex,age,zhicheng)错了，zhicheng应该没有(因为父类没有)，不然会导致参数错误
        SchoolMember.__init__(self,name,sex,age)
        self.zhicheng = zhicheng

    def say_hello(self):
        SchoolMember.say_hello(self)
        print("我是老师，我的职称是:%s"%self.zhicheng)

    def __del__(self):
        SchoolMember.__del__(self)


class Student(SchoolMember):
    def __init__(self,name,sex,age,score):
        SchoolMember.__init__(self,name,sex,age)
        self.score = score

    def say_hello(self):
        SchoolMember.say_hello(self)
        print("我是学生，我的成绩是:%d"%self.score)

    def __del__(self):
        SchoolMember.__del__(self)

t = Teacher(name="张三",sex="男",age=35,zhicheng=1)
t.say_hello()
"""
s = Student(name='李四',sex="男",age=18,score=100)
s.say_hello()
"""
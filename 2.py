class Student:
    count = 0 #计数
    def __init__(self,name,age,count=0):
        self.name = name
        self.age = age
        self.count = count
        self.count +=1
        Student.count += 1 #要使得变量全局有效，就定义为类的属性
    def __del__(self):
        if Student.count>1:
            Student.count -=1
    def learn(self):
        print(self.name,"is learning")
s1 = Student('张三',111)
s2 = Student('李四',222)
s3 = Student("王五",333)
s1.learn()
print(Student.count)
print(s1.count)
print(s2.count)
print(s3.count)
del s1
print(Student.count)


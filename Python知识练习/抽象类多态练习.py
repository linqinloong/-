from abc import ABCMeta,abstractmethod
from tkinter import *
class Shape(object):
    def draw(self):
        __metaclass__ = ABCMeta
        root = None
        cv = None
        def __init__(self):
            self.color = 'black'  #默认使用黑色
        @abstractmethod
        def draw(self):pass


class Circle(Shape):
    def __init__(self,x1,y1,x2,y2):  #定义圆的外接矩形
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.root = Tk()
        self.cv = Canvas(self.root,bg='white',width=300,height=200)
    def draw(self):
        self.cv.create_oval(self.x1,self.y1,self.x2,self.y2)
        self.cv.pack()
        self.root.mainloop()


class Line(Shape):
    def __init__(self,x1,y1,x2,y2):  #定义线的坐标
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.root = Tk()
        self.cv = Canvas(self.root,bg='white',width=300,height=200)
    def draw(self):
        self.cv.create_line(self.x1,self.y1,self.x2,self.y2)
        self.cv.pack()
        self.root.mainloop()


class Rectangle(Shape):
    def __init__(self,x1,y1,x2,y2):  #定义左上和右下点的坐标值
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.root = Tk()
        self.cv = Canvas(self.root,bg='white',width=300,height=200)
    def draw(self):
        self.cv.create_rectangle(self.x1, self.y1, self.x2, self.y2)
        self.cv.pack()
        self.root.mainloop()

a = Circle(x1=0,y1=0,x2=210,y2=200)
print(a.draw())
#print(a.draw(x1=0,y1=0,x2=210,y2=200))#是错误的，因为在把类实例化的时候构造函数就需要x1,y1,x2,y2了
b = Line(0,0,200,200)
print(b.draw())
c = Rectangle(0,0,200,200)
print(c.draw())
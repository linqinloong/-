"""a="2+3"
print(eval(a))"""
#print(sorted([6,11,205,14,16,216,36,51,12,56,73,93]))

"""class corrdinate():
    #坐标
    def __init__(self,monkey,peach,box):
        print("这是一个新的类")
        list1 = []
        list1.append(monkey)  # -1 or 0 or 1
        list1.append(peach)  # 1 0 1都可以
        list1.append(box)  # 1 或者 不是-1"""
"""    def inputval(monkey,peach,box):    #def inputval(monkey,peach,box,relativeposition)
        list1 = []
        list1.append(monkey)        #-1 or 0 or 1
        list1.append(peach)         #1 0 1都可以
        list1.append(box)           #1 或者 不是-1
        #list1.append(relativeposition)"""

def corrdinate(monkey,peach,box):
    #坐标
    list1 = []
    list1.append(monkey)  # -1 or 0 or 1
    list1.append(peach)  # 1 0 1都可以
    list1.append(box)  # 1 或者 不是-1
    return list1


list2 = corrdinate(-1,0,1)
print(list2)

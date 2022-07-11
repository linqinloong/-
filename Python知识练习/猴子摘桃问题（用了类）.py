class location():
    def corrdinate(monkey,peach,box):
        #坐标
        list1 = []
        list1.append(monkey)  # -1 or 0 or 1
        list1.append(peach)  # 1 0 1都可以
        list1.append(box)  # 1 或者 不是-1
        return list1
"""    def inputval(monkey,peach,box):    #def inputval(monkey,peach,box,relativeposition)
        list1 = []
        list1.append(monkey)        #-1 or 0 or 1
        list1.append(peach)         #1 0 1都可以
        list1.append(box)           #1 或者 不是-1
        #list1.append(relativeposition)"""

"""def monkeymove(list):       #list[0]猴子 list[1]桃子 list[2]箱子
    a = list[1] - list[0]
    return a"""

def monkeymovebox(list):
    if list[0] < 0:
        g = list[0] - list[2] + 1
    else:
        g = list[0] - list[2] - 1
    return g

def boxmovepeach(list):
    b = list[2] - list[1]
    return b

def relativeposition(list):
    c = list[0] - list[2]
    return c

def main():
    x = input("请输入猴子，桃子，箱子的位置")
    xlist = x.split(" ")
    xlist = [int(xlist[i]) for i in range(len(xlist))]  #把每个字符转成int值
    #print(xlist)
    list1 = location.corrdinate(int(xlist[0]),int(xlist[1]),int(xlist[2]))
    #print(list1)
    #a = monkeymove(list1)
    b = boxmovepeach(list1)
    c = relativeposition(list1)
    g = monkeymovebox(list1)
    #e = a + 1
    print("数据正值说明往左移动，数据负值说明往右移动")
    print("猴子与箱子的相对位置为%d"%(c))
    print("猴子移动到箱子的相邻位置要走%d" % g)
    print("箱子要移动%d个单位即可到达桃子下方" % (b))
    #print("猴要移动%d个单位到达桃子下方"%(b+1))
    print("因为猴子要爬上箱子才能拿到桃子，猴子总共要运动%d步才能摘到桃子"%(abs(g)+abs(b)+1))


if __name__ == '__main__':
    main()


"""list1 = []
member = 1
while(member != 0):
    member =eval(input("输入数据"))
    list1.append(member)
print(list1)"""
#依题意，这是一个一维坐标系，且只能在[-1,0,1]上运动,既然纵坐标都是0，那么为什么我不直接用一维列表做呢？
#猴子可推拉箱子
#最终目的：猴子在某一状态下（设猴子位置为A，桃子位置在B，箱子位置为C），如何行动可摘取到桃子
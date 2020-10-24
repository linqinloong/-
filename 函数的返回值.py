def fun(list):
    list1 = []
    for i in range (len(list)):
        if list[i] %2 != 0:
            list1.append(list[i])
    return list1
list = [1,2,3,4,5,6,7,8,9,10]
list2 = fun(list)
print(list2)
"""
fun(list = [1,2,3,4,5,6,7,8,9,10])
list2 = fun(list)
是错误的
因为fun括号后把fun(list=....)变成了一个类
"""
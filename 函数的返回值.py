"""
函数的返回值

Version: 0.1
Author: 晏雨新
Date: 2018-09-27
"""
def fun(list):
    list1 = []
    for i in range (len(list)):
        if list[i] %2 != 0:
            list1.append(list[i])
    return list1
#fun(list = [1,2,3,4,5,6,7,8,9,10])
#list2 = fun(alist)
list = [1,2,3,4,5,6,7,8,9,10]
list2 = fun(list)
print(list2)

"""
 最好不要用list这种特殊字符
 fun(list = [1,2,3,4,5,6,7,8,9,10])
 错在fun不接受字符串变量，所以fun函数读不到长度。或者把fun改成有默认值的函数就能读到了。
"""
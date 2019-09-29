"""
使用可变长参数计算任意个指定数字之和

Version: 0.1
Author: 晏雨新
Date: 2018-09-27
"""

def sum(*nums):
    print("nums:",nums)
    sum = 0
    for num in nums:
        sum += num**2     #1**2+2**2+3**3
        print("sum = %d"%(sum))
sum(1,2,3)

"""
def SumFun(*args):
    result = 0
    for x in args[0:]:
      result += x
    return result
print(SumFun(2, 4))
print(SumFun(1,2,3,4,5))
print(SumFun())
"""
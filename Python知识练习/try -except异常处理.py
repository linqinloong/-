"""
try -except异常处理
Version: 0.1
Author: 晏雨新
Date: 2019-09-27
"""
def fun(num1,num2):
    num3 = num1/num2
    print("两数相除结果:%d"%num3)
try:
    fun(num1=4,num2=2)
    fun(num1=4, num2=0)
except Exception as e:
    print(e)
finally:
    print("执行完成")
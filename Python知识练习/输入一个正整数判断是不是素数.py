"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 晏雨新
Date: 2018-09-26
"""
#素数指的是只能被1和自身整除的大于1的整数。
from math import sqrt
num=int(input("请输入一个正整数:"))
end=num-1
panduan=0
if num==1 or num==3:
    print("这个正整数是素数")
    panduan=1

if panduan==0:
    for i in range(2,end+1):
        if num%i==0:
            print("这个正整数是素数")
        else:
            print("这个正整数不是素数")
""""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
"""

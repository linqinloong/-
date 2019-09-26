"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
time:2019.9.25  22:34
Author: 晏雨新
"""

length1=float(input("第一条边长:"))
length2=float(input("第二条边长:"))
length3=float(input("第三条边长:"))
if length1+length2>length3 and length1+length3>length2 and length2+length3>length1:
  #  print("周长：%f",length1+length2+length3)    是错的
  print("周长:%f" %(length1 + length2 + length3))    #是对的
  p=(length1+length2 +length3)/2
  area=(p*(p-length1)*(p-length2)*(p-length3))**0.5
  print("面积:%f"%area)
else:
    print("不能构成三角形")

"""
错误：
1.海伦公式记忆不清
2.if else 语句中的冒号又忘了
3.print中传值的语法记忆不清。
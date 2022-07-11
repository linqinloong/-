"""
Version: 0.1
time:2019.9.25  22:04
Author: 晏雨新
"""
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
"""
做这个程序时出现的错误：
1.input("内容")前应该加个指定的数字类型
2.if score>=90后没加:
3.grade="A""A"是字符应该加引号
4.最后的print应该是不用缩进的，不然只有输入值低于60时才会输出'对应的等级是:'
"""
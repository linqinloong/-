"""
Version: 0.1
time:2019.9.25  22:54
Author: 晏雨新
"""
from random import randint

face = randint(1, 6)
if face == 1:
    result = '打DOTA2'
elif face == 2:
    result = '洗碗'
elif face == 3:
    result = '炒菜'
elif face == 4:
    result = '学英语'
elif face == 5:
    result = '学python'
else:
    result = '看小说'
print(result)
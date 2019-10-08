"""
在屏幕上显示跑马灯文字
Version: 0.1
Author: 晏雨新
Date: 2019-10-08
"""
import os
import time


def main():
    content = 'O(∩_∩)O哈哈~~~~~~~~'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

#while True 语句中一定要有结束该循环的break语句，否则会一直循环下去的
#while则是逻辑运算

if __name__ == '__main__':
    main()
def guess(num1, num2):
    if num1 < num2:
        print('太小了！')
        return 0;
    elif num1 > num2:
        print('太大了！')
        return 0;
    else:
        print('猜对了！')
        return 1


from random import randint

num = randint(0, 100)
print('猜猜我在想什么？')
bingo = 0
while bingo == 0:
    answer = int(input())
    bingo = guess(answer, num)

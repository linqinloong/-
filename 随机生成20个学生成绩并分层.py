import random
def ran(n):
    if n >90:
        return 'A'
    elif 80 < n < 89:
        return 'B'
    elif 70 < n < 79:
        return 'C'
    elif 60 < n < 69:
        return 'D'
    else:
        return 'E'

def main():
    for i in range(1,21):
        score=random.randint(1,100)
        print('得分%s,等级为%s'%(score,ran(score)))

main()
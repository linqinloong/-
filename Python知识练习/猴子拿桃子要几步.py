class Monkey():
    def monkeymovebox(self,a, b):  # a猴位置，b箱子位置1 0;-1,0
        if a > b:
            a = a - 1
            print("当a等于零的时候说明猴子向左移动了1个单位长度")
            print("a=%d" % (a))
        else:
            a = a + 1
            print("当a等于零的时候说明猴子向右移动了1个单位长度")
            print("a=%d" % (a))
        return a

    def boxmovepeach(self,b,c):     #b是箱子位置，c是桃子位置 1,0；-1,0
        if b>c:
            b=b-1
            print("当b等于零的时候说明猴子向左移动了1个单位长度")
            print("b=%d"%(b))
        else:
            b=b+1
            print("当b等于零的时候说明猴子向右移动了1个单位长度")
            print("b=%d"%(b))
        return b

    def mgetp(self,a,b):
        if a == 0 and b == 0 :
            f = 3
        elif a == 0 or b ==0 :
            f = a + b + 2
        else:
            f = a + b + 1
        print("f=%d"%(f))
        return f

def main():
    print("-1代表A处，0代表B处，1代表C处，2代表猴子在箱子下，3代表猴子在箱子上")
    a = int(input("猴子的位置："))
    b = int(input("箱子的位置："))
    c = int(input("桃子的位置："))
    #print(a,b,c)
    A = Monkey()
    d = A.monkeymovebox(a,b)
    e = A.boxmovepeach(b,c)
    o = A.mgetp(d,e)
    print("总步数为:%d"%(o))

if __name__ == '__main__':
    main()


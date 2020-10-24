# -*- coding: utf-8 -*-

class State:   #1此处作用是（定义一个State类，并给猴子，箱子，桃子，相对位置一个默认值）
    def __init__(self, monkey=-1, box=0,peach=1, monbox=-1):
        self.monkey = monkey  # -1:Monkey at A  0: Monkey at B  1:Monkey at C
        self.box = box      # -1:box at A  0:box at B  1:box at C
        self.peach = peach   # Banana at C,Banana=1
        self.monbox = monbox  # -1: monkey not on the box  1: monkey on the box
#2.以下函数作用是(复制一个State,保存中间状态信息)
def copyState(source):
    state = State()   #3.该语句作用是（类的实例化）
    state.monkey = source.monkey    #4.该语句作用是（把用于传值的source类中的猴子的位置来传给类的实例对象state中的猴子位置。）
    state.box = source.box
    state.peach = source.peach
    state.monbox = source.monbox
    return state    #5.该语句作用是（返回一个类的实例state）

def monkeygoto(b,i):   #6.该函数作用是（确定猴子位置，并在相应语句上插入信息）
    a=b
    if (a==-1):
        routesave.insert(i,"Monkey go to A")  #7.该语句作用是（在列表routesave的i位置插入信息“Monkey go to A”）
        state.monkey = States[i].monkey
        States[i+1]=copyState(States[i])
        States[i+1].monkey=-1
    elif(a==0):
        routesave.insert(i,"Monkey go to B")   #8.该语句作用是（在列表routesave的i位置插入信息“Monkey go to B”）
        States[i+1]=copyState(States[i])
        States[i+1].monkey=0
    elif(a==1):
        routesave.insert(i,"Monkey go to C")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=1
    else:
        print("parameter is wrong")


def movebox(a,i):    #9.该函数作用是（移动箱子）
    B=a
    if(B==-1):
        routesave.insert(i,"Monkey move box to A")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=-1   #10.该语句作用是（使猴子在A处）
        States[i+1].box=-1   #11.该语句作用是（使箱子在A处）
    elif(B==0):
        routesave.insert(i,"Monkey move box to B")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=0
        States[i+1].box=0
    elif(B==1):
        routesave.insert(i,"Monkey move box to C")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=1
        States[i+1].box=1
    else:
        print("parameter is wrong")

def climbonto(i):    #12.该函数作用是（猴子爬上箱子）
    routesave.insert(i,"Monkey climb onto the box")
    States[i+1]=copyState(States[i])
    States[i+1].monbox=1   #13.该语句作用是（使猴子在箱子上）

def climbdown(i):
    routesave.insert(i,"Monkey climb down from the box")
    States[i+1]=copyState(States[i])
    States[i+1].monbox=-1



def reach(i):
    routesave.insert(i,"Monkey reach the peach")

def showSolution(i):   #14.该函数作用是（解决问题）
    print ("Result to problem:")
    for c in range(i+1):
        print("Step %d : %s \n"%(c+1,routesave[c]))
    print("\n")   #15.该语句作用是（换行）


'''
perform next step
'''
def nextStep(i):
    #print States[i].box
    if(i>=150):  #16.该语句作用是（判断步骤长度有没有大于150）
        print("%s  \n", "steplength reached 150,have problem ")

    if(States[i].monbox==1 and States[i].monkey==States[i].peach and States[i].peach==States[i].peach and States[i].box==States[i].peach):
        showSolution(i)   #17.该语句作用是（在上述条件下，展示结果）
        exit(0)           #18.该语句作用是（表示程序中断，但是程序是正常退出的）
    j=i+1

    if(States[i].box==States[i].peach):
        if(States[i].monkey==States[i].peach):
            if(States[i].monbox==-1):
                climbonto(i)
                reach(i+1)
                nextStep(j)    #monkeygoto(-1,i)  nextStep(j)  monkeygoto(0,i)   nextStep(j)    movebox(-1,i)    nextStep(j)     movebox(0,i)    nextStep(j)
            else:
                reach(i+1)
                nextStep(j)    #climbdown(i)  nextStep(j)
        else:
            monkeygoto(States[i].box,i)
            nextStep(j)

    else:
        if(States[i].monkey==States[i].box):
            if(States[i].monbox==-1):
                movebox(States[i].peach, i)   #19.该语句作用是（判断States[i].peach所处的状态并移动盒子）
                nextStep(j)
            else:
                climbdown(i)
                nextStep(j)
        else:
            monkeygoto(States[i].box, i)
            nextStep(j)


if __name__ == "__main__":
    s = input("please input state: monkey, box, peach, ifMonkeyIsOnBox: \n")
    states = s.split(" ")   #20.该语句作用是（用空格分隔字符串s并把字符串用列表的形式给states）
    state = State(int(states[0]), int(states[1]), int(states[2]), int(states[3]))
    #state = State()
    States = [None]*150     #这个就是创建了150个值为None的列表
    routesave = [None]*150
    States.insert(0,state)
    nextStep(0)


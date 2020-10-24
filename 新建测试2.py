# -*- coding: utf-8 -*-
'''
@author: xinghuazhang
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: xing_hua_zhang@126.com
@software: PyCharm 2017.1.4
@file: MpickBanana.py
@time: 2017/12/19 22:38
@desc:
'''
class State:
    def __init__(self, monkey=-1, box=0,banana=1, monbox=-1):
        self.monkey = monkey  # -1:Monkey at A  0: Monkey at B  1:Monkey at C
        self.box = box      # -1:box at A  0:box at B  1:box at C
        self.banana = banana   # Banana at C,Banana=1
        self.monbox = monbox  # -1: monkey not on the box  1: monkey on the box

def copyState(source):
    state = State()
    state.monkey = source.monkey
    state.box = source.box
    state.banana = source.banana
    state.monbox = source.monbox
    return state
'''
function monkeygoto,it makes the monkey goto the other place
'''
def monkeygoto(b,i):
    a=b

    if (a==-1):
        routesave.insert(i,"Monkey go to A")
        state.monkey = States[i].monkey
        States[i+1]=copyState(States[i])
        States[i+1].monkey=-1
    elif(a==0):
        routesave.insert(i,"Monkey go to B")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=0
    elif(a==1):
        routesave.insert(i,"Monkey go to C")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=1
    else:
        print("parameter is wrong")
'''
end function monkeyygoto
'''

'''
function movebox,the monkey move the box to the other place
'''
def movebox(a,i):
    B=a
    if(B==-1):
        routesave.insert(i,"Monkey move box to A")
        States[i+1]=copyState(States[i])
        States[i+1].monkey=-1
        States[i+1].box=-1
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
'''
end function movebox
'''

'''
function climbonto,the monkey climb onto the box
'''
def climbonto(i):
    routesave.insert(i,"Monkey climb onto the box")
    States[i+1]=copyState(States[i])
    States[i+1].monbox=1
'''
end function climbonto
'''

'''
function climbdown,monkey climb down from the box
'''
def climbdown(i):
    routesave.insert(i,"Monkey climb down from the box")
    States[i+1]=copyState(States[i])
    States[i+1].monbox=-1
'''
end function climbdown
'''

'''
function reach,if the monkey,box,and banana are at the same place,the monkey reach banana
'''
def reach(i):
    routesave.insert(i,"Monkey reach the banana")
'''
end function reach
'''

'''
output the solution to the problem
'''
def showSolution(i):
    print ("Result to problem:")
    for c in range(i+1):
        print("Step %d : %s \n"%(c+1,routesave[c]))
    print("\n")
'''
end function showSolution
'''

'''
perform next step
'''
def nextStep(i):
    #print States[i].box
    if(i>=150):
        print("%s  \n", "steplength reached 150,have problem ")

    if(States[i].monbox==1 and States[i].monkey==States[i].banana and States[i].banana==States[i].banana and States[i].box==States[i].banana):
        showSolution(i)
        exit(0)
    j=i+1

    if(States[i].box==States[i].banana):
        if(States[i].monkey==States[i].banana):
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
                movebox(States[i].banana, i)
                nextStep(j)
            else:
                climbdown(i)
                nextStep(j)
        else:
            monkeygoto(States[i].box, i)
            nextStep(j)


if __name__ == "__main__":
    s = raw_input("please input state: monkey, box, banana, ifMonkeyIsOnBox: \n")
    states = s.split(" ")
    state = State(int(states[0]), int(states[1]), int(states[2]), int(states[3]))
    States = [None]*150
    routesave = [None]*150
    States.insert(0,state)
    nextStep(0)
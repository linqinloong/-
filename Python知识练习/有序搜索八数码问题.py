import numpy as np

class State:
    def __init__(self, state, directionFlag=None, parent=None, depth=1):
        self.state = state
        # state is a ndarray with a shape(3,3) to storage the state
        self.direction = ['up', 'down', 'right', 'left']
        if directionFlag:
            self.direction.remove(directionFlag)        #删除需要删除的方向标
            # record the possible directions to generate the sub-states
        self.parent = parent
        self.symbol = ' '
        self.answer = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])
        self.depth = depth
        # calculate the num of elements which are not in the proper position
        num = 0
        for i in range(len(state)):
            for j in range(len(state)):
                if self.state[i, j] != ' 'and self.state[i, j] != self.answer[i, j]:
                    num += 1
        self.cost = num + self.depth

    def getDirection(self):             #得到方向
        return self.direction

    def showInfo(self):                 #展示每一个方向
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end='  ')
            print("\n")
        print('->')
        return

    def getEmptyPos(self):              #得到一个空的点
        postion = np.where(self.state == self.symbol)       #输出满足()内的条件，即非零的坐标
        return postion
    def generateSubStates(self):        #使形成副本类
        if not self.direction:
            return []
        subStates = []
        boarder = len(self.state) - 1
        # the maximum of the x,y
        row, col = self.getEmptyPos()        #空格的行，列坐标给row和col
        if 'left' in self.direction and col > 0:
        #it can move to left place
            s = self.state.copy()           #深拷贝不会随state修改而修改
            temp = s.copy()
            s[row, col] = s[row, col-1]     #row是纵坐标，col是横坐标，例如(1,1)变(0,1)向左移动了一格
            s[row, col-1] = temp[row, col]  #有值的数右移一位到原来空格位置
            news = State(s, directionFlag='right', parent=self, depth=self.depth+1)     #一个新类的实例对象news。
            subStates.append(news)          #新类news，删了right添加到副本类中
        if 'up' in self.direction and row > 0:
        #it can move to upper place
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row-1, col]
            s[row-1, col] = temp[row, col]
            news = State(s, directionFlag='down', parent=self, depth=self.depth+1)
            subStates.append(news)          #删了down再加入副本类中
        if 'down' in self.direction and row < boarder:
            #it can move to down place
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row+1, col]
            s[row+1, col] = temp[row, col]
            news = State(s, directionFlag='up', parent=self, depth=self.depth+1)
            subStates.append(news)          #删了up再加入副本类中
        if self.direction.count('right') and col < boarder:
            #it can move to right place
            s = self.state.copy()
            temp = s.copy()
            s[row, col] = s[row, col+1]
            s[row, col+1] = temp[row, col]
            news = State(s, directionFlag='left', parent=self, depth=self.depth+1)
            subStates.append(news)          #删了left再加入副本类中
        return subStates
    def solve(self):
        # generate a empty openTable
        openTable = []          #形成open表
        # generate a empty closeTable
        closeTable = []         #形成close表
        # append the origin state to the openTable
        openTable.append(self)
        # denote the steps it travels
        steps = 0
        while len(openTable) > 0:     # start the loop
            n = openTable.pop(0)      #从open表出
            closeTable.append(n)      #进close表
            subStates = n.generateSubStates()   #形成副本类
            path = []
            for s in subStates:
                if (s.state == s.answer).all():
                    while s.parent and s.parent != originState:
                        path.append(s.parent)
                        s = s.parent
                    path.reverse()              #列表数据反转
                    return path, steps+1
            openTable.extend(subStates)         #在openTable末尾一次性追加subStates中的多个值
            # sort the openTable in terms of the cost
            openTable.sort(key=lambda x: x.cost)
            steps += 1
        else:
            return None, None
if __name__ == '__main__':
    # the symbol representing the empty place
    symbolOfEmpty = ' '                 #代表空
    # you can change the symbol at here
    State.symbol = symbolOfEmpty
    # set the origin state of the puzzle
    originState = State(np.array([[2, 8, 3], [1, 6 , 4], [7, symbolOfEmpty, 5]]))       #初始状态
    State.answer = np.array([[1, 2, 3], [7, 8, 4], [State.symbol, 6, 5]])               #目标状态
    s1 = State(state=originState.state)
    path, steps = s1.solve()
    if path:                        # if find the solution
        for node in path:
                # print the path from the origin to final state
                node.showInfo()
        print(State.answer)
        print("Total steps is %d" % steps)
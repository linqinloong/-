def judge(wheel,run):
    if wheel == 1 and run == 4:
        print("该物体是飞机")
    elif wheel==1 and run == 5:
        print("该物体是自行车")
    elif wheel == 3 and run == 7:
        print("该物体是火车或地铁")
    elif wheel == 3 and run == 6 :
        print("该物体是火车")
    elif wheel == 2 and run == 6 :
        print("该物体是汽车或公交车")
    elif wheel == 3 and run == 6 :
        print("该物体是火车")
    elif wheel == 4 and run == 6 :
        print("该物体是汽车或公交车")
    else:
        print("输入的情况不存在")

def main():
    print("请输入轮子数：")
    w = int(input())
    print("请输入在哪运行：")
    r = int(input())
    #print(wheel,run)
    judge(w,r)

main()
#判断条件：
# 1 有两个轮子。
# 2 有四个轮子。
# 3 有多个轮子。
# 4 在空中运行.
# 5 在陆地上运行.
# 6 在地上运行.
# 7 在地下运行.

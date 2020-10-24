import os
count=0
def findSzieFile(path,size):
    global count
    if os.path.isfile(path):
        if os.path.getsize(path) > size*1024*1024:
            print(u"文件:",os.path.basename(path),u"大小：",os.path.getsize(path),u"路径在：",os.path.dirname(path))
            count += 1
        else:
            pass
    else:
        for p1 in os.listdir(path):
            findSzieFile(os.path.join(path,p1),size)
findSzieFile(r"E:\晏雨新Python程序",20)
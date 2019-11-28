def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    #start在这句话中是做初始化作用?注释掉start后出现cannot assign# to literal错误
  #  print(start)
  #  显示0 None
    while start <= end:
        mid = (start + end) // 2
        print(mid)
"""
        if key > items[mid]:      #精髓！往后找值了（跟位置有关了）。
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1
"""

a = [1,2,3,4,5,6,7,8,9,0]
print(bin_search(a,8))
#为什么是显示4的死循环？这个4是怎么算出来的？可能解释start+end=9 9//2=4 注:start+end=9是因为len(items) - 1？
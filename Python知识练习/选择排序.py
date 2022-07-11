def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]      #为什么第三行去掉:就无效语法了[:]不是表示列表中从前往后所有元素吗？
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items
a = [1,2,3,4,5,6,7,8,9,0]
print(select_sort(a))

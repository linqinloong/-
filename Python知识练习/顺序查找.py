def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1
a = [1,2,3,4,5,6,7,8,9,0]
print(seq_search(a,8))
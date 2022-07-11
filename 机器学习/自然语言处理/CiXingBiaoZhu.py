import jieba
import jieba.posseg as pseg


def CiXingBiaoZhu():
    del_space_f = open("del_space_f.txt", 'r', encoding='utf-8')
    CiXingBiaoZhu = open("CiXingBiaoZhu.txt", 'w', encoding='utf-8')
    for line in del_space_f:
        words = pseg.cut(line)
        for word, flag in words:
            CiXingBiaoZhu.write(str(word) + str(flag) + "  ")
        CiXingBiaoZhu.write('\n')

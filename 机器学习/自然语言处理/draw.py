import wordcloud as wc
import matplotlib.pyplot as plt


def word_cloud():
    font = r'C:\Windows\Fonts\simfang.ttf'
    word_cloud = wc.WordCloud(font_path=font)

    with open("del_space_f.txt", "r", encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
        # print(data)

    word_cloud.generate(data)  # 生成词云
    plt.imshow(word_cloud)  # 显示图片
    plt.axis("off")  # 不显示坐标轴
    plt.show()  # 显示图
    word_cloud.to_file("ciyun.png")

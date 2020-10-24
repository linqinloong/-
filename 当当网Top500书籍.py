import requests
import re
import json


def request_dandan(url):
    response = requests.get(url)
    return response.text




def parse_result(html):
    pattern = re.compile(

        re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'range': item[0],
            'iamge': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    print(html)
    items = parse_result(html)  # 解析过滤我们想要的信息
    for item in items:
        write_item_to_file(item)
        print(items)


if __name__ == "__main__":
    for i in range(1, 26):
        main(i)
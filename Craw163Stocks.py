import requests
from bs4 import BeautifulSoup
import traceback
import re

def getStockWeb(stock_code,year,season):     #获得url网站链接
    url = "http://quotes.money.163.com/trade/lsjysj_"
    #+ 'stock_code' + ".html?year=" + year + "&season=" + season
    return url


def getHTMLText(url):    #获得url对应页面
    try:
        r = requests.get(url,timeout = 30)
        #print(r.content)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #print(r.content)
        return r
    except:
        return ""
    """"
    requests.get(url)
    self.parse_pager(content.content, item["code"])
    """


def getStockInfo(parse_list,output_file):   #获得股票链接，获得股票链接的主体部分
    url = getStockWeb('600508',2019,1)
    html = getHTMLText('http://quotes.money.163.com/trade/lsjysj_603088.html?year=2018&season=1')
    #print(html.text)
    soup = BeautifulSoup(html.text,'html.parser')
#    parse_list = soup.find_all(('div','inner_box',''))          #待完成，看beautifulsoup 文档写不出来了。
    parse_list = soup.select("div.inner_box tr")                #在div.inner_box标签下找tr标签
    #print(type(parse_list))
    for i in range(len(parse_list)):
        print(parse_list[i])


    data = []
    #data = [x.string for x in parse_list.select("td")]          #在tr标签下找td标签并把td标签的内容按列表形式存给data
    with open(output_file,'w',encoding='utf-8') as f:
        try:
            f.write(str(data)+'\n')
        except:
            traceback.print_exc()
            #continue      #报错(?)

""""
def re_Request():        #重新请求模块
    max_try = 8
    for tries in range(max_try):
        try:
            content = requests.get(url)
            self.parse_pager(content.content, item["code"])
            break
        except Exception:
            if tries < (max_try - 1):
                sleep(2)
                continue
            else:
                add_error_logs("crawl_error", "501", stock_code)
"""


def main():
    output_file = 'E:\晏雨新Python程序\股票数据爬虫.txt'   #爬虫获取的文件存储地
    stock_code = '600508'   #股票代码
    year = 2019             #查询年份
    season = '1'            #查询季度
    parse_list = []
    url = getStockWeb(stock_code, year,season)  #获取相应的股票网站
    getHTMLText(url)    #获得页面信息
#    re_Request()     #防止网络连接不稳定调用re_Request模块
    getStockInfo(parse_list,output_file)  #在网易财经上获取股票信息并把它存入文件中


main()
"""
五个问题:
1.run这个程序后的错误如何修改。
2.第35行continue为什么错误
3.如何用beautifulsoup库中找到标签，并且在其标签的子标签中把所需要的字符串内容遍历存储为一个列表。
4.用data = soup.find_all("td") 直接找到td标签所包含的全部内容再过滤可行吗？
5.chrome浏览器beautifulsoup库文档中的修改.string    i linked to是做什么的？
待优化:
1.前端界面输入程序
2.可以把python标准库解析器换成lxml html解析器
3.添加re_Request模块
4.getHTMLText可用固定的编码方式（例:ios-8859）加快运行速度
"""
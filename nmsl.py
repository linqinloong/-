from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
import xlwt
import xlrd
import xlutils.copy
import re


def egine(n):
    print('开始访问骂人宝典')
    browser = webdriver.Chrome()
    browser.get("https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn")
    # browser.get("https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn")
    # print(browser.page_source)
    #WAIT = WebDriverWait(browser, 10)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('nmsl', cell_overwrite_ok=True)
    sheet.write(0, 0,'骂人数据')
    html = browser.page_source  #获取网页源码
    #print(html)
    math = re.search(r'<body>(.*?)</body>',html).group(0)
    math1 = math.replace('<body>','')
    math2 = math1.replace('</body>','')
    #save_to_excel(n)    #存储数据
    sheet.write(n, 0, math2)        #行数，重要！！！！
    book.save('nmsl.xls')
    #browser.refresh()
    return math2


def copy(math2,n):
    rb = xlrd.open_workbook('E:\\晏雨新Python程序\\nmsl.xls')
    wb = xlutils.copy.copy(rb)
    ws = wb.get_sheet(0)
    ws.write(n,0,math2)
    wb.add_sheet('nmsl2',cell_overwrite_ok=True)
    wb.save('E:\\晏雨新Python程序\\nmsl.xls')

def main():
    n = 1
    for i in range(0,2):
        egine(n)         #第一次运行程序
        #a = egine(n)
        #copy(a,n)          #复制文件
        n = n + 1
        i = i + 1

main()
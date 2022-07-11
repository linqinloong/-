import requests
from bs4 import BeautifulSoup
import csv


def getStockLink(stock_code,year,season):     #获得url网站链接
    stockCodeStr = str(stock_code)
    yearStr = str(year)
    seasonStr = str(season)
    url = 'http://quotes.money.163.com/trade/lsjysj_'+stockCodeStr+'.html?year='+yearStr+'&season='+seasonStr
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


def getStockInfo(stock_code,year,season):   #获得网页信息
    url = getStockLink(stock_code,year,season)
    html = getHTMLText(url)
    soup = BeautifulSoup(html.text,'html.parser')
    table = soup.findAll('table',{'class':'table_bg001'})[0]
    rows = table.findAll('tr')
    print(rows)
    return rows[::-1]      #取从后向前的元素


def writeCSV(stock_code,year,season):
    shareCodeStr = str(stock_code)

    csvFile = open('E:\晏雨新Python程序\股票数据' + shareCodeStr + '.csv', 'w')
    writer = csv.writer(csvFile)
    writer.writerow(('日期','开盘价','最高价','最低价','收盘价','涨跌额','涨跌幅','成交量','成交金额','振幅','换手率'))

    try:
        rows = getStockInfo(stock_code,year,season)
        for row in rows:
            csvRow = []
            # 判断是否有数据
            if row.findAll('td') != []:
                for cell in row.findAll('td'):
                    csvRow.append(cell.get_text().replace(',',''))
                if csvRow != []:
                    writer.writerow(csvRow)
        #time.sleep(3)
        print(year + '年' + season + '季度is done')
    except:
        print('----- 爬虫出错了！没有进入循环-----')
    finally:
        csvFile.close()



def main():
    stock_code = "600801"
    year = "2019"
    season = "1"
    getStockLink(stock_code,year,season)
    getHTMLText(url=getStockLink(stock_code,year,season))
    getStockInfo(stock_code,year,season)
    writeCSV(stock_code, year, season)


main()

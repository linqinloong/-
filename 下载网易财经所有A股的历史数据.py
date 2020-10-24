import urllib.request
import re
import time

stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'

# 获取股票代码列表

def urlTolist(url):
    allCodeList = []
    html = urllib.request.urlopen(url).read()
    html = html.decode('gbk')
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        if item[2] == '6' or item[2] == '3' or item[2] == '0':
            allCodeList.append(item)
    return allCodeList


allCodelist = urlTolist(stock_CodeUrl)

for code in allCodelist:
    print('正在获取%s股票数据...' % code)
    if code[2] == '6':
        url = 'http://quotes.money.163.com/service/chddata.html?code=0'+ code[2:] + \
        '&start=20180101&end=20180831&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
    else:
        url = 'http://quotes.money.163.com/service/chddata.html?code=1'+ code[2:] + \
        '&start=20180101&end=20180831&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    urllib.request.urlretrieve(url, '/home/'+code+'.csv')
    time.sleep(3)
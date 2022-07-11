import requests
import urllib


#查看头部信息
r = requests.head('http://quotes.money.163.com/trade/lsjysj_603088.html?year=2018&season=1')
r = urllib.request.urlopen('http://quotes.money.163.com/trade/lsjysj_603088.html?year=2018&season=1')
print(r.read().decode("utf-8"))
#print(r.headers)
#print(r.text)  #内容是空，所以可以用很少网络流量来获取概要信息


""""
#post()方法向服务器提供新增数据
payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data = payload)
print(r.text)
"""

"""
#post()方法提交字符串
r = requests.post('http://httpbin.org/post',data='ABC')
print(r.text)
"""

"""
#params:字典或字节序列,作为参数增加到url中
kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)
"""

"""
#data:字典、字节序列或文件对象，作为Request的内容
kv ={'key1':'value1','key2':'value2'}
r = requests.request('POST','htt[://python123.io/ws',data=kv)
body = "主体内容"
r = requests.request('POST','http://python123.io/ws',data=body)
"""

"""
#json:json格式的数据,作为Request的内容
kv = {'key1':'value1'}
r = requests.request('POST','http://python123.io/ws',json=kv)
"""

"""
#header:字典，HTTP定制头
hd = {'user-agent':'chrome/10'}
r= requests.request('POST','http://python123.io/ws',headers=hd)
"""

"""
#files:字典类型，传输文件
fs = {'file':open('data.xls','rb')}
r = requests.request(('POST','http://python123.io/ws',files=fs))
"""

"""
#proxies:字典类型，设定访问代理服务器，可以增加登录认证
pxs = {'http':'http://user;pass@10.10.10.1:1234'
       'http':'https://10.10.10.1:4321'   }
r = requests.request('GET','http://www.baidu.com',proxies=pxs)
"""

"""
#检测状态码
import requests
r = requests.get('http://quotes.money.163.com/trade/lsjysj_603088.html?year=2018&season=1')
print(r.status_code)

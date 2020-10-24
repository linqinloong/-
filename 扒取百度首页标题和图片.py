from urllib.request import urlopen
html=urlopen("https://www.baidu.com")
html_text=bytes.decode(html.read())
print(html_text)

import re


content = 'Xiaoshuaib has 100 bananas'
res = re.match('^Xi.*?(\d+)\s.*s$',content)
print(res.group(1))

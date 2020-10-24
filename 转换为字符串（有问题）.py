str(1)            #str()是把数值转换为字符串
print(str)        #为何运行后把str当成了一个类?
print(repr(123))  #为何在repr()内的对象要把它先当成字符串()内打引号?因为abc是字符串,而123也是对象，而不是字符串所以就可以不打引号。
print(chr(48), chr(49), chr(97))         # 十进制
print(str(1),str(2))                    #str()是把数值转换为字符串
print(repr("abc"))                      #repr()将对象转化为字符串显示
print(repr('abc'))                      #为何这句和上一句都是单引号，而上一句不是双引号？
print(ord("a"))                         #ord()将字符转换为ASCII码
print(hex(10))                          #hex()将整数转换为十六进制字符串
print(oct(10))                          #oct()将整数转换为八进制字符串             为啥这两句输出的字符串就无引号？
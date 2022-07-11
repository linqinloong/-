def onesumtwoproduct(list,times=1):
    if times == 1:
        total = 0
        for x in range (len(list)):
            print(list[x],"+")
            total += list[x]
        print("=",total)
    if times == 2:
        product = 1
        for x in range (len(list)):
            print(list[x],"*")
            product *= list[x]
        print("=",product)
onesumtwoproduct(list = [15,25,35,65])
onesumtwoproduct(list = [15,25,35,65],times = 2)

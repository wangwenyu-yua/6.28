num=0
i=2
while i<=100:
    #判断该数字是不是偶数 如果是偶数再求和
    if i%2==0:
        num+=i
    i+=2
    print(i)
print("求和的结果是",num)
#方法一 直接找到1-100所有的偶数 进行相加
# 2. 2. 4. 6.8

#定义变量 保存求和的结果
num=0
#定义循环 定义一到一百之间的偶数并求和
i=2
while i<=100:
    num+=i#就是相当于
    print(i)
    i+=2#就是相当于 每次加2才能保证每次的数字都是偶数
#打印求和结果
print('求和的结果是',num)



#2.找1-100所有的数字
   # 判断这个数字是不是偶数 如果是偶数就求和（数字除2的余数是0    i%2==0）

#切片会得到一个字符串 即可以得到字符串的多个字符

str='abcdefg'
#获取abc字符
print(str[0:3:1])#abc
#如果步长是1可以不写 最后一个冒号也不写
print(str[0:3])
#如果开始位置是0 可以不写
print(str[:3])#abc

#获取efg字符
print(str[4:7])#efg
print(str[-3:7])#efg

#如果最后一个字符要取可以不写
print(str[4:])#efg

#如果开头结束都不写 获取全部内容 但是冒号必须有
print(str[:])#abcdefg

#获取aceg # 0 2 4 6 步长为2


print(str[0:7:2])#aceg
print(str[::2])#aceg

#特殊应用 步长为负数 开始和结束不写 意思全变 一般不用管 只有一种使用场景
#反转 逆置 字符串  [::-1]
print(str[::-1])
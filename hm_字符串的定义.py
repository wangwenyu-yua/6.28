#1.单引号的定义
my_str="hello"
print(my_str,type(my_str))#type输出类型


#字符串包含引号 I'm 小明   如果字符串本身包含单引号 则定义的时候不能使用单引号
my_str1="I'm 小明"
print(my_str1)


#字符串本身包含单引号 在定义的时候 我就是想用单引号
# 使用\转义字符 将字符串本身的引号进行转义
my_str2='i\'m小明'
print(my_str2)

#字符串本身就是   'i\'m小明

my_str3='i\\\'m小明'
print(my_str3)


#字符串前面家加上 r"" 原字符串 字符串中的\不会作为转义符

my_str4=r'i\'m小明'
print(my_str4)
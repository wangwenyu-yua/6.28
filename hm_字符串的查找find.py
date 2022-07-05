str1="and hello world and itcast and it and python"
#在字符串中查找and
num=str1.find('and')
print(num)


#找到字符串中第二个and出现的下标

num1=str1.find('and',num+1)
print(num1)

#找到字符串中第三个and出现的下标
num2=str1.find('and',num1+1)
print(num2)
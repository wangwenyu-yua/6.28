"""
字符串1.join（列表）括号的内容主要是列表，可以是其他容器
作用：将字符串插入到列表中每个相邻的两个数据之间 组成一个新的字符串
列表中的数据使用 逗号隔开
注意点，列表中的类型都是字符串 否则会报错


"""
list1=['helle','world','and','it','python']
#将列表中的字符串使用空格隔开

str1=' '.join(list1)
print(str1)

#将列表中的字符串使用and连接
str2=' and '.join(list1)
print(str2)
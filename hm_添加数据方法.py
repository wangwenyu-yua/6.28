
# 尾部添加（最常用）
#     列表.append(数据)  将数据添加到列表的尾部
#     返回的是none 是一个关键字 可以认为是空 啥都没有 一般不再使用变量来保存 返回的内容
#     想要查看添加后的列表 需要打印的是列表
# 指定位置添加
#     insert
#   列表.insert(下标，数据) 在指定的下标位置添加数据 如果指定下标位置本来有数据 原数据会修改
# 列表的合并
#     列表1.extend（列表2） 将列表2的所有数据诸葛添加到 列表1的尾部
#

my_list=[]
print(my_list)
# 向列表中添加一个数据  娃娃鱼

my_list.append('娃娃鱼')
print(my_list)
#向列表的尾部添加 李四
my_list.append('李四')
print(my_list)
# 在下标位置为1的位置 添加一个数据 张三
my_list.insert(1,'张三')
print(my_list)
# 将mylist2 合并到list1
my_list2=['小五','赚钱']

my_list.extend(my_list2)
print(my_list)
# 将list2作为整体添加到 list

my_list.append(my_list2)
print(my_list)




"""
列表list，是使用最多的一种容器（数据类型）
列表中可以存储多个数据，每个数据之间使用都好隔开
列表中可以存放任何数据类型


"""
#类实例化的方法   不常用
#1.1定义空列表 没有任何数的列表
#1.2  变 量= list（）

list1=list()
print(type(list1),list1)

#类型转换   list（容器）将其他中容器转换为列表

#转换之后会将字符串中的字符作为一个数据 存入到列表中

list2=list('hello')
print(type(list2),list2)

#直接使用【】进行定义常用
#2.1定义空列表
my_list=[]
print(my_list)

# 2.2 定义非空列表
my_list1=[1,'小明',3.22,]
print(my_list1)


# 下标

list3=['小明','18','1.7',True]
print(list3[0])

#列表也支持len 求长度 求元素的个数 相当于数据元素的个数
print(len(list3))




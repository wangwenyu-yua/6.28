# 在字符串中使用find方法查找下标的方法 不存在返回值-1
# 在列表中不存在find方法 想要查找数据的下标 使用index（）方法
# 方法    列表.index(数据，start，end)  使用和find方法一样 调试在字符串中也有index方法

# 区别 返回 index（）方法 找到返回第一次出现的下标 并没有找到代码直接报错

# 查找判断是否存在
# 判断容器中 某个数据是否存在可以使用in关键字

#  数据  in  容器   如果 存在返回true  如果不存在返回 false
#  查找统计出现的次数
# ？统计出现的次数 使用的是 count（）方法
# 列表.count(数据)   返回数据出现的方法


# 例子如下


my_list=[1,3,5,7]
# 查找数据3出现的下标
num=my_list.index(3)
print(num)

# 找到是数据6出现的下标
if 6 in my_list:
    num1=my_list.index(6)#  代码报错
    print(num1)
else:
    print("不在数据中")

if my_list.count(4)>0:#统计数据4出现的次数
    num1 = my_list.index(6)  # 代码报错
    print(num1)
else:
    print("不在数据中")
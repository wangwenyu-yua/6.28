
#
my_list=[1,3,5,7,9,2,4,6,8,0]
# 删除最后一个位置的数据
num=my_list.pop()
print('删除的数据为',num)
print(my_list)

# 删除下标为1的数据
my_list.pop(1)
print(my_list)

# 要删除数据为7的数据
my_list.remove(7)  #如果有多个7只能删掉一个7  如果数据不存在会报错
print(my_list)


# 清空
my_list.clear()
print(my_list)
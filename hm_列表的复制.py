
# 将列表中的数据复制一份 给到新的一个列表    使用场景 有一个列表需要修改操作到列表中的数据 修改之后 需要和原数据进行对比
#  使用切片复制
#     变量=列表【：】
#      使用copy方法来完成
#       变量=列表.copy（）

list=[1,2,3]
list1=list[:]
print("list",list)
print("list1",list1)



list2=list.copy()
print(list2)
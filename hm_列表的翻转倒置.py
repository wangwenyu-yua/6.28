
#   字符串中反转倒置的方法是
#     字符串（::-1）
# 列表中反转和倒置
#   列表【：：-1】  使用切片的方法 他会得到新列表 原来的列表不会改变的
#   列表.reverse()  直接改变原来的列表 返回none

list=[1,2,3,4,5,6,7]
list1=list[::-1]
print("list",list)
print("list1",list1)


list.reverse()
print(list)
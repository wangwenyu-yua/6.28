#for 变量 in range（n）：
    #重复执行的代码

#   1   range（）是python 中的函数 作用使用可以生成的[0,n )之间的整数 不包含n的  一共是n个数字 所有循环n次
#   2   想让for循环多少次  n就写几
#   3    变量的值是每次循环从 o到n中取出一个值  第一次取到的是0  最后一次取得是 n-1
#例子如下
for  i in range(5):
    print(i)
print('-'*30)
#需求使用for循环获取5到10之间的数字

for m in  range(5,11):
    print(m)


"""
range()变形
#需求 使用for循环来获取 5-10之间的数字
for 变量 in range（a，b）：
    重复的代码
#1.range（a，b）作用是生成[a,b)之间的整数数字  不包含b

"""
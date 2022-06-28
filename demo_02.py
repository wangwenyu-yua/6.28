"""
在python当中获得整数数字的可以使用以下方法
    导入随机数工具包
    1..import  random
    2..使用工具包中产生指定范围内的数字
    random.random(1.3)


"""
import random
num=random.randint(1,3)

shitou=1
jiandao=2
bu=3
player=int(input("请出拳  石头是1  剪刀是2 布是3"))
if player==1 and num==2 or player==2 and num==3 or player==3 and num ==1:
    print(num)
    print("你胜利了")

elif  player==num:
    print("平局哟")
else:
    print(num)
    print("您输了")

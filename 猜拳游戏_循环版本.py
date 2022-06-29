import random
num=random.randint(1,3)
while True:#不知道你要玩几次 所以使用无限循环
    shitou=1
    jiandao=2
    bu=3
    player=int(input("请出拳  石头是1  剪刀是2 布是3 退出（0）"))
    if player==0:
        break
    if player==1 and num==2 or player==2 and num==3 or player==3 and num ==1:
        print(num)
        print("你胜利了")

    elif  player==num:
        print("平局哟")
    else:
        print(num)
        print("您输了")

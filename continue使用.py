#1.获取你输入的字符串
#2遍历这个字符串
#3 在遍历的时候，如果字符是e的时候不打印

result=input("请输入")
for i in result:
    if i=="e":
        continue#本次循环后续的代码不执行 执行下一次循环
    print(i)
print("--"*30)
for i in result:
    if i !="e":
        print(i)
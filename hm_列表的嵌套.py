
# 列表嵌套  列表中的内容还是列表
# 使用下标来确定获取的是什么类型的数据 然后确定可以继续进行什么操作

person=[['里斯','18'],['张三','20']]
print(person[0]) #['里斯']
print(len(person)) #2
print(person[0][0])#里斯
print(person[0][0][0])#里

# 将18改为19
person[0][1]='19'
print(person)

# 给张三添加一个性别信息
person[1].append('男')
print(person)

# 将张三的年龄删除
person[1].pop(1)
print(person)
person[0].remove('18')# 俩种方式都可以
print(person)
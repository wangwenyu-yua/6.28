str1='good good syudy'
#将str1中所有的g替换为大写的g
str2=str1.replace('g','G')
print('str1',str1)
print('str2',str2)

#将str1中 第一个good改为 GOOD
str3=str1.replace('good','GOOD',1)
print('str3',str3)

#将str1中第二个good改为GOOD

#先将good变为大写的GOOD 再将第一个大写的GOOD改为小写的good

str4=str1.replace('good','GOOD')
str4=str4.replace('GOOD','good',1)
print('str4',str4)
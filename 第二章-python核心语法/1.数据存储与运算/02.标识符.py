# 标识符是为变量函数类等元素所起的名字
# 1.只能包括字母大小写,数字,下划线
# 2.不能以数字开头
# 3.不能使用关键字 True,False,None,class,def,if,elif,else,for,while,
# yield,print,import,from,as,in,is,and,or,not,with,try,except,
# finally,break,continue,return,global,nonlocal,lambda,del,assert,
# except,raise,pass,def,class
# 4.严格区分大小写
# 都是标识符name _name __name na_me name_1 true(小写合法)
# true = 1
# print(true) #能运行则证明是标识符  把true换成True则不能运行的

#变量名规范
# 1.见名知意  变量名尽可能的符合代表的意义  例子 11岁的起名为age
# 2.多个部分使用下划线连接  例 name_age,update_name
# 3.英文字母全小写

# 例子
# a = 10, b = 20 让这两个变量值互换再输出
# a = 10
# b = 20
# #a, b = b, a  #---1
# # c = a + b   #3---2
# # a = c - a
# # b = c - b
# c = a;a = b;b = c   #---3   #换成一行就中间加一个;
#
# print(a, b)

# 练习
# 现有三个变量a=100,b=200,c=300,
# 现将三个变量的值进行交换,将三个值分别赋值给,c,a,b
a = 100
b = 200
c = 300
# d = a + b + c
# a = d - a -c
# b = d - a - b
# c = d - b -c
c,a,b = a,b,c    #
print(a,b,c)


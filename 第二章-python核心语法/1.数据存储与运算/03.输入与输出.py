# 输入----input函数的功能是获取键盘输入的数据,具体用法 s = input('请输入：')
# 输出----print函数的功能是将数据输出到控制台,print(数据)----数据 + . + 回车 可以快速打出

# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# print(f"您的姓名是{name},今年{age}岁")

# 例题:小智银行卡中有10000元,现进行以下ATM进行取钱操作
# 1.输入密码
# 2.输入取款金额
# 3.计算余额并输出

total = 10000

password = input('请输入密码：')
print(f"密码正确,{password}")

money = input('请输入取款金额：')
print(f"取款成功,余额为{money}")

print(f"取款成功,余额为{total - int(money)}")
#这时候的money是字符串类型,所以需要转换成数字类型(int)  str()是将转化为字符串
# float()浮点型   bool()布尔型

#完整的步骤
password = input('请输入密码：')
if password =='123456':
    print('密码正确')
    money = input('请输入取款金额：')
    if money.isdigit():   #判断输入的是不是数字
        money = int (money)  #将字符串转换成整型
        if money <= total:
            print(f"取款成功,余额为{total - money}")
        else :
            print('取款金额超出余额')
    else :
        print('请输入数字')
else :
    print('密码错误')
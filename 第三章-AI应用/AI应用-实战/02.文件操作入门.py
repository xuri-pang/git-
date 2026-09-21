# # 读文件---r
# # 1.打开方式
# f = open("./resources/文件操作案例.txt","r",encoding="utf-8")
# # 2.读取文件内容
# # content = f.read()
# # print(content)
#
# content_list = f.readlines()     #原文本读完一句会换行所以呈现的结果是这几句诗中间隔着一行
# for line in content_list:        #为了更美观就用到了strip方法
#     print(line.strip())          #strip()方法去除字符串两端的空格、换行符等
#
#
# # 3.关闭方式
# f.close()


# ============================释放资源方式一=========================
# # 写文件---w
# # 1.打开方式
# f = open("./resources/静夜思.txt","w",encoding="utf-8")
#
# # 2.写入文件内容
# try:
#     f.write("静夜思\n\n")   #两个\n是换行再空一行
#     f.write("床前明月光\n")
#     f.write("疑是地上霜\n")
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
#
#
# finally:
# # 3.关闭方式
#     f.close()

# ============================释放资源方式二=========================

# # 写文件---w
#  1.打开方式和写入结合
with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
    f.write("静夜思\n\n")   #两个\n是换行再空一行
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")


# 2.关闭方式
    f.close()





# 读写文件---w+
# 1.打开方式
f = open("./resources/静夜思.txt", "w+", encoding="utf-8")

# 2.写入文件内容
try:
    f.write("静夜思\n\n")  # 两个\n是换行再空一行
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

# 出错方式:w+模式会清空原文件、同时支持读写；两次write写入内容后，文件指针停在文本末尾，
    # 直接调用read会从末尾向后读取，返回空字符串。
# 解决办法：调用seek方法，将文件指针移动到文件开头
    f.seek(0)
    content = f.read()
    print(content)
finally:
    # 3.关闭方式
    f.close()


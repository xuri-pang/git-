# 读文件

# with open(r"D:\develop\PythonProject\py_project01\第三章-AI应用\file\寻隐者不遇.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# a---追加模式:新内容被追加到原有内容之后;文件不存在则创建新文件
with open("./resources/静夜思.txt","a",encoding="utf-8") as f:
    f.write("绝句\n[唐]杜甫\n\n")   #两个\n是换行再空一行
    f.write("两个黄鹂鸣翠柳，\n")
    f.write("一行白鹭上青天。\n")
    f.write("窗含西岭千秋雪，\n")
    f.write("门泊东吴万里船。\n")

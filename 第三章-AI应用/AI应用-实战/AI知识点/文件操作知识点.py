# 一.文件操作----打开,读/写,关闭=========io流
#     三步操作:打开,读/写,关闭----以下皆是python的内置函数
#     1.打开文件:open (文件路径,打开模式)
#     2.读:read() / readlines()
#     3.写:write() / writelines()
# ①.open函数:f = open (文件路径,打开模式.编码)
    # 文件路径:"文件操作案例.txt"  # 如果这个文件没有会自动创建(但不会创建文件夹)
    # 打开模式:"r"是"读"  "w"是"写" "w+"是"读写"  "a"是"末尾追加" "a+"是 "不清空，默认光标在末尾"-----w和w+都会清空原文件,a和a+不会
    # 编码:默认是 encoding = "utf-8" :是全球统一的都能编译兼容的  常见的编码还有:ASCII :是英文规范不能存中文  GBK :是按照中国编码规范设计的其他的语言并不兼容
    # 计算机底层只能读懂0和1,所以需要编码来将文字转换为计算机能读懂的0和1

    # 代码示例:f返回值戴表我们的打开对象---file-------------mode--encoding
             # f = open("./文件位置如resources/文件操作案例.txt", "w", encoding="utf-8")
# ②.read()函数:读取文件内容
    #代码例子
    #content= f.read()  # 读取文件内容
    # print(content)  # 打印文件内容
# ③.readlines()函数:读取文件内容并按行分割
    #代码例子
    #content= f.readlines()  # 读取文件内容并按行分割
    # print(content)  # 打印文件内容
    # ④.close()函数:关闭文件
# ③.write()函数:写入文件内容
    #代码例子
    # f.write("hello world")  # 写入文件内容
# ④.writelines()函数:写入文件内容并按行分割
    #代码例子
    # f.writelines(["hello world\n", "hello python\n"])  # 写入文件内容并按行分割
    # ⑤.close()函数:关闭文件
# ⑤.close()  # 关闭文件
    # f = open("文件操作案例.txt", "w", encoding="utf-8")
    # 具体操作
    # f. close()      #每次操作完成后都需要关闭文件,否则将被python程序占用,无法操作
# 具体操作----w+
    #注意事项:w+模式会清空原文件、同时支持读写；两次write写入内容后，文件指针停在文本末尾，
        #直接调用read会从末尾向后读取，返回空字符串。
    # 解决办法：调用seek方法，将文件指针移动到文件开头
        # f.write("hello world\n")
        # f.write("hello python\n")
        # f.seek(0)                #重点区别
        # content = f.read()
        # print(content)

# 二.操作文件----资源释放----文件操作出现异常:文件无法关闭,怎么解决

# 1.用finally模块解决-----用来释放资源--关闭项目
    # try:
          #写入的内容---这部分出错照样能运行关闭文件
    #     f.write("静夜思\n\n")   #两个\n是换行再空一行
    #     f.write("床前明月光\n")
    #     f.write("疑是地上霜\n")
    #     f.write("举头望明月\n")
    #     f.write("低头思故乡\n")
    # finally:
    #     f.close()
# 缺点：代码写起来繁琐，容易忘记手动写 f.close()，会造成文件资源泄漏

# 2.用with模块解决-------------推荐,最佳实践
# with open() as f 上下文管理器
# with语句（上下文管理器）：自动确保资源正确获取和释放
# ✅ 就算代码中间抛出异常，也会自动关闭文件、释放资源，不用手动写 close()，企业开发首选！
    # with open("文件操作案例.txt", "w", encoding="utf-8") as f:
    #     f.write("静夜思\n\n")
    #     f.write("床前明月光\n")
    #     f.write("疑是地上霜\n")
    #     f.write("举头望明月\n")
    #     f.write("低头思故乡\n")

# 三.读写json格式文件
# Python标准库中提供了处理json数据的核心模块json----是软件开发中最常见的数据交互格式,简化的json数据的处理
# 1.json的序列化和反序列化
    # 1.序列化--json.dump:将python对象转换为json字符串
        # json.dump(obj,f,ensure_ascii=False,indent=4)
    # 2.反序列化--json.load:将json字符串转换为python对象
        # obj = json.load(f)
        # print(obj)
    # 代码示例
    # # 1.序列化

    # import json
    #
    # obj = {
    #     "name" == "张三",
    #     "age" == 18,
    #     "gender" == "男"
    #     }
    # with open("./resources/session.json","w",encoding="utf-8") as f:
    #     json.dump(obj,f,ensure_ascii=False,indent=4)
    # # 2.反序列化

    # import json

    # with open("./resources/session.json","r",encoding="utf-8") as f:
    #     obj = json.load(f)
    #     print(obj)
# 2.json函数的参数
    # 1.ensure_ascii:默认为True,确保所有的数据输出都是ascii码(非ascii码会转义),如果为False,(非ascii码不转义)保留原义输出
    # 例如:输出的张三是中文,为了保留中文不将其转义,就要改动ensure_ascii 将True改为False
    # 2."f"的作用
    # 因为json函数的参数是有顺序的,所以中间跳过的参数要用关键字"f"来传参
    # 3.indent:表示缩进的空格数,默认为None,表示不缩进,还有换行的功能
    # 4,file:表示要操作的文件对象
    # ①.导入：from pathlib import Path
    # ②.__file__：内置变量，获取当前 py 文件完整路径
    # ③.parent：取上一级文件夹；连续写.parent.parent代表向上跳两层目录
    # ④./：Path 专用路径拼接符，自动适配不同系统分隔符
    # ⑤.直接将json_file填入open()里
    # 代码:json_file = Path(__file__).parent.parent / "resources" / "JSON" / "user.json"
# 3.读取json数据文件
    # 利用反序化来操作--还可以将其中的数据提取储存到另外一个文件
    # with open("./resources/user.json","r",encoding="utf-8") as f:
    #     user = json.load(f)
    #     print(user)

# 五.文件操作扩展
# 1.路径的写法---相对路径(推荐使用,因为可移植性强)
    # 相对路径的写法:相对于当前工作目录的路径;  例如:./resources/xxx.json    ./是可以省略的
    # . :是当前目录---->./resources/xxx.json  ./可以省略
    # ../是进入上一级目录后面加的是(这一级目录的子目录)例如:文件操作扩展到file文件
        # ../file/寻隐者不遇.txt
    # ../../是上上个目录后面加的是点击的顺序例如../../第二章/file/寻隐者不遇.txt
# 2.路径的写法---绝对路径
    # 绝对路径的写法:从根目录开始的路径;  例如:/Users/xxx/Desktop/xxx.json
# 3.转义问题
    # 在 Python 字符串里，\是转义符号，\P会被 Python 当成特殊转义字符，不会当成普通路径分隔符。(例如\n是换行符,\t是制表符,\f是换页符,\r是回车符)
    # 解决办法：使用 r 前缀，表示原始字符串，\不会被转义，直接当成普通字符处理
        # 或者将\换成\\或/
# 4.a---追加模式:新内容被追加到原有内容之后;文件不存在则创建新文件(只能写不能读)
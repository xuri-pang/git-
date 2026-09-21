#========================== 一.Streamlit====================================================
# 1.介绍:是一个开源的python库,专为数据工程师及机器学习工程师设计,用来快速基于Python代码构建交互式web网站(无需掌握前端技术)
    # 首先这是前端呈现出来的,现在可以不用学习前端,通过使用第三方库:Streamlit,就是在python文件里引入streamlit,
    #调用Streamlit里的一些api功能,也就是方法基于python代码来构建这个页面
    # 并不是所有的网页都适用--例如复杂的电商网页是不行的
    # 官方网站: https://streamlit.io

# 2.应用的步骤
# 1.安装streamlit:pip install streamlit
# 2.在python文件中引入streamlit模块---去02文件里操作  (上面官网上有更多的使用步骤就上面的网址)
# 3.基于streamlit中提供的API来构建Web应用
# 4.运行程序:streamlit run xxx.py
    #想运行不能用这个里边的绿三角  要用终端运行 streamlit run xxx.py  这个命令
    # (run 后面的项目名可以先输入02再点tab就可以自动补全)运行完后他会出现一个email 直接点回车
    #它会自动输入访问地址例如http://localhost:8501/  一般都是8501

#========================== 二.使用streamlit构建web页面====================================================
# 1.设置页面的配置项，标题，段落文字，图片，音频，视频，Logo，
    # 表格，输入框，密码输入框，单选按钮--具体见Streamlit入门测试

# 2.设置侧边栏功能
# 运用到的内置封装函数:
# sidebar ---作用：在页面左侧开辟独立区域，集中放设置、按钮，分离主内容区,
# text_input ---(单行文本输入框)特点：不能换行，适合昵称等短内容---- 常用参数：标签、placeholder空白提示、value回填旧值
# text_area---(多行文本输入框)特点：支持换行滚动，适合性格、长人设描述，可加height调框高----参数和text_input通用


# 1.侧边栏两种写法
# ① 链式写法：单个控件前加st.sidebar.  例如st.sidebar.text_input()
# ② 批量写法：写with st.sidebar:，缩进内所有控件自动归入侧边栏，无需重复标注 sidebar。
# 2.侧边栏搭建输入控件并同步数据
# 单行短昵称用st.text_input，多行性格描述用st.text_area，输入非空时更新会话存储值
    # 例如:昵称输入框 -------------------placeholder是提示语--------value是默认值,因为前面初始化有默认值了所以把上面的填在这即可
    # nick_name = st.text_input("昵称",placeholder = "请输入昵称",value = st.session_state.nick_name )
# 3.初始化会话持久数据（防止页面刷新丢失）
# 用st.session_state提前给昵称、性格设默认值，聊天记录用列表初始化，示例：
        # if "nick_name" not in st.session_state:
        #     st.session_state.nick_name = "AI伴侣"          ##根据所存信息的不同后面等于号的双引号也可以更改message用的是[]
        # if "nature" not in st.session_state:
        #     st.session_state.nature = "温柔善谈"

# 4.动态拼接系统提示词联动人设
# 用%s占位绑定会话数据，侧边栏修改后 AI 人设实时生效：
# 将系统提示词的昵称和性格具体用占位符%s占位，然后在大模型返回值message里的system_prompt后面加
        #  % (st.session_state.nick_name,st.session_state.nature)




#========================== 三.调用的大模型进入AI伴侣的步骤====================================================
# 1.把所有import导入语句放在 Python 文件的最顶部；
# 2.在全局位置（聊天逻辑外部）初始化 DeepSeek 客户端client，只创建一次；
# 3.用户输入消息后，先打印调用日志，紧接着编写调用大模型的代码；
# 4.构造messages列表，使用变量system_prompt传入角色设定、变量prompt传入用户提问，不要写死内容；
# 5.在全局代码区域（和 logo、页面标题代码同一层级）定义系统提示词变量system_prompt
# 6.返回大模型的响应结果:st.chat_message("user").write(prompt)
    # 重新复制粘贴在交互代码的下面一行将user换成assistant(机器人图标)再将prompt换成response(大模型返回的响应结果)


#========================== 四.回忆整个学习步骤=======================================
# 1.安装streamlit:pip install streamlit---在终端内下载
# 2.利用streamlit构建web页面----streamlit需要在终端内运行streamlit run xxx.py
# 3.调用大模型实现AI伴侣功能--只能一次会话---暂时没有记忆功能


#========================== 五.增加数据保存和展示功能---st.session_state (这个没有记忆能力)=============
#来源 : streamlit / api reference / caching and state / session_state
# 1.核心作用
# 先记住 Streamlit 致命特点:只要用户点按钮、输入框打字、拖动滑块，整个 Python 脚本会从头到尾重新执行一遍。
# 普通在函数里定义的变量，每次重跑都会被重置成初始值，数据留不住。
# st.session_state 就是专门用来跨脚本重跑保存数据的会话存储空间。

# 2.代码演示
# Initialization----1：字典下标方式
# 把 st.session_state 当作 Python 字典操作，用字符串键取值 / 赋值
# 优点：键名可以包含空格、特殊字符、Python 关键字，兼容性最强
# 适合键名动态生成、非常规命名场景
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

# Session State also supports attribute based syntax----属性点语法
# 直接用.属性访问，写法更简洁直观
# 限制：键名必须是合法 Python 标识符（不能以数字开头、不能有空格 / 横杠、不能是关键字如class、for
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'

# 3.具体操作步骤---三步
# 一.在全局代码区域（和 logo、页面标题代码同一层级）定义储存message的st.session_state.messages = []
# 二.展示所有聊天记录
# for message in st.session_state.messages:
#     if message["role"] == "user":                             #这个判断是用来返回具体角色对应的信息
#         st.chat_message("user").write(message["content"])     #write(message)是输出
#     else:
#         st.chat_message("assistant").write(message["content"])
            # st.chat_message("user")：自动生成用户聊天气泡（头像 + 侧边布局） 后面接 .write() / .markdown() / .code() 就是往气泡里填内容
    # 精简方案---在测试页面
# 三.然后分别在用户输出和机器人输出代码后面,写下储存代码:
# st.session_state.messages.append({"role": "user", "content": prompt})
# 只需将更改user和后面的内容content


#========================== 六.增加大模型记忆能力--会话记忆===================================
# 处理方案(会话历史滚雪球)
# 1.syseam--user--assistant--user  这第二个user是根据前一对user-asssistant的对话提问的,所以要进行下一个对话时需要将前一对也添加上
# 这里只需把st.session_state.messages 添加到第一行system后面就行,但是需要将user的删除(因为这里面包括所有的user和assistant的内容)
# 因为st.session_state.messages里存储的方式是字典类型,所以需要将其解包出来*st.session_state.messages
# 解包出来的st.session_state.messages是包括所有的user和assistant的所有内容
# 只需改动以下就可以增加会话记忆功能
# messages = [
#     {"role": "system", "content": system_prompt},
#     *st.session_state.messages
# ],
# 测试:可以加以下代码来从终端里面看提示词是否滚雪球
# print ([
#     {"role": "system", "content": system_prompt},
#     *st.session_state.messages
# ])


#========================== 七.增加流式输出==============================================
# 1.什么是流式输出:例如就像deepseek的输出模式一样,字一点点的输出--
    # 同时文件传输也是一个字或一个词一个符号的输出,所以要用到遍历for将chunk结构(resources照片里有)
# 2.解决方案
# 首先要将stream的false改为true,其次因为是流式输出所以要将所有文本连接起来--用for遍历
# response_message = st.empty()                               # 作用:创建一个空容器,用于存放流式输出
# full_response = ""
# for chunk in response:
#     if chunk.choices[0].delta.content is not None:
#         content = chunk.choices[0].delta.content
#         full_response += content                            # full_response初始为空字符串，循环里不断把新片段追加拼接
#         st.chat_message("assistant").write(full_response)
#上面都是流式输出下面等拼接完后再一次性输出,就不是流式输出了,所以要将输出放到if语句里面.
# 但是他会输出很多行,每行比前面多一个字或者符号--具体输出了多少次取决于for循环了多少次
# 我们需要一整个容器,来呈现不断输出的样式--streamlit官网layouts and containers(布局和容器) / empty
# 书写格式:st.empty()    # 作用:创建一个空容器,用于存放流式输出
# 然后把st.empty()赋值给response_message,不断更新这个容器就能呈现流式输出
# 循环内禁用全局st.chat_message直写，本质是因为它只能追加不能覆盖；
# st.empty()占位容器支持原地刷新，是实现流式打字效果的唯一稳妥方案。
# response_message = st.empty()  # 作用:创建一个空容器,用于存放流式输出
        # st.chat_message("assistant").write(full_response)

# 注意事项--集体步骤

# 1.开启接口流式开关
# 调用大模型接口时，把请求参数stream从False改为True；开启后顶层 response 为迭代器，禁止直接用response.choices[0].message.content取值。
# 2.遍历分片拼接完整文本
# ① 循环前初始化空字符串full_response = ""存储全文；
# ② 通过for chunk in response遍历所有文字分片；
# ③ 增加双层判空过滤无效分片：if chunk.choices and chunk.choices[0].delta.content is not None，提取单段增量内容追加写入full_response，规避空值、索引报错。
# 3.固定容器实现原地流式刷新
# ① 遍历分片前创建占位容器response_message = st.empty()，避免循环调用全局st.chat_message重复生成气泡；
# ② 将response_message.chat_message("assistant").write(full_response)缩进放入循环内部，每拼接一段内容就原地刷新页面，实现逐字打字效果，不可把渲染代码写在循环外。
# 4.同步保存完整对话内容
# 往st.session_state写入助手回复时，取值替换为累加完成的full_response，保证聊天历史完整留存。
# 5.额外避坑提醒
# 禁止嵌套写response_message.st.chat_message()；循环结束后不要重复调用全局st.chat_message输出全文，防止出现重复消息气泡。

# 自己总结：
# 1. 修改 stream 的值将 false 改为 true
# 2. 更改输出方式，先定义一个空字符串 full_response, 再用 for 方法遍历输出的所有文字片段 - for chunk in response,
#     在加一个 if 语句来将空的排除在外 if chunk.choices [0].delta.content is not None: -- 在定义一个迭代的 content 用来将 full_response 补满
# 3. 用一个固定的容器来刷新输出已遍历的字，这就用了另外一个函数 st.empty ()-- 先在返回结果代码的最上方定义一个固定容器 (用来在一张便利贴上写下所有输出的语句，而不是写一个字撕一张便利贴)--response_message = st.empty ()
#     最后将输出语句 st.chat_message.("assistant").write (大模型返回的结果) 改为 response_message.chat_message ("assistant").write (full_response)
# 4.最后保存大模型的结果也要将之前的content改为full_response

#========================== 八.会话管理==============================================
# 一.新建会话:分为两个功能1.保存当前对话数据 2.创建新会话并保存
# 1.保存当前对话数据:注意内存中存放的数据在计算机关机后就会消失,要永久保存数据,就要将数据保存到文件中.
    # 思考: 每一个历史会话文件中,需要保存哪些信息?  回答:时间,昵称,性格,会话记录
    # 正确答案:交互信息,昵称,性格,会话标识(名字唯一)

# 二.文件操作----打开,读/写,关闭=========io流
#     三步操作:打开,读/写,关闭----以下皆是python的内置函数
#     1.打开文件:open (文件路径,打开模式)
#     2.读:read() / readlines()
#     3.写:write() / writelines()
# ①.open函数:f = open (文件路径,打开模式.编码)
    # 文件路径:"文件操作案例.txt"  # 如果这个文件没有会自动创建
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

# 三.操作文件----资源释放----文件操作出现异常:文件无法关闭,怎么解决

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

# 四.读写json格式文件
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

# 五.实现会话管理

# 1.datetime库--需要在最上面调用
    # 分为类 , 类方法 , 实例方法
    # datetime是datetime库的类,datetime.now()是类方法,strftime("%Y-%m-%d %H:%M:%S")是实例方法
# 2.st.button()函数是streamlit的增加按钮方法
# 3.st.rerun() 是 streamlit 的页面重运行函数

# 1.增加会话标识
    # ①.状态初始化:判断会话状态不存在该变量时，才执行初始化赋值
        # if "current_session" not in st.session_state:
        #     st.session_state.current_session = ""
    # ②.增加会话标识:将当前会话标识赋值给current_session
    # 用当前时间来作为标识
    # 调用时间库datetime来获取当前时间
    # 方法一:
        # import datetime    后面的调用更复杂
        # datetime.datetime.now()       #第一个是模块名字,第二个是功能名字
    # 方法二:
          # from datetime import datetime   #直接调用datetime
        # datetime.now()                  #直接调用datetime
    # 还需格式化时间并将其定义为now
    # strftime是格式化时间,把时间格式化成字符串(中间的连接符号可以更改) Y是年 M是月 D是日 H是小时 M是分钟 S是秒
    # now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 最后返回给current_session
    # st.session_state.current_session = now
# 2.增加侧边栏按钮功能
    # ①.增加按钮控件，实现事件触发与会话状态传递
        # 增加--官网api--input widgets--button  button是普通按钮
        # 传导--按钮点击后的反应用if语句来传导信息
        # if st.button("新建会话"):
    # ②.button函数的参数
        # st.button(label,......)
        # label是按钮的名称-必须的要填的参数
        # icon参数是按钮里的小图标
        # width(宽度):"stretch"是填满整个侧边栏，默认width= "content"是等于输入内容宽度
# 3.实现会话保存
    # 保存当前会话:将当前会话内容保存到会话文件中-------可以单独定义为函数方便调用写到配置页面后面
        # ①.current.session作为标志,当st.session_state.current_session
        # ②.就可以进行创建新的会话对象session_data{}--(里面包含nick_name等),封装当前文件的数据准备转移
        # ③.健壮性判断---如果文件不存在,创建文件,否则就不运行---创建目录操作
            # if not Path(session_file).exists():
                # Path(session_file).touch()
        # ④.保存会话书局到json文件中;  需要引入json模块import json
        # ⑤.用with open as f: 打开指定目录的文件和用json.dump将封装的会话数据写入
            # with open(f"session/{st.session_state.current_session}.json","w",encoding="utf-8") as f:
                # json.dump(session_data,f,ensure_ascii=False,indent=4)
        # ⑥.最后:将以上操作定义成一个全新的函数来使会话管理一栏变得更加简洁 save_session()
 # 4.创建新的会话
    # ①.将储存会话的容器清空---用哪个清那个,nick_name是默认的不用清空
        # st.session_state.messages = []     #对话列表清空
        # st.session_state.current_session = generate_session_id()     #会话标识清空更新
    # ②.因为会话标识的创建需要经常用,则将其定义为函数调用更简洁
        # def generate_session_id():
        # return datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # ③.将以上保存到一个文件里方便使用(与保存对话步骤一样)
        # save_session()
    # ④.重新运行文件,渲染页面
        # 出的问题:点击新建会话后,也不会重新运行文件,也不会重新渲染页面,所以表现为之前的状态
        # 用到函数:rerun()---重新运行当前页面(文件)前面加st
    # ⑤.解决空聊天反复创建问题
        # 在保存会话之前,判断一下会话标识是否为空,如果为空,则不保存---用if语句解决

# 六.侧边栏历史会话

# 1.st.columns() 用来把一行切分成多列，实现页面横向布局
    # st.error()---Streamlit 的状态提示组件，用来展示红色错误提示框，给用户显示错误信息
# 2.try‑except(python语言语法结构)：捕获文件操作异常（文件被占用、文件损坏、权限不足），程序不会直接崩溃。
    # except Exception as e:
# 3.os.path.exists()---需要导包 : 是 os.path 模块提供的函数，判断路径（文件 / 文件夹）是否存在。
# 4.三元运算符(python语法结构):如果条件为真,则返回第一个表达式的值;否则,返回第二个表达式的值
    #语法结构---> 值1 if 条件 else 值2  (可以写在button的()里)

# 1.展示历史会话列表
# ①.定义一个加载所有会话列表信息的函数---load_sessions()
# 代码演示
        # def load_sessions():
        #     session_list= []
        #     # 加载sessions目录下的文件
        #     if os.path.exists("./sessions"):
        #         file_list = os.listdir("./sessions")
        #         for filename in file_list:
        #             if filename.endswith(".json"):
        #                 session_list.append(filename[:-5:1])   # 去掉.json后缀名 可以直接写成[:-5]后面的步长是1
        #     return session_list   #返回会话列表,要放到if语句外面,不然会报错

# ②.在侧边栏生成展示界面
# 使用 st.text() 输出普通文本：会话历史
# 调用函数获取全部会话列表
# 使用 for 循环遍历会话列表，一行放置两个按钮组件：st.columns()
    # columns 参数 spec：设置列宽度占比，示例 [4, 1]，第一列占 4 份，第二列占 1 份
    # 语法结构:
        # col1,col2 = st.columns(2)
        #     with col1:
        #         st.header("组件1")
        #         .....
        #     with col2:
        #         st.header("组件2")
        #         .....
    # ⚠️循环动态生成按钮，缺少唯一key会触发组件 ID 冲突报错
    # ✅解决：给button增加key参数，保证每个按钮 ID 唯一
        # 常用格式：功能描述 + 循环变量，保证 key 全局不重复
    # ✨按钮高亮区分当前会话：三元运算符
        # 当前打开会话：type="primary"（蓝色高亮）；其他会话：type="secondary"（灰色普通）
        # 可以在按钮里加if语句,判断当前会话id是否等于按钮的id,如果相等就加高亮,否则不加高亮
    # 💡切换会话前调用 save_session()，保存正在编辑的会话，防止数据丢失
    # 代码演示:
        # col1, col2 = st.columns([4, 1])
        # with col1:
        #     # 加载会话信息
        #     if st.button(session, width="stretch", icon="📄", key=f"load_{session}",
        #                  type="primary" if session == st.session_state.current_session else "secondary"):
        #         load_session(session)
        #         st.rerun()
        # with col2:
        #     # 删除会话信息
        #     if st.button("", width="stretch", icon="❌️
        # ③.增加当前点击的会话名字,增加在展示聊天信息后面", key=f"delete_{session}"):
        #         pass

# 2.加载指定历史会话
    # 补全加载按钮点击对应的业务逻辑

# try‑except 异常处理
    # 一般放在文件读取逻辑外层
    # 作用：捕获文件被占用、文件损坏、权限不足等异常，避免程序直接崩溃
    # except Exception as e：e接收捕获到的异常对象，保存错误信息
    # st.error("提示文字")：红色提示框，向用户展示错误信息

# ①. 定义加载会话函数 load_session(session_name)
    # 参数 session_name：要加载的会话 ID
    # 健壮性检验:用打开函数来判断sessions里是否有文件
    # try:
        # if os.path.exists(f"sessions/{session_name}.json"):
        # 用with open打开文件,用json.load读取文件内容,并返回
                # with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                # 就是新定义的一个局部变量，专门用来临时保存从文件中读取出来的信息,用来给完整聊天记录列表赋值
                    # session_data = return json.load(f)
                # 将刚读取的信息赋值给,会话消息信息(完整聊天记录列表)
                    # st.session_state.messages = session_data["message"]
                # 把从文件中读出的历史昵称，更新到页面全局状态，让侧边栏和AI人设恢复成历史会话的样子
                    # st.session_state.nick_name = session_data["nick_name"]
                # 把从文件里读出的历史性格，更新到页面全局状态，让侧边栏和AI人设恢复成历史会话的样子
                    # st.session_state.nature = session_data["nature"]
                # 把当前加载的历史会话的ID，更新到全局状态中，让系统知道现在正在显示的是哪个历史会话
                # current_session 表示当前会话id---session_表示的是读取的历史会话id
                    # st.session_state.current_session = session_name
    # except Exception as e:
        # st.error(f"加载会话失败: {e}")
# ②.解决点击之前的会话,再回到当前会话没保存的问题
    # 在代码最后面加一个save_session()函数,用来保存当前会话信息
# ③.增加按钮高亮功能(button的参数可以解决)----来分辨那个是当前看到的文件
    #在加载会话的button加一个参数即可type="primary"高亮type="secondary"不高亮正常灰色
    # 为了更好区分需要用  三元运算符  来判断那个是高亮:如果
    # st.button(session, width="stretch", icon="📄", key=f"load_{session}", type="primary" if session == st.session_state.current_session else "secondary")
# ④.增加当前点击的会话名字,增加在展示聊天信息后面
    # st.text(f"会话名称")st.text(f"会话名称:{st.session_state.current_session}")
# 3.删除指定历史会话
# 增加一个删除会话的函数---delete_session()
#     def delete_session():
#         try:
#             #先打开具体的文件
#             if os.path.exists(f"sessions/{session_name}.json"):
#                 os.remvoe(f"sessions/{session_name}.json")
#         except Exception as e:
#             st.error(f"删除会话失败: {e}")
# 在会话历史中的按钮功能下面调用delete_session()函数
    # delete_session(session)
    # rerun()     #重新运行一下文件
# 遇到的问题:删除当前会话但会话的数据还没有清空
    # if session_state.current_session == session_name:
    #     # 清空当前会话
    #     session_state.messages = []
    # st.session_state.current_session = generate_session_name()

# 七.功能优化与检测
# 1.解决新会话在最下面的问题---定位侧边栏st.sidebar()的位置
# 会话历史列表是调用load_sessions()函数和for循环进行遍历后排序的结果,
    # 运用一个列表list的成员方法sort(reverse=True)将其顺序反转---
    # 因为load_sessions的返回值是session_list列表,所以直接改变返回值的顺序即可
    # session_list.sort(reverse=True)

# 2.将历史会话和伴侣信息分隔开看的更明显---输出一个分隔线
# 分隔线在侧边栏里面写
# st.divider()

# 八.总结
# 一.功能
    # 1.大模型对话交互---deepseek大模型
    # 2.会话记忆
    # 3.伴侣性格定制
    # 4.会话管理
        # 新建会话
            # 保存会话
        # 会话历史查询
            # 加载指定会话信息
            # 删除会话
# 二.技术点
    # 1.大模型部署方案
        # 基于本地ollama部署大模型
        # 使用官方api调用大模型
    # 2.HTTP协议
    # 大模型的api调用都是基于HTTP协议
        # 请求数据的格式
        # 响应数据的格式
        # 响应状态码
    # 3.大模型交互的方案
        # 1.基于apifox接口测试工具来进行测试和交互
            # 将提示词组装成对应的请求参数来交给大模型
        # 2.基于open ai 所提供的api来与大模型进行交互
    # 4.大模型会话记忆方案
        # 1.会话历史滚雪球
    # 5.Streamlit构建页面
    # 6.python的文件基本操作
    # 7.json操作
    # 8.os/datetime模块  os-操作系统的标准库


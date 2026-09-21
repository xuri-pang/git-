import streamlit as st
import os
from openai import OpenAI
# import datetime          #不调用这里是灰的

# ======================================改动节点一.增加了两个调用===================================================
from datetime import datetime     #让下面的调用更简洁
import json
print("-------> 重新执行此文件,渲染展示页面")  #可以在终端看见用来判断执行了几次程序



# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣"
               "",  #浏览器最上面的小页面显示的
    page_icon="🤖",  #浏览器最小页面前面的logo  可以去浏览器的Emoji6百宝库里挑
    layout="wide",  #标题视频啥的占整个页面的程度 wide是广泛是比较多 centered占中央的意思  none是不设置的意思
    initial_sidebar_state="expanded",  #是控制侧边栏的状态
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "这是一个Streamlit的入门页面"
    }  #菜单的信息--页面右上角三个点的设置中Report a bug和Get Help都是可跳转的,后面网页是跳转的地址.这里菜单可以是空的,去掉后设置里就剩默认菜单了
)



# ======================================改动节点二.定义封装了4个函数===================================================
# 保存会话信息的函数
def save_session():
        if st.session_state.current_session:
            # 构建新的会话对象
            session_data = {
                "nick_name": st.session_state.nick_name,
                "nature": st.session_state.nature,
                "current_session": st.session_state.current_session,
                "messages": st.session_state.messages
            }

            # 如果 sessions 目录不存在,则创建,如果存在则不执行
            if not os.path.exists("sessions"):
                os.makedirs("sessions")
            # 保存会话到文件
            with open(f"sessions/{st.session_state.current_session}.json", "w",encoding="utf-8") as f:
                json.dump(session_data, f, ensure_ascii=False, indent=4)


# 生成会话标识的函数(具体时间)
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# 加载所有会话列表信息的函数---load_sessions()
def load_sessions():
    session_list= []
    # 加载sessions目录下的文件
    if os.path.exists("./sessions"):
        file_list = os.listdir("./sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5:1])   # 去掉.json后缀名 可以直接写成[:-5]后面的步长是1
    return session_list   #返回会话列表,要放到if语句外面,不然会报错

# 加载指定的会话信息
def load_session(session_name):
    #捕获文件操作异常（文件被占用、文件损坏、权限不足），程序不会直接崩溃
    try:
        if os.path.exists(f"sessions/{session_name}.json"):  #健壮性测试检查sessions目录是否有json文件
            # 读取会话信息
            with open(f"sessions/{session_name}.json","r",encoding="utf-8") as f:
                session_data = json.load(f)
                # 更新会话状态
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception as e:
        #输出会话加载失败的信息
        st.error(f"会话加载失败: {e}")

# 删除会话信息函数
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):   #打开具体的文件
            os.remove(f"sessions/{session_name}.json")    #remove移除指定的json文件
            st.success(f"会话 {session_name} 已删除")    #删除成功提示
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception as e:
        st.error(f"会话删除失败: {e}")
# ==============================================================================================================


# 大标题
st.title("AI智能伴侣")


# logo
st.logo("./resources/猫咪logo.png")


# 系统提示词
# system_prompt预先用%s预留两个占位位，分别对应AI昵称、性格
# 调用大模型时读取session_state最新值填充占位(system_prompt后面的)，侧边栏改昵称/性格，AI人设实时生效无需重写文案
system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """
# st.session_state是Streamlit专属会话全局容器，页面刷新数据不丢失，全模块共享变量
# 提前初始化3类核心数据：聊天记录、AI昵称、AI性格人设，为侧边栏修改、动态提示词提供数据源

# =====================================================================================
# 初始化对话列表：存放历史聊天内容，角色+消息内容成对存储，刷新页面可自动渲染历史对话----这里message是聊天记录
if "messages" not in st.session_state:     #'key'换成聊天记录"messages"
    st.session_state.messages = []         #暂时将'value'换成[]


#初始化昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小涵"   #建立一个库储存输入的信息,默认值是小涵


#初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的台湾姑娘"

# =============================改动节点1.增加会话标识=============================
# 会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()   #设置名字:用实时时间来表示


# ======================================改动节点四.增加了展示文件名字===================================================

# 展示聊天信息
st.text(f"会话名称:{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])  #用if语句主要是区分role的不同


# 创建与DeepSeek大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# =============================改动节点五.增加侧边栏新增会话和会话历史连个区域按钮======================================

# with st.sidebar侧边栏上下文语法：缩进内控件自动归入左侧侧边栏，无需重复写st.sidebar前缀
# 读取节点1初始化的全局值回填输入框(指的是nick_name =)；用户输入新内容后反向更新session_state，实现数据双向同步(指的是if语句)
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")
    # 新建会话
    if st.button("新建会话",width ="stretch",icon="✏️"):
        # 1.保存当前会话信息
        save_session()

        # 2.新建会话
        # 出的问题:点击新建会话后,也不会重新运行文件,也不会重新渲染页面,所以表现为之前的状态
        if st.session_state.messages:          #如果message非空,则执行
            st.session_state.messages = []     #对话列表清空
            st.session_state.current_session = generate_session_name()     #会话标识清空更新
            save_session()
            st.rerun()

    # 会话历史
    st.text("会话历史")  #输出普通文本就行(text)
    session_list = load_sessions()   #调用函数,获取会话列表
    for session in session_list:     #自动把列表里面每一个历史会话，逐个生成页面上的按钮
        col1,col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            if st.button(session,width ="stretch",icon="📄",key = f"load_{session}",type ="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            #删除会话信息
            if st.button("",width ="stretch",icon="❌️",key = f"delete_{session}"):
                delete_session(session)
                st.rerun()


    #伴侣信息
    st.subheader("伴侣信息")
    #昵称输入框 --------------------------placeholder是提示语---------value是默认值,因为前面初始化有默认值了所以把上面的填在这即可
    nick_name = st.text_input("昵称",placeholder = "请输入昵称",value = st.session_state.nick_name )
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature = st.text_area("性格",placeholder = "请输入性格",value = st.session_state.nature)       #text_area是文本输入域--比文本框大可以输入多行文字
    if nature:                         #如果nature非空,则把nature赋值给st.session_state.nature
        st.session_state.nature = nature

# ===========================================================================================================

# 消息输入框--caht_iput   # 消息输出框--chat_message  这两个配合使用
prompt = st.chat_input("请输入您的问题")
if prompt:                                        #字符串会自动转化为布尔值,如果字符串非空,则为True,否则为False
    # st.write(f"用户: {prompt}")                  # 上面是streamlit的写法,下面是streamlit的api reference的chat elements里写法
    st.chat_message("user").write(prompt)         # "user", "assistant", "ai", "human", or str  都有各自不同预设的样式和头像,你也可以填任何但是没有前面的头像
    print("--------> 调用AI大模型,提示词:" ,prompt)

    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})  #role是角色 content是内容


    # 调用大模型,获取返回值---例子看deepseek测试
    # system_prompt预先用%s预留两个占位位，分别对应AI昵称、性格
    # 调用大模型时读取session_state最新值填充占位(system_prompt后面的)，侧边栏改昵称/性格，AI人设实时生效无需重写文案
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name,st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "enabled"}}
    )


    # 输出大模型返回的结果(非流式输出的解析方式)
    # print("<----------- 大模型返回结果: ",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果(流式输出的解析方式)
    response_message = st.empty()                           #作用:创建一个空容器,用于存放流式输出
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content                        # full_response初始为空字符串，循环里不断把新片段追加拼接
            response_message.chat_message("assistant").write(full_response)


    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # =============================改动节点六.增加会话保存======================================================
    # 保存会话信息
    save_session()
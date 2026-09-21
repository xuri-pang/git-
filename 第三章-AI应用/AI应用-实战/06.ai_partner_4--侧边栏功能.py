import streamlit as st
import os
from openai import OpenAI

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
# 大标题
st.title("AI智能伴侣")


# logo
st.logo("./resources/猫咪logo.png")


# 系统提示词
# ========================== 改动节点3:提示词占位符动态替换（联动侧边栏人设） ==========================
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
# ========================== 改动节点1:新增角色提示词配置 + 全局会话数据共享 ==========================
# st.session_state是Streamlit专属会话全局容器，页面刷新数据不丢失，全模块共享变量
# 提前初始化3类核心数据：聊天记录、AI昵称、AI性格人设，为侧边栏修改、动态提示词提供数据源

# 初始化对话列表：存放历史聊天内容，角色+消息内容成对存储，刷新页面可自动渲染历史对话----这里message是聊天记录
if "messages" not in st.session_state:     #'key'换成聊天记录"message"
    st.session_state.messages = []         #暂时将'value'换成[]


#初始化昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小涵"   #建立一个库储存输入的信息,默认值是小涵


#初始化性格-
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的台湾姑娘"

# =====================================================================================

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])  #用if语句主要是区分role的不同


# 创建与DeepSeek大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")


# ========================== 改动节点2:侧边栏人设编辑模块（sidebar布局+数据双向绑定） ==========================
# with st.sidebar侧边栏上下文语法：缩进内控件自动归入左侧侧边栏，无需重复写st.sidebar前缀
# 读取节点1初始化的全局值回填输入框(指的是nick_name =)；用户输入新内容后反向更新session_state，实现数据双向同步(指的是if语句)
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")
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

# =============================================================================================================

# 消息输入框--caht_iput   # 消息输出框--chat_message  这两个配合使用
prompt = st.chat_input("请输入您的问题")
if prompt:                                        #字符串会自动转化为布尔值,如果字符串非空,则为True,否则为False
    # st.write(f"用户: {prompt}")                  # 上面是streamlit的写法,下面是streamlit的api reference的chat elements里写法
    st.chat_message("user").write(prompt)         # "user", "assistant", "ai", "human", or str  都有各自不同预设的样式和头像,你也可以填任何但是没有前面的头像
    print("--------> 调用AI大模型,提示词:" ,prompt)

    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})  #role是角色 content是内容


    # 调用大模型,获取返回值---例子看deepseek测试
    # ========================== 改动节点3:提示词占位符动态替换（联动侧边栏人设） ==========================
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
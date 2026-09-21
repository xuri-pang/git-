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

# logo容错：图片缺失不中断程序
st.logo("./resources/猫咪logo.png")
if os.path.exists(logo_path):
    st.logo(logo_path)


# 系统提示词
system_prompt = "你是一名霸道总裁,请用霸道的语气来回复我"


# 初始化聊天信息
# st.session_state是Streamlit全局会话容器，页面刷新不丢失数据
if "messages" not in st.session_state:     #'key'换成聊天记录"messages"
    st.session_state.messages = []         #暂时将'value'换成[]


# 展示聊天信息
# 页面加载/刷新时，遍历历史记录，把过往问答全部展示出来
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])  #用if语句主要是区分role的不同


# 创建与DeepSeek大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 大模型聊天框具体见resources的ai智能伴侣---在streamlit里的api reference的chat elements里

# 消息输入框--caht_iput   # 消息输出框--chat_message  这两个配合使用
prompt = st.chat_input("请输入您的问题")
if prompt:                                        #字符串会自动转化为布尔值,如果字符串非空,则为True,否则为False
    # st.write(f"用户: {prompt}")                  # 上面是streamlit的写法,下面是streamlit的api reference的chat elements里写法
    st.chat_message("user").write(prompt)         # "user", "assistant", "ai", "human", or str  都有各自不同预设的样式和头像,你也可以填任何但是没有前面的头像
    print("--------> 调用AI大模型,提示词:" ,prompt)


    # 保存用户输入的提示词
    # 先把当前提问追加进全局列表，后续接口调用能读到这条新内容
    st.session_state.messages.append({"role": "user", "content": prompt})  #role是角色 content是内容


    # 调用大模型,获取返回值---例子看deepseek测试
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages  # *解包：展开全部历史user+assistant对话，实现上下文继承
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )


    # 输出大模型返回的结果
    print("<----------- 大模型返回结果: ",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)



    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

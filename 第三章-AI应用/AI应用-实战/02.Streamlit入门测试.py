import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",  #浏览器最上面的小页面显示的
    page_icon="🧊",  #浏览器最小页面前面的logo
    layout="wide",  #标题视频啥的占整个页面的程度 wide是广泛是比较多 centered占中央的意思  none是不设置的意思
    initial_sidebar_state="expanded",  #是控制侧边栏的状态
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "这是一个Streamlit的入门页面"
    }  #菜单的信息--页面右上角三个点的设置中Report a bug和Get Help都是可跳转的,后面网页是跳转的地址.这里菜单可以是空的,去掉后设置里就剩默认菜单了
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")  #子标题即第一标题
st.subheader("Streamlit 二级标题") #次级标题
st.write("Hello, Streamlit!") #显示文字内容

# 段落文字--可以去streamlit官网API reference的Write and magic里st.write看具体方法
st.write("布偶猫，宛如坠入人间的云朵，是集温柔与美貌于一身的大型宠物猫。它们起源于20世纪60年代的美国，由一位名叫安·贝克的繁育者通过精心选育而成。布偶猫最显著的特征是它们那双湛蓝如星辰的杏眼，仿佛能看透人心，充满灵性。")
st.write("它们拥有一身丰厚的中长毛，质地如丝绒般顺滑，因毛色分布不同而被分为重点色、手套色和双色等品种。其最迷人之处在于那柔软的躯体，当你抱起它时，它会像布偶般完全放松、信赖地倚靠在你怀中，这也是“布偶猫”名字的由来。")
st.write("性格上，布偶猫是出了名的“小狗猫”。它们温顺安静，对人充满依恋，喜欢跟随主人穿梭于各个房间，却极少大声叫嚷。它们忍耐力极佳，能与孩童及其他宠物和睦相处，是非常理想的家庭伴侣。")
st.write("尽管外表华丽，布偶猫的日常打理却相对简单，每周梳理一两次毛发即可。它们身体强壮，但需要主人投入大量的陪伴与关爱。选择布偶猫，就是选择了一份温柔缱绻、绵延不绝的深情守候。")
# 图片--上面相同的路径Media elements的st.(image-图片,audio-音频,pdf,video-视频,loge)
st.image("./resources/img.png")
# 音频
st.audio("./resources/1个球 - 大雨还在下.mp3.baiduyun.p.downloading")
# 视频
st.video("./resources/布偶猫照片 (2).mp4")
# Logo
st.logo("./resources/猫咪logo.png")
# 表格
student_data = {
    "姓名":["赵丙赫","袁越超","王瑞涵"],
    "学号":["202417","202418","202419"],
    "语文":[11,12,12],
    "数学":[2,4,6],
    "总分":[13,16,18]
}
st.table(student_data)
# 输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名是:{name}")   #st.write相当于python的print
# 密码输入框
password = st.text_input("请输入密码",type="password")
st.write(f"您输入的密码为:{password}")
# 单选按钮
gender = st.radio("请输入你的性别",["男","女","未知"],index = 2 )  #index是默认功能的函数用下标表示
st.write(f"您的姓名为:{gender}")  #定义gender是为了这里调用
# 一.网络机器人的介绍
# 1.网络爬虫:按照一定的预设规则,自动浏览并抓取网络数据的程序或脚本
    #例如:百度等浏览器都是有很多爬虫从各个网站爬取数据到自己的数据库,再调用
        # (搜素引擎,舆情监控,商业分析(电商比价系统),AI大模型训练的语料)
from pydoc import HTMLDoc

# 二.网络爬虫的流程
    # 自己找信息的流程--思考:打开网址--手动寻找抓取
# 开始---->发起HTTP请求---->解析结果提取数据---->数据处理(清洗)---->数据存储---->结束

    # 3.数据清洗:是指对采集的原始数据进行处理、修正、转换和标准化的过程,目的是让数据变得规范、准确

# 三.网络机器人-合规性(robots协议)
# robots协议:网站通过robots协议告诉爬虫哪些页面可以爬取,哪些页面不可以爬取
# 通用规则(针对所有爬虫)
    # User-Agent:# 用户代理,通过请求头确认爬虫类型  *表示任何的网络机器人
    # Disallow:# 禁止爬取的目录或文件  /表示根目录
    # Allow:# 允许爬取的目录或文件
    # Sitemap:# 网站地图,告诉爬虫网站的结构:帮助爬虫更高效地获取网站内容
        # 一般网站都会有Sitemap,可以提高网站的曝光率
        # SEO:搜索引擎优化
    # Crawl-delay:爬取时间间隔,避免频繁访问造成网站压力过大
# 特定规则(针对豌豆荚爬虫)
    # User - agent: Wandoujia
    # Spider
    # Disallow: /
# 在网址后面加/robots.txt即可查看具体网站的协议

# 四.网络机器人--入门程序
# 题目:获取TIOBE编程语言排行榜单
# 操作步骤
    # 1.查看TIOBE官网的robots.txt文件,明确资源获取规则
    # 2.安装 requests库用于发送HTTP请求(pip install requests)
    # 3.编写python代码,访问TIOBE官网,获取数据

# TIOBE.robots.txt
    # User-agent: *
    # Disallow: /wp-admin/
    # Allow: /wp-admin/admin-ajax.php
    # Sitemap: https://www.tiobe.com/sitemap_index.xml
# 找到所要爬取榜单的地址:https://www.tiobe.com/tiobe-index/
    # 对比wp-admin的开头不许爬取,其他可以,tiobe-index可以爬取

# 三.前端网页结构
# 组成部分:HTML、CSS、JS
# HTML(身体):超文本标记语言,负责元素和内容和结构,标签<h1>一级标题</h1>
# CSS(皮囊):层叠样式表,负责样式,标签<style>h1{color:red}</style>
# JS(交互):JavaScript,负责交互,开始标签<script>     alert('hello')     </script>结束标签-----一般在代码最底端

# 1.HTML
    # 1.1 超文本:超越文本限制,比普通文本更强大.除了文字信息,还可以定义图片、音频、视频等内容。
    # 1.2 标记语言:由标签 "<标签名>"构成的语言,
        # HTML都是定义好的.例如:<h1>展示标签,使用<img>展示图片,<video>展示视频
        # HTML标签一般都是成对出现的,例如:<h1>一级标题</h1>
        # HTML代码直接在浏览器中运行,HTML标签由浏览器解析

# 四.网页解析
# 网页解析指的是从原始HTML文档中提取数据的过程,也是网络爬虫的关键步骤,从一堆标签文本中提取需要的数据
    # 可以借助第三方的标准库---lxm库
# 1.安装lxml库(pip install lxml)
    # lxml库是一个用于解析HTML(超文本标记语言)和XML(可扩展的标记语言)文档的Python库,它提供了强大的解析功能,可以方便地提取网页中的数据
        # 支持Xpath语法来解析和获取网页数据
            # Xpath:是一种在HTML/XML文档中 导航或定位 元素的查询语言,让你能够准确的定位文档的特定 元素、属性或文本


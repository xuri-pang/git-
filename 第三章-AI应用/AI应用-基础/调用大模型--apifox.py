# 一.调用api
# 调用deepseek大模型,传递的提示词是大量的,所以http协议的请求行要用post而不是get
# 这时就不能用浏览器来发起请求(一般浏览器的请求是get类型的)(post一般是私人软件才有的)
# 所以要用一款软件来测试(Apifox)--接口测试工具

# 二.Apifox
# 1.介绍
# Apifox:是一款api设计,开发,测试的一体化平台,是项目开发中进行API接口测试的重要工具

# 三.会话记忆-处理方案(会话历史滚雪球)
# 原因是:调用的大模型是每一次对话都是独立的,后续对话不会记忆
# 解决方案:让下次新对话把上次的问题加上--这就是会话记忆(这就很费token)  (后面有会话缓存和命中缓存可以避免大量token浪费)
# 就是把上一轮对话message{}里的复制,在user后面加,复制粘贴就能解决----也叫上下文
# 也就是增加assistant  和  user 两个{}每个后面加,隔开

# 四.reasoning_content思考过程
# 可以设置以下五种---这影响对问题的处理的效果
# low:低(思考强度弱,思考内容简短)
# medium:中等(均衡)
# high:高(充分思考)
# max:最高
# xhigh:极高

# 五.调用本地的大模型
# 1.首先打开cmd 输入ollama run deepseek
# 2.打开ollama官网寻找url地址复制到apifox里
# 3.打开body选择json输入调用大模型的代码,例如deepseek官网里可以找到调用接口api的curl代码
#     前两个是标头需要填到apifox里的header里面(本地倒是不用写这个)

# 六.用python代码调用大模型---(与apifox调用是两个差不多的方法)
# 例子:利用python代码调用deepseek大模型
# 1.将deepseek官网里的api文档里的python代码复制粘贴到pycham里
# 2.首先引入一个内置模块(python官方提供用来获取操作系统信息,需要在pycham终端用pip install openai下载),从操作系统里获取一个环境变量(DEEPSEEK_API_KEY  是用来保护自己的api key避免泄露)
# 3.在系统高级设置里环境变量增加一个DEEPSEEK_API_KEY  的环境变量(用来避免密钥泄露)



# 七.python里接入第三方软件----(是python里的不是pycham,但可以在pyaham里的终端下载输入下面的代码即可)
# python里会存在一些内置软件包,第三方软件包在一个1名为PyPl的仓库里
# pip(pip3) install openai : pip是python官方提供的python包的管理工具,提供了python包的查找,下载,安装,卸载等功能
# 具体操作代码:  安装:pip install ()  卸载:pip uninstall ()  列出已安装的包:pip list  查看包详情:pip show openai


# 总结:四种大模型调用方法
# 1.运用apifox调用deepseek官方的api(花token),先打开apifox点开快捷请求在deepseek官方,
    # 找到api文档里的curl代码,把两个请求头和参数值复制粘贴到headers里,并且将-d{}里的代码复制到body里包括大括号
# 2.运用apifox调用本地的大模型(不花token),先打开cmd输入 (ollama run 你的大模型),不知道名字用(ollama list)查找,
    # 依旧在body里复制curl里{}的代码,并将model改为你自己下载的模型
# 3.在pycham里调用deepseek官方的api(花token),打开deepseek官网找到api文档,复制里的python代码粘贴到pycham里的python文件
    # 这里需要在电脑系统里增加一个环境变量(DEEPSEEK_API_KEY)下面的值填写你的(deepseek密钥),还要下载一个python的第三方软件包openai
    # 只需打开pycham里的终端输入(pip install openai)重启pycham,即可运行该程序呈现的效果跟前两种方法差不多
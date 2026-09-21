 # 一.大模型的下载
# 用ollama软件可以实现本地部署,下大模型需要去ollama官网里找对应的大模型,找到后会显示下载的指令
# 找到指令后打开终端win+r 找cmd  输入指令就可以下载(前提是已经下载ollama)  例如:ollama run deepseek-coder:6.7b
# 二.ollama的应用
# 1.输出ollama --help  会显示ollama常用的指令
# 2.运行:需要输出ollama run 大模型   前面必须加ollama
# 3.ollama serve和ollama run  是两个没有联系的东西
    # 前者是启动后台服务器(只有启动后才可以通过python代码或第三方软件发HTTP请求这个端口,服务器收到后才可以运行大模型)相当于这个服务器是餐厅,api调用是顾客通过窗口点餐
    # 后者是启动对话客户端,直接和你对话互动,
    # ollama serve一般是用不到,因为一般用ollama list或run时就会静默启动服务器,
    # 除非是软件连不上了,报错 或者让服务器监听0.0.0.0允许局域网电脑访问你的电脑  或者你想在前台看详细的调试日志
# 4.彻底关闭
# 关闭模型的话是输出ollama stop deepseek-r1:7b
# 要关闭服务器的话是需要从电脑右下方从任务栏里关闭 Quit ollama
# 5.本地大模型的应用
# 1.作为pycham的插件,安装完成后可以在PyCham中运行大模型代码块
# 集体步骤: 安装ollama，启动对话客户端, 在PyCham中输入相应的命令，然后按住Shift+Enter，
    # 让ollama跑(ollama run 大模型), 这样就可以直接调用大模型功能,但是需要手动写api请求代码,每次调试都需要单独运行脚本,复制粘贴结果
# 另外一种是:下载proxyai软件,通过启动ollama的本地大模型,来作为一个ai助手(换模型的话需要点go to setting,再点击providers中的ollama切换模型)
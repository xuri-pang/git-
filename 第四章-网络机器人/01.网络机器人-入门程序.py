import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求,获取数据
response = requests.get(target_url)    #用一个变量来接收返回的结果

# 输出数据到控制台
print(response.text)    #获取到文本数据(把对应的前端代码响应回来了)代码解析渲染之后就呈现出前端的页面了
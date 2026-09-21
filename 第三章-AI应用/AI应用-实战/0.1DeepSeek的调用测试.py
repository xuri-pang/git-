# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与DeepSeek大模型交互的客户端对象
# os.environ用于读取系统环境变量，DEEPSEEK_API_KEY是环境变量名，存储DeepSeek的API访问密钥
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 与ai大模型进行交互(参数)
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名霸道总裁,请用霸道的语气来回复我"},
        {"role": "user", "content": "为什么"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出大模型返回的结果
print(response.choices[0].message.content)
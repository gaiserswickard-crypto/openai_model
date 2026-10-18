"""
需求：
    使用 OpenAI 兼容方式调用阿里百炼模型。

步骤：
    1. 从环境变量读取 API Key，避免密钥泄露。
    2. 创建 OpenAI 客户端对象。
    3. 准备 messages，包含 system 和 user。
    4. 调用模型并打印模型生成的文本内容。
"""

import os  # 用于读取环境变量，避免把真实 API Key 写进代码
from platform import system

from openai import OpenAI  # OpenAI 客户端类，用于发送模型调用请求


api_key = os.getenv("DASHSCOPE_API_KEY")  # 从环境变量中读取密钥

if not api_key:
    # 如果没有读到密钥，说明环境变量没有配置好，或者配置后没有重启 PyCharm
    raise ValueError("没有读取到 DASHSCOPE_API_KEY，请检查环境变量并重启 PyCharm。")

client = OpenAI(
    api_key=api_key,  # 用于证明调用者身份
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里百炼 OpenAI 兼容接口地址
)

completion = client.chat.completions.create(
    model="qwen-plus",  # 指定要调用的模型名称
    messages=[
        {
          "role":"system",
          "content":"请你一步一步思考我给的问题，写出推理过程和正确答案"
        },
        {
            "role": "user",
            "content":"当小明 6 岁时，他的妹妹年龄是他的一半。他的哥哥比小明大 4 岁。现在小明 70 岁了，请问他的妹妹和哥哥年龄加起来是多少？"
        }

    ],
)

# choices 表示候选回复列表，通常取第 1 个
# message 表示模型返回的消息对象
# content 才是真正要打印给用户看的文本内容
print(completion.choices[0].message.content)












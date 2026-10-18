```
需求：
    使用 OpenAI 兼容方式调用阿里百炼模型。

步骤：
    1. 从环境变量读取 API Key，避免密钥泄露。
    2. 创建 OpenAI 客户端对象。
    3. 准备 messages，包含 system 和 user。
    4. 调用模型并打印模型生成的文本内容。
```
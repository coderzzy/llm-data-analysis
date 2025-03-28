# llm-data-analysis
摸索使用大模型进行数据分析

## 总体思路
- 方向：金融股票（akshare...）、城市财政分析
- 借鉴 multi-agent
    - 1. 数据获取（人工、或者使用python-sdk获取）
    - 2. LLM 进行 数据理解
    - 3. LLM 进行 python数据分析代码生成，并生成结果
    - 4. LLM 对结果，使用 html 进行网页渲染展示报告
    - 5. 在自媒体平台分享（小红书、公众号等）

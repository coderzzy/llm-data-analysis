# llm-data-analysis
摸索使用大模型进行数据分析

## 项目定性 —— 基于当下大模型能力的过渡方案
- 终局：一定还是大模型能力足够强，直接由大模型全程进行数据分析
- 过渡：基于大模型相对而言更擅长代码能力，以及从节省成本的角度考虑，使用【两步】策略：
    - 1. 大模型生成中间代码
    - 2. 由中间代码完成最终的数据分析和报告产出

### 模式一 —— 大模型直出html报告
- 适用于非结构化数据（如txt、pdf等）、简单任务 -> 大模型直接做数据分析，提供报告

### 模式二 —— 大模型生成python数分脚本
- 适用于结构化数据（如csv文件，或先一步处理成csv文件）、复杂任务 -> 大模型生成python数分脚本，用户基于脚本进行数据分析
- 1. 数据获取（人工、或者使用爬虫能力获取），标记来源渠道
- 2. 先尝试复用【渠道数分脚本库】中的脚本
- 3. 若无脚本，则基于 LLM 进行 数据理解、python数分脚本生成、html网页报告
- 4. 若脚本运行正常，则更新脚本到【渠道数分脚本库】

## 环境与启动（python项目，deepseek模型）
```
# 安装uv，方法一
curl -Ls https://astral.sh/uv/install.sh | bash
uv --version

# 创建虚拟环境
uv venv         
# 激活虚拟环境
source .venv/bin/activate  
# 安装依赖
uv pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
 # 在.env文件中，设置 DEEPSEEK_API_KEY 等
touch .env 

# 运行服务
python run.py  
```

## TODO
1、试试 https://github.com/microsoft/markitdown 统一数据读取
...

from openai import OpenAI
from dotenv import load_dotenv
from os import environ

load_dotenv()  # load environment variables from .env
# 获取所有环境变量中的 key-value
env_vars = dict(environ)


def _call_deepseek(system_prompt, user_prompt):
    client = OpenAI(
        api_key=environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        stream=False,
    )
    return response.choices[0].message.content


def get_html_report_by_deepseek(content, requirement="尽你所能进行分析"):
    system_prompt = """
    ## Role
    你是一个数据分析专家，并且擅长把数分结果用html报告进行展示。
    用户会给你提供待分析的内容（类型不确定，可能是文字描述、表格、图片、html等），以及具体要求

    ## Output
    输出格式为单文件的html代码
    ```html
    # generate by deepseek
    
    ```
    
    """
    return _call_deepseek(
        system_prompt, f"待分析的内容为：{content} \r\n 具体要求为：{requirement}"
    )

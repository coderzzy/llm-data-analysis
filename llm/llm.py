from .deepseek import get_html_report_by_deepseek
import tiktoken


def calculate_token_count(content):
    # 使用tiktoken计算token数量，采用cl100k_base编码（适用于GPT-3.5/4）
    encoding = tiktoken.get_encoding("cl100k_base")
    token_count = len(encoding.encode(content))
    return token_count


def get_html_report_by_llm(llm_name, content, requirement):
    result = ""
    if llm_name == "deepseek":
        result = get_html_report_by_deepseek(content, requirement)
    else:
        # 默认是deepseek
        result = get_html_report_by_deepseek(content, requirement)
    print(f"llm_name: {llm_name}, input_token_count: {calculate_token_count(content)}, output_token_count: {calculate_token_count(result)}")
    return result

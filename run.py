from data_read.data_read import read_xlsx
from llm.llm import get_html_report_by_llm
import re


def process_xlsx(file_path):
    content = read_xlsx(file_path)
    html_response = get_html_report_by_llm("deepseek", content, "")
    # 提取html代码块
    html = re.search(r"```html\n(.*?)\n```", html_response, re.DOTALL).group(1)
    with open(f"./outputs/{file_path.split('/')[-1].split('.')[0]}.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    file_path = "./inputs/2025年6月份居民消费价格主要数据.xlsx"
    process_xlsx(file_path)

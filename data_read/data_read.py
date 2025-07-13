import pandas as pd

def read_xlsx(file_path):
    """
    读取xlsx文件数据并转换为字符串格式
    :param file_path: xlsx文件路径
    :return: 返回字符串格式的数据
    """
    try:
        data = pd.read_excel(file_path)
        return data.to_string()
    except Exception as e:
        print(f"读取xlsx文件出错: {e}")
        return None

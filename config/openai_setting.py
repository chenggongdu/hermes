# config.py
import os

import openai

# openai key
api_key = 'sk-xx'
# openai_proxy:代理地址
openai_proxy = 'http://127.0.0.1:33210'
# openai_api_base: 默认https://api.openai.com/v1
openai_api_base = 'https://www.wushuangai.com'


class OpenAISetting:
    """OpenAI Setting"""
    def __init__(self):
        """OpenAI Setting"""
        openai.api_key = api_key
        os.environ['OPENAI_API_KEY'] = api_key
        os.environ['OPENAI_API_BASE'] = 'https://www.wushuangai.com'
        os.environ["OPENAI_PROXY"] = openai_proxy

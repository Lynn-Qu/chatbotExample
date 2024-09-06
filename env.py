import os

from dotenv import load_dotenv

# 获取当前环境
ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')
# 根据环境加载相应的 .env 文件
dotenv_path = f".env.{ENVIRONMENT}"
load_dotenv(dotenv_path)


# 获取 OpenAI API 密钥列表
OPENAI_KEY_LIST = os.getenv('OPENAI_KEY_LIST', '')
OPENAI_KEYS = OPENAI_KEY_LIST.split(',')

# 打印 OpenAI API 密钥列表（调试用）
print("OpenAI API Keys:", OPENAI_KEYS)

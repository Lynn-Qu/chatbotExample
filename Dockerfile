# 使用官方的 Python 基础镜像
FROM python:3.10-slim

#设置环境变量
ARG env=test
ENV ENVIRONMENT=${env}

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器的工作目录
COPY . .

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt


# 暴露 Streamlit 默认的端口 8501
EXPOSE 8080

# 启动 Streamlit 应用
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]

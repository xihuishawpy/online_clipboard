FROM python:3.9-alpine

WORKDIR /app

# 安装系统依赖和工具，添加tzdata包并设置时区
RUN apk add --no-cache gcc musl-dev linux-headers wget curl tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata

# 复制依赖文件
COPY src/requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 复制应用代码和静态文件
COPY src/ .

# 添加健康检查脚本
COPY docker/healthcheck.sh /healthcheck.sh
RUN chmod +x /healthcheck.sh

# 设置生产环境变量
ENV FLASK_ENV=production
ENV FLASK_APP=app.py
ENV TZ=Asia/Shanghai

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
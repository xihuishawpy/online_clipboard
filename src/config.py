import os

# Redis配置
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')

# 应用配置
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
DEBUG = os.environ.get('FLASK_ENV') == 'development'

# 剪贴板配置
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB 
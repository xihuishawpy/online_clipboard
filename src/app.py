from flask import Flask, render_template, request, jsonify, abort
import redis
import hashlib
import json
from datetime import datetime, timedelta
import secrets
import os
import time

# 根据环境变量加载不同的配置
if os.environ.get('FLASK_ENV') == 'development':
    import config_dev as config
else:
    import config

app = Flask(__name__)
app.config.from_object(config)

# 修改调试配置检查
debug_mode = os.environ.get('FLASK_ENV') == 'development'
app.debug = debug_mode

# Redis连接
def get_redis_connection():
    return redis.Redis(
        host=os.environ.get('REDIS_HOST', 'localhost'),  # 从环境变量获取主机名
        port=int(os.environ.get('REDIS_PORT', 6379)),
        password=os.environ.get('REDIS_PASSWORD'),
        decode_responses=True,
        socket_connect_timeout=5,  # 添加连接超时
        retry_on_timeout=True      # 启用重试
    )

redis_client = get_redis_connection()

def generate_paste_id():
    """生成唯一的粘贴ID"""
    return secrets.token_urlsafe(8)

def hash_password(password):
    """密码哈希"""
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/paste', methods=['POST'])
def create_paste():
    """创建新的粘贴内容"""
    data = request.json
    content = data.get('content')
    password = data.get('password')
    expire_time = data.get('expireTime', '1h')
    burn_after_read = data.get('burnAfterRead', False)
    
    if not content:
        return jsonify({'error': '内容不能为空'}), 400
    
    paste_id = generate_paste_id()
    
    # 计算过期时间
    expire_times = {
        '1h': timedelta(hours=1),
        '1d': timedelta(days=1),
        '7d': timedelta(days=7),
        '30d': timedelta(days=30)
    }
    ttl = expire_times.get(expire_time, expire_times['1h'])
    
    paste_data = {
        'content': content,
        'password': hash_password(password) if password else None,
        'burn_after_read': burn_after_read,
        'created_at': datetime.now().isoformat()
    }
    
    # 存储到Redis
    redis_client.setex(
        f'paste:{paste_id}',
        int(ttl.total_seconds()),
        json.dumps(paste_data)
    )
    
    return jsonify({
        'id': paste_id,
        'url': f'/view/{paste_id}'
    })

@app.route('/api/paste/<paste_id>', methods=['GET'])
def get_paste(paste_id):
    """获取粘贴内容"""
    password = request.args.get('password', '')
    
    paste_data = redis_client.get(f'paste:{paste_id}')
    if not paste_data:
        return jsonify({'error': '内容不存在或已过期'}), 404
    
    paste = json.loads(paste_data)
    
    # 验证密码
    if paste['password']:
        if not password or hash_password(password) != paste['password']:
            return jsonify({'error': '密码错误'}), 403
    
    # 处理阅后即焚
    if paste['burn_after_read']:
        redis_client.delete(f'paste:{paste_id}')
    
    return jsonify({
        'content': paste['content'],
        'created_at': paste['created_at']
    })

@app.route('/view/<paste_id>')
def view_paste(paste_id):
    return render_template('view.html', paste_id=paste_id)

@app.route('/health')
def health_check():
    try:
        # 测试 Redis 连接
        redis_client.ping()
        return jsonify({'status': 'healthy', 'redis': 'connected'}), 200
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

if __name__ == '__main__':
    # 本地开发时使用 debug 模式
    app.run(host='0.0.0.0', port=5000, debug=True) 
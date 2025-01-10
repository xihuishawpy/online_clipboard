from flask import Flask, jsonify
from redis import Redis
import os
import json

app = Flask(__name__)
redis_client = Redis(
    host=os.environ.get('REDIS_URL', 'localhost'),
    port=6379,
    password=os.environ.get('REDIS_PASSWORD')
)

def handler(event, context):
    # 处理API请求
    path = event['path'].replace('/api/', '')
    method = event['httpMethod']
    
    try:
        # 根据路径和方法处理请求
        if method == 'POST' and path == 'paste':
            body = json.loads(event['body'])
            # 处理创建粘贴请求
            # ...

        elif method == 'GET' and path.startswith('paste/'):
            paste_id = path.split('/')[-1]
            # 处理获取粘贴内容请求
            # ...

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'success'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        } 
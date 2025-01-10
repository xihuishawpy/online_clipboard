# 在线剪贴板

一个安全、高效的在线剪贴板服务，支持密码保护、过期时间设置和阅后即焚功能。

## 功能特点

- 🔒 密码保护：设置访问密码，保护敏感内容
- ⏰ 过期时间：支持1小时、1天、7天、30天的过期设置
- 🔥 阅后即焚：查看一次后自动销毁内容
- 📱 响应式设计：完美支持移动端访问
- ⚡ 快速响应：毫秒级的访问速度
- 🎨 美观界面：现代化的UI设计

## 演示

[查看完整演示视频](https://github.com/user-attachments/assets/7430eaa9-0764-43bd-8597-a038c584f003)

## 项目结构

```
online_clipboard/
├── docker/
│   ├── Dockerfile          # Docker 构建文件
│   ├── nginx.conf          # Nginx 配置
│   ├── healthcheck.sh      # 健康检查脚本
│   └── docker-compose.yml  # Docker 编排配置
├── src/
│   ├── static/             # 静态文件
│   │   └── images/         # 图片资源
│   ├── templates/          # HTML 模板
│   │   ├── index.html     # 主页模板
│   │   └── view.html      # 查看页模板
│   ├── app.py             # Flask 应用主文件
│   ├── config.py          # 配置文件
│   └── requirements.txt    # Python 依赖
├── run_dev.sh             # 开发环境启动脚本
└── README.md              # 项目文档
```

## 安装部署

### 前置要求

- Docker 20.10.0 或更高版本
- Docker Compose v2.0.0 或更高版本
- 2GB 以上可用内存
- 10GB 以上磁盘空间

### 快速开始

1. 克隆仓库：
```bash
git clone https://github.com/xihuishawpy/online_clipboard.git
cd online_clipboard
```

2. 启动服务：
```bash
docker-compose -f docker/docker-compose.yml up -d
```

3. 访问服务：
```bash
http://localhost:8099
```

### 开发环境

如果你想在本地开发环境运行：

1. 安装依赖：
```bash
pip install -r src/requirements.txt
```

2. 启动开发服务器：
```bash
chmod +x run_dev.sh
./run_dev.sh
```

## 监控和维护

### 查看服务状态

```bash
# 查看所有容器状态
docker-compose -f docker/docker-compose.yml ps

# 查看特定服务状态
docker-compose -f docker/docker-compose.yml ps web
docker-compose -f docker/docker-compose.yml ps redis
docker-compose -f docker/docker-compose.yml ps nginx
```

### 查看日志

```bash
# 查看所有服务日志
docker-compose -f docker/docker-compose.yml logs -f

# 查看特定服务日志
docker-compose -f docker/docker-compose.yml logs web
docker-compose -f docker/docker-compose.yml logs redis
docker-compose -f docker/docker-compose.yml logs nginx
```

### 停止服务

```bash
docker-compose -f docker/docker-compose.yml down
```

### 重新构建并启动服务

```bash
docker-compose -f docker/docker-compose.yml up -d --build
```

### 停止并删除所有容器、网络和卷

```bash
docker-compose -f docker/docker-compose.yml down --volumes --remove-orphans
```

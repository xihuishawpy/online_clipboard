```
// Start Generation Here
# Online Clipboard

A secure and efficient online clipboard service that supports password protection, expiration time settings, and burn-after-reading functionality.

## Features

- 🔒 Password Protection: Set an access password to protect sensitive content.
- ⏰ Expiration Time: Supports expiration settings of 1 hour, 1 day, 7 days, and 30 days.
- 🔥 Burn After Reading: Content is automatically destroyed after being viewed once.
- 📱 Responsive Design: Perfectly supports mobile access.
- ⚡ Fast Response: Millisecond-level access speed.
- 🎨 Beautiful Interface: Modern UI design.

## Project Structure

```bash
clipboard/
├── docker/
│ ├── Dockerfile # Docker build file
│ ├── nginx.conf # Nginx configuration
│ ├── healthcheck.sh # Health check script
│ └── docker-compose.yml # Docker orchestration configuration
├── src/
│ ├── static/ # Static files
│ ├── templates/ # HTML templates
│ ├── app.py # Flask application main file
│ ├── config.py # Configuration file
│ └── requirements.txt # Python dependencies
├── netlify/
│ └── functions/
│ └── api.py # Netlify Functions API
├── run_dev.sh # Development environment startup script
├── netlify.toml # Netlify configuration
└── README.md # Project documentation
```

## Installation and Deployment

### Prerequisites

- Docker 20.10.0 or higher
- Docker Compose v2.0.0 or higher
- More than 2GB of available memory
- More than 10GB of disk space

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/xihuishawpy/online_clipboard.git
cd online_clipboard
```

2. Start the service:
```bash
docker-compose -f docker/docker-compose.yml up -d
```

3. Access the service:
```bash
http://localhost:8099
```

### Development Environment

If you want to run in a local development environment:

1. Install dependencies:
```bash
pip install -r src/requirements.txt
```

2. Start the development server:
```bash
chmod +x run_dev.sh
./run_dev.sh
```

## Monitoring and Maintenance

### Check Service Status

```bash
# Check the status of all containers
docker-compose -f docker/docker-compose.yml ps

# Check the status of a specific service
docker-compose -f docker/docker-compose.yml ps web
docker-compose -f docker/docker-compose.yml ps redis
docker-compose -f docker/docker-compose.yml ps nginx
```

### View Logs

```bash
# View logs for all services
docker-compose -f docker/docker-compose.yml logs -f

# View logs for a specific service
docker-compose -f docker/docker-compose.yml logs -f web
docker-compose -f docker/docker-compose.yml logs -f redis
docker-compose -f docker/docker-compose.yml logs -f nginx
```

### Stop Service

```bash
docker-compose -f docker/docker-compose.yml down
```

### Rebuild and Start Service

```bash
docker-compose -f docker/docker-compose.yml up -d --build
```

### Stop and Delete All Containers, Networks, and Volumes

```bash
docker-compose -f docker/docker-compose.yml down --volumes --remove-orphans
```


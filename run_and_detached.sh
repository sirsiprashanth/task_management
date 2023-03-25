echo 'Building docker image...⏳'
docker build -t task_mgmt:latest .
echo 'Running Docker image task_mgmt...⚡'
docker-compose up -d
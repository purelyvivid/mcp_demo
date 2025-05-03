# Docker

docker 操作前確認離開venv環境

Windows（PowerShell） 
```
$IMG_PATH = "purelyvivid/mcp_fastapi_uv:weather_0.0.1"    
$DOCKERFILE_PATH = "fastapi_mcp_server\weather\Dockerfile"   
```

build
```
docker build -t $IMG_PATH  -f $DOCKERFILE_PATH  .
```

run
```
$YOUR_MCP_SERVER_API_PORT = 8003
docker run -d -p $YOUR_MCP_SERVER_API_PORT:8000 $IMG_PATH
```

push to dockerhub
```
docker push $IMG_PATH
```
check dockerhub: https://hub.docker.com/repository/docker/purelyvivid/mcp_fastapi_uv/general


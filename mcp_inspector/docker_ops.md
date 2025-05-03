# Docker

docker 操作前確認離開venv環境

Windows（PowerShell） 
```
$IMG_PATH = "purelyvivid/mcp_inspector:1.0.7"    
$DOCKERFILE_PATH = "mcp_inspector\Dockerfile"   
```

build
```
docker build -t $IMG_PATH  -f $DOCKERFILE_PATH  .
```

run
```
$YOUR_WEBUI_PORT = 6274    
$YOUR_PROXY_PORT = 6277 
docker run -d -p $YOUR_WEBUI_PORT:6274 -p $YOUR_PROXY_PORT:6277 $IMG_PATH
```

push to dockerhub
```
docker push $IMG_PATH
```
check dockerhub: https://hub.docker.com/repository/docker/purelyvivid/mcp_inspector/tags



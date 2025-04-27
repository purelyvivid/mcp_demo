


# Docker

## mcp inspector
build
```
docker build -t purelyvivid/mcp_inspector:1.0.6 -f .\Dockerfile_insp  .
```

run
```
docker run -d -p <your_webui_port>:6274 -p <your_proxy_port>:6277 purelyvivid/mcp_inspector:1.0.6 
```

push to dockerhub
```
docker push purelyvivid/mcp_inspector:1.0.6
```
https://hub.docker.com/repository/docker/purelyvivid/mcp_inspector/tags


## mcp server
build
```
docker build -t purelyvivid/mcp_fastapi_uv:1.0.1 -f .\Dockerfile_insp  .
```

run
```
docker run -d -p <your_mcp_server_api_port>:8000 purelyvivid/mcp_fastapi_uv:1.0.1 
```

push to dockerhub
```
docker push purelyvivid/mcp_fastapi_uv:1.0.1
```

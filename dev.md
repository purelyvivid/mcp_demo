

## 創建虛擬環境 20250427
```
python -m venv .venv
```

## 進入虛擬環境

```
# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: 
.venv\Scripts\Activate.ps1
```

## 安裝套件
```
pip install --upgrade pip
pip install -r .\requirements.txt
```

## Git (須先進入虛擬環境)
```
git add .
git commit -m "modified"
git push -u origin
```

## 本地 shell 啟動服務

### mcp_inspector
current version: 0.11.0
```
mcp dev <your server filename>.py
```
default port webui: 6274 , proxy: 6277

### mcp_server_fastapi
```
fastapi dev --host 0.0.0.0 --port 8001 fastapi_mcp_server\user_id\main.py
fastapi dev --host 0.0.0.0 --port 8002 fastapi_mcp_server\weather\main.py
fastapi dev --host 0.0.0.0 --port 8003 fastapi_mcp_server\math\main.py
```

base_url:
http://localhost:8001/docs/
http://localhost:8002/docs/
http://localhost:8003/docs/
確認服務正常

## 打包成 docker 容器 / 本地跑docker容器 / 推上 docker hub

- mcp_inspector : [doc](mcp_inspector.md)
- mcp_server_fastapi : weather [doc] (fastapi_mcp_server\math\docker_ops.md)
- mcp_server_fastapi : math [doc](fastapi_mcp_server\math\docker_ops.md)
- mcp_server_fastapi : user_id [doc](fastapi_mcp_server\user_id\docker_ops.md)

## 部署到雲端 (GCP cloud run 為例)

備註: GCP cloud run 部署的 mcp_inspector 不能使用, 因為 GCP cloud run 只允許單一 port expose, proxy port 無法出去

base_url:
https://<your_deployment_info>.run.app #user_id

- mcp endpoint
```
<base_url>/mcp
```

- fastapi docs
```
<base_url>/docs
```

- fastapi api
```
http://localhost:8003/add?a=1&b=3
```
get `4`


## MCP 測試

- 利用本地啟動的  mcp_inspector (shell or docker) 測試 mcp 端點
- 注意最好用無痕視窗 才不會 connection error
- mcp_inspector 若為本地部署, 測試不需要設置 Inspector Proxy Address
- 若 mcp_inspector 部署 port號有更改, 需設置 Inspector Proxy Address








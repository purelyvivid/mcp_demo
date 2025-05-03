創建虛擬環境 20250427
```
python -m venv .venv

# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: 
.venv\Scripts\Activate.ps1
```

安裝套件
```
pip install --upgrade pip
pip install -r .\requirements.txt
```

Git (須先進入虛擬環境)
```
git add .
git commit -m "modified"
git push -u origin
```


```
fastapi dev --host 0.0.0.0 --port 8001 fastapi_mcp_server\user_id\main.py
fastapi dev --host 0.0.0.0 --port 8002 fastapi_mcp_server\weather\main.py
```


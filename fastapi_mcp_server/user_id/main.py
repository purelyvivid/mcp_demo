import uvicorn
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()



# Auto-generated operation_id (something like "read_user_users__user_id__get")
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

# Explicit operation_id (tool will be named "get_user_info")
@app.get("/users/{user_id}", operation_id="get_user_info")
async def read_user(user_id: int):
    return {"user_id": user_id}

mcp = FastApiMCP(app)

# Mount the MCP server directly to your FastAPI app
mcp.mount()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


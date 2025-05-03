import uvicorn
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()


@app.get("/add")
def add(a: int, b: int) -> int:
    """
    A simple math tool that calculates the sum of two numbers. 
    For example, adding 5 and 7 returns 12.

    Args:
        a: the first number
        b: the second number
    
    """
    return a + b

@app.post("/multiple")
def multiple(a: str, b: str) -> str:
    """
    A simple math tool that calculates the product of two numbers. 
    For example, 3 multiplied by 4 returns 12.

    Args:
        a: the first number
        b: the second number
    """
    return f"a*b={str(a*b)}"

@app.get("/power")
def power(a: float, b: float) -> float:
    """
    A simple math tool that calculates the result of raising a base number to an exponent. For example, 2 to the power of 3 returns 8.
    
    Args:
        a: base number
        b: exponent
    """
    return a ** b

mcp = FastApiMCP(app, )

# Mount the MCP server directly to your FastAPI app
mcp.mount()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


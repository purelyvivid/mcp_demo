# server.py
from mcp.server.fastmcp import FastMCP



# Create an MCP server
mcp = FastMCP("Hello MCP")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.tool()
def get_greeting(name:str) -> str:
    """Get a personalized greeting"""
    return f"Hello, MCP {name}!"

if __name__ == "__main__":
    mcp.run(transport="sse")


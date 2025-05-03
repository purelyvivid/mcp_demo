# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Hello MCP")


# Add a dynamic greeting resource
@mcp.tool()
def get_greeting(name:str) -> str:
    """Get a personalized greeting"""
    return f"Hello, MCP {name}!"

if __name__ == "__main__":
    mcp.run(transport="sse")


# server.py
from mcp.server.fastmcp import FastMCP



# Create an MCP server
mcp = FastMCP("Hello MCP 001")


# Add an addition tool
@mcp.tool()
def add001(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run()


# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Simple Math Ops")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    A simple math tool that calculates the sum of two numbers. 
    For example, adding 5 and 7 returns 12.

    Args:
        a: the first number
        b: the second number
    
    """
    return a + b

@mcp.tool()
def multiple(a: str, b: str) -> str:
    """
    A simple math tool that calculates the product of two numbers. 
    For example, 3 multiplied by 4 returns 12.

    Args:
        a: the first number
        b: the second number
    """
    return f"a*b={str(a*b)}"

@mcp.tool()
def power(a: float, b: float) -> float:
    """
    A simple math tool that calculates the result of raising a base number to an exponent. For example, 2 to the power of 3 returns 8.
    
    Args:
        a: base number
        b: exponent
    """
    return a ** b


if __name__ == "__main__":
    mcp.run()


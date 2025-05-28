# server.py
from fastmcp import FastMCP
import uvicorn

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    app = mcp.http_app
    # Print the URL to make it clear where to connect
    print("Starting MCP server at http://localhost:8080")
    uvicorn.run(app, host="0.0.0.0", port=8080)

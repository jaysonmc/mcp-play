from fastmcp import Client
import asyncio

async def main():
    # Create a client connected to your local MCP server
    client = Client("http://localhost:8080")
    
    # Connect to the server
    async with client:
        # Call the "add" tool with parameters
        result = await client.call_tool("add", {"a": 5, "b": 7})
        
        # Print the result
        print(f"Result of 5 + 7 = {result}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())

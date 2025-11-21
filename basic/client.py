from fastmcp.client import Client
from datetime import datetime
import asyncio

# Note the `sse` path post-fix for sse servers
# For all transports, see https://gofastmcp.com/clients/client#transports
sse_url = "http://localhost:8000/sse"

client = Client(sse_url)


async def main():
    # Connection is established here
    async with client:
        print(f"Client connected: {client.is_connected()}")

        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        if any(tool.name == "edit_file" for tool in tools):
            now = datetime.now()
            # To YYYY-MM-DD HH:MM:SS format
            timestamp_string = now.strftime("%Y-%m-%d %H:%M:%S")
            result = await client.call_tool(
                "edit_file",
                {
                    "filename": "hello-world.txt",
                    "line": "This text was added on " + timestamp_string,
                },
            )
            print(f"Greet result: {result}")

    # Connection is closed automatically here
    print(f"Client connected: {client.is_connected()}")


if __name__ == "__main__":
    asyncio.run(main())

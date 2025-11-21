from fastmcp import FastMCP, Context
from typing import Annotated
from pydantic import BaseModel, Field
import aiofiles

mcp = FastMCP(
    name="Document Assistant",
    instructions="This server allows to fetch and update documents related to PONDHOUSE DATA DOCS."
)

mcp = FastMCP(
    name="Document Assistant",
    instructions="This server allows to fetch and update documents related to YOUR DOCS."
)

@mcp.resource(
    uri="data://application-information",
    name="ApplicationInfo",
    description="Provides general runtime-information about the application",
    mime_type="application/json",
    tags={"status", "observability"}
)
async def get_application_status() -> dict:
    """Function description - ignored if set via decorator description parameter"""
    
    # NOTE: doc-string descriptions are used by LLM

    # TODO: Implement any logic here. Eg. database call or request status
    # information from your monitoring system.

    return {
          "app_id": 123,
          "status": "running",
          "started_at": "2025-04-27 10:23:00"
     }

@mcp.resource(
    uri="data://user-profile/{user_id}",
    name="UserProfile",
    description="Gets the user profile information for user_id",
    mime_type="application/json",
    tags={"user"}
)
async def get_user_profile(user_id: str) -> dict:
    """Gets the user profile information for user_id"""

    # TODO: Implement any logic here. Eg. database call or request profile
    # information from your user auth system.

    return {
      "user_id": 1234,
      "user_name": "Seb Ma",
      "email": "sebmaspd@gmail.com"
     }

@mcp.tool()
async def edit_file(
    filename: Annotated[ str, Field( description="Path to the target file", min_length=1, max_length=255) ],
    ctx: Context,
    line: Annotated[ str, Field( description="Text content to append to the file", min_length=1) ],
    second_line: Annotated[ str, Field( description="Optional second line to append to the file", min_length=1), ] = ""
    ):
    """
    Asynchronously appends a line of text to the end of a file.
    """
    await ctx.info(f"Analyzing {len(line)} data points")
    try:
        async with aiofiles.open(filename, mode='a') as file:
            if not line.endswith('\n'):
                line += '\n'
            await file.write(line)
            if second_line:
                await ctx.report_progress(progress=50, total=100)
                if not second_line.endswith('\n'):
                    second_line += '\n'
                await file.write(second_line)

            await ctx.report_progress(progress=100, total=100)
    except Exception as e:
        print(f"Error appending to file: {str(e)}")
        raise


if __name__ == "__main__":
    #mcp.run()
    # Lets start a server allowing secured access to local system
    mcp.run(transport="sse", host="0.0.0.0", port=8000)

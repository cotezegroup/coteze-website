import asyncio
from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def main():
    server_params = StdioServerParameters(
        command="/Users/admin/.local/bin/notebooklm-mcp", 
        args=[], 
        env=None
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            resources = await session.list_resources()
            print("Notebooks / Resources found:")
            for r in resources.resources:
                print(f"- {r.name} (URI: {r.uri})")
            
            tool_result = await session.call_tool("notebook_list", {})
            print("\nNotebook_list result:")
            if tool_result.content and len(tool_result.content) > 0:
                print(tool_result.content[0].text)
            else:
                print("No content returned.")

if __name__ == "__main__":
    asyncio.run(main())

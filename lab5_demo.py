import anyio

from mcp import Client

from app.connectors.meeting_mcp_server import mcp_server


async def main():

    print("\n========================================")
    print("       MCP CONNECTOR DEMONSTRATION")
    print("========================================")

    # Connect to the MCP server
    async with Client(mcp_server) as client:

        print("\n1. CONNECTED TO MCP SERVER")

        print("Server:", client.server_info.name)

        # Discover available tools
        print("\n2. DISCOVERING AVAILABLE TOOLS")

        tools = await client.list_tools()

        for tool in tools.tools:
            print("-", tool.name)

        # Call the availability tool
        print("\n3. CALLING AVAILABILITY TOOL")

        availability = await client.call_tool(
            "check_meeting_availability",
            {
                "participants": "Dr. Ravi, Dr. Priya",
                "proposed_time": "10:00 AM",
            },
        )

        print("Tool result:")

        for item in availability.content:
            if hasattr(item, "text"):
                print(item.text)

        # Call the meeting-memory search tool
        print("\n4. SEARCHING PREVIOUS MEETINGS")

        history = await client.call_tool(
            "search_previous_meetings",
            {
                "keyword": "semester",
            },
        )

        print("Memory result:")

        for item in history.content:
            if hasattr(item, "text"):
                print(item.text)

        # Read the MCP resource
        print("\n5. READING MEETING MEMORY RESOURCE")

        resource = await client.read_resource(
            "meeting-memory://recent"
        )

        for item in resource.contents:
            if hasattr(item, "text"):
                print(item.text)

    print("\nMCP CONNECTOR TEST COMPLETED.")


if __name__ == "__main__":
    anyio.run(main)
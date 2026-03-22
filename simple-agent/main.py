from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from .env file
load_dotenv()

# Initialize the Anthropic language model with specified parameters
model = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    temperature=0,
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Define server parameters for the MCP server using Firecrawl
server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY")
    },
    args=["firecrawl-mcp"]
)

async def main():
    """
    Main asynchronous function to run the simple agent.
    Sets up the MCP client session, loads tools, creates the agent, and handles user interaction.
    """
    # Establish stdio client connection to the MCP server
    async with stdio_client(server_params) as (reader, write):
        # Create a client session with the server
        async with ClientSession(reader, write) as session:
            # Initialize the session
            await session.initialize()
            # Load MCP tools from the session
            tools = await load_mcp_tools(session)
            # Create a ReAct agent with the model and tools
            agent = create_react_agent(model, tools)

            # Define system message for the agent
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can use that can scrape websites, crawl pages and extract data using Firecrawl. Think step by step and use the appropriate tools at your disposal to answer the user's question."
                }
            ]

            # Print available tools for user reference
            print("Available tools:")
            for tool in tools:
                print(f" - {tool.name}")
            print('-'*60)

            # Main interaction loop
            while True:
                user_input = input("\nYou: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting...")
                    break

                # Append user message to conversation
                messages.append({"role": "user", "content": user_input})

                try:
                    # Invoke the agent with the current messages
                    agent_response = await agent.ainvoke({"messages": messages})
                    ai_message = agent_response["messages"][-1].content
                    print(f"\nAgent: {ai_message}")
                except Exception as e:
                    print(f"Error: {e}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    asyncio.run(main())
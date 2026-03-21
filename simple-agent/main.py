from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


model = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    temperature=0,
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY")
    },
    args=["firecrawl-mcp"]
)

async def main():
    async with stdio_client(server_params) as (reader, write):
        async with ClientSession(reader, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)

            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can use that can scrape websites, crawl pages and extract data using Firecrawl. Think step by step and use the appropriate tools at your disposal to answer the user's question."
                }
            ]

            print("Available tools:")
            for tool in tools:
                print(f" - {tool.name}")
            print('-'*60)

            while True:
                user_input = input("\nYou: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting...")
                    break

                messages.append({"role": "user", "content": user_input})

                try:
                    agent_response = await agent.ainvoke({"messages": messages})
                    ai_message = agent_response["messages"][-1].content
                    print(f"\nAgent: {ai_message}")
                except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
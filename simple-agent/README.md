# Simple Agent

A basic AI agent that uses MCP (Model Context Protocol) with Firecrawl for web scraping and data extraction. This agent provides a simple command-line interface for interacting with web content using natural language queries.

## Features

- **Web Scraping**: Uses Firecrawl to scrape and extract data from websites
- **MCP Integration**: Leverages Model Context Protocol for tool integration
- **LangChain Integration**: Built with LangChain and LangGraph for agent orchestration
- **Anthropic Claude**: Powered by Claude Haiku for intelligent responses
- **Command-line Interface**: Simple interactive CLI for user queries

## Prerequisites

- Python 3.8+
- Node.js and npm (for Firecrawl MCP server)
- API keys for Anthropic and Firecrawl

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple-agent
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   # or using uv
   uv sync
   ```

3. Install the Firecrawl MCP server globally:
   ```bash
   npm install -g firecrawl-mcp
   ```

4. Set up environment variables:
   Create a `.env` file in the project root:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   ```

## Usage

Run the agent:
```bash
python main.py
```

The agent will start an interactive session. You can ask questions like:
- "Scrape the pricing information from example.com"
- "Extract all the blog posts from techsite.com"
- "Find information about AI tools on developer websites"

Type "exit" or "quit" to end the session.

## Architecture

- `main.py`: Entry point and main agent loop
- `pyproject.toml`: Project configuration and dependencies
- `.env`: Environment variables (not committed to version control)

## Dependencies

- `mcp`: Model Context Protocol client
- `langchain`: Framework for building LLM applications
- `langgraph`: Library for creating agent workflows
- `langchain-anthropic`: Anthropic Claude integration
- `python-dotenv`: Environment variable management
- `firecrawl-py`: Firecrawl Python SDK

## Configuration

The agent is configured to use:
- Claude Haiku 4.5 (20251001) model
- Temperature 0 for deterministic responses
- Firecrawl MCP server for web scraping tools


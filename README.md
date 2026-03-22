# Dev Recommendation AI Tool

A collection of AI agents for developer tool research and recommendations. This project contains two agent implementations: a simple MCP-based agent and an advanced workflow-based agent for analyzing and recommending developer tools.

## Project Structure

```
dev-recommendation-ai-tool/
├── simple-agent/          # Basic MCP agent with Firecrawl integration
│   ├── main.py           # CLI interface for simple interactions
│   ├── pyproject.toml    # Project configuration and dependencies
│   ├── README.md         # Simple agent documentation
│   └── .env              # Environment variables (not committed)
└── advacned-agent/       # Advanced agent with structured analysis workflow
    ├── main.py           # CLI interface for tool recommendations
    ├── src/              # Source code modules
    │   ├── workflow.py   # LangGraph workflow orchestration
    │   ├── firecrawl.py  # Firecrawl service wrapper
    │   ├── models.py     # Pydantic data models
    │   └── prompts.py    # LLM prompt templates
    ├── pyproject.toml    # Project configuration and dependencies
    ├── README.md         # Advanced agent documentation
    └── .env              # Environment variables (not committed)
```

## Agents Overview

### Simple Agent
- **Purpose**: Basic web scraping and data extraction using MCP
- **Technology**: LangChain + MCP + Firecrawl
- **Use Case**: General web content analysis and extraction
- **Interface**: Command-line chat interface

### Advanced Agent
- **Purpose**: Structured analysis and recommendations for developer tools
- **Technology**: LangGraph workflow + Firecrawl + Pydantic models
- **Use Case**: Developer tool research, comparisons, and recommendations
- **Interface**: Query-based analysis with detailed output

## Prerequisites

- Python 3.13+
- Node.js and npm (for Firecrawl MCP server in simple-agent)
- API keys for Anthropic Claude and Firecrawl

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd dev-recommendation-ai-tool
   ```

2. **Set up environment variables**:
   Create `.env` files in both agent directories:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   FIRECRAWL_API_KEY=your_firecrawl_api_key
   ```

3. **Install dependencies**:
   For simple-agent:
   ```bash
   cd simple-agent
   uv sync  # or pip install -r requirements.txt
   npm install -g firecrawl-mcp  # For MCP server
   ```

   For advanced-agent:
   ```bash
   cd advacned-agent
   uv sync  # or pip install -r requirements.txt
   ```

4. **Run the agents**:
   ```bash
   # Simple agent
   cd simple-agent && python main.py

   # Advanced agent
   cd advacned-agent && python main.py
   ```

## Use Cases

### Simple Agent
- Web scraping and content extraction
- General data gathering from websites
- Interactive Q&A with web content

### Advanced Agent
- "Best database alternatives to MongoDB"
- "API testing tools comparison"
- "Frontend frameworks for 2024"
- "CI/CD solutions for small teams"
- "Cloud storage options for developers"

## Architecture

### Simple Agent Architecture
- MCP client-server architecture
- LangChain ReAct agent pattern
- Firecrawl for web content access
- Command-line interface

### Advanced Agent Architecture
- LangGraph state machine workflow
- Multi-step analysis pipeline:
  1. Tool extraction from articles
  2. Company/website research
  3. Structured analysis
  4. Recommendation generation
- Pydantic models for data validation
- Structured LLM outputs

## Contributing

1. Choose the appropriate agent for your contribution
2. Follow the existing code structure and patterns
3. Add comprehensive docstrings and comments
4. Test your changes thoroughly
5. Update relevant README files
6. Submit a pull request


## Support

For issues and questions:
- Check the individual agent READMEs
- Review the code comments and docstrings
- Test with sample queries to understand behavior
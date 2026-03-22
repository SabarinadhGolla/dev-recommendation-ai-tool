# Advanced Developer Tools Recommendation Agent

An intelligent AI agent that analyzes and recommends developer tools and technologies. This advanced agent uses a structured workflow to research, analyze, and provide recommendations for developer tools based on natural language queries.

## Features

- **Intelligent Tool Discovery**: Automatically extracts relevant tools from articles and comparisons
- **Comprehensive Analysis**: Analyzes pricing models, tech stacks, APIs, and integrations
- **Structured Recommendations**: Provides concise, actionable recommendations for developers
- **Web Scraping Integration**: Uses Firecrawl for real-time data collection from official websites
- **LangGraph Workflow**: Orchestrates complex analysis workflows with state management
- **Pydantic Models**: Structured data models for consistent analysis output

## Prerequisites

- Python 3.8+
- API keys for Anthropic and Firecrawl

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd advacned-agent
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   # or using uv
   uv sync
   ```

3. Set up environment variables:
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

Enter your developer tool queries, such as:
- "database alternatives to PostgreSQL"
- "best API testing tools"
- "frontend frameworks comparison"
- "CI/CD tools for small teams"

The agent will:
1. Search for relevant articles and extract tool names
2. Research official websites for detailed information
3. Analyze pricing, features, and developer aspects
4. Provide concise recommendations

## Architecture

### Core Components

- `main.py`: CLI interface and result display
- `src/workflow.py`: Main LangGraph workflow orchestration
- `src/firecrawl.py`: Firecrawl service wrapper
- `src/models.py`: Pydantic data models
- `src/prompts.py`: LLM prompt templates
- `pyproject.toml`: Project configuration

### Workflow Steps

1. **Tool Extraction**: Searches articles and extracts relevant tool names using LLM
2. **Research**: Scrapes official websites and gathers detailed information
3. **Analysis**: Analyzes each tool's features, pricing, and developer aspects
4. **Recommendations**: Generates concise recommendations based on analysis

## Dependencies

- `langchain`: LLM application framework
- `langgraph`: Agent workflow orchestration
- `langchain-anthropic`: Claude integration
- `firecrawl-py`: Web scraping service
- `pydantic`: Data validation and models
- `python-dotenv`: Environment management

## Configuration

The agent uses:
- Claude Haiku 4.5 (20251001) with temperature 0.1
- Structured output parsing for consistent results
- Firecrawl for web content extraction
- Markdown format for scraped content

## Analysis Categories

For each tool, the agent analyzes:
- **Pricing Model**: Free, Freemium, Paid, Enterprise
- **Open Source Status**: Whether the tool is open source
- **Tech Stack**: Supported languages, frameworks, databases
- **API Availability**: REST, GraphQL, SDK support
- **Language Support**: Programming languages supported
- **Integration Capabilities**: Compatible tools and platforms

## Example Output

```
Developer Tools Query: database alternatives to PostgreSQL

Analysis Result for database alternatives to PostgreSQL
============================================================

1. 🏢 Supabase
   🌐 Website: https://supabase.com
   💰 Pricing: Freemium
   📖 Open Source: true
   🛠️  Tech Stack: PostgreSQL, TypeScript, React
   💻 Language Support: JavaScript, TypeScript, Python
   🔌 API: ✅ Available
   🔗 Integrations: Vercel, Netlify, GitHub
   📝 Description: Open source Firebase alternative with PostgreSQL backend

Developer Recommendations:
Supabase offers the best balance of PostgreSQL compatibility and developer experience. Freemium pricing makes it accessible for startups. Its real-time capabilities and extensive API support provide significant advantages over plain PostgreSQL.
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Update documentation
6. Submit a pull request

## License

[Add your license information here]
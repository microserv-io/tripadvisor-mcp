# Tripadvisor MCP Server

A [Model Context Protocol][mcp] (MCP) server for the Tripadvisor Content API.

This provides access to Tripadvisor location data, reviews, and photos through standardized MCP interfaces, allowing AI assistants to search and analyze travel information.

[mcp]: https://modelcontextprotocol.io

## Features

- [x] Search for locations (hotels, restaurants, attractions) on Tripadvisor
- [x] Get detailed information about specific locations
- [x] Retrieve reviews and photos for locations
- [x] Search for nearby locations based on coordinates
- [x] API Key authentication
- [x] Resources for static data access
- [x] Interactive tools for AI assistants

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/tripadvisor-mcp.git
cd tripadvisor-mcp
```

Install the package:

```bash
pip install -e .
```

For development, install with additional dependencies:

```bash
pip install -e ".[dev]"
```

## Configuration

Set your Tripadvisor Content API key:

```bash
export TRIPADVISOR_API_KEY=your_api_key_here
```

Alternatively, create a `.env` file in the project root:

```
TRIPADVISOR_API_KEY=your_api_key_here
```

## Usage

### Run the MCP Server

```bash
tripadvisor-mcp
```

### Install in Claude Desktop

To install this server in Claude Desktop, add the following to your client configuration file:

```json
{
  "mcpServers": {
    "tripadvisor": {
      "command": "uv",
      "args": [
        "--directory",
        "<full path to tripadvisor-mcp directory>",
        "run",
        "src/tripadvisor_mcp/main.py"
      ],
      "env": {
        "TRIPADVISOR_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

> Note: If you see `Error: spawn uv ENOENT` in Claude Desktop, you may need to specify the full path to `uv` or use `python` instead of `uv run`.

#### Alternative Installation Method

You can also use the MCP command line tools to install the server:

```bash
mcp install src/tripadvisor_mcp/main.py -n "Tripadvisor API" -v TRIPADVISOR_API_KEY=your_api_key_here
```

### Development Mode with MCP Inspector

For development and testing, use the MCP Inspector:

```bash
mcp dev src/tripadvisor_mcp/main.py
```

## MCP Tools

This server provides the following tools:

| Tool | Description |
| --- | --- |
| `search_locations` | Search for locations by query text, category, and other filters |
| `search_nearby_locations` | Find locations near specific coordinates |
| `get_location_details` | Get detailed information about a location |
| `get_location_reviews` | Retrieve reviews for a location |
| `get_location_photos` | Get photos for a location |

### Example Tool Usage

When using Claude with the MCP server installed, you can ask questions like:

- "Find hotels in New York City"
- "Show me restaurants near the Eiffel Tower"
- "What are the reviews for the Museum of Modern Art?"
- "Show me photos of the Grand Canyon"

## MCP Resources

Resources are available at:

| Resource URI | Description |
| --- | --- |
| `tripadvisor://search-results/{query}` | Results for a search query |
| `tripadvisor://location/{location_id}` | Details for a specific location |
| `tripadvisor://reviews/{location_id}` | Reviews for a specific location |
| `tripadvisor://photos/{location_id}` | Photos for a specific location |

## Project Structure

The project structure follows standard Python packaging conventions:

```
tripadvisor-mcp/
├── .env.template           # Template for environment variables
├── .gitignore              # Git ignore file
├── README.md               # This file
├── pyproject.toml          # Project configuration
└── src/
    └── tripadvisor_mcp/
        ├── __init__.py     # Package initialization
        ├── main.py         # Main application logic
        └── server.py       # MCP server implementation
```

## Development

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

This project uses standard Python tooling. To set up a development environment:

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Install development dependencies
pip install -e ".[dev]"
```

## License

MIT

---

[mcp]: https://modelcontextprotocol.io

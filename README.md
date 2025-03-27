# Tripadvisor MCP Server

This repository contains a Model Context Protocol (MCP) server implementation for the Tripadvisor Content API. It provides tools and resources for interacting with Tripadvisor location data, reviews, and photos.

## Features

- Search for locations (hotels, restaurants, attractions) on Tripadvisor
- Get detailed information about specific locations
- Retrieve reviews and photos for locations
- Search for nearby locations based on coordinates

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

```bash
mcp install src/tripadvisor_mcp/main.py
```

### Development Mode with MCP Inspector

```bash
mcp dev src/tripadvisor_mcp/main.py
```

## MCP Tools

This server provides the following tools:

1. `search_locations` - Search for locations by query text, category, and other filters
2. `search_nearby_locations` - Find locations near specific coordinates
3. `get_location_details` - Get detailed information about a location
4. `get_location_reviews` - Retrieve reviews for a location
5. `get_location_photos` - Get photos for a location

## MCP Resources

Resources are available at:

1. `tripadvisor://search-results/{query}` - Results for a search query
2. `tripadvisor://location/{location_id}` - Details for a specific location
3. `tripadvisor://reviews/{location_id}` - Reviews for a specific location
4. `tripadvisor://photos/{location_id}` - Photos for a specific location

## License

MIT

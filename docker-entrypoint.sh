#!/bin/bash
set -e

# Output environment variables for debugging (excluding secrets)
echo "Starting Tripadvisor MCP Server in Docker..."
echo "  API Key: ${TRIPADVISOR_API_KEY:0:4}****"

# Run the MCP server
exec /app/.venv/bin/python -m tripadvisor_mcp.main "$@"

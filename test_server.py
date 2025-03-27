
import os
from dotenv import load_dotenv
load_dotenv()

# Set the API key directly for testing
os.environ["TRIPADVISOR_API_KEY"] = "test_api_key_12345"

from src.tripadvisor_mcp.server import mcp, config

print("MCP Server configuration:")
print(f"  Name: {mcp.name}")
print(f"  API Key: {'*' * (len(config.api_key) - 4)}...{config.api_key[-4:] if config.api_key else 'Not set'}")
print(f"  Base URL: {config.base_url}")

print("\nServer test completed successfully!")

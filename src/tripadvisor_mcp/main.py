#!/usr/bin/env python
import sys
import argparse
import dotenv
from tripadvisor_mcp.server import mcp, config


def setup_environment():
    if dotenv.load_dotenv():
        print("Loaded environment variables from .env file")
    else:
        print("No .env file found or could not load it - using environment variables")

    if not config.api_key:
        print("ERROR: TRIPADVISOR_API_KEY environment variable is not set")
        print("Please set it to your Tripadvisor Content API key")
        return False

    print("Tripadvisor Content API configuration:")
    print(
        f"  API Key: {'*' * (len(config.api_key) - 8) + config.api_key[-8:] if config.api_key else 'Not set'}"
    )
    print(f"  Base URL: {config.base_url}")

    return True


def parse_args():
    parser = argparse.ArgumentParser(description="Tripadvisor MCP Server")
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port to listen on for SSE transport. If not specified, uses stdio transport.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to bind to for SSE transport (default: 0.0.0.0)",
    )
    return parser.parse_args()


def run_server():
    """Main entry point for the Tripadvisor MCP Server"""
    args = parse_args()

    # Setup environment
    if not setup_environment():
        sys.exit(1)

    print("\nStarting Tripadvisor MCP Server...")

    if args.port:
        print(f"Running server in SSE mode on {args.host}:{args.port}...")
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        print("Running server in stdio mode...")
        mcp.run(transport="stdio")


if __name__ == "__main__":
    run_server()

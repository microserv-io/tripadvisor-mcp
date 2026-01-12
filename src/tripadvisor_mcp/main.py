#!/usr/bin/env python
import sys
import os
import argparse
import dotenv


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


def setup_environment():
    if dotenv.load_dotenv():
        print("Loaded environment variables from .env file")
    else:
        print("No .env file found or could not load it - using environment variables")

    api_key = os.environ.get("TRIPADVISOR_API_KEY", "")
    if not api_key:
        print("ERROR: TRIPADVISOR_API_KEY environment variable is not set")
        print("Please set it to your Tripadvisor Content API key")
        return False

    print("Tripadvisor Content API configuration:")
    print(
        f"  API Key: {'*' * (len(api_key) - 8) + api_key[-8:] if api_key else 'Not set'}"
    )
    print(f"  Base URL: https://api.content.tripadvisor.com/api/v1")

    return True


def run_server():
    """Main entry point for the Tripadvisor MCP Server"""
    args = parse_args()

    # Set FastMCP settings via environment variables BEFORE importing server
    # This ensures the FastMCP instance uses these settings
    if args.port:
        os.environ["FASTMCP_PORT"] = str(args.port)
        os.environ["FASTMCP_HOST"] = args.host

    # Now import the server (which creates the FastMCP instance)
    from tripadvisor_mcp.server import mcp

    # Setup environment
    if not setup_environment():
        sys.exit(1)

    print("\nStarting Tripadvisor MCP Server...")

    if args.port:
        print(f"Running server in SSE mode on {args.host}:{args.port}...")
        mcp.run(transport="sse")
    else:
        print("Running server in stdio mode...")
        mcp.run(transport="stdio")


if __name__ == "__main__":
    run_server()

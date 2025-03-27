#!/usr/bin/env python

import os
import json
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
import httpx

import dotenv
from mcp.server.fastmcp import FastMCP

dotenv.load_dotenv()
mcp = FastMCP("Tripadvisor Content API MCP")

@dataclass
class TripadvisorConfig:
    api_key: str
    base_url: str = "https://api.content.tripadvisor.com/api/v1"

config = TripadvisorConfig(
    api_key=os.environ.get("TRIPADVISOR_API_KEY", ""),
)

async def make_api_request(endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
    """Make a request to the Tripadvisor Content API"""
    if not config.api_key:
        raise ValueError("Tripadvisor API key is missing. Please set TRIPADVISOR_API_KEY environment variable.")
    
    url = f"{config.base_url}/{endpoint}"
    headers = {
        "accept": "application/json",
        "x-api-key": config.api_key
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params or {})
        response.raise_for_status()
        return response.json()

@mcp.tool(description="Search for locations (hotels, restaurants, attractions) on Tripadvisor")
async def search_locations(
    searchQuery: str,
    language: str = "en",
    category: Optional[str] = None,
    phone: Optional[str] = None,
    address: Optional[str] = None,
    latLong: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for locations on Tripadvisor.
    
    Parameters:
    - searchQuery: The text to search for
    - language: Language code (default: 'en')
    - category: Optional category filter ('hotels', 'attractions', 'restaurants', 'geos')
    - phone: Optional phone number to search for
    - address: Optional address to search for
    - latLong: Optional latitude,longitude coordinates (e.g., '42.3455,-71.0983')
    """
    params = {
        "searchQuery": searchQuery,
        "language": language,
    }
    
    if category:
        params["category"] = category
    if phone:
        params["phone"] = phone
    if address:
        params["address"] = address
    if latLong:
        params["latLong"] = latLong
    
    return await make_api_request("location/search", params)

@mcp.tool(description="Search for locations near a specific latitude/longitude")
async def search_nearby_locations(
    latitude: float,
    longitude: float,
    language: str = "en",
    category: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for locations near a specific latitude/longitude.
    
    Parameters:
    - latitude: Latitude coordinate
    - longitude: Longitude coordinate
    - language: Language code (default: 'en')
    - category: Optional category filter ('hotels', 'attractions', 'restaurants')
    """
    params = {
        "latLong": f"{latitude},{longitude}",
        "language": language,
    }
    
    if category:
        params["category"] = category
    
    return await make_api_request("location/search", params)

@mcp.tool(description="Get detailed information about a specific location")
async def get_location_details(
    location_id: str,
    language: str = "en",
) -> Dict[str, Any]:
    """
    Get detailed information about a specific location (hotel, restaurant, or attraction).
    
    Parameters:
    - location_id: Tripadvisor location ID
    - language: Language code (default: 'en')
    """
    params = {
        "language": language,
    }
    
    return await make_api_request(f"location/{location_id}/details", params)

@mcp.tool(description="Get reviews for a specific location")
async def get_location_reviews(
    location_id: str,
    language: str = "en",
) -> Dict[str, Any]:
    """
    Get the most recent reviews for a specific location.
    
    Parameters:
    - location_id: Tripadvisor location ID
    - language: Language code (default: 'en')
    """
    params = {
        "language": language,
    }
    
    return await make_api_request(f"location/{location_id}/reviews", params)

@mcp.tool(description="Get photos for a specific location")
async def get_location_photos(
    location_id: str,
    language: str = "en",
) -> Dict[str, Any]:
    """
    Get high-quality photos for a specific location.
    
    Parameters:
    - location_id: Tripadvisor location ID
    - language: Language code (default: 'en')
    """
    params = {
        "language": language,
    }
    
    return await make_api_request(f"location/{location_id}/photos", params)

@mcp.resource("tripadvisor://search-results/{query}")
async def search_results_resource(query: str) -> str:
    """
    Resource that returns search results for a given query.
    
    Parameters:
    - query: The search query
    """
    try:
        results = await search_locations(searchQuery=query)
        return json.dumps(results, indent=2)
    except Exception as e:
        return f"Error retrieving search results: {str(e)}"

@mcp.resource("tripadvisor://location/{location_id}")
async def location_details_resource(location_id: str) -> str:
    """
    Resource that returns details for a specific location.
    
    Parameters:
    - location_id: Tripadvisor location ID
    """
    try:
        details = await get_location_details(location_id=location_id)
        return json.dumps(details, indent=2)
    except Exception as e:
        return f"Error retrieving location details: {str(e)}"

@mcp.resource("tripadvisor://reviews/{location_id}")
async def location_reviews_resource(location_id: str) -> str:
    """
    Resource that returns reviews for a specific location.
    
    Parameters:
    - location_id: Tripadvisor location ID
    """
    try:
        reviews = await get_location_reviews(location_id=location_id)
        return json.dumps(reviews, indent=2)
    except Exception as e:
        return f"Error retrieving location reviews: {str(e)}"

@mcp.resource("tripadvisor://photos/{location_id}")
async def location_photos_resource(location_id: str) -> str:
    """
    Resource that returns photos for a specific location.
    
    Parameters:
    - location_id: Tripadvisor location ID
    """
    try:
        photos = await get_location_photos(location_id=location_id)
        return json.dumps(photos, indent=2)
    except Exception as e:
        return f"Error retrieving location photos: {str(e)}"

if __name__ == "__main__":
    print(f"Starting Tripadvisor MCP Server...")
    mcp.run()

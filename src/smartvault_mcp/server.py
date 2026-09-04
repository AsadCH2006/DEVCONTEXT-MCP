import sys
import logging
from fastmcp import FastMCP

# Route all logging exclusively to stderr so stdout remains clean for JSON-RPC
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize FastMCP server
mcp = FastMCP("DevContext")

# Example internal storage for notes/context
context_store = {}

@mcp.tool()
def save_context(key: str, value: str) -> str:
    """Save a context note or key-value pair."""
    context_store[key] = value
    logging.info(f"Saved context key: {key}")
    return f"Context key '{key}' saved successfully."

@mcp.tool()
def get_context(key: str) -> str:
    """Retrieve a stored context note by key."""
    if key not in context_store:
        return f"Key '{key}' not found."
    return context_store[key]

@mcp.tool()
def list_context() -> list:
    """List all stored context keys."""
    return list(context_store.keys())

@mcp.tool()
def delete_context(key: str) -> str:
    """Delete a context entry by key."""
    if key in context_store:
        del context_store[key]
        return f"Key '{key}' deleted successfully."
    return f"Key '{key}' not found."

@mcp.tool()
def clear_context() -> str:
    """Clear all stored context entries."""
    context_store.clear()
    return "All context entries cleared."

@mcp.resource("context://summary")
def get_summary() -> str:
    """Read summary resource of current dev context."""
    total_keys = len(context_store)
    return f"DevContext summary: {total_keys} items currently stored."

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()

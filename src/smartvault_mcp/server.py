import json
import os
import uuid
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Initialize the MCP Server
mcp = FastMCP("SmartVault MCP")

DATA_FILE = Path.home() / ".smartvault" / "notes.json"

def load_notes():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=2)

# --- TOOLS (Actions the AI can perform) ---

@mcp.tool()
def add_note(title: str, content: str, category: str = "general") -> str:
    """Save a new note to the vault."""
    notes = load_notes()
    note_id = str(uuid.uuid4())[:8]
    notes.append({"id": note_id, "title": title, "content": content, "category": category})
    save_notes(notes)
    return f"Saved note '{title}' with ID [{note_id}]."

@mcp.tool()
def list_notes() -> str:
    """List all saved notes."""
    notes = load_notes()
    if not notes:
        return "No notes found in SmartVault."
    return "\n".join([f"- [{n['id']}] {n['title']} ({n['category']})" for n in notes])

@mcp.tool()
def delete_note(note_id: str) -> str:
    """Delete a note by its ID."""
    notes = load_notes()
    filtered = [n for n in notes if n["id"] != note_id]
    if len(filtered) == len(notes):
        return f"Note [{note_id}] not found."
    save_notes(filtered)
    return f"Deleted note [{note_id}]."

# --- RESOURCE (Data stream the AI can read) ---

@mcp.resource("vault://all")
def get_vault() -> str:
    """View all notes formatted in Markdown."""
    notes = load_notes()
    if not notes:
        return "# SmartVault\nNo notes stored."
    return "\n".join([f"## {n['title']}\n{n['content']}\n" for n in notes])

def main():
    mcp.run()

if __name__ == "__main__":
    main()
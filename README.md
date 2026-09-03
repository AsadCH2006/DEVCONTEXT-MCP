# DEVCONTEXT MCP

[![MCP Protocol](https://img.shields.io/badge/MCP-FastMCP-blue.svg)](https://modelcontextprotocol.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Marketplace: Glama](https://img.shields.io/badge/Glama-Listed-green.svg)](https://glama.ai)

**SmartVault MCP** (also known as **DevContext MCP**) is a lightweight, persistent local memory vault and developer scratchpad built on top of the **Model Context Protocol (MCP)** using the `FastMCP` framework. 

Standard AI chat sessions are inherently stateless — once a chat window closes or context limits are hit, valuable architectural decisions, debugging notes, code snippets, and key project context are lost. **SmartVault MCP** solves this problem by giving AI assistants (such as Claude Desktop, Cursor, or custom MCP clients) a secure, local structured storage system to read, write, search, and manage notes across chat sessions.

---

## Hands-On MCP Experience

> **Developer Reflection:**  
> Before building SmartVault MCP, I explored existing MCP implementations (such as the standard Filesystem and Memory MCP servers) within Claude Desktop. Experiencing how MCP standardizes communication via `stdio` JSON-RPC highlighted the power of context-aware AI tooling. 
> 
> Key takeaways from using existing MCP servers:
> - **Seamless Tool Execution**: The AI client automatically infers when to trigger specific tools (e.g., searching or writing files) based on natural language intent without explicit function syntax.
> - **Continuous Context Stream**: Utilizing MCP resources provides persistent background context to the model across multiple chat turns, eliminating the need to re-paste instructions or notes.
> - **Local First Privacy**: Running MCP servers locally ensures all sensitive developer notes and code snippets remain stored securely on the host machine.

---

## Key Features

- **Persistent Local Memory**: Stores all notes structured cleanly in JSON (`~/.smartvault/notes.json`), ensuring your data remains entirely on your local file system.
- **Full Tool Set**: Enables LLMs to execute CRUD operations (Create, Read, Update, Delete), text searches, and pin high-priority notes.
- **Dynamic Resource Stream (`vault://all`)**: Exposes an auto-generated Markdown digest resource that AI assistants can pull directly into their context window for instant workspace awareness.
- **Zero Heavy Dependencies**: Built natively using modern Python standard libraries and the official `mcp` FastMCP SDK.
- **Seamless Local & Marketplace Integration**: Configured for local usage in Claude Desktop and containerized deployment on platforms like Glama or Smithery.

---

## System Architecture

```
┌───────────────────────────────┐
│       AI Assistant Client     │
│  (Claude Desktop / Cursor)    │
└───────────────┬───────────────┘
                │
                │ JSON-RPC (stdio)
                ▼
┌───────────────────────────────┐
│        SmartVault MCP         │
│     (src/smartvault_mcp)      │
│                               │
│  ┌───────────┐ ┌───────────┐  │
│  │ MCP Tools │ │ Resources │  │
│  └─────┬─────┘ └─────┬─────┘  │
└────────┼─────────────┼────────┘
         │             │
         ▼             ▼
┌───────────────────────────────┐
│     Storage Engine (JSON)     │
│   (~/.smartvault/notes.json)   │
└───────────────────────────────┘
```

---

## MCP Capabilities

SmartVault exposes both **MCP Tools** (callable actions) and **MCP Resources** (readable context streams).

### 1. MCP Tools

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `add_note` | `title` (str), `content` (str), `category` (str, optional) | Creates and saves a new note or code snippet into the vault. |
| `list_notes` | *None* | Returns a complete structured list of all saved notes with their metadata. |
| `delete_note` | `note_id` (str) | Permanently deletes a specific note from local storage by ID. |
| `search_notes` | `query` (str) | Performs a case-insensitive search across note titles, contents, and categories. |
| `toggle_pin` | `note_id` (str) | Toggles the pinned status (`true`/`false`) of a note for high-priority context visibility. |

### 2. MCP Resources

| URI | Content Type | Description |
| :--- | :--- | :--- |
| `vault://all` | `text/markdown` | Generates a real-time aggregated Markdown summary of all stored notes, formatted for direct LLM context injection. |

---

## Repository Structure

```text
DEVCONTEXT-MCP/
├── src/
│   └── smartvault_mcp/
│       ├── __init__.py
│       └── server.py          # Core FastMCP server implementation & handlers
├── tests/
│   └── demo_client.py         # Local client test script verifying tools & resources
├── .gitignore                 # Standard Python & environment exclusions
├── Dockerfile                 # Container deployment specification
├── LICENSE                    # MIT Open Source License
├── pyproject.toml             # Python package configuration & entry points
├── README.md                  # Detailed documentation
└── smithery.yaml              # Smithery deployment manifest
```

---

## Quick Start & Local Setup

### Prerequisites

- Python **3.10** or higher
- `pip` or `uv` package manager

### 1. Clone the Repository

```bash
git clone https://github.com/ghostrekon1999/DEVCONTEXT-MCP.git
cd DEVCONTEXT-MCP
```

### 2. Set Up Virtual Environment & Install Dependencies

Using standard `venv`:
```bash
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

pip install -e .
```

---

## Testing Your Local Setup

To verify that the MCP server initializes correctly and handles tool calls without launching Claude Desktop, run the included demo test client:

```bash
python tests/demo_client.py
```

This test client will:
1. Initialize the SmartVault MCP server via `stdio`.
2. Save a test note using `add_note`.
3. Query the vault using `list_notes` and `search_notes`.
4. Read the `vault://all` resource stream.
5. Clean up by executing `delete_note`.

---

## Integrating with Claude Desktop

To connect SmartVault MCP to your local Claude Desktop application:

1. Open your Claude Desktop configuration file:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

2. Add the `smartvault` server definition under `mcpServers`:

```json
{
  "mcpServers": {
    "smartvault": {
      "command": "python",
      "args": [
        "-m",
        "smartvault_mcp.server"
      ],
      "env": {
        "PYTHONPATH": "D:\SPIRAL-WorkFlows\DEVCONTEXT-MCP\src"
      }
    }
  }
}
```
*(Note: Replace the `PYTHONPATH` path above with the absolute path to your project's `src` folder).*

3. Restart Claude Desktop. You will see a hammer icon indicating that the 5 SmartVault tools and 1 resource are active and ready for use.

---

## Example AI Prompts

Once integrated, you can ask your AI assistant:

- **Save context:** *"Save a note under the category 'Backend' titled 'Database Schema' with the contents 'Users table uses UUID v4 for primary keys'."*
- **Recall notes:** *"List all my saved notes in SmartVault."*
- **Search vault:** *"Search my notes for anything related to API endpoints."*
- **Pin priority context:** *"Pin my note about project deployment guidelines."*
- **Read resource:** *"Load the vault://all resource and summarize my active project notes."*

---

## Marketplace Publishing

SmartVault MCP is structured for instant listing and containerized hosting across MCP registries:

- **Glama**: Simply submit the repository URL `https://github.com/ghostrekon1999/DEVCONTEXT-MCP` under the **Add Server** tab.
- **Smithery**: Contains a validated `smithery.yaml` and `Dockerfile` for single-command bundle builds and deployment.

---

## License

This project is open-source software licensed under the [MIT License](LICENSE).

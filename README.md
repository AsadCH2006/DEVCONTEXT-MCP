# SmartVault MCP Server 🔒⚡

SmartVault is a fast, lightweight, zero-bloat Model Context Protocol (MCP) server that grants AI assistants a persistent scratchpad and developer context engine.

## Features
- 🎯 **All 3 MCP Primitives Supported:** Tools, Resources, and Prompts.
- 📌 **Pinning & Tagging:** Keep critical notes prioritized for LLM context retrieval.
- ⚡ **Zero Configuration:** Stores notes locally in `~/.smartvault/notes.json`.

## Installation & Local Setup

```bash
# Clone repository
git clone [https://github.com/YOUR_USERNAME/smartvault-mcp.git](https://github.com/YOUR_USERNAME/smartvault-mcp.git)
cd smartvault-mcp

# Install via uv
uv pip install -e .

# Run test demo
python tests/demo_client.py
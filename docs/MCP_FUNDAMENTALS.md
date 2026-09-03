# Model Context Protocol (MCP) Architecture Overview

## What is MCP?
Model Context Protocol (MCP) is an open specification that standardizes how LLM clients (like Claude Desktop, Cursor, or custom UI apps) communicate with local or remote tool/data providers (MCP Servers).

## Key MCP Primitives
1. **Tools:** Model-controlled functions that perform side effects or data retrieval actions (e.g., creating a note, making an API request).
2. **Resources:** Read-only data streams exposed via URIs (e.g., `vault://all`, `file:///logs.txt`) that provide context to the LLM.
3. **Prompts:** Pre-engineered client templates that guide model interaction workflows (e.g., standup summaries, code reviews).

## Host <-> Client <-> Server Lifecycle
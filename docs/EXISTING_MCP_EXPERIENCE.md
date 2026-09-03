# Hands-On Experience: Exploring Existing MCPs

## Evaluated MCP Server
- **MCP Server Name:** `@modelcontextprotocol/server-playwright` / `Context7`
- **Category:** Web Automation & Dynamic Page Fetching / Technical Documentation Lookup

## What It Does
1. Enables LLMs to launch a browser, navigate to live URLs, fill out forms, and click UI elements.
2. Evaluates dynamic JavaScript rendering to extract structured HTML/Markdown content directly into the conversation context.

## How It Was Useful
- **Automated Verification:** Allowed Claude Desktop to verify local web service endpoints directly during code execution.
- **Dynamic Scraping:** Provided direct access to single-page applications (SPAs) that standard static web crawlers failed to process properly.
- **Reduced Context Switching:** Reduced the need to manually copy-paste server logs or website states back and forth between browser tabs and the client.

## Key Insights
- **Standardized Communication:** Standardized tool definitions allow seamless tool-calling regardless of host system architecture.
- **Primitive Synergy:** Combining **Tools** (actions) with **Resources** (data streams) creates significantly richer context windows.
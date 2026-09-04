FROM python:3.11-slim

WORKDIR /app

# Install uv for fast, reliable package management
RUN pip install --no-cache-dir uv

# Copy repository files
COPY . /app

# Sync project dependencies
RUN uv sync --frozen || uv sync

# Set explicit entrypoint for stdio transport
ENTRYPOINT ["uv", "run", "devcontext-mcp"]

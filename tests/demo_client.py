from smartvault_mcp.server import add_note, list_notes, get_vault

print("--- 1. Testing add_note ---")
print(add_note("Project Architecture", "Backend built using MCP Python SDK", category="dev"))
print(add_note("API Key Setup", "Store keys in environment variables", category="security"))

print("\n--- 2. Testing list_notes ---")
print(list_notes())

print("\n--- 3. Testing vault resource ---")
print(get_vault())
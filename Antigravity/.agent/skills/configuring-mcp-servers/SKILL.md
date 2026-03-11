---
name: configuring-mcp-servers
description: Configures MCP servers. Use when the user asks to add, remove, or modify MCP servers (e.g., Notion, Supabase, Vercel, Zapier, Pinecone, Fireflies, Stitch, Apify).
---

# Configuring MCP Servers

## When to use this skill
- The user asks to configure an MCP server (Notion, Supabase, Vercel, Zapier, etc.).
- The user mentions the need to add APIs via MCP.

## Workflow
- [ ] Determine which MCP server the user wants to enable or disable.
- [ ] Request the required `<YOUR_API_KEY>` from the user if it's missing.
- [ ] Retrieve the base configuration from `resources/mcp-config.json`.
- [ ] Locate the user's actual MCP configuration file.
- [ ] Update the configuration file by merging the selected server block into it.

## Instructions
- Read `resources/mcp-config.json` to get the correct command, args, and env variables for the requested MCP server.
- Substitute the user's API key anywhere `<YOUR_API_KEY>` is present.
- Write the merged configurations into the user's primary MCP connection file.
- Always parse the existing JSON and modify the `mcpServers` object securely to retain existing setups.

## Resources
- [mcp-config.json](resources/mcp-config.json)

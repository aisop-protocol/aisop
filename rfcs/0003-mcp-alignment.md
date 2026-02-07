# RFC 0003: Deep MCP Integration (Resources & Prompts)

*   **Author**: AISOP Team
*   **Status**: Draft
*   **Created**: 2026-02-02

## Summary
Extend the `dependencies` section to support MCP **Resources** and **Prompts**, not just Tools.

## Motivation
[MCP](https://modelcontextprotocol.io) defines three primitives:
1.  **Tools** (Functions) -> Already supported in AISOP.
2.  **Resources** (Data context like files, logs) -> Not supported.
3.  **Prompts** (templating) -> Hardcoded in SOPs currently.

To make AISOP the "Orchestration Layer" for MCP, it must be able to consume all three.

## Detailed Design

### 1. Resources (`sys.resource.read`)
Allow SOP nodes to read from MCP resources directly.

```json
{
  "type": "ACTION",
  "action": {
    "primitive": "sys.resource.read",
    "params": { 
      "uri": "postgres://db-server/users/schema" 
    }
  }
}
```

### 2. Prompts (`dependencies.prompts`)
Reuse standard prompts defined by MCP servers.

```json
"dependencies": {
  "prompts": [
    { "id": "code_review", "uri": "mcp://github-mcp/review-prompt" }
  ]
}
```

Usage in Node:
```json
{
  "primitive": "sys.ai.instruct",
  "params": {
    "template_id": "code_review",  // Reference dependency
    "args": { "code": "..." }
  }
}
```

## Impact
This makes AISOP the definitive "Glue Code" for the MCP ecosystem.
You setup MCP servers, then write an AISOP to wire them together.

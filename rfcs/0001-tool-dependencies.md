# RFC 0001: Tool Dependencies & MCP Integration

*   **Author**: AISOP Team
*   **Status**: Draft
*   **Created**: 2026-02-02

## Summary
Introduce a `dependencies` section in the AISOP root object to plainly declare required external tools, enabling runtimes to auto-provision or validate environments. We specifically endorse **MCP (Model Context Protocol)** as the standard URI format.

## Motivation
Current AISOP files assume the host environment has all necessary tools ("magic"). This breaks portability. If an SOP uses `excel.parse`, but the host doesn't have it, execution fails mid-stream.

## Detailed Design

### Schema Change
Add `dependencies` (optional) to root:

```json
{
  "aisop": "1.0",
  "dependencies": {
    "tools": [
      {
        "id": "excel_parser",
        "uri": "mcp://github.com/microsoft/excel-mcp@^1.0",
        "description": "Required for parsing financial reports."
      },
      {
        "id": "ffmpeg",
        "uri": "docker://jrottenberg/ffmpeg:4.4-alpine",
        "cmd": "ffmpeg"
      }
    ]
  },
  "nodes": [...]
}
```

### Runtime Behavior
1.  **Strict Mode**: Runtime MUST verify all tools in `dependencies` are available before starting.
2.  **Auto-Install**: Smart runtimes MAY attempt to fetch the tools via the provided URI (e.g., `git clone` the MCP server).

## Drawbacks
*   Increases complexity of the Runtime (need dependency resolution).
*   URI standards for tools are still fragmenting (MCP vs Docker vs PyPI).

## Alternatives
*   Embed tool code directly in SOP (Bloated, security risk).
*   Ignore dependencies and fail at runtime (Bad UX).

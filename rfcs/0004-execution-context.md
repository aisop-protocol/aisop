# RFC 0004: Standard Execution Context (Identity & Auth)

*   **Author**: AISOP Team
*   **Status**: Draft
*   **Created**: 2026-02-02

## Summary
Define a standard **Execution Context** object that is implicitly available to all nodes alongside `variables`. This standardizes how Identity and Authorization tokens are passed.

## Motivation
Enterprise Agents (like Microsoft's) require strict authentication (On-Behalf-Of flow).
Currently, AISOP has no standard place to store "Who is the user?" or "Where is the GitHub Token?".
If we don't standardize this, every SOP author will invent their own variable names (`$TOKEN`, `$GITHUB_KEY`, `$USER_ID`), killing interoperability.

## Detailed Design

### The `sys.context` Object
A read-only global object available in all expressions `${{ sys.context... }}`.

```typescript
interface ExecutionContext {
  // 1. Identity (The Human)
  user: {
    id: string;       // e.g. "alice@contoso.com"
    name?: string;    // e.g. "Alice Smith"
    locale?: string;  // e.g. "en-US"
    roles?: string[]; // e.g. ["admin", "editor"]
  };

  // 2. Authorization ( The Keys)
  // Map of Provider -> TokenStr
  auth: {
    [provider: string]: string; 
    // e.g. "github": "ghp_...", "microsoft": "ey..."
  };

  // 3. Runtime Info (The Machine)
  runtime: {
    engine: string;   // "ReferenceRuntime"
    version: string;  // "1.0.0"
    mode: "probabilistic" | "deterministic";
  };
}
```

### Usage
In an Action Node:
```json
{
  "primitive": "sys.net.http_request",
  "params": {
    "url": "https://api.github.com/user",
    "headers": {
      // Standard way to get the token
      "Authorization": "Bearer ${{ sys.context.auth.github }}" 
    }
  }
}
```

## Security Implications
*   `sys.context.auth` MUST be redacted in logs.
*   Runtimes MUST sanitize context before injection.

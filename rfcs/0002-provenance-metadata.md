# RFC 0002: Provenance & Execution Mode

*   **Author**: AISOP Team
*   **Status**: Draft
*   **Created**: 2026-02-02

## Summary
Add fields to describe **where** an SOP has been verified (`tested_agents`) and **how** it should be executed (`mode`).

## Motivation
Not all Agents are created equal. An SOP designed for GPT-4 might fail catastrophically on Llama-2.
Users need to know:
1.  **Is my Agent smart enough?** (implied by `tested_agents` history).
2.  **Is this SOP deterministic?** (defined by `mode`).

## Detailed Design

### 1. Execution Mode (`mode`)
Added to root:
*   `deterministic`: Contains NO fuzzy logic (e.g. `sys.ai.instruct`). Input A always equals Output B. Can be run by "dumb" CLI runners.
*   `probabilistic` (Default): Contains AI calls. Output varies. Requires an LLM Runtime.

### 2. Tested Agents (`metadata.tested_agents`)
A list of certification records:

```json
"tested_agents": [
  {
    "engine": "ReferenceRuntime",
    "version": "1.2.0",
    "model": "gpt-4-turbo",
    "success_rate": 1.0,
    "date": "2026-02-02"
  }
]
```

## Drawbacks
*   `tested_agents` is manually maintained and can become stale.
*   "Success Rate" is subjective for probabilistic tasks.

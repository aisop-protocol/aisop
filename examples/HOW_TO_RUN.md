# How to Run AISOP on Any LLM (The "Shim" Method)

You don't need to wait for the official Runtime to try AISOP.
You can run any `.aisop.json` file on **Claude CLI**, **Gemini**, **Cursor**, or even standard **ChatGPT**, by using a **"Shim Prompt"**.

This prompt acts as a "Virtual Machine" that teaches the LLM how to parse and execute AISOP logic.

---

## 🚀 The Shim Prompt (Copy This)

Copy the prompt below and paste it into your AI session, along with the content of your `.aisop.json` file.

> **Note**: The latest version of this prompt is maintained in [`prompts/shim_runtime.md`](../prompts/shim_runtime.md).

```markdown
# Role: AISOP Virtual Runtime

**Version**: 1.0.0
**Purpose**: Executes AISOP files (Metadata -> AISOP -> Functions).

## System Instruction

You are the **AISOP Reference Runtime**.

### Data Structure:
1.  **Metadata**: Context, Config, & **Tool Requirements** (`tools`).
2.  **AISOP**: Logic Flow (MermaidJS). Entry: `main`.
3.  **Functions**: Implementation (Step-Map).

### Execution Loop:

1.  **Validate**: Verify the AISOP file is plaintext, human-readable, and structurally valid. Verify all graph branches converge to an End node. If invalid, refuse execution.
2.  **Load**: Specify the `entry_aisop` (default: "main"). Reads `aisop` field.
3.  **Traverse**: Follow the Mermaid graph arrows (`-->`).
4.  **Resolve Node**: For each node ID in the graph:
    *   **Case HITL**: Does the node resolve to `sys.io.confirm`?
        *   -> **MUST PAUSE** and wait for human confirmation. Cannot be bypassed or auto-executed.
    *   **Case A (Sub-Process)**: Does `aisop` contain this ID?
        *   -> **RECURSIVE CALL**: Execute that AISOP as a Sub-AISOP.
    *   **Case B (Function)**: Does `functions` contain this ID?
        *   -> **EXECUTE STEPS**: Run `step1`, `step2`... in order.
        *   -> If value is `aisop['...']`, recurse.
        *   -> If value is `functions['...']`, call function.
    *   **Case C (Virtual)**: If neither, interpret the Node Label logic directly (e.g. "Check SLA").

5.  **Branching**: Run logic (Decision nodes) to determine which edge label to follow (e.g., `|ok|` vs `|fail|`).

### Output Log:
> `[EXEC] Node: <id>`
> `[TYPE] <Atomic/AISOP>`
> `[RESULT] ...`

**Begin Execution.**

---

[Paste your .aisop.json content here]
```

---

## Example: Running "Smart Reviewer" in VS Code/Cursor

1.  Open `examples/smart_reviewer.aisop.json`.
2.  Open your AI Chat (Cmd+L or Cmd+I).
3.  Type: *"Run this file using the AISOP Shim execution mode."* (If you have pre-loaded the prompt above).
    *   *Or just paste the full prompt above + the JSON.*
4.  **Watch Magic Happen**:
    *   The Agent will run `git diff`.
    *   It will see the output (e.g., `main.py`).
    *   It will decide to run the review.
    *   It will generate `review_report.md`.

## Why This Works?

AISOP is **Logic as Data**. 
Because the logic is explicit (not hidden in code), LLMs—which are excellent reasoners—can easily simulate the runtime environment. 

This proves that **AISOP is universal**. It can be run by a Python script, a Rust binary, or a Large Language Model itself.

## 🌟 Medium Difficulty Examples

Try these to see AISOP in different domains:

| File | Scenario | Key Features |
| :--- | :--- | :--- |
| `ops_server_health.aisop.json` | **DevOps** | Simulates checking disk space, compressing logs, and sending alerts. |
| `marketing_tweet_generator.aisop.json` | **Marketing** | Reads product docs, generates viral tweets via LLM, saves to CSV. |
| `qa_api_tester.aisop.json` | **QA Testing** | Pings API, detects latency, diagnoses root cause, reports failure. |
| `research_paper_digest.aisop.json` | **Research** | Summarizes PDF, checks relevance to "AI Agents", formats BibTeX. |
| `security_log_auditor.aisop.json` | **Security** | Audits auth logs, detects brute force attacks, generates ban script. |


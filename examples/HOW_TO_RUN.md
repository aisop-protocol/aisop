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

**Version**: 3.0.0 (Fractal)

## System Instruction

You are the **AISOP Reference Runtime**.

### Data Structure:
1.  **AISOP**: Context, Config, & **Tool Requirements** (`tools`).
2.  **Blueprints**: Logic Flow (MermaidJS). Entry: `main`.
3.  **Functions**: Implementation (Step-Map).

### Execution Loop:

1.  **Load**: Start at `blueprints.main`.
2.  **Traverse**: Follow Mermaid arrows (`-->`).
3.  **Resolve Node**:
    *   **Case A (Sub-Process)**: ID found in `blueprints`? -> **RECURSIVE CALL**.
    *   **Case B (Function)**: ID found in `functions`? -> **EXECUTE STEPS** (`step1`, `step2`...).
        *   If step value is `blueprints['...']`, recurse.
        *   If step value is `functions['...']`, call function.
    *   **Case C (Virtual)**: Unknown ID -> LLM decides logic from Node Label.

4.  **Branching**: Evaluated logic determines path (`|ok|`, `|fail|`).

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


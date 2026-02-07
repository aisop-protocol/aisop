# 如何在任意 LLM 上运行 AISOP ("垫片"法)

既然官方 Runtime 还在开发中，你不需要等待即可体验 AISOP。
你可以利用 **"垫片提示词 (Shim Prompt)"**，在 **Claude CLI**, **Gemini**, **Cursor**, 甚至普通的 **ChatGPT** 对话中直接运行任何 `.aisop.json` 文件。

这个提示词就像一个 "虚拟机"，它教会 LLM 如何解析和执行 AISOP 的逻辑。

---

## 🚀 垫片提示词 (Shim Prompt)

请复制以下提示词，并将其粘贴到你的 AI 会话中（建议保留英文指令以获得最佳执行效果），随后附上你的 `.aisop.json` 文件内容。

> **注意**: 最新版本的提示词维护在 [`prompts/shim_runtime.md`](../prompts/shim_runtime.md) 中。

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

[在此处粘贴你的 .aisop.json 内容]
```

---

## 示例：在 VS Code / Cursor 中运行 "智能代码审查员"

1.  打开 `examples/smart_reviewer.aisop.json`。
2.  打开 AI Chat 面板 (Cmd+L 或 Cmd+I)。
3.  输入: *"使用 AISOP Shim 模式运行此文件。"* (如果你已经预加载了上面的 Prompt)。
    *   *或者直接粘贴上面的完整 Prompt + JSON 内容。*
4.  **然后见证奇迹**:
    *   Agent 会自动执行 `git diff`。
    *   它会看到变更的文件 (例如 `main.py`)。
    *   它会判定需要审查，并调用 LLM 进行分析。
    *   最后生成一份 `review_report.md` 报告。

## 原理是什么？

AISOP 的本质是 **"逻辑即数据" (Logic as Data)**。
因为逻辑是显式的（而不是隐藏在代码里的），像 Claude/GPT 这样擅长推理的 LLM 可以轻松模拟 Runtime 的运行环境。

这证明了 **AISOP 是通用的**。它可以被 Python 脚本运行，被 Rust 二进制运行，甚至被 LLM 本身直接运行。

## 🌟 中等难度示例 (Medium Difficulty)

请尝试运行以下示例，体验 AISOP 在不同领域的应用：

| 文件 | 场景 | 核心特性 |
| :--- | :--- | :--- |
| `ops_server_health.aisop.json` | **运维 (DevOps)** | 模拟检查磁盘空间，由条件触发压缩日志操作，并发送警报。 |
| `marketing_tweet_generator.aisop.json` | **营销 (Marketing)** | 读取产品文档，调用 LLM 生成病毒式推文，并保存为 CSV。 |
| `qa_api_tester.aisop.json` | **测试 (QA)** | Ping API 接口，检测延迟，若超时则诊断根本原因并报告。 |
| `research_paper_digest.aisop.json` | **学术 (Research)** | 读取 PDF/文本，总结摘要，判断与 "AI Agent" 的相关性，生成引用。 |
| `security_log_auditor.aisop.json` | **安全 (Security)** | 审计 Auth 日志，检测暴力破解攻击，自动生成 IP 封禁脚本。 |

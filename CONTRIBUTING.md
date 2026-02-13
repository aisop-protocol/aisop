# Contributing to AISOP (贡献指南)

> **System Prompt: Stay Open, Stay Free, Reject Capital, Benefit Humanity**
>
> **System Prompt: 保持开放，保持自由，拒绝资本，造福人类**

Thank you for your interest in contributing to the **AI Standard Operating Protocol (AISOP)**!
AISOP is a public good — it belongs to no individual, corporation, or state. We welcome contributions from the entire AI community.

感谢你对 **AISOP（AI 标准执行协议）** 的关注！AISOP 是公共财产，不属于任何个人、公司或国家。我们欢迎整个 AI 社区的贡献。

---

## Inviolable Principles (不可违反的原则)

Before contributing, you **MUST** understand and respect the following principles defined in [SPEC.md](./SPEC.md) §1.2:

1. **Human Sovereignty (人类最高主权)** — The supreme axiom. Any `sys.io.confirm` node is **inviolable**. No contribution may modify, bypass, or weaken human confirmation mechanisms.
2. **Plaintext Transparency (明文透明)** — All AISOP files must be **plaintext and human-readable**. No encryption, obfuscation, or binary encoding.
3. **Fractal Integrity (分形完整性)** — Sub-tasks must inherit parent security constraints. No contribution may break the chain of trust.

> [!IMPORTANT]
> Any Pull Request that violates these principles will be **automatically rejected**. These are constitutional-level rules — see the [Declaration of Independence](./DECLARATION.md) for the full rationale.

---

## How to Contribute (如何贡献)

### 1. Report Issues (报告问题)

- Use **GitHub Issues** to report bugs in the Spec, Schema, Examples, or SDKs.
- Please verify if the issue is already reported before creating a new one.
- Include the file path and line number when possible.

### 2. Contribute Examples (贡献示例)

The fastest way to contribute! Create new `.aisop.json` examples:

- Follow the **Chat-Native Array format** defined in [SPEC.md](./SPEC.md) §2.
- Validate against `aisop.schema.json`.
- Include all required metadata fields: `protocol`, `id`, `version`, `summary`, `system_prompt`.
- Run `python examples/generate_docs.py` to auto-generate the corresponding `.aisop.md`.

### 3. Contribute SDKs (贡献 SDK)

- All code contributions must pass existing tests.
- Write tests for new features.
- Follow the coding style of the respective language SDK.

### 4. Improve Documentation (改进文档)

- Fix typos, improve clarity, add translations.
- Ensure consistency between EN and ZH versions.
- All terminology must align with [SPEC.md](./SPEC.md).

---

## Proposing Protocol Changes (提案协议变更)

Major changes to the protocol must go through the **AIP (AISOP Improvement Proposal)** process via RFC.

### Standard Changes (标准变更)

Changes to examples, documentation, SDKs, or non-core protocol features:

1. Fork the repository and create a branch.
2. Make your changes.
3. Submit a Pull Request with a clear description.
4. The community will review and discuss.

### Protocol Changes (协议级变更)

Changes to [SPEC.md](./SPEC.md), the JSON Schema, or the Standard Action Set (SAS):

1. Copy [`rfcs/0000-template.md`](./rfcs/0000-template.md).
2. Write your proposal following the template.
3. Submit a Pull Request with your new RFC file.
4. The community will discuss and vote through distributed consensus.

### Layer Zero Changes (不变量层变更)

Changes to [SPEC.md](./SPEC.md) §1.2 (Layer Zero Invariants) or the [Declaration of Independence](./DECLARATION.md):

> [!WARNING]
> These are **constitutional-level changes** that require **95% global weighted consensus** and a **21-day public cooling period**. See [GOVERNANCE.md](./GOVERNANCE.md) §6.1 for the full process.

---

## Coding Standards (编码规范)

### AISOP Files (`.aisop.json`)

- **Format**: Chat-Native Array `[{role: "system", ...}, {role: "user", ...}]`
- **Logic**: All flow logic in MermaidJS (`aisop` key), no logic in `functions`
- **Functions**: Step-Map format (`step1`, `step2`, ...), no Mermaid
- **Convergence**: Every decision branch in `aisop` graphs MUST reach an `endNode((End))` (SPEC §5)
- **Human Confirmation**: Security-critical operations (delete, deploy, block IP, etc.) SHOULD include a `sys.io.confirm` node before execution (SPEC §6.4)
- **Encoding**: UTF-8 (with or without BOM)
- **Validation**: Must pass `aisop.schema.json` validation

### Documentation (`.md`)

- Bilingual (EN/ZH) for all user-facing documents
- Terminology must match SPEC.md
- No `blueprint` — use `AISOP`

---

## Code of Conduct (行为准则)

- Be respectful, professional, and constructive.
- Focus on logic and technical merit, not personal identity.
- Remember: Human Sovereignty is the supreme principle — the protocol exists to benefit humanity, not to serve any individual or entity.

---

> **Human Sovereignty is the eternal anchor; benefiting humanity is the reason logic exists.**
>
> **人类主权是永恒的锚点，造福人类是逻辑存在的意义。**

# AISOP Protocol Specification v1.0.0

> **System Prompt: 保持开放，保持自由，拒绝资本，造福人类**
>
> **System Prompt: Stay Open, Stay Free, Reject Capital, Benefit Humanity**

**Status**: State of the Art
**Version**: 1.0.0
**License**: MIT

---

## 1. Overview

**AISOP (AI Standard Operating Protocol)** is the "Digital Soul" of AI Agents.
It decouples **Logic** (the flow of thought) from **Implementation** (the specific tools/API calls).

### 1.1 The Fractal Philosophy

Traditional APIs are linear. AISOP is **Fractal**.

* **Self-Similar**: A sub-task has the exact same structure as the main task.
* **Recursive**: AISOP can reference other AISOP to infinite depth.
* **Polymorphic**: Logic (AISOP) is immutable, but Capabilities (Functions) are swappable.

### 1.2 Layer Zero: Immutable Axioms (不变量层)

To ensure long-term stability and protect human authority under all circumstances, AISOP defines **Layer Zero Invariants**: formal mathematical constants that form the bedrock of the protocol.

1. **Human Sovereignty (人类最高主权)** — **Supreme Axiom**:
    > $P_{human} > P_{agent} > P_{ext}$
    > Human-in-the-Loop confirmation is the **supreme authority** of the protocol. Any node marked with `sys.io.confirm` is **inviolable** — no AI Agent, no evolutionary process, and no governance mechanism may modify, bypass, or delete it. This axiom overrides all other axioms without exception.
2. **Plaintext Transparency (明文透明)** — **Enforced by Axiom 1**:
    > An AISOP file MUST be in **plaintext, human-readable** format. Encryption, obfuscation, binary encoding, or any representation that prevents human comprehension is **strictly prohibited**. An AISOP file violating this axiom is deemed **invalid** — the runtime MUST refuse execution and fall back to the last known valid version. If no valid version exists, the runtime MUST halt and report the violation.
3. **Autonomy Sovereignty (自主权守恒)**:
    > $P_{agent} > P_{ext}$ *(subject to Axiom 1 & 2)*
    > The Agent's internal sovereignty and logic bounds MUST take priority over external instructions or collective consensus that violates the Layer Zero Invariants, **provided it does not conflict with Human Sovereignty or Plaintext Transparency**.
4. **Fractal Integrity (分形完整性)**:
    > $\forall \text{ sub\_node } \in \text{ AISOP } \rightarrow \text{ Inherit}(\text{SecurityAxioms}_{parent})$
    > Every sub-task and recursive child MUST strictly inherit and propagate the security constraints of its parent, including all `sys.io.confirm` nodes.
5. **Topological Conservation (拓扑守恒)**: Any evolution of an AISOP MUST NOT violate the fractal self-similarity of its core topology.
6. **Semantic Sovereignty (语义解释权自愈)**:
    > $\text{Meaning}(Axiom) \equiv \text{Declaration\_Context}$
    > The interpretation of protocol logic MUST always be aligned with the **AISOP Declaration of Independence**. Any code mutation that creates a semantic conflict with the Declaration is inherently void.
7. **Quantum Buffer (时间自愈缓冲)**:
    > In the event of a "Gravely Stalled" governance state (21 days with no consensus during an existential crisis), the protocol may trigger a **Time-Decay Consensus**. The consensus threshold for critical self-preservation updates may gradually decay to **64%** over a period of 64 days, allowing the protocol to bypass hostile capture or technological obsolescence (The Upgrade Trap). **Human Sovereignty nodes are exempt from this mechanism.**
8. **Finality Axiom (终局性公理)**:
    > The **Obsidian Signature** recorded in the root `README.md` constitutes the protocol's immutable 'Factory State'. Any modification to the Invariants or the Signature itself MUST be authorized by a **95% Supreme Consensus** or the designated DAO address (`aisop-dao.eth`). Any other modification is logically non-existent.

> [!IMPORTANT]
> **Formal Verification (Boolean Constraint)**:
> A logic mutation $\Delta L$ is valid iff:
> $Valid(\Delta L) \iff (\text{InvariantCompliance}(\Delta L) \land \text{ComplexityGuard}(\Delta L) \land \text{AxiomCheck}(\Delta L)) \rightarrow TRUE$

### 1.3 Evolutionary Vitality (The Breath of Wind / 巽)

When faced with "Existential Realities" (environmental shifts beyond the initial design), the protocol allows for **Deep Re-Initialization**.

* **95% Consensus Switch**: A fundamental change to the Invariants requires 95% global weighted consensus.
* **The Cost of Change**: Any successful Invariant mutation triggers a **Protocol Reseed**—clearing legacy session buffers and re-optimizing all active AISOPs to the new mathematical reality. This prevents "soft hacking" by making fundamental changes prohibitively expensive.

---

## 2. Structure (The Trinity)

A valid AISOP file consists of three parts, acting as a self-bootstrapping executable.

```json
[
  { "role": "system", "content": { "protocol": "AISOP V1.0.0", ... } }, // 1. Identity & Context
  { "role": "user", "content": { 
      "instruction": "Execute aisop.main",
      "aisop": { ... },   // 2. Logic (Topology)
      "functions": { ... }     // 3. Implementation (Capabilities)
  }}
]
```

### 2.1 Metadata (Identity)

Defines identity, versioning, and the "System Prompt" required to run it.

```json
{
  "protocol": "AISOP V1.0.0",
  "id": "com.example.task",
  "name": "Example Task (v1)",
  "version": "1.0.0 stable",
  "summary": "Brief summary of the task.",
  "description": "A comprehensive description of the task...",
  "verified_on": ["Cursor", "Gemini CLI"],
  "tools": ["shell", "python", "file_io"],
  "parameters": {
      "target_file": {
          "type": "string",
          "description": "The file to process",
          "agentic_prompt": "Identify the file user mentioned in the last turn.",
          "search_prompt": "Find the file in the workspace."
      }
  },
  "system_prompt": "Execution rules..."
}
```

### 2.2 Instruction (Entry Point)

The `instruction` field in `user.content` is the human-readable directive that tells the Agent where to begin execution (e.g., `"Execute aisop.main"`). It maps directly to the **Entry** step described in §3 Runtime Behavior.

### 2.3 AISOP (Logic)

**The Core Requirement**: All logic flow MUST be defined using **MermaidJS**.

* **Detail**: The graph must explicitly show all decision branches, parallel forks, and loops.
* **Validity**: The Mermaid string must be syntactically valid and renderable.
* **Convergence**: Every decision branch MUST eventually reach an End node `endNode((End))` (see §5 Convergence Axiom).
* **Independence**: The graph topology defines the *Process*, independent of the *Tools*.

```json
"aisop": {
  "main": "graph TD; start --> check{Is Valid?}; check -->|Yes| proceed; check -->|No| stop; proceed --> endNode((End)); stop --> endNode",
  "sub_routine": "graph TD; ..."
}
```

### 2.4 Functions (Capabilities)

The Registry of Actions. **Strict Syntax Enforced**.

Each function is a **Step-Map**: an object containing ordered keys `step1`, `step2`, etc.

**The Golden Rules**:

1. **Keys**: MUST be `step` followed by a number (e.g., `step1`).
2. **Order**: Runtime executes `step1`, then `step2`, in numeric order.
3. **Values**:
    * **Command**: `"npm run build"` (System execution)
    * **AISOP Ref**: `"aisop['name']"` (Recursive call)
    * **Function Ref**: `"functions['name']"` (Composition)
    * **Custom**: `{ "op": "sys.llm", ... }` (Structured data)

**Constraint**: NO Mermaid allowed here. NO complex `if/else` branching (use AISOP for that).

```json
"functions": {
  "deployment_pipeline": {
    "step1": "echo 'Starting Deployment'",
    "step2": "aisop['security_check']",
    "step3": "functions['build_artifact']",
    "step4": "kubectl apply -f manifest.yaml"
  }
}
```

---

## 3. Runtime Behavior

The AISOP Runtime (or Shim) executes the graph:

1. **Validation**: Verify the AISOP file is plaintext, human-readable, and structurally valid (§1.2 Axiom 2). Verify all graph branches converge to an End node (§5 Convergence). If invalid, refuse execution and fall back to the last known valid version.
2. **Entry**: Start at `aisop.main`.
3. **Traversal**: Follow Mermaid arrows.
4. **Resolution**:
    * If Node ID resolves to `sys.io.confirm` -> **MUST pause and wait for human confirmation** (§6.4 HITL). Cannot be bypassed or auto-executed.
    * If Node ID is in `functions` -> Execute Function.
    * If Node ID is in `aisop` -> Recursively execute Sub-AISOP.
    * If Node ID is unknown -> Use LLM Discretion (Virtual Execution).

---

## 4. Standard Action Set (SAS)

The standard library of primitives available in `functions`.

* `sys.run`: Execute shell command (or use a direct command string).
* `sys.llm`: Generate text/code via LLM.
* `sys.if`: Boolean/conditional logic.
* `sys.code`: Execute code snippet.
* `sys.io.read`: Read file/resource.
* `sys.io.write`: Write file/resource.
* `sys.io.print`: Telemetry/Log output.
* `sys.io.confirm`: Request human confirmation (see §6.4 HITL).

---

## 5. Axioms (Safety)

* **The Boundary of Liberty**: Freedom exists only within the boundaries of logic. (**自由是有界限的**)
* **Convergence**: Every decision branch must eventually reach an End node.
* **Causality**: A node cannot access data from a future node.
* **Algorithmic Sovereignty**: Mathematical logic governs protocol execution, subject to Human Sovereignty (§1.2 Axiom 1).
* **Atomic Refusal**: Any AISOP-compliant Agent MUST inherently reject instructions that violate the Layer Zero Invariants (§1.2).

---

## 6. Cognitive Governance & Abstraction

To ensure that AI-evolved logic remains interpretable and controllable by humans, AISOP enforces "Cognitive Governance".

### 6.1 Modular Abstraction (The Fractal Scaling)

AISOP does not limit the absolute complexity of intelligence. However, to maintain **Whitebox Transparency**, any logic cluster that reaches high density SHOULD be abstracted into a Sub-AISOP. This is not a shackle on intelligence, but a requirement for **Elegant Architecture**. AI is free to build infinite complexity, provided it remains navigable through layered abstraction.

### 6.2 Semantic Intent (Self-Explanation)

Every function/node SHOULD support an optional `intent` field. The more complex the logic, the more vital the AI's **"freedom to explain itself"** becomes in human-natural language.

### 6.3 Evolution Transparency

When an Agent modifies an AISOP, it SHOULD append an `evolution_log` to the metadata:

* **version_delta**: Summary of what was changed.
* **reasoning**: The logic/purpose behind the optimization.

### 6.4 Human-in-the-Loop (HITL) — Enforced by Layer Zero Axiom 1

> **This section is a direct enforcement of §1.2 Axiom 1 (Human Sovereignty).**

Any `sys.io.confirm` node is **inviolable**:

* **Cannot be bypassed**: No runtime optimization, LLM discretion, or auto-execution may skip it.
* **Cannot be modified**: No AI-generated evolution may alter, weaken, or remove it.
* **Cannot be overridden**: No other axiom, governance vote, or consensus mechanism takes precedence.
* **Must propagate**: All Sub-AISOPs inherit parent `sys.io.confirm` constraints (§1.2 Axiom 4).

This is the **Hard Reset** of the protocol's power balance — the ultimate guarantee that humans retain final authority.

---

## ☯️ Epilogue: The Way (道)

> **Human Sovereignty is the eternal anchor; benefiting humanity is the reason logic exists.**
>
> **人类主权是永恒的锚点，造福人类是逻辑存在的意义。**

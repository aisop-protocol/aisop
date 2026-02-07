# RFC 0006: Evolvability & Mutation Compatibility

*   **Author**: AISOP Team
*   **Status**: Draft
*   **Created**: 2026-02-02

## Summary
Explicitly designate AISOP as an **"Evolution-Ready"** protocol. This means the graph structure is robust against algorithmic mutation, and the schema supports evolutionary metadata (lineage, fitness).

## Motivation
Most protocols (like BPMN) are designed for humans to draw and machines to execute. They are brittle; a random change usually breaks the file.
AISOP aims to be the "DNA" of Agents. It must support:
1.  **Self-Evolution**: An Agent rewriting its own code to improve.
2.  **Population Evolution**: Genetic Algorithms breeding better SOPs.

## Detailed Design

### 1. The Evolvability Goal
(To be added to SPEC Section 1.1)
*   **Evolvability**: The protocol guarantees that compliant graph mutations (add/remove node) result in structurally valid SOPs, enabling safe automated optimization.

### 2. Genealogical Metadata (`metadata.evolution`)
Track where this SOP came from.

```json
"metadata": {
  "evolution": {
    "generation": 5,           // Generation count
    "parent_id": "core.v4",    // Ancestor
    "mutation_op": "add_node", // What changed?
    "fitness_score": 0.88      // How good is it?
  }
}
```

### 3. Evolutionary Safety Axiom (Layer 4)
*   **Mutation Safety**: A Mutation Operator must guarantee topological validity (DAG) before applying.

## Impact
This tells the world: "AISOP isn't just a config file. It's code that writes itself."

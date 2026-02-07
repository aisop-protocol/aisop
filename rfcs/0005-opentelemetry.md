# RFC 0005: OpenTelemetry Integration

*   **Author**: AISOP Team
*   **Status**: Draft
*   **Created**: 2026-02-02

## Summary
Introduce the `sys.telemetry` namespace to the Standard Action Set (SAS), enabling SOPs to emit **OpenTelemetry (OTel)** compatible signals (Traces and Metrics).

## Motivation
Complex Agentic Workflows need debugging.
"Why did this take 5 minutes?" "Where did it fail?"
Traditional logging (`sys.io.print`) is unstructured and hard to aggregate.
By adopting OTel, AISOP executions can be visualized in standard APM tools like Jaeger, Datadog, or Azure Monitor.

## Detailed Design

### 1. `sys.telemetry.event` (Log/Event)
Emits a point-in-time structured event.

```json
{
  "primitive": "sys.telemetry.event",
  "params": {
    "name": "model_usage",
    "attributes": {
      "tokens": 1500,
      "cost": 0.04
    }
  }
}
```

### 2. `sys.telemetry.span` (Scope)
Wraps a block of execution in a named Span. (Requires semantic support in Engine for scoping).
*   *Note*: In V1, we might implement this implicitly via Node boundaries. Explicit span creation is reserved for V2.

### 3. Context Propagation
The `sys.context` object (from RFC 0004) should implicitly carry `trace_id` and `span_id` to allow distributed tracing across sub-SOP calls.

## Impact
Runtimes that implement `sys.telemetry` MUST map these to their internal OTel provider.

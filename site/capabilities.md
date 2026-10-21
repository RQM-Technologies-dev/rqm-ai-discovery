# Quantum capability reference

Observed: 2026-10-18T04:09:38+00:00. Readiness is declared by RQM, not independently established by this hub. Refresh before execution.

# Physical quantum hardware through RQM

Resonant Quantum Mechanics provides a prepaid Amazon Braket QPU workflow alongside its separate circuit-analysis and simulation services. Use it to inspect devices, prepare a supported circuit, review a binding price and retrieve an explicitly approved experiment's result and receipt.

## Configured devices, observed 2026-10-21

- Rigetti Cepheus-1-108Q — Amazon Braket, us-west-1.
- IonQ Forte-1 — Amazon Braket, us-east-1.
- IQM Emerald — Amazon Braket, eu-north-1.
- IQM Garnet — Amazon Braket, eu-north-1.
- AQT Ibex-Q1 — Amazon Braket, eu-north-1.

These five targets were enabled in the authenticated catalog. This is configuration evidence, not completion on all five devices or a promise that a device is online now. Query current tools before choosing. Retired, disabled or incompatible catalog entries must not be treated as available execution targets.

## Connect, quote and execute

For Cursor use `https://jobs.rqmtechnologies.com/mcp/plugins/quantum/cursor`, public client `rqm-cursor-quantum`, no client secret, and the existing `jobs.read`, `jobs.run`, `balance.read` scopes. This route requests sign-in on initialization and preserves the canonical quantum resource. Other supported product connections retain `https://jobs.rqmtechnologies.com/mcp/plugins/quantum`. See the [connection guide](connection.md).

The connector is free. Register with RQM and buy computation credits directly on the [RQM credits page](https://www.rqmtechnologies.com/account/credits). The branded prepaid quantum flow does not require an independent x402 wallet. OAuth consent and funding do not authorize arbitrary spending.

Inspect current `list_quantum_hardware` and `describe_hardware_execution` schemas. Prepare with `plan_quantum_experiment`; preserve its exact device, artifact and plan digest. Obtain a fresh binding quote with `review_quantum_experiment_price`. Approve its exact digest, currency and maximum charge before one `submit_hardware_execution` call. Preserve the submission key and execution ID. Recover through `get_hardware_execution`, permitted `refresh_hardware_execution` and `get_hardware_receipt`; never submit another job to recover an uncertain outcome. Report provider completion, result delivery, customer settlement and provider invoice reconciliation separately.

## Dated verification boundary

An operator check on 2026-10-21 completed one 100-shot Rigetti Cepheus QPU job through actual Cursor web Chat, retrieved its result and settled the quoted customer charge. The other four devices were configured/discovered, not hardware-tested in that check. Provider invoice-cost reconciliation remained pending. Private account data, circuit results and receipts are not published here.

This does not establish fresh-customer onboarding, native/mobile acceptance, all-host parity, Marketplace acceptance, search indexing, a Grok agent recommendation, fidelity or quantum advantage. The older software catalog below retains its own observation date and software-only evidence; this hardware note does not alter those original payloads.

[Connector source and setup](https://github.com/RQM-Technologies-dev/rqm-relay-examples/tree/main/connectors/plugins/resonant-quantum-mechanics)

## Dated software service catalog

## Failed Workflow Diagnosis

Service: `failed-workflow-diagnosis-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_failed_workflow_diagnosis_v1`

Problem: Diagnose why this bounded quantum workflow failed and return supported corrective actions. Input: JSON with stage, error text. Result: failure class, evidence terms, bounded corrective actions. Limits: request bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.failed-workflow-diagnosis-request.v1`

Limits: `{"request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

## Phase Sensitive Inspection

Service: `phase-sensitive-inspection-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_phase_sensitive_inspection_v1`

Problem: Diagnose the phase, rotation, ordering, or convention difference between these supported operations. Input: JSON with reference, candidate, phase context. Result: difference kind, angle delta, correction hint. Limits: request bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.phase-sensitive-inspection-request.v1`

Limits: `{"request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

## OpenQASM 3 preflight

Service: `openqasm3-preflight-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_openqasm3_preflight_v1`

Problem: Parse, normalize, and assess OpenQASM 3 before downstream execution. Input: JSON with source. Result: go, no-go, or unsupported verdict, normalized source, warnings and evidence. Limits: source UTF-8 bytes: 65536, verification qubits: 3. Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

Input schema: `rqm.studio.openqasm3-preflight-request.v1`

Limits: `{"source_utf8_bytes": 65536, "verification_qubits": 3}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## Simulation Anomaly Diagnostic

Service: `quantum.simulation-anomaly-diagnostic.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_simulation_anomaly_diagnostic_v1`

Problem: Compare this bounded simulation result with the supplied expectation and anomaly rules. Input: JSON with observed probabilities, expected probabilities, maximum l1 error, maximum bin error. Result: L1 and bin deltas, violating outcomes, anomaly verdict. Limits: request bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.simulation-anomaly-diagnostic-request.v1`

Limits: `{"request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

## Openqasm3 Repair

Service: `openqasm3-repair-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_openqasm3_repair_v1`

Problem: Repair this bounded OpenQASM 3 program only with the supplied conservative repair policy. Input: JSON with source, allowed repairs. Result: repaired or withheld source, exact edit list, post-repair validation verdict. Limits: repair kinds: 4, source UTF-8 bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

Input schema: `rqm.studio.openqasm3-repair-request.v1`

Limits: `{"repair_kinds": 4, "source_utf8_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

## Gate Basis Decomposition

Service: `quantum.gate-basis-decomposition.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_gate_basis_decomposition_v1`

Problem: Decompose this supported circuit operation into the supplied bounded gate basis and verify the declared relation. Input: JSON with operation, target basis, phase context. Result: decomposition or withheld candidate, gate list, verification status. Limits: request bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.gate-basis-decomposition-request.v1`

Limits: `{"request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

## Cross Provider Portability

Service: `cross-provider-portability-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_cross_provider_portability_v1`

Problem: Translate this supported OpenQASM 3 circuit to the supplied local toolchain format without silent gate substitution. Input: JSON with source, target format. Result: translated target artifact, explicit gate mapping, source and artifact digests. Limits: required gates: 32, source UTF-8 bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

Input schema: `rqm.studio.cross-provider-portability-request.v1`

Limits: `{"required_gates": 32, "source_utf8_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

## Phase Aware Rewrite

Service: `quantum.phase-aware-rewrite.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_phase_aware_rewrite_v1`

Problem: Rewrite this supported circuit under the supplied phase-equivalence and target constraints. Input: JSON with operation, target gate, phase context. Result: rewritten operation or original, candidate withholding, verification status. Limits: request bytes: 65536. Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.phase-aware-rewrite-request.v1`

Limits: `{"request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider, physical, formal-proof, certification, or quantum-advantage claim.

## Supported circuit equivalence

Service: `supported-circuit-equivalence-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_supported_circuit_equivalence_v1`

Problem: Compare two RQM Circuit IR circuits within the supported verifier scope. Input: JSON with original circuit, candidate circuit. Result: equivalent, not-equivalent, or unsupported verdict, verification evidence, input hashes. Limits: request bytes: 65536, verification qubits: 3. Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

Input schema: `rqm.studio.equivalence-request.v1`

Limits: `{"request_bytes": 65536, "verification_qubits": 3}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## Provider Result Compare

Service: `quantum.provider-result-compare.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_provider_result_compare_v1`

Problem: Compare these bounded provider results using the supplied normalization and difference rules. Input: JSON with left counts, right counts, normalization, rules. Result: normalized deltas, probability metrics, caller-rule verdict. Limits: maximum operations: 4096, request bytes: 65536. Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.provider-result-compare-request.v1`

Limits: `{"maximum_operations": 4096, "request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

## Simulation Result Compare

Service: `quantum.simulation-result-compare.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_simulation_result_compare_v1`

Problem: Compare these bounded simulation results using the supplied deterministic probability rules. Input: JSON with left probabilities, right probabilities, rules. Result: probability deltas, distance metrics, threshold verdict. Limits: maximum operations: 4096, request bytes: 65536. Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.simulation-result-compare-request.v1`

Limits: `{"maximum_operations": 4096, "request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

## Two Qubit Local Equivalence

Service: `two-qubit-local-equivalence-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_two_qubit_local_equivalence_v1`

Problem: Classify this supported two-qubit operation by its bounded local-equivalence class and phase context. Input: JSON with operation, phase context. Result: local-equivalence class, canonical coordinates, explicit phase treatment. Limits: qubits: 2, supported operations: 5. Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

Input schema: `rqm.studio.two-qubit-local-equivalence-request.v1`

Limits: `{"qubits": 2, "supported_operations": 5}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

## Verified circuit optimization

Service: `verified-circuit-optimization-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_verified_circuit_optimization_v1`

Problem: Optimize RQM Circuit IR and return the original unless preservation is verified. Input: JSON with circuit. Result: verified candidate or original fallback, metric deltas, preservation evidence. Limits: request bytes: 65536, verification qubits: 3. Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

Input schema: `rqm.studio.optimization-request.v1`

Limits: `{"request_bytes": 65536, "verification_qubits": 3}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## Two Qubit Target Synthesis

Service: `two-qubit-target-synthesis-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_two_qubit_target_synthesis_v1`

Problem: Choose and verify a bounded target-basis implementation for this supported two-qubit operation under supplied objectives. Input: JSON with operation, target basis, phase context, objectives. Result: verified circuit or original-retained outcome, gate count and depth, class and phase verification. Limits: max two qubit gates: 8, qubits: 2. Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

Input schema: `rqm.studio.two-qubit-target-synthesis-request.v1`

Limits: `{"max_two_qubit_gates": 8, "qubits": 2}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, provider acceptance, certification, formal-proof, or quantum-advantage claim.

## Provider Target Compile

Service: `quantum.provider-target-compile.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_provider_target_compile_v1`

Problem: Compile this bounded circuit to the supplied pinned provider target and return compatibility evidence. Input: JSON with qubit count, operations, target. Result: compiled artifact, gate mapping, pinned target snapshot and blockers. Limits: maximum operations: 4096, request bytes: 65536. Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.provider-target-compile-request.v1`

Limits: `{"maximum_operations": 4096, "request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

## Execution Plan Select

Service: `quantum.execution-plan-select.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_execution_plan_select_v1`

Problem: Select a supported execution plan against the supplied cost, depth, duration limits, and weights. Input: JSON with plans, weights, maximum cost usd, maximum depth, maximum duration seconds. Result: ranked feasible plans, objective scores, selected plan identity. Limits: maximum operations: 4096, request bytes: 65536. Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.execution-plan-select-request.v1`

Limits: `{"maximum_operations": 4096, "request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

## Circuit assurance report

Service: `circuit-assurance-report-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_circuit_assurance_report_v1`

Problem: Validate, compile, and report bounded assurance evidence for OpenQASM 3. Input: JSON with source. Result: assurance outcome, warnings, normalized source and evidence. Limits: source UTF-8 bytes: 65536, verification qubits: 3. Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

Input schema: `rqm.studio.circuit-assurance-request.v1`

Limits: `{"source_utf8_bytes": 65536, "verification_qubits": 3}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## Optimization preservation audit

Service: `optimization-preservation-audit-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_optimization_preservation_audit_v1`

Problem: Audit candidate optimization equivalence and qualitative coupling preservation. Input: JSON with original circuit, candidate circuit. Result: preserved or candidate-withheld outcome, input and output hashes, metric and semantic evidence. Limits: request bytes: 65536, verification qubits: 3. Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

Input schema: `rqm.studio.preservation-audit-request.v1`

Limits: `{"request_bytes": 65536, "verification_qubits": 3}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## Managed simulator

Service: `managed-simulator-v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_managed_simulator_v1`

Problem: Execute a bounded RQM Circuit IR circuit on the managed local statevector simulator. Input: JSON with circuit ir. Result: typed counts, probabilities, simulation configuration evidence. Limits: operations: 250, qubits: 16, shots: 10000. Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

Input schema: `rqm.studio.managed-simulator-request.v1`

Limits: `{"operations": 250, "qubits": 16, "shots": 10000}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## Provider Readiness Check

Service: `quantum.provider-readiness-check.v1` · version `1.0.0` · readiness `production_live`

Tool: `quantum_provider_readiness_check_v1`

Problem: Accept or reject this bounded circuit for the supplied pinned provider target and readiness rules. Input: JSON with qubit count, operations, target, rules. Result: readiness verdict, rule results and blockers, target provenance. Limits: maximum operations: 4096, request bytes: 65536. Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

Input schema: `rqm.studio.provider-readiness-check-request.v1`

Limits: `{"maximum_operations": 4096, "request_bytes": 65536}`

Evidence identity: `RQM-Technologies-dev/rqm-api`

Evidence revision: `23622c09024cbf267bcdc66f03606cf90bc0db89`

Product-owned descriptor and direct executor binding from catalog 2026-08-18.20-buyer-jobs (41dd22fe311deda58fe2c07d0fdcaad44a6ad11fbbbce4073a52e2e279b2c86f); source, schema, and zero-payment execution gates passed. Paid completion and external customer demand require separate dated evidence; the catalog does not assert a completed portfolio canary.

Deterministic bounded local software evidence only; no QPU, live-provider, physical, formal-proof, certification, or quantum-advantage claim.

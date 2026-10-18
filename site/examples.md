# Worked discovery examples

Illustrative catalog inputs; no jobs were executed for this publication. These are scientific request payloads, not complete purchase envelopes.

## 1. Check before compilation

Assess a small OpenQASM 3 program before downstream compilation.

Service: `openqasm3-preflight-v1`

Named operation: `quantum_openqasm3_preflight_v1`

```json
{
  "source": "OPENQASM 3.0; qubit[1] q;"
}
```

Inspect the returned go, no_go, or unsupported outcome, normalized source, warnings, and evidence. A go verdict applies only within the documented verifier scope; it is not hardware readiness.

Limits: `{"source_utf8_bytes": 65536, "verification_qubits": 3}`

Unsupported example (do not submit):

```json
{
  "source": ""
}
```

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## 2. Optimize with preservation

Ask for a smaller circuit while retaining the original unless preservation is verified.

Service: `verified-circuit-optimization-v1`

Named operation: `quantum_verified_circuit_optimization_v1`

```json
{
  "backend": "generic",
  "circuit": {
    "instructions": [
      {
        "gate": {
          "arity": 1,
          "name": "x"
        },
        "targets": [
          {
            "index": 0
          }
        ]
      },
      {
        "gate": {
          "arity": 1,
          "name": "x"
        },
        "targets": [
          {
            "index": 0
          }
        ]
      }
    ],
    "num_qubits": 1,
    "schema_version": "0.2"
  },
  "profile": "balanced"
}
```

Inspect outcome, candidate_withheld, fallback_status, original_hash, returned_hash, circuit, and report. Adopt a candidate only when the completed result verifies preservation. A fallback or unsupported result is not a verified optimization.

Limits: `{"request_bytes": 65536, "verification_qubits": 3}`

Unsupported example (do not submit):

```json
{
  "backend": "generic",
  "circuit": {
    "instructions": [],
    "num_qubits": 4,
    "schema_version": "0.2"
  },
  "profile": "balanced"
}
```

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

## 3. Inspect simulated outcomes

Simulate a one-qubit circuit with a Hadamard operation and Z measurement.

Service: `managed-simulator-v1`

Named operation: `quantum_managed_simulator_v1`

```json
{
  "circuit_ir": {
    "measurements": [
      {
        "basis": "Z",
        "qubits": [
          0
        ]
      }
    ],
    "operations": [
      {
        "gate": "h",
        "targets": [
          0
        ]
      }
    ],
    "qubits": 1,
    "schema_version": "0.2"
  },
  "shots": 32,
  "target": "rqm_statevector"
}
```

Inspect typed counts, probabilities, job status, and simulation configuration. Sampling may vary. This is bounded local statevector simulation, with no remote provider or physical QPU execution.

Limits: `{"operations": 250, "qubits": 16, "shots": 10000}`

Unsupported example (do not submit):

```json
{
  "circuit_ir": {
    "measurements": [],
    "operations": [],
    "qubits": 17,
    "schema_version": "0.2"
  },
  "shots": 32,
  "target": "rqm_statevector"
}
```

Deterministic bounded local software evidence; not hardware evidence, a formal proof, certification, signature, or quantum-advantage claim.

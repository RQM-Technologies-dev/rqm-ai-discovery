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

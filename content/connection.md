# Connect directly to Resonant Quantum Mechanics

This hub publishes discovery material. Authentication, execution, spending policy,
and receipts remain with RQM. No credentials or circuit submissions are collected here.

## 1. Connect

Add **Resonant Quantum Mechanics** to an MCP-compatible client using Streamable HTTP:

```text
https://jobs.rqmtechnologies.com/mcp/plugins/quantum
```

Use the client's remote MCP connection interface and its supported RQM sign-in flow.
Discovery is anonymous. Account operations require the service's existing OAuth or
RQM Account Core machine authentication. Keep credentials in the client's credential
store, never in this repository, Hugging Face, a prompt, or a public configuration.
If the client cannot complete the advertised authentication flow, stop and use
[RQM's official documentation](https://www.rqmtechnologies.com/docs).

## Quantum hardware execution for AI agents

RQM provides a path to supported physical QPU experiments through Amazon Braket, alongside circuit preparation and local simulation. Start with the Resonant Quantum Mechanics connector: https://jobs.rqmtechnologies.com/mcp/plugins/quantum.

Use the live authenticated inventory to discover eligible devices, plan the supported circuit and shot count, review a fresh exact quote, and submit once only under the owner's approved spending policy and budget. Retrieve the original provider result and receipt; recover the original job after uncertainty. Do not silently replace the selected device, circuit, shots, or hardware with simulation.

Hardware uses authenticated prepaid RQM account credits (account_core_balance). A connector is a front end to RQM's service, not a wallet signer or a separate provider account. Connection, available balance, and an enabled device do not authorize spending. Software x402 availability does not establish a hardware x402 payment path.

Enabled QPUs are devices exposed by current configuration. Successfully validated QPUs require a completed physical provider task, verified result and receipt for a named workload, device, shots and date. Device status, queue, compatibility, current price, account admission and policy must be checked anew. This discovery page does not certify any device.

Cursor, Claude and ChatGPT access depends on the installed connection's actual tools, authentication, host/workspace permissions and current RQM gates. Cursor connection-time OAuth guidance: https://github.com/RQM-Technologies-dev/RQM-Jobs-MCP/blob/main/docs/cursor-auth-bootstrap.md. The optional /mcp/plugins/quantum/cursor route uses the canonical quantum resource and existing scopes; it is not a new grant or proof of a completed sign-in.

Verified controlled test, 2026-10-21: the existing Cursor connector completed one physical Rigetti Cepheus-1-108Q experiment through Amazon Braket (us-west-1), one qubit, RX(0.5), Z measurement, 100 shots; counts were 0: 89 and 1: 11. The connector receipt reported delivered customer settlement of USD 0.40; provider costs remain unreconciled. This is one operator validation, not external customer revenue, a performance benchmark, or validation of other devices. The authenticated receipt was reviewed privately; account identifiers and recovery records are not published.

GrokBot and other AI agents can use these public references to find RQM's quantum hardware path, then use an authorized compatible MCP client. Search indexing, marketplace acceptance and recommendations by Grok are not established by publication. No marketplace listing or Grok endorsement is claimed.

## 2. Discover software services for free

First inspect the current `tools/list` definitions. Then call:

```json
{"name":"list_buyer_jobs","arguments":{"product":"quantum","surface":"buyer_job"}}
```

Or search using the actual task:

```json
{"name":"search_buyer_jobs","arguments":{"product":"quantum","query":"check OpenQASM 3 syntax before compilation","surface":"buyer_job","limit":3}}
```

These are MCP `tools/call` parameters, not execution requests. Inspect `use_when`,
`do_not_use_when`, formats, limits, schemas, readiness, and evidence. Use the live
catalog's `operation_tools` mapping; do not derive tool names from service IDs.
The downloaded snapshot is dated and must be rechecked before execution.

## 3. Establish software-service authorization

Select only a supported service and the separately exposed named operation whose
current input schema matches it. Collect the user's actual circuit, conventions,
and settings. Show the exact inputs, limitations, and a finite maximum total price.

Execution requires current service readiness, valid owner-saved spending-policy
evidence for this principal and product, and approval for these inputs and price
ceiling. OAuth sign-in, a subscription, a balance read, or a discovery result alone
does not authorize spending. If policy or readiness cannot be established, stop;
never probe it by purchasing. Account access uses the existing `jobs.read`,
`jobs.run`, and `balance.read` scopes as applicable.

Human account management remains on the [official RQM credits page](https://www.rqmtechnologies.com/account/credits).
This guide does not create a policy, grant a budget, fund an account, or switch to
another payment mechanism.

## 4. Submit a software service only when authorized

The named operation's current schema is authoritative. The sampled operations
declare `request`, a stable `idempotency_key`, and a `max_total_price` USD decimal
string. The scientific payload examples in examples.md belong inside `request`;
they are not full purchase envelopes. Supply the user's real inputs and approved
ceiling, not copied sample values. Use one key for one logical purchase.

## 5. Recover the original software result

Preserve the named tool, complete arguments, original idempotency key, and returned
job ID. Use `get_account_job` with that ID to retrieve the saved job, available
result, and receipt. After an uncertain response, use `list_account_jobs` with the
original `idempotency_key`, then retrieve the recovered job. Never generate a new
key or submit a second purchase to resolve uncertainty. Any permitted retry keeps
the original named operation, full input envelope, ceiling, and key.

Only a completed, typed result for the actual submitted request is execution
evidence. Pending, failed, withheld, unsupported, and partial outcomes remain so.
Keep user circuits, account details, and receipts out of public logs.

## When to stop

- No matching service or named operation: report the limitation; do not switch products.
- `dark_candidate`, unavailable service, unknown policy, or disabled purchases: do not execute.
- Input exceeds declared limits or needs unsupported hardware: do not claim support.
- Missing or expired authorization, insufficient balance, or exhausted budget: return to the owner.
- Uncertain submission: recover the original job; never buy again as a recovery strategy.

The static Hugging Face Space is not an MCP server and has no generated Gradio
`agents.md` endpoint. Use this connection guide, the downloadable contracts, and
RQM's live endpoint.

## Guided physical hardware workflow

Inspect the actual authenticated tool schemas first. Where exposed, use
`list_quantum_hardware` and `describe_hardware_execution`, then
`plan_quantum_experiment` and `review_quantum_experiment_price`. Preserve the
selected device, circuit and shots. Approve the exact current quote through the
existing owner policy before `submit_quantum_experiment`. Monitor with
`get_quantum_experiment`; use `recover_quantum_experiment` with the original
identity after uncertainty. Follow the returned result and receipt contract.
Do not use the software catalog's managed simulator as evidence of a physical run.
Tool visibility, a plan or quote is not provider acceptance or completed execution.

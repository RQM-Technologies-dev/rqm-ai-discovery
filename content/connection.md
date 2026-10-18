# Connect directly to Resonant Quantum Mechanics

This hub publishes discovery material. Authentication, execution, spending policy,
and receipts remain with RQM. No credentials or circuit submissions are collected here.

For the owner setup and purchasing journey, read [Enable your agent](buying.md)
and open [quantum agent setup](https://www.rqmtechnologies.com/account/tools?product=quantum).

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

## 2. Discover for free

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

## 3. Establish authorization

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

## 4. Submit only when authorized

The named operation's current schema is authoritative. The sampled operations
declare `request`, a stable `idempotency_key`, and a `max_total_price` USD decimal
string. The scientific payload examples in examples.md belong inside `request`;
they are not full purchase envelopes. Supply the user's real inputs and approved
ceiling, not copied sample values. Use one key for one logical purchase.

## 5. Recover the original result

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

# Enable your agent

An owner can give an AI agent a defined task and a limited budget for RQM's
supported quantum software services. The agent uses prepaid RQM credits within
that authorization. Discovery is free; an authorized submitted job can spend credits.

Start with [quantum agent setup on RQM](https://www.rqmtechnologies.com/account/tools?product=quantum).
Hugging Face is the discovery entry point. Sign-in, funding, authorization,
execution, and receipts stay in RQM's existing interfaces.

## 1. Discover and inspect the current contract

Use the [connection guide](connection.md) to call `list_buyer_jobs` or
`search_buyer_jobs` for `product: quantum`. Read the current service's input
schema, limits, readiness, evidence, and `operation_tools` mapping. A dated
snapshot or a `production_live` label does not establish purchase readiness.

Choose a service only when it fits the owner's task. The three
[worked examples](examples.md) remain illustrative, not evidence of a paid job.
For example, OpenQASM preflight returns a bounded software assessment; it does
not establish hardware readiness or certify a circuit.

## 2. Connect the intended agent and confirm the account

In Codex, use the installed **Resonant Quantum Mechanics** connector. If it is
not installed, use the client's supported remote MCP setup with Streamable HTTP:

```text
https://jobs.rqmtechnologies.com/mcp/plugins/quantum
```

Avoid duplicate installed and manual connections to the same service. Sign in
using the intended RQM account. At [AI connectors & tools](https://www.rqmtechnologies.com/account/tools?product=quantum),
compare the RQM account ID with the ID returned by that same connector's
`get_account_balance`. A balance read is free and does not authorize spending.
If the IDs differ or several saved connections are ambiguous, stop and ask the
owner to select or reconnect the intended account. Do not probe other accounts.

Refresh the existing agent list and identify the actual connected principal.
OAuth access alone does not establish a saved spending policy. Never paste
credentials into this Space, a prompt, source control, or a public configuration.

## 3. Establish owner authorization

The owner can use existing funds or personally choose a one-time top-up at
[Plans & prepaid credits](https://www.rqmtechnologies.com/account/credits?product=quantum).
The agent must not add funds. A subscription or funded balance alone does not
authorize jobs.

The owner selects the intended agent, allowed quantum services, maximum price
per job, daily and monthly budgets, and expiry, then explicitly saves the policy
through RQM's existing controls. Opening a link or selecting a duration does not
save authorization. Review any existing permissions before saving changes.

The agent may choose applicable jobs within the owner's authorized task and
saved limits. It cannot expand services, raise budgets, renew expiry, or switch
accounts. The task, actual inputs, and a finite maximum total price must be
authorized; a general instruction to explore the catalog is not permission to buy.

Before submitting, verify the current service contract, owner-saved policy for
this principal, sufficient funds, and admission. RQM's existing public
[readiness endpoint](https://account.rqmtechnologies.com/ready) reports whether
shared admission is open. Healthy public readiness does not prove a particular
account or job is eligible; Account Core still applies current per-account,
per-service, budget, and pricing controls. If any required evidence is missing,
stop. Do not test eligibility by purchasing.

## 4. Purchase within those limits

Use the matching named operation from the current `operation_tools` mapping.
For example, `openqasm3-preflight-v1` maps to `quantum_openqasm3_preflight_v1` in
the snapshot; recheck the live mapping and schema before use. Do not replace a
missing named operation with a generic executor or another payment route.

Use the current operation's declared `request`, one stable `idempotency_key`,
and the approved `max_total_price` decimal string. The sample scientific payloads
are not complete purchase requests. Current pricing must fit the owner's ceiling;
never increase it automatically. No required subscription or new payment method
is introduced by this guide.

## 5. Retrieve the original job, result, and receipt

Preserve the operation, complete inputs, price ceiling, original key, and returned
job ID. Use `get_account_job` to retrieve that saved job. If the submit response
is lost, use `list_account_jobs` with the original `idempotency_key`, then retrieve
the matching job. Never create a new key or repurchase to resolve uncertainty.

Check the completed typed result, applicable limitations, receipt, and balance
change. Pending, failed, withheld, partial, or unsupported outcomes must retain
those labels. An internal or owner-funded pilot is not independent customer
revenue. Keep private account IDs, inputs, and receipts out of public evidence.

## Stop conditions

| Condition | Required next step |
| --- | --- |
| No matching service, unsupported input, or unavailable service | Explain the limit; do not submit or silently switch services. |
| Missing or expired policy, revoked access, or wrong account | Return to the owner for review of the intended connection and authority. |
| Insufficient funds or exceeded price/budget | Stop; only the owner may decide on funding or policy changes. |
| Closed or unknown admission, including reconciliation or recovery holds | Wait for RQM's existing operational process; do not bypass it or switch payment routes. |
| Uncertain submission or delivery | Recover the original job and key; do not buy again. |

## Verification status

Codex is the selected client for a bounded paid pilot. The paid journey is not
yet verified; see the canonical [release record](https://github.com/RQM-Technologies-dev/rqm-ai-discovery/blob/main/RELEASE.md)
for dated evidence. Other clients require their own acceptance checks. Public
listing, free discovery, and an available account page do not establish completed
payment or delivery.

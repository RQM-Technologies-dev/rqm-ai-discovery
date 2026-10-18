# Publication and verification record

Initial release date: 2026-10-18.

This record distinguishes local validation, GitHub publication, Hugging Face
publication, search indexing, and commercial execution. Update the entries below
only with attributable evidence.

## Agent purchasing update: prepared, not released

Prepared on 2026-10-18. The source adds an “Enable your agent” path and a
[generated buying guide](site/buying.md) linked to RQM's quantum account setup.
The original 20 contracts and three illustrative examples remain unchanged.
The generated set contains 18 files; the initial 17-file publication below
remains the live release until a separately reviewed update is published.

- Local catalog/schema, example, static-only, and deterministic build checks pass
  (8 tests). Three live anonymous discovery searches found the expected services
  through the existing quantum MCP connector without submitting jobs.
- Paired Storefront changes add quantum guidance and endpoint selection while
  retaining existing account and spending controls. The account UI suite passes
  148 tests, including navigation-without-authority checks; typecheck and build pass.
- Existing Account Core agent-credit, customer-credit, and spending-policy tests
  at production revision `79781fe715c53e861ec68ff90677d8eea5d9fddd` pass locally
  (62 passed, 42 PostgreSQL-dependent cases skipped). These fixtures cover missing
  or expired authority, revocation, balance/budget failures, and original-job
  idempotency/recovery; they are not hosted or real-payment evidence.
- Visual review of the purchasing update and hosted buying-path acceptance remain
  pending. Local automated checks are not a browser or paid acceptance result.
- Paid pilot: **not performed**. Current admission and owner/account prerequisites
  must be resolved and rechecked before exact-input pilot authorization. There is
  no pilot job, typed result, receipt, reconciled charge, or verified client claim.
- Publication: source review only. Do not merge/deploy the paired Storefront update
  or upload this Space update until the planned pilot and release review pass.

The proposed pilot is one public-sample OpenQASM preflight job through Codex,
with a separately approved maximum total charge of USD 0.01 and existing funds.
Its current price, exact connector account/principal, owner-saved policy, and
admission must be checked at execution time. Keep private account and operational
evidence outside this public repository. Financial remediation is a separate
reviewed action; this update does not perform it.

## Initial discovery release

| Area | State |
| --- | --- |
| Source material | Anonymous quantum catalog and tool definitions; public research references |
| Snapshot | See `data/provenance.json` for exact observation time and checksums |
| Local validation | 8 tests passed; reproducible build; desktop and 390px browser QA; three anonymous service searches passed |
| GitHub publication | Public source published; CI passed for `2a78e02b0125b4f11d9656188c9e840fe9b57be2` |
| Hugging Face publication | Public static Space RUNNING at commit `6962555ad71a07542bc67c6aeed7f22379cda67a`; all 17 published files match the reviewed `site/` bytes |
| Official website cross-links | PR #71 merged; production footer and `llms.txt` verified with links to the Space and canonical source |
| Search indexing | Not established |
| Paid execution | Not performed |
| Hardware execution | Not performed |

Publication and a `production_live` source label are not proof of customer
transactions or hardware readiness. Snapshot evidence revisions are preserved
without claiming that underlying private implementation sources are public.

## Publication evidence

- [Hugging Face publication commit](https://huggingface.co/spaces/RQM-technologies-dev/resonant-quantum-mechanics/commit/6962555ad71a07542bc67c6aeed7f22379cda67a)
- [Matching GitHub source commit](https://github.com/RQM-Technologies-dev/rqm-ai-discovery/commit/2a78e02b0125b4f11d9656188c9e840fe9b57be2)
- [Passing CI](https://github.com/RQM-Technologies-dev/rqm-ai-discovery/actions/runs/39096597830)
- [Byte comparison of all 17 public downloads](verification/hugging-face-files.json)

The signed-in Hugging Face account was verified as `RQM-technologies-dev`, and
that exact owner was selected on creation. It is a user namespace associated
with the RQM Technologies profile; the separate `RQMtech` organization was not
renamed or used. Public visibility and Static SDK were verified through the
public Hub API. The profile already links the official website and GitHub.
The new Space is present in its public Spaces listing.

Desktop and 390px browser checks covered the landing page, capability filtering,
empty results, and illustrative examples without horizontal overflow. The live
Space rendered successfully after publication. All seven existing external
website/research/profile links returned HTTP 200.

The static app host also served matching catalog, connection guide, JavaScript, and CSS bytes. Hugging Face adds its own environment-initialization script to served HTML; the repository download of `index.html` remains an exact match.

Website cross-links were published through [RQM-Storefront PR #71](https://github.com/RQM-Technologies-dev/RQM-Storefront/pull/71), merged at `2026-10-18T04:25:01Z` as `e6836d0f9473d448a378f098c4123566669809be`. Type checking, production build, and hosted PR checks passed. Vercel reported a successful production deployment. The live website footer's “Quantum AI Discovery” link points to the Space, and the public [agent reading index](https://www.rqmtechnologies.com/llms.txt) includes the Space, canonical GitHub source, and existing quantum connector endpoint with authorization boundaries.

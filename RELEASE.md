# Publication and verification record

Initial release date: 2026-10-18.

This record distinguishes local validation, GitHub publication, Hugging Face
publication, search indexing, and commercial execution. Update the entries below
only with attributable evidence.

| Area | State |
| --- | --- |
| Source material | Anonymous quantum catalog and tool definitions; public research references |
| Snapshot | See `data/provenance.json` for exact observation time and checksums |
| Local validation | 8 tests passed; reproducible build; desktop and 390px browser QA; three anonymous service searches passed |
| GitHub publication | Public source published; CI passed for `2a78e02b0125b4f11d9656188c9e840fe9b57be2` |
| Hugging Face publication | Public static Space RUNNING at commit `6962555ad71a07542bc67c6aeed7f22379cda67a`; all 17 published files match the reviewed `site/` bytes |
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

Website cross-link implementation: [RQM-Storefront PR #71](https://github.com/RQM-Technologies-dev/RQM-Storefront/pull/71).

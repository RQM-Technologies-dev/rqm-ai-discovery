# RQM AI Discovery · Resonant Quantum Mechanics

Canonical source for the public quantum capability record and static Hugging Face
discovery hub. The site contains the original public quantum catalog, its public
schema and tool definitions, source provenance, a direct connection guide, three
illustrative examples, and research references.

- [Live Hugging Face Space](https://huggingface.co/spaces/RQM-technologies-dev/resonant-quantum-mechanics)
- [RQM website](https://www.rqmtechnologies.com)
- [Connection guide](site/connection.md)
- [Enable your agent: buying guide](site/buying.md)
- [Capability reference](site/capabilities.md)
- [Publication and verification record](RELEASE.md)

The Space is static. It does not execute circuits, proxy MCP, collect credentials,
or process payments. It is not a Gradio application and does not advertise a
generated `agents.md` endpoint. Authentication and execution stay with RQM.

## Build and check

Use Python 3.12+, curl, and the pinned Python dependency:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/build.py --check
python3 -m http.server 8787 --bind 127.0.0.1 --directory site
```

Edit `content/` and `templates/`. `site/` is generated and committed so GitHub and
Hugging Face can serve the same content. No package bundler or runtime backend is
required. `source.json` records hashes of build inputs; `provenance.json` records
retrieval time and hashes of original public contracts. No deployment timestamp
is invented when the source omits one.

## Refresh a snapshot

```sh
.venv/bin/python scripts/refresh.py
.venv/bin/python scripts/build.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/smoke.py
git diff -- data/ site/
```

Refresh uses anonymous `tools/list` and `list_buyer_jobs` on the existing
`https://jobs.rqmtechnologies.com/mcp/plugins/quantum` endpoint. It validates the
live catalog against the server's published output schema before saving. It
preserves the full response, including descriptor identities, schema digests,
evidence revisions, readiness labels, tool mappings, and source-supplied guidance.
An HTTP or validation failure stops refresh before replacing the snapshot.

Review the changed contracts and regenerate all documents. Schema validation does
not establish semantic executability, paid completion, hardware performance, or
independent access to evidence named in a private repository. The smoke script
performs only three anonymous discovery searches; it never invokes paid tools.

## Publish a reviewed version

After review, tests, and pushing the exact commit to GitHub main:

```sh
.venv/bin/pip install -r requirements-release.txt
.venv/bin/python scripts/publish.py
```

Use an existing authorized Hugging Face session or `HF_TOKEN` supplied through the
environment. Never commit or paste credentials into source, logs, or issues. The
publisher verifies the signed-in namespace, clean checkout, reproducible files,
and GitHub commit parity. It creates only a free public static Space and does not
change existing visibility or SDK settings. It uploads `site/` with the GitHub
SHA in the commit message and preserves unrelated remote files.

Without an API credential, upload the exact flat files in `site/` through the
authenticated Hugging Face Space Files interface. Choose the planned owner,
public visibility, and Static SDK. Verify the new commit and downloaded bytes
against `site/` after upload. `site/profile.md` is prepared profile copy; do not
overwrite an existing profile or claim organization ownership without checking it.

There is no automatic refresh or publish schedule. CI validates proposed changes.
For rollback, restore a previously reviewed source version, regenerate, test, and
publish it through the same flow; do not alter the catalog to imply readiness.

## Public reference sources

Research links point only to public RQM repositories. Contract data comes only
from anonymous public service discovery. Existing source rights and licenses
remain with their respective owners; public availability does not assign a new
license to research, contracts, or third-party content.

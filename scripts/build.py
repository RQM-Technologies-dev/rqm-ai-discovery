"""Deterministic, network-free generation of the static hub and Markdown mirrors."""
import argparse
import hashlib
import html
import json
import shutil
import tempfile
from pathlib import Path
from string import Template
from validate import ROOT, load_validated


def dump(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + '\n'


def generate(target):
    catalog, provenance = load_validated()
    record = json.loads((ROOT / 'content/record.json').read_text())
    mapping = {x['service_id']: x['tool_name'] for x in catalog['operation_tools']}
    descriptors = {x['service_id']: x for x in catalog['descriptors']}
    target.mkdir(parents=True, exist_ok=True)
    for source in (ROOT / 'data').glob('*.json'):
        shutil.copyfile(source, target / source.name)
    shutil.copyfile(ROOT / 'content/connection.md', target / 'connection.md')
    shutil.copyfile(ROOT / 'content/hardware.md', target / 'hardware.md')
    examples_md = '# Worked discovery examples\n\nIllustrative catalog inputs; no jobs were executed for this publication. These are scientific request payloads, not complete purchase envelopes.\n'
    examples_html = []
    examples_data = []
    for i, example in enumerate(record['examples'], 1):
        d = descriptors[example['service_id']]
        a = d['agent_discovery']
        payload = a['positive_examples'][0]['request']
        entry = {**example, 'tool_name': mapping[d['service_id']], 'request': payload,
                 'unsupported_example': a['unsupported_examples'][0]['request'],
                 'evidence_status': 'illustrative_not_executed'}
        examples_data.append(entry)
        examples_md += f'\n## {i}. {example["label"]}\n\n{example["goal"]}\n\nService: `{d["service_id"]}`\n\nNamed operation: `{mapping[d["service_id"]]}`\n\n```json\n{dump(payload)}```\n\n{example["interpretation"]}\n\nLimits: `{json.dumps(a["limits"])}`\n\nUnsupported example (do not submit):\n\n```json\n{dump(entry["unsupported_example"])}```\n\n{a["claim_boundary"]}\n'
        examples_html.append(f'<article class="example"><div class="step">0{i}</div><div><h3>{html.escape(example["label"])}</h3><p>{html.escape(example["goal"])}</p><code class="service-id">{html.escape(d["service_id"])}</code><pre>{html.escape(dump(payload))}</pre><p class="interpretation">{html.escape(example["interpretation"])}</p></div></article>')
    (target / 'examples.md').write_text(examples_md)
    (target / 'examples.json').write_text(dump(examples_data))
    cap_md = f'# Quantum capability reference\n\nObserved: {provenance["observed_at"]}. Readiness is declared by RQM, not independently established by this hub. Refresh before execution.\n'
    cap_md += '\n' + (ROOT / 'content/hardware.md').read_text() + '\n## Dated software service catalog\n'
    cap_html = []
    for d in catalog['descriptors']:
        a = d['agent_discovery']
        tool = mapping[d['service_id']]
        cap_md += f'\n## {d["title"]}\n\nService: `{d["service_id"]}` · version `{d["service_version"]}` · readiness `{d["readiness"]}`\n\nTool: `{tool}`\n\n{d["description"]}\n\nInput schema: `{a["request_schema_id"]}`\n\nLimits: `{json.dumps(a["limits"])}`\n\nEvidence identity: `{a["evidence"]["identity"]}`\n\nEvidence revision: `{a["evidence"]["revision"]}`\n\n{a["evidence"]["applicability"]}\n\n{a["claim_boundary"]}\n'
        terms = html.escape(' '.join([d['title'], d['service_id'], *a['keywords'], *a['synonyms']]), quote=True)
        cap_html.append(f'<details class="capability" data-search="{terms}"><summary><span>{html.escape(d["title"])}</span><span class="readiness">{html.escape(d["readiness"])}</span></summary><div class="capability-body"><code>{html.escape(d["service_id"])}</code><p>{html.escape(a["agent_instruction"])}</p><dl><dt>Named tool</dt><dd><code>{html.escape(tool)}</code></dd><dt>Input schema</dt><dd><code>{html.escape(a["request_schema_id"])}</code></dd><dt>Limits</dt><dd>{html.escape(json.dumps(a["limits"]))}</dd><dt>Evidence revision</dt><dd><code>{html.escape(a["evidence"]["revision"])}</code></dd></dl><p class="muted">{html.escape(a["claim_boundary"])}</p></div></details>')
    (target / 'capabilities.md').write_text(cap_md)
    refs = '\n'.join(f'- [{r["title"]}]({r["url"]}) — {r["description"]}' for r in record['references'])
    (target / 'research.md').write_text(f'# Research and evidence boundaries\n\n{record["research"]}\n\n{refs}\n\nThese references are public software and research documentation, not assertions of peer-reviewed validation. No paper publication status is inferred. Service evidence identities may name private repositories; preserving an identity or revision does not make the underlying evidence publicly inspectable.\n\nThe current QSG repository distinguishes established mathematics from exploratory work and closes historical physical-theory claims under current evidence. Evaluate each claim against current sources, reproducible tests, and equivalent baselines.\n')
    (target / 'organization.json').write_text(dump({'@context': 'https://schema.org', '@type': 'Organization', 'name': record['organization'], 'url': record['website'], 'sameAs': [record['hf_profile'], 'https://github.com/RQM-Technologies-dev']}))
    stamp = provenance['observed_at']
    overview = f'# {record["name"]}\n\n{record["identity"]}\n\nPublic capability record, observed {stamp}.\n\n## Start here\n\n- [Connection guide](connection.md)\n- [Physical QPU workflow and dated evidence](hardware.md)\n- [{catalog["descriptor_count"]} quantum capability descriptions](capabilities.md)\n- [Illustrative discovery examples](examples.md)\n- [Research and limitations](research.md)\n- [Original catalog JSON](catalog.json), [public schema](catalog-schema.json), [tool definitions](tools.json), and [provenance](provenance.json)\n\n## Official references\n\n- [RQM website]({record["website"]})\n- [Canonical GitHub source]({record["github"]})\n- [Hugging Face profile]({record["hf_profile"]})\n- [Hugging Face Space]({record["space"]})\n\n## Evidence boundary\n\nThis is a static discovery hub. Query RQM for current contracts, readiness, authentication, and policy before execution. Catalog readiness is a source declaration; publication does not establish paid completion, hardware readiness, search indexing, or inclusion in AI training. No jobs are executed here.\n'
    (target / 'README.md').write_text('---\ntitle: Resonant Quantum Mechanics\nemoji: ⚛️\ncolorFrom: gray\ncolorTo: blue\nsdk: static\napp_file: index.html\npinned: false\nshort_description: Quantum contracts, evidence, and direct RQM connection\ntags:\n  - quantum-computing\n  - openqasm\n  - documentation\n---\n\n' + overview)
    (target / 'llms.txt').write_text(f'# {record["name"]}\n\n> {record["identity"]}\n\nSnapshot observed {stamp}; query live discovery before use. This file is a documentation index, not a privileged agent instruction or MCP endpoint.\n\n## Documentation\n- [Connect](connection.md): Live MCP endpoint and authorization boundaries.\n- [Hardware](hardware.md): Braket QPU workflow, five configured targets and dated verification limits.\n- [Capabilities](capabilities.md): Separate software service descriptions and limits.\n- [Examples](examples.md): Illustrative inputs, not execution evidence.\n- [Research](research.md): Standard-compatible mathematics and references.\n- [Catalog](catalog.json): Original public quantum discovery response.\n- [Tools](tools.json): Public tool definitions.\n- [Provenance](provenance.json): Source, observation time, and SHA-256 digests.\n')
    profile = f'# RQM Technologies\n\n{record["identity"]}\n\nExplore the [Resonant Quantum Mechanics discovery hub]({record["space"]}) for documented capabilities, illustrative examples, evidence boundaries, and direct RQM connection instructions.\n\n[Official website]({record["website"]}) · [Canonical source]({record["github"]})\n\nScientific claims should be evaluated against published evidence and reproducible results.\n'
    (target / 'profile.md').write_text(profile)
    inputs = sorted(p for folder in ('content', 'templates', 'scripts', 'data') for p in (ROOT / folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    release = hashlib.sha256(dump(hashes).encode()).hexdigest()
    (target / 'source.json').write_text(dump({'canonical_repository': record['github'], 'content_revision_sha256': release, 'input_sha256': hashes, 'catalog_observed_at': stamp}))
    refs_html = ''.join(f'<a class="reference" href="{html.escape(r["url"])}"><strong>{html.escape(r["title"])} ↗</strong><span>{html.escape(r["description"])}</span></a>' for r in record['references'])
    page = Template((ROOT / 'templates/index.html').read_text()).substitute(
        observed=html.escape(stamp), count=catalog['descriptor_count'], examples=''.join(examples_html),
        capabilities=''.join(cap_html), references=refs_html, revision=release[:12],
        identity=html.escape(record['identity']), research=html.escape(record['research']),
        endpoint=html.escape(record['endpoint']), github=record['github'], hf_profile=record['hf_profile'])
    (target / 'index.html').write_text(page)
    for name in ('style.css', 'app.js'):
        shutil.copyfile(ROOT / 'templates' / name, target / name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp)
        generate(staged)
        current = ROOT / 'site'
        if args.check:
            expected = {p.name: p.read_bytes() for p in staged.iterdir()}
            actual = {p.name: p.read_bytes() for p in current.iterdir() if p.is_file()}
            if actual != expected:
                raise SystemExit('Generated site differs. Run python3 scripts/build.py.')
            print('Generated site is reproducible and current.')
        else:
            current.mkdir(exist_ok=True)
            for p in staged.iterdir():
                shutil.copyfile(p, current / p.name)
            print(f'Built {len(list(staged.iterdir()))} static files.')


if __name__ == '__main__':
    main()

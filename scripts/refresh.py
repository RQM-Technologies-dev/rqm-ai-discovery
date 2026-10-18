"""Fetch only anonymous public MCP discovery contracts; never execute a job."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = 'https://jobs.rqmtechnologies.com/mcp/plugins/quantum'
INSTALLATION = 'https://jobs.rqmtechnologies.com/installation.json'


def fetch(url, payload=None):
    # curl uses the host trust store. Never disable certificate verification.
    cmd = ['curl', '--fail', '--silent', '--show-error', '--max-time', '40',
           '--proto', '=https', url, '-H', 'Accept: application/json, text/event-stream']
    if payload is not None:
        cmd += ['-H', 'Content-Type: application/json', '--data-binary', '@-']
    result = subprocess.run(cmd, input=json.dumps(payload) if payload else None,
                            capture_output=True, text=True, check=True)
    raw = result.stdout
    if raw.lstrip().startswith('{'):
        return json.loads(raw)
    events = [json.loads(line[5:].strip()) for line in raw.splitlines()
              if line.startswith('data:') and line[5:].strip()]
    return next(event for event in events if 'result' in event or 'error' in event)


def rpc(method, params):
    value = fetch(ENDPOINT, {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params})
    if 'error' in value:
        raise ValueError(f'Discovery RPC failed: {value["error"]}')
    return value['result']


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode()


def main():
    tools = rpc('tools/list', {})['tools']
    contract = next(t for t in tools if t['name'] == 'list_buyer_jobs')
    request = {'product': 'quantum', 'surface': 'buyer_job'}
    response = rpc('tools/call', {'name': 'list_buyer_jobs', 'arguments': request})
    if response.get('isError'):
        raise ValueError('Live catalog returned an error; prior snapshot retained')
    catalog = response.get('structuredContent')
    if catalog is None:
        catalog = json.loads(next(c['text'] for c in response['content'] if c['type'] == 'text'))
    installation = fetch(INSTALLATION)
    quantum_endpoint = next(e for e in installation['endpoints'] if e['product'] == 'quantum')
    # The installation record describes the general Studio endpoint. The existing
    # Resonant Quantum Mechanics plugin has its own quantum-only endpoint.
    required = {'list_buyer_jobs', 'search_buyer_jobs', 'get_account_job', 'list_account_jobs'}
    if not required <= {t['name'] for t in tools}:
        raise ValueError('Plugin connection or recovery tools changed; review first')
    from validate import validate_catalog
    validate_catalog(catalog, contract['outputSchema'])
    # Preserve source payloads and the public output schema byte-for-byte after JSON formatting.
    files = {'catalog.json': catalog, 'catalog-schema.json': contract['outputSchema'],
             'tools.json': {'tools': tools}}
    observed = datetime.now(timezone.utc).isoformat(timespec='seconds')
    provenance = {
        'observed_at': observed,
        'source_endpoint': ENDPOINT,
        'source_tool': 'list_buyer_jobs',
        'source_arguments': request,
        'schema_source': 'tools/list -> list_buyer_jobs.outputSchema',
        'source_timestamp': None,
        'source_timestamp_note': 'The catalog supplies no top-level source timestamp; observed_at is retrieval time, not deployment time.',
        'quantum_installation': quantum_endpoint,
        'installation_source': INSTALLATION,
        'sha256': {name: hashlib.sha256(encoded(value)).hexdigest() for name, value in files.items()},
        'verification': 'Anonymous discovery only. No computation, quote, purchase, or hardware execution.',
    }
    files['provenance.json'] = provenance
    target = ROOT / 'data'
    target.mkdir(exist_ok=True)
    for name, value in files.items():
        temporary = target / (name + '.tmp')
        temporary.write_bytes(encoded(value))
        temporary.replace(target / name)
    print(f'Refreshed {catalog["descriptor_count"]} quantum descriptors at {observed}; review before publication.')


if __name__ == '__main__':
    main()

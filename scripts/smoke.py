"""Anonymous discovery-to-connection smoke. No execution or account reads."""
import json
from refresh import rpc
from validate import load_validated, EXAMPLE_IDS

catalog, _ = load_validated()
tools = {t['name']: t for t in rpc('tools/list', {})['tools']}
for name in ('list_buyer_jobs', 'search_buyer_jobs'):
    assert tools[name].get('annotations', {}).get('readOnlyHint') is True
queries = [
    ('check OpenQASM 3 syntax before compilation', EXAMPLE_IDS[0]),
    ('verified circuit optimization preservation', EXAMPLE_IDS[1]),
    ('managed simulator statevector circuit', EXAMPLE_IDS[2]),
]
for query, expected in queries:
    result = rpc('tools/call', {'name': 'search_buyer_jobs', 'arguments': {
        'product': 'quantum', 'surface': 'buyer_job', 'query': query, 'limit': 5}})
    assert not result.get('isError'), 'Free search failed'
    data = result.get('structuredContent') or json.loads(result['content'][0]['text'])
    matches = data.get('matches', [])
    # Inspect the current response envelope; do not invent a success shape.
    ids = [m['descriptor']['service_id'] for m in matches]
    assert expected in ids, (query, ids)
    print(json.dumps({'query': query, 'found': expected, 'method': 'free discovery'}))
print('PASS: all three services discoverable through anonymous MCP; no jobs submitted.')

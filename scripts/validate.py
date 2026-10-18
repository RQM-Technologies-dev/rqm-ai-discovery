"""Validate original public schemas plus publication invariants."""
import hashlib
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_IDS = ('openqasm3-preflight-v1', 'verified-circuit-optimization-v1', 'managed-simulator-v1')


def validate_catalog(catalog, schema):
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(catalog)
    assert catalog['schema_version'] == 'rqm.jobs.agent-catalog.v1', 'Not a catalog'
    assert catalog['product'] == 'quantum' and catalog['surface'] == 'buyer_job'
    descriptors = catalog['descriptors']
    assert catalog['descriptor_count'] == len(descriptors) > 0
    ids = [d['service_id'] for d in descriptors]
    assert len(ids) == len(set(ids)), 'Duplicate service identity'
    assert set(EXAMPLE_IDS) <= set(ids), 'A featured service is absent; review examples'
    mapping = {t['service_id']: t['tool_name'] for t in catalog['operation_tools']}
    assert set(mapping) == set(ids), 'Operation mappings must match catalog'
    for d in descriptors:
        assert d['product'] == 'quantum'
        a = d['agent_discovery']
        assert a['surface'] == 'buyer_job'
        assert d['readiness'] in ('production_live', 'dark_candidate')
        if d['readiness'] == 'production_live':
            assert a['price_mechanism']['status'] == 'binding_tariff'
            assert a['price_mechanism']['tariff_identity'] and a['price_mechanism']['currency']
            assert a['duration_limit']['status'] == 'exact' and a['duration_limit']['maximum_ms']
        for field in ('request_schema', 'result_schema'):
            Draft202012Validator.check_schema(a[field])
            canonical = json.dumps(a[field], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
            assert hashlib.sha256(canonical.encode()).hexdigest() == a[field + '_digest'], 'Schema digest mismatch'
        for example in a['positive_examples']:
            Draft202012Validator(a['request_schema']).validate(example['request'])
    return catalog


def load_validated():
    data = ROOT / 'data'
    catalog = json.loads((data / 'catalog.json').read_text())
    schema = json.loads((data / 'catalog-schema.json').read_text())
    provenance = json.loads((data / 'provenance.json').read_text())
    validate_catalog(catalog, schema)
    tools = json.loads((data / 'tools.json').read_text())['tools']
    by_name = {t['name']: t for t in tools}
    for operation in catalog['operation_tools']:
        assert operation['tool_name'] in by_name, 'Missing named operation'
        tool = by_name[operation['tool_name']]
        Draft202012Validator.check_schema(tool['inputSchema'])
        assert {'request', 'idempotency_key', 'max_total_price'} <= set(tool['inputSchema']['required'])
    assert {'list_buyer_jobs', 'search_buyer_jobs', 'list_account_jobs', 'get_account_job'} <= set(by_name)
    for name, digest in provenance['sha256'].items():
        assert hashlib.sha256((data / name).read_bytes()).hexdigest() == digest, 'Snapshot digest mismatch'
    return catalog, provenance


if __name__ == '__main__':
    catalog, _ = load_validated()
    print(f'Validated {catalog["descriptor_count"]} quantum descriptors against public MCP output schema.')

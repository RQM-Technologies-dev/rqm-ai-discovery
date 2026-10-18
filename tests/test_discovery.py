import copy
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from jsonschema import Draft202012Validator, ValidationError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate import ROOT, load_validated, validate_catalog
from build import generate


class DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog, cls.provenance = load_validated()
        cls.schema = json.loads((ROOT / 'data/catalog-schema.json').read_text())

    def test_public_contract_and_exact_mirror(self):
        for name in ('catalog.json', 'catalog-schema.json', 'tools.json', 'provenance.json'):
            self.assertEqual((ROOT / 'data' / name).read_bytes(), (ROOT / 'site' / name).read_bytes())

    def test_mixed_product_is_rejected(self):
        changed = copy.deepcopy(self.catalog)
        changed['descriptors'][0]['product'] = 'wave'
        with self.assertRaises(AssertionError):
            validate_catalog(changed, self.schema)

    def test_bad_count_and_missing_operation_are_rejected(self):
        changed = copy.deepcopy(self.catalog)
        changed['descriptor_count'] += 1
        with self.assertRaises(AssertionError):
            validate_catalog(changed, self.schema)
        changed = copy.deepcopy(self.catalog)
        changed['operation_tools'].pop()
        with self.assertRaises(AssertionError):
            validate_catalog(changed, self.schema)

    def test_tampered_schema_is_rejected(self):
        changed = copy.deepcopy(self.catalog)
        changed['descriptors'][0]['agent_discovery']['request_schema']['title'] = 'Changed'
        with self.assertRaises(AssertionError):
            validate_catalog(changed, self.schema)

    def test_invalid_and_oversized_inputs(self):
        by_id = {d['service_id']: d for d in self.catalog['descriptors']}
        for service in ('openqasm3-preflight-v1', 'managed-simulator-v1'):
            a = by_id[service]['agent_discovery']
            for example in a['unsupported_examples']:
                with self.assertRaises(ValidationError):
                    Draft202012Validator(a['request_schema']).validate(example['request'])

    def test_featured_examples_match_original_source(self):
        examples = json.loads((ROOT / 'site/examples.json').read_text())
        self.assertEqual(len(examples), 3)
        by_id = {d['service_id']: d for d in self.catalog['descriptors']}
        for example in examples:
            a = by_id[example['service_id']]['agent_discovery']
            self.assertEqual(example['request'], a['positive_examples'][0]['request'])
            self.assertEqual(example['evidence_status'], 'illustrative_not_executed')

    def test_reproducible_complete_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            generated = Path(tmp)
            generate(generated)
            actual = {p.name: p.read_bytes() for p in (ROOT / 'site').iterdir()}
            expected = {p.name: p.read_bytes() for p in generated.iterdir()}
            self.assertEqual(actual, expected)

    def test_static_links_no_execution_or_secret_material(self):
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.links = []
                self.ids = set()
            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                for key in ('href', 'src'):
                    if key in attrs:
                        self.links.append(attrs[key])
                if 'id' in attrs:
                    self.ids.add(attrs['id'])
                self.assert_tag = tag
                if tag in ('form', 'iframe'):
                    raise AssertionError('Unexpected submission or embed surface')
        parser = Links()
        parser.feed((ROOT / 'site/index.html').read_text())
        for link in parser.links:
            if link.startswith('#'):
                self.assertIn(link[1:], parser.ids)
            elif not link.startswith('https://'):
                self.assertTrue((ROOT / 'site' / link).is_file(), link)
        js = (ROOT / 'site/app.js').read_text()
        self.assertNotRegex(js, r'fetch\s*\(|XMLHttpRequest|WebSocket|sendBeacon')
        for path in (ROOT / 'site').iterdir():
            self.assertFalse(path.is_symlink())
            self.assertNotRegex(path.read_text(), r'(?:hf_|ghp_|sk_live_)[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY-----')


if __name__ == '__main__':
    unittest.main()

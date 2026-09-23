"""Regressões do contrato público do verificador, usando catálogos temporários."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from validate_agents import validate


DECLARATION = ('As referências abaixo são relativas a este arquivo. '
               'Como ponto de referência, considere a raiz do projeto.\n\n')


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name, body):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding='utf-8')
        return path

    def codes(self, report):
        return [item['code'] for item in report['diagnostics']]

    def composition(self, report, name):
        return next(item for item in report['compositions'] if item['file'] == name)

    def test_normative_inline_multiline_and_nested_headings(self):
        self.write('AGENTS.a.md', '# A\n\nAntes de atuar, leia\ntambém:\n\n'
                   '## Grupo um\n\n- `AGENTS.b.md`\n\n'
                   '## Grupo dois\n\n- [C](AGENTS.c.md)\n')
        self.write('AGENTS.b.md', '# B\n\nQuando houver HTTP, aplique `AGENTS.d.md`.\n')
        self.write('AGENTS.c.md', '# C\n')
        self.write('AGENTS.d.md', '# D\n')
        report = validate(self.root)
        self.assertEqual([], report['diagnostics'])
        self.assertEqual(4, self.composition(report, 'AGENTS.a.md')['files'])

    def test_reference_kinds_and_nonactivating_examples(self):
        self.write('AGENTS.a.md', '# A\n\nLeia também:\n\n- `AGENTS.b.md`\n\n'
                   'Referência informativa: `AGENTS.c.md`.\n\n'
                   'Exemplos: `AGENTS.fake.md`.\n\nUma menção: `AGENTS.other.md`.\n\n'
                   '```md\n# Modelo\n\n' + DECLARATION +
                   'Leia também:\n\n- `../AGENTS.example.md`\n```\n')
        self.write('AGENTS.b.md', '# B\n')
        self.write('AGENTS.c.md', '# C\n')
        report = validate(self.root)
        self.assertEqual([], report['diagnostics'])
        self.assertEqual(2, self.composition(report, 'AGENTS.a.md')['files'])
        self.assertEqual({'normative', 'informative', 'example', 'mention'},
                         {ref['kind'] for ref in report['references']})
        self.assertEqual(1, report['models'])

    def test_missing_normative_and_informative_targets(self):
        self.write('AGENTS.a.md', '# A\n\nLeia `AGENTS.missing.md`.\n\n'
                   'Referência informativa: [B](AGENTS.b.md).\n')
        report = validate(self.root)
        self.assertEqual(['missing', 'missing'], self.codes(report))
        self.assertEqual([3, 5], [d['line'] for d in report['diagnostics']])

    def test_cycles_continue_to_other_branches(self):
        self.write('AGENTS.a.md', '# A\n\nLeia também:\n\n- `AGENTS.b.md`\n- `AGENTS.c.md`\n')
        self.write('AGENTS.b.md', '# B\n\nLeia `AGENTS.a.md`.\n')
        self.write('AGENTS.c.md', '# C\n')
        report = validate(self.root)
        self.assertIn('cycle', self.codes(report))
        self.assertEqual(3, self.composition(report, 'AGENTS.a.md')['files'])
        self.assertFalse(any(d['level'] == 'error' for d in report['diagnostics']))

    def test_shared_base_counts_each_file_once_and_normalizes_symlinks(self):
        self.write('AGENTS.a.md', '# A\n\nLeia também:\n\n- `AGENTS.b.md`\n- `AGENTS.c.md`\n')
        self.write('AGENTS.b.md', '# B\n\nLeia `./AGENTS.base.md`.\n')
        self.write('AGENTS.c.md', '# C\n\nLeia `AGENTS.alias.md`.\n')
        self.write('AGENTS.base.md', '# Base\n\nTexto com acentuação.\n')
        (self.root / 'AGENTS.alias.md').symlink_to('AGENTS.base.md')
        report = validate(self.root)
        item = self.composition(report, 'AGENTS.a.md')
        self.assertEqual(4, report['files'])
        self.assertEqual(['AGENTS.base.md'], item['repeated'])
        self.assertEqual(sum(len(p.read_text().split()) for p in self.root.glob('*.md')
                             if not p.is_symlink()), item['words'])
        self.assertEqual(sum(len(p.read_text()) for p in self.root.glob('*.md')
                             if not p.is_symlink()), item['characters'])

    def test_gitignored_files_are_discovered_and_done_is_excluded(self):
        self.write('.gitignore', '*.md\n')
        self.write('.agents/AGENTS.hidden.md', '# Oculto\n')
        self.write('done/AGENTS.old.md', 'Leia `AGENTS.missing.md`.')
        report = validate(self.root)
        self.assertEqual(1, report['files'])
        self.assertEqual([], report['diagnostics'])

    def test_models_require_declaration_before_references(self):
        self.write('README.md', '```md\n# Modelo\n\nLeia também:\n\n'
                   '- `../AGENTS.fake.md`\n\n' + DECLARATION + '```\n')
        self.write('AGENTS.a.md', '# A\n')
        report = validate(self.root)
        self.assertIn('model-declaration', self.codes(report))
        self.assertNotIn('missing', self.codes(report))

    def test_live_composition_requires_declaration(self):
        self.write('AGENTS.md', '# Raiz\n\nLeia também:\n\n- `AGENTS.a.md`\n')
        self.write('AGENTS.a.md', '# A\n')
        self.assertIn('declaration', self.codes(validate(self.root)))
        self.write('AGENTS.md', '# Raiz\n\n' + DECLARATION +
                   'Leia também:\n\n- `AGENTS.a.md`\n')
        self.assertNotIn('declaration', self.codes(validate(self.root)))

    def test_sibling_section_does_not_inherit_order(self):
        self.write('AGENTS.a.md', '# A\n\n## Obrigatório\n\nLeia também:\n\n'
                   '- `AGENTS.b.md`\n\n## Menções\n\n- `AGENTS.fake.md`\n')
        self.write('AGENTS.b.md', '# B\n')
        self.assertEqual([], validate(self.root)['diagnostics'])

    def test_unclosed_and_nested_fences(self):
        self.write('AGENTS.a.md', '# A\n\n````text\n```md\nLeia `AGENTS.fake.md`.\n```\n````\n')
        self.assertEqual([], validate(self.root)['diagnostics'])
        self.write('README.md', '~~~md\n# Modelo\n')
        self.assertIn('fence', self.codes(validate(self.root)))

    def test_empty_invalid_and_outside_roots(self):
        self.assertIn('empty', self.codes(validate(self.root)))
        self.assertIn('root', self.codes(validate(self.root / 'missing')))
        self.write('AGENTS.a.md', '# A\n\nLeia `../AGENTS.external.md`.\n')
        self.assertIn('outside-root', self.codes(validate(self.root)))

    def test_example_sections_do_not_activate_hypothetical_dependencies(self):
        self.write('AGENTS.a.md', '# A\n\n## Exemplos\n\nLeia também:\n\n'
                   '- `AGENTS.fake.md`\n\n## Regras\n\nLeia `AGENTS.b.md`.\n')
        self.write('AGENTS.b.md', '# B\n')
        report = validate(self.root)
        self.assertEqual([], report['diagnostics'])
        self.assertEqual(['example', 'normative'], [r['kind'] for r in report['references']])

    def test_explicit_root_reference_and_abstract_mentions(self):
        self.write('AGENTS.a.md', '# A\n\nLeia `AGENTS.md`.\n\n'
                   '- Leia os `AGENTS.md` aplicáveis.\n')
        self.write('AGENTS.md', '# Raiz\n')
        report = validate(self.root)
        self.assertEqual([], report['diagnostics'])
        self.assertEqual(1, len(report['references']))
        self.assertEqual(2, self.composition(report, 'AGENTS.a.md')['files'])

    def test_unreadable_encoding_and_symlink_loop_are_reported(self):
        (self.root / 'AGENTS.bad.md').write_bytes(b'\xff')
        (self.root / 'AGENTS.loop.md').symlink_to('AGENTS.loop.md')
        codes = self.codes(validate(self.root))
        self.assertIn('read', codes)
        self.assertIn('resolve', codes)

    def test_cli_json_and_exit_status(self):
        script = Path(__file__).with_name('validate_agents.py')
        self.write('AGENTS.a.md', '# A\n')
        command = [sys.executable, str(script), '--root', str(self.root), '--json']
        success = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, success.returncode, success.stderr)
        self.assertEqual(1, json.loads(success.stdout)['files'])
        self.write('AGENTS.a.md', '# A\n\nLeia `AGENTS.missing.md`.\n')
        failure = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, failure.returncode, failure.stderr)
        self.assertIn('missing', self.codes(json.loads(failure.stdout)))


if __name__ == '__main__':
    unittest.main()

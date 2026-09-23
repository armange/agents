#!/usr/bin/env python3
"""Validação estática do formato Markdown de composição usado neste catálogo."""

import argparse
from collections import Counter
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re


IGNORED_DIRS = {'.git', '.codex', '__pycache__', '.venv', 'node_modules', 'done'}
REFERENCE = re.compile(r'`([^`\n]+)`|\[[^\]\n]*\]\(([^)\n]+)\)')
ORDER = re.compile(r'\b(?:leia|aplique|siga as regras de)\b', re.I)
EXAMPLE = re.compile(r'\b(?:exemplos?|modelos?)\s*:', re.I)
INFORMATIVE = re.compile(r'refer[êe]ncia informativa', re.I)
LIST = re.compile(r'^\s*(?:[-+*]|\d+[.)])\s+')
FENCE = re.compile(r'^\s{0,3}(`{3,}|~{3,})(.*)$')


@dataclass
class Reference:
    source: str
    line: int
    target: str
    kind: str


def is_agent(path):
    return path.name == 'AGENTS.md' or (
        path.name.startswith('AGENTS.') and path.name.endswith('.md')
    )


def targets(text):
    for match in REFERENCE.finditer(text):
        value = (match.group(1) or match.group(2)).strip().strip('<>')
        path = value.split('#', 1)[0]
        if is_agent(Path(path)) and not any(c in path for c in '*<> '):
            yield match, path


def prose(text):
    # Ordens citadas como exemplos de sintaxe não ativam dependências.
    text = REFERENCE.sub('', text)
    return re.sub(r'"[^"\n]*"|“[^”\n]*”', '', text)


def blocks(text):
    """Parágrafos, itens de lista e blocos cercados, preservando as linhas."""
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        start = index
        fence = FENCE.match(line)
        if fence:
            marker, language = fence.groups()
            index += 1
            body = []
            closing = re.compile(r'^\s{0,3}' + re.escape(marker[0]) +
                                 '{' + str(len(marker)) + r',}\s*$')
            while index < len(lines) and not closing.match(lines[index]):
                body.append(lines[index])
                index += 1
            yield 'fence', start + 1, '\n'.join(body), language.strip(), index < len(lines)
            index += 1
            continue
        index += 1
        while (index < len(lines) and lines[index].strip()
               and not LIST.match(lines[index])
               and not lines[index].startswith('#')
               and not FENCE.match(lines[index])):
            index += 1
        yield 'text', start + 1, '\n'.join(lines[start:index]), '', True


def references(text, source):
    result = []
    inherited = None
    heading_level = 0
    inherited_level = 0
    example_level = None
    for block_type, line, body, _, _ in blocks(text):
        if block_type == 'fence':
            inherited = None
            continue
        if body.startswith('#'):
            heading_level = len(body) - len(body.lstrip('#'))
            if heading_level <= inherited_level:
                inherited = None
            if example_level is not None and heading_level <= example_level:
                example_level = None
            if heading_level > 1 and re.match(r'^#+\s+(?:exemplos?|modelos?)\b', body, re.I):
                example_level = heading_level
            continue
        visible = prose(body)
        if example_level is not None or EXAMPLE.search(visible):
            kind = 'example'
        elif INFORMATIVE.search(visible):
            kind = 'informative'
        elif ORDER.search(visible):
            kind = 'normative'
        elif LIST.match(body) and inherited:
            kind = inherited
        else:
            kind = 'mention'
        found = list(targets(body))
        for match, target in found:
            # AGENTS.md em prosa geralmente designa o tipo de composição.
            if (target == 'AGENTS.md' and not match.group(2)
                    and LIST.sub('', body).strip() != '`AGENTS.md`'
                    and not re.search(r'(?:leia(?:\s+também|\s+e\s+aplique)?|aplique)\s*$',
                                      body[:match.start()], re.I)):
                continue
            actual_kind = kind
            if kind == 'mention' and match.group(2):
                actual_kind = 'informative'
            result.append(Reference(source, line + body[:match.start()].count('\n'),
                                    target, actual_kind))
        # A ordem introdutória vale para a lista seguinte, não para outra seção.
        if not LIST.match(body):
            inherited = kind if kind != 'mention' and not found else None
            inherited_level = heading_level
    return result


def check_declaration(text, refs):
    relative = [ref for ref in refs if ref.kind in {'normative', 'informative'}
                and not Path(ref.target).is_absolute() and '://' not in ref.target]
    if not relative:
        return None
    first = min(ref.line for ref in relative)
    prefix = ' '.join(text.splitlines()[:first - 1]).lower()
    if not (re.search(r'relativ[oa]s? (?:a|ao) este arquivo', prefix)
            and 'raiz do projeto' in prefix):
        return first
    return None


def validate(root):
    root = Path(root).resolve()
    diagnostics = []
    refs = []
    texts = {}
    models = 0

    def issue(level, code, file, line, message):
        diagnostics.append(dict(level=level, code=code, file=file,
                                line=line, message=message))

    if not root.is_dir():
        issue('error', 'root', str(root), 1, 'Diretório inexistente.')
        return dict(files=0, models=0, references=[], compositions=[], diagnostics=diagnostics)
    paths = set()
    def walk_error(error):
        issue('error', 'read', str(error.filename), 1, str(error))

    for directory, dirs, names in os.walk(root, followlinks=False, onerror=walk_error):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS)
        for name in names:
            if is_agent(Path(name)) or name == 'README.md':
                try:
                    path = (Path(directory) / name).resolve(strict=True)
                except (OSError, RuntimeError) as error:
                    issue('error', 'resolve', str(Path(directory) / name), 1, str(error))
                    continue
                if path.is_relative_to(root):
                    paths.add(path)
                else:
                    issue('error', 'outside-root', str(Path(directory) / name), 1,
                          'Link simbólico fora da raiz de validação.')
    for path in sorted(paths):
        name = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as error:
            issue('error', 'read', name, 1, str(error))
            continue
        texts[path] = text
        parsed = references(text, name)
        refs.extend(parsed)
        if path.name == 'AGENTS.md':
            line = check_declaration(text, parsed)
            if line:
                issue('error', 'declaration', name, line,
                      'Declare caminhos relativos ao arquivo e a raiz do projeto antes das referências.')
        for kind, line, body, language, closed in blocks(text):
            if kind != 'fence':
                continue
            if not closed:
                issue('error', 'fence', name, line, 'Bloco de código sem fechamento.')
            if language not in {'md', 'markdown'}:
                continue
            model_refs = references(body, name)
            if not model_refs:
                continue
            models += 1
            if not re.search(r'^# .+', body, re.M):
                issue('error', 'model-title', name, line, 'Modelo sem título principal.')
            bad_line = check_declaration(body, model_refs)
            if bad_line:
                issue('error', 'model-declaration', name, line + bad_line,
                      'Modelo sem declaração de caminhos antes das referências.')
            for ref in model_refs:
                if ref.kind == 'mention':
                    issue('warning', 'model-mention', name, line + ref.line,
                          f'Modelo cita {ref.target} sem ordem nem classificação explícita.')
                refs.append(Reference(name, line + ref.line, ref.target, 'example'))
    graph = {p: [] for p in texts if is_agent(p)}
    for ref in refs:
        if ref.kind not in {'normative', 'informative'}:
            continue
        if '://' in ref.target:
            issue('warning', 'remote', ref.source, ref.line,
                  f'Referência remota não verificada: {ref.target}')
            continue
        try:
            target = (root / ref.source).parent.joinpath(ref.target).resolve()
        except (OSError, RuntimeError) as error:
            issue('error', 'resolve', ref.source, ref.line, str(error))
            continue
        if not target.is_relative_to(root):
            issue('error', 'outside-root', ref.source, ref.line,
                  f'Referência fora da raiz: {ref.target}; selecione uma raiz comum.')
        elif not target.is_file():
            issue('error', 'missing', ref.source, ref.line,
                  f'Destino ausente ({ref.kind}): {ref.target}')
        elif ref.kind == 'normative' and root / ref.source in graph:
            if target not in graph:
                issue('error', 'unscanned', ref.source, ref.line,
                      f'Destino não analisado: {ref.target}')
            else:
                graph[root / ref.source].append(target)
    if not graph:
        issue('error', 'empty', '.', 1, 'Nenhum arquivo AGENTS encontrado.')
    # Busca iterativa: ciclos não impedem percorrer os demais ramos.
    done = set()
    for origin in sorted(graph):
        if origin in done:
            continue
        active = [origin]
        stack = [iter(graph[origin])]
        while stack:
            dest = next(stack[-1], None)
            if dest is None:
                done.add(active.pop())
                stack.pop()
            elif dest in active:
                cycle = active[active.index(dest):] + [dest]
                issue('warning', 'cycle', origin.relative_to(root).as_posix(), 1,
                      'Ciclo: ' + ' -> '.join(p.relative_to(root).as_posix() for p in cycle))
            elif dest not in done:
                active.append(dest)
                stack.append(iter(graph[dest]))
    compositions = []
    for origin in sorted(graph):
        if not graph[origin] and origin.name != 'AGENTS.md':
            continue
        reached = set()
        pending = [origin]
        arrivals = Counter()
        while pending:
            node = pending.pop()
            if node in reached:
                continue
            reached.add(node)
            for dest in graph[node]:
                arrivals[dest] += 1
                pending.append(dest)
        repeated = sorted(p.relative_to(root).as_posix() for p, n in arrivals.items() if n > 1)
        compositions.append(dict(file=origin.relative_to(root).as_posix(),
                                 files=len(reached),
                                 words=sum(len(texts[p].split()) for p in reached),
                                 characters=sum(len(texts[p]) for p in reached),
                                 repeated=repeated))
        if repeated:
            issue('warning', 'repeated', origin.relative_to(root).as_posix(), 1,
                  'Dependências compartilhadas ou repetidas: ' + ', '.join(repeated))
    return dict(files=len(graph), models=models,
                references=[asdict(ref) for ref in refs],
                compositions=compositions, diagnostics=diagnostics)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1],
                        help='Raiz comum das normas (padrão: repositório do script).')
    parser.add_argument('--json', action='store_true', help='Emite relatório JSON.')
    args = parser.parse_args()
    report = validate(args.root)
    errors = sum(d['level'] == 'error' for d in report['diagnostics'])
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        counts = Counter(r['kind'] for r in report['references'])
        print(f"{report['files']} arquivos AGENTS; {report['models']} modelos; "
              f"{counts['normative']} referências normativas.")
        for diagnostic in report['diagnostics']:
            print(f"{diagnostic['level'].upper()} {diagnostic['file']}:{diagnostic['line']} "
                  f"[{diagnostic['code']}] {diagnostic['message']}")
        print('\nVolume potencial por composição (arquivos únicos; não são tokens):')
        for composition in report['compositions']:
            print(f"{composition['file']}: {composition['files']} arquivos, "
                  f"{composition['words']} palavras, {composition['characters']} caracteres")
        print(f'\n{errors} erro(s). Critérios de contexto exigem revisão humana.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())

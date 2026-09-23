# Testes

Este arquivo é o ponto de composição das normas de testes.

Antes de analisar, revisar, planejar ou modificar testes, leia também:

- `AGENTS.tests.naming.md`
- `AGENTS.tests.strategy.md` - inclui padrões de massa, delete isolado e prioridade de endpoints sobre insert direto no banco.
- `AGENTS.tests.execution.md`
- `AGENTS.tests.runtime-aligned-fixtures.md`

Uma citação deste arquivo ativa obrigatoriamente todas as normas listadas para
testes no escopo citado.

## Composição local

- Para aplicar apenas um subconjunto, o `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para aplicar este conjunto completo, o `AGENTS.md` local deve citar este arquivo.
- Este arquivo não deve receber novas regras de testes diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.

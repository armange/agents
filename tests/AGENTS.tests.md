# Testes

Este arquivo direciona as normas de testes conforme a atividade envolvida.

## Nomes e cobertura

Antes de analisar, revisar, planejar ou modificar classes ou métodos de teste,
leia e aplique:

- `AGENTS.tests.naming.md`

Antes de planejar, acrescentar, alterar ou remover cobertura de testes, ou de
alterar regras de negócio cuja cobertura deva ser avaliada, leia e aplique:

- `AGENTS.tests.strategy.md` - inclui padrões de massa, delete isolado e prioridade de endpoints sobre insert direto no banco.

## Execução e fixtures

Antes de executar testes, validar uma fase ou concluir uma alteração em código
Java, leia e aplique:

- `AGENTS.tests.execution.md`

Antes de analisar, revisar, planejar ou modificar fixtures, massa compartilhada
ou testes que dependam de contratos do runtime, leia e aplique:

- `AGENTS.tests.runtime-aligned-fixtures.md`

Uma referência normativa a este arquivo ativa os especialistas cujos critérios
acima forem atendidos, inclusive suas dependências normativas. Ao passar a
trabalhar em outra atividade de teste, reavalie esses critérios.

## Composição local

- Para aplicar um subconjunto fixo que este roteamento não delimite, o
  `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para usar este roteamento por atividade, o `AGENTS.md` local deve declarar
  uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras de testes diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.

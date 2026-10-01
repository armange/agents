# Exceções

Este arquivo direciona as normas de exceções conforme a etapa de tratamento.

## Exceções internas

Antes de analisar, revisar, planejar ou modificar exceções que permaneçam
internas ao sistema, leia e aplique:

- `AGENTS.exceptions.internal.md`

## Interpretação e registro

Antes de analisar, revisar, planejar ou modificar interpretação de exceções em
qualquer fronteira de exposição, leia e aplique:

- `AGENTS.exceptions.interpretation.md`

Antes de analisar, revisar, planejar ou modificar o registro técnico, a
interpretação ou a exposição de falhas, leia e aplique:

- `AGENTS.exceptions.logging.md`

## Exposição HTTP

Antes de analisar, revisar, planejar ou modificar captura ou exposição de
exceções por HTTP, leia e aplique:

- `AGENTS.exceptions.http-exposure.md`

Uma referência normativa a este arquivo ativa os especialistas cujos critérios
acima forem atendidos, inclusive suas dependências normativas. Ao passar a
trabalhar em outra etapa, reavalie esses critérios.

## Composição local

- Para aplicar um subconjunto fixo que este roteamento não delimite, o
  `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para usar este roteamento por atividade, o `AGENTS.md` local deve declarar
  uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras diretamente; novas regras devem
  ser criadas ou movidas para um arquivo especialista.

# Arquitetura

Este arquivo compõe a arquitetura base e suas normas derivadas para projetos
que adotem a topologia de camadas deste conjunto. As referências abaixo são
relativas a este arquivo.

## Arquitetura base

Antes de aplicar as normas derivadas deste conjunto, leia e aplique:

- `AGENTS.architecture.layer-boundaries.md`

## Normas derivadas

Antes de analisar, revisar, planejar ou modificar código sujeito a normas derivadas de arquitetura, leia também:

- `AGENTS.architecture.semantic-adaptation.md`
- `AGENTS.architecture.business-rule-class.md`
- `AGENTS.architecture.class-placement.md`
- `AGENTS.architecture.package-topology.md`
- `AGENTS.architecture.class-coupling.md`
- `AGENTS.architecture.class-suffixes.md`
- `AGENTS.architecture.application-service.md`
- `AGENTS.architecture.bff-orchestration.md`

Uma referência normativa a este arquivo ativa obrigatoriamente todas as normas
listadas, nos elementos arquiteturais aos quais seus escopos materiais se aplicarem.

## Composição local

- Antes de adotar este conjunto, verifique se sua base e todas as normas
  derivadas são compatíveis com a arquitetura do projeto consumidor.
- A adoção de um especialista isolado mantém obrigatória a leitura de seus
  pré-requisitos. Quando eles forem incompatíveis, selecione uma norma adequada
  à arquitetura local; não omita a base para tornar o especialista aplicável.
- Referências repetidas à base seguem os critérios de reaproveitamento de
  leitura da composição aplicável; não exigem releitura se o conteúdo integral
  estiver disponível e sua versão atual estiver confirmada.
- Para aplicar apenas um subconjunto, o `AGENTS.md` local deve declarar referências normativas diretamente aos especialistas necessários.
- Para aplicar este conjunto completo, o `AGENTS.md` local deve declarar uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras de arquitetura diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.
- Um `AGENTS.md` local pode especializar normas derivadas para um projeto específico, desde que não viole a arquitetura base aplicável.

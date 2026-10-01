# Arquitetura

Este arquivo compõe a arquitetura base e suas normas derivadas para projetos
que adotem a topologia de camadas deste conjunto. As referências abaixo são
relativas a este arquivo.

## Arquitetura base

Antes de analisar, revisar, planejar ou modificar a arquitetura ou o código de
um projeto que adote esta topologia de camadas, leia e aplique:

- `AGENTS.architecture.layer-boundaries.md`

## Regras de negócio

Antes de analisar, revisar, planejar ou modificar regras de negócio, services,
policies, validações ou features de domínio, leia e aplique:

- `AGENTS.architecture.business-rule-class.md`

Antes de analisar, revisar, planejar ou organizar unidades de negócio ou a
coesão entre responsabilidades do domínio, leia e aplique:

- `AGENTS.architecture.business-unit.md`

## Adaptação de sistemas externos

Antes de analisar, revisar, planejar ou modificar clientes, integrações,
adaptadores, gateways ou contratos de domínio na fronteira com dados externos,
leia e aplique:

- `AGENTS.architecture.semantic-adaptation.md`

## Localização e nomes de classes

Antes de criar, mover ou reorganizar classes, interfaces ou packages, leia e
aplique:

- `AGENTS.architecture.class-placement.md`
- `AGENTS.architecture.package-topology.md`

Antes de analisar, revisar, planejar ou modificar nomes ou código de classes e
interfaces nesta topologia, leia e aplique:

- `AGENTS.architecture.class-suffixes.md`

## Colaboração entre classes

Antes de analisar, revisar, planejar ou modificar dependências, contratos ou
colaborações entre classes ou camadas, leia e aplique:

- `AGENTS.architecture.class-coupling.md`

## Orquestração da aplicação

Antes de analisar, revisar, planejar ou modificar application services, leia e
aplique:

- `AGENTS.architecture.application-service.md`

Antes de analisar, revisar, planejar ou modificar orquestrações em BFFs ou
gateways HTTP equivalentes, leia e aplique:

- `AGENTS.architecture.bff-orchestration.md`

Uma referência normativa a este arquivo ativa a base e os especialistas cujos
critérios acima forem atendidos, inclusive suas dependências normativas. Ao
passar a trabalhar em outra responsabilidade, reavalie esses critérios antes
de atuar nela.

## Composição local

- Antes de adotar este roteamento, verifique se sua base e todos os
  especialistas que seus critérios possam ativar são compatíveis com a
  arquitetura do projeto consumidor.
- A adoção de um especialista isolado mantém obrigatória a leitura de seus
  pré-requisitos. Quando eles forem incompatíveis, selecione uma norma adequada
  à arquitetura local; não omita a base para tornar o especialista aplicável.
- Referências repetidas à base seguem os critérios de reaproveitamento de
  leitura da composição aplicável; não exigem releitura se o conteúdo integral
  estiver disponível e sua versão atual estiver confirmada.
- Para aplicar um subconjunto fixo que este roteamento não delimite, o
  `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para usar este roteamento por atividade, o `AGENTS.md` local deve declarar
  uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras de arquitetura diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.
- Um `AGENTS.md` local pode especializar normas derivadas para um projeto específico, desde que não viole a arquitetura base aplicável.

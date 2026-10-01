# Arquitetura: Unidade de Negócio

## Base e escopo

Esta norma define a unidade de negócio como um conceito de organização do
domínio nos projetos que adotam a topologia de camadas deste conjunto. Antes de
aplicá-la, leia e aplique a base arquitetural, mesmo na adoção isolada desta
norma. O caminho abaixo é relativo a este arquivo:

- `AGENTS.architecture.layer-boundaries.md`

Esta norma não altera as responsabilidades nem as dependências das camadas e
não obriga a criar uma estrutura de código adicional.

## Conceito

- Uma unidade de negócio reúne responsabilidades de domínio que atendem a um
  interesse de negócio comum. Sua fronteira deve permitir reconhecer esse
  interesse e a relação entre as responsabilidades contidas nela.
- A escala da unidade varia conforme o assunto: uma decisão ou operação coesa
  pode constituir uma unidade pequena; um conjunto de unidades relacionadas
  pode constituir uma unidade maior.
- `Policy`, `Service` e `Feature` podem materializar unidades de negócio, cada
  qual segundo sua responsabilidade e suas regras próprias. O conceito não
  exige escolher uma dessas estruturas nem cria um novo tipo de classe,
  package ou módulo.
- Toda a camada de domínio de um projeto também pode ser considerada uma
  unidade de negócio quando suas diversas responsabilidades atendem a um
  interesse de negócio comum. Nesse caso, ela pode conter unidades menores,
  cada uma com seu propósito coeso.
- O tamanho da unidade não é determinado pela quantidade de classes, regras
  ou responsabilidades. Ao delimitar uma unidade, explicite o interesse comum
  que reúne suas partes; responsabilidades sem essa relação devem permanecer
  em unidades distintas.

## Precedência

- A classificação como unidade de negócio não amplia o acesso entre camadas,
  não substitui as fronteiras de `Service`, `Policy` ou `Feature` e não torna
  obrigatória a adoção de uma feature.

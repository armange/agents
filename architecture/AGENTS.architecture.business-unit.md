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

## Aplicação ao desenvolvimento

- Antes de planejar ou implementar um comportamento de domínio, identifique o
  interesse de negócio atendido, a unidade responsável e a relação de cada
  responsabilidade envolvida com esse interesse. Quando a mudança envolver
  mais de uma unidade, explicite a fronteira e a colaboração entre elas.
- Organize o código a partir dessa delimitação. Distribua as responsabilidades
  relacionadas ao interesse identificado nas estruturas e localizações
  permitidas pela arquitetura base; mantenha em unidades distintas as
  responsabilidades que não compartilham esse interesse.
- Escolha `Policy`, `Service` ou `Feature` conforme a responsabilidade e as
  regras próprias de cada estrutura. A quantidade de classes não determina a
  escolha, e a classificação como unidade de negócio não exige criar uma
  estrutura nova.
- Ao revisar a implementação, confira se é possível explicar o interesse
  comum da unidade e a relação de cada parte com ele. Se alguma
  responsabilidade não pertencer a esse interesse, revise a delimitação antes
  de concluir o trabalho.

## Precedência

- A classificação como unidade de negócio não amplia o acesso entre camadas,
  não substitui as fronteiras de `Service`, `Policy` ou `Feature` e não torna
  obrigatória a adoção de uma feature.

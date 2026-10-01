# Arquitetura: Features de Domínio

## Base e normas relacionadas

Esta norma se aplica somente aos projetos que adotam a topologia de camadas
deste conjunto e optam por organizar um comportamento de domínio como feature.
Antes de analisar, revisar, planejar ou modificar uma feature, leia e aplique:

- `AGENTS.architecture.package-topology.md`
- `AGENTS.architecture.class-suffixes.md`
- `../coding/AGENTS.coding.data-contract-naming.md`

As regras abaixo especializam a organização interna da feature sem alterar as
responsabilidades das demais camadas nem autorizar dependências além das
permitidas pela arquitetura base, carregada obrigatoriamente pelas normas de
topologia e de sufixos citadas acima.

## Quando usar

- Uma feature encapsula a colaboração de várias classes especializadas para
  produzir um comportamento de negócio coeso do domínio.
- A adoção da estrutura de feature é opcional. Uma regra que caiba de modo
  coeso em um método ou classe pode permanecer em um `Service` ou `Policy`.
- A quantidade de classes não é um limiar automático. Use a menor fronteira
  que reúna os colaboradores necessários para um único propósito de domínio;
  não agrupe comportamentos independentes na mesma feature.
- Uma feature pode conter services, policies, validações e outras classes de
  domínio conforme suas responsabilidades reais. Nenhum desses tipos de
  colaborador é obrigatório apenas pela adoção da feature.

## Pacote e módulo

- Cada feature ocupa um único package `domain.feature.<nome>`, identificado
  por um nome único e significativo no domínio do projeto.
- Todas as classes próprias da feature, inclusive seus contratos públicos de
  dados, ficam diretamente nesse package. Não crie subpackages como `dto`,
  `service`, `policy` ou `internal` dentro dele.
- Uma feature pode ocupar sozinha um módulo de domínio quando isso criar uma
  fronteira útil de dependência, publicação, teste ou reutilização. O módulo é
  opcional e contém somente a feature como responsabilidade de produção; o
  package e as regras de encapsulamento continuam os mesmos.
- O módulo da feature pode depender de tipos compartilhados do domínio de que
  sua API ou implementação realmente precise. Ele não contém aplicação,
  persistência, clientes, integrações ou adaptadores.

## API pública e encapsulamento

- Cada feature expõe uma única classe ou interface de entrada com o sufixo
  `Feature`, como `ApproveSaleFeature`. Ela recebe os dados necessários e
  devolve um resultado de domínio; a quantidade de métodos não define se o
  comportamento é coeso.
- A API pública da feature consiste nessa entrada e nos tipos de dados
  necessários às suas assinaturas. Tipos próprios de entrada e resultado ficam
  no mesmo package e são públicos somente quando precisam ser consumidos fora
  dele.
- Prefira tipos próprios da feature para entrada e resultado. Tipos públicos
  já existentes do domínio podem ser usados quando representam conceitos
  compartilhados e estáveis. Não exponha tipos internos de outra feature,
  formatos de transporte ou detalhes de infraestrutura.
- Todas as demais classes e interfaces da feature devem ter visibilidade de
  package em Java, ou a menor visibilidade equivalente na linguagem adotada.
  Nenhuma assinatura pública pode expor tipos internos.
- Código externo à feature acessa apenas sua API pública. Services, policies,
  validações e outros colaboradores internos não são pontos de acesso direto.

## Dependências e efeitos externos

- A feature usa dados do domínio fornecidos na entrada e produz um resultado
  de domínio. Ela não realiza leitura ou escrita em banco de dados, arquivos,
  rede, filas ou outros recursos externos, nem solicita essas operações por
  contratos de saída.
- O chamador fornece à feature os dados de domínio necessários. A aplicação
  pode chamá-la diretamente ou por um service ou uma policy de domínio. Um
  service de domínio pode usar o resultado da feature e solicitar um efeito
  externo por contrato de saída do domínio. Uma policy pode usar o resultado
  para compor outra decisão de negócio, mas não solicita efeitos externos.
- Não é obrigatória uma classe intermediária apenas para repassar o resultado
  da feature. A implementação concreta da operação externa permanece na
  camada de saída apropriada, fora do package e do eventual módulo da feature;
  um service técnico dessa camada pode cumprir esse papel.
- O resultado da feature representa o comportamento calculado no domínio.
  Confirmações de persistência e dados gerados por recursos externos pertencem
  à orquestração que executa esses efeitos.
- Nas camadas externas ao domínio, a entrada pública da feature tem as mesmas
  permissões de consumo de `domain.service`, conforme os limites de camadas.
  Services e policies de domínio também podem chamá-la, somente por sua API
  pública. Acesso permitido à API não concede acesso a colaboradores internos.

## Precedência

- Quando uma feature for adotada, seu package único prevalece sobre a
  localização usual de services, policies, validações e DTOs próprios em
  packages separados. Classes fora de features continuam nas localizações
  canônicas de suas responsabilidades.
- A regra de ausência de efeitos externos é específica da feature. Ela não
  altera as permissões dos services de domínio que não pertencem a features.

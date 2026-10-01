# Arquitetura: Limites de Camadas

- Depende de: contratos de domínio, separação entre domínio e infraestrutura e regras locais que adotem esta topologia.
- Objetivo: permitir evolução isolada de cada camada, substituição de tecnologia sem reescrever regras de negócio e futura modularização sem acoplamento entre camadas por implementações concretas.
- A arquitetura mantém o domínio como fonte de contratos e semântica; as demais camadas apenas expõem, implementam ou adaptam esses contratos, sem transferir ao domínio detalhes de tecnologia, protocolo ou infraestrutura.
- Escopo: projetos podem adotar ou não cada uma das camadas `application`, `domain`, `persistence`, `client`, `integration.input` e `integration.output`. A adoção é opcional, mas não flexibiliza a arquitetura: toda camada presente deve obedecer integralmente às responsabilidades, packages e dependências definidos por esta norma.
- Precedência: esta é a fonte normativa para responsabilidades e direções de dependência entre camadas. As normas de adaptação semântica, acoplamento, localização e topologia de packages a complementam, mas não ampliam as dependências permitidas por esta norma.

## Princípios

- Uma alteração interna de camada não deve exigir refatoração em outra camada quando os contratos permanecerem compatíveis.
- Cada camada pode usar a tecnologia adequada à sua responsabilidade.
- A adoção desta base ou de uma norma derivada não exige criar camadas ou
  packages vazios; materialize somente responsabilidades necessárias ao projeto.

## Responsabilidades

### Aplicação

- `application` expõe as operações e endpoints que pertencem ao próprio sistema.
- Pode receber dados de entrada, oferecer respostas do sistema, validar estrutura, formato, protocolo e parâmetros e orquestrar casos de uso por contratos do domínio.
- Para entrada HTTP nova, prefira `application.controller`. O uso de `application.api` para essa responsabilidade é desencorajado; estruturas existentes não exigem migração automática.
- Chamadas HTTP recebidas para operar recursos do sistema pertencem à entrada da aplicação, inclusive quando o chamador é um terceiro. Callbacks HTTP autônomos, como webhooks, pertencem a `integration.input`.
- Não deve conter regra ou decisão de negócio, implementar comunicação destinada a terceiros ou depender de camada além do domínio.

### Cliente

- `client` executa chamadas HTTP síncronas de saída para sistemas de terceiros ou serviços independentes.
- Os endpoints acessados por `client` pertencem ao sistema chamado, nunca à API do próprio sistema.
- Deve traduzir dados e contratos do domínio para requisições do terceiro e traduzir as respostas recebidas para tipos do domínio.
- Seus DTOs de requisição e resposta seguem o contrato do terceiro, inclusive formatos específicos do provedor; não devem compor contratos públicos do domínio. `client` não implementa regra de negócio.
- `client.dto` é interno ao cliente: nenhuma outra camada deve acessar esses formatos de terceiros. A fronteira de `client` com o domínio usa tipos e contratos do domínio; a tradução para formatos de terceiros e a tradução de suas respostas ocorrem dentro de `client`.

### Domínio

- `domain.model` contém modelos e formatos internos; não depende de outra camada.
- `domain.service` contém contratos, invariantes e colaborações coesas de domínio, inclusive implementações internas que coordenem policies, a API pública de features, supports e contratos de saída para executar uma operação. Pode conter decisões locais inseparáveis dessa operação, mas não acumular regras de negócio independentes.
- `domain.policy` contém decisões de negócio especializadas e coesas, com significado próprio e potencial de reutilização. Essas decisões podem ser implementadas em classes concretas do próprio domínio e usar a API pública de uma feature para compor outra decisão, sem executar efeitos externos.
- `domain.feature` contém, quando adotada, a composição encapsulada de classes de domínio necessárias a um comportamento de negócio coeso. Sua entrada pública ocupa o mesmo nível arquitetural de `domain.service`; seus colaboradores internos não são pontos de acesso de outras camadas. A feature não executa efeitos externos, inclusive por contratos de saída.
- `domain.service`, `domain.policy` e `domain.feature` podem decidir a semântica de dados já representados por tipos do domínio, mas não traduzem DTOs de terceiros nem dependem de `client.dto`.
- `domain.support` contém somente estruturas e utilitários reutilizáveis; pode depender de `domain.model` e de outros supports, mas não de `domain.policy`, `domain.service` nem `domain.feature`.
- Contratos de acesso a persistência, serviços externos e publicação pertencem ao domínio. Todo contrato de saída fica em `domain.integration.output`.
- Modelos de entrada e saída do próprio domínio podem ser concretos.

### Persistência

- `persistence` implementa contratos de domínio e isola armazenamento de estado, queries, entidades de armazenamento, transações e detalhes da tecnologia.
- Armazenamento em memória também pertence a `persistence`.
- Pode adaptar o armazenamento ao formato técnico exigido, sem criar ou alterar regra e semântica de negócio.

### Integração

- `integration.input` recebe fluxos autônomos, como mensagens, eventos, filas, schedulers e callbacks HTTP, incluindo webhooks, desserializa e traduz o payload externo para contratos do domínio antes de delegar o processamento.
- `integration.output` publica fluxos autônomos para destinos externos, traduzindo contratos do domínio para o protocolo de saída.
- Nenhuma integração deve implementar regra de negócio ou expor seu protocolo como contrato público do domínio.

## Direção obrigatória das dependências

Dependências permitidas:

- `application` → `domain`;
- Dentro da entrada HTTP, `application.controller` e `application.api` → somente `domain.model.dto`, `domain.service` e a API pública de `domain.feature` no acesso direto ao domínio; não devem acessar diretamente `domain.policy`, repositories nem outros packages do domínio. A permissão geral de `application` → `domain` não amplia essa restrição específica.
- `persistence` → `domain`; pode usar tipos públicos de resultado da feature quando necessários à adaptação de dados, mas não executa sua entrada pública;
- `client` → `domain.model` e `domain.integration.output`; não acessa `domain.service` nem `domain.feature` para executar chamadas HTTP de saída.
- `integration.input` → `domain.model`, `domain.service` e a API pública de `domain.feature`;
- `integration.output` → `domain.model` e `domain.integration.output`;
- `domain.service` → `domain.model`, `domain.policy`, `domain.support`, `domain.integration.output` e a API pública de `domain.feature`;
- `domain.feature` → `domain.model`, `domain.support` e classes do próprio package; não acessa `domain.integration.output` nem outras features;
- `domain.policy` → `domain.model`, `domain.support` e a API pública de `domain.feature`;
- `domain.support` → `domain.model` e `domain.support`.

- Uma dependência não listada é proibida.
- `domain.service` usa somente contratos de saída do domínio, nunca implementações concretas de saída ou formatos de terceiros.

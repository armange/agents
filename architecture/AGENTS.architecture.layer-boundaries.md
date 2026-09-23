# Arquitetura: Limites de Camadas

- Depende de: contratos de domínio, separação entre domínio e infraestrutura e regras locais que adotem esta topologia.
- Objetivo: permitir evolução isolada de cada camada, substituição de tecnologia sem reescrever regras de negócio e futura modularização sem acoplamento por implementações concretas.
- A arquitetura mantém o domínio como fonte de contratos e semântica; as demais camadas apenas expõem, implementam ou adaptam esses contratos, sem transferir ao domínio detalhes de tecnologia, protocolo ou infraestrutura.
- Escopo: projetos podem adotar ou não cada uma das camadas `application`, `domain`, `persistence`, `client`, `integration.input` e `integration.output`. A adoção é opcional, mas não flexibiliza a arquitetura: toda camada presente deve obedecer integralmente às responsabilidades, packages e dependências definidos por esta norma.
- Precedência: esta é a fonte normativa para responsabilidades e direções de dependência entre camadas. As normas de adaptação semântica, acoplamento, localização e topologia de packages a complementam, mas não ampliam as dependências permitidas por esta norma.

## Princípios

- Uma alteração interna de camada não deve exigir refatoração em outra camada quando os contratos permanecerem compatíveis.
- Cada camada pode usar a tecnologia adequada à sua responsabilidade.

## Responsabilidades

### Aplicação

- `application` expõe as operações e endpoints que pertencem ao próprio sistema.
- Pode receber dados de entrada, oferecer respostas do sistema, validar estrutura, formato, protocolo e parâmetros e orquestrar casos de uso por contratos do domínio.
- Não deve conter regra ou decisão de negócio, implementar comunicação destinada a terceiros ou depender de camada além do domínio.

### Cliente

- `client` implementa comunicação síncrona de entrada ou saída com sistemas de terceiros.
- Endpoints em `client` pertencem a terceiros, nunca à API do próprio sistema.
- Deve traduzir entre o protocolo de terceiro e os contratos e tipos internos do domínio.
- Pode definir formatos técnicos de terceiros, mas não expô-los nos contratos públicos do domínio nem implementar regra de negócio.

### Domínio

- `domain.model` contém modelos e formatos internos; não depende de outra camada.
- `domain.service` contém contratos, invariantes, implementações internas e colaborações de negócio, inclusive orquestrações internas que usem policies ou supports.
- `domain.policy` contém decisões reutilizáveis de negócio.
- `domain.support` contém somente estruturas e utilitários reutilizáveis; pode depender de `domain.model` e de outros supports, mas não de `domain.policy` nem de `domain.service`.
- Contratos de acesso a persistência, serviços externos e publicação pertencem ao domínio. Todo contrato de saída fica em `domain.integration.output`.
- Modelos de entrada e saída do próprio domínio podem ser concretos.

### Persistência

- `persistence` implementa contratos de domínio e isola armazenamento de estado, queries, entidades de armazenamento, transações e detalhes da tecnologia.
- Armazenamento em memória também pertence a `persistence`.
- Pode adaptar o armazenamento ao formato técnico exigido, sem criar ou alterar regra e semântica de negócio.

### Integração

- `integration.input` recebe fluxos autônomos, como mensagens, eventos, filas, schedulers e callbacks, desserializa e traduz o payload externo para contratos do domínio antes de delegar o processamento.
- `integration.output` publica fluxos autônomos para destinos externos, traduzindo contratos do domínio para o protocolo de saída.
- Nenhuma integração deve implementar regra de negócio ou expor seu protocolo como contrato público do domínio.

## Direção obrigatória das dependências

Dependências permitidas:

- `application` → `domain`;
- `persistence` → `domain`;
- `client` → `domain.model`, `domain.service` e `domain.integration.output`;
- `integration.input` → `domain.model` e `domain.service`;
- `integration.output` → `domain.model` e `domain.integration.output`;
- `domain.service` → `domain.model`, `domain.policy`, `domain.support` e `domain.integration.output`;
- `domain.policy` → `domain.model` e `domain.support`;
- `domain.support` → `domain.model` e `domain.support`.

- Uma dependência não listada é proibida.
- `domain.service` usa somente contratos de saída do domínio, nunca implementações concretas ou formatos de terceiros.

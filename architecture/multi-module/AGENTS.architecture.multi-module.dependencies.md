# Arquitetura Multi-module: Dependências

- `application` pode depender de `domain` ou `domain-api`.
- Essa dependência entre módulos não autoriza acesso irrestrito das classes de entrada HTTP: em `application.controller` ou `application.api`, o acesso direto ao domínio fica limitado a `domain.model.dto`, `domain.service` e à API pública de `domain.feature`.
- `integration-input` pode depender de `domain` ou `domain-api`.
- `persistence` pode depender de `domain` ou `domain-api`.
- `persistence` pode usar tipos públicos de resultado de uma feature para adaptar dados, mas não deve executar a entrada pública da feature.
- `client` pode depender dos tipos de domínio necessários à tradução e dos contratos de saída definidos pelo domínio ou por um módulo de contratos explicitamente definido; não deve depender de `domain.service` nem da entrada pública de `domain.feature`.
- Nenhum módulo de produção fora de `client` deve depender de seus DTOs de terceiros, inclusive módulos de domínio com services, policies ou features e módulos de persistência. A comunicação entre eles usa contratos e tipos do domínio.
- `integration-output` pode depender de `domain` ou contratos de saída definidos pelo domínio.
- `domain-impl` pode depender de `domain-api`, quando houver separação entre API e implementação do domínio.
- Um módulo dedicado a uma feature é um módulo de domínio: pode depender de tipos compartilhados do domínio, mas não de módulos de aplicação, persistência, cliente, integração ou de outra feature.
- Módulos de domínio com services ou policies podem depender do módulo dedicado
  a uma feature para consumir somente sua API pública, desde que não formem um
  ciclo de dependências.
- `runtime` ou `bootstrap` pode depender de módulos de entrada, domínio, persistência, cliente e integração necessários para montar a aplicação.
- Módulos de teste podem depender dos módulos necessários ao escopo do teste, sem publicar dependências de teste como contrato de produção.
- `domain` não deve depender de `application`.
- `domain` não deve depender de `persistence`.
- `domain` não deve depender de `client` com implementação concreta.
- `domain` não deve depender de `integration-input`.
- `domain` não deve depender de `runtime` ou `bootstrap`.
- `application` não deve depender de `persistence`, salvo em módulo de composição explicitamente separado da entrada.
- `application` não deve depender de `client` concreto, salvo quando a responsabilidade real do módulo for composição ou gateway e estiver documentada.
- `persistence` não deve depender de `application`.
- `client` não deve depender de `application`.
- Nenhum módulo deve depender de `runtime` ou `bootstrap`, exceto testes específicos do próprio runtime.
- Qualquer dependência cíclica, direta ou indireta, é proibida.
- Quando o domínio precisar solicitar dados externos ou publicar eventos, o contrato deve pertencer ao domínio ou a um módulo de contrato pertencente ao domínio.
- A implementação concreta de um contrato de saída do domínio deve ficar em módulo de cliente, integração de saída ou infraestrutura equivalente.
- O domínio não deve depender de um módulo que contenha implementação concreta de comunicação externa.
- Se um módulo de cliente contém interfaces e implementação, ele não deve ser usado como dependência do domínio.

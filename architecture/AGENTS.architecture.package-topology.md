# Arquitetura: topologia de packages

## Regra geral

- Cada classe deve ficar no package que expressa sua camada, responsabilidade
  e tecnologia, quando aplicável.
- Os packages abaixo são canônicos. Não crie package paralelo quando uma
  responsabilidade já tiver localização definida nesta norma.
- Um contexto coeso pode ser acrescentado após o package de responsabilidade,
  como em `domain.model.repository.sale` ou
  `persistence.model.jpa.entity.sale`.
- Não é necessário criar packages vazios. Um package não listado só é
  permitido quando representar responsabilidade real que não se encaixe nos
  packages canônicos e não esconda uma responsabilidade já prevista.

## Aplicação, clientes e integrações

- `application.api`, `application.controller`, `application.config` e
  `application.event` recebem, respectivamente, APIs, controllers,
  configurações da aplicação e listeners de eventos. APIs e controllers de
  `application` pertencem ao próprio sistema.
- `application.service.<contexto>` contém o
  `<Contexto>ApplicationService`; `application.validation.<contexto>` contém
  o `<Contexto>InputValidation`.
- `client` contém adaptadores síncronos de entrada e saída para terceiros;
  `client.dto` contém seus formatos técnicos de dados e
  `client.<tecnologia>.config`, a configuração da tecnologia usada.
- `integration` é a raiz de adaptadores de integração; `integration.input` e
  `integration.output` contêm, respectivamente, adaptadores de fluxos
  autônomos de entrada e saída. Suas configurações ficam em
  `integration.input.<tecnologia>.config` e
  `integration.output.<tecnologia>.config`.

## Domínio

- `domain.model` concentra o modelo de domínio; use seus subpackages `dto`,
  `entity`, `document`, `dao`, `factory`, `mapper` e `repository` conforme a
  responsabilidade.
- `domain.policy.<contexto>` contém decisões de negócio reutilizáveis;
  `domain.validation.<contexto>` contém validações de regras de negócio;
  `domain.service.<contexto>` contém contratos e colaborações coesas de
  domínio.
- `domain.support.<contexto>` é reservado a estruturas de suporte
  reutilizáveis e não recebe policies ou validações de negócio.
- `domain.integration` contém contratos de integração pertencentes ao domínio;
  `domain.integration.output` contém seus contratos de saída.

## Persistência e infraestrutura de dados

- Modelos específicos de JPA ficam em
  `persistence.model.jpa.<responsabilidade>`; modelos JDBC ficam em
  `persistence.model.jdbc.<responsabilidade>`; modelos NoSQL ficam em
  `persistence.model.nosql.<responsabilidade>`.
- JPA e JDBC usam as responsabilidades `entity`, `dao`, `factory`,
  `repository`, `service` e `validation`. NoSQL usa `document`, `dao`,
  `factory`, `repository`, `service` e `validation`.
- Configurações técnicas ficam em `persistence.<tecnologia>.config`.
- Serviços técnicos de persistência ficam em
  `persistence.<tecnologia>.service`; quando não houver tecnologia específica,
  ficam em `persistence.service`.

## Estruturas transversais

- `model.wrapper` contém wrappers de modelo com semântica própria.

## Exemplos

```java
package net.example.application.validation.sale;

public class SaleInputValidation {
}
```

```java
package net.example.domain.validation.sale;

public final class SaleContractReferenceValidation {
}
```

```java
package net.example.persistence.model.jpa.repository.sale;

public interface SaleJpaRepository {
}
```

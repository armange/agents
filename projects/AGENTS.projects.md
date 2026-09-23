# Regras Multiprojetos e Multilinguagens

## Versionamento e publicação

Antes de analisar, revisar, planejar ou modificar versão de projeto, dependência
entre projetos, publicação de artefato ou compatibilidade de contrato, leia
também:

- `AGENTS.projects.versioning.md`

Uma citação deste arquivo ativa obrigatoriamente a norma de versionamento. Suas
regras materiais devem ser seguidas sempre que a atividade tratar de versão,
dependência entre projetos, publicação de artefato ou compatibilidade de
contrato.

## Regra Global de Aliases

- Aliases de projetos devem ser reconhecidos sem diferenciar maiúsculas de minúsculas.

## Projetos

### archguard

- nome: `archguard`
- tipo: plugin
- exposição: não aplicável
- descrição: Plugin de controle de arquitetura desacoplada, multicamadas e orientada ao DDD.
- aliases: nenhum alias adicional declarado

### nexus-auth-service

- nome: `nexus-auth-service`
- tipo: serviço
- exposição: interno, não exposto publicamente
- descrição: Serviço de autenticação e autorização de acesso aos serviços Nexus.
- aliases: `auth`, `auth service`, `serviço auth`

### nexus-bff-web

- nome: `nexus-bff-web`
- tipo: serviço
- exposição: externo, exposto publicamente
- descrição: Serviço de entrada para os serviços internos, em formato de proxy, com controle de acesso provido em conjunto com o `nexus-auth-service`.
- aliases: `bff`, `serviço bff`

### nexus-customer-service

- nome: `nexus-customer-service`
- tipo: serviço
- exposição: interno, não exposto publicamente
- descrição: Serviço de cadastro de clientes.
- aliases: `customer`, `serviço customer`

### nexus-database

- nome: `nexus-database`
- tipo: ferramenta auxiliar interna
- exposição: não aplicável
- descrição: Ferramenta de migrations focada em Postgres para versionar e implantar schemas de banco de dados dos serviços Nexus.
- aliases: `migrations`, `migration`

### nexus-karate-tests

- nome: `nexus-karate-tests`
- tipo: ferramenta auxiliar interna
- exposição: não aplicável
- descrição: Ferramenta de testes automatizados E2E focada nos serviços Nexus implantados e em execução em ambiente completo.
- aliases: `karate`

### nexus-persistence

- nome: `nexus-persistence`
- tipo: biblioteca auxiliar interna
- exposição: não aplicável
- descrição: Biblioteca de comportamentos transversais de persistência para os serviços Nexus.
- aliases: `lib de persistência`

### nexus-postman-collection

- nome: `nexus-postman-collection`
- tipo: ferramenta auxiliar interna
- exposição: não aplicável
- descrição: Ferramenta para versionar e compartilhar coleções do Postman focadas nos serviços Nexus.
- aliases: `coleções do postman`

### nexus-request-foundation

- nome: `nexus-request-foundation`
- tipo: biblioteca auxiliar interna
- exposição: não aplicável
- descrição: Biblioteca de comportamentos de requisição e resposta HTTP para os serviços Nexus.
- aliases: `lib de requisições`, `lib do foundation`, `foundation`

### nexus-simcard-management-service

- nome: `nexus-simcard-management-service`
- tipo: serviço
- exposição: interno, não exposto publicamente
- descrição: Serviço de cadastro de produto, plano, contrato e subscrições relacionados ao fluxo de simcard.
- aliases: `simcard`, `serviço simcard`

### nexus-validation

- nome: `nexus-validation`
- tipo: biblioteca auxiliar interna
- exposição: não aplicável
- descrição: Biblioteca de comportamentos relacionados à validação de dados e à internacionalização de mensagens (i18n) para os serviços Nexus.
- aliases: `validation`, `lib de validation`

### nexus-customer-scope

- nome: `nexus-customer-scope`
- tipo: biblioteca auxiliar interna
- exposição: não aplicável
- descrição: Biblioteca de controle de acesso a dados, baseado na hierarquia de clientes armazenado em banco.
- aliases: `customer scope`, `lib de scope`

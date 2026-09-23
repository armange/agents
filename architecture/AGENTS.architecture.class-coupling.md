# Arquitetura: acoplamento entre classes

## Arquitetura base

Esta norma pressupõe a topologia de camadas deste conjunto. Antes de aplicar
suas regras, leia e aplique a base, mesmo na adoção isolada deste especialista.
O caminho abaixo é relativo a este arquivo:

- `AGENTS.architecture.layer-boundaries.md`

As regras desta norma não ampliam as responsabilidades nem as dependências
permitidas pela base. Camadas opcionais só devem existir quando necessárias
às responsabilidades do projeto.

## Direção das dependências

- Classes de domínio não devem depender de classes de aplicação, persistência,
  cliente, integração, configuração, framework, protocolo externo, banco de
  dados ou outra implementação concreta de infraestrutura.
- Classes de persistência, cliente e integração devem depender de contratos e
  tipos de domínio quando implementarem uma colaboração definida pelo domínio.
- Quando o domínio precisar acessar persistência, serviço externo ou publicar
  evento, o contrato deve pertencer à camada de domínio; a implementação
  concreta deve permanecer na camada de saída adequada.
- Classes de entrada e adaptação devem traduzir protocolos externos para os
  contratos internos. DTOs, exceções e tipos específicos de HTTP, mensageria
  ou provedores externos não devem compor contratos públicos do domínio.

## Composição e configuração

- Tipos concretos de camadas diferentes só podem ser reunidos em configuração
  ou runtime para injeção de dependência.
- Fora da configuração de runtime, uma camada deve colaborar com outra por
  contratos, e não por injeção ou import direto de implementações concretas.
- Estruturas de dados concretas podem ser usadas quando fizerem parte do
  contrato de dados aplicável; essa exceção não autoriza acoplamento a
  implementação de infraestrutura.
- Uma configuração pertence à camada que configura. `application.config`
  configura somente a aplicação; configurações técnicas ficam na camada e na
  tecnologia que configuram.
- Classes de configuração e runtime devem permanecer finas: não devem conter
  regra de negócio, query, adaptação de protocolo ou transformação de domínio.

## Ciclos e colaboração

- Dependências cíclicas, diretas ou indiretas, entre classes ou packages são
  proibidas.
- Toda dependência deve representar uma colaboração real, compatível com a
  responsabilidade da classe e com a direção arquitetural das camadas.
- Não crie interfaces, abstrações ou packages intermediários apenas para
  reduzir imports, esconder um acoplamento legítimo ou contornar uma direção
  de dependência proibida.

## Exceções e precedência

- Adaptações técnicas exigidas por frameworks podem existir na borda ou na
  infraestrutura, desde que não vazem para o domínio.
- Normas mais específicas de policies, services, persistência, clientes,
  integrações e localização de classes prevalecem sobre esta norma geral
  somente quando compatíveis com as responsabilidades e direções de
  dependência da arquitetura base.

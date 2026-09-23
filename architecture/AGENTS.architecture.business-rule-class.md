# Arquitetura: Classe Dedicada por Regra de Negócio

## Arquitetura base

Esta norma pressupõe a topologia de camadas deste conjunto. Antes de aplicar
suas regras, leia e aplique a base, mesmo na adoção isolada deste especialista.
O caminho abaixo é relativo a este arquivo:

- `AGENTS.architecture.layer-boundaries.md`

As regras desta norma não ampliam as responsabilidades nem as dependências
permitidas pela base. Camadas opcionais só devem existir quando necessárias
às responsabilidades do projeto.

## Regras

- Depende de: arquitetura base indicada acima e separação de responsabilidades nela definida.
- Objetivo: manter regras de negócio isoladas, legíveis, testáveis e substituíveis sem acúmulo de responsabilidades em classes genéricas.
- Cada implementação de regra de negócio deve ficar em uma classe nova e dedicada àquela regra.
- Quando houver um grupo coeso de regras de negócio relacionadas ao mesmo recurso, fluxo, entidade ou política, as classes dedicadas dessas regras devem ficar em um package dedicado dentro da camada de domínio.
- Validações de regra de negócio devem ser implementadas em classes especializadas e dedicadas, organizadas pelo recurso, entidade, agregado, fluxo ou política validada.
- Validadores de domínio devem operar preferencialmente sobre tipos de domínio já resolvidos, e não sobre DTOs crus, sempre que a validação depender de factories, referências, tipos internos ou normalizações já pertencentes ao domínio.
- Validadores reutilizáveis devem receber explicitamente o contexto necessário para produzir erro correto ao chamador, como path de campo, path de coleção, identificador de fluxo ou payload de erro, sem depender de protocolo externo dentro da regra.
- Validações de coleções devem definir comportamento explícito para lista ausente, lista vazia, itens inválidos, montagem de path com índice, ordem de varredura e estratégia de falha, como fail-fast ou acumulação de erros.
- Validações contextuais de merge, replace, transição ou reconciliação devem ficar na mesma classe dedicada da entidade, recurso ou política validada quando fizerem parte da mesma regra coesa.
- A classe chamadora deve aplicar a validação depois de mapear ou resolver os valores necessários e antes de executar persistência, chamada externa, autorização dependente do estado mutado ou qualquer efeito colateral que pressuponha payload válido.
- Quando a validação produzir resposta de API, a regra deve definir explicitamente status HTTP, chave de mensagem, path de erro, payload e mensagens internacionalizadas quando esses elementos fizerem parte do contrato público do serviço.
- Grupos de regras que representem decisões ou políticas de negócio reutilizáveis devem ficar preferencialmente sob `domain.policy.<contexto>`.
- Validações de regra de negócio, invariantes e referências já resolvidas devem
  ficar sob `domain.validation.<contexto>` e usar o sufixo `Validation`.
- Grupos de regras que representem contratos ou orquestrações coesas de caso
  de uso do domínio devem ficar preferencialmente sob
  `domain.service.<contexto>`.
- Packages como `domain.support.<contexto>` devem ser reservados para suportes reutilizáveis, utilitários de domínio e estruturas compartilhadas; não devem ser a casa principal de decisões de negócio.
- Quando uma regra de negócio for complexa demais para uma única classe simples, a implementação pode usar orquestradores, desde que cada parte orquestrada continue coesa e dedicada a uma responsabilidade clara.
- Não deve: manter múltiplas regras de negócio independentes na mesma classe.
- Não deve: colocar validação de regra de negócio em mappers; mappers devem apenas transformar, copiar, adaptar ou compor valores entre representações.
- Não deve: transformar services, mappers, controllers, repositories, clients ou adapters em agregadores de regras de negócio heterogêneas.
- Não deve: lançar erro genérico, erro de banco ou erro de infraestrutura para violação de payload que pode ser validada antes do efeito colateral.
- Não deve: criar packages de regras de negócio fora das camadas reconhecidas pela arquitetura do projeto, como packages raiz `rules`, `business` ou equivalentes, quando a arquitetura base já definir a camada de domínio.
- Exceções: composições pequenas e inseparáveis de uma mesma regra podem permanecer na mesma classe quando separá-las criar complexidade artificial.
- Exceções: validações puramente sintáticas ou estruturais do protocolo de entrada podem permanecer na borda quando não dependerem de semântica de domínio.
- Precedência: esta norma não altera a direção de dependências nem as responsabilidades das camadas definidas pela arquitetura base.

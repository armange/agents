# HTTP: Semântica de exclusão e desativação

## Objetivo e escopo

Esta norma se aplica à criação ou revisão de contratos HTTP que excluem um recurso, removem uma relação ou alteram um recurso para um estado inativo. Ela define o significado do método para quem consome a API; não impõe modelo de persistência a operações que não exponham esses contratos.

## Regras

- `DELETE` indica exclusão física do recurso identificado pela rota. Quando a rota identifica uma relação ou configuração filha, a exclusão física dessa relação ou configuração não implica excluir o recurso pai.
- Não use `DELETE` para apenas marcar como inativo, desabilitado, cancelado ou removido logicamente um recurso que continua persistido. Quando o registro deve permanecer, exponha a mudança de estado como atualização; `PATCH` é uma opção para alterar somente o estado.
- O contrato de atualização deve declarar os estados aceitos, o payload, a autorização e o efeito de requisições repetidas. A manutenção do registro e das relações necessárias deve ser verificável.
- Uma operação de exclusão física e uma de desativação lógica têm efeitos diferentes e não devem ser tratadas como contratos equivalentes apenas por compartilharem um objetivo de negócio.

## Compatibilidade

- Esta norma orienta contratos novos e contratos alterados no escopo do trabalho. Ela não exige refatoração, remoção ou rejeição automática de endpoints legados em outros projetos.
- Ao alterar um contrato existente, avalie consumidores e versionamento antes de retirar ou mudar o significado de seu método HTTP. Não mude silenciosamente a semântica de um `DELETE` publicado.

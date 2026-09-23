# Codificação: Semântica de Operações

- `find*`: localizar, consultar ou listar dados sem mutação de estado.
- `create*`: criar um novo recurso ou registro, sem semântica de atualização.
- `save*`: persistir o estado de uma entidade ou agregado apenas quando a intenção for explicitamente genérica e não houver semântica mais precisa de `create*`, `replace*` ou `merge*`.
- `replace*`: substituir integralmente o estado de um recurso existente.
- `merge*`: combinar ou atualizar parcialmente um estado existente, preservando dados não informados.
- `delete*`: remover logicamente ou fisicamente, conforme a política do domínio ou da infraestrutura.
- Não misture semânticas no nome da operação.
- Não use `save*` quando a operação for claramente `create*`, `replace*` ou `merge*`.

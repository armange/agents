# Regras de Configuração

## Prefixo `nexus`

- Quando forem criadas novas configurações em projetos deste workspace, elas devem ser posicionadas sob o tópico `nexus`.
- Novas chaves de configuração do domínio Nexus devem usar namespace explícito sob `nexus`, sem criar tópicos soltos na raiz da configuração do projeto.
- Exemplos preferidos:
  - `nexus.any.configuration.item`
  - `nexus.customer.scope.cache.ttl`
- Exemplo de referência de estilo:
  - assim como configurações nativas do Spring usam prefixos como `spring.any.configuration.item`, configurações novas do domínio Nexus devem seguir padrão equivalente sob `nexus`.

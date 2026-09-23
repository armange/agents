# Regras de Configuração

## Namespace da aplicação

- Novas configurações próprias da aplicação devem usar o namespace definido
  pelo projeto, sem criar tópicos soltos na raiz da configuração.
- Preserve o namespace já adotado. Quando ele ainda não existir, defina um
  prefixo que identifique a aplicação ou seu domínio e documente essa escolha.
- Mantenha as configurações próprias separadas dos namespaces reservados por
  frameworks e bibliotecas.
- Exemplos abstratos para uma aplicação cujo prefixo escolhido seja `app`:
  - `app.feature.enabled`
  - `app.cache.ttl`
- O prefixo dos exemplos é ilustrativo; não deve substituir o namespace real
  definido pelo projeto consumidor.

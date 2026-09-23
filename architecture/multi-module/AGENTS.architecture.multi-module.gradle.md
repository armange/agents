# Arquitetura Multi-module: Gradle

- Dependências entre módulos devem ser declaradas com a menor exposição possível.
- Use `api` apenas quando os tipos da dependência aparecerem na API pública do módulo consumidor.
- Use `implementation` quando a dependência for detalhe interno do módulo.
- Não use `api` para vazar infraestrutura para consumidores.
- Não use `testFixtures` como forma de compartilhar implementação de produção.
- `testFixtures` deve conter apenas suporte de teste, builders, fixtures e utilitários de validação.
- O módulo raiz deve centralizar convenções de build quando isso reduzir repetição, mas não deve esconder dependências arquiteturais relevantes.
- Cada submódulo deve declarar suas dependências de forma rastreável.

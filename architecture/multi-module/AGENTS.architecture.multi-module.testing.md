# Arquitetura Multi-module: Testes

- Regras de negócio devem ser testadas preferencialmente no módulo de domínio.
- Adapters de persistência, clientes e integrações devem ter testes focados no próprio módulo quando dependerem de infraestrutura, serialização, query, protocolo ou configuração técnica.
- O módulo de aplicação deve testar contratos de entrada, validação de protocolo e delegação correta ao domínio.
- O módulo de runtime deve ter testes de composição suficientes para provar que o conjunto de módulos inicia e injeta as implementações esperadas.
- Testes integrados de ponta a ponta dentro do projeto devem ficar no módulo que representa o runtime ou em módulo de testes dedicado.
- Ao alterar uma dependência entre módulos, deve-se validar pelo menos o módulo alterado e os consumidores diretos afetados.
- Alterações Java em projeto multi-module continuam exigindo verificação completa na fase final, conforme a regra local do projeto aplicável.

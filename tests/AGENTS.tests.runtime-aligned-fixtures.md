# Testes: fixtures alinhadas ao runtime

- Test fixtures devem espelhar o comportamento real do módulo que testam.
- Não crie um segundo padrão de mensagens, contratos HTTP ou resolvers apenas para testes quando o runtime já tiver um padrão definido.
- Fixtures compartilhadas devem reutilizar helpers e factories do runtime sempre que isso preservar o mesmo contrato observado pelo cliente.
- Se o teste depende de mensagens i18n, deve usar o mesmo bundle e o mesmo resolver que o runtime usa para aquele módulo.
- A fixture pode simplificar a montagem, mas não pode alterar o formato do erro, a origem das mensagens ou o fallback de resolução.

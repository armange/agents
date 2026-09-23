# i18n: resolvers de mensagem

- A criação de resolvers de mensagem deve ser centralizada em um helper, factory ou classe dedicada por módulo.
- Não espalhe instâncias diretas de resolvers em controllers, filtros, handlers ou testes quando o módulo já tiver um ponto central de criação.
- Fixtures e testes devem reutilizar o mesmo resolver usado em runtime quando dependerem das mesmas mensagens.
- Se um módulo publica bundle próprio, o resolver correspondente deve apontar explicitamente para esse bundle.
- O resolver local pode combinar bundle do módulo e fallback da biblioteca, desde que a ordem e a intenção fiquem explícitas.

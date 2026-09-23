# Exceções: interpretação

## Interpretação neutra de transporte

- Toda `Exception` que alcançar uma fronteira de exposição deve ser submetida
  a interpretação antes de ser formatada pelo canal de saída.
- A interpretação de exceções não deve depender de HTTP, mensageria, jobs, CLI
  ou outro protocolo de transporte.
- `ConstraintViolationsDto` e `ViolationDto` são o envelope padrão de
  violações reutilizável entre canais de exposição; nenhum canal deve criar
  envelope paralelo para representar as mesmas violações.
- Não crie ou mantenha estruturas intermediárias que dupliquem o envelope
  padrão de violações, como `ValidationViolation`.
- Interpretadores devem ser extensíveis, ordenados e especializados por tipo
  de exceção ou família de exceções.
- Um interpretador pode reconhecer exceções encapsuladas em sua cadeia de
  causas, inclusive exceções de bibliotecas, frameworks, bancos de dados ou
  provedores externos.
- Toda exceção sem interpretador aplicável deve produzir resultado de fallback
  seguro, sem expor tipo, mensagem, stack trace ou detalhes técnicos ao
  consumidor externo.
- Não crie interpretadores apenas para ocultar uma violação de direção de
  dependências ou para transformar regra de negócio em detalhe de transporte.

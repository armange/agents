# Exceções: registro técnico

## Registro de falhas

- Exceções interpretadas com sucesso como falhas esperadas de entrada, estado
  ou validação não devem gerar automaticamente log de erro.
- Toda exceção que resulte em falha interna deve gerar log de erro com os
  detalhes técnicos e stack trace completos.
- Toda falha de componente do pipeline de interpretação ou enriquecimento de
  violações deve gerar o mesmo log completo, ainda que a resposta externa
  permaneça uma falha esperada.
- Detalhes registrados no log não devem ser incluídos no envelope exposto ao
  consumidor.

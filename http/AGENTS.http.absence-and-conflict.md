# HTTP: ausência de recurso e conflito

## Objetivo e escopo

Esta norma define os status HTTP para ausência normal de recurso e para
conflitos de dados ou estado em contratos que adotem estas convenções. Aplica-se
a endpoints, respostas de exceção e cenários de contrato que dependam desses status.

## Ausência normal do recurso-alvo

- `404 Not Found` é reservado exclusivamente para endpoint ou path inexistente.
- Quando uma consulta por filtro ou por identificador não encontrar dados, o
  contrato deve retornar `204 No Content`, sem corpo, envelope de erro ou
  exceção exposta.
- Quando um comando direto por identificador não encontrar o seu próprio
  recurso-alvo, o contrato deve retornar `204 No Content`, sem corpo, envelope
  de erro, exceção exposta ou mutação.
- A ausência normal do recurso-alvo não é conflito nem falha de integridade e
  não deve ser convertida para `409 Conflict`.

## Conflito de dependência, dados ou estado

- Quando uma operação de escrita depender de entidade relacionada obrigatória
  inexistente, o contrato deve retornar `409 Conflict` com o envelope canônico
  de violações definido pelo projeto.
- Violações de integridade conhecidas, inclusive as identificadas por causa
  específica de banco ou trigger, devem retornar `409 Conflict` com o envelope
  canônico de violações.
- Exceções desconhecidas não devem ser classificadas como conflito por
  aproximação: devem retornar `500 Internal Server Error` com envelope seguro,
  sem detalhes técnicos.

## Precedência e composição

- Estas regras especializam a conversão HTTP de exceções para os contextos de
  ausência e conflito e prevalecem sobre regra genérica que trate toda falha de
  dados ou estado como `409 Conflict`.
- O BFF deve preservar esses status e envelopes quando recebidos de serviço
  interno, sem reinterpretar a ausência normal ou o conflito de domínio.

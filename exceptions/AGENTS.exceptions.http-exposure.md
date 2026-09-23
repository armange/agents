# Exceções: exposição HTTP

## Captura e formatação

- A fronteira HTTP deve capturar toda `Exception` que a alcançar, aplicar os
  interpretadores disponíveis e converter o resultado para o contrato
  canônico de erro.
- Na exposição HTTP, use o envelope canônico de erro definido pelo projeto.
  Esse envelope deve ser reutilizável entre canais; HTTP apenas o adapta para
  sua resposta. Não introduza um formato paralelo ao contrato adotado, salvo
  exceção explícita e documentada.
- A conversão para HTTP deve definir o status e construir as violações do
  envelope sem vazar detalhes técnicos de exceções não reconhecidas.
- i18n e resolução de mensagens ocorrem exclusivamente nesta etapa de
  exposição, para todos os idiomas suportados pela aplicação.
- O HTTP deve reservar `404 Not Found` para endpoint ou path inexistente.
- A ausência normal do recurso-alvo de uma consulta ou operação direta por ID
  não é falha de dados ou estado: deve retornar `204 No Content`, sem exceção
  nem envelope canônico de erro.
- Uma falha exposta relacionada a dados ou estado, distinta da ausência normal
  do recurso-alvo, deve usar `409 Conflict` com o envelope canônico.

## Extensão e múltiplas violações

- Conversores HTTP reutilizáveis devem ser implementados no componente
  compartilhado de tratamento de erros adotado pelo projeto; conversores locais
  são permitidos apenas para erros específicos e devem produzir o mesmo contrato
  canônico.
- Múltiplas violações devem ser acumuladas e expostas por uma única exceção;
  no HTTP, elas retornam `422 Unprocessable Entity` em um único envelope canônico
  contendo todas as violações.
- Quando o serviço já utilizar um conversor compatível, ele deve ser reutilizado
  em vez de duplicado.

## Responsabilidade do BFF

- O BFF não deve reinterpretar erros de regra de negócio já expostos por
  serviços internos.
- O BFF pode interpretar erros de comunicação, arquitetura ou processamento
  de baixo nível de sua própria responsabilidade.

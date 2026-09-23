# Codificação: Desenho de Operações

- Cada operação, como função, método, procedimento, handler ou equivalente da linguagem, deve ter uma única responsabilidade.
- Quando uma operação orquestrar responsabilidades distintas, cada etapa deve ser delegada a uma operação auxiliar coesa e nomeada pela responsabilidade executada.
- A orquestração pode conter apenas instruções técnicas inseparáveis da composição, como atribuições locais, preparação de argumentos, chamadas das etapas e retorno do resultado.
- Se uma operação contiver múltiplas validações, ramificações ou etapas relevantes, cada parte deve ser extraída para operações coesas e nomeadas pela responsabilidade.
- Estruturas de decisão complexas devem ser divididas em operações menores com nomes descritivos.
- Operações longas ou densas devem ser simplificadas por composição de operações menores.

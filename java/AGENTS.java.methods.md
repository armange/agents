# Java: Métodos e Assinaturas

## Parâmetros

- Parâmetros de métodos e construtores devem ser declarados como `final` por padrão.
  - Exceções permitidas: limitações técnicas, contratos de frameworks, código gerado ou casos em que `final` seja inadequado ao padrão da implementação.

## Assinatura

- Quando a operação tiver a mesma semântica e variar apenas na assinatura, deve-se usar sobrecarga de método.
- Sobrescrita deve ser usada apenas quando houver contrato herdado, interface, classe base ou exigência explícita do framework.

## Retorno

- O retorno do método deve estar separado por uma linha em branco acima do retorno, exceto se a implementação do método tiver uma única instrução de retorno de valor.

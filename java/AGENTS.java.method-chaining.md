# Java: encadeamento de chamadas

## Quebra de linha

- Encadeamentos com mais de uma chamada de método devem ser escritos em
  múltiplas linhas.
- A expressão inicial deve permanecer na primeira linha.
- Cada chamada encadeada deve iniciar em uma nova linha, com um nível adicional
  de indentação e o ponto (`.`) no início da linha.
- A regra também se aplica quando uma das chamadas recebe lambda, referência de
  método ou argumentos extensos.

```java
final Sale sale = repository
        .findById(saleId)
        .filter(this::isActive)
        .orElseThrow();
```

Não escreva encadeamentos de múltiplas chamadas em uma única linha.

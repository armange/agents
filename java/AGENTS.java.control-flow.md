# Java: estruturas de controle

## Blocos delimitados por chaves

- Todas as estruturas condicionais e de repetição devem delimitar seus blocos
  com chaves (`{` e `}`), mesmo quando o bloco possuir apenas uma instrução.
- A regra se aplica a `if`, `else`, `else if`, `for`, `foreach`, `while` e
  `do-while`.
- Não utilize a sintaxe de instrução única sem chaves, inclusive quando a
  instrução for `return`, `throw`, `break` ou `continue`.

```java
if (sale.isCancelled()) {
    return;
}

for (final SaleItem item : sale.getItems()) {
    process(item);
}
```

## Uma instrução por linha

- Cada instrução Java terminada por ponto e vírgula (`;`) deve ocupar sua
  própria linha.
- Após um ponto e vírgula, inicie a próxima instrução em uma nova linha; não
  escreva múltiplas instruções na mesma linha.

```java
final Sale sale = findSale(saleId);
sale.cancel(reason);
```

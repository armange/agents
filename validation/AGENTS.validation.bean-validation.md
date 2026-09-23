# Java: Bean Validation

## Integração padrão

- Projetos Java Nexus que recebam contratos de entrada devem usar Jakarta Bean
  Validation por meio da integração fornecida pelo `nexus-validation`.
- Projetos que não recebam contratos de entrada não devem adicionar essa
  dependência sem necessidade concreta.
- Não crie integração, envelope, exceção ou conversor paralelo para violações
  declarativas quando o `nexus-validation` já fornecer o comportamento
  necessário.

## Validações estruturais

- Validações locais e declarativas de estrutura devem usar constraints Jakarta
  Bean Validation no contrato correspondente.
- Esta regra abrange presença, coleção vazia, texto em branco, formato,
  tamanho, faixa numérica, positividade e validação de valores aninhados.
- Objetos, coleções e elementos aninhados que também possuam constraints devem
  usar `@Valid` para que a validação seja propagada.
- A fronteira de entrada deve disparar a validação declarativa: use `@Valid`
  em entradas HTTP e o mecanismo Jakarta Bean Validation equivalente nos
  demais tipos de entrada.
- Quando uma entrada não HTTP precisar de uma fronteira explícita para disparar
  a validação declarativa, use `<Contexto>InputValidation` em
  `application.validation.<contexto>`. Essa classe apenas dispara Bean
  Validation; não consulta referências nem implementa regra de negócio.

```java
public record CreateSaleItemDto(
        @NotNull UUID contractId,
        @Positive Integer quantity,
        @Valid CreateSaleProvisioningDto provisioning) {
}
```

## Regras de negócio

- `Policy` e `Validation` manuais devem ser usados apenas para regras de
  negócio que dependam de estado, referências, múltiplos dados ou decisão
  contextual complexa. `Validation` deve ficar em
  `domain.validation.<contexto>`; `Policy` permanece em
  `domain.policy.<contexto>` quando representar uma decisão reutilizável.
- Regras estruturais não devem ser reimplementadas manualmente em policies,
  services, controllers, mappers ou repositories quando puderem ser expressas
  por Jakarta Bean Validation.
- Uma validação que exija consulta, contrato ativo ou comparação entre dados
  de recursos distintos é regra de negócio e deve permanecer em classe de
  domínio dedicada.

```java
public static void validate(final SaleContract contract) {
    if (!contract.isActive()) {
        throw new IllegalStateException("Sale contract must be active");
    }
}
```

## Migração

- Ao alterar uma validação estrutural manual existente, migre-a para Jakarta
  Bean Validation na mesma atividade.
- Não é exigida migração retroativa de validações estruturais que não façam
  parte da alteração em andamento.

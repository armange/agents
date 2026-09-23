# Arquitetura: Application Services

## Orquestração por contexto

- Cada contexto de domínio deve ter um `<Contexto>ApplicationService` como
  ponto público de orquestração de seus casos de uso relacionados.
- Casos de uso são operações desse serviço, e não sufixos de classes ou
  interfaces. Por exemplo, `SaleApplicationService` pode expor `create`,
  `approve`, `reject` e `cancel`.
- O `ApplicationService` deve coordenar validação de entrada, resolução de
  dependências, chamadas a policies e serviços especializados, persistência
  por contratos do domínio e limites transacionais necessários ao caso de uso.
- O `ApplicationService` não deve concentrar regra de negócio; decisões de
  domínio devem ser delegadas a classes especializadas da camada de domínio.

```java
public class SaleApplicationService {

    public SaleCreatedDto create(final CreateSaleDto dto) {
        saleInputValidation.validate(dto);
        final SaleCreationReferencesDto refs = findCreationReferences(dto);

        return createSale(dto, refs);
    }
}
```

## Colaboradores especializados

- Uma etapa separada por função deve ser implementada como colaborador
  especializado na camada e no package compatíveis com sua responsabilidade.
- Um colaborador especializado não deve receber o sufixo
  `ApplicationService` apenas por participar de um caso de uso. Por exemplo,
  use `SaleInputValidation` para validar entrada e `SaleContractValidation`
  para regra de contrato.
- Um `<Ação>ApplicationService` só é permitido quando a ação representar uma
  fronteira de contexto, transação, autorização, ciclo de vida ou dependências
  realmente independentes do `<Contexto>ApplicationService` existente.

## Localização

- `ApplicationService`s devem ficar em `application.service.<contexto>`.
- `InputValidation`s devem ficar em `application.validation.<contexto>`.
- `Validation`s de regra de negócio devem ficar em
  `domain.validation.<contexto>`; policies de decisão continuam em
  `domain.policy.<contexto>`.

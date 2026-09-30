# Arquitetura: sufixos de classes

## Arquitetura base

Esta norma pressupõe a topologia de camadas deste conjunto. Antes de aplicar
suas regras, leia e aplique a base, mesmo na adoção isolada deste especialista.
O caminho abaixo é relativo a este arquivo:

- `AGENTS.architecture.layer-boundaries.md`

As regras desta norma não ampliam as responsabilidades nem as dependências
permitidas pela base. Camadas opcionais só devem existir quando necessárias
às responsabilidades do projeto.

## Referência e aplicação

- Esta norma complementa a arquitetura base, em um ou vários módulos, com a
  nomenclatura concreta de classes; não substitui responsabilidades, camadas
  ou direções de dependência já definidas.
- Esta norma define integralmente os sufixos aplicáveis, sem depender de
  ferramenta, plugin ou mecanismo de verificação.
- Um sufixo só deve ser usado quando a classe exercer a responsabilidade que
  ele representa; não crie classes ou packages apenas para satisfazer a
  nomenclatura.
- Código novo ou alterado deve seguir esta matriz. Nomes legados só devem ser
  migrados quando fizerem parte da alteração em andamento.

## Aplicação e bordas

- `<Contexto>ApplicationService` orquestra os casos de uso de um contexto.
- `<Contexto>InputValidation` dispara a validação estrutural da entrada antes
  de consultar referências ou produzir efeitos colaterais.
- `Api`, `Controller`, `Config` e `EventListener` representam as
  responsabilidades de aplicação correspondentes.
- Para novos endpoints HTTP em `application`, prefira classes `Controller` em `application.controller`. O uso de `Api` em `application.api` para essa responsabilidade é desencorajado, sem migração automática dos nomes existentes.
- `Client` representa comunicação de saída com sistema externo ou serviço
  independente.
- `Input` e `Output` representam adaptadores de integração de entrada e
  saída, respectivamente.

## Domínio e dados

- `Service` representa um contrato ou colaboração coesa do domínio, ou implementação técnica fora da orquestração de aplicação. No domínio, pode coordenar policies e outros colaboradores para executar uma operação. Pode manter decisões pequenas e inseparáveis dessa operação, mas não concentrar regras independentes.
- `Policy` representa uma decisão de negócio especializada e coesa, com significado próprio e potencial de reutilização. A decisão não precisa já ter múltiplos consumidores. Não use esse sufixo apenas porque a classe rejeita uma entrada.
- Escolha entre `Policy` e `Service` pela responsabilidade principal, não pela quantidade ou complexidade das decisões.
- `<Contexto><Regra>Validation` valida uma única regra de negócio, invariante
  ou conjunto coeso de referências já resolvidas.
- `Resolver` resolve referência, seleção ou valor conhecido sem decidir
  política de negócio.
- `Factory` cria ou inicializa modelos; `Mapper` converte representações.
- `Repository` representa contrato de repositório do domínio.
- `Dto` representa contrato de dados interno ou de cliente.
- Em `client.dto`, `RequestDto` e `ResponseDto` são finais de nome permitidos quando distinguem formatos de requisição e resposta exigidos pelo terceiro. O nome deve identificar a operação ou o provedor quando isso for necessário para evitar ambiguidade; por exemplo, `ProviderTokenRequestDto` e `ProviderTokenResponseDto`. O sufixo `Dto` continua opcional e não deve ser exigido apenas pela localização no package.
- As mesmas permissões de nome de `client.dto` valem para seus subpackages por provedor, quando usados.
- Entidades de domínio não usam o sufixo `Entity`.
- `Support`, `Command`, `Context`, `Mode`, `Names` e `Types` são sufixos
  permitidos para estruturas de suporte de domínio que exerçam exatamente a
  responsabilidade indicada.

## Persistência e infraestrutura técnica

- `JpaRepository` representa contrato ou adaptação específica de JPA;
  `Dao` representa acesso técnico a dados fora dessa abstração.
- `Entity` é exclusivo de modelo de persistência.
- `Document` representa modelo de armazenamento documental.
- `Validator` é reservado à validação técnica ou exigida por framework, como
  a validação de persistência ou uma implementação de `ConstraintValidator`.
- `Wrapper` representa um envoltório técnico ou de modelo com semântica
  própria.
- `Exception` representa uma exceção concreta.

## Implementações e proibições

- `FactoryImpl` e `MapperImpl` só podem ser usados quando a classe implementar
  interface ou classe-base real do mesmo papel.
- Não use `Impl` em classe concreta sem contrato real nem no único ponto de
  aplicação de um contexto.
- Não use `UseCase` em classes ou interfaces próprias; casos de uso são
  operações de um `ApplicationService`.
- Não use `Configuration`; o sufixo padronizado é `Config`.
- É proibido usar as combinações `PolicyService` e `ServicePolicy` em nomes de classes e interfaces, pois elas deixam ambígua a responsabilidade. Use `Policy` para uma decisão de negócio especializada e `Service` para uma colaboração ou operação coesa.

## Exemplos

```java
public class SaleApplicationService {
}

public class SaleInputValidation {
}

public final class SaleContractValidation {
}

public interface SaleRepository {
}

public interface SaleJpaRepository {
}

public class Sale {
}

public class SaleEntity {
}

public class SaleEntityValidator {
}
```

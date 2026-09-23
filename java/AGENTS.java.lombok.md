# Java: Lombok

- Esta norma só se aplica quando o projeto já estiver configurado para usar Lombok.
- Projetos configurados com Lombok devem usá-lo para getters, setters, construtores, logging com `@Slf4j` e boilerplate equivalente.
- Deve-se evitar implementação manual de boilerplate que o Lombok resolva sem necessidade técnica explícita.
- Quando `@RequiredArgsConstructor` gerar um construtor de injeção do Spring a
  partir de campo anotado com `@Qualifier`, o projeto deve configurar
  `lombok.copyableAnnotations += org.springframework.beans.factory.annotation.Qualifier`
  em `lombok.config`.
- Não se deve presumir que `@Qualifier` declarado somente no campo será
  propagado ao parâmetro do construtor gerado sem essa configuração.
- Quando a configuração de anotações copiáveis não puder ser aplicada, o
  construtor deve ser declarado explicitamente com `@Qualifier` no parâmetro.
- `@Primary` não deve ser usado para ocultar a necessidade de distinguir
  colaboradores com responsabilidades diferentes.
- Exceções permitidas: limitações de framework, serialização, herança, depuração, legibilidade ou projetos que não usem Lombok.

# Testes: Estratégia

- A implementação deve usar testes unitários sempre que a regra, decisão ou transformação puder ser validada sem infraestrutura externa.
- Regras de negócio, políticas, validadores, mappers, normalizações, decisões de fluxo e cálculos devem ser cobertos por testes unitários quando puderem ser validados sem infraestrutura externa.
- Testes integrados devem ser usados para validar comportamentos que dependem da colaboração real entre camadas, infraestrutura, banco de dados, framework, serialização, configuração, transação, migrations ou contratos HTTP.
- Não se deve repetir em testes integrados todos os cenários já cobertos por testes unitários quando um ou poucos testes integrados forem suficientes para provar a integração do fluxo.
- Uma suíte integrada deve cobrir os caminhos representativos de integração, sem substituir a responsabilidade dos testes unitários sobre as variações da regra de negócio.
- Ao adicionar ou modificar uma regra de negócio, deve-se primeiro verificar se ela pode ser testada em unidade.
- Se a regra também depender de integração real, deve-se combinar teste unitário da regra com teste integrado do fluxo principal.
- A redução de testes integrados só deve ocorrer quando houver cobertura unitária equivalente para a regra removida e permanecer pelo menos um teste integrado representativo do contrato externo ou da integração envolvida.
- Testes integrados não devem ser removidos quando forem a única cobertura de comportamento dependente de banco, migration, transação, serialização, segurança, configuração ou contrato HTTP.

## Massa de teste

- Antes de testar um `delete`, o cenário deve criar um registro novo e exclusivo para esse teste; não reutilize o mesmo registro seedado como alvo principal.
- Quando houver endpoint suficiente para montar a massa necessária, o teste deve usar endpoints do serviço para criar os dados.
- `insert` direto no banco é secundário e só deve ser usado quando não existir endpoint adequado ou quando a rota estiver inconsistente e bloquear a entrega.

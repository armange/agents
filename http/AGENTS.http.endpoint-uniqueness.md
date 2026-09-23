# HTTP: Unicidade de Endpoints e Contratos

- Não devem existir N endpoints diferentes que fazem a mesma coisa em formatos diferentes.
- Endpoints novos devem ser criados apenas quando houver diferença real de recurso, semântica, autorização, ciclo de vida, consumidor, compatibilidade versionada ou contrato público.
- Quando uma operação já existir com a mesma semântica necessária, deve-se reaproveitar esse contrato em vez de criar outro endpoint equivalente.
- Não se deve criar endpoint novo apenas para variar identificador, path, shape do payload ou nome da operação quando a semântica for a mesma de um endpoint existente.
- Não se deve induzir outro serviço a criar endpoint paralelo equivalente quando o consumidor pode reaproveitar corretamente o contrato já existente.
- Endpoints paralelos só podem existir quando houver regra explícita, documentada e justificada por versionamento, compatibilidade temporária, migração controlada, segurança, diferença real de consumidor ou outra restrição arquitetural concreta.

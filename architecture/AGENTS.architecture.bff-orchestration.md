# Arquitetura: Orquestração em BFFs

- Depende de: arquitetura em camadas, separação de responsabilidades entre BFFs e serviços internos, e definição de domínio responsável por cada operação.
- Objetivo: manter BFFs como camadas de entrada e adaptação, evitando que acumulem orquestrações que pertencem ao serviço interno dono do domínio.
- Escopo: BFFs e camadas equivalentes de gateway HTTP que chamam serviços internos do workspace Nexus.
- BFFs podem orquestrar múltiplas requisições quando a operação envolver serviços internos distintos.
- Quando uma operação exigir múltiplas leituras ou mutações dentro de um mesmo serviço interno, o serviço interno responsável deve expor uma operação agregada para atender essa necessidade.
- Sempre que viável, uma operação pública de BFF deve resultar em uma única chamada para cada serviço interno envolvido.
- Não deve: orquestrar múltiplas chamadas para o mesmo serviço interno quando essa orquestração puder ser implementada no próprio serviço interno.
- Não deve: reconstruir no BFF regras, agregações ou fluxos transacionais que pertencem ao domínio de um serviço interno.
- Exceções: chamadas adicionais técnicas e inevitáveis podem ocorrer quando forem exigidas por autenticação, autorização, observabilidade, idempotência, compatibilidade temporária ou limitação explícita de um serviço interno ainda não evoluído.
- Precedência: quando uma tecnologia externa exigir adaptação, a borda deve traduzir para o contrato do domínio; não se deve mover essa adaptação para o domínio apenas para acomodar o broker, cliente ou protocolo.
- Precedência: esta norma não autoriza BFFs a implementar regra de negócio; quando houver conflito, prevalecem as regras de negócio e limites de camada do serviço interno dono do domínio.

# Arquitetura: Adaptação Semântica pelo Domínio

## Arquitetura do projeto

Antes de aplicar esta norma, leia e aplique as instruções arquiteturais do
projeto consumidor, identificadas nos `AGENTS.md` aplicáveis e em suas
referências normativas. Use as responsabilidades e os limites de dependência
ali definidos; esta norma não exige a topologia específica deste catálogo
nem autoriza ampliar as permissões da arquitetura adotada.

## Regras

- Depende de: arquitetura em camadas, contratos do domínio e separação entre domínio e tecnologia externa.
- Objetivo: garantir que a tecnologia externa se adapte ao modelo e à semântica do domínio, e não o contrário.
- Escopo: clientes, integrações, adaptadores, gateways e quaisquer bordas que traduzam protocolos externos.
- Regra: quando houver divergência entre um protocolo ou ferramenta externa e o modelo do domínio, a tradução e a adaptação devem ocorrer na camada de borda correspondente, preservando o contrato interno do domínio.
- Não deve: remodelar o domínio para seguir limitações, convenções ou formatos do provedor externo quando existir tradução viável na borda.
- Exceções: somente quando a tecnologia impuser uma limitação objetiva e não houver tradução sem perda de semântica ou violação de contrato.
- Precedência: esta norma não altera os limites de dependência da arquitetura base; ela apenas reforça que o domínio é a referência semântica principal.

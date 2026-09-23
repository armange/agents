# Arquitetura

Este arquivo é o ponto de composição das normas derivadas de arquitetura.

Antes de analisar, revisar, planejar ou modificar código sujeito a normas derivadas de arquitetura, leia também:

- `AGENTS.architecture.semantic-adaptation.md`
- `AGENTS.architecture.business-rule-class.md`
- `AGENTS.architecture.class-placement.md`
- `AGENTS.architecture.package-topology.md`
- `AGENTS.architecture.class-coupling.md`
- `AGENTS.architecture.class-suffixes.md`
- `AGENTS.architecture.application-service.md`
- `AGENTS.architecture.bff-orchestration.md`

Uma citação deste arquivo ativa obrigatoriamente todas as normas listadas, nos
elementos arquiteturais aos quais seus escopos materiais se aplicarem.

## Composição local

- Para aplicar apenas um subconjunto, o `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para aplicar este conjunto completo, o `AGENTS.md` local deve citar este arquivo.
- Este arquivo não deve receber novas regras de arquitetura diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.
- Um `AGENTS.md` local pode especializar normas derivadas para um projeto específico, desde que não viole a arquitetura base aplicável.

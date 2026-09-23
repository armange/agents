# Arquitetura Multi-module

Este arquivo é o ponto de composição das normas de arquitetura multi-module.

## Topologia de packages

Antes de analisar, revisar, planejar ou modificar código em projeto
multi-module, leia também:

- `../AGENTS.architecture.package-topology.md`

Essa norma é requisito obrigatório para a organização de packages de todos os
módulos do projeto.

Antes de analisar, revisar, planejar ou modificar código em projeto multi-module, leia também:

- `AGENTS.architecture.multi-module.boundaries.md`
- `AGENTS.architecture.multi-module.module-types.md`
- `AGENTS.architecture.multi-module.dependencies.md`
- `AGENTS.architecture.multi-module.runtime.md`
- `AGENTS.architecture.multi-module.gradle.md`
- `AGENTS.architecture.multi-module.testing.md`

Uma citação deste arquivo ativa obrigatoriamente todas as normas listadas para
o projeto multi-module no escopo citado.

## Composição local

- Para aplicar apenas um subconjunto, o `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para aplicar este conjunto completo, o `AGENTS.md` local deve citar este arquivo.
- Este arquivo não deve receber novas regras de arquitetura multi-module diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.

# Arquitetura Multi-module

Este arquivo compõe as normas de arquitetura multi-module para projetos que
adotem a topologia de camadas e packages deste conjunto.

## Topologia de packages

Antes de analisar, revisar, planejar ou modificar código em projeto
multi-module, leia também:

- `../AGENTS.architecture.package-topology.md`

Essa norma é requisito obrigatório para a organização de packages de todos os
módulos do projeto. Sua referência normativa à arquitetura base exige ler e
aplicar os limites de camadas antes de aplicar a topologia, mesmo que a base
não seja citada diretamente pelo projeto consumidor.

Antes de analisar, revisar, planejar ou modificar código em projeto multi-module, leia também:

- `AGENTS.architecture.multi-module.boundaries.md`
- `AGENTS.architecture.multi-module.module-types.md`
- `AGENTS.architecture.multi-module.dependencies.md`
- `AGENTS.architecture.multi-module.runtime.md`
- `AGENTS.architecture.multi-module.gradle.md`
- `AGENTS.architecture.multi-module.testing.md`

Uma referência normativa a este arquivo ativa obrigatoriamente todas as normas
listadas para o projeto multi-module no escopo citado.

## Composição local

- Verifique a compatibilidade da topologia e de sua base com o projeto antes
  de adotar este agregador. A existência de vários módulos, por si só, não
  justifica aplicar o conjunto completo.
- Para aplicar apenas um subconjunto, o `AGENTS.md` local deve declarar referências normativas diretamente aos especialistas necessários.
- Para aplicar este conjunto completo, o `AGENTS.md` local deve declarar uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras de arquitetura multi-module diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.

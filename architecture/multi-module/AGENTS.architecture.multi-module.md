# Arquitetura Multi-module

Este arquivo compõe as normas de arquitetura multi-module para projetos que
adotem a topologia de camadas e packages deste conjunto.

## Topologia de packages

Antes de analisar, revisar, planejar ou modificar código ou a estrutura de
módulos em projeto multi-module, leia e aplique:

- `../AGENTS.architecture.package-topology.md`

Essa norma é requisito obrigatório para a organização de packages de todos os
módulos do projeto. Sua referência normativa à arquitetura base exige ler e
aplicar os limites de camadas antes de aplicar a topologia, mesmo que a base
não seja citada diretamente pelo projeto consumidor.

## Fronteiras e responsabilidades dos módulos

Antes de analisar, revisar, planejar ou modificar a responsabilidade de um
módulo, a localização de código entre módulos ou contratos publicados por eles,
leia e aplique:

- `AGENTS.architecture.multi-module.boundaries.md`
- `AGENTS.architecture.multi-module.module-types.md`

## Dependências entre módulos

Antes de analisar, revisar, planejar ou modificar imports entre módulos,
dependências de produção ou tipos expostos entre módulos, leia e aplique:

- `AGENTS.architecture.multi-module.dependencies.md`

## Composição de runtime

Antes de analisar, revisar, planejar ou modificar composição, configuração ou
inicialização do runtime, leia e aplique:

- `AGENTS.architecture.multi-module.runtime.md`

## Build Gradle

Antes de analisar, revisar, planejar ou modificar scripts Gradle, publicação de
dependências ou configurações de build, leia e aplique:

- `AGENTS.architecture.multi-module.gradle.md`

## Testes e verificação

Antes de analisar, revisar, planejar ou modificar testes em projeto multi-module,
ou de concluir alterações Java ou de dependências entre módulos, leia e aplique:

- `AGENTS.architecture.multi-module.testing.md`

Uma referência normativa a este arquivo ativa a topologia de packages e os
especialistas cujos critérios acima forem atendidos, inclusive suas
dependências normativas. Ao passar a trabalhar em outra responsabilidade,
reavalie esses critérios antes de atuar nela.

## Composição local

- Verifique a compatibilidade da topologia, de sua base e dos especialistas
  que os critérios possam ativar antes de adotar este agregador. A existência
  de vários módulos, por si só, não justifica adotar a topologia deste conjunto.
- Para aplicar um subconjunto fixo que este roteamento não delimite, o
  `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para usar este roteamento por atividade, o `AGENTS.md` local deve declarar
  uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras de arquitetura multi-module diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.

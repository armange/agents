# Organização de Normas AGENTS: Composição

## Processo de execução

### 1. Compor a raiz

- Crie ou ajuste o `AGENTS.md` da raiz como ponto de entrada do projeto.
- Separe as citações por título que deixe claros o tema e o escopo; não faça
  listas de referências sem um título explicativo.
- Declare como normativas as referências usadas para compor regras, com uma
  ordem explícita de leitura ou aplicação. Mantenha explicações informativas e
  exemplos identificados para que não sejam carregados como dependências.
- Mantenha a base de leitura inicial restrita às regras transversais. Para
  instruções de uma atividade específica, declare antes da referência o
  critério objetivo que exige sua leitura, inclusive nas citações transitivas.
- Inclua na composição a verificação obrigatória antes de cada novo trabalho
  e sempre que a atividade alcançar outro contexto. Declare que as novas normas
  aplicáveis devem ser lidas antes de atuar, mesmo dentro da mesma conversa.
- Todo `AGENTS.md` que citar caminhos relativos deve declarar, antes das
  citações, que os caminhos são relativos ao próprio arquivo e indicar a raiz
  do projeto como referência nominal, sem citar qualquer path.
- Cite um agregador somente quando sua base e todos os especialistas que seus
  critérios possam ativar forem compatíveis com o escopo. Se o conjunto não
  oferecer critérios suficientemente precisos, cite diretamente apenas os
  especialistas compatíveis.

Modelo de raiz para projeto multi-módulo:

```md
# Instruções do Projeto

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

## Verificação de contexto

Antes de cada novo trabalho e sempre que seu contexto mudar, verifique os
`AGENTS.md` da raiz e do caminho até os arquivos envolvidos. Leia as instruções
aplicáveis e suas referências obrigatórias antes de atuar na área. As seções
abaixo indicam quando carregar cada conjunto; a verificação é obrigatória
mesmo que outro trabalho já tenha sido realizado nesta conversa.

## Normas globais e de projetos

Antes de analisar, revisar, planejar ou modificar este projeto, leia também:

- `../.agents/global/AGENTS.global.md`
- `../.agents/projects/AGENTS.projects.md`

## Documentação Markdown

Antes de modificar documentação Markdown deste projeto, leia também:

- `../.agents/readme/AGENTS.markdown.md`

## Nomenclatura de código

Antes de analisar, revisar, planejar ou modificar código de qualquer linguagem
neste projeto, leia e aplique:

- `../.agents/coding/AGENTS.coding.suffixes.md`

## Arquitetura multi-módulo

Antes de modificar módulos, dependências entre módulos ou build Gradle, leia
também:

- `../.agents/architecture/multi-module/AGENTS.architecture.multi-module.dependencies.md`
- `../.agents/architecture/multi-module/AGENTS.architecture.multi-module.gradle.md`
```

- O modelo é apenas uma estrutura. A lista final deve conter somente normas que
  a análise classificou como aplicáveis ao projeto.

### 2. Compor árvores de código e teste

- Em uma árvore Java que não precise da composição completa de Java, cite
  diretamente os especialistas de codificação e Java necessários.
- Quando `src/AGENTS.md` já compuser as normas Java, os `AGENTS.md` de
  subdiretórios de teste devem acrescentar somente as normas próprias de teste,
  sem repetir a composição Java herdada.
- Em testes Java, acrescente as normas de testes ao conjunto Java. Recursos de
  teste devem receber, por referências com critérios explícitos em
  `src/AGENTS.md` ou na composição raiz, apenas as normas relacionadas a
  fixtures, mensagens ou outros recursos presentes. Não crie composições
  dentro dos diretórios de recursos.

Modelo para `modulo/src/AGENTS.md`:

```md
# Instruções Java

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

Antes de analisar, revisar, planejar ou modificar código Java nesta pasta, leia
também:

- `../../../.agents/coding/AGENTS.coding.md`
- `../../../.agents/java/AGENTS.java.methods.md`
- `../../../.agents/java/AGENTS.java.control-flow.md`
- `../../../.agents/java/AGENTS.java.method-chaining.md`
- `../../../.agents/java/AGENTS.java.naming.md`
- `../../../.agents/java/AGENTS.java.lombok.md`
```

Modelo para `modulo/src/test/java/AGENTS.md`:

```md
# Instruções de Testes Java

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

Antes de analisar, revisar, planejar ou modificar testes Java nesta pasta, leia
também:

- `../../../../../.agents/tests/AGENTS.tests.md`
```

- Os caminhos relativos dos modelos devem ser recalculados a partir do arquivo
  que os cita; nunca copie um caminho sem verificar se ele resolve no projeto
  de destino.
- Valide também se cada `AGENTS.md` com citações relativas declara a referência
  nominal exigida para orientar a resolução dos caminhos, sem incluir paths.

### 3. Especializar por responsabilidade técnica

- Crie um `AGENTS.md` em um package filho quando ele for uma fronteira técnica
  identificável e tiver normas adicionais próprias.
- Cite especialistas diretamente quando a fronteira usar apenas uma parte do
  conjunto que o agregador não delimite por critérios objetivos.

Modelo para um package de adaptadores HTTP de exceções:

```md
# Instruções de Exposição HTTP

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

Antes de modificar adaptadores HTTP de exceções nesta pasta, leia também:

- `../../../../.agents/exceptions/AGENTS.exceptions.interpretation.md`
- `../../../../.agents/exceptions/AGENTS.exceptions.logging.md`
- `../../../../.agents/exceptions/AGENTS.exceptions.http-exposure.md`
```

Modelo para `modulo/src/AGENTS.md` quando o escopo exigir apenas normas de
bundles de mensagens. Se já houver composição Java nesse arquivo, incorpore
a seção de recursos ao arquivo existente:

```md
# Instruções de Recursos

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

## Recursos internacionalizados

Antes de analisar, revisar, planejar ou modificar bundles de mensagens em
`main/resources` ou `test/resources` e suas subpastas, relativos a este
arquivo, leia também:

- `../../../.agents/i18n/AGENTS.i18n.messages.md`
```

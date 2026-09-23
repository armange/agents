# Organização de Normas AGENTS em Projetos

## Objetivo e escopo

- Esta norma define como analisar, planejar, executar e validar a organização
  de arquivos `AGENTS.md` e `AGENTS.*.md` em projetos novos ou existentes.
- O objetivo é aplicar a cada diretório somente as normas úteis ao seu conteúdo
  e às suas subpastas, reduzindo contexto desnecessário sem perder regras
  obrigatórias.
- Esta norma complementa `AGENTS.agents.specialized-files.md`. Aquele arquivo
  define como normas e composições devem ser estruturadas; este arquivo define
  o processo para aplicar essa estrutura com segurança.
- O processo se aplica tanto ao reaproveitamento de normas existentes quanto à
  criação de novas normas especialistas.

## Conceitos obrigatórios

- `AGENTS.*.md` é uma norma especialista: deve cobrir um único assunto
  normativo reutilizável, como Java, testes, i18n, configuração, HTTP ou uma
  regra arquitetural específica.
- `AGENTS.md` é um ponto local de composição: seleciona as normas especialistas
  aplicáveis ao diretório em que está localizado e às suas subpastas.
- Uma especialização local é uma regra adicional do projeto, módulo ou package.
  Ela deve declarar escopo e precedência de forma explícita e não pode
  contradizer uma norma superior.
- A existência de uma norma central não ativa sua aplicação. Ela só se torna
  obrigatória quando um `AGENTS.md` local a cita, respeitado o escopo material
  declarado na própria norma.
- Arquivos de plano operacional e relatórios não são normas permanentes. Devem
  seguir suas regras de nomenclatura e localização próprias, sem serem usados
  para substituir um `AGENTS.md` de composição.

## Processo de análise

### 1. Descobrir o contexto antes de propor arquivos

- Leia todos os `AGENTS.md` e `AGENTS.*.md` aplicáveis, inclusive as citações
  transitivas, antes de decidir a distribuição.
- Inspecione a raiz do projeto, o build, os módulos, linguagens, frameworks,
  diretórios `src/main`, `src/test`, recursos, documentação e configurações.
- Identifique o tipo do projeto: serviço HTTP, biblioteca, ferramenta,
  migration, plugin ou outro tipo equivalente.
- Compare prioritariamente com projetos de mesma natureza. Uma biblioteca deve
  usar outras bibliotecas como referência principal; um serviço HTTP deve usar
  outros serviços HTTP.
- Ignore diretórios `done/` na raiz dos projetos durante a análise, pois eles
  não representam o estado atual.

### 2. Inventariar normas e compatibilidade

- Faça uma matriz para cada norma candidata com uma das decisões: `aplicar`,
  `aplicar em subdiretório` ou `não aplicar`.
- Registre a evidência da decisão: tecnologia presente, tipo de arquivo,
  responsabilidade do módulo, protocolo implementado ou condição material da
  própria norma.
- Não aplique uma norma apenas porque o projeto usa a mesma linguagem. Por
  exemplo, uma biblioteca Java sem fronteira HTTP não deve receber normas de
  endpoints, `PUT`/`PATCH`, autoria da requisição ou auditoria persistida.
- Não aplique uma arquitetura de serviço a uma biblioteca quando ela pressupor
  camadas, packages ou responsabilidades que a biblioteca não adota.
- Quando uma norma for parcialmente compatível, cite somente os especialistas
  que correspondem ao caso real, em vez do arquivo agregador que ativaria temas
  não aplicáveis.

Exemplo de matriz para uma biblioteca Java multi-módulo:

| Norma | Decisão | Local de aplicação | Evidência |
| --- | --- | --- | --- |
| Codificação e Java | aplicar | `src` ou package de produção | há código Java |
| Testes | aplicar em subdiretório | `src/test/java` e recursos de teste | há testes e fixtures |
| i18n | aplicar em subdiretório | package de resolver e bundles | há resolver e `.properties` |
| Exposição HTTP | aplicar em subdiretório | package de adaptadores HTTP | há advice/handler HTTP |
| Endpoints HTTP | não aplicar | nenhum | a biblioteca não expõe endpoints próprios |
| Arquitetura multi-módulo | aplicar | raiz | o Gradle declara módulos e dependências |

### 3. Escolher a granularidade

- Coloque na raiz somente normas transversais ao projeto: operação global,
  identificação multiprojeto, documentação e fronteiras entre módulos.
- Em projetos Java, `src/main` e `src/main/java` devem conter apenas packages
  e classes de produção; não crie `AGENTS.md` nesses diretórios.
- Para normas Java comuns a toda a árvore de fontes, use `src/AGENTS.md`.
  Quando a norma tiver escopo menor, use um `AGENTS.md` dentro do package de
  produção correspondente.
- Coloque normas de testes em `src/test`, `src/test/java` ou em um módulo de
  testes, nunca na árvore principal quando elas não forem úteis ali.
- Coloque normas de recursos em `src/main/resources` ou `src/test/resources`
  apenas quando houver recursos do assunto, como bundles i18n ou fixtures.
- Coloque normas de HTTP somente na fronteira que implementa HTTP, como
  `api`, `controller`, `web`, `rest` ou outro package equivalente.
- Coloque normas de configuração somente onde são criadas ou mantidas
  configurações do projeto.
- Não crie `AGENTS.md` em diretório vazio, módulo agregador sem conteúdo ou
  pasta que não tenha uma responsabilidade diferente da pasta ancestral.
- Evite repetir uma composição em packages filhos quando ela já é integralmente
  aplicável por herança. Crie o arquivo filho apenas para acrescentar ou
  restringir normas em razão de uma responsabilidade específica.

## Processo de execução

### 1. Compor a raiz

- Crie ou ajuste o `AGENTS.md` da raiz como ponto de entrada do projeto.
- Separe as citações por título que deixe claros o tema e o escopo; não faça
  listas de referências sem um título explicativo.
- Todo `AGENTS.md` que citar caminhos relativos deve declarar, antes das
  citações, que os caminhos são relativos ao próprio arquivo e indicar a raiz
  do projeto como referência nominal, sem citar qualquer path.
- Cite normas agregadoras somente quando todas as suas normas filhas forem
  pertinentes ao escopo. Caso contrário, cite exclusivamente os especialistas
  compatíveis.

Modelo de raiz para projeto multi-módulo:

```md
# Instruções do Projeto

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

## Normas globais e de projetos

Antes de analisar, revisar, planejar ou modificar este projeto, leia também:

- `../.agents/global/AGENTS.global.md`
- `../.agents/projects/AGENTS.projects.md`

## Documentação Markdown

Antes de modificar documentação Markdown deste projeto, leia também:

- `../.agents/readme/AGENTS.markdown.md`

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
  teste devem receber apenas as normas relacionadas a fixtures, mensagens ou
  outros recursos presentes.

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
- Cite especialistas diretamente em vez de agregadores quando a fronteira usar
  apenas uma parte do conjunto.

Modelo para um package de adaptadores HTTP de exceções:

```md
# Instruções de Exposição HTTP

Antes de modificar adaptadores HTTP de exceções nesta pasta, leia também:

- `../../../../.agents/exceptions/AGENTS.exceptions.interpretation.md`
- `../../../../.agents/exceptions/AGENTS.exceptions.logging.md`
- `../../../../.agents/exceptions/AGENTS.exceptions.http-exposure.md`
```

Modelo para bundles de mensagens:

```md
# Instruções de Recursos Internacionalizados

Antes de modificar bundles de mensagens nesta pasta, leia também:

- `../../../../../.agents/i18n/AGENTS.i18n.messages.md`
```

## Criação e evolução de normas especialistas

- Antes de criar uma nova norma, procure uma norma existente que já cubra o
  assunto ou que possa ser citada diretamente sem alterar sua semântica.
- Crie uma nova norma especialista somente quando houver uma regra reutilizável
  e coesa que não pertença a nenhum especialista existente.
- O nome deve identificar domínio e assunto, no formato
  `AGENTS.<dominio>.<assunto>.md`. Exemplos: `AGENTS.i18n.fallback.md` e
  `AGENTS.http.idempotency.md`.
- A nova norma deve declarar objetivo, escopo material, regras, exceções e
  precedência quando necessária. Não misture um tutorial de Java, regras HTTP
  e regras de testes no mesmo arquivo.
- Atualize um arquivo agregador somente se todos os consumidores que citam esse
  agregador realmente devem receber a nova norma. Caso contrário, mantenha a
  nova norma independente e cite-a apenas nos pontos locais adequados.
- Não altere normas compartilhadas para acomodar uma exceção de um único
  projeto. Crie uma especialização local clara quando a exceção for legítima.
- Ao alterar uma norma compartilhada, reavalie todas as composições que a citam
  direta ou transitivamente e informe os projetos potencialmente afetados antes
  de concluir a atividade.

## Validação e aceite

- Verifique que cada citação em todos os novos ou alterados `AGENTS.md` aponta
  para arquivo existente a partir do diretório que a contém.
- Verifique que cada `AGENTS.md` com caminhos relativos declara que eles são
  relativos ao próprio arquivo e inclui a raiz do projeto como referência
  nominal, sem incluir path.
- Verifique a cadeia transitiva das normas agregadoras para garantir que ela não
  introduz temas incompatíveis no diretório local.
- Revise ao menos um exemplo representativo de cada escopo criado: raiz,
  código principal, testes, recursos e uma fronteira técnica especializada.
- Confirme que nenhuma norma de protocolo, banco, framework ou teste foi
  posicionada em árvore que não contenha essa responsabilidade.
- Confirme que diretórios vazios e módulos puramente agregadores não receberam
  instruções redundantes.
- Inspecione os arquivos diretamente no filesystem. Arquivos de instrução podem
  ser ignorados pelo git, portanto a ausência no `git status` ou `git diff` não
  é evidência de que a alteração não existe.
- Documente no fechamento quais normas foram aplicadas, quais foram excluídas
  por incompatibilidade e quais validações estruturais foram executadas.

## Critério de resultado

- Um projeto está organizado quando uma pessoa ou IA consegue começar por seu
  `AGENTS.md` raiz, seguir as citações aplicáveis e encontrar em cada pasta
  somente as normas necessárias para modificar seu conteúdo corretamente.
- A redução de contexto deve vir da composição precisa, e nunca da omissão de
  uma norma materialmente aplicável.

# Organização de Normas AGENTS em Projetos

## Objetivo e escopo

- Esta norma define como analisar, planejar, executar e validar a organização
  de arquivos `AGENTS.md` e `AGENTS.*.md` em projetos novos ou existentes.
- O objetivo é aplicar a cada diretório somente as normas úteis ao seu conteúdo
  e às suas subpastas, reduzindo contexto desnecessário sem perder regras
  obrigatórias.
- Referência informativa: `AGENTS.agents.specialized-files.md` apresenta a
  estrutura das normas e composições. Este guia descreve o processo de
  organização; esta menção não exige leitura nem ativa o outro documento.
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
  obrigatória por referência normativa de uma composição local aplicável,
  direta ou transitiva, quando o trabalho atende ao escopo declarado para a
  referência, respeitado também o escopo material da norma.
- A composição local deve permitir que, antes de cada novo trabalho ou mudança
  de contexto, a IA verifique obrigatoriamente quais instruções precisa ler.
  A verificação parte da raiz e percorre os `AGENTS.md` aplicáveis até a área
  envolvida, antes de analisar, revisar, planejar ou modificar seu conteúdo.
- Arquivos de plano operacional e relatórios não são normas permanentes. Devem
  seguir suas regras de nomenclatura e localização próprias, sem serem usados
  para substituir um `AGENTS.md` de composição.

## Tipos de referência na composição

- Para ativar uma norma, escreva uma ordem explícita de leitura ou aplicação,
  como "leia também", "leia e aplique" ou "aplique", antes do arquivo ou da
  lista de arquivos. Declare o contexto em que essa referência normativa vale.
- Para apresentar documentação complementar, identifique a referência como
  informativa. Sua leitura é opcional e não ativa regras. Um nome ou link sem
  ordem de leitura ou aplicação não é suficiente para compor normas.
- Identifique modelos e nomes ilustrativos como exemplos. As ordens dentro
  desses trechos não ativam normas neste guia; quando adotadas como instruções
  no projeto de destino, passam a valer no escopo da composição local.
- Os blocos de modelos deste guia e os exemplos de nomes de novas normas são
  ilustrativos. Os caminhos de um modelo adotado devem ser ajustados e validados
  no projeto de destino; nomes hipotéticos não precisam existir neste repositório.
- Uma dependência necessária deve ser normativa. Não use a classificação
  informativa ou de exemplo para dispensar uma obrigação real.

## Processo de análise

### 0. Inicializar um projeto sem composição raiz

- Verifique se o projeto possui `AGENTS.md` na raiz. Se já existir, carregue
  sua composição aplicável e prossiga com a análise normal.
- Se não existir e o usuário tiver solicitado criar ou organizar os AGENTS,
  realize a análise inicial e a criação das composições sem exigir um arquivo
  raiz prévio nem nova confirmação para a mesma organização já solicitada.
- Leia as instruções existentes aplicáveis, inclusive as de pastas ancestrais
  e subdiretórios. A ausência da composição raiz não suspende essas instruções.
- Limite a inspeção de estrutura, build, configurações e conteúdo à identificação
  das tecnologias e responsabilidades necessárias para distribuir as normas.
  Use as etapas seguintes para selecionar normas e criar composições com
  referências normativas, critérios de carregamento e escopos explícitos.
- O pedido de inicialização autoriza organizar os AGENTS. Trabalhos funcionais
  dependem de autorização correspondente e só devem começar depois de validar
  e carregar as composições criadas e suas referências aplicáveis.
- Sem pedido de criação ou organização dos AGENTS, informe a ausência e
  solicite a inicialização antes de prosseguir com o trabalho no projeto.

### 1. Descobrir o contexto antes de propor arquivos

- Leia todos os `AGENTS.md` e `AGENTS.*.md` aplicáveis, inclusive suas referências
  normativas transitivas, antes de decidir a distribuição.
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
- Para cada norma arquitetural candidata, verifique também os pré-requisitos
  normativos transitivos e sua compatibilidade com a arquitetura adotada.
  Especialistas que pressupõem uma topologia devem citar sua base como leitura
  obrigatória, inclusive para adoção isolada. Normas reutilizáveis entre
  arquiteturas devem seguir explicitamente a arquitetura do projeto consumidor.
- Não selecione um especialista cuja base seja incompatível nem omita seus
  pré-requisitos para adaptá-lo ao projeto. A existência de módulos ou o uso de
  uma linguagem não implica adoção de uma topologia de camadas.
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
| Dependências entre módulos e build Gradle | aplicar | raiz | o Gradle declara módulos e dependências; especialistas selecionados sem pressupor a topologia do agregador completo |

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
- Cite normas agregadoras somente quando todas as suas normas filhas forem
  pertinentes ao escopo. Caso contrário, cite exclusivamente os especialistas
  compatíveis.

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

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

Antes de modificar adaptadores HTTP de exceções nesta pasta, leia também:

- `../../../../.agents/exceptions/AGENTS.exceptions.interpretation.md`
- `../../../../.agents/exceptions/AGENTS.exceptions.logging.md`
- `../../../../.agents/exceptions/AGENTS.exceptions.http-exposure.md`
```

Modelo para bundles de mensagens:

```md
# Instruções de Recursos Internacionalizados

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

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
- Ao alterar uma norma compartilhada, reavalie as composições que a referenciam
  normativamente, direta ou transitivamente, e informe os projetos potencialmente
  afetados antes de concluir a atividade. Confira também as explicações e os
  exemplos que descrevam a regra alterada para manter a documentação coerente.

## Validação e aceite

- Ao manter este catálogo, execute `python3 scripts/validate_agents.py` na raiz
  do repositório para conferir referências, modelos, ciclos, repetições e volume
  potencial das composições. O comando usa arquivos do disco, mesmo ignorados
  pelo Git. Corrija os erros e revise os avisos antes de concluir a manutenção.
- Referência informativa: [uso e limites do verificador](../README.md#4-validação-automática).
  A verificação automática complementa a revisão abaixo; não decide critérios
  de contexto nem compatibilidade semântica das normas. Projetos consumidores
  podem usar o script do catálogo com `--root` apontando para a raiz comum das
  normas, sem precisar copiá-lo para cada projeto.

- Em uma inicialização, confirme que a composição raiz foi criada e que ela e
  as composições locais aplicáveis foram carregadas antes de qualquer outro
  trabalho solicitado. A descoberta inicial deve ter servido à organização
  das instruções e preservado as regras já existentes nos diretórios envolvidos.
- Verifique que cada referência normativa nos arquivos novos ou alterados aponta
  para arquivo existente a partir do diretório que a contém. Referências
  informativas a documentos reais devem ser corretas; nomes hipotéticos em
  exemplos não devem ser tratados como dependências ausentes.
- Verifique que cada `AGENTS.md` com caminhos relativos declara que eles são
  relativos ao próprio arquivo e inclui a raiz do projeto como referência
  nominal, sem incluir path.
- Confira que a adoção isolada de cada especialista arquitetural alcança sua
  base obrigatória e que normas independentes de uma topologia não a importam
  sem necessidade. Normas derivadas não ampliam permissões da base nem exigem
  materializar camadas opcionais sem responsabilidade real.
- Verifique a cadeia transitiva das normas agregadoras para garantir que ela não
  introduz temas incompatíveis no diretório local.
- Resolva os caminhos das referências normativas, incluindo links simbólicos,
  e identifique ciclos e dependências repetidas. Durante a leitura, um retorno
  a um arquivo em leitura encerra apenas a repetição; as demais dependências
  continuam obrigatórias. Referências informativas não integram essa cadeia.
- Confira que uma leitura anterior só é reaproveitada com conteúdo integral
  disponível e versão atual confirmada. Cada novo trabalho ou contexto exige
  reavaliar as referências do arquivo, mesmo quando ele não precisa ser relido.
- Verifique que a composição exige nova avaliação de contexto antes de cada
  trabalho e durante mudanças de escopo, com leitura prévia das novas normas.
- Confira um cenário restrito a uma atividade e outro que passe a envolver uma
  segunda área. No primeiro, referências fora do escopo devem aguardar; no
  segundo, suas instruções devem ser carregadas antes da nova atividade.
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
  `AGENTS.md` raiz, seguir as referências normativas aplicáveis e encontrar em
  cada pasta somente as normas necessárias para modificar seu conteúdo corretamente.
- A redução de contexto deve vir da composição precisa, e nunca da omissão de
  uma norma materialmente aplicável.

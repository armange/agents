# Organização de Normas AGENTS: Análise

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
  que correspondem ao caso real, em vez de um agregador cuja base ou cujos
  critérios ativariam temas não aplicáveis.

Exemplo de matriz para uma biblioteca Java multi-módulo:

| Norma | Decisão | Local de aplicação | Evidência |
| --- | --- | --- | --- |
| Codificação e Java | aplicar | `src` ou package de produção | há código Java |
| Avaliação de sufixos | aplicar | raiz, com critério para código | há código em qualquer linguagem; sufixo não é obrigatório |
| Testes | aplicar em subdiretório | `src/test/java` para código; `src/AGENTS.md` com critério para recursos de teste | há testes e fixtures |
| i18n | aplicar em subdiretório | package de resolver; `src/AGENTS.md` com critério para bundles | há resolver e `.properties` |
| Exposição HTTP | aplicar em subdiretório | package de adaptadores HTTP | há advice/handler HTTP |
| Endpoints HTTP | não aplicar | nenhum | a biblioteca não expõe endpoints próprios |
| Dependências entre módulos e build Gradle | aplicar | raiz | o Gradle declara módulos e dependências; especialistas selecionados sem pressupor a topologia do agregador completo |

### 3. Escolher a granularidade

- Coloque na raiz somente normas transversais ao projeto: operação global,
  identificação multiprojeto, documentação e fronteiras entre módulos.
  Normas de recursos também podem ser referenciadas na raiz, desde que tenham
  critérios explícitos restritos aos recursos correspondentes.
- Em projetos com código, cite `AGENTS.coding.suffixes.md` na raiz com critério
  para código de qualquer linguagem. Se a citação ficar em composições locais,
  confirme que todas as árvores de código estejam cobertas.
- Em projetos Java, `src/main` e `src/main/java` devem conter apenas packages
  e classes de produção; não crie `AGENTS.md` nesses diretórios.
- Para normas Java comuns a toda a árvore de fontes, use `src/AGENTS.md`.
  Quando a norma tiver escopo menor, use um `AGENTS.md` dentro do package de
  produção correspondente.
- Coloque normas de testes em `src/test`, `src/test/java` ou em um módulo de
  testes, nunca na árvore principal quando elas não forem úteis ali.
- Não crie nem mantenha `AGENTS.md` ou `AGENTS.*.md` em
  `src/main/resources`, `src/test/resources` ou suas subpastas. A proibição
  também vale para outros diretórios configurados como recursos no build,
  para evitar que instruções de agentes sejam incluídas nos artefatos.
- Declare as referências normativas de recursos em `src/AGENTS.md` ou no
  `AGENTS.md` da raiz, fora dos diretórios de recursos. Use critérios explícitos
  de diretório, tipo de arquivo ou atividade para bundles i18n, configurações,
  fixtures e outros recursos presentes, sem ativar essas normas para toda a
  árvore. Não use exclusões no build como substituto dessa organização.
- Coloque normas de HTTP somente na fronteira que implementa HTTP, como
  `api`, `controller`, `web`, `rest` ou outro package equivalente.
- Coloque normas de configuração somente onde são criadas ou mantidas
  configurações do projeto. Para configurações em diretórios de recursos,
  use a composição ancestral com critérios de escopo descrita acima.
- Não crie `AGENTS.md` em diretório vazio, módulo agregador sem conteúdo ou
  pasta que não tenha uma responsabilidade diferente da pasta ancestral.
- Evite repetir uma composição em packages filhos quando ela já é integralmente
  aplicável por herança. Crie o arquivo filho apenas para acrescentar ou
  restringir normas em razão de uma responsabilidade específica.

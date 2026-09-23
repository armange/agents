# agents

Este repositório reúne instruções reutilizáveis para orientar o trabalho de agentes de IA em projetos de software. Cada arquivo `AGENTS.*.md` trata de um tema específico e pode ser citado por um projeto que queira adotar suas regras.

## Sumário

- [1 Como funciona](#1-como-funciona)
- [2 Como usar em outro projeto](#2-como-usar-em-outro-projeto)
  - [2.1 Prompt sugerido para projetos novos](#21-prompt-sugerido-para-projetos-novos)
- [3 Organização](#3-organização)
- [4 Validação automática](#4-validação-automática)
- [5 Licença](#5-licença)

## 1 Como funciona

[Voltar ao sumário](#sumário)

As instruções são organizadas por assunto, como arquitetura, codificação, Java, HTTP, testes e documentação. Alguns arquivos são **especialistas** e definem regras de um tema restrito. Outros, como `coding/AGENTS.coding.md`, **compõem um conjunto** de especialistas relacionados.

Cada projeto escolhe as instruções pertinentes ao seu contexto e declara referências normativas no `AGENTS.md` da pasta em que devem valer. A referência normativa a um arquivo de composição inclui também suas dependências normativas aplicáveis. Uma instrução presente neste repositório não se aplica automaticamente a outros projetos; depois de ativada, deve ser seguida no escopo correspondente.

Antes de cada novo trabalho, a IA deve obrigatoriamente verificar os `AGENTS.md` da raiz e dos diretórios envolvidos. A base é de leitura obrigatória; conjuntos com critérios explícitos são carregados quando a atividade os exige, incluindo suas dependências aplicáveis. Se o contexto mudar durante o trabalho, a verificação deve ser repetida e as novas instruções devem ser lidas antes de atuar na nova área, mesmo na mesma conversa.

As referências podem ter três funções no mesmo documento:

- **Normativa:** uma ordem como "leia também" ou "leia e aplique" exige a leitura e o cumprimento do arquivo no contexto indicado.
- **Informativa:** apresenta documentação complementar; a leitura é opcional e não ativa regras. Um nome ou link isolado também não ativa normas.
- **Exemplo ou menção:** ilustra nomes ou modelos, sem exigir leitura nem existência dos arquivos. As ordens de um modelo passam a valer quando adotadas como instruções no projeto de destino.

Em composições existentes, listas de caminhos usadas como dependências devem ter uma ordem explícita de leitura ou aplicação. As formas "leia também" e "aplique" já usadas neste repositório continuam normativas.

Ao encontrar uma referência circular, o agente encerra somente a repetição e continua as demais dependências. Uma leitura anterior só pode ser reaproveitada com o conteúdo integral disponível e a versão atual confirmada; cada novo trabalho continua exigindo verificar quais normas se aplicam.

## 2 Como usar em outro projeto

[Voltar ao sumário](#sumário)

Referência informativa: o [guia de organização dos AGENTS](agents/AGENTS.agents.organization.md)
descreve como analisar o projeto, selecionar normas compatíveis, distribuí-las
entre a raiz e os subdiretórios e validar as composições.

Se o projeto ainda não possui `AGENTS.md` na raiz, solicite a criação ou organização das instruções de agentes. Esse pedido permite à IA inspecionar o projeto para selecionar as normas e criar as composições. Ao concluir a distribuição, ela deve validar e carregar as instruções antes de iniciar outros trabalhos já solicitados.

### 2.1 Prompt sugerido para projetos novos

[Voltar ao sumário](#sumário)

> **Para começar:** disponibilize o catálogo à IA, copie o prompt abaixo e
> substitua `[caminho do repositório agents]` pela localização do catálogo.

Este é um exemplo de solicitação para usar no projeto de destino:

```text
Organize as instruções de IA deste projeto usando o catálogo de normas em
[caminho do repositório agents].

Leia e aplique o guia agents/AGENTS.agents.organization.md do catálogo.

Analise a estrutura, as tecnologias, o tipo de projeto e as responsabilidades
existentes. Se o projeto ainda estiver vazio, use os requisitos disponíveis
e pergunte apenas pelas definições indispensáveis que estiverem faltando.

Crie o AGENTS.md raiz e distribua composições locais onde houver necessidade,
respeitando as instruções existentes.

Requisitos:
- Selecione somente normas compatíveis com o projeto, incluindo seus
  pré-requisitos obrigatórios.
- Use referências normativas explícitas aos especialistas, sem copiar
  seu conteúdo.
- Declare caminhos relativos ao arquivo que faz a referência e valide-os.
- Mantenha na raiz as normas transversais e condicione as demais ao contexto
  em que são necessárias.
- Exija que, antes de cada novo trabalho ou mudança de contexto, a IA
  verifique e leia todas as novas instruções aplicáveis.
- Para Java, inclua as normas de coesão de classes e responsabilidade única
  por operação.
- Avalie a arquitetura antes de adotar normas que pressuponham uma
  topologia específica.
- Evite composições redundantes e a criação de diretórios sem necessidade.

Valide as composições criadas com o verificador do catálogo, quando disponível,
e revise manualmente sua compatibilidade e seus critérios de aplicação.

Ao concluir, informe os arquivos criados, as normas selecionadas, as exclusões
relevantes e o resultado da validação. Limite as alterações à organização das
instruções de IA.
```

### 2.2 Exemplo de composição manual

Disponibilize este repositório em um local acessível ao projeto, por exemplo, na pasta `.agents/` da sua raiz. Em seguida, crie ou edite o `AGENTS.md` do projeto para indicar quais instruções o agente deve ler:

```md
# Instruções do projeto

As referências abaixo são relativas a este arquivo. Como ponto de referência,
considere a raiz do projeto.

## Verificação de contexto

Antes de cada novo trabalho e sempre que seu contexto mudar, verifique os
AGENTS.md da raiz e do caminho até os arquivos envolvidos. Leia as instruções
aplicáveis e suas referências obrigatórias antes de atuar, mesmo que já tenha
realizado outro trabalho nesta conversa.

## Simplicidade do código

Antes de analisar ou modificar código, leia também:

- `.agents/coding/AGENTS.coding.simplicity.md`
```

O caminho do exemplo é relativo ao `AGENTS.md` do projeto. Ajuste-o conforme a localização dos arquivos. Para adotar todas as regras de um assunto, declare uma referência normativa ao arquivo de composição; para adotar apenas algumas, faça isso diretamente para os especialistas desejados. Siga também as dependências normativas aplicáveis dos arquivos escolhidos. O bloco acima é um modelo ilustrativo e não ativa suas referências neste README.

Na adoção de arquitetura, confira a compatibilidade dos pré-requisitos com o
projeto. O [agregador de arquitetura](architecture/AGENTS.architecture.md) exige
ler a base de limites de camadas antes das normas derivadas. Os especialistas
que dependem dessa topologia também citam a base, inclusive para uso isolado.
O agregador multi-módulo a inclui pela norma de packages. Adaptação semântica,
localização de classes e orquestração de BFF podem seguir a arquitetura do
projeto consumidor. A adoção das normas não exige criar camadas vazias.

## 3 Organização

[Voltar ao sumário](#sumário)

As pastas agrupam as instruções por tema. Além das áreas de código e arquitetura, há normas para exceções, internacionalização, configuração, validação, auditoria e organização dos próprios arquivos `AGENTS`. Os arquivos em `global/` e `projects/` contêm regras de operação, identificação e versionamento que podem ser adotadas conforme o contexto.

Referência informativa: o [especialista em conhecimento de projetos reais](projects/AGENTS.projects.known-projects.md) preserva o catálogo, os aliases e as convenções de um conjunto específico de projetos. Sua adoção exige referência normativa explícita no `AGENTS.md` local dos projetos abrangidos; os agregadores genéricos não o carregam automaticamente.

## 4 Validação automática

[Voltar ao sumário](#sumário)

Requer Python 3.9 ou superior, sem dependências externas. Na raiz deste
repositório, execute:

```bash
python3 scripts/validate_agents.py
```

O [verificador](scripts/validate_agents.py) lê os arquivos diretamente do disco,
inclusive os ignorados pelo Git. Analisa `AGENTS.md`, `AGENTS.*.md` e os modelos
em arquivos `README.md`. Ignora diretórios `.git`, `.codex`, `.venv`,
`__pycache__`, `node_modules` e `done`; não percorre diretórios simbólicos.
Arquivos simbólicos são identificados pelo destino, evitando contagem duplicada.

Ele verifica destinos locais de referências normativas e informativas,
identifica ciclos e dependências repetidas e confere declarações de caminhos
relativos nos `AGENTS.md` e modelos de composição. Modelos também precisam de
título principal e blocos de código fechados. Caminhos ilustrativos não precisam
existir no catálogo; sua resolução deve ser conferida no projeto de destino.

A classificação reconhece caminhos entre crases ou em links Markdown diretos,
ordens como “leia”, “aplique” e “siga as regras de”, o marcador “Referência
informativa” e exemplos identificados por “Exemplo:” ou seções “Exemplos” e
“Modelos”. Uma ordem introdutória vale para a lista seguinte e pode abranger
subseções, como no agregador Java. Blocos cercados por crases ou tils são
ilustrativos; modelos de composição usam a linguagem `md` ou `markdown`.
Nomes isolados em prosa são menções, sem exigência de existência.

O relatório mostra arquivos únicos, palavras e caracteres por composição,
incluindo o próprio arquivo e todas as dependências normativas transitivas.
Esse é o **volume potencial do conjunto**, considerando todas as condições de
carregamento. Não representa os tokens consumidos numa tarefa nem determina
quais condições se aplicam a ela.

| Resultado | Tratamento |
| --- | --- |
| Destino local ausente, arquivo ilegível ou modelo inconsistente | erro; saída `1` |
| Ciclo ou dependência repetida/compartilhada | aviso; saída `0` se não houver erros |
| Referência remota | aviso; não consultada pela ferramenta |
| Nenhum arquivo AGENTS ou raiz inexistente | erro; saída `1` |
| Argumento de linha de comando inválido | saída `2` |

Para obter detalhes das referências, com classificação e linha de origem:

```bash
python3 scripts/validate_agents.py --json
```

Para validar outra árvore, informe uma raiz que contenha todas as normas
referenciadas. Referências que saiam dessa raiz são reportadas como erro:

```bash
python3 scripts/validate_agents.py --root /caminho/da/arvore
```

A análise segue o formato descrito acima, sem interpretar Markdown completo ou
linguagem natural arbitrária. Links por identificador, caminhos sem crases e
outras formulações de ordens exigem revisão manual. A ferramenta não valida
compatibilidade arquitetural, precedência semântica nem o comportamento real da
IA. A revisão dos critérios de contexto continua obrigatória.

Os testes usam catálogos temporários com destinos ausentes, ciclos, referências
compartilhadas, modelos, links simbólicos e arquivos ignorados pelo Git:

```bash
python3 -B -m unittest discover -s scripts -p 'test_*.py'
```

## 5 Licença

[Voltar ao sumário](#sumário)

Distribuído sob a [licença Apache 2.0](LICENSE).

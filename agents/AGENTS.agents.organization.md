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
- Arquivos `PLAN.*.md` de plano operacional e `FEEDBACK.*.md` de relatório não
  são normas permanentes. Devem seguir suas regras próprias, sem serem usados
  para substituir um `AGENTS.md` de composição.
- Todo projeto com arquivos de código, de qualquer linguagem, deve citar
  normativamente `AGENTS.coding.suffixes.md` em uma composição `AGENTS.md`
  aplicável a todos esses arquivos. A leitura antes do desenvolvimento é
  obrigatória; o uso de sufixo não é.

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

## Etapas de leitura

Antes de analisar a estrutura das instruções de agentes em um projeto ou
catálogo, selecionar normas ou planejar a distribuição das composições, leia e
aplique:

- `AGENTS.agents.organization.analysis.md`

Antes de criar, revisar ou reorganizar arquivos locais de composição, leia e
aplique:

- `AGENTS.agents.organization.composition.md`

Antes de criar, revisar ou reorganizar normas especialistas ou agregadores,
leia e aplique:

- `AGENTS.agents.organization.specialists.md`

Antes de validar ou concluir uma manutenção das instruções de agentes, leia e
aplique:

- `AGENTS.agents.organization.validation.md`

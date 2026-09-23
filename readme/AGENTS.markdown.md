# Regras de Markdown

## Objetivo

- Todo documento Markdown operacional do projeto deve servir como referencia operacional e tecnica atual do projeto.
- Todo documento Markdown operacional deve ajudar uma pessoa ou IA a executar, configurar, testar, integrar, operar e diagnosticar o projeto sem depender de historico de conversa ou planejamento antigo.
- Todo documento Markdown operacional deve descrever o estado atual do sistema, nao o historico de implementacao.
- Arquivos `AGENTS***.md` sao excecao a estas regras de formatacao de Markdown; eles existem para leitura e aplicacao por IA e devem priorizar clareza normativa em vez de convencoes de sumario, ancoras e retorno ao sumario.

## Estrutura esperada

- O documento Markdown deve iniciar com o titulo do projeto em H1; quando o nome do projeto for seu identificador canonico, use `# nome-do-projeto`.
- Logo apos o titulo, deve haver uma descricao curta do objetivo do projeto.
- Documentos Markdown medios ou grandes devem possuir `## Sumario` antes das secoes de conteudo.
- Quando houver sumario, as secoes principais devem ser numeradas e os links do sumario devem apontar para os titulos reais.
- Para o link funcionar, o texto visivel do item no sumario e o texto do topo da secao devem ser escritos de forma identica. Acentos, maiusculas e demais caracteres devem permanecer iguais entre o texto do link e o texto do titulo.
- Essa igualdade e uma regra de escrita do documento, nao uma sugestao de lint: nao aplicar transliteracao manual, nao remover acentos e nao alterar a grafia do titulo para compensar o link.
- O fragmento do link deve ser derivado do titulo trocando espacos por hifens, depois de cumpridos os demais requisitos da norma, sem transliteracao manual, sem remocao de acentos e sem alterar a grafia do titulo.
- Se a forma escolhida para o titulo nao puder ser representada com uma ancora equivalente e consistente no proprio documento, reescreva o titulo e o item do sumario juntos ate que a igualdade seja preservada; nao deixe o texto do sumario e o titulo divergirem.
- Cada secao principal listada no sumario deve ter um link de retorno ao sumario logo abaixo do titulo, em formato pequeno e discreto, seguindo o padrao `[Voltar ao sumario](#sumario)` quando o anchor permitir ASCII simples, ou o anchor real usado no arquivo.
- O link de retorno ao sumario deve ser aplicado a todas as secoes que aparecem no sumario, sem excecao por relevancia ou tamanho.
- O link de retorno deve apontar para o sumario do proprio documento e usar o mesmo fragmento definido para o topo do sumario no arquivo, mantendo a grafia consistente com a regra do link principal.
- O texto do link de retorno deve permanecer discreto e pequeno, sem competir com o titulo da secao, para servir apenas como atalho de navegacao.
- Titulos devem manter grafia natural com acentuacao quando isso melhorar a leitura.
- Se a acentuacao for usada em titulos, sumario ou anchors, a documentacao deve preservar essa igualdade de texto e evitar que a escolha da grafia quebre os links.
- Documentos Markdown operacionais extensos devem seguir a estrutura desta norma e o modelo de documentacao adotado pelo projeto, quando houver.

## Conteudo minimo por tipo de projeto

- Documentos Markdown de servicos devem documentar, quando aplicavel: execucao local, profiles, portas, configuracoes obrigatorias, variaveis de ambiente, build/container, migrations, autenticacao/autorizacao, arquitetura dos modulos ou camadas, endpoints relevantes, testes e troubleshooting.
- Documentos Markdown de bibliotecas devem documentar, quando aplicavel: objetivo, quando usar, modulos, coordenadas de publicacao, configuracao, exemplo de consumo, comportamento esperado, limitacoes e troubleshooting.
- Documentos Markdown de ferramentas auxiliares devem documentar, quando aplicavel: objetivo, comandos principais, configuracao, entradas e saidas, integracao com outros projetos, execucao local e troubleshooting.
- Documentos Markdown de projetos de migration devem documentar schemas, modulos, ordem de execucao, publicacao dos artefatos, compatibilidade e regras de versao.

## Regras de escrita

- A escrita deve ser objetiva, operacional e verificavel.
- Evite texto promocional, historico de decisoes antigas, planos futuros soltos e explicacoes que nao ajudem execucao, manutencao ou operacao do projeto.
- Decisoes futuras, planos e analises devem ficar em documentos proprios, nao misturados ao documento Markdown operacional, salvo quando representarem uma diretriz operacional atual.
- O documento Markdown nao deve contradizer `AGENTS.md`, `AGENTS.*.md`, configuracoes reais, scripts, endpoints, tasks Gradle ou comportamento implementado.
- Quando houver divergencia entre documento Markdown e codigo/configuracao, investigue a fonte correta antes de atualizar a documentacao.
- Use nomes reais de modulos, properties, variaveis de ambiente, profiles, endpoints, roles, scopes, tabelas e comandos.
- Segredos reais nao devem ser documentados; use placeholders claros.

## Comandos e exemplos

- Comandos devem ser copiaveis e executaveis a partir da raiz indicada pelo proprio texto.
- Blocos de comando devem usar fenced code block com linguagem apropriada, como `bash`, `yaml`, `json`, `xml`, `text` ou `sql`.
- Exemplos devem ser pequenos o suficiente para manutencao, mas completos o bastante para execucao ou entendimento do contrato.
- Quando um comando depender de outro projeto, porta, servico externo ou variavel de ambiente, essa dependencia deve estar explicita.

## Configuracoes

- Configuracoes documentadas devem informar nome, finalidade e valor padrao quando existir.
- Quando o documento tratar de configuracoes proprias da aplicacao, aplique `../config/AGENTS.config.md`, respeitando o namespace definido pelo projeto.
- Variaveis de ambiente devem ser listadas com efeito pratico e contexto de uso.

## Atualizacao obrigatoria

- Ao alterar execucao local, profiles, portas, build, container, migrations, propriedades, variaveis de ambiente, endpoints, autenticacao, autorizacao, roles, scopes, modulos, arquitetura, testes, publicacao ou operacao, avalie e atualize o documento Markdown correspondente.
- Se a mudanca tornar uma instrucao do documento Markdown falsa ou incompleta, o documento deve ser atualizado na mesma atividade.
- Se a atualizacao do documento Markdown for propositalmente adiada, o fechamento da atividade deve informar essa pendencia explicitamente.

## Padronizacao entre projetos

- Projetos semelhantes devem manter estrutura de documento Markdown semelhante sempre que isso nao prejudicar clareza local.
- Servicos HTTP devem ser comparados prioritariamente com outros servicos HTTP.
- Bibliotecas devem ser comparadas prioritariamente com outras bibliotecas.
- Ferramentas auxiliares devem ser comparadas prioritariamente com outras ferramentas auxiliares.
- Ao reutilizar um modelo de documentacao, adapte-o ao tipo e as responsabilidades do projeto de destino, sem importar configuracoes, endpoints ou dependencias de outro projeto.

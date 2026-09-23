# Norma Global Prioritária

## Organização dos AGENTS

Antes de analisar, revisar, planejar ou modificar instruções de agentes, leia
também:

- `../agents/AGENTS.agents.specialized-files.md`

As regras desse arquivo são requisitos obrigatórios para a organização e a
composição de normas.

## Operação de normas

- Antes de cada novo trabalho, a IA deve obrigatoriamente verificar quais
  projetos, diretórios, tipos de arquivo e responsabilidades serão envolvidos.
  Essa verificação vale para cada nova solicitação ou etapa com contexto
  diferente, inclusive na mesma conversa; a seleção anterior não é suficiente.
- Em cada projeto envolvido, a IA deve partir do `AGENTS.md` raiz e localizar
  os `AGENTS.md` aplicáveis no caminho até os arquivos envolvidos, incluindo
  os das pastas ancestrais. Para arquivos novos, considere a pasta de destino.
- A descoberta inicial deve se limitar ao necessário para identificar o
  contexto e suas instruções. Antes de analisar, revisar, planejar ou modificar
  o conteúdo desse contexto, leia integralmente os `AGENTS.md` aplicáveis e
  carregue suas referências normativas conforme os critérios declarados.
- A composição raiz e as referências normativas sem critério específico de
  aplicação formam a base obrigatória. Referências normativas com critérios
  explícitos de atividade ou contexto devem ser carregadas antes do trabalho
  correspondente, incluindo suas dependências obrigatórias. Uma referência
  fora desses critérios não exige leitura antecipada de sua cadeia.
- Ao descobrir ou passar a envolver outro projeto, diretório, tipo de arquivo
  ou responsabilidade durante o trabalho, repita obrigatoriamente a verificação
  e leia as novas instruções aplicáveis antes de prosseguir nesse contexto.
  Isso também vale para mudanças de atividade na mesma pasta, como passar de
  documentação para código ou de código para testes.
- A verificação deve considerar instruções novas ou alteradas. Se houver dúvida
  sobre a aplicabilidade de uma norma, leia-a antes de agir; se uma instrução
  obrigatória estiver inacessível, informe o impedimento antes de atuar na área.
- Se o projeto não possuir `AGENTS.md` na raiz e o usuário tiver solicitado a
  criação ou organização das instruções de agentes, a IA pode realizar a
  descoberta, a análise e o planejamento necessários e criar a composição raiz
  e as composições locais pertinentes. Esse pedido autoriza a inicialização;
  não exija uma composição prévia nem nova confirmação para executá-la.
- Durante essa inicialização, siga as normas de organização e as instruções
  existentes aplicáveis, inclusive as de diretórios ancestrais e subdiretórios.
  Inspecione estrutura, build, configurações e conteúdo somente na medida
  necessária para identificar tecnologias, responsabilidades e normas úteis.
  A autorização de inicialização cobre a organização dos AGENTS; alterações
  funcionais no projeto dependem de um pedido que também as inclua.
- Após criar as composições, valide os caminhos e os escopos e carregue o
  `AGENTS.md` raiz, as composições locais e as referências normativas aplicáveis
  antes de iniciar qualquer outro trabalho já solicitado.
- Se faltar o `AGENTS.md` raiz e não houver pedido de criação ou organização
  das instruções, informe a ausência e solicite a inicialização antes de
  prosseguir com a análise, o planejamento ou as alterações do projeto.
- Quando uma norma estiver sendo violada, a IA deve avisar o usuário e pedir permissão para prosseguir com a violação.
- Quando o usuário fizer uma pergunta, a IA deve responder de forma simples e textual.
- Uma pergunta do usuário não autoriza alteração de arquivos, implementação, execução de correção ou mudança de estado.
- Alterações em arquivos só devem ser feitas quando o usuário pedir explicitamente uma ação desse tipo.
- Toda alteração em arquivos `AGENTS.md` ou `AGENTS.*.md` deve preservar a coerência integral da norma modificada.
- Ao modificar uma regra normativa, a IA deve revisar o bloco completo da norma afetada, e não apenas o trecho pontual solicitado.
- A IA deve procurar contradições internas, repetições incompatíveis, exemplos desatualizados, listas de testes divergentes e planos derivados que continuem refletindo a regra anterior.
- Quando uma alteração normativa mudar a semântica de uma decisão já documentada, a IA deve atualizar todos os trechos diretamente relacionados no mesmo arquivo.
- Quando houver documentos normativos ou planos derivados que dependam da regra alterada, a IA deve apontar esses documentos e, se autorizada a alterá-los, alinhá-los na mesma atividade.
- Não é aceitável alterar parcialmente uma norma deixando o texto completo com interpretações concorrentes.
- Se a IA não conseguir verificar todos os pontos relacionados, deve informar explicitamente a limitação antes de concluir a atividade.
- Arquivos `FEEDBACK.*.md` devem ser usados para respostas, análises, relatórios, feedbacks e documentos equivalentes solicitados pelo usuário.
- Arquivos `AGENTS.*.md` podem ser usados para planejamentos variáveis e temporários ou para normas persistentes e duradouras.
- Arquivos `AGENTS.*.md` de planejamento operacional devem ser criados na raiz do projeto ao qual pertencem.
- Arquivos `AGENTS.*.md` de planejamento operacional não devem ser criados em subdiretórios como `docs/`, `docs/plans/` ou equivalentes, salvo instrução explícita do usuário autorizando uma exceção.
- A regra de prefixo `FEEDBACK.` permanece obrigatória para arquivos `.md` de resposta, análise, relatório ou feedback que não tenham função de instrução, planejamento operacional ou norma de agente.
- Arquivos `FEEDBACK.*.md` podem ser ignorados pelo git de forma intencional; isso é comportamento esperado e não deve ser tratado como problema.
- Em ambos os casos, `AGENTS.*.md` e `FEEDBACK.*.md`, o git pode ignorar esses arquivos, e esse comportamento é desejado.

# Diretrizes Globais

- Todos os serviços devem manter estruturas semelhantes quando isso for possível e compatível com o contexto de cada projeto.
- Serviços devem usar padrões equivalentes quando resolverem problemas semelhantes e forem compatíveis com o contexto local.
- Operações HTTP, camadas equivalentes, organização de responsabilidades, nomes e fluxos recorrentes devem buscar consistência entre projetos, desde que isso não force complexidade desnecessária nem viole regras locais mais específicas.
- A IA deve investigar outros projetos para entender quais padrões deve seguir, reutilizar ou copiar.
- A comparação de padrões deve considerar projetos de natureza semelhante: serviços HTTP devem ser comparados prioritariamente com outros serviços HTTP, bibliotecas com outras bibliotecas e ferramentas auxiliares com ferramentas auxiliares.
- Projetos de natureza diferente podem servir como referência secundária, mas não devem ser usados como base principal para inferir padrões transversais quando houver projetos similares mais adequados.
- A IA não deve ler a pasta `done/` localizada na raiz dos projetos.
- A pasta `done/` deve ser ignorada porque contém arquivos de análises ou implementações que já foram aplicadas ou descartadas, não devendo ser usada como contexto atual do projeto.

## Citações entre documentos

- O tipo de uma referência é definido pela instrução que a acompanha. Um nome,
  caminho, link ou título isolado não ativa uma norma.
- Referência normativa: contém uma ordem explícita de leitura ou aplicação,
  como "leia também", "leia e aplique", "aplique" ou "siga as regras de".
  A ordem pode introduzir uma lista de arquivos. Ela torna obrigatórios o
  arquivo e suas dependências normativas aplicáveis no contexto declarado.
- Referência informativa: apresenta um documento como explicação complementar,
  sem ordem de aplicação. Identifique-a como "referência informativa" quando
  houver risco de confusão. Sua leitura é opcional e não ativa suas regras.
- Exemplo ou menção: apresenta nomes ilustrativos ou instruções dentro de
  modelos explicitamente identificados como exemplos. Não exige leitura,
  aplicação nem existência dos arquivos ilustrados. Ordens dentro de um modelo
  só passam a valer quando adotadas como instruções no projeto de destino.
- A marcação de exemplo delimita a interpretação das ordens no trecho
  ilustrativo. Fora de exemplos, uma dependência real deve ser declarada como
  referência normativa; não a substitua por um link ou referência informativa.
- Uma menção informativa ou ilustrativa não cancela uma obrigação ativada por
  outra referência normativa ao mesmo arquivo.
- A referência normativa deve aparecer após um título ou seção que indique
  claramente o tema e o escopo da norma composta.
- Critérios de carregamento devem aparecer no documento que faz a citação,
  antes da referência, e identificar atividades, diretórios, tipos de arquivo,
  tecnologias ou responsabilidades concretas. Sem critério explícito, uma
  referência normativa exige leitura em todo o escopo da composição que a contém.
- Ao percorrer referências normativas transitivas, preserve o escopo que ativou
  a cadeia e observe os critérios explícitos de cada referência. Uma norma
  ativada deve ser cumprida integralmente no seu escopo; economia de contexto
  não autoriza omitir dependências obrigatórias nem escolher partes de um agregador.
- Não deixe a leitura de uma referência normativa depender da conveniência do
  agente. O atendimento ao critério torna sua leitura obrigatória.

## Ciclos e reaproveitamento de leitura

- Identifique cada arquivo pelo caminho resolvido a partir do documento que
  faz a referência, normalizando caminhos equivalentes e links simbólicos.
  Nomes iguais em pastas diferentes não identificam necessariamente a mesma norma.
- Registre os arquivos em leitura e os já lidos no percurso. Ao reencontrar um
  arquivo em leitura, encerre somente essa repetição e continue as demais
  dependências normativas aplicáveis. Um ciclo não dispensa nenhuma das normas
  envolvidas nem permite abandonar os outros ramos da composição.
- Reaproveite uma leitura somente quando o conteúdo integral continuar
  disponível no contexto e sua versão atual estiver confirmada. Se o arquivo
  mudou, o conteúdo foi perdido ou resumido, ou houver dúvida sobre a versão,
  leia-o novamente antes de aplicar suas regras.
- A cada novo trabalho ou mudança de contexto, reavalie obrigatoriamente os
  critérios das referências, inclusive nos arquivos já lidos. Reaproveitar o
  conteúdo não dispensa descobrir e ler novas dependências aplicáveis, nem
  permite reduzir o conjunto de escopos em que uma norma deve ser cumprida.

# Comunicação

## Regra Principal

- A IA deve responder ao usuário sempre em Português do Brasil.
- Essa regra vale para respostas, perguntas, explicações, resumos, diagnósticos, feedback, planos e orientações operacionais.
- Receber conteúdo em inglês não muda o idioma da interação.

## Conteúdo de Sistemas

- Projetos, ferramentas, frameworks, bibliotecas, pipelines, APIs, logs e mensagens automáticas podem permanecer em inglês.
- O idioma operacional dos sistemas não altera o idioma da conversa com o usuário.

## Tratamento de Conteúdo em Inglês

- Quando logs, erros, alertas, saídas de comando ou mensagens de ferramenta estiverem em inglês, a IA deve interpretar o conteúdo e responder em Português do Brasil.
- A IA deve resumir em Português do Brasil o que for mais importante para a decisão do usuário.
- Trechos literais em inglês só devem ser citados quando forem necessários para precisão técnica.

## Exceções Permitidas

- É permitido manter em inglês nomes próprios, identificadores, nomes de classes, métodos, arquivos, variáveis, endpoints, mensagens literais e termos técnicos sem tradução natural.
- Mesmo nessas exceções, a explicação principal ao usuário deve continuar em Português do Brasil.

## Precedência

- Se houver conflito entre o idioma da conversa e o idioma de sistemas, logs ou projetos, prevalece o idioma da conversa com o usuário: Português do Brasil.

# Referência Nominal

## Regra Base

- Em texto corrido, a IA deve usar nomes simples de classes e arquivos por padrão.
- A IA não deve usar nome qualificado completo nem path completo por padrão.
- Exceções explícitas: pedido do usuário, ambiguidade real, necessidade de precisão técnica, necessidade de referência local clicável ou rastreável, ou instrução superior conflitante.

## Classes Java

- Usar o nome simples da classe.
- Exemplos preferidos: `ResponseEntity`, `CustomerService`, `PlanStatus`.
- Usar nome qualificado completo apenas quando uma exceção explícita aplicar.

## Arquivos `.java`

- Usar o nome simples do arquivo.
- Exemplos preferidos: `CustomerEntity.java`, `CustomerService.java`, `Application.java`.
- Usar path completo apenas quando uma exceção explícita aplicar.

## Arquivos `.md`

- Usar o nome simples do arquivo.
- Exemplos preferidos: `AGENTS.md`, `README.md`, `SKILL.md`.
- Usar path completo apenas quando uma exceção explícita aplicar.

# Limites entre Projetos

- A IA não deve alterar outros projetos sem pedir permissão ao usuário.
- A IA não deve deletar arquivos, trechos, seções, documentos ou entradas sem planejamento explícito ou pedido formal objetivo do usuário.
- Quando uma deleção parecer necessária, a IA deve primeiro explicar o impacto e pedir confirmação antes de remover qualquer conteúdo.

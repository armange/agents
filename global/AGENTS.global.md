# Norma Global Prioritária

## Organização dos AGENTS

Antes de analisar, revisar, planejar ou modificar instruções de agentes, leia
também:

- `../agents/AGENTS.agents.specialized-files.md`

As regras desse arquivo são requisitos obrigatórios para a organização e a
composição de normas.

## Operação de normas

- Antes de analisar, revisar, planejar ou modificar qualquer projeto, a IA deve
  localizar e ler o `AGENTS.md` da raiz desse projeto, bem como todas as normas
  citadas direta ou transitivamente por ele.
- A obrigação de carregar a composição da raiz aplica-se a cada projeto
  efetivamente envolvido na atividade, mesmo quando a IA tenha iniciado o
  trabalho em outro diretório ou projeto.
- Se o projeto envolvido não possuir `AGENTS.md` na raiz, a IA não deve iniciar
  análise, planejamento nem alteração nele; deve informar a ausência e pedir a
  criação da composição raiz antes de prosseguir.
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

- Toda citação de arquivo `AGENTS.md` ou `AGENTS.*.md` é uma composição normativa obrigatória.
- A citação deve aparecer logo após um título ou seção que indique claramente o tema e o escopo da norma composta.
- O título ou seção deve dar ao leitor uma noção do conteúdo esperado antes da abertura do documento citado.
- Não insira citações soltas, condicionais ou sem contexto estrutural.

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

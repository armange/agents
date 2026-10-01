# Arquivos AGENTS Especialistas

## Organização de normas em projetos

Antes de analisar, planejar ou executar a organização de normas, ou de criar,
revisar ou modificar instruções de agentes, leia e aplique:

- `AGENTS.agents.organization.md`

As referências desse arquivo selecionam as etapas aplicáveis de análise,
distribuição, criação e validação das instruções de agentes.

## Estrutura e composição

- Arquivos `AGENTS.*.md` devem ser especialistas em apenas um assunto normativo.
- Um arquivo `AGENTS.*.md` não deve misturar assuntos independentes.
- Quando uma norma atual concentrar temas diferentes, ela deve ser quebrada em partes lógicas menores, cada uma com um único assunto.
- A quebra deve permitir reaproveitamento, composição mais precisa e otimização do contexto carregado em cada tarefa.
- Arquivos `AGENTS.md` locais dentro de projetos, módulos ou pastas são os pontos de composição de normas.
- Um `AGENTS.md` local pode tratar vários assuntos por meio de citações a múltiplos arquivos `AGENTS.*.md` especialistas.
- Um `AGENTS.md` local não deve copiar nem reimplementar normas especialistas no próprio corpo, salvo quando precisar declarar uma especialização local explícita.
- Especializações locais devem ter escopo claro, precedência clara e não devem contradizer normas superiores.
- A centralização física dos arquivos especialistas é permitida para simplificar manutenção.
- A existência de uma norma especialista na pasta central não a torna automaticamente aplicável.
- Antes de cada novo trabalho e de cada mudança de contexto durante sua
  execução, a IA deve obrigatoriamente verificar os `AGENTS.md` da raiz e dos
  diretórios envolvidos e ler as novas instruções aplicáveis antes de atuar.
  A verificação anterior não dispensa essa etapa, mesmo na mesma conversa.
- Uma referência normativa contém uma ordem explícita, como "leia também",
  "leia e aplique" ou "aplique", dirigida ao arquivo ou à lista que a segue.
  Ela ativa obrigatoriamente a norma e suas dependências normativas aplicáveis
  quando o trabalho atender ao escopo declarado antes da referência.
- Referências informativas explicam ou apresentam outros documentos sem ordem
  de aplicação; sua leitura é opcional e não ativa regras. Nomes e links
  isolados também não constituem referências normativas.
- Exemplos e menções ilustrativas não ativam normas nem exigem que os arquivos
  existam. Ordens dentro de modelos identificados como exemplos só passam a
  valer quando adotadas como instruções no projeto de destino.
- Declare dependências reais como referências normativas. Uma referência
  informativa ou exemplo não pode substituir nem cancelar essa obrigação.
- Critérios devem identificar atividades ou contextos concretos; referências
  normativas sem critério explícito pertencem à base obrigatória da composição.
- Preserve o escopo de ativação ao seguir a cadeia de referências normativas e
  observe os critérios de cada referência. Cadeias fora do contexto atual podem
  aguardar a atividade correspondente; normas ativadas devem ser lidas
  integralmente antes dessa atividade. Em caso de dúvida, leia a norma.
- Para ativar um subconjunto fixo que o agregador não delimite por critérios
  objetivos, o `AGENTS.md` local deve declarar referências normativas direta e
  exclusivamente aos especialistas necessários.
- Condições materiais declaradas na norma, como uma tecnologia já configurada no projeto, continuam delimitando o seu escopo; elas não tornam facultativo o cumprimento da norma ativada.

## Ciclos e leituras anteriores

- Identifique o arquivo pelo caminho resolvido a partir de quem o referencia,
  normalizando caminhos equivalentes e links simbólicos. Ao reencontrar um
  arquivo em leitura no percurso, encerre apenas essa repetição e continue
  todas as outras dependências normativas aplicáveis.
- Reaproveite uma leitura apenas se o conteúdo integral estiver disponível no
  contexto e a versão atual estiver confirmada. Mudança de conteúdo, perda ou
  resumo no contexto e dúvida de versão exigem nova leitura antes de aplicar.
- Mesmo quando a leitura for reaproveitada, cada novo trabalho ou mudança de
  contexto exige reavaliar as referências e ler as novas dependências aplicáveis.
  Um arquivo já lido deve ter suas regras cumpridas em todos os escopos ativados.

## Integridade das alterações em AGENTS

- Toda alteração em arquivos `AGENTS.md` ou `AGENTS.*.md` deve preservar a coerência integral da norma modificada.
- Ao modificar uma regra normativa, a IA deve revisar o bloco completo da norma afetada, e não apenas o trecho pontual solicitado.
- A IA deve procurar contradições internas, repetições incompatíveis, exemplos desatualizados, listas de testes divergentes e planos derivados que continuem refletindo a regra anterior.
- Quando uma alteração normativa mudar a semântica de uma decisão já documentada, a IA deve atualizar todos os trechos diretamente relacionados no mesmo arquivo.
- Quando houver documentos normativos ou planos derivados que dependam da regra alterada, a IA deve apontar esses documentos e, se autorizada a alterá-los, alinhá-los na mesma atividade.
- Não é aceitável alterar parcialmente uma norma deixando o texto completo com interpretações concorrentes.
- Se a IA não conseguir verificar todos os pontos relacionados, deve informar explicitamente a limitação antes de concluir a atividade.
- Arquivos `AGENTS.*.md` são reservados a normas especializadas; planos em
  arquivo seguem o especialista de planos indicado pela norma global.

# Arquivos AGENTS Especialistas

## Organização de normas em projetos

Antes de analisar, planejar ou executar a organização de normas em um projeto,
leia também:

- `AGENTS.agents.organization.md`

As regras desse arquivo complementam esta norma com o processo obrigatório de
análise, distribuição, criação e validação das instruções de agentes.

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
- Uma citação ativa obrigatoriamente a norma citada e, quando ela compõe outras normas, toda a cadeia de citações.
- Para ativar apenas parte de um conjunto, o `AGENTS.md` local deve citar diretamente e exclusivamente os especialistas necessários.
- Condições materiais declaradas na norma, como uma tecnologia já configurada no projeto, continuam delimitando o seu escopo; elas não tornam facultativo o cumprimento da norma ativada.

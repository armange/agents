# Organização de Normas AGENTS: Especialistas

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
- Atualize um arquivo agregador somente se sua base e seus critérios fizerem a
  nova norma chegar a todos os consumidores para os quais ela é aplicável, sem
  ativá-la nos demais. Caso contrário, mantenha a nova norma independente e
  cite-a apenas nos pontos locais adequados.
- Não altere normas compartilhadas para acomodar uma exceção de um único
  projeto. Crie uma especialização local clara quando a exceção for legítima.
- Ao alterar uma norma compartilhada, reavalie as composições que a referenciam
  normativamente, direta ou transitivamente, e informe os projetos potencialmente
  afetados antes de concluir a atividade. Confira também as explicações e os
  exemplos que descrevam a regra alterada para manter a documentação coerente.

# Arquivos de Planos de Desenvolvimento

## Objetivo e escopo

- Esta norma define a identificação e a localização de planos de desenvolvimento ou de outros planejamentos operacionais associados a alterações de um projeto, quando forem registrados em arquivos Markdown.
- Ela não exige criar um plano para toda alteração. Aplica-se quando a criação ou a manutenção de um plano em arquivo fizer parte do trabalho autorizado.

## Nome e natureza do arquivo

- Arquivos de plano devem começar com `PLAN.` e terminar com `.md`, no formato `PLAN.<assunto>.md`. O assunto deve identificar de forma curta e específica o objetivo do plano.
- Não use `AGENTS.plan.*.md` nem outro arquivo `AGENTS.*.md` para armazenar um plano. Arquivos `AGENTS.md` compõem instruções e arquivos `AGENTS.*.md` contêm normas especializadas; um plano registra trabalho a executar e não ativa normas.
- Um plano não substitui uma norma duradoura. Quando uma decisão do plano precisar tornar-se regra permanente, trate a criação ou a alteração da norma correspondente como trabalho próprio.
- Relatórios e análises sem função de plano continuam seguindo a convenção `FEEDBACK.*.md`.

## Localização e manutenção

- Crie o plano na raiz do projeto ao qual ele pertence. Não o coloque em `docs/`, `docs/plans/` ou subdiretório equivalente, salvo instrução explícita do usuário para uma exceção.
- Ao retomar ou modificar um plano legado com outro prefixo, adote o formato `PLAN.<assunto>.md`, atualize as referências que apontam para ele e preserve seu conteúdo. Esta norma não exige migração em massa de arquivos fora do escopo da atividade atual.

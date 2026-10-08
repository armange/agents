# Arquivos de Planos de Desenvolvimento

## Objetivo e escopo

- Esta norma define a identificação, a localização e a decomposição de planos de desenvolvimento ou de outros planejamentos operacionais associados a alterações de um projeto, quando forem registrados em arquivos Markdown.
- Ela não exige criar um plano para toda alteração. Aplica-se quando a criação ou a manutenção de um plano em arquivo fizer parte do trabalho autorizado.

## Unidades de negócio e decomposição

- Antes de dividir um plano por projeto, módulo ou componente, identifique as unidades de negócio envolvidas e o resultado esperado de cada uma. Preserve as unidades já definidas pelo usuário; não as redefina implicitamente.
- Para cada unidade, descreva seu interesse de negócio, entradas, decisões e regras, resultados, falhas e colaboração com outras unidades. Registre quais critérios de aceite comprovam seu funcionamento completo.
- Relacione cada fase e subtarefa à unidade que ela entrega ou apoia. Classes, interceptors, bibliotecas e etapas técnicas não se tornam unidades de negócio apenas por serem entregáveis separados.
- Antes de declarar o plano pronto para implementação, verifique se todas as unidades estão cobertas de ponta a ponta e se a divisão técnica preserva suas fronteiras. Se uma fronteira de negócio continuar ambígua, registre a decisão necessária.
- Em planos exclusivamente técnicos, declare brevemente por que não há unidade de negócio a delimitar. Respeite as normas arquiteturais específicas adotadas pelo projeto; esta seção não exige uma estrutura de código.

## Nome e natureza do arquivo

- Arquivos de plano devem começar com `PLAN.` e terminar com `.md`, no formato `PLAN.<assunto>.md`. O assunto deve identificar de forma curta e específica o objetivo do plano.
- Não use `AGENTS.plan.*.md` nem outro arquivo `AGENTS.*.md` para armazenar um plano. Arquivos `AGENTS.md` compõem instruções e arquivos `AGENTS.*.md` contêm normas especializadas; um plano registra trabalho a executar e não ativa normas.
- Um plano não substitui uma norma duradoura. Quando uma decisão do plano precisar tornar-se regra permanente, trate a criação ou a alteração da norma correspondente como trabalho próprio.
- Relatórios e análises sem função de plano continuam seguindo a convenção `FEEDBACK.*.md`.

## Localização e manutenção

- Crie o plano na raiz do projeto ao qual ele pertence. Não o coloque em `docs/`, `docs/plans/` ou subdiretório equivalente, salvo instrução explícita do usuário para uma exceção.
- Ao retomar ou modificar um plano legado com outro prefixo, adote o formato `PLAN.<assunto>.md`, atualize as referências que apontam para ele e preserve seu conteúdo. Esta norma não exige migração em massa de arquivos fora do escopo da atividade atual.

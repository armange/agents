# Execução de planos: controle de escopo

## Objetivo e escopo

Esta norma se aplica quando uma tarefa executa um plano de implementação,
independentemente de o plano estar em arquivo, em uma story ou na conversa.
Seu objetivo é manter rastreável o que pertence à implementação aprovada.

## Execução do escopo aprovado

- Antes de alterar arquivos, identifique o objetivo, os entregáveis, os
  critérios de aceite, os projetos envolvidos e os limites do plano vigente.
- Restrinja as alterações ao que é necessário para entregar e verificar esse
  escopo. Inclua testes, documentação e ajustes de integração quando forem
  consequências necessárias dos entregáveis planejados.
- Relacione cada alteração material a um entregável ou critério de aceite. Se
  essa relação não puder ser explicada, não incorpore a alteração à execução.
- Não use falhas descobertas durante a implementação ou nos testes como
  autorização automática para modificar componentes alheios ao plano.
  Investigue a causa e a relação com o escopo antes de corrigir.

## Necessidades e requisitos descobertos durante a execução

- Ao encontrar uma necessidade nova, avalie sua origem, sua relação com o
  objetivo, os projetos afetados, as dependências, o impacto e o risco de
  incluí-la na implementação em curso.
- Se for necessária para satisfazer o objetivo ou os critérios de aceite,
  registre a decisão e atualize o plano e seus entregáveis antes da alteração,
  quando houver plano em arquivo. Para uma ampliação material de escopo, obtenha
  a decisão do usuário antes de executá-la; a autorização do plano original
  não cobre automaticamente essa ampliação.
- Se for independente ou puder ser entregue depois sem comprometer o objetivo
  aprovado, registre-a como trabalho futuro, em outro plano quando for
  planejada, e continue a execução do escopo atual.
- Se a necessidade impedir a conclusão e não houver decisão sobre sua inclusão,
  apresente o impedimento e as opções ao usuário. Não a implemente
  silenciosamente nem declare o plano concluído.

Ao concluir, informe os entregáveis realizados, as alterações de escopo
decididas e as necessidades registradas para outro momento.

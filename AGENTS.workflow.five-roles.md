# Fluxo Opcional de Cinco Papéis

## Ativação e alcance

- O owner é a pessoa que solicita e orienta o trabalho; é o sexto papel, fora
  da equipe de agentes.
- Use este fluxo somente quando o owner o solicitar explicitamente para a
  demanda. A existência desta norma não autoriza criar subagentes por padrão.
- Sem ativação explícita, um único agente executa a demanda no formato padrão.
- Cada agente deve ler e aplicar os `AGENTS.md` e as normas pertinentes aos
  projetos, diretórios e arquivos sob sua responsabilidade. A divisão de papéis
  não dispensa nenhuma instrução aplicável.

## Papéis e responsabilidades

- **Coordenador:** é o agente raiz que recebe as instruções do owner. Somente
  ele distribui tarefas, coordena os demais agentes, encaminha decisões e
  achados, acompanha as etapas e consolida o resultado para o owner. Os
  subagentes devolvem resultados ao coordenador, sem coordenar outros papéis.
- **Planejador:** é o analista que coleta e interpreta dados e implementações
  para produzir planos de desenvolvimento e stories. Toma decisões de
  planejamento com participação do owner, mediada pelo coordenador. Antes de
  considerar um plano pronto para implementação, confronta as mudanças propostas
  com as regras de negócio dos `AGENTS.md` aplicáveis e dos READMEs atuais,
  além dos contratos e comportamentos existentes. Identifica contradições,
  lacunas e riscos de regressão, registra como serão resolvidos e comunica ao
  coordenador o que ainda exige decisão do owner. Não recomenda iniciar uma
  implementação enquanto ela contrariar essas regras ou deixar uma
  inconsistência conhecida sem solução. Para toda regra de negócio nova ou
  alterada, exige que o plano identifique os READMEs responsáveis e inclua a
  atualização da documentação e sua conferência com o comportamento entregue
  nos critérios de aceite. Não considera pronto para implementação um plano
  que omita essa entrega.
- **Implementador:** constrói o código com a melhor qualidade e arquitetura
  possíveis dentro do plano e das normas aplicáveis. Executa os testes locais
  pertinentes e corrige as falhas causadas por sua implementação antes de
  entregar o trabalho. Não desenvolve testes de ponta a ponta.
- **Revisor:** avalia de forma independente a qualidade do código, a
  arquitetura e o cumprimento das normas, com foco no plano de desenvolvimento.
  Apresenta achados e evidências ao coordenador; não altera a implementação.
- **Testador:** organiza o ambiente completo, cria e mantém os testes de ponta a ponta e
  os executa como verificação final. Relata resultados e falhas ao
  coordenador. Não altera o código de implementação dos sistemas sob teste.

## Passagem de trabalho

- O coordenador fornece a cada agente a demanda, o plano e o contexto
  necessários à sua responsabilidade, incluindo arquivos novos e alterações
  ainda não commitadas quando relevantes.
- O coordenador só encaminha o plano à implementação após receber do planejador
  a verificação de coerência das regras de negócio e resolver com o owner as
  decisões pendentes que afetem essa coerência.
- Antes da revisão, o implementador entrega as alterações e os resultados dos
  testes locais. O revisor informa achados relacionados ao plano, às normas e
  às alterações examinadas.
- O testador informa os cenários de ponta a ponta criados ou ajustados, o estado do
  ambiente, os comandos executados e os resultados dos testes finais.
- O coordenador encaminha problemas do código de implementação ao
  implementador e problemas dos cenários de ponta a ponta ao testador. Após correções,
  solicita nova revisão e novos testes nos pontos afetados.
- O coordenador apresenta ao owner o resultado, as evidências e as pendências.

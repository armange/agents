# Codificação: Avaliação de Sufixos

## Escopo

- Esta norma se aplica a arquivos de código de qualquer linguagem, com ou sem
  classes, independentemente da arquitetura adotada pelo projeto.
- Todo projeto com código deve citá-la normativamente em um `AGENTS.md` que
  alcance todos os seus arquivos de código. Ela deve ser lida antes de
  analisar, revisar, planejar ou modificar código.
- Esta norma não exige sufixos nem impõe camadas, packages, tecnologias ou
  uma matriz fechada de nomes.

## Regras

- Ao criar ou alterar uma unidade nomeada, como classe, interface, tipo, função,
  componente ou módulo, avalie se um sufixo comunica sua responsabilidade com
  mais clareza do que um nome sem sufixo.
- O uso de sufixo é opcional. Quando usado, ele deve corresponder ao papel real
  da unidade e respeitar a convenção de nomenclatura da linguagem.
- É proibido combinar `PolicyService` ou `ServicePolicy` no mesmo nome,
  incluindo grafias equivalentes de outras linguagens, como `policy_service`
  e `service_policy`, pois a responsabilidade fica ambígua.
- Antes do desenvolvimento, verifique também as normas específicas de sufixos
  que a composição aplicável citar. Esta norma não ativa automaticamente uma
  topologia arquitetural ou uma matriz específica de sufixos.
- Nomes legados não exigem migração automática; reavalie-os quando fizerem
  parte da alteração em andamento.

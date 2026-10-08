# Arquitetura: Refatoração de Unidades de Negócio

## Base e escopo

Esta norma orienta refatorações ligadas à coesão de unidades de negócio nos
projetos que adotam a topologia de camadas deste conjunto. Sua adoção é
opcional. Antes de aplicá-la, leia e aplique a definição de unidade de negócio
e sua base arquitetural pela referência abaixo, relativa a este arquivo:

- `AGENTS.architecture.business-unit.md`

## Diretriz

- Durante uma implementação autorizada, procure oportunidades evidentes de
  refatoração que melhorem a coesão da unidade de negócio afetada. Favoreça
  mudanças pontuais diretamente relacionadas ao trabalho em curso e dentro do
  escopo autorizado; a identificação de uma oportunidade não obriga a
  refatorar.
- Refatoração deve preservar o comportamento observável e os contratos
  existentes. Se a mudança corrigir um comportamento ou introduzir outro,
  trate essa parte como correção ou implementação, com escopo próprio.
- Antes de refatorar, identifique o problema de organização, delimite a mudança
  e verifique a preservação do comportamento por meios adequados ao contexto.
  Se o comportamento atual não estiver suficientemente caracterizado, obtenha
  evidência antes de reorganizar o código.
- Prefira um plano prévio breve, inclusive na conversa, sobretudo quando a
  mudança envolver várias responsabilidades. Esta preferência não cria uma
  exigência de plano para toda refatoração nem dispensa exigências de
  planejamento, confirmação ou controle de escopo já aplicáveis.

## Exemplos de oportunidades

Os sinais abaixo são ilustrativos, não formam uma lista exaustiva nem são
condições obrigatórias para refatorar:

- Uma classe reúne responsabilidades ligadas a interesses de negócio distintos.
- A mesma decisão de negócio está espalhada ou duplicada em vários lugares.
- As fronteiras entre `Service`, `Policy` e `Feature` não deixam clara a
  responsabilidade por um comportamento.
- Uma mudança local em uma unidade exige alterações em partes sem relação com
  o interesse de negócio atendido.

Tamanho da classe ou quantidade de arquivos, isoladamente, não justificam a
refatoração. Falta de testes é um risco a tratar, não um sinal de que a
estrutura precise mudar.

## Precedência

Esta norma não altera as responsabilidades e dependências das camadas nem
autoriza remoções ou ampliações de escopo vedadas pelas normas aplicáveis.

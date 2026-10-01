# Organização de Normas AGENTS: Validação

## Validação e aceite

- Ao manter este catálogo, execute `python3 scripts/validate_agents.py` na raiz
  do repositório para conferir referências, modelos, ciclos, repetições e volume
  potencial das composições. O comando usa arquivos do disco, mesmo ignorados
  pelo Git. Corrija os erros e revise os avisos antes de concluir a manutenção.
- Referência informativa: [uso e limites do verificador](../README.md#4-validação-automática).
  A verificação automática complementa a revisão abaixo; não decide critérios
  de contexto nem compatibilidade semântica das normas. Projetos consumidores
  podem usar o script do catálogo com `--root` apontando para a raiz comum das
  normas, sem precisar copiá-lo para cada projeto.

- Em uma inicialização, confirme que a composição raiz foi criada e que ela e
  as composições locais aplicáveis foram carregadas antes de qualquer outro
  trabalho solicitado. A descoberta inicial deve ter servido à organização
  das instruções e preservado as regras já existentes nos diretórios envolvidos.
- Em projetos com código, confirme que a referência normativa à avaliação
  de sufixos alcance todos os arquivos de código e exija sua leitura antes do
  desenvolvimento. A ausência de classes não dispensa a citação; a avaliação
  pode concluir que nenhum sufixo se aplica.
- Verifique que cada referência normativa nos arquivos novos ou alterados aponta
  para arquivo existente a partir do diretório que a contém. Referências
  informativas a documentos reais devem ser corretas; nomes hipotéticos em
  exemplos não devem ser tratados como dependências ausentes.
- Verifique que cada `AGENTS.md` com caminhos relativos declara que eles são
  relativos ao próprio arquivo e inclui a raiz do projeto como referência
  nominal, sem incluir path.
- Confira que a adoção isolada de cada especialista arquitetural alcança sua
  base obrigatória e que normas independentes de uma topologia não a importam
  sem necessidade. Normas derivadas não ampliam permissões da base nem exigem
  materializar camadas opcionais sem responsabilidade real.
- Verifique a cadeia transitiva das normas agregadoras para garantir que ela não
  introduz temas incompatíveis no diretório local.
- Resolva os caminhos das referências normativas, incluindo links simbólicos,
  e identifique ciclos e dependências repetidas. Durante a leitura, um retorno
  a um arquivo em leitura encerra apenas a repetição; as demais dependências
  continuam obrigatórias. Referências informativas não integram essa cadeia.
- Confira que uma leitura anterior só é reaproveitada com conteúdo integral
  disponível e versão atual confirmada. Cada novo trabalho ou contexto exige
  reavaliar as referências do arquivo, mesmo quando ele não precisa ser relido.
- Verifique que a composição exige nova avaliação de contexto antes de cada
  trabalho e durante mudanças de escopo, com leitura prévia das novas normas.
- Confira um cenário restrito a uma atividade e outro que passe a envolver uma
  segunda área. No primeiro, referências fora do escopo devem aguardar; no
  segundo, suas instruções devem ser carregadas antes da nova atividade.
- Revise ao menos um exemplo representativo de cada escopo criado: raiz,
  código principal, testes, recursos e uma fronteira técnica especializada.
- Confirme que `src/main/resources`, `src/test/resources`, outros diretórios
  configurados como recursos e suas subpastas não contêm `AGENTS.md` nem
  `AGENTS.*.md`. Confira que as normas desses recursos são alcançadas pela
  composição ancestral, com critérios explícitos para o escopo correspondente.
- Confirme que nenhuma norma de protocolo, banco, framework ou teste foi
  posicionada em árvore que não contenha essa responsabilidade.
- Confirme que diretórios vazios e módulos puramente agregadores não receberam
  instruções redundantes.
- Inspecione os arquivos diretamente no filesystem para validar seu conteúdo atual.
- Documente no fechamento quais normas foram aplicadas, quais foram excluídas
  por incompatibilidade e quais validações estruturais foram executadas.

## Critério de resultado

- Um projeto está organizado quando uma pessoa ou IA consegue começar por seu
  `AGENTS.md` raiz, seguir as referências normativas aplicáveis e encontrar em
  cada escopo somente as normas necessárias para modificar seu conteúdo
  corretamente. Diretórios de recursos recebem suas instruções por composição
  ancestral, sem arquivos AGENTS dentro deles.
- A redução de contexto deve vir da composição precisa, e nunca da omissão de
  uma norma materialmente aplicável.

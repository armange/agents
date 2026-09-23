# Projetos: versionamento e ciclo de release

## Estados de versão

- Uma versão terminada em `-SNAPSHOT` representa implementação em andamento.
  Seu contrato pode mudar e ela não é referência estável de compatibilidade.
- Uma versão sem sufixo de pré-release representa artefato publicado e
  imutável. O mesmo número de versão não deve receber novo código, novo
  artefato ou nova publicação.
- Após publicar uma versão estável, o projeto deve iniciar a próxima iteração
  em uma nova versão `-SNAPSHOT` antes de receber novas alterações.
- Sufixos de release candidate, como `-RC.1`, é permitido para validar um
  contrato congelado antes da publicação estável, mas não substitui uma versão
  estável como referência de produção ou homologação.

## Uso de dependências

- Serviços e ferramentas executados em homologação ou produção devem depender
  exclusivamente de versões estáveis, explícitas e imutáveis de bibliotecas e
  artefatos internos.
- Dependências dinâmicas, intervalos de versão, `latest` e equivalentes são
  proibidos nesses ambientes.
- Dependências `-SNAPSHOT` são permitidas somente em desenvolvimento ou em
  integração coordenada e temporária, com a versão de origem registrada no
  plano ou na atividade correspondente.
- Uma dependência `-SNAPSHOT` não deve ser promovida para homologação ou
  produção.

## Compatibilidade e quebras

- A análise de quebra de uma nova versão deve comparar seu contrato com a
  última versão estável publicada do mesmo artefato.
- Alterações realizadas apenas dentro de uma versão `-SNAPSHOT` ainda não são
  quebra de contrato publicado, salvo se outro projeto tiver sido autorizado a
  consumi-la em integração coordenada.
- Remoção ou alteração incompatível de contrato público publicado exige novo
  número major. Inclusão compatível exige incremento minor; correção compatível
  exige incremento patch.
- A atividade que alterar contrato público deve registrar a versão estável de
  referência, a versão de trabalho e as quebras intencionais, quando houver.

## Publicação

- Uma versão estável só pode ser publicada a partir de commit identificado por
  tag correspondente à sua versão e após a suíte de validação definida pelo
  projeto ser aprovada.
- Antes da publicação estável, o projeto deve documentar mudanças de contrato,
  compatibilidade e instruções de atualização quando aplicáveis.
- Depois de publicada, uma versão estável deve permanecer disponível e não
  pode ser sobrescrita ou republicada com conteúdo diferente.

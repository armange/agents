# Regras Multiprojetos e Multilinguagens

## Versionamento e publicação

Antes de analisar, revisar, planejar ou modificar versão de projeto, dependência
entre projetos, publicação de artefato ou compatibilidade de contrato, leia
também:

- `AGENTS.projects.versioning.md`

Uma referência normativa a este arquivo ativa obrigatoriamente a norma de
versionamento. Suas regras materiais devem ser seguidas sempre que a atividade
tratar de versão, dependência entre projetos, publicação de artefato ou
compatibilidade de contrato.

## Regra Global de Aliases

- Aliases de projetos devem ser reconhecidos sem diferenciar maiúsculas de minúsculas.

## Identificação de projetos

- Registre o nome canônico, o tipo, a exposição, a finalidade e os aliases de
  cada projeto no contexto especializado correspondente.
- Use esses dados para distinguir responsabilidades e reconhecer referências
  do usuário; confirme a identidade do projeto antes de atuar nele.
- Catálogos de projetos reais devem ficar em um especialista próprio, adotado
  explicitamente pelas composições que precisem desse conhecimento.
- A adoção destas regras gerais não carrega automaticamente um catálogo.

Exemplo abstrato de identificação; os nomes abaixo não representam projetos reais:

| Nome | Tipo | Exposição | Finalidade | Aliases |
| --- | --- | --- | --- | --- |
| `service-a` | serviço | interno | implementar operações de um domínio | `api-a` |
| `library-b` | biblioteca | não aplicável | compartilhar funcionalidades entre aplicações | `lib-b` |

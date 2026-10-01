# HTTP

Este arquivo direciona as normas HTTP conforme o contrato envolvido no
trabalho.

## Endpoints

Antes de analisar, revisar, planejar ou modificar a criação, identidade ou
equivalência de endpoints HTTP, leia e aplique:

- `AGENTS.http.endpoint-uniqueness.md`

## Atualizações e campos de auditoria

Antes de analisar, revisar, planejar ou modificar contratos `PUT` ou `PATCH`,
incluindo o significado de campos ausentes, nulos ou coleções, leia e aplique:

- `AGENTS.http.update-semantics.md`

Antes de analisar, revisar, planejar ou modificar campos de auditoria em
requisições ou respostas HTTP, leia e aplique:

- `AGENTS.http.audit-fields.md`

## Erros, ausência e conflitos

Antes de analisar, revisar, planejar ou modificar contratos, endpoints ou
respostas HTTP que possam expor exceções ou erros, leia e aplique:

- `AGENTS.http.exception-responses.md`

Antes de analisar, revisar, planejar ou modificar consultas por identificador
ou filtro, comandos por identificador, integridade ou conflitos de dados ou
estado em HTTP, leia e aplique:

- `AGENTS.http.absence-and-conflict.md`

Uma referência normativa a este arquivo ativa os especialistas cujos critérios
acima forem atendidos, inclusive suas dependências normativas. Ao passar a
trabalhar em outro tipo de contrato ou resposta, reavalie esses critérios.

## Composição local

- Para aplicar um subconjunto fixo que este roteamento não delimite, o
  `AGENTS.md` local deve citar diretamente os especialistas necessários.
- Para usar este roteamento por atividade, o `AGENTS.md` local deve declarar
  uma referência normativa a este arquivo.
- Este arquivo não deve receber novas regras HTTP diretamente; novas regras devem ser criadas ou movidas para um arquivo especialista.

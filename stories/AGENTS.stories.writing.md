# Escrita de Histórias de Desenvolvimento

## Objetivo e escopo

Esta norma define a criação e revisão de histórias de desenvolvimento.

A norma se aplica somente onde histórias são produzidas ou mantidas, mediante referência normativa em um `AGENTS.md` aplicável à criação ou revisão dessas histórias. Não deve ser distribuída automaticamente aos projetos de código. Se as histórias forem mantidas fora desses projetos, a composição deve estar no local em que elas são mantidas.

As histórias devem ser escritas de forma clara, verificável e suficientemente precisa para orientar desenvolvedores humanos ou agentes de IA, sem impor detalhes de implementação que não sejam realmente necessários.

A história deve funcionar como um pequeno contrato de implementação.

---

## Princípios gerais

1. Descrever o problema e o resultado esperado antes de descrever qualquer solução técnica.
2. Separar claramente objetivo, requisitos, regras de negócio, critérios de aceitação e restrições.
3. Evitar ambiguidades.
4. Evitar detalhes técnicos desnecessários.
5. Tornar todo comportamento relevante verificável.
6. Declarar explicitamente o que está fora do escopo quando houver risco de interpretação incorreta.
7. Não usar requisitos implícitos quando eles puderem ser escritos explicitamente.
8. Não misturar decisões arquiteturais permanentes com detalhes locais de implementação.
9. Sempre que houver uma restrição obrigatória de arquitetura, segurança, compatibilidade ou tecnologia, registrá-la explicitamente.
10. Uma história deve permitir que outra pessoa determine objetivamente se ela foi concluída ou não.

---

# Estrutura obrigatória

Cada história deve seguir a estrutura abaixo.

```md
# [Título da história]

## Objetivo

[Descrever objetivamente o que deve ser alcançado e por quê.]

## Contexto

[Informar somente o contexto necessário para compreender a necessidade.]

## Requisitos

- O sistema deve...
- O sistema deve...
- Quando X ocorrer, deve...
- Caso Y aconteça, deve...

## Regras de negócio

- Regra 1.
- Regra 2.
- Regra 3.

## Critérios de aceitação

### Cenário 1 — [descrição]

Dado que ...
Quando ...
Então ...

### Cenário 2 — [descrição]

Dado que ...
Quando ...
Então ...

## Restrições

- Não alterar ...
- Deve utilizar ...
- Deve permanecer compatível com ...
- Não deve introduzir ...

## Fora do escopo

- ...
- ...

## Critérios de conclusão

A história será considerada concluída quando:

- todos os critérios de aceitação forem atendidos;
- os testes necessários estiverem implementados;
- não houver regressões conhecidas relacionadas à alteração;
- a documentação afetada estiver atualizada.
```

---

# 1. Título

O título deve identificar de forma curta e objetiva o resultado esperado.

## Bom exemplo

```text
Permitir consulta de usuários por identificador
```

## Exemplo inadequado

```text
Alterações no UserService
```

O segundo exemplo descreve um local de implementação, mas não informa claramente qual comportamento deve ser entregue.

---

# 2. Objetivo

O objetivo explica o resultado pretendido.

Deve responder, de forma simples:

- o que precisa ser alcançado;
- por que isso é necessário.

Não deve conter detalhes desnecessários de implementação.

## Bom exemplo

```md
## Objetivo

Permitir que um usuário seja localizado por seu identificador único para que outros fluxos do sistema possam recuperar seus dados de forma determinística.
```

## Exemplo inadequado

```md
## Objetivo

Criar um método `findById` no `UserService` usando um `HashMap`.
```

Esse texto já determina uma implementação específica sem demonstrar que ela seja uma necessidade real.

---

# 3. Contexto

O contexto deve conter somente as informações necessárias para compreender a história.

Não deve repetir documentação arquitetural, regras globais ou informações já mantidas em outros documentos permanentes.

## Bom exemplo

```md
## Contexto

Atualmente os usuários podem ser listados, mas não existe uma operação pública para recuperar um único usuário pelo identificador.
```

## Evitar

- histórico extenso do projeto;
- decisões não relacionadas diretamente à história;
- explicações já disponíveis em ADRs, AGENTS ou documentação técnica;
- justificativas especulativas.

---

# 4. Requisitos

Os requisitos descrevem o comportamento que obrigatoriamente deve existir.

Devem ser:

- objetivos;
- verificáveis;
- independentes entre si sempre que possível;
- escritos em linguagem imperativa.

Preferir frases como:

```text
O sistema deve...
A operação deve...
Quando X ocorrer...
Caso Y aconteça...
```

## Bom exemplo

```md
## Requisitos

- O sistema deve permitir consultar um usuário pelo identificador.
- A operação deve retornar os dados do usuário quando ele existir.
- A operação deve informar que o usuário não foi encontrado quando o identificador não existir.
- Identificadores nulos não devem ser aceitos.
```

## Exemplo inadequado

```md
## Requisitos

- Criar um método legal para procurar usuários.
- Tratar os erros corretamente.
- Fazer da melhor forma possível.
```

Termos como "corretamente", "adequadamente", "melhor", "rápido" ou "seguro" não são suficientes sem critérios objetivos.

---

# 5. Regras de negócio

As regras de negócio descrevem comportamentos do domínio.

Elas não devem ser confundidas com detalhes técnicos.

## Bom exemplo

```md
## Regras de negócio

- Um identificador de usuário corresponde a, no máximo, um usuário.
- Usuários inativos continuam localizáveis pela consulta por identificador.
- Usuários removidos logicamente não devem ser retornados.
```

## Exemplo técnico que não pertence a regras de negócio

```text
Usar Optional no retorno do repository.
```

Isso é uma decisão de implementação e somente deve aparecer se houver uma restrição técnica explícita que a torne obrigatória.

---

# 6. Critérios de aceitação

Os critérios de aceitação definem como comprovar que o comportamento esperado foi implementado.

Devem cobrir:

- fluxo principal;
- casos alternativos relevantes;
- erros previsíveis;
- limites relevantes da história.

Sempre que possível, utilizar o formato:

```text
Dado que ...
Quando ...
Então ...
```

## Exemplo

```md
## Critérios de aceitação

### Cenário 1 — Usuário existente

Dado que existe um usuário com identificador `123`
Quando a consulta pelo identificador `123` for executada
Então os dados desse usuário devem ser retornados

### Cenário 2 — Usuário inexistente

Dado que não existe usuário com identificador `999`
Quando a consulta pelo identificador `999` for executada
Então o sistema deve informar que o usuário não foi encontrado

### Cenário 3 — Identificador inválido

Dado que nenhum identificador válido foi informado
Quando a consulta for executada
Então a operação deve ser rejeitada
```

---

# 7. Restrições

Restrições devem ser usadas somente quando algo realmente precisa limitar a implementação.

Exemplos válidos:

- arquitetura obrigatória;
- contrato público existente;
- compatibilidade;
- segurança;
- tecnologia obrigatória;
- dependência que não pode ser adicionada;
- componentes que não podem ser modificados.

## Bom exemplo

```md
## Restrições

- A implementação deve utilizar a porta `UserRepository` existente.
- O domínio não pode depender de Spring.
- O contrato público atual não pode sofrer alteração incompatível.
- Nenhuma nova dependência externa deve ser adicionada.
```

## Exemplo inadequado

```md
## Restrições

- Criar uma classe `UserFinder`.
- Usar `HashMap`.
- Criar exatamente três métodos privados.
```

Essas decisões devem permanecer a cargo da implementação, salvo quando existir uma razão arquitetural explícita.

---

# 8. Fora do escopo

Esta seção deve impedir que a história seja ampliada indevidamente.

Deve ser usada quando existirem funcionalidades próximas que possam ser confundidas com o objetivo atual.

## Exemplo

```md
## Fora do escopo

- Pesquisa de usuários por nome.
- Paginação.
- Alteração dos dados do usuário.
- Criação de novos usuários.
```

O fato de algo estar fora do escopo não significa que esteja proibido permanentemente. Significa apenas que não faz parte da entrega desta história.

---

# 9. Critérios de conclusão

Os critérios de conclusão representam condições gerais para considerar a história terminada.

Eles não substituem os critérios de aceitação.

## Padrão recomendado

```md
## Critérios de conclusão

A história será considerada concluída quando:

- todos os critérios de aceitação forem atendidos;
- os testes necessários estiverem implementados;
- todos os testes relacionados estiverem passando;
- não houver regressões conhecidas relacionadas à alteração;
- a documentação afetada estiver atualizada;
- as restrições definidas nesta história forem respeitadas.
```

Critérios adicionais podem ser incluídos quando necessário.

---

# Separação obrigatória de conceitos

Toda história deve preservar a seguinte distinção:

| Seção | Pergunta respondida |
|---|---|
| Objetivo | O que queremos alcançar e por quê? |
| Contexto | O que preciso saber para entender a necessidade? |
| Requisitos | O que obrigatoriamente deve existir? |
| Regras de negócio | Como o domínio deve se comportar? |
| Critérios de aceitação | Como comprovamos o comportamento? |
| Restrições | O que limita a implementação? |
| Fora do escopo | O que não deve ser incluído nesta entrega? |
| Critérios de conclusão | Quando o trabalho pode ser considerado terminado? |

Não repetir a mesma informação em várias seções sem necessidade.

---

# Detalhes técnicos

Detalhes técnicos devem ser evitados quando representam apenas uma possível forma de implementação.

## Evitar

```text
Criar uma classe UserService usando HashMap e implementar um método findById.
```

## Preferir

```text
O sistema deve permitir consultar um usuário pelo identificador.
```

Detalhes técnicos devem aparecer quando forem requisitos reais.

## Exemplo válido

```md
## Restrições

- A funcionalidade deve utilizar a porta `UserRepository` existente.
- O módulo de domínio não pode depender de Spring.
```

A regra é:

> Especificar o comportamento necessário e restringir apenas aquilo que realmente não pode ser decidido pelo implementador.

---

# Referências arquiteturais

Quando uma história depender de uma regra já documentada, deve referenciá-la em vez de reescrevê-la.

## Exemplo

```text
## Restrições

- A implementação deve respeitar as regras definidas em `AGENTS.architecture.md`.
- A decisão registrada em `ADR-012` permanece válida.
```

Não copiar ADRs inteiros para dentro de histórias.

---

# Ambiguidade

Uma história não deve depender de interpretações subjetivas.

## Evitar

```text
A consulta deve ser rápida.
```

## Preferir

Quando houver um requisito real de desempenho:

```text
A consulta deve apresentar tempo de resposta inferior a 200 ms no cenário de referência definido pelo projeto.
```

## Evitar

```text
O erro deve ser amigável.
```

## Preferir

```text
Quando o usuário não existir, a operação deve retornar o código de erro `USER_NOT_FOUND`.
```

---

# Requisitos negativos

Comportamentos proibidos devem ser declarados explicitamente quando relevantes.

## Exemplo

```md
## Requisitos

- A consulta não deve criar, alterar ou remover usuários.
- A operação não deve retornar usuários removidos logicamente.
```

---

# Dependências entre histórias

Se uma história depender de outra entrega, registrar a dependência explicitamente.

## Exemplo

```md
## Dependências

- Requer a conclusão da história `USER-012 — Persistir usuários`.
```

Não duplicar na nova história os requisitos que pertencem à história dependente.

---

# Histórias pequenas

Uma história deve representar uma unidade de trabalho com objetivo claro.

Se uma história contiver vários objetivos independentes, deve ser dividida.

## Exemplo inadequado

```text
Criar usuário, consultar usuário, editar usuário, excluir usuário e implementar auditoria.
```

## Divisão recomendada

```text
Criar usuário
Consultar usuário por identificador
Editar dados do usuário
Remover usuário
Registrar auditoria das alterações de usuário
```

---

# Exemplo completo

```md
# Consultar usuário por identificador

## Objetivo

Permitir que outros fluxos do sistema recuperem um usuário específico por seu identificador único.

## Contexto

Atualmente existe suporte para persistência e listagem de usuários, mas não existe uma operação pública para recuperar individualmente um usuário pelo identificador.

## Requisitos

- O sistema deve permitir consultar um usuário pelo identificador.
- A operação deve retornar o usuário correspondente quando ele existir.
- A operação deve informar quando nenhum usuário corresponder ao identificador informado.
- Identificadores nulos não devem ser aceitos.
- A consulta não deve modificar o usuário.

## Regras de negócio

- Um identificador corresponde a, no máximo, um usuário.
- Usuários removidos logicamente não devem ser retornados.

## Critérios de aceitação

### Cenário 1 — Usuário existente

Dado que existe um usuário com identificador `123`
Quando for realizada uma consulta pelo identificador `123`
Então os dados do usuário devem ser retornados

### Cenário 2 — Usuário inexistente

Dado que não existe usuário com identificador `999`
Quando for realizada uma consulta pelo identificador `999`
Então o sistema deve informar que o usuário não foi encontrado

### Cenário 3 — Identificador nulo

Dado que nenhum identificador foi informado
Quando a consulta for executada
Então a operação deve ser rejeitada

### Cenário 4 — Usuário removido logicamente

Dado que existe um usuário com identificador `456`
E esse usuário está removido logicamente
Quando for realizada uma consulta pelo identificador `456`
Então o sistema deve tratá-lo como não encontrado

## Restrições

- A implementação deve utilizar a porta `UserRepository` existente.
- O domínio não pode depender de Spring.
- Nenhuma nova dependência externa deve ser adicionada.
- O contrato público existente não deve sofrer alteração incompatível.

## Fora do escopo

- Pesquisa por nome.
- Pesquisa por e-mail.
- Paginação.
- Alteração de usuário.
- Criação de usuário.

## Critérios de conclusão

A história será considerada concluída quando:

- todos os critérios de aceitação forem atendidos;
- os testes necessários estiverem implementados;
- todos os testes relacionados estiverem passando;
- não houver regressões conhecidas relacionadas à alteração;
- a documentação afetada estiver atualizada;
- todas as restrições desta história forem respeitadas.
```

---

# Checklist para criação de uma história

Antes de considerar uma história pronta para desenvolvimento, verificar:

- O título descreve claramente o resultado esperado?
- O objetivo explica o que deve ser alcançado?
- O contexto contém somente informação necessária?
- Todos os comportamentos obrigatórios estão descritos?
- As regras de negócio estão separadas dos detalhes técnicos?
- Os critérios de aceitação são verificáveis?
- Os principais fluxos de erro foram considerados?
- As restrições realmente precisam limitar a implementação?
- Há detalhes técnicos desnecessários?
- O que não faz parte da entrega está claro?
- Existe alguma expressão subjetiva ou ambígua?
- A história possui mais de um objetivo independente?
- Uma pessoa que não participou da discussão conseguiria entender o que deve ser entregue?
- É possível determinar objetivamente se a história foi concluída?

Se qualquer uma dessas respostas for negativa, a história deve ser revisada antes de seguir para implementação.

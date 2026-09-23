# Arquitetura Multi-module: Fronteiras

- Esta norma adapta a arquitetura em camadas para projetos em que a separação de responsabilidades ocorre por módulos de build, e não apenas por packages.
- Em projetos multi-module, o módulo é a primeira fronteira arquitetural.
- O package continua relevante, mas não substitui a fronteira de dependência declarada no build.
- Cada módulo deve ter uma responsabilidade arquitetural clara.
- Um módulo não deve existir apenas para refletir um package se isso não criar uma fronteira útil de dependência, publicação, teste ou reutilização.
- A direção das dependências entre módulos deve preservar a direção das camadas.
- O domínio deve continuar independente de frameworks, protocolos, banco de dados, mensageria, HTTP, JPA, Spring e implementações concretas.
- Implementações de infraestrutura devem depender dos contratos do domínio, nunca o contrário.
- O módulo que monta a aplicação pode depender de múltiplos módulos concretos, mas essa permissão é exclusiva de composição e não deve ser usada como precedente para os demais módulos.
- Toda dependência entre módulos deve representar uma colaboração real e justificável.
- Dependências cíclicas entre módulos são proibidas.
- A fronteira arquitetural principal é o módulo Gradle.
- Packages internos devem continuar expressando camada, domínio, contexto e responsabilidade local.
- Quando houver conflito entre a responsabilidade declarada do módulo e o package de uma classe, a responsabilidade do módulo prevalece.
- Uma classe em package `domain` dentro de um módulo de aplicação continua sendo suspeita, porque o módulo de aplicação não é o dono natural do domínio.
- Uma classe em package `application` dentro de um módulo de domínio continua sendo inválida, porque o domínio não deve conter entrada HTTP, CLI, mensageria ou composição de framework.

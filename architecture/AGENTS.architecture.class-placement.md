# Arquitetura: localização de classes

## Arquitetura do projeto

Antes de aplicar esta norma, leia e aplique as instruções arquiteturais do
projeto consumidor, identificadas nos `AGENTS.md` aplicáveis e em suas
referências normativas. Use as responsabilidades e os limites de dependência
ali definidos; esta norma não exige a topologia específica deste catálogo
nem autoriza ampliar as permissões da arquitetura adotada.

## Camada e package

- Cada classe deve ser armazenada na camada e no package compatíveis com sua
  responsabilidade e suas dependências.
- A localização de uma classe não deve ser escolhida apenas por conveniência
  técnica, proximidade com o chamador ou para evitar a criação de uma classe
  especializada.
- Classes de uma mesma camada devem ser organizadas pelo contexto ou assunto
  coeso que representam, conforme as convenções arquiteturais já aplicáveis ao
  projeto.
- Quando uma classe assumir responsabilidade de outra camada ou assunto, a
  responsabilidade deve ser movida para a camada e o package adequados.

## Precedência

- Regras arquiteturais mais específicas para policies, services, adapters,
  repositories, bordas ou outros componentes prevalecem sobre esta norma geral.

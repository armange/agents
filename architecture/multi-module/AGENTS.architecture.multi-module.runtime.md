# Arquitetura Multi-module: Composição de Runtime

- O módulo de runtime é o único lugar onde dependências concretas de camadas diferentes podem se encontrar livremente para montagem da aplicação.
- Essa composição deve ocorrer por configuração, auto-configuração, injeção de dependência, factories ou mecanismo equivalente do framework.
- A existência da dependência no runtime não autoriza imports equivalentes em módulos de domínio ou entrada.
- O runtime deve ser fino: inicialização, configuração, wiring e propriedades.
- Se o runtime começar a acumular regra, adaptação de protocolo, query ou transformação de domínio, a responsabilidade deve ser movida para o módulo apropriado.
- Configurações de runtime devem ficar no módulo executável ou em módulos de auto-configuração claramente identificados.
- DTOs externos de HTTP, mensageria ou terceiros devem ficar no módulo que implementa o protocolo correspondente, salvo quando o contrato público do projeto exigir publicação explícita.

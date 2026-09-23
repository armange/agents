# Exceções: comportamento interno

## Escopo interno

- Exceções que não serão expostas fora do sistema não exigem i18n nem envelope
  de resposta.
- Não há classe-base ou formato adicional obrigatório para exceções internas;
  aplicam-se as convenções normais da linguagem e do framework utilizado.
- Exceções internas devem preservar causa e contexto suficientes quando uma
  tradução técnica for necessária para diagnóstico ou tratamento posterior.
- `Error` e seus derivados não devem ser capturados ou tratados como fluxo
  normal de execução.

# i18n: bundles e mensagens

- Bundles de mensagens devem usar nomes explícitos e específicos ao projeto, módulo ou bounded context.
- Evite nomes genéricos de alto risco de colisão entre dependências, como nomes compartilhados por bibliotecas diferentes.
- Quando um bundle local complementar ou sobrescrever um bundle de biblioteca, o fallback da biblioteca deve ser preservado.
- Se uma chave de mensagem for publicada para um idioma suportado, a mesma chave deve existir em todos os idiomas suportados pelo sistema naquele contexto.
- Não publique tradução parcial quando o recurso já estiver exposto como contrato operacional do módulo.
- O nome do bundle deve ser estável e refletir o módulo que o publica.

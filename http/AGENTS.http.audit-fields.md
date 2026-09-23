# HTTP: Campos de Auditoria

- Campos de auditoria são somente leitura do ponto de vista do cliente.
- O cliente não pode definir, sobrescrever ou alterar campos de auditoria em payloads de criação ou atualização.
- Campos de auditoria podem aparecer em respostas HTTP apenas como leitura.
- O preenchimento e a atualização desses campos devem ficar restritos à infraestrutura ou à regra de auditoria do sistema.
- Lista padrão de campos de auditoria: `_created_at`, `created_by`, `updated_at`, `updated_by`, `deleted_at`, `deleted_by`.

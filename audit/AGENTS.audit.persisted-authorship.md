# Auditoria: Autoria Persistida

- Escopo: modelos, entidades, migrations, seeds e processamentos técnicos que persistam autoria.
- Campos persistidos de autoria, como `created_by`, `updated_by` e equivalentes, devem ser modelados como `UUID`.
- Entidades Java devem representar esses campos com `java.util.UUID`.
- Quando `created_at` existir em uma tabela, `created_by` também deve existir e ser obrigatório.
- Quando `updated_at` existir em uma tabela, `updated_by` também deve existir e ser preenchido junto com `updated_at` em toda atualização.
- Seeds e processamentos técnicos devem usar UUID técnico fixo e conhecido para autoria.
- Auditoria persistida não deve usar texto livre, como `system`, nome, email ou outro identificador textual, para representar autoria.

# Codificação: Nomes de Contratos de Dados

- Contratos de dados internos ou de domínio não devem usar os sufixos `Request` ou `Response`, reservados a protocolos de transporte nas bordas.
- O nome do contrato deve refletir os dados transportados, a ação solicitada ou o resultado representado, e não o protocolo de transporte.
- Quando a distinção temporal ou de intenção for necessária, prefira verbo no infinitivo para entrada ou comando e verbo no particípio ou passado para saída ou resultado.
- Exemplos preferidos: `CreateCustomerDto`, `CustomerCreatedDto`, `ReplacePlanDto`, `PlanReplacedDto`.

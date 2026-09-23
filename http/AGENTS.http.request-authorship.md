# HTTP: Autoria da Requisição

- Escopo: serviços HTTP que adotem o padrão Nexus de autoria persistida por usuário da requisição.
- O valor de autoria da requisição deve ser obtido pelo header HTTP `X-User-ID`.
- A leitura de `X-User-ID` deve usar o suporte oferecido pela lib `request-foundation`.
- Esta norma regula somente a origem da autoria na requisição HTTP; ela não define a modelagem nem a persistência dessa autoria.

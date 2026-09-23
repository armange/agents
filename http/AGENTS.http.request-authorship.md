# HTTP: Autoria da Requisição

- Escopo: serviços HTTP que identifiquem o usuário responsável pela requisição
  para registrar autoria persistida.
- Obtenha a autoria pelo mecanismo de identidade definido no contrato do
  projeto. Quando a origem for um header HTTP, use o nome documentado nesse contrato.
- Reutilize o suporte de identidade já adotado pela aplicação para obter esse
  valor, sem duplicar a integração existente.
- Esta norma regula somente a origem da autoria na requisição HTTP; ela não define a modelagem nem a persistência dessa autoria.

# Testes: Execução e Fechamento

- Em implementações divididas em fases, fases intermediárias podem ser validadas com testes focados e testes estratégicos suficientes para cobrir o comportamento alterado e riscos próximos.
- Testes focados são os testes diretamente relacionados à mudança.
- Testes estratégicos são testes adicionais escolhidos pelo risco técnico da fase, como contrato HTTP, integração com banco, migration, arquitetura, segurança, regressão de fluxo adjacente ou integração entre camadas.
- A suíte completa de testes do projeto só é requisito quando houver alteração em código Java.
- Quando houver alteração em código Java, a suíte completa de testes do projeto deve ser executada na fase final da implementação, como certificação de integridade antes do fechamento.
- Quando não houver alteração em código Java, a suíte completa não é obrigatória; devem ser executados testes ou checks focados adequados ao artefato alterado.
- Quando a implementação não estiver dividida em fases, a fase final é o próprio fechamento da atividade.
- Havendo alteração em código Java, a suíte completa deve complementar os testes focados e estratégicos já executados.
- Se houver alteração em código Java e a suíte completa não puder ser executada na fase final, o fechamento deve registrar o motivo e listar os testes e checks executados.

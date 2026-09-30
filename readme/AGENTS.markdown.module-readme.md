# Markdown: README de Módulo

## Objetivo e escopo

- Esta norma se aplica à documentação de projetos organizados em módulos com responsabilidades próprias, independentemente da linguagem ou ferramenta de build.
- O README de módulo descreve sua responsabilidade atual; não substitui a documentação operacional geral do projeto nem impõe uma arquitetura de módulos.

## Conteúdo e localização

- Cada módulo com responsabilidade própria deve ter um `README.md` na raiz do módulo. Módulos puramente agregadores, sem comportamento ou contrato próprio a explicar, podem ser descritos somente no índice do projeto.
- Descreva, de forma objetiva e verificável, o objetivo do módulo, seus conceitos principais, o que ele oferece aos demais módulos ou consumidores e suas fronteiras de responsabilidade.
- Diferencie o papel do módulo dos papéis dos módulos com que ele se relaciona. Registre o estado implementado; planos e oportunidades futuras pertencem aos documentos apropriados.
- Mantenha o README do módulo isolado na raiz desse módulo. Para instruções operacionais extensas, use a organização temática do projeto e links, sem duplicar procedimentos nos READMEs dos módulos.

## Descoberta e navegação

- O README principal deve permitir localizar os READMEs dos módulos. Quando a relação dos módulos precisar de espaço próprio, use um índice temático, como `README.modules.md`, e ligue esse índice ao README principal.
- O índice deve apontar para o README de cada módulo documentado e resumir sua responsabilidade, sem reproduzir sua descrição completa.
- Cada README de módulo deve oferecer um link relativo de volta ao README principal antes do sumário; se não houver sumário, coloque-o antes da primeira seção de conteúdo.
- Ao acrescentar, remover ou renomear módulos, atualize a navegação e confira os links. A documentação não deve apresentar como ativo um módulo que não faça parte do projeto atual.

## Limites

- Não exija um sumário em um README de módulo curto; a norma geral de Markdown determina quando ele é necessário.
- Não crie README vazio ou repetido apenas para reproduzir a lista de módulos do projeto.

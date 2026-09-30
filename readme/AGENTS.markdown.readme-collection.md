# Markdown: Coleção de READMEs

## Objetivo e escopo

- Esta norma orienta a divisão da documentação operacional de um projeto entre o `README.md` principal e arquivos temáticos na raiz.
- Aplica-se quando a documentação já está distribuída, quando sua divisão está em avaliação ou quando a estrutura de uma coleção de READMEs é usada como referência para outro projeto.
- Complementa as regras gerais de Markdown sobre conteúdo atual, sumários, títulos e links internos; não exige dividir todo README.

## Divisão por assunto

- Divida a documentação quando assuntos distintos tornarem o `README.md` principal difícil de consultar ou manter. Cada arquivo derivado deve reunir um assunto coeso e ter finalidade identificável pelo título e pela descrição inicial.
- Não estabeleça número obrigatório de partes nem limite fixo de linhas. Um assunto longo pode permanecer em um único arquivo quando a divisão adicional prejudicar sua compreensão.
- O `README.md` principal deve continuar como ponto de entrada: apresente o projeto, ofereça acesso rápido aos arquivos derivados e mantenha nele os assuntos curtos ou transversais que não justifiquem arquivo próprio.
- Use `README.<assunto>.md` para os arquivos temáticos na raiz, com assunto curto, descritivo e coerente com o idioma da documentação. A existência de uma coleção não obriga renomear arquivos já publicados apenas para uniformizar nomes.
- Mantenha cada instrução detalhada em um lugar principal. Quando um assunto for necessário em outro arquivo, ofereça um resumo curto e um link para a fonte correspondente. Ao dividir conteúdo existente, reúna trechos duplicados antes de criar novos arquivos.

## Navegação e manutenção

- O `README.md` principal deve apontar para cada arquivo temático ativo por um link com texto que descreva o assunto.
- Cada arquivo temático deve oferecer um link relativo de volta ao `README.md` principal antes do sumário; se não houver sumário, coloque-o antes da primeira seção de conteúdo.
- Use links relativos entre arquivos do mesmo projeto. Ao criar, mover ou renomear um arquivo, revise os links de entrada e de saída e verifique se destinos e âncoras continuam válidos.
- A estrutura de sumário e o retorno ao sumário dentro de cada arquivo seguem a norma geral de Markdown; o retorno ao README principal é uma navegação adicional entre arquivos.
- Ao usar outro projeto como modelo estrutural, examine o README principal e os arquivos a que ele remete. Adapte a organização aos assuntos e responsabilidades do projeto de destino, sem presumir que os mesmos arquivos ou conteúdos sejam necessários.

## Limites

- Um README curto ou de assunto único pode permanecer em um único arquivo.
- A divisão não deve espalhar a mesma instrução operacional por múltiplos arquivos nem transformar o README principal em um índice sem descrição útil do projeto.

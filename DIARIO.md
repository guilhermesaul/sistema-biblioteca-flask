# Diario de Desenvolvimento - Sistema de Biblioteca

---

## Guilherme Saul dos Santos Saraiva

### Registro 1
- **Data:** 13/10/2026
- **O que foi feito:** Definicao do tema (Sistema de Biblioteca), entidades (Autor, Livro, Leitor) e relacionamentos (1:N entre Autor e Livro, N:N entre Leitor e Livro via Emprestimo).
- **Dificuldade encontrada:** Decidir quais campos cada entidade deveria ter para manter o projeto simples e funcional.
- **Como resolvi:** Discutimos em grupo e definimos os campos essenciais de cada entidade.
- **Proximo passo:** Criar a estrutura de pastas MVC e configurar o Flask.

### Registro 2
- **Data:** 17/10/2026
- **O que foi feito:** Criacao da estrutura MVC com pastas models, controllers, templates e static. Configuracao do app.py, database.py e requirements.txt.
- **Dificuldade encontrada:** Entender como o SQLAlchemy se integra com o Flask usando init_app.
- **Como resolvi:** Consultei a documentacao do Flask-SQLAlchemy e os slides da aula.
- **Proximo passo:** Criar o model Autor e as rotas CRUD.

### Registro 3
- **Data:** 21/10/2026
- **O que foi feito:** Implementacao do model Autor com SQLAlchemy, criacao do controller com CRUD completo (listar, cadastrar, editar, excluir) e templates HTML para gerenciar autores.
- **Dificuldade encontrada:** Fazer o relationship funcionar entre Autor e Livro com cascade.
- **Como resolvi:** Usei cascade='all, delete-orphan' no relationship para que ao excluir um autor, seus livros tambem sejam excluidos.
- **Proximo passo:** Implementar os templates com o relacionamento 1:N visivel.

### Registro 4
- **Data:** 24/10/2026
- **O que foi feito:** Criacao dos templates de autores (index, form, detalhes) mostrando o relacionamento 1:N. Na pagina de detalhes do autor, os livros vinculados aparecem listados.
- **Dificuldade encontrada:** Montar a tabela de livros dentro do template de detalhes do autor usando Jinja2.
- **Como resolvi:** Usei um for loop para iterar sobre autor.livros e mostrar cada livro em uma linha da tabela.
- **Proximo passo:** Aguardar a integracao dos livros pela Joana.

---

## Joao Victor Dantas e Souza

### Registro 1
- **Data:** 21/10/2026
- **O que foi feito:** Criacao do model Livro com chave estrangeira autor_id referenciando a tabela de autores. Inicio do controller de livros.
- **Dificuldade encontrada:** Definir corretamente o ForeignKey apontando para a tabela autores.
- **Como resolvi:** Consultei a documentacao do SQLAlchemy sobre ForeignKey e relationship.
- **Proximo passo:** Completar o CRUD de livros e criar os templates.

### Registro 2
- **Data:** 28/10/2026
- **O que foi feito:** Implementacao completa do controller livro_controller.py com CRUD (listar, cadastrar, editar, excluir, detalhes), criacao dos templates de livros com selecao dinamica de autores e integracao do relacionamento 1:N.
- **Dificuldade encontrada:** Fazer o dropdown de autores carregar dinamicamente na tela de criacao e edicao do livro mantendo o autor selecionado.
- **Como resolvi:** Passei a lista de autores na renderizacao do template e usei Jinja para comparar o autor_id atual com o autor do loop.
- **Proximo passo:** Apoiar a integracao do relacionamento N:N com os Leitores e Emprestimos.

---

## Lucas Eduardo da Silva

### Registro 1
- **Data:** 28/10/2026
- **O que foi feito:** Melhoria do template base.html com cabecalho, menu de navegacao responsivo e rodape. Adicionei a meta tag viewport e a referencia ao CSS.
- **Dificuldade encontrada:** Fazer o menu funcionar tanto em tela grande quanto em celular sem usar bibliotecas externas.
- **Como resolvi:** Usei uma funcao JavaScript simples para alternar a classe do menu e media queries no CSS para controlar a visibilidade.
- **Proximo passo:** Criar o arquivo CSS com a estilizacao completa.

### Registro 2
- **Data:** 28/10/2026
- **O que foi feito:** Criacao do style.css com estilizacao padronizada para cabecalho, tabelas, formularios, botoes, alertas e rodape. Apliquei cores consistentes e responsividade com media queries.
- **Dificuldade encontrada:** Padronizar o visual de botoes e tabelas em todas as paginas sem quebrar o layout existente.
- **Como resolvi:** Usei seletores genericos para table, button e input, garantindo que todas as paginas recebam o mesmo estilo.
- **Proximo passo:** Criar o seed.py para popular o banco.

### Registro 3
- **Data:** 28/10/2026
- **O que foi feito:** Criacao do seed.py com funcoes para limpar o banco e inserir dados de teste (5 autores e 10 livros com vinculos corretos).
- **Dificuldade encontrada:** Garantir que os IDs dos autores estejam disponiveis antes de vincular os livros.
- **Como resolvi:** Fiz o commit dos autores primeiro, depois usei autor.id para criar os livros vinculados.
- **Proximo passo:** Criar o README.md e o DIARIO.md.

### Registro 4
- **Data:** 28/10/2026
- **O que foi feito:** Elaboracao do README.md com descricao do projeto, integrantes, responsabilidades, instrucoes de instalacao e execucao, estrutura do projeto e declaracao de autoria. Elaboracao do DIARIO.md com os registros de desenvolvimento de todos os integrantes.
- **Dificuldade encontrada:** Organizar as informacoes do README seguindo todos os requisitos da especificacao do projeto.
- **Como resolvi:** Segui o checklist do documento de instrucoes do projeto ponto a ponto.
- **Proximo passo:** Aguardar a integracao das partes do Rafael (Leitor e Emprestimos) para atualizar o seed e a documentacao.

---

## Raissa Raquel da Silva Costa

### Registro 1
- **Data:** 24/10/2026
- **O que foi feito:** Definicao dos modelos de dados para Leitor e para a tabela intermediaria de Emprestimo, estabelecendo as chaves estrangeiras leitor_id e livro_id e mapeamento N:N.
- **Dificuldade encontrada:** Modelar a tabela intermediaria com atributos adicionais como data_emprestimo e status sem quebrar a consulta direta do relacionamento.
- **Como resolvi:** Criei o model Emprestimo mapeando a tabela intermediaria e relacionei com Leitor e Livro usando back_populates e secondary='emprestimos'.
- **Proximo passo:** Criar os controllers com as rotas de gerenciamento de Leitores e operacoes de Emprestimo.

### Registro 2
- **Data:** 28/10/2026
- **O que foi feito:** Criacao dos controllers leitor_controller.py (CRUD de Leitor) e emprestimo_controller.py com rotas para conceder emprestimo (criar vinculo N:N) e devolver livro (remover vinculo N:N).
- **Dificuldade encontrada:** Garantir que um leitor nao pegue o mesmo livro duplicado caso o emprestimo anterior ainda esteja ativo.
- **Como resolvi:** Adicionei uma verificacao antes do commit para checar se ja existia emprestimo ativo com a combinacao leitor_id e livro_id.
- **Proximo passo:** Criar as interfaces HTML com Jinja2 para Leitores e Emprestimos.

### Registro 3
- **Data:** 30/10/2026
- **O que foi feito:** Criacao dos templates de leitores (index, form, detalhes) e emprestimos (index, form e tela de consulta bidirecional de leitores por livro).
- **Dificuldade encontrada:** Implementar a navegacao bidirecional entre Leitores e Livros de forma clara para o usuario.
- **Como resolvi:** Na tela de detalhes do Leitor exibo todos os livros emprestados por ele, e na tela de Emprestimos adicionei consulta para dado um livro exibir todos os leitores que o pegaram.
- **Proximo passo:** Atualizar o seed.py com dados de leitores e emprestimos e realizar testes finais do fluxo completo.

### Registro 4
- **Data:** 31/10/2026
- **O que foi feito:** Atualizacao do seed.py com populacao automatica de leitores e emprestimos de exemplo, testes de criacao e remocao de vinculos na interface e revisao da documentacao.
- **Dificuldade encontrada:** Testar o cascade de exclusao para garantir integridade quando um leitor ou livro e excluido.
- **Como resolvi:** Configurei cascade='all, delete-orphan' nos relacionamentos e testei a exclusao pelo navegador, confirmando que os registros orfaos sao removidos.
- **Proximo passo:** Projeto finalizado com sucesso e pronto para apresentacao e defesa oral.

---

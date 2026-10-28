# Sistema de Biblioteca

Sistema web para gerenciamento de uma biblioteca, desenvolvido com Flask, arquitetura MVC e SQLAlchemy ORM.

## Tema

Sistema de Biblioteca — permite gerenciar autores, livros, leitores e emprestimos de livros.

## Integrantes do Grupo

| Integrante | Responsabilidade Principal |
|---|---|
| **Guilherme Saul dos Santos Saraiva** | Estrutura base do projeto e CRUD de Autor (Entidade 1 + Relacionamento 1:N) |
| **Joao Victor Dantas e Souza** | CRUD de Livro e integracao do relacionamento 1:N com Autor |
| **Lucas Eduardo da Silva** | Interface visual (CSS), layout base, seed de dados, README e DIARIO |
| **Raissa Raquel da Silva Costa** | CRUD de Leitor e relacionamento N:N (Emprestimos) |

## Descricao do Sistema

O sistema permite:
- Cadastrar, listar, editar e excluir **Autores**
- Cadastrar, listar, editar e excluir **Livros** vinculados a autores
- Cadastrar, listar, editar e excluir **Leitores** *(em desenvolvimento)*
- Registrar e gerenciar **Emprestimos** de livros para leitores *(em desenvolvimento)*

## Entidades

1. **Autor** — possui id, nome, nacionalidade e biografia
2. **Livro** — possui id, titulo, ano de publicacao, genero e vinculo com autor
3. **Leitor** — possui id, nome, email e telefone *(em desenvolvimento)*

## Relacionamentos

### Relacionamento 1:N (Um para Muitos)
Um **Autor** possui varios **Livros**. Cada livro pertence a exatamente um autor. Implementado com `ForeignKey` na tabela de livros apontando para a tabela de autores e `relationship()` no model Autor.

### Relacionamento N:N (Muitos para Muitos)
**Leitores** emprestam varios **Livros**, e um livro pode ser emprestado por varios leitores. Sera implementado com uma tabela intermediaria de Emprestimos. *(Em desenvolvimento pelo integrante responsavel)*

## Tecnologias Utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML / CSS
- Jinja2

## Como Executar

### 1. Clonar o repositorio
```bash
git clone https://github.com/guilhermesaul/sistema-biblioteca-flask.git
cd sistema-biblioteca-flask
```

### 2. Criar ambiente virtual (recomendado)
```bash
python -m venv venv
```
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Popular o banco de dados com dados de teste
```bash
python seed.py
```

### 5. Executar a aplicacao
```bash
python app.py
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estrutura do Projeto

```
sistema-biblioteca-flask/
    app.py                  # Configuracao e inicializacao do Flask
    database.py             # Instancia do SQLAlchemy
    seed.py                 # Populacao do banco com dados de teste
    requirements.txt        # Dependencias do projeto
    README.md               # Este arquivo
    DIARIO.md               # Diario de desenvolvimento
    models/
        __init__.py
        autor.py            # Model Autor (1:N com Livro)
        livro.py            # Model Livro (FK para Autor)
    controllers/
        __init__.py
        autor_controller.py # Rotas CRUD de Autor
    templates/
        base.html           # Layout base com menu e rodape
        autores/
            index.html      # Listagem de autores
            form.html       # Formulario de cadastro/edicao
            detalhes.html   # Detalhes do autor e livros (1:N)
    static/
        style.css           # Estilizacao das paginas
```

## Dificuldades Encontradas

- Configurar o ambiente Flask para funcionar corretamente com SQLAlchemy e o banco SQLite
- Organizar a estrutura MVC separando responsabilidades entre models, controllers e templates
- Garantir que o CSS fique responsivo e padronizado em todas as telas

## Declaracao de Autoria

> **Declaracao de autoria:**
> Declaro que desenvolvi este projeto compreendendo o codigo entregue e que sou capaz de explicar e modificar suas partes principais.
>
> **Uso de IA:**
> - [x] Nao utilizei IA generativa.

from app import create_app
from database import db
from models.autor import Autor
from models.livro import Livro
from models.leitor import Leitor
from models.emprestimo import Emprestimo
from datetime import date, timedelta

def limpar_banco():
    """Limpa todas as tabelas na ordem correta respeitando as chaves estrangeiras."""
    Emprestimo.query.delete()
    Livro.query.delete()
    Autor.query.delete()
    Leitor.query.delete()
    db.session.commit()
    print("Banco de dados limpo com sucesso.")

def popular_autores():
    autores_dados = [
        {
            "nome": "Machado de Assis",
            "nacionalidade": "Brasileira",
            "biografia": "Considerado um dos maiores escritores da literatura brasileira."
        },
        {
            "nome": "Clarice Lispector",
            "nacionalidade": "Brasileira",
            "biografia": "Escritora e jornalista reconhecida por sua prosa intimista."
        },
        {
            "nome": "Jorge Amado",
            "nacionalidade": "Brasileira",
            "biografia": "Romancista baiano, um dos escritores mais adaptados do Brasil."
        },
        {
            "nome": "Gabriel Garcia Marquez",
            "nacionalidade": "Colombiana",
            "biografia": "Ganhador do Nobel, famoso pelo realismo magico."
        },
        {
            "nome": "Jose Saramago",
            "nacionalidade": "Portuguesa",
            "biografia": "Escritor portugues, vencedor do Premio Nobel de Literatura."
        }
    ]

    lista_autores = []
    for dados in autores_dados:
        autor = Autor(
            nome=dados["nome"],
            nacionalidade=dados["nacionalidade"],
            biografia=dados["biografia"]
        )
        db.session.add(autor)
        lista_autores.append(autor)

    db.session.commit()
    print(f"{len(lista_autores)} autores inseridos.")
    return lista_autores

def popular_livros(autores):
    livros_dados = [
        {"titulo": "Dom Casmurro", "ano_publicacao": 1899, "genero": "Romance", "autor_idx": 0},
        {"titulo": "Memorias Postumas de Bras Cubas", "ano_publicacao": 1881, "genero": "Romance", "autor_idx": 0},
        {"titulo": "Quincas Borba", "ano_publicacao": 1891, "genero": "Romance", "autor_idx": 0},
        {"titulo": "A Hora da Estrela", "ano_publicacao": 1977, "genero": "Romance", "autor_idx": 1},
        {"titulo": "A Paixao Segundo G.H.", "ano_publicacao": 1964, "genero": "Romance", "autor_idx": 1},
        {"titulo": "Capitaes da Areia", "ano_publicacao": 1937, "genero": "Romance", "autor_idx": 2},
        {"titulo": "Gabriela, Cravo e Canela", "ano_publicacao": 1958, "genero": "Romance", "autor_idx": 2},
        {"titulo": "Cem Anos de Solidao", "ano_publicacao": 1967, "genero": "Realismo Magico", "autor_idx": 3},
        {"titulo": "O Amor nos Tempos do Colera", "ano_publicacao": 1985, "genero": "Romance", "autor_idx": 3},
        {"titulo": "Ensaio Sobre a Cegueira", "ano_publicacao": 1995, "genero": "Ficcao", "autor_idx": 4},
    ]

    lista_livros = []
    for dados in livros_dados:
        livro = Livro(
            titulo=dados["titulo"],
            ano_publicacao=dados["ano_publicacao"],
            genero=dados["genero"],
            autor_id=autores[dados["autor_idx"]].id
        )
        db.session.add(livro)
        lista_livros.append(livro)

    db.session.commit()
    print(f"{len(lista_livros)} livros inseridos.")
    return lista_livros

def popular_leitores():
    leitores_dados = [
        {"nome": "Ana Beatriz Silva", "email": "ana.silva@email.com", "telefone": "(84) 98888-1001"},
        {"nome": "Bruno Henrique Costa", "email": "bruno.costa@email.com", "telefone": "(84) 98888-1002"},
        {"nome": "Camila Vasconcelos", "email": "camila.vasconcelos@email.com", "telefone": "(84) 98888-1003"},
        {"nome": "Diego Fernandes", "email": "diego.fernandes@email.com", "telefone": "(84) 98888-1004"},
        {"nome": "Elena Moreira", "email": "elena.moreira@email.com", "telefone": "(84) 98888-1005"},
        {"nome": "Felipe Santiago", "email": "felipe.santiago@email.com", "telefone": "(84) 98888-1006"},
    ]

    lista_leitores = []
    for dados in leitores_dados:
        leitor = Leitor(
            nome=dados["nome"],
            email=dados["email"],
            telefone=dados["telefone"]
        )
        db.session.add(leitor)
        lista_leitores.append(leitor)

    db.session.commit()
    print(f"{len(lista_leitores)} leitores inseridos.")
    return lista_leitores

def popular_emprestimos(leitores, livros):
    """Insere empréstimos de teste para demonstrar o relacionamento N:N."""
    hoje = date.today()
    emprestimos_dados = [
        {"leitor_idx": 0, "livro_idx": 0, "dias_atras": 5}, # Ana pegou Dom Casmurro
        {"leitor_idx": 0, "livro_idx": 3, "dias_atras": 3}, # Ana pegou A Hora da Estrela
        {"leitor_idx": 1, "livro_idx": 0, "dias_atras": 12}, # Bruno pegou Dom Casmurro
        {"leitor_idx": 2, "livro_idx": 5, "dias_atras": 2}, # Camila pegou Capitães da Areia
        {"leitor_idx": 3, "livro_idx": 7, "dias_atras": 7}, # Diego pegou Cem Anos de Solidão
        {"leitor_idx": 4, "livro_idx": 9, "dias_atras": 1}, # Elena pegou Ensaio Sobre a Cegueira
    ]

    contador = 0
    for dados in emprestimos_dados:
        emp = Emprestimo(
            leitor_id=leitores[dados["leitor_idx"]].id,
            livro_id=livros[dados["livro_idx"]].id,
            data_emprestimo=hoje - timedelta(days=dados["dias_atras"]),
            status="Ativo"
        )
        db.session.add(emp)
        contador += 1

    db.session.commit()
    print(f"{contador} empréstimos inseridos.")

def executar_seed():
    print("=" * 50)
    print("Iniciando populacao do banco de dados...")
    print("=" * 50)

    limpar_banco()

    autores = popular_autores()
    livros = popular_livros(autores)
    leitores = popular_leitores()
    popular_emprestimos(leitores, livros)

    print("=" * 50)
    print("Banco de dados populado com sucesso!")
    print("=" * 50)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        executar_seed()

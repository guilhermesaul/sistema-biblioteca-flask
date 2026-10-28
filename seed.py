from app import create_app
from database import db
from models.autor import Autor
from models.livro import Livro

def limpar_banco():
    Livro.query.delete()
    Autor.query.delete()
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

    contador = 0
    for dados in livros_dados:
        livro = Livro(
            titulo=dados["titulo"],
            ano_publicacao=dados["ano_publicacao"],
            genero=dados["genero"],
            autor_id=autores[dados["autor_idx"]].id
        )
        db.session.add(livro)
        contador += 1

    db.session.commit()
    print(f"{contador} livros inseridos.")

def executar_seed():
    print("=" * 50)
    print("Iniciando populacao do banco de dados...")
    print("=" * 50)

    limpar_banco()

    autores = popular_autores()
    popular_livros(autores)

    print("=" * 50)
    print("Banco de dados populado com sucesso!")
    print("=" * 50)

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        executar_seed()

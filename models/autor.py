from database import db

class Autor(db.Model):
    """
    Model representando a entidade Autor.
    Implementado por: Guilhermina (Responsável pela Entidade Autor e Arquitetura Base).
    Possui relacionamento 1:N com a entidade Livro (um autor possui vários livros).
    """
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    nacionalidade = db.Column(db.String(80), nullable=True)
    biografia = db.Column(db.Text, nullable=True)

    # Relacionamento 1:N (Um Autor para N Livros)
    # A classe Livro será integrada pela Joana (backref 'autor' permite acessar livro.autor)
    livros = db.relationship('Livro', backref='autor', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Autor {self.nome}>'

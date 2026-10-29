from database import db

class Livro(db.Model):
    """
    Model representando a entidade Livro.
    Responsabilidade: Joana (Gestão do Livro & Integração do Relacionamento 1:N).
    Estrutura com relacionamento 1:N com Autor e N:N com Leitor (via Empréstimos).
    """
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=True)
    genero = db.Column(db.String(50), nullable=True)

    # Chave estrangeira para o relacionamento 1:N com Autor
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)

    # Relacionamento com Emprestimo e Leitor (Relacionamento N:N)
    emprestimos = db.relationship('Emprestimo', back_populates='livro', cascade='all, delete-orphan')
    leitores = db.relationship('Leitor', secondary='emprestimos', back_populates='livros', viewonly=True)

    def __repr__(self):
        return f'<Livro {self.titulo}>'

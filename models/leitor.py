from database import db

class Leitor(db.Model):
    """
    Model representando a entidade Leitor.
    Responsabilidade: Raissa (Gestão do Leitor & Relacionamento N:N - Empréstimos).
    Possui relacionamento N:N com Livro através da tabela intermediária Emprestimo.
    """
    __tablename__ = 'leitores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefone = db.Column(db.String(30), nullable=True)

    # Relacionamento 1:N com Emprestimo
    emprestimos = db.relationship('Emprestimo', back_populates='leitor', cascade='all, delete-orphan')

    # Relacionamento N:N com Livro (acesso direto aos livros emprestados)
    livros = db.relationship('Livro', secondary='emprestimos', back_populates='leitores', viewonly=True)

    def __repr__(self):
        return f'<Leitor {self.nome}>'

from database import db
from datetime import date

class Emprestimo(db.Model):
    """
    Model representando a tabela intermediária do relacionamento N:N entre Leitor e Livro.
    Responsabilidade: Raissa (Gestão do Leitor & Relacionamento N:N - Empréstimos).
    Armazena o vínculo de empréstimo entre um Leitor e um Livro.
    """
    __tablename__ = 'emprestimos'

    id = db.Column(db.Integer, primary_key=True)
    leitor_id = db.Column(db.Integer, db.ForeignKey('leitores.id'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livros.id'), nullable=False)
    data_emprestimo = db.Column(db.Date, nullable=False, default=date.today)
    data_devolucao = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='Ativo')

    # Relacionamentos
    leitor = db.relationship('Leitor', back_populates='emprestimos')
    livro = db.relationship('Livro', back_populates='emprestimos')

    def __repr__(self):
        return f'<Emprestimo Leitor:{self.leitor_id} Livro:{self.livro_id}>'

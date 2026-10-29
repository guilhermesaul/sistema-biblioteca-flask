from database import db
from models.autor import Autor
from models.livro import Livro
from models.leitor import Leitor
from models.emprestimo import Emprestimo

__all__ = ['db', 'Autor', 'Livro', 'Leitor', 'Emprestimo']

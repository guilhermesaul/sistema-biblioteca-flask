from flask import Flask, redirect, url_for
from database import db
import os

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados SQLite
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'biblioteca.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sistema-biblioteca-chave-secreta-2026'

    # Inicialização do banco de dados
    db.init_app(app)

    # Registro dos Blueprints (Controllers)
    from controllers.autor_controller import autor_bp
    app.register_blueprint(autor_bp, url_prefix='/autores')

    from controllers.livro_controller import livro_bp
    app.register_blueprint(livro_bp, url_prefix='/livros')

    from controllers.leitor_controller import leitor_bp
    app.register_blueprint(leitor_bp, url_prefix='/leitores')

    from controllers.emprestimo_controller import emprestimo_bp
    app.register_blueprint(emprestimo_bp, url_prefix='/emprestimos')

    @app.route('/')
    def index():
        return redirect(url_for('autores.listar_autores'))

    with app.app_context():
        # Importa os models para garantir que sejam registrados antes de criar as tabelas
        from models import autor, livro, leitor, emprestimo
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.livro import Livro
from models.autor import Autor

livro_bp = Blueprint('livros', __name__)

@livro_bp.route('/')
def listar_livros():
    """Lista todos os livros cadastrados no sistema com seus autores."""
    livros = Livro.query.order_by(Livro.titulo.asc()).all()
    return render_template('livros/index.html', livros=livros)

@livro_bp.route('/novo', methods=['GET', 'POST'])
def cadastrar_livro():
    """Formulário para cadastrar um novo livro vinculado a um autor."""
    autores = Autor.query.order_by(Autor.nome.asc()).all()
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        genero = request.form.get('genero', '').strip()
        ano_publicacao = request.form.get('ano_publicacao', '').strip()
        autor_id = request.form.get('autor_id', '').strip()

        if not titulo:
            flash('O título do livro é obrigatório.', 'danger')
            return render_template('livros/form.html', livro=None, autores=autores)

        if not autor_id:
            flash('Selecione um autor para o livro.', 'danger')
            return render_template('livros/form.html', livro=None, autores=autores)

        try:
            ano = int(ano_publicacao) if ano_publicacao else None
        except ValueError:
            flash('Ano de publicação inválido.', 'danger')
            return render_template('livros/form.html', livro=None, autores=autores)

        novo_livro = Livro(
            titulo=titulo,
            genero=genero if genero else None,
            ano_publicacao=ano,
            autor_id=int(autor_id)
        )

        try:
            db.session.add(novo_livro)
            db.session.commit()
            flash(f'Livro "{novo_livro.titulo}" cadastrado com sucesso!', 'success')
            return redirect(url_for('livros.listar_livros'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar livro: {str(e)}', 'danger')

    return render_template('livros/form.html', livro=None, autores=autores)

@livro_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_livro(id):
    """Edita as informações de um livro existente."""
    livro = Livro.query.get_or_404(id)
    autores = Autor.query.order_by(Autor.nome.asc()).all()

    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        genero = request.form.get('genero', '').strip()
        ano_publicacao = request.form.get('ano_publicacao', '').strip()
        autor_id = request.form.get('autor_id', '').strip()

        if not titulo:
            flash('O título do livro é obrigatório.', 'danger')
            return render_template('livros/form.html', livro=livro, autores=autores)

        if not autor_id:
            flash('Selecione um autor para o livro.', 'danger')
            return render_template('livros/form.html', livro=livro, autores=autores)

        try:
            ano = int(ano_publicacao) if ano_publicacao else None
        except ValueError:
            flash('Ano de publicação inválido.', 'danger')
            return render_template('livros/form.html', livro=livro, autores=autores)

        livro.titulo = titulo
        livro.genero = genero if genero else None
        livro.ano_publicacao = ano
        livro.autor_id = int(autor_id)

        try:
            db.session.commit()
            flash(f'Livro "{livro.titulo}" atualizado com sucesso!', 'success')
            return redirect(url_for('livros.detalhes_livro', id=livro.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar o livro: {str(e)}', 'danger')

    return render_template('livros/form.html', livro=livro, autores=autores)

@livro_bp.route('/<int:id>/excluir', methods=['POST'])
def excluir_livro(id):
    """Exclui um livro do sistema."""
    livro = Livro.query.get_or_404(id)
    titulo = livro.titulo
    try:
        db.session.delete(livro)
        db.session.commit()
        flash(f'Livro "{titulo}" excluído com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir o livro: {str(e)}', 'danger')

    return redirect(url_for('livros.listar_livros'))

@livro_bp.route('/<int:id>')
def detalhes_livro(id):
    """Exibe os detalhes de um livro e seu autor (relacionamento 1:N)."""
    livro = Livro.query.get_or_404(id)
    return render_template('livros/detalhes.html', livro=livro)

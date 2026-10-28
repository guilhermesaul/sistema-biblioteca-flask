from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.autor import Autor

autor_bp = Blueprint('autores', __name__)

@autor_bp.route('/')
def listar_autores():
    """Lista todos os autores cadastrados no sistema."""
    autores = Autor.query.order_by(Autor.nome.asc()).all()
    return render_template('autores/index.html', autores=autores)

@autor_bp.route('/novo', methods=['GET', 'POST'])
def cadastrar_autor():
    """Formulário para cadastrar um novo autor."""
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        nacionalidade = request.form.get('nacionalidade', '').strip()
        biografia = request.form.get('biografia', '').strip()

        if not nome:
            flash('O nome do autor é obrigatório.', 'danger')
            return render_template('autores/form.html', autor=None)

        novo_autor = Autor(
            nome=nome,
            nacionalidade=nacionalidade if nacionalidade else None,
            biografia=biografia if biografia else None
        )

        try:
            db.session.add(novo_autor)
            db.session.commit()
            flash(f'Autor "{novo_autor.nome}" cadastrado com sucesso!', 'success')
            return redirect(url_for('autores.listar_autores'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao salvar o autor: {str(e)}', 'danger')

    return render_template('autores/form.html', autor=None)

@autor_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_autor(id):
    """Edita as informações de um autor existente."""
    autor = Autor.query.get_or_404(id)

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        nacionalidade = request.form.get('nacionalidade', '').strip()
        biografia = request.form.get('biografia', '').strip()

        if not nome:
            flash('O nome do autor é obrigatório.', 'danger')
            return render_template('autores/form.html', autor=autor)

        autor.nome = nome
        autor.nacionalidade = nacionalidade if nacionalidade else None
        autor.biografia = biografia if biografia else None

        try:
            db.session.commit()
            flash(f'Autor "{autor.nome}" atualizado com sucesso!', 'success')
            return redirect(url_for('autores.detalhes_autor', id=autor.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar o autor: {str(e)}', 'danger')

    return render_template('autores/form.html', autor=autor)

@autor_bp.route('/<int:id>/excluir', methods=['POST'])
def excluir_autor(id):
    """Exclui um autor e seus livros vinculados."""
    autor = Autor.query.get_or_404(id)
    nome_autor = autor.nome
    try:
        db.session.delete(autor)
        db.session.commit()
        flash(f'Autor "{nome_autor}" excluído com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir o autor: {str(e)}', 'danger')

    return redirect(url_for('autores.listar_autores'))

@autor_bp.route('/<int:id>')
def detalhes_autor(id):
    """
    Exibe os detalhes de um autor específico e demonstra o relacionamento 1:N
    listando todos os livros associados a ele.
    """
    autor = Autor.query.get_or_404(id)
    return render_template('autores/detalhes.html', autor=autor)

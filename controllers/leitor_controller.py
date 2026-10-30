from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.leitor import Leitor
from models.livro import Livro

leitor_bp = Blueprint('leitores', __name__)

@leitor_bp.route('/')
def listar_leitores():
    """Lista todos os leitores cadastrados no sistema."""
    leitores = Leitor.query.order_by(Leitor.nome.asc()).all()
    return render_template('leitores/index.html', leitores=leitores)

@leitor_bp.route('/novo', methods=['GET', 'POST'])
def cadastrar_leitor():
    """Formulário para cadastrar um novo leitor."""
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        telefone = request.form.get('telefone', '').strip()

        if not nome:
            flash('O nome do leitor é obrigatório.', 'danger')
            return render_template('leitores/form.html', leitor=None)

        if not email:
            flash('O e-mail do leitor é obrigatório.', 'danger')
            return render_template('leitores/form.html', leitor=None)

        leitor_existente = Leitor.query.filter_by(email=email).first()
        if leitor_existente:
            flash('Já existe um leitor cadastrado com este e-mail.', 'warning')
            return render_template('leitores/form.html', leitor=None)

        novo_leitor = Leitor(
            nome=nome,
            email=email,
            telefone=telefone if telefone else None
        )

        try:
            db.session.add(novo_leitor)
            db.session.commit()
            flash(f'Leitor "{novo_leitor.nome}" cadastrado com sucesso!', 'success')
            return redirect(url_for('leitores.listar_leitores'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar leitor: {str(e)}', 'danger')

    return render_template('leitores/form.html', leitor=None)

@leitor_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_leitor(id):
    """Edita as informações de um leitor existente."""
    leitor = Leitor.query.get_or_404(id)

    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        telefone = request.form.get('telefone', '').strip()

        if not nome:
            flash('O nome do leitor é obrigatório.', 'danger')
            return render_template('leitores/form.html', leitor=leitor)

        if not email:
            flash('O e-mail do leitor é obrigatório.', 'danger')
            return render_template('leitores/form.html', leitor=leitor)

        outro_leitor = Leitor.query.filter(Leitor.email == email, Leitor.id != id).first()
        if outro_leitor:
            flash('Já existe outro leitor cadastrado com este e-mail.', 'warning')
            return render_template('leitores/form.html', leitor=leitor)

        leitor.nome = nome
        leitor.email = email
        leitor.telefone = telefone if telefone else None

        try:
            db.session.commit()
            flash(f'Leitor "{leitor.nome}" atualizado com sucesso!', 'success')
            return redirect(url_for('leitores.detalhes_leitor', id=leitor.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar o leitor: {str(e)}', 'danger')

    return render_template('leitores/form.html', leitor=leitor)

@leitor_bp.route('/<int:id>/excluir', methods=['POST'])
def excluir_leitor(id):
    """Exclui um leitor e seus registros de empréstimos vinculados."""
    leitor = Leitor.query.get_or_404(id)
    nome_leitor = leitor.nome
    try:
        db.session.delete(leitor)
        db.session.commit()
        flash(f'Leitor "{nome_leitor}" excluído com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir o leitor: {str(e)}', 'danger')

    return redirect(url_for('leitores.listar_leitores'))

@leitor_bp.route('/<int:id>')
def detalhes_leitor(id):
    """
    Exibe os detalhes de um leitor e demonstra o relacionamento N:N
    listando todos os livros que ele pegou emprestado.
    """
    leitor = Leitor.query.get_or_404(id)
    return render_template('leitores/detalhes.html', leitor=leitor)

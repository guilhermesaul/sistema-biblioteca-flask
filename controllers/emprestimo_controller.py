from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.emprestimo import Emprestimo
from models.leitor import Leitor
from models.livro import Livro
from datetime import date, datetime

emprestimo_bp = Blueprint('emprestimos', __name__)

@emprestimo_bp.route('/')
def listar_emprestimos():
    """
    Lista todos os empréstimos cadastrados (Relacionamento N:N).
    Também fornece acesso para consulta bidirecional (quem pegou qual livro).
    """
    emprestimos = Emprestimo.query.order_by(Emprestimo.data_emprestimo.desc()).all()
    livros = Livro.query.order_by(Livro.titulo.asc()).all()
    return render_template('emprestimos/index.html', emprestimos=emprestimos, livros=livros)

@emprestimo_bp.route('/novo', methods=['GET', 'POST'])
def cadastrar_emprestimo():
    """
    Cria um novo vínculo N:N entre Leitor e Livro (Concessão de Empréstimo).
    """
    leitores = Leitor.query.order_by(Leitor.nome.asc()).all()
    livros = Livro.query.order_by(Livro.titulo.asc()).all()

    # Leitor pré-selecionado se vier da tela de detalhes do leitor
    leitor_id_param = request.args.get('leitor_id', type=int)

    if request.method == 'POST':
        leitor_id = request.form.get('leitor_id')
        livro_id = request.form.get('livro_id')
        data_str = request.form.get('data_emprestimo', '').strip()

        if not leitor_id or not livro_id:
            flash('Selecione tanto o leitor quanto o livro para registrar o empréstimo.', 'danger')
            return render_template('emprestimos/form.html', leitores=leitores, livros=livros, leitor_id_selecionado=leitor_id_param)

        data_emprestimo = date.today()
        if data_str:
            try:
                data_emprestimo = datetime.strptime(data_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Data de empréstimo inválida.', 'danger')
                return render_template('emprestimos/form.html', leitores=leitores, livros=livros, leitor_id_selecionado=leitor_id_param)

        # Verifica se já existe esse vínculo ativo
        existente = Emprestimo.query.filter_by(
            leitor_id=int(leitor_id),
            livro_id=int(livro_id),
            status='Ativo'
        ).first()

        if existente:
            flash('Este leitor já possui um empréstimo ativo para este livro.', 'warning')
            return render_template('emprestimos/form.html', leitores=leitores, livros=livros, leitor_id_selecionado=leitor_id_param)

        novo_emprestimo = Emprestimo(
            leitor_id=int(leitor_id),
            livro_id=int(livro_id),
            data_emprestimo=data_emprestimo,
            status='Ativo'
        )

        try:
            db.session.add(novo_emprestimo)
            db.session.commit()
            flash('Empréstimo registrado com sucesso!', 'success')
            return redirect(url_for('emprestimos.listar_emprestimos'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao registrar empréstimo: {str(e)}', 'danger')

    return render_template('emprestimos/form.html', leitores=leitores, livros=livros, leitor_id_selecionado=leitor_id_param)

@emprestimo_bp.route('/<int:id>/devolver', methods=['POST'])
def devolver_emprestimo(id):
    """
    Remove o vínculo N:N entre Leitor e Livro (Devolução de Livro).
    Pode redirecionar de volta para a tela de origem (Leitor, Livro ou Lista de Empréstimos).
    """
    emprestimo = Emprestimo.query.get_or_404(id)
    titulo_livro = emprestimo.livro.titulo
    nome_leitor = emprestimo.leitor.nome
    origem = request.form.get('origem', 'emprestimos')

    try:
        db.session.delete(emprestimo)
        db.session.commit()
        flash(f'Livro "{titulo_livro}" devolvido pelo leitor "{nome_leitor}" com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao processar devolução: {str(e)}', 'danger')

    if origem == 'leitor':
        return redirect(url_for('leitores.detalhes_leitor', id=emprestimo.leitor_id))
    elif origem == 'livro':
        return redirect(url_for('livros.detalhes_livro', id=emprestimo.livro_id))
    return redirect(url_for('emprestimos.listar_emprestimos'))

@emprestimo_bp.route('/livro/<int:livro_id>')
def leitores_por_livro(livro_id):
    """
    Listagem bidirecional (Sentido 2 do N:N):
    Exibe todos os leitores que pegaram emprestado um determinado livro.
    """
    livro = Livro.query.get_or_404(livro_id)
    return render_template('emprestimos/livro_leitores.html', livro=livro)

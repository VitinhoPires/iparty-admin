from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
import os

bp = Blueprint('main', __name__)

# Usuário padrão para teste
USUARIO = {
    "email": "admin@iparty.com",
    "senha": "123456"
}

@bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == USUARIO['email'] and senha == USUARIO['senha']:
            session['user'] = email
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('login.html', erro='Usuário ou senha incorretos')
    return render_template('login.html')

@bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    return render_template('dashboard.html')

@bp.route('/logout')
def logout():
    session.clear()  # Remove todos os dados da sessão
    return redirect(url_for('main.login'))
 # Redireciona para a página de login

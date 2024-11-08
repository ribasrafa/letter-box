# Importando a biblioteca do Flask para fazer um site
import aqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "chave_segura"

#função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('meu_banco.db')
    conn.row_factory = sqlite3.Row
    #facilita acessar as colunas pelo nome
    return conn

# criar uma lista de usuarios e senha, depois vamos pegar no DB
usuarios = {
    'admin' : 'admin',
    'usuario' : 'senha',
    'rafaela' : '111111',
}

# Definindo a rota principal do site
@app.route('/')
def home ():
    return render_template('index.html')

# Definindo a rota login do site
@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/inicio')
def inicio ():
    return render_template('inicio.html')

@app.route('/perfil')
def perfil ():
    return render_template('perfil.html')

@app.route('/amigos')
def amigos ():
    return render_template('amigos.html')

@app.route('/assistidos')
def assistidos ():
    return render_template('assistidos.html')

@app.route('/postagens')
def postagens ():
    return render_template('postagens.html')

@app.route('/quero')
def quero ():
    return render_template('quero.html')

#Verificar o login
@app.route('/verificar-login', methods=['POST'])
def verificar_login():

#Pegando o que o usuario digitou no campo de entrada de user e senha
    username = request.form['usuario']
    password = request.form['senha']

    #Verificar se o usuario digitado está na lista e se a senha está certa
    if username in usuarios and usuarios[username] == password:
        return redirect(url_for("inicio"))
    else:
        flash('Usuário ou senha inválidos.', 'danger')
        return redirect(url_for('login'))

# Parte principal do programa em Python
if __name__ == '__main__':
    app.run(debug=True)

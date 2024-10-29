# Importando a biblioteca do Flask para fazer um site
from flask import Flask, render_template, request
app = Flask(__name__)

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

# Definindo a rota principal do site
@app.route('/login')
def login ():
    return render_template('login.html')

#Verificar o login
@app.route('/verificar-login', methos=['POST'])
def verificar_login():

#Pegando o que o usuario digitou no campo de entrada de user e senha
    username = request.form['username']
    password = request.form['password']

#Verificar se o usuario digitado está na lista e se a senha está certa
if username in usuarios and usuarios[username] == password:
    return f"Bem-vindo, {username}!"
else:
    return "Usuário ou senha inválidos."

# Parte principal do programa em Python
if __name__ == '__main__':
    app.run(debug=True)

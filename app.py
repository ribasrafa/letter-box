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

# Parte principal do programa em Python
if __name__ == '__main__':
    app.run(debug=True)

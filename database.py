import sqlite3

#Função que conecta banco de dados
def conectar_banco ():
    #Conectar ao banco ou criar se não existir
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
(id INTEGER PRIMARY KEY, usuario TEXT, senha TEXT, email TEXT)''')

#Confirma as alterações
    conexao.commit()
    
#Parte principal do programa
if __name__== '__main__':
    conectar_banco()

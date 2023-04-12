from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Olá Sejam Bem Vindo ao MBA Arquitetura de Soluções da FIAP - Grupo 18"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Bem Vindo ao MBA Arquitetura de Soluções da FIAP - Grupo 18"

if __name__ == '__main__':
    app.run()
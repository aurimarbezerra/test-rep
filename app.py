from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "FIAP MBA Arquitetura de Soluções Grupo 18"

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Gestão de Biblioteca"

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"

@app.route("/cadastro-livro")
def cadastro_livro():
    return {"mensagem": API funcionando}



if __name__ == "__main__":
    app.run(debug=True)
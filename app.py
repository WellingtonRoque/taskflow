from flask import Flask
import os

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
    return "Livros cadastrados"

@app.route("/status")
def status():
    return {"status": "ok"}

"""
if __name__ == "__main__":
    app.run(debug=True)
"""
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
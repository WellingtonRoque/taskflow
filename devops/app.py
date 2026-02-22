from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "API funcionando"}

@app.route("/status")
def status():
    return {"status": "API online"}

@app.route("/teste")
def teste():
    return {"status": "API teste"}



if __name__ == "__main__":
    app.run(debug=True)
# Criar arquivo app.py
with open("app.py", "w") as f:
    f.write("""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API CI/CD funcionando!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
""")

# Criar requirements.txt
with open("requirements.txt", "w") as f:
    f.write("Flask==3.0.0")
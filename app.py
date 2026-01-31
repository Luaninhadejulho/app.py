from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/alunos")
def lista_alunos():
    return jsonify([
        {"id": 1, "nome": "Luana"},
        {"id": 2, "nome": "Carlos"}
    ])

if __name__ == "__main__":
    app.run(debug=True)

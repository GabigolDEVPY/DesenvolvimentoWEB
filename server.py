from flask import Flask, jsonify
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

@app.route("/dados", methods=["GET"])
def retornarDados():
    return jsonify([{"id": 32, "nome": "Gabriel", "mensagem": "nãooo"}])



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def retornarDados():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def EnviarDados():
    dados = request.form.to_dict()
    print(dados)
    return render_template("usuarios.html", user=dados)


if __name__ == "__main__":
    app.run(debug=True)
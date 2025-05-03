from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, template_folder='../templates')

produtos = [
    {"id": 1, "nome": "Fone Bluetooth Rosa", "preco": 129.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 2, "nome": "Caixinha JBL", "preco": 299.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 3, "nome": "Teclado Mecânico RGB", "preco": 189.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 4, "nome": "Mouse Gamer com LED", "preco": 99.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 5, "nome": "Monitor 24'' Full HD", "preco": 849.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 6, "nome": "Notebook i5 8GB RAM", "preco": 2999.00, "imagem": "https://via.placeholder.com/150"},
    {"id": 7, "nome": "Cadeira Gamer Rosa", "preco": 999.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 8, "nome": "Suporte de Celular", "preco": 24.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 9, "nome": "Webcam Full HD", "preco": 179.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 10, "nome": "Headset com Microfone", "preco": 159.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 11, "nome": "Hub USB 4 portas", "preco": 49.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 12, "nome": "Controle Bluetooth", "preco": 89.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 13, "nome": "Echo Dot Alexa", "preco": 279.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 14, "nome": "Smartwatch Rosa", "preco": 199.90, "imagem": "https://via.placeholder.com/150"},
    {"id": 15, "nome": "Capinha de Celular Personalizada", "preco": 39.90, "imagem": "https://via.placeholder.com/150"},
]


@home_bp.route("/home", methods=["POST"])
def enviar_dados():
    return render_template("usuarios.html", produtos=produtos)
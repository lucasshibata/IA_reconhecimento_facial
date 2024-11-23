from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Middleware para registrar informações da requisição
@app.before_request
def log_request():
    print(f"[{datetime.datetime.now()}] {request.method} {request.path}")

# Middleware para modificar respostas
@app.after_request
def modify_response(response):
    response.headers["X-Custom-Header"] = "MiddlewareDemo"
    return response

# Rotas simples para teste
@app.route("/")
def home():
    return jsonify({"message": "Bem-vindo à API com Middleware!"})

@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Olá, {name}!"})

@app.route("/error")
def trigger_error():
    return jsonify({"error": "Simulação de erro!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
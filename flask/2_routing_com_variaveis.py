from flask import Flask 

app = Flask(__name__)


"""as regras de definicao da rota sao baseadas no modulo Werkzeug's
"/index/" poderia ser acessado como "localhost:5000/index" ou "localhost:5000/index/
mas  se definido como "/index" so poderia ser acessado como tal, 
se não daria erro 404 not found
"""
@app.route("/saudacao/<nome>/<int:idade>", methods = ["GET"])
def saudacao(nome, idade):
    return f"Olá {nome}, que belo nome, vi que você tem {idade} anos"

app.run(debug= True)
@app.route("/admin/")
def saudar_admin():
    return "Olá administrador, seja bem vindo"